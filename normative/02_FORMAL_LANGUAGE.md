# Formal Language and Typing Rules

## A. Levels
Use the following levels explicitly.

### L0 — Metatheoretic presentation
Objects used by the mathematician to represent structural content: sets, categories, graphs, algebras, etc.

### L1 — Declared structural content
`B_K` and typed substructures represented in the chosen presentation.

### L2 — Empirical quotient/signature
`E_R`, `Sigma_R`, descended operations and relations.

### L3 — Mathematical representation of mature empirical structure
Probability spaces, ordered groups, manifolds, operator algebras, fields, gauge representations, etc.

Never infer L1 ontology from L3 coordinates without an explicit descent/recognition argument.

## B. Required annotations for new symbols
For every new symbol state:
- type/domain/codomain;
- level L0–L3;
- dependencies;
- whether core/derived/diagnostic/representational;
- whether unique, chosen, or defined only up to equivalence;
- which equivalence relation it must respect.

## C. Equivalence notation
- `~_R`: empirical equivalence at repertoire R.
- `≅`: mathematical isomorphism in a declared category/class.
- `~rep_R`: empirical equivalence of representations relative to `Sigma_R`, when defined.

Do not conflate them.

## D. Descent diagram
Whenever a new scientist-level map is introduced, require a commuting diagram:

```
X_tilde --F_tilde--> Y_tilde
  | q_X               | q_Y
  v                   v
X      --F------->     Y
```

If no such descended `F` exists, mark the operation `NOT DEFINED AT THIS QUOTIENT`.

## E. Refinement diagram
For `R ⊆ R'`:

```
Sigma_R' --optional late structure--> M_R'
   | pi                           | c
   v                              v
Sigma_R  --optional late structure--> M_R
```

Compatibility must be stated; never assume it globally.

## F. Modal vocabulary
Avoid unqualified use of:
- possible, necessary, actual, all experiments, all continuations, all worlds.

If modal language is needed, define a concrete finite/generated domain within the formalization.

## G. Probability vocabulary
Never use “true probability” as primitive. Distinguish:
- finite count vector;
- rational empirical profile;
- compatible profile;
- stable predictive profile;
- set-valued predictive content;
- probability representation.

## H. Time/order vocabulary
No universal continuation relation. Any order must be declared for the concrete module in which it appears.

## I. Recognition vocabulary
A statement of the form

`Sigma_R has property P => Sigma_R admits representation in class M`

is a `RECOGNITION THEOREM`, not an emergence theorem, unless `P` itself has been independently derived from weaker core structure.
