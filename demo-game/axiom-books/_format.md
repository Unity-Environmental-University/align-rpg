# Axiom Book — format

**Status: muslin** — drafted, not yet muslin-tested.

---

An **axiom book** is a character class. It is not a stat block; it is a book
of axioms — load-bearing beliefs a character is composed from. This is
AMALGAM's partbook, in the align-rpg idiom: where a partbook is a piece of a
divine body, an axiom book is a piece of a mind.

A character is *assembled* from one or more axiom books. Each axiom in the
book is an Axiom Sheet (see `modules/axiom-sheets/axiom-sheet.md`): it carries
its own Stress and Grief tracks, and it can be Grieved.

**Moves hang on axioms.** A class move belongs to a specific axiom in the
book. The character can make that move *because* they hold that axiom. This is
the load-bearing rule of the whole module:

> If an axiom is Grieved and **Released**, its moves go with it.
> If an axiom is **Revised**, its moves may change with it.

A character's moveset is therefore a live readout of their current beliefs.
Belief-revision has mechanical teeth: what you can *do* follows from what you
still hold true.

---

## Book format

```
# <Class Name>  (axiom book)

## <one-line description of who this class is>

### Axiom: "<the belief, in plain words>"
Built upon: <what rests on it>
Stress  O O O O O
Grief   Denial[ ] Anxiety[ ] Depression[ ]

  Move — <Move Name>
  Trigger: <when it fires>
  Action: <the attempt>
  Evaluate Result: <Fail Forward / Partial / Full, deferred — read on response>

### Axiom: "<the next belief>"
  ... (an axiom may carry zero, one, or more moves)
```

Keep axioms few — three is plenty for a class. An axiom with no move is still
real: it shapes how the character plays even without granting an action.
