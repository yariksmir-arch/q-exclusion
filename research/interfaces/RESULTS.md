# Results, assumptions and proofs

All results are optional diagnostics. No NEW_FORMAL_RESULT is claimed. Types
are in SPECIFICATION. Each result uses full transported data (RMI-D7), passes
Q only relative to its stated inputs, and has no reverse dependency into the
core. Quotient/update results inherit T0/T1/RR/BCS/CMQ; records inherit CRS/QD.

## THM RMI1 — sufficient quotient and autonomous quotient are separate (KNOWN)

Assumptions: finite S, complete joint records for the represented grammar;
functional law/support outputs with failure tags. Equality of B_x is an
equivalence; q_* is the coarsest quotient preserving B_x. A candidate q
preserves B_x iff `ker q ⊆ ker B`. Separately, an exact quotient kernel exists
iff domains are saturated and each `q#K_u` is constant on q-fibres; it is unique
on im(q). With factored readouts this implies equal finite recorded behaviour
by induction on protocols, including recorded feedback.

Proof: equality and fibre-factorization give the first statements. Define
bar K_u(z) by any x in that fibre; constancy and saturation give independence
and domain. Induction pushes the same joint transition/readout law through
each subsequent protocol node. It does not assert necessity of bisimulation
for trace equivalence. Countermodel: with no probes, arbitrary transitions
have constant behaviour but a proposed nontrivial q can have unequal successor
class images. Without saturated domains, x enabled and y disabled in one fibre
refutes descent. One-state q and identity may satisfy descent but fail eligibility.

## PROP RMI2 — bounded noisy autonomy (KNOWN)

Assumptions: rational kernels, common saturated domains, deterministic surjective
q; finite protocols of depth H; η_q for their immediate records and δ_q for
the joint successor/retained-event kernels. Choose any row per fibre as an
approximate coarse kernel, for comparison only, not a licensed exact operation.
Then trace-law error against that comparison is at most `min(1,Hδ_q+(H+1)η_q)`.
If readouts/events are already folded into the joint kernel, η=0 except for
the initial probe. If every row of K' is within ρ of K on the common joint
alphabet, `δ_q(K')≤δ_q(K)+2ρ`; analogous inequalities hold for readout/mediation
response defects with their own response-law perturbation radii.

Proof: maximal coupling/TV contraction at each common protocol node and a
union bound; same recorded feedback implies same next chosen operation.
Triangle inequality through each original pair of pushed rows gives 2ρ.
No canonical representative is selected as empirical content. Countermodel:
two hidden states whose coarse exit probabilities are 0 and ε have small
one-step defect but eventual-exit probabilities 0 and 1. No uniform infinite-
depth conclusion. A newly enabled operation or added probe is not a small row
perturbation. Three Bernoulli laws at 0,0.4,0.8 with tolerance 0.5 demonstrate
nontransitive approximate similarity.

## THM RMI3 — operational mediation and conditional role invariance (KNOWN)

Assumptions: supplied candidate F,C,b; complete named crossing responses,
represented preparation support and saturated b-update domains. μ_b=0 iff
each response factors through `(b,c)` on that support. A repeatable b-update
requires the independent RMI1 update condition. All factors, δ,η,μ and
eligibility transport under RMI-D7 strict changes; no uniqueness of b follows.

Proof: fibre constancy on response functions/laws; transported equality and TV
are unchanged by alphabet bijections. Countermodels: `e'=a` with F=(a,h) and
b=a screens h; adding `e'=h` as an actually available coupling defeats it.
For `(a,b,e)'=(a,a,b)`, initial b screens the one-step e response but not the
two-step response, which exposes a. Equal duplicate channels b1=b2=a permit
two equally good minimal screens; swapping them forbids an equivariant choice
of one. Static conditional independence of any supplied density alone does
not certify these interventional response/update equations.

## NO-GO RMI4 — the bare D→C→D cycle is vacuous (RECOMBINATION)

Assumptions: any finite transition presentation and specified bounded protocol.
Its finite path rows can be Γ_D; successive readout records define compatibility
subsets by restriction. Thus every such system admits the bare schema, even
identity or constant-reset systems with no new contrast. No nontrivial interface
or recognizable transfer pattern follows.

Proof: expand the finite path rows and restrict by each next recorded equality.
The rows are calculation witnesses, not global histories of the world. The
strictness/independent-query/available-channel/update conditions of RMI-D6
exclude the constant/no-information cases but reduce to standard propagation
and congruence. For `Γ={(0,0),(1,1)}`, probing first coordinate identifies the
second without a new channel; on the full four-row relation it does not. This
is a constraint consequence, not creation of a previously erased distinction.

## REC RMI5 — separation of locked finite controls (RECOMBINATION)

Assumptions: RMI-D8 port procedures/readouts, complete candidate inventory,
matched route-clamp and equal-yield/scramble interventions available; finite
rational kernels; two input/output slots, mixed payloads (0,1). Source allocation
uses weights α_0,α_1>0; outputs independently copy their allocated source with
symmetric payload error m. Fresh clear/refill rounds reuse this kernel. This
is a bounded two-type Wright–Fisher model when α differs and m<1/2, regardless
of naming. It is an explicitly supplied joint kernel, not derived from Q.

For this test, `w_0=2α_0/(α_0+α_1)`, `w_1=2α_1/(α_0+α_1)`,
`h=|1-2m|`, and
`p'_1=m+(1-2m)α_1/(α_0+α_1)`.
With α=(1,2), m=0, the scores are h=1, d=2/3, g=1/6, max w=4/3.
With 0≤m<1/2 they retain strictly positive margins; the output shift is
`(1-2m)/6`. Equalizing α and scrambling transfer to m=1/2 both give p'=1/2.
Thus the recognizer passes C, rejects one-type stable/growth controls A,
rejects reset-transfer autocatalytic controls B (h=0), and rejects equal-yield
copying (d=g=0) and persistence filtering (no fresh amplification).

Proof: sum the enumerated route/payload event kernel; contrast under fixed
route yields Bernoulli parameters m and 1-m. The same expressions apply after
any refill on mixed support. Composition of the recognized route relations is
a finite path relation, not an absolute lineage identity. Existing population
models motivate this recognizer externally; it is not a universal life theorem.
Countermodels removing each clause are CONTROLS rows A/B/filter/copy/reset and
the unavailable-clamp completion in RMI6. Complete noise boundary m=1/2 kills
transmission. Excluding reverse transmission m>1/2 is not part of the general
recognizer, but is part of the faithful-copy control family.

## NO-GO RMI6 — even complete cohort trajectories need not identify transfer (KNOWN)

Assumptions: X is bounded payload-cohort configurations; U contains cohort
preparation/refill, O all payload-cohort readouts; no event incidence or
postallocation source perturbation is available. Consider two extensions:
(i) sample weighted source addresses then copy their payloads with error m;
(ii) sample output payloads from the same `p'_1(x)` via a context-fed generator,
with no source-to-output transfer channel. Their **whole** K on X is identical
for every x, not just one observed trace. All U and O in the reduct agree.
The clamped-transfer response is nonzero in (i) and zero in (ii).

Proof: in either extension each output has the same conditional Bernoulli law,
independently given x. Induction gives identical laws for arbitrary finite
adaptive cohort protocols. Holding allocated routes and generator context
fixed while changing a source payload gives m versus 1-m in (i); (ii) remains
unchanged. That operation is absent from the reduct. For its forgetful map U,
`U(e1)=U(e2)` but their response contrast F differs: NEW THEORY REQUIRED for
this transfer fact. No number of extra trajectories supplies the missing
operation. This is a scoped identifiability obstruction, not a no-go for all
neutral operational structures, nor proof that the feed mechanism cannot be
Darwinian at some other supplied articulation. Adding a physically implemented
clamp/route channel separates the extensions and removes this obstruction.

## NO-GO RMI7 — exact minimal full-repertoire quotients cannot form a strict ladder (KNOWN)

Assumptions: q1=q_* of RMI1, and X1 inherits **all** original protocol records
with their transported contrasts. Any q2:X1→X2 preserving those records is
injective. Proof: distinct q1 classes have a separating protocol, which cannot
factor through a map identifying them. Thus no second strict reduction exists.
Removing full record inheritance permits task-relative coarse-graining, but
is not an interface emerging from unchanged information. Removing minimality
permits reducing an over-refined first q, which is not evidence of a new level.

Worked neutral case: X0={0,1}³=(a,b,h), `u(a,b,h)=(a,b,0)`. Original probes
read (a,b), so q1=(a,b), sizes 8→4, δ=0, and invariants a,b survive. On an
independently **restricted** next repertoire reading a only, q2=a gives 4→2,
δ=0 and invariant a survives while b is lost. Another restricted task gives
b; these two interfaces are incomparable. Nested versions retain a similar
copy/reset pattern, but the repetition was supplied. No scale-invariance,
linear hierarchy or new emergence theorem is inferred. q2 fails under inherited
probe b. A syntactic isomorphism mixing a,b transports both probes and q1.

## PROP RMI8 — erased distinctions and operational completeness (KNOWN)

Assumptions: x≡y for the **complete** original generated repertoire and same
subsequent available protocols, with all decision inputs recorded. Then no
subsequent protocol separates x,y: it is already one component of B. Repeated
descent therefore cannot recover an erased contrast. On incomplete closure,
`(a,h)'=(h,h)` exposes hidden h through a later a-probe; so equal immediate
a-readouts were not full behavioural equivalence. Correlated stored records
are a channel in the **joint** signature, not spontaneous recovery. A new
independent probe or coupling can refine the quotient. This is frozen
empirical closure/availability discipline, not a new multiscale law (D fails).

## NO-GO RMI9 — no privileged factorization/flow/component from the bare carrier (KNOWN)

Assumptions: an abstract carrier with only a supplied transition/readout
signature, lacking independent address/intervention grammar. Set bijections
alone do not choose a decomposition or eligible intermediate interface.
In a fully probed carrier ≡ is identity and no proper sufficient quotient
exists; with constant probes/reset it is one-state and fails eligibility.
A lookup transition can realize any finite automaton, so expressiveness gives
no emergence mechanism (universal-constructor kill).

For the immediate response relation of `(a,b,c)'=(a,a,b)`, a influences b,
b influences c, a does not immediately influence c; b does not influence a.
This relation is neither symmetric nor transitive. Its undirected connected
closure is an equivalence **by definition**, not a derived objective flow.
Grouping ports without retaining decoders changes component reports; adequate
decoded transport retains old response answers. The STRONG FLOW THESIS has
no admissible universal form in these premises and is CLOSED. This does not
contradict invariance of a properly transported, task-relative graph component.

## Assumption-removal ledger (applies to all positive claims)

| Assumption | Failure witness and effect |
|---|---|
| Finite supplied carriers / closed domains | Infinite unbounded ports defeat finite exhaustive algorithm/capacity claims; partial enabledness in one q-fibre defeats descent |
| Independently supplied U,O,G and complete decisions | Empty grammar or withheld probe hides transfer; missing negative table membership makes exact test NOT_DEFINED |
| Rational row kernel (optional) | Same full-support two-state relation with weights 1/2 or 9/10 has equal supports and unequal d/g/TV; numerical scores not support facts |
| Exact congruence / autonomous update | Hidden-bit reveal and non-lumpable proposed partition in finite enumeration |
| Adequate transport including probes/clamps/noise | Reblock without decoding or add hidden-bit probe; old q is insufficient |
| Supplied candidate sectors and preparation support | Diagonal-only preparation cannot justify off-diagonal intervention comparisons; symmetric duplicates preclude unique chosen screen |
| Bounded perturbation family and depth | Unbounded bit leakage/deep rare-exit witness defeats stability extrapolation |
| Matched transfer beyond context | m=1/2 output reset or identical trajectory completion RMI6 |
| Multiple payload values/fresh amplification/differential yields | One-type growth / persistence filtering / equal-yield copying respectively |
| Full-repertoire inheritance in RMI7/RMI8 | Restricted b-dropping task permits second quotient; absent closure permits later reveal |

## Local/global firewall

Every result concerns a finite sector/protocol. A trace through separately
available local contexts does not provide a simultaneous compatible assignment.
Three Boolean contextual scopes AB,BC,CA with a=b, b=c, c≠a have nonempty local
supports and locally valid readout traces but no global section. A context
switch/repreparation record can successively visit each scope. It does not
assert overlap identity across visits. An overlap-preserving global gluing rule
would be an additional assumption and would fail in this witness (SW5/CO/P5).
No proof above assumes a global section, chosen history or completion.
