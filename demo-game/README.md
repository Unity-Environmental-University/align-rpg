# Demo Game

**Status: muslin** — a worked example, under test, not a finished product.

---

This folder is a playable assembly of align-rpg: a place to see the whole
system standing up together — characters built from axiom books, with moves
bound to axioms, with live state, actually playing.

It exists because the rest of the repo is well-tested *parts*. This is where
the parts become a game.

## What's here

- **`axiom-books/`** — character classes. An axiom book is a book of axioms
  (load-bearing beliefs); moves hang on specific axioms. `_format.md` is the
  shape; `warden.md` and `trickster.md` are the first two classes.
- **`characters/`** — assembled characters. `rell.md` is one character built
  from two axiom books; `rell-state.md` is Rell's live, mutable state.
- **`playthroughs/`** — saved transcripts of actual play.

## The load-bearing rule

**Moves hang on axioms.** A character can make a move because they hold the
axiom it sits on. If that axiom is Grieved and Released, the move goes with
it. A character's moveset is a live readout of their current beliefs — change
what you believe and you change what you can do.

This is the whole project's thesis as a game mechanic: belief-revision with
mechanical teeth. It is why the system is built around the Grieve move and the
Axiom Sheet (see `modules/axiom-sheets/`).

## How to read it

Start with `axiom-books/_format.md`, then a book, then `characters/rell.md` to
see assembly, then `characters/rell-state.md` to see state. Playthroughs show
it all in motion.

---

Drafted for align-rpg by Hallie Larsson and Claude.
Tools: Claude Opus 4.7, Claude Code, alkahest-rhizome edge register.
