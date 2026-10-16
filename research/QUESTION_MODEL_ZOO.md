# Question definability — optional finite model zoo

Run `python research/regression/question_definability_check.py` from repo root.
Status: PASS, 99,098 exact assertions, separate from every preserved suite.
No numerical probability, universal extension domain or available procedure
is inferred. Small enumeration is not mechanized general proof.

## Exhaustive finite scope

All set partitions U on 0–4 extension entries, all ternary answer maps Q:
1,372 question diagrams. Check point determinacy, least set envelope (37,352
checks), generated answer quotient and all image quotient coarsenings (2,224
universal-property checks), joint kernel and all sufficient base refinements
(2,371 checks), every support subset and its answer shrinkage (50,226 checks).
Target-chosen Q reduct and constant-reduct overblocking are checked separately.
Each finite E is named comparison data, not a universe of possibilities.

## Named countermodels

| Witness | Data / result |
|---|---|
| Point/set/empty | U=(0,0), Q=(0,1): answer {0,1} at 0, ∅ at unused 1; Q=(0,0) point identified |
| Hidden selector | Selecting extension 0 or 1 yields unequal singleton answers; selection is extra data |
| Answer weakening | U=(0,0,1,1), Q=(0,1,1,2): transitive collision closure collapses 0,1,2 |
| Base refinement | (U,Q) has exactly ker U∩ker Q, with unique image factor for each sufficient refinement |
| Competing restrictions | {0} and {1} both maximal resolving subsets, exchanged by adequate swap; no invariant selector |
| Whole Boolean query | F=G=(0,1), U constant: each ambiguous, F XOR G=0 determinate |
| Joint correlation | Joint diagonal {(0,0),(1,1)} strictly smaller than marginal product |
| CI/change pattern | Persistence ambiguous with d=0: Boolean change 0, packet ambiguous (existing OC4) |
| Unavailable decoder | U=id two labels, Q=id; declared decoder grammar constants only, no answer route |
| Presentation | 24 extension permutations and answer reversal preserve whole images/status |
| Extension expansion | Singleton support factors, adjoining conflicting extension destroys point factor |
| Target-defined reduct | U=Q forces descent; no independent boundary certificate follows |
| Constant overblocking | Constant U permits exactly constant Q (including vacuous empty domain) |
| Partial domain | Defined only at one member of a U-fibre: singleton defined-value image is not partial descent |
| Empty comparison class | E=∅ gives no point answer at an unused base value |
| Recognition target pollution | Two/three-element chain meet completions agree on named mix value but full triples nonisomorphic |

The RD6 fixture checks concrete midpoint meet controls and sizes only. The
all-completion self-mix agreement is the mathematical idempotence argument,
not an exhaustive enumeration of rational barycentric algebras. Likewise
the symmetric witness rules out a transport-natural choice in its precise
adequacy class; it does not prohibit externally supplied symmetry-breaking.

General proofs and categorical limits: QUESTION_DEFINABILITY.md. Other
domain countermodels (CPG diagonal/antidiagonal marginals, non-globalizable
network, overlapping linguistic alternatives) remain in existing suites and
the corresponding canonical suites, with their counts kept separate.
