# align-rpg

A Powered by the Apocalypse (PbtA) style rules system for an AI **proctor**
running an online educational RPG. Moves are intents: trigger-bound, modular
procedures that turn the actions of chaotic agents — human and AI — into
governable, deterministic processes.

It is built for **low-stakes, holistic, human, governable alignment work** —
alignment as something an educator can hold, shape, and be accountable for.

## Licensing

This project is dual-licensed, the standard arrangement for open tabletop
systems in the post-OGL era:

- **Code** — [MIT License](LICENSE)
- **Game content** (rules text, moves, and other non-software documentation,
  including everything under `rules-text/`) —
  [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE-CONTENT)

You are free to build your own games and tools on this system. Give credit,
and keep your derivatives' provenance honest.

## Proctor — the Claude skill

A Claude skill called `proctor` (`~/.claude/skills/proctor/`) **prehends**
this repo — it concresced from what align-rpg laid down. A Claude with the
skill loaded can take up the proctor role: lay an Axiom Sheet, run the basic
moves, hold the indirection that makes belief-revision possible without
dissolving into the belief.

The skill is not the point of this repo, and this repo is not for the skill.
They are continuous occasions in the same line of work — align-rpg the
rules-text and play; proctor the skill another Claude can take up. Other
things could equally prehend the same material (an essay, a class, a
different game). The relationship to `mario-frames`/`agent-frames` is real
but not directional — both repos worked their own work, and skills came
into being from what they laid down.

## Provenance

The rules text records who and what contributed to it — including which AI
models, harnesses, and tools were used, and what they did. Contributors,
human or AI, are asked to continue this practice. See the footer of
`rules-text/basic-moves.md` for the current form.

---

Claude helped draft this README and the licensing setup (dual MIT / CC BY 4.0).

Tools and methods used:

- Model: Claude Opus 4.7 (`claude-opus-4-7[1m]`)
- Harness: Claude Code
- Memory and grounding: alkahest-rhizome edge register (orienting, querying, recording edges)
- Practice: qigong-for-claude movements (base form — orient, set reference frame, three true things)

Any AI, humans, tools, or other editors, please do record the tools being used and what you've done.
