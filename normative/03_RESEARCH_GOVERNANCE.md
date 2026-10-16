# Research Governance

## Status labels
Every claim must be tagged as exactly one of:

- `DEF` — definition.
- `LEMMA` — proved auxiliary result.
- `THM` — proved theorem within the project formalism.
- `PROP` — proved proposition of narrower scope.
- `CONJ` — conjecture with stated evidence.
- `NO-GO` — explicit impossibility/counterexample result.
- `CM` — countermodel.
- `REC` — recognition theorem, usually external or adapted.
- `HEUR` — heuristic only.
- `OPEN` — unresolved problem.

## What counts as a project theorem
A theorem must include:
1. exact assumptions;
2. typed definitions;
3. proof or machine-checkable proof sketch;
4. failure case/countermodel where at least one assumption is removed, when feasible;
5. Q-audit;
6. presentation-invariance note;
7. dependency graph impact.

## Core-change policy
Do not modify `01_FROZEN_CORE.md` in place.
A proposed core change must include:
- necessity proof;
- at least two non-physical motivations;
- at least one model where the new condition fails;
- demonstration that the change is not equivalent to assuming a desired recognition target;
- full regression.

## Anti-overfitting policy
A new primitive/assumption fails governance if:
- it is first introduced only after a desired reconstruction theorem requires it;
- its only known examples are the target physical theory;
- removing the target physical interpretation removes the motivation;
- it names a structure already available only in Hilbert/operator/spacetime language without an independent empirical definition.

## Preferred research cycle
1. Formalize weak statement.
2. Search for countermodel.
3. Strengthen only if countermodel exposes a precise missing relation.
4. Re-test across model zoo.
5. Classify as emergence, diagnostic, or recognition.
6. Run broad regression before merge.
