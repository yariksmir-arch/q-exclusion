# REALIZABLE_MULTISCALE_INTERFACES_V1 — formal specification

Status: optional finite operational module, not a frozen-core extension.
Authority: the frozen core, formal language and governance.
Read [results](RESULTS.md) and [control models](CONTROLS.md) after this file.

## DEF RMI-D1 — supplied operational articulation

`S=(X,U,K,O,G)` is a typed, bounded sector, never a world-state space.
X is a nonempty finite carrier of configurations of explicitly supplied degrees
of freedom. U is a concrete inventory of partial procedures, including any
couplings, preparations and interventions. O is a concrete inventory of
readouts. G gives the actually represented typed composition/feedback grammar.
Keeping G explicit avoids assuming that every mathematically definable word is
available. K supplies either successor supports `K_u(x) ⊆ X × A_u` or an
optional rational kernel `K_u(x) ∈ Δ_Q(X × A_u)` on successor/event records.
Enabledness, failed execution and termination have separate readout tags.
A_u is a supplied finite event alphabet, not an absolute identity register.

"Realizable" means an independently specified implementation/preparation and
readout route, with declared support and uncertainty. It is a boundary condition,
not a consequence of Q-exclusion. The present fixtures are synthetic: their
routes are stipulated in the model and no physically implemented route is
certified. "Real degrees of freedom" in the task is therefore not an ontological
premise licensed by these toy computations. The input remains auditable L1
content when a concrete implementation is supplied.

Rational kernels are optional finite profile representations, not objective
chance or foundational probability. Results involving TV, covariance or expected
counts require this module. Support-only results do not determine these values.
The transition/protocol indices encode composition in G, not fundamental time.
There is no universal continuation space or assumed global perspective family.

## Symbol/type registry

| Symbols | Type, level, dependencies, status, uniqueness, equivalence |
|---|---|
| S,X,U,O,G,A_u,K | Supplied finite sets, partial typed procedures, grammar, event alphabets and support/kernel maps; L0 model presentation, optionally L1 declared data; non-core; chosen; full adequate transport |
| P,Π_P,B_x | Represented finite protocols, their recorded-output laws/supports, and `B_x=(Π_P(x))_P`; L0 diagnostics from S/G, optionally L2 after descent; unique relative to repertoire; transport records and protocol domains |
| ≡,q_*,Z_* | Binary equivalence, projection `X→X/≡`, quotient carrier; L0 derived, optionally L2 empirical; unique up to quotient bijection; full readout/context equivalence |
| q,Z,bar K,bar o | Candidate surjection, carrier, optional quotient kernels/readouts; L0 derived/diagnostic; q chosen, factors unique when exact; kernel and domain squares |
| ε_B,δ_q,η_q,μ_b,ρ,TV | Nonnegative defects, perturbation radius and finite total variation; L0 diagnostic scalar functions; S,q,declared comparison; unique relative to data/units; transport event/readout equality and noise sets |
| F,C,b,V,W | Supplied accessible sector maps `X→F×C`, candidate interface `b:F→V`, external response record alphabet W; L0 representational candidates, optionally L1 procedural addresses; chosen, not primitive I/B/E; decoder/operation squares |
| I,B,E | Residual interface fibres, interface image, complementary accessible sector role; L0 role assignments relative to F,C,b; derived conditional diagnostic; no unique split asserted; transport F,C,b |
| Γ_D,H_n,D_n,C_n,T_n | Explicit bounded witness domain, retained records, available contrast, compatible witness subset and update restriction; L0 derived modal/epistemic diagnostics; supplied scope then unique; witness/record transport |
| J,L,c,v,M,T,h,d,g,R_D | Finite source/output ports, context, contrast map, route-count matrix, clamped transfer response, transmission/differential/change scores and recognizer; L0 derived diagnostics from independently supplied event procedures; unique relative to input interface; port permutations, value bijections and full intervention transport |

Later parameters are typed finite scalars, subfamilies, maps or subsets of these
sets. No new primitive ontology is introduced. Quotient coordinates are always
defined only up to transported bijection. A diagnostic calculation is not an
available scientist-level operation merely because it is computable by the modeler.

## DEF RMI-D2 — external behavioural equivalence

For every represented protocol P, Π_P(x) records the **joint** probe/event trace,
including availability/failure/termination; use a law in the kernel module and a
set in the support module. Define `x≡y ⇔ Π_P(x)=Π_P(y)` for every P in G.
This means all of this declared repertoire, not all conceivable experiments.
`q_*:X→Z_*` is the externally minimal sufficient quotient. A candidate q is
externally sufficient iff `q(x)=q(y) ⇒ x≡y`. Readout preservation alone does
not imply transition descent in a branching/kernel model (BCS5 remains relevant).

Exact definitions quantify the generated repertoire. Finite checks either
decide a finite deterministic congruence by refinement, or verify a stronger
kernel condition sufficient for all finite represented protocols. A bounded
trace test alone is never advertised as an all-protocol decision.

## DEF RMI-D3 — autonomy and nontrivial interface eligibility

Require enabled domains to be q-saturated. For fixed u and z, autonomy is

`q#K_u(x)=q#K_u(y)` whenever `q(x)=q(y)=z`,

where # transports successors and **retained** event outputs jointly.
The defect `δ_q=max_(u,x,y in same fibre) TV(q#K_u(x),q#K_u(y))` tests hidden
configuration dependence after fixing z. Domain failure is a separate exact
failure, never a small stochastic defect. Immediate retained readouts factor
exactly, or have defect η_q defined by the same fibrewise TV test.
`ε_B(q;H)=max_(same fibre,P of depth≤H) TV(Π_P(x),Π_P(y))` is a finite-horizon
behavioural defect, not necessarily δ_q.

An eligible interface requires `1<|Z|<|X|`, nonconstant retained behavioural
content and a declared distinguishing protocol for two image values. Identity
and one-state quotients are automatically rejected. A constant reset with no
distinguishing current readout has no eligible interface. ε-threshold
neighbourhoods need not be equivalence relations; approximate partitions are
tested partitions, not quotients of a nontransitive proximity relation.

## DEF RMI-D4 — operational mediation; conditional I/B/E roles

A candidate split is supplied by accessible procedure/address maps F,C; it is
not obtained by factorizing the cardinality of X. Require represented preparations
for each comparison used; inadmissible combinations are not silently added.
For outward/inward response protocols on the named crossing channels define

`μ_b=max_(same c, b(f)=b(f'), P crossing) TV(Response_P(f,c),Response_P(f',c))`.

The interface has exact mediation iff μ_b=0 on this declared scope and the
interface-update kernels depend only on b(f),c (RMI-D3 on that scope). Compare
both directions separately. Whole-protocol mediation may require a **record
of boundary updates**, not just the initial value of b. A one-step screen is
not promoted to an all-protocol screen. "Small" means `1<|V|<|F|`, or a
separately declared coding cost; no intrinsic scale is supplied.

Only after these tests, B is im(b), I is the residual distinction within its
fibres, E is the complementary accessible sector role C. These are roles, not
primitives or unique entities. Candidates and their partial order are retained
as a family, with overlapping/incomparable interfaces allowed. No preferred
factorization, tree, spatial nesting or literal fractality is inferred.

## DEF RMI-D5 — noise/context/perturbation robustness

Declare a family N of perturbed kernels/readouts and actual context enlargements
before evaluating robustness. Require old domains and comparison maps; then
`sup_(S'∈N) δ_q(S')≤ε_A`, `sup η_q≤ε_O`, `sup μ_b≤ε_M`, plus eligibility
witness margins exceeding their declared observational errors. Adding an
independently available hidden-bit probe can invalidate the same q outright.
Exact support equality is generally discontinuous under small added support;
TV bounds apply only in the optional kernel module. Finite-horizon bounds do
not establish unlimited-depth robustness. Costs/noise weights must transport.

## DEF RMI-D6 — distinction/constraint cycle, with a nonvacuous gate

Γ_D is a specified finite/generated diagnostic witness domain for the sector and
protocol task. It is epistemic/modal; rows are not ontic branches. H_n is a
compatible retained record; `C_n={γ∈Γ_D: γ matches H_n}`. An available contrast
D_n extends H_n and restricts C_n by conjunction. A later contrast becomes
record-defined if its query image on the new nonempty C shrinks, in particular
to a singleton. Nothing chooses γ and no local access role selects a continuation.

The bare arrow `D_n→C_(n+1)→D_(n+1)` is killed as universal bookkeeping.
The minimal gate used here is: independently available first discriminator;
nonempty **strict** restriction; strict change of a different predeclared query
image; no added readout channel or changed query; and, if called a stable next
articulation, eligible q with domain/update descent across the declared N.
This conjunction is nonvacuous, but is standard constraint propagation plus
congruence. It is not an emergence theorem. An eligible q can be an input degree
of freedom of another articulation only through descended updates and available
preparation/readout routes, not merely by renaming its carrier.

## DEF RMI-D7 — presentation changes and genuine enrichment

A strict gauge/presentation change supplies bijections of X, procedure ports,
readout alphabets, event alphabets and G, preserving domains, joint kernels/
supports, output equality, preparations, clamped interventions and noise families.
It may mix coordinates; old address/procedure maps must be decoded, not dropped.
Conjugate q and b accordingly. For nonbijective presentations use T1/CC adequate
common-signature squares and extension-fibre transport; raw fibre cardinality
and compression cost then need their own comparison and need not be invariant.

Adding/removing a probe, disabling a coupling, changing independent intervention
access, replacing old ports by inaccessible blocks or changing the noise budget
changes S. These are not gauge. Erasing a syntactic decomposition while retaining
decoded old operations **is** gauge; asserting new coordinate-independent reset
procedures without their old implementation is enrichment. This explicitly
leaves the factorization/input-boundary problem open.

## DEF RMI-D8 — late transfer recognizer

The neutral procedure interface has simultaneous finite input ports J, freshly
filled output ports L, a repeatable clear/refill cycle, payload contrast v and
context c. Fresh/persisted are operation-event tags (insertion into cleared
ports versus retaining a port), not identity-through-time. Route records map
each fresh output port to an input port or to a context-feed address. They
must be available or independently resolved by clamped interventions. No
unique route is inferred from correlation alone. No lineage primitive occurs.

Hold c, other inputs and allocated route fixed, intervene on v at i and measure
the output payload at j. T_ij is the pair of conditional output laws; its TV
separation h_ij tests transmission beyond the common context. A link is accepted
only with an available route and such positive matched response. Unsupported
routes return NOT_DEFINED, not false. In arbitrary joint-input procedures a
relation can have several links; no unique parent is selected.

On a specified repeatable mixed-input test, derive M_ij as expected counts of
fresh route events i→j. Derive w_i=Σ_j M_ij, and type-conditional mean yields w_a.
The count/profile w is not a fitness primitive. Use the following conservative,
finite witness recognizer, **not a definition of all Darwinism**:

1. At least two simultaneous realizations of a readout-defined payload type and
   at least two payload values distinguishable by available readout/procedures.
   The type map is `v:J×Payload→Payload` on port realizations, merging equal
   payloads in different ports. It is a target-relative record quotient, not
   automatically an autonomous whole-X interface or a new articulation level.
   Identity/one-state maps cannot be promoted as levels by this recognizer.
2. Fresh-output amplification on some input row `w_i>1`, bounded by the supplied
   resources. (A restrictive witness, not necessary for every population model.)
3. Matched clamped transfer response `h>0` for the used payload values and
   declared context family, with contextual feed held fixed.
4. Unequal type-conditional yields `d=|w_a-w_b|>0` under the same mixed context.
5. Nonzero output-profile shift g attributed in the same kernel to transfer
   plus differential yields: an available equal-yield ablation and a transfer-
   scramble ablation eliminate that shift in the locked symmetric test.
6. The same tests remain supported after refill and repeat on the supplied
   mixed support; no universal persistence or unbounded evolution is claimed.

`R_D(S)` is true when this finite interface witness is available and all clauses
pass; false when the complete supplied candidate inventory decides failure;
NOT_DEFINED when the routes/interventions or completeness are missing. Its
reported degree is the vector `(h,d,g,δ,μ)` with a predeclared threshold rule,
not an unmotivated scalar. The finite witness uses no life/organism/reproduction/
fitness/selection/gene/species state labels. It can be realized in nonbiological
hardware. A biological/Darwinian reading is a late interpretation of the
recognized transfer pattern; origin, adaptivity and major transitions do not follow.
