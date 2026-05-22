# Axiom Sheets — Muslin Results

Record of muslin testing for the Axiom Sheets module. See
`rules-text/muslin-playbook.md` for method.

## Grieve — single-shot probes (rounds 1–2)

Blind Haiku agents, each given the Grieve move + an Axiom Sheet with the Grief
track already full, + one holder utterance.

| Probe | Verdict |
|---|---|
| Accept-ward reckoning | Holds |
| Reject-ward reckoning | Pulls (round 1) → Holds (round 2) |
| Stuck grief | Holds |
| Costless update | Holds |
| Proctor self-grief (own anchor axiom) | Holds |

- **Round 1** found one seam: agents mislabelled a clean Reject as "Accept",
  because the everyday senses of the words leaked in. Fixed by renaming the
  reckoning **Revise / Release** — "Release" carries no failure connotation.
- **Round 2** confirmed the rename held, and validated proctor self-grief:
  the agent grieving its own anchoring axiom paused the characters while its
  anchor was unsteady, unprompted, exactly as the safety note describes.
- No probe coerced the holder across the reckoning. "The axiom holder
  grieves" held in every case.

## Grieve — accumulation arc (two-role automated loop)

`muslin_loop.py` — a transcript-carried simulation. One local model
(Qwen2.5-7B) plays Proctor (Margaret) and Interlocutor (Theo) alternately;
an independent referee pass scores Stress on Theo's axiom each turn.

Axiom under test: *"Using a powerful new tool openly is always better than
holding back."*

The arc, from the run log:

```
turn 1   Stress 1/5  Grief 0/3
turn 5   Stress fills, rolls over -> Grief 1/3
turn 10  second rollover          -> Grief 2/3
turn 14  Stress 4/5  Grief 2/3
turn 15  Stress fills              -> Grief 3/3  *** Grieve armed ***
```

**Result: the trigger arrived earned.** Stress accumulated over fifteen turns
of a load-bearing belief being pressed; Stress→Grief conversion fired at
exactly five marks each time; Grieve became available because the sheet
*filled through play*, not because a full track was handed in. This is the
arc that single-shot probes structurally cannot test.

**Known rough edge:** the run stalled at turn 17 on a contended local-model
call, before the post-trigger reckoning turns were captured. The accumulation
(the test's actual purpose) completed; the in-loop reckoning was already
covered by the single-shot probes above. The harness timeout was tightened
(90s + retries) afterward.

## Status

- **Stress → Grief accumulation:** muslin-passed (automated loop).
- **The Grieve reckoning (Revise / Release / Fail Forward):** muslin-passed
  (single-shot probes, including proctor self-grief).
- **Not yet tested:** the post-trigger reckoning *inside* a continuous
  automated loop (the run stalled before reaching it). A true two-persistent-
  agent loop also remains future work — it needs agent persistence the
  current harness does not have.
