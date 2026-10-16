# Control-class comparison

The class names below are **annotations after construction**. [interface checks](../verification/interface_check.py)
passes no such names to recognizer(). Every model uses RMI-D1 event kernels,
finite resources, declared readouts and available intervention procedures.
The shared formalism does not mean equal carriers or equal kernels.

## Locked controls and their neutral definitions

| Control/class | Neutral operations/constraint input | Recognizer result | Missing property |
|---|---|---|---|
| A1, stable attractor relaxation | Persisted two-port payload maps deterministically to (0,0); reapplying gives (0,0); no fresh insertion event | false | Fresh amplification and clamped transfer |
| A2, single-type crystal-growth control | Capacity 2; input count n∈{0,1,2}, type 0; refill count min(2,2n); all fresh payloads 0 | false | Distinguishable variation; no mixed type witness |
| B1, autocatalytic/prebiotic-like reset control | Nonzero occupancy produces two fresh outputs, zero occupancy stays empty; source routes can have unequal allocation; payload reset to Bernoulli(1/2) independent of clamped source | false | h=0 despite persistence/propagation; g=0 |
| B2, transfer with insufficient differential continuation | Same bounded refill, matched payload transmission, equal route yields | false | d=g=0 |
| C1, finite two-type population model | Capacity 2; allocation per output proportional to payload-dependent weight (1,2); copy allocated payload; clear/refill repeatable | true | All declared witness clauses pass |
| C2, noisy version | C1 with symmetric error 1/10 and available same clamps/ablations | true | h=4/5, d=2/3, g=2/15 |
| Filtering | Persisted (0,1) retains only port 1; no fresh fill; profile changes to all 1 | false | Variation/filtering alone: no fresh amplification |
| Constraint satisfaction | Deterministic reset to (0,0), satisfying imposed equality; no fresh fill or transfer | false | Constraint satisfaction alone |
| Ordinary autocatalysis without heredity | Reset-payload B1 with equal route allocation | false | h=d=g=0 |
| Arbitrary equal-rate copying | All output payloads copy source; allocation weights (1,1) | false | d=g=0 even with h=1 |
| Cohort-only C reduct | Same whole payload transition kernel as C1, but no route/clamp interface | NOT_DEFINED | RMI6: transfer not identified by the declared operations |

B1 is an occupancy-amplifying **toy** model, not a claim about every chemical
autocatalytic set or a simulation of a published prebiotic experiment. C1 is a
standard bounded weighted-sampling population model with a supplied transfer
implementation; it is not merely states named "organism". Its source event
incidence and matched response are neutral operational records. Type = payload
record quotient on port realizations, token = a simultaneous accessible port
realization, not an ontic unit. This typing map is not a discovered whole-cohort
autonomous level; RMI5 therefore supplies A control recognition, not B interface
emergence. No irrelevant hidden degrees are added just to make a quotient proper.

The full refill kernel is checked on all seven cohort configurations of capacity
at most two. Two actual composed C1 rounds have expected payload-1 fractions
`1/2 → 2/3 → 20/27`, with mixed support still nonempty. This is not just
repreparing the original mixed input. Finite zero-mutation fixation is allowed;
the recognizer does not promise indefinite maintenance of variation.

## Structural versus statistical transmission

Uncontrolled input/output correlation is insufficient. A common-context generator
can reproduce the same observed cohort kernel. The discriminator is a physically
implemented postallocation source-payload perturbation holding route and contextual
feed fixed, with joint output readout. It is an additional operation class.
Neither manual biological lineage labels nor a chosen hidden source is used.
If only multiple-source influence is supplied, keep a relation, not a selected
parent. A uniquely resolved route is a feature of the **supplied** single-source
process in C1, not a premise of Q-exclusion or a universal reproduction theorem.

## Population-change algebra (KNOWN)

For a declared route matrix, payload f_i, row yield w_i and output-route payload
mean f'_i, with all fresh outputs attributed and nonzero total W, direct counting
gives

`mean(f')-mean(f) = Cov(w,f)/mean(w) + mean(w*(f'-f))/mean(w)`.

This is the Price identity, not a proof that every covariance is biological
selection. Unattributed contextual outputs add a separate term; missing route
records make f'_i undefined. The equal-yield and transfer-scramble interventions
in the locked test specify an attribution contrast that an algebraic identity
alone does not. Conditioning on a chosen variant-labelled source after the fact
would be circular and is prohibited. The reported α weights are operational row
parameters, not an imported fitness label.

## Overreach boundary

No automatic positive verdict on the listed controls. No universal negative
verdict for **all** crystal growth or nonliving systems is proved: a two-variant
crystal/template/computer process with genuine repeatable transmission and
differential fresh output can satisfy this substrate-neutral recognition
property. Renaming that process cannot make the result negative. Requiring
"nonliving ⇒ false" in addition would introduce the very semantic primitive
the task excludes. Likewise the conservative amplification witness can miss
Darwinian systems observable only through survival; it is sufficient in the
specified control family, not necessary across all biology.

## Outcome of requested A/B/C/D gates

- A: `PASS_IN_DECLARED_TOY_OPERATION_CLASS` (RMI5), no biological state labels;
  recognizer uses independently specified routes/clamps and finite kernel data.
  This is a control separation, not physical validation or universal classification.
- B: `FAILED_TO_FIND_NONSTANDARD_CONDITION`; every interface existence condition
  obtained reduces to congruence/lumpability or response sufficiency.
- C: `SCOPED_IDENTIFIABILITY_NO_GO` (RMI6); even exact cohort kernels/trajectories
  fail to decide clamped transfer without additional available operations.
  Standard identifiability/descent mathematics; not a universal impossibility.
- D: `FAILED_NONSTANDARD_CONTENT`; stable erasure adds no result beyond complete
  behavioural closure and standard coarse-graining/data processing.

There is conditional A and a scoped C obstruction. They justify reporting the
test and its operation boundary, not claiming new mathematics or starting a
further abstract hierarchy program.
