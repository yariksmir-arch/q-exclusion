# Correlation Identity — adversarial finite model zoo

All slots below are distinct L0 addresses; `J` means only a diagnostic
partition.  Each listed constraint is a finite declared `Lambda_id` formula.

| ID | finite slots and declared constraint | admissible completions / verdict | audit point |
|---|---|---|---|
| CI-CM1 | `a,b` have identical record outputs; no gluing-sensitive constraint | discrete and `ab` | same role gives underdetermination |
| CI-CM2 | `a` occurs as input, `b` as output; declared persistence law requires `aJb` | only `ab` | different roles can be forced same; the law, not role, does work |
| CI-CM3 | `a,b`, no distinctness clause | `a|b` and `ab` | two slots do not imply multiplicity |
| CI-CM4 | `a,b`, descended readout `Distinct(a,b)` | only `a|b` | explicit descended separation forces distinction |
| CI-CM5 | `a,b`, declared functional/persistence constraint `owner(a)=owner(b)` with its equality rule explicitly descended | only `ab` | uniqueness/functionality is usable only as declared content |
| CI-CM6 | `a,b,c,d`; require a perfect matching from left to right, with all four edges allowed | `ac|bd` and `ad|bc` | symmetry leaves equally valid matchings; no canonical one |
| CI-CM7 | `a,b,c`; constraint: at most one non-singleton block | each requested pair may merge, but no one `J` has `aJb`, `bJc`, `aJc` | pairwise possibility is not joint gluing |
| CI-CM8 | `a,b`; require both `aJb` and `not aJb` | empty class | no vacuous forced same/distinct: `NO_COHERENT_IDENTITY_EXTENSION` |
| CI-CM9 | base has no constraint on `a,b`; refinement adds descended `Distinct(a,b)` | underdetermined becomes forced distinct | CI8's permitted resolution |
| CI-CM10 | rename `a,b` to `u,v`, transport the distinctness table | `a#b` iff `u#v` | presentation relabelling carries verdicts |
| CI-CM11 | `a,b,c`; admissible `ab|c`, `a|bc`, `a|b|c` | a minimum-block selector chooses one merge arbitrarily | minimization is not a fact and fails symmetry transport |
| CI-CM12 | slots named `sensor-7` in two records; no cross-record formula | discrete and merged partitions | shared labels are syntax, not identity |

Additional failure checks: CI-CM1 rejects hidden extensionality; CI-CM2 rejects
role-to-identity and identity-to-role inferences; CI-CM5 rejects unannounced
functionality; CI-CM6/11 reject canonical matching and Occam completion.  In
CI-CM4/5 the stated constraint must itself pass the ordinary L1-to-L2 descent
test; otherwise its correct status is `NEW THEORY REQUIRED` rather than a
member restriction on `mathfrak J(T)`.
