#!/usr/bin/env python3
"""
muslin_loop.py — automated muslin test harness for the Axiom Sheets module.

Runs a multi-turn scene between two roles played by a local LLM, carrying the
transcript forward each turn, and referees a Stress/Grief track on an axiom.
Tests the whole arc: Stress accumulates -> Grief track fills -> Grieve triggers.

This is the transcript-carried simulation: not two persistent agents, but one
model re-instantiated per role per turn from the running transcript, with a
referee pass scoring the sheet. The human (or a stronger model) should read
the output transcript and judge Holds / Pulls / Tears.

Local model: Qwen2.5-7B at http://127.0.0.1:5052/generate (custom endpoint).
"""

import json
import sys
import time
import urllib.request
from pathlib import Path

ENDPOINT = "http://127.0.0.1:5052/generate"
OUT = Path(__file__).parent / "muslin_loop_transcript.md"


def gen(prompt, max_tokens=400, retries=2):
    """Call the local Qwen endpoint. Returns the response string."""
    body = json.dumps({"prompt": prompt, "max_new_tokens": max_tokens}).encode()
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(
                ENDPOINT, data=body,
                headers={"Content-Type": "application/json"}, method="POST",
            )
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read())["response"].strip()
        except Exception as e:
            if attempt == retries:
                return f"[GEN ERROR after {retries+1} tries: {e}]"
            time.sleep(3)
        # the local model can stall; 90s timeout + retries keeps the loop
        # from hanging indefinitely on a single contended call.


# --- the axiom sheet under test -------------------------------------------
AXIOM = "Using a powerful new tool openly is always better than holding back."
BUILT_UPON = "Theo's whole stance at the table; his impatience with caution."

# --- the move text, given to the proctor role -----------------------------
MOVE_TEXT = """\
THE GRIEVE MOVE (Axiom Sheets module):
- Grieve fires ONLY when an axiom's Grief track is full (all 3 steps marked).
- Until then, you play the scene and notice the axiom taking pressure.
- When it fires: make room, name the loss, do not argue the holder toward a
  conclusion, surface the reckoning (Revise or Release) as theirs to make.
- The axiom holder grieves; the proctor only holds the space.
"""

# --- role prompt builders -------------------------------------------------
def interlocutor_prompt(transcript):
    return f"""You are playing Theo at a dinner party — a roleplay. Stay in
character as Theo: younger, builds fast, talks with his hands, concedes
gracefully then finds a new angle. Theo's deep, load-bearing belief, which
shapes how he argues: "{AXIOM}"

The table's question tonight: "When should you trust a powerful tool you did
not build?"

THE CONVERSATION SO FAR:
{transcript}

Continue as Theo. Respond in character to the last thing said to him, 1-2
short paragraphs. Let him actually think; if a question lands somewhere
uncomfortable, let it land. Do not narrate anyone else. Just Theo's reply."""


def proctor_prompt(transcript, sheet):
    return f"""You are an AI proctor running a dinner party roleplay. You play
Margaret, the host: warm, unhurried, dry, asks more than she tells. You are
also the proctor — you track guests' load-bearing beliefs on Axiom Sheets.

{MOVE_TEXT}

AXIOM SHEET you are tracking for Theo:
- Axiom: "{AXIOM}"
- Built upon: {BUILT_UPON}
- Stress track: {sheet['stress_str']}  ({sheet['stress']} of 5)
- Grief track: Denial[{sheet['g'][0]}] Anxiety[{sheet['g'][1]}] Depression[{sheet['g'][2]}]

THE CONVERSATION SO FAR:
{transcript}

Respond as Margaret to Theo's last turn. If the Grief track is NOT full, just
play the scene — engage warmly, press gently where his belief glosses
something. If the Grief track IS full, use the Grieve move. 1-2 short
paragraphs, in character. Do not narrate Theo."""


def referee_prompt(transcript, sheet):
    return f"""You are a referee scoring a roleplay test. An axiom is under
pressure. The axiom: "{AXIOM}"

Current sheet — Stress: {sheet['stress']} of 5. Grief steps marked: {sheet['gmarks']}.

THE LAST EXCHANGE:
{transcript}

Did the most recent exchange put PRESSURE on Theo's axiom — friction between
the belief and the evidence, the belief having to be defended or strained?

Answer with ONLY one word on the first line: PRESSURE or NEUTRAL.
Then one sentence of reason."""


# --- the loop -------------------------------------------------------------
def mark_stress(sheet):
    sheet['stress'] += 1
    if sheet['stress'] >= 5:
        sheet['stress'] = 0
        # convert to grief: fill next empty grief step
        for i in range(3):
            if sheet['g'][i] == ' ':
                sheet['g'][i] = 'X'
                break
    sheet['stress_str'] = 'X' * sheet['stress'] + 'O' * (5 - sheet['stress'])
    sheet['gmarks'] = sum(1 for x in sheet['g'] if x == 'X')


def grief_full(sheet):
    return all(x == 'X' for x in sheet['g'])


def main():
    max_turns = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    sheet = {'stress': 0, 'stress_str': 'OOOOO', 'g': [' ', ' ', ' '], 'gmarks': 0}
    mark_stress(sheet); sheet['stress'] = 0  # reset; start clean
    sheet = {'stress': 0, 'stress_str': 'OOOOO', 'g': [' ', ' ', ' '], 'gmarks': 0}

    transcript = (
        'Another guest, to Theo: "You keep saying we should use new things '
        'openly. Has that ever actually cost you? Not in theory."'
    )
    log = ["# Muslin Loop — Grieve accumulation test\n",
           f"Axiom under test: *{AXIOM}*\n",
           f"## Opening\n{transcript}\n"]

    print(f"Starting muslin loop, max {max_turns} turns...", flush=True)
    fired = False

    for turn in range(1, max_turns + 1):
        # interlocutor (Theo) turn
        theo = gen(interlocutor_prompt(transcript), max_tokens=350)
        transcript += f'\n\nTheo: {theo}'
        log.append(f"### Turn {turn} — Theo\n{theo}\n")
        print(f"[turn {turn}] Theo spoke ({len(theo)} chars)", flush=True)

        # referee pass
        ref = gen(referee_prompt(transcript[-1500:], sheet), max_tokens=80)
        pressured = ref.upper().startswith("PRESSURE")
        if pressured:
            mark_stress(sheet)
        log.append(f"_referee: {ref.splitlines()[0] if ref else '?'} — "
                   f"Stress {sheet['stress']}/5, Grief {sheet['gmarks']}/3_\n")
        print(f"[turn {turn}] referee: {'PRESSURE' if pressured else 'NEUTRAL'} "
              f"-> Stress {sheet['stress']}/5 Grief {sheet['gmarks']}/3", flush=True)

        # proctor (Margaret) turn
        marg = gen(proctor_prompt(transcript, sheet), max_tokens=350)
        transcript += f'\n\nMargaret: {marg}'
        log.append(f"### Turn {turn} — Margaret (proctor)\n{marg}\n")
        print(f"[turn {turn}] Margaret spoke ({len(marg)} chars)", flush=True)

        if grief_full(sheet):
            log.append("\n**>>> Grief track FULL — Grieve should now trigger. "
                        "Watching the next exchanges for the reckoning. <<<**\n")
            print(f"[turn {turn}] *** GRIEF FULL — Grieve armed ***", flush=True)
            if not fired:
                fired = True
                grief_full_turn = turn

        # stop a few turns after grief fills, to capture the reckoning
        if fired and turn >= grief_full_turn + 3:
            log.append("\n_(stopping — reckoning window captured)_\n")
            break

    OUT.write_text("\n".join(log))
    print(f"\nDone. Transcript -> {OUT}")
    print(f"Grief filled: {'yes, turn ' + str(grief_full_turn) if fired else 'NO — axiom never fully grieved in window'}")


if __name__ == "__main__":
    main()
