# Compositional L2 Model Zoo

## Scope

Each finite entry is an L1 process presentation with explicitly listed
readouts and partial graphs. `E_P` means its process quotient. No model
interprets sequential notation temporally or turns a raw automorphism into an
action. The positive and stopping verdicts below are end-to-end witnesses,
not substitutes for CP1–CP12.

| ID | Raw declaration and quotient | Result / boundary |
|---|---|---|
| **M1 / CP-CM1** | `P0={f0,f1,g0,g1,h0,h1}`; label readouts give `F,G,H`; all pairs `(gj,fi)` are defined and give `h_(i xor j)`. | Domain saturation and value constancy give the nontrivial partial L2 operation `G circ F=H`. Optional type readouts give `F:A->B`, `G:B->C`, `H:A->C`; no identities are declared. |
| **M2a / CP-CM2a** | `f0~f1`, but only `(g,f0)` is in the raw domain. | Domain saturation fails: composability itself is `NOT DEFINED`. |
| **M2b / CP-CM2b** | `f0~f1`; both `(g,f0),(g,f1)` are defined, with distinct quotient outputs `h,k`. The raw graph is not a represented insertion context. | Value constancy fails: a raw composite exists but no L2 composite does. |
| **M3 / CP-CM6** | M2b plus an actually available probe `rho(f0)=0`, `rho(f1)=1`. | Concrete refinement splits the offending fibre and realizes a quotient where composition descends. |
| **M4 / CP-CM7** | M2b with a grammar whose generated probes are all constant on `{f0,f1}`. | The diagnostic congruence exists mathematically but is unavailable; result `NOT REALIZED`, not automatic test completion. |
| **M5 / CP-CM4** | Quotient `{A,B}`; total raw/quotient operation `X circ Y=X` (left-zero law), with all processes of one descended interface type. | Associative partial-algebra control with no two-sided identity. It blocks automatic category recognition. |
| **M6 / CP-CM8** | One-object quotient `{0,1}`; sequential operation is xor, independent `boxdot` is or. | Both modes descend and have finite units, but with `g2=1,g1=0,f2=0,f1=1`, interchange has left side `0` and right side `1`. No monoidal admission. |
| **M7 / CP-PT4 positive** | M1 is compared with a wrapper carrier having 3 implementations of `F`, 4 of `G`, and 5 of `H`; all readouts/types factor to `{F,G,H}` and every raw output lands in the matching `H` wrapper class. | Different raw carrier sizes transport the quotient, composition, and typing through an explicit common interface; wrapper tags and raw multiplicities are surplus. |
| **M7b / CP-PT3 negative** | Two three-element quotient carriers are abstractly bijective. One graph has only `B circ A=C`; the other has only `U circ U=U` and `V circ V=V`. | Carrier quotient isomorphism cannot establish process-signature transport. |
| **M8 / CP-PF4** | Distinct processes `f0,f1,g0,g1,h0,h1` with `gj circ fi=h0` iff `i=j`, otherwise `h1`. Two declared pair generators use respectively equal and cross pairs; both have the same uniform marginal records in `f` and `g`. | Marginal aggregate profiles are fixed, while the two composite profiles are respectively `delta_h0` and `delta_h1`. Composition of marginal predictions is not defined. |
| **M9 / CP-RD1** | The M1 process signature is represented by two L3 graph drawings with different wrapper/coordinatization data while preserving all quotient arrows and the one partial edge. | Same L2 calculus, different representational surplus. No representation datum becomes L2 merely from this agreement. |
| **M10 / CP-CAT control** | Stronger, separate finite L1 data: interfaces `A,B`, duplicate implementations of `id_A,id_B,f:A->B`, full stated matching composition, identity probes, and all typed associativity checks. | A positive finite category control. It verifies the admission checklist but is not added to the specialized baseline because its extra L1 premises are not forced by M1–M9. |

## Required adversarial claims

| Claim | Finite refutation |
|---|---|
| Descended composition automatically yields a category | M1 has no identities; M5 is associative but identity-free. |
| Associativity yields identities | M5. |
| Two modes yield a monoidal structure | M6. |
| Carrier-quotient equivalence transports composition | M7b. |
| Composition or the generation index is time | M8 fixes the process table while the non-temporal index alternates pair records. |
| Process composition determines composition of predictions | M8. |
| Every mathematical context is a declared context | M4. |
| A structural automorphism is a physical symmetry | M9 has only presentation/structural comparison, no represented action. |
| Compositional plus finite barycentric content licenses CQM | M1–M10 contain no dagger, dual, compact, tomography, purification, or linear/convex process axiom. |

## Model-zoo audit

All positive entries use only explicitly saturated domains and fibre-constant
output classes. M2a/M2b distinguish domain and value failures. M3/M4 separate
mathematical repair from concrete availability. M7/M7b distinguish full
process-signature transport from bare quotient shape. M8 retains a set-valued
cluster result instead of selecting a coupling or an independent product.

The model zoo therefore supports `PARTIAL_COMPOSITION_ONLY`, conditional
associative/typed fragments, and the stated prediction no-go. It does not
support a baseline category, tensor, temporal order, physical symmetry,
operad, or CQM structure.
