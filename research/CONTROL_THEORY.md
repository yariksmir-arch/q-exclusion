# Control, branching and continuation records

Conditional existing results. DCS concerns deterministic controls; BCS concerns branching records; CPC concerns a distinct protocol-composition quotient; CMQ concerns static sufficient records and their update boundary. Proofs and removal countermodels are included below. No new theorem-level novelty is claimed.

## 3. Definitions introduced

**DEF DCS-D1 (control-word observation kernel).** Let `(X_s)` be declared carriers, `theta_s` their base empirical equivalences, and each declared unary control `u:s->t` a partial function `T_u:D_u subseteq X_s -> X_t`. These are L0 descriptions of declared L1 content, non-core. Let `W_s` consist of all finite type-correct chains generated from these controls, including the empty word; composition is evaluated left to right. The syntax is derived L0 diagnostic data, unique relative to the declared generators. A type-correct word need not be executable on every input. Define the totalized diagnostic probe

`J_w(x) = bottom_t` if execution fails, and `J_w(x)=[T_w(x)]_theta_t` otherwise,

where `bottom_t` is a separate failure tag, never an arrangement or ontic object. Put `x alpha_s y` iff `J_w(x)=J_w(y)` for every `w in W_s`. `alpha` is derived L0 equivalence data; its quotient is only diagnostic until concrete probe availability is established. All input dependence is explicit; no arbitrary representative is selected.

**DEF DCS-D2 (finite observation-conditioned policy).** A policy is a declared finite rooted decision tree. At a node it may read an available non-destructive observation constant on `theta_s`, select a control using that readout and the previously declared finite readout/control transcript, and continue in the corresponding target sort. Every leaf readout is also constant on the terminal `theta_s` class; termination tags depend only on the common declared transcript/node. Execution failure returns the separate failure tag. Node number/transcript position is syntax, not fundamental time. This L0 description of optional L1 syntax is derived, non-core, and chosen from a declared grammar. Equal transcripts at corresponding nodes must prescribe the same control. A readout that changes the continuation must instead be included as an explicit deterministic instrument/control, with its readout and update in the interface.

## 4. Results

**THM DCS3 (word normal form for deterministic repair).** Under DCS-D1: (a) `alpha` is an equivalence; (b) `alpha subseteq theta`; (c) each `D_u` is alpha-saturated and `T_u` preserves alpha; (d) `alpha=C_K(theta)` for `K={T_u}`. Consequently it is the greatest/coarsest strong control congruence below theta. Totality is unnecessary. No finiteness of carriers, generator family, or word length bound is required.

**PROP DCS4 (conditional repertoire equality).** Suppose `theta` is the kernel of a declared readout family `R`. For every word/readout pair, suppose the grammar actually implements a tagged probe returning failure when execution fails and `r(T_w(x))` otherwise, and its closure contains exactly these probes or only additional alpha-constant probes. Then that generated repertoire has empirical equivalence alpha. Without probe availability the claim is diagnostic only (RR7); without alpha-sound closure only one inclusion follows. A family of empty readout coordinates must still supply an execution-success tag: undefinedness cannot be recovered from an empty tuple.

**THM DCS5 (deterministic finite feedback does not split the word kernel).** Under DCS-D1/DCS-D2, alpha-related inputs yield the same complete policy transcript and terminal readout/failure for every declared finite policy. If the policy grammar also contains the fixed-word experiments and their terminal readouts/failure tags used in DCS4, policy and word observational equivalences coincide. Without that inclusion only the no-additional-distinction direction is proved.

**NO-GO DCS6 (unlicensed composition promotion).** Unary stability and feedback invariance do not imply congruence for an arbitrary represented multi-input protocol composition, do not supply protocol-fibre descent, and do not create a generation scheme. Existing CPG3/PF4/CRS conditions remain necessary.

Novelty status: DCS3 is an explicit normal form and partial-domain specialization of T0.5, not an independent generic minimal-refinement theorem. DCS4 specializes RR4–RR7. DCS5 supplies a repo-new specialized deterministic adaptive-policy boundary lemma, with no external originality claim and without strengthening SP5/SV/PF. DCS6 reiterates their established interface firewall.

## 5. Proofs / proof sketches

For DCS3(a), alpha is an intersection of kernels of total functions `J_w`. The empty word has `J_empty=q_theta`, proving (b). Equality of `J_u` preserves definedness. If `x alpha y` and `u` is defined, for every target-sort word `v`, the generated concatenation `uv` gives `J_v(T_u(x))=J_v(T_u(y))`, proving (c). Conversely let beta be any strong unary-control congruence below theta. Induction on word length shows that beta-related inputs have matching execution domains and beta-related terminal values; therefore they have equal `J_w`. Thus beta is contained in alpha. Together with (c) this proves maximality and identification with T0.5. No quotient compatibility of the original theta is assumed: its failure is precisely what alpha repairs.

For DCS4, equality of all terminal readouts is equality of theta classes by the kernel assumption; the failure/success tag enforces domain equality. Hence equality of generated word probes is exactly equality of all `J_w`. Additional closure observations may be included only if alpha-constant. This is RR soundness/separation with a specific grammar, not permission to extend the grammar.

For DCS5, induct on the common path through a policy. At its root related inputs have equal node readout. The policy consequently selects the same control, with the same type and admissibility. DCS3 gives simultaneous failure or alpha-related successors. Their next node readouts agree. The recorded transcripts therefore remain equal, so transcript-dependent choices agree as well. Finite tree depth gives the same leaf or failure. For the converse equivalence inclusion, a fixed word followed by a terminal probe is itself an admitted policy. Histories already represented by the carrier pose no new difficulty; ignored historical coordinates do.

For DCS6, take a single sort `X={a,b,c}`, `theta={{a,b},{c}}`, all unary controls identities, and base readout `r(a)=r(b)=0,r(c)=1`. Then alpha=theta. Declare total binary composition `F:X×X->X` with `F(b,a)=c` and `F(x,y)=a` for every other pair. Inputs `(a,a)` and `(b,a)` are componentwise alpha-equivalent but their outputs are not. Thus F fails product-fibre constancy despite DCS3/DCS5. No control saturation can claim this F descends unless its plugging contexts enter the declared operation/probe grammar.

## 6. Countermodels and failed routes

**CM DCS-M1 (empty word missing).** With two inputs, distinguishing base readout, and no controls, a word family omitting the empty word imposes no tests: its kernel is universal and fails refinement. The empty-word assumption is essential.

**CM DCS-M2 (bounded/arbitrary words).** On `X={a,b,c,d}`, readouts `r(a)=r(b)=r(c)=0,r(d)=1`, let `u(a)=a,u(b)=c,u(c)=d,u(d)=d`. Testing only empty and one-letter words relates a,b, but sends them to a,c, which those probes distinguish. `uu` kills the pair. A bounded word family or arbitrary family lacking the required concatenations is not generally stable. Finite-state stabilization can justify a bound only after a separate argument.

**CM DCS-M3 (common-domain comparison).** `X={a,b}`, constant readout, `u` defined only at a with `u(a)=a`. Comparing terminal observations only when both executions succeed relates a,b; a policy attempting u distinguishes success from failure. Domain-totalization repairs the theorem. Moreover, the relation produced by ignoring undefinedness need not even be transitive: three points with probe values `0,bottom,1` relate the first to the second and the second to the third but not the first to the third.

**CM DCS-M4 (history omitted from carrier).** A reduced carrier contains only one symbol z and constant readout. A declared prefix decoration h is either 0 or 1, and future control u is admissible iff h=0. Then the reduced carrier does not carry a function/domain for u. Adding h to a history carrier makes a legitimate partial interface and DCS-M3 detects the distinction. Treating the reduced z semantics as deterministic while allowing this historical admissibility is ill-typed; it is not a counterexample to DCS5. Erasing h witnesses `NEW THEORY REQUIRED` for its claimed old-theory admissibility fact.

**CM DCS-M5 (policy uses a hidden selector).** Use DCS6's base carrier, and unary controls identity and constant-c. On equivalent a,b, a purported controller reads their unrevealed names and chooses identity at a and constant-c at b. The final readouts differ. This controller is not observation-conditioned: its choice fails input-fibre invariance. A policy may use a declared external memory, but comparison must fix that memory or equip it with an explicit compatible relation.

**CM DCS-M6 (probe availability absent).** The RR availability countermodel in INTEGRATED_THEORY.md declares an operation f separating a,b after readout, but its available test grammar cannot form `r composed with f`. DCS3 remains a diagnostic result; DCS4 fails. Conversely a closure containing an extra readout separating two alpha-related copies fails alpha-soundness and produces a finer equivalence. These are both existing RR kill tests, not new refinements.

**CM DCS-M7 (type mismatch).** Let `u:s->t` and `v:k->s` with distinct t,k. Formal token concatenation uv is not a map at all. Word quantification must be over the generated typed category of chains, not all token strings. Disjoint sort tagging prevents false cross-sort pairs.

**CM DCS-M8 (observations update content).** On carrier `{z}`, an alleged observation returns 0 and secretly replaces an erased memory by h=0 or h=1. A later control reads h. The reduced observation is not a non-destructive probe and the reduced update is not a declared deterministic map. Restating it as an instrument on an explicit carrier is required. DCS5 does not authorize readout disturbance to be ignored.

**CM DCS-M9 (unrestricted terminal output).** Two arrangements a,b have constant base readout and identity controls, hence `a alpha b`. A zero-step policy whose leaf outputs 0 at a and 1 at b distinguishes them. Its leaf readout is not theta-constant and is excluded by DCS-D2. Merely requiring internal decisions to be observation-conditioned is insufficient.

These models discharge the removal tests for word inclusion/closure, domains, typed composition, policy input, non-disturbing probes, and operational availability. Determinism itself is essential; branching/open-loop separation is handled by the branching-control definitions and BCS1–BCS6 below. Infinite carriers and partial maps are allowed, so no artificial totality/finite-state requirement is proposed.


## 3. Definitions introduced

**DEF BCS-D1 (declared branching interface).** `X` is an L0 set presenting an
L1 carrier of arrangements in a single declared module; alternatively it is
a disjoint union of declared sorts. `A` is a declared set of action codes,
not a universal action space. For each typed action `u`, its declared partial
graph has enabled domain `D_u` and successor map `Delta_u:D_u -> P(X)`
(with the specified output sort). `o:X -> O` is the declared totalized
observation map. `theta` is a specified sort-respecting equivalence contained
in `ker(o)` (normally the current empirical equivalence). `D_u`, `Delta_u`,
and `o` are optional L1 data, not core consequences. Their powerset
presentation is representational L0 machinery; it makes no chance assertion.

**DEF BCS-D2 (branching repair).** On relations `Z subseteq theta` define
`Phi(Z)` by: `x theta y`, equal enabledness for every typed `u`, and for
each enabled action every successor of `x` has a `Z`-related successor of
`y` and conversely. Let `beta = nu Phi`. This is the unique greatest fixed
point in the powerset lattice of the declared `X x X`, L0 diagnostic and
derived, dependent on exactly BCS-D1. It is not automatically a new empirical
quotient. Empty enabled successor sets and disabled actions are distinct.

**DEF BCS-D3 (finite records and policies).** A finite control word is a
finite derivation in the specified typed control grammar. A record is the
tuple `(o(x0),...,o(xn))` along a matching execution. A deterministic
history policy chooses the next admissible action from the declared observed
record and declared interface type; its finite depth bound is part of its
code. `Trace_x(w) subseteq O^(n+1)` and the corresponding policy record
sets are L0 diagnostic direct images of the declared L1 execution graph,
or L2 content only after descent. There is no selected execution. Terminal
content is the last-coordinate projection of this record set.

## 4. Results

**NO-GO BCS1 (terminal open-loop content is insufficient).** Under BCS-D1,
equality of terminal observation sets for every admissible fixed word does
not imply finite deterministic feedback equality. Eight-node CM1 below is
a witness. H3 is correct for this signature; it is false if interpreted as
equality of complete observation-record sets for every word.

**THM BCS2 (complete trace filtering).** Assume BCS-D3; the same typed word
grammar is used on both inputs; action availability, undefinedness, and
early termination that are declared observable are included in the records;
policy decisions depend only on such recorded data. If
`Trace_x(w)=Trace_y(w)` for every admissible fixed word, all declared finite
deterministic history policies have equal full record sets and terminal
content on `x,y`. No finiteness of `X`, determinism of `Delta`, or nonempty
successor condition is required. This is a trace-semantics statement, not a
bisimulation necessity theorem.

**THM BCS3 (coarsest branching descent repair).** Under BCS-D1–BCS-D2, `beta`
is an equivalence, refines `theta`, and is the greatest equivalence refining
`theta` for which all enabledness predicates and all maps
`[x] -> { [z] : z in Delta_u(x) }` are well-defined on its quotient.
This is powerset-image descent, not descent of a selected successor.
It is the strongest justified version of H4(1)–(3), at a diagnostic level.

**THM BCS4 (finite feedback sufficiency).** Under BCS-D1–BCS-D3 with
observation-respecting policies, `x beta y` implies equal finite feedback
record sets, including equal enabledness/termination behaviour if recorded.
It therefore implies equality of any declared function of those records,
including terminal readouts. H4(4) holds in this stated scope.

**NO-GO BCS5 (branching equivalence is not necessary).** Complete finite
feedback trace equivalence need not imply `beta`: CM2 is a seven-node
witness. Thus refining to bisimulation may distinguish presentations that
the declared record signature does not distinguish. It cannot be asserted
as physically preferred or automatically available refinement.

**PROP BCS6 / NO-GO (composition boundary).** If finite policy composition
means concatenation of represented history policies, retaining the recorded
history and typed residual interface, BCS4 applies to their represented
composite. It does not make `beta` a congruence for a separately declared
binary protocol/process operation `c:D -> X`. Such congruence holds exactly
when `D` is `beta x beta`-saturated and equivalent defined pairs have
`beta`-equivalent outputs (CP1). CM3 defeats unconditional H4(5).

## 5. Proofs / proof sketches

BCS2: for each policy leaf of depth `n`, pair its action word `w` with a
record `h`. It occurs precisely when `h in Trace_x(w)` and at each prefix
the policy chooses the next letter of `w`. Filter the fixed-word record
sets by these policy-compatibility equalities, then take their union over
the finite-depth policy's declared leaves. Equality is preserved. Variable
termination is treated by leaf records, not by a fictitious extra execution.
The action words may range over a set-sized branching policy; depth alone
is finite. There is no finiteness or compactness inference.

BCS3: `Phi` is monotone, so its greatest fixed point exists as a diagnostic
set relation. Identity is a postfixed relation. Inverse of any postfixed
relation is postfixed. Composition of two postfixed relations is postfixed:
match a successor first through the first relation, then through the second;
the reverse matching follows in reverse order. Enabledness agrees through
the intermediate node and `theta` is transitive. Thus the greatest relation
contains identity, equals its inverse, and contains its own composition; it
is an equivalence. For any equivalence `alpha subseteq theta`, equality of
successor `alpha`-class sets is exactly the two matching clauses, while
partial-map descent additionally requires enabledness saturation. Therefore
`alpha` has the claimed descent iff `alpha subseteq Phi(alpha)`, and maximality
places it in `beta`. Conversely the fixed-point clauses give descent for
`beta`. No successor representative is chosen in defining the quotient map.

BCS4: induct on finite policy depth. Related inputs have equal observations,
so the policy selects the same admissible action. Match every successor
using the fixed-point property; apply induction to the identical extended
history. The symmetric condition gives equality of the resulting record
sets. Terminal/deadlock handling uses the declared enabledness flag.
BCS6's first part follows because the composite belongs to this policy
grammar; the second part is CP1's binary instance, not a new category axiom.

## 6. Countermodels and failed routes

**CM1 (terminal correlation loss).** Typed grammar has precisely the words
`epsilon,u,ua,ub`. Roots `x,y` have observation `root`. Action `u` sends
`x` to `{x0,x1}` and `y` to `{y0,y1}`; `o(xi)=o(yi)=i`. Shared terminal
nodes `zero,one` have observations 0,1. For `x0`, `a` goes to `one` and
`b` to `zero`; for `x1`, reverse those outputs. For `y0,y1`, reverse each
of the respective `x` tables. Terminal sets for `u` are `{0,1}`, and for
both `ua,ub` are `{0,1}`, on both roots. The policy choosing `a` after 0
and `b` after 1 produces `{1}` at `x` and `{0}` at `y`. Full records for
`ua` already differ, so CM1 does not refute BCS2. No claim of globally
minimal node count is made; this is a small explicit finite witness.

**CM2 (feedback equality without branching descent).** Roots `p,q` have
observation `root`. `u` sends `p` to `{r,s}`, `q` to `{v}`; all three
intermediate nodes have observation `mid`. Both `a,b` send `r` only to
`zero`, `s` only to `one`, and `v` to `{zero,one}`. Same depth-two grammar
as CM1; terminal nodes have no further enabled actions. All fixed-word
full trace sets agree, hence all finite history policies agree. But neither
`r` nor `s` can match `v` under any observation-respecting bisimulation,
so the roots are not `beta`-related. Recorded enabledness also agrees.

**CM3 (independent composition).** `X={x,y,z}`, observations 0,0,1, no
controls. Thus `x beta y`. Declare a total binary operation with
`c(y,x)=z`, and all other outputs `x`. Then input pairs `(x,x),(y,x)`
are equivalent but outputs are not. Neither branching saturation nor
feedback closure can repair the missing compositional relation automatically.

**CM4 (disabled versus empty).** Two observation-equal nodes have no
successors for `u`, but `u` is enabled only at the first node. Ignoring
`D_u` makes them pass successor matching and falsely claims partial-domain
descent. This kills H4's unqualified formula for partial operations.

**CM5 (unrecorded choice input).** Two equal records can carry an extra
unrecorded bit supplied to a purported policy; choosing different actions
from that bit need not preserve BCS2/BCS4. Such a function is not a BCS-D3
history policy. Declaring the bit adds content; hiding it is a selector.

The executable `research/regression/control_branching_check.py` verifies
CM1–CM4 and the trace-filter identity without external dependencies. Result:
PASS under the installed Python. These are finite checks, not mechanized
proofs of the unbounded theorems above.


## 3. Definitions introduced

**DEF CPC1 (joint branch control).** Fix finite declared sets `O=C=U={0,1}`. A realization table `J subseteq O x C` is L0-presented optional L1 content; it lists a declared branch readout `o` and a continuation parameter `c`. Its marginal-forgetting map is `M(J)=(pr_O J,pr_C J)`. Given independently declared final readout `b(c,u)=1` iff `c=u`, a represented finite policy `pi:O->U` has terminal content `F_pi(J)={b(c,pi(o)):(o,c) in J}`. These are derived diagnostic functions, not core carriers, chance assignments, or a universal continuation domain. Equality on declared tables and output sets is the relevant equivalence. No member of `J` is selected.

**DEF CPC2 (protocol composition datum).** Let `E` be a derived empirical carrier, `tau:E->P` a surjection onto its declared active protocol image, `D subseteq E x E` the declared composition domain and `c:D->E` its descended concrete implementation. `D,c,tau` are independently declared/derived non-core L2 data. A protocol composition must respect `ker tau` in both arguments and output. A notation `P` never licenses operations absent from this datum.

**DEF CPC3 (agency interface).** A declared finite/generated policy carrier `Pi`, admissibility domain, record readouts and policy-execution graph constitute optional L1 content; their descended graph/readouts are L2 only after all required domain/value fibre tests. The word agency denotes this interface only if used at all. It introduces no subject, hidden selector, objective chance, primitive identity or order.

## 4. Results

**NO-GO CPC4 (H5, joint forgetting).** Terminal feedback content `F_pi` need not descend through `M`, even when all marginal sets and all fixed-control terminal sets agree. This proves insufficiency of this particular fibre-union/marginal reduct; it does not prove that every set-valued signature loses composition.

**THM CPC5 (exact protocol composition criterion; conditional).** Under CPC2, a unique partial operation `bar c:D_P->P` with exact pullback domain and value square

`D=(tau x tau)^(-1)(D_P)`, `bar c(tau g,tau f)=tau(c(g,f))`

exists iff (i) `D` is saturated under `ker tau x ker tau` and (ii) `tau c` is constant on each defined input fibre of `tau x tau`. Its domain is exactly `D_P=(tau x tau)(D)`. Neither empirical composition nor PF4 generator descent alone entails these two conditions. If the operation is required to output `E` instead of `P`, replace (ii) by constancy of `c` itself; that is a strictly stronger typing claim.

**PROP CPC6 (target-relative least sufficient record).** For any declared family of operations `F_j:S->Y_j`, the largest equivalence refining a given record kernel `ker r` and on which every `F_j` factors is `ker r intersect intersection_j ker F_j`. This is diagnostic only. Available record realization additionally requires the RR/CRS soundness-and-separation criterion. It need not preserve successor matching or any operation outside the declared family.

**NO-GO CPC7 (H8, agency decoration).** If a putative agency predicate varies while the complete declared protocol/policy/record/execution interface is fixed, it fails Q-descent. If it is only a new name for that interface, it adds no theorem-level result. No present record or continuation theorem derives an independent agency primitive.

**OPEN CPC8.** A policy quotient can support independently declared composition only after CPC5 applied to that composition graph. Control stability on an arrangement carrier alone is not congruence for composition on a distinct protocol/policy carrier. The particular bridges must be declared and audited. No generic bridge is derived here.

## 5. Proofs / proof sketches

CPC4: take `J_plus={(0,0),(1,1)}` and `J_minus={(0,1),(1,0)}`. Both have marginal reduct `({0,1},{0,1})`. For fixed `u=0` or `u=1`, both terminal content sets are `{0,1}`. For `pi(o)=o`, `F_pi(J_plus)={1}` and `F_pi(J_minus)={0}`. Thus `F_pi` varies in an `M` fibre: `NEW THEORY REQUIRED` relative to that reduct. All branch data remain finite, declared, and selector-free. If the repertoire already reads the full fixed-control transcript `(o,b)`, these two tables are distinguishable; this witness must not be promoted to a full-transcript open-loop equivalence result.

CPC5 necessity: the pullback domain is saturated; the value square forces fibre constancy. Sufficiency: set `bar c(p2,p1)=tau c(g,f)` for any representative pair in `D`. Saturation makes admissibility independent of the pair; constancy makes the value independent. Surjectivity of `tau x tau` onto its active pair image gives uniqueness. This is precisely T0.4/CP1 at the second quotient, not new quotient mathematics.

CPC6: any admissible equivalence identifies only pairs equal under `r` and all `F_j`, hence is contained in the displayed intersection. The intersection itself has all required equalities, so every target factors uniquely on its image. This is CRS1/2/5 generalized to a declared target family; it proves no availability.

CPC7: decorate one fixed finite CPC3 interface with either tag `a` or `b`. Forgetting the tag identifies the two extensions. A predicate assigning agency to only one extension violates frozen-core fibre invariance. If the predicate is interface-definable, it factors but contributes only a definitional reclassification.

## 6. Countermodels and failed routes

- Joint content removal: CPC4; full joint `J` is sufficient for its explicit relational policy evaluation, whereas its marginals are not.
- Domain removal from CPC5: `E={a,b}`, `tau(a)=tau(b)=p`, `D={(a,a)}`, `c(a,a)=a`. No protocol domain can have this exact pullback.
- Output constancy removal: `E={a,b,z}`, `tau(a)=tau(b)=p`, `tau(z)=q`, `D={a,b}²`; set `c(a,a)=z`, all other values `a`. Domain saturation holds, but one input protocol pair has outputs `q` and `p`.
- Compatibility only in the arrangement/control sort: take a singleton arrangement quotient with identity controls; separately use the preceding protocol-composition countermodel. All control maps descend, yet protocol composition does not.
- Availability removal from CPC6: `S={a,b}`, constant available record, target values `0,1`. The diagnostic partition is discrete; the available probe grammar contains no separator. Refinement is `NOT REALIZED`.
- Agency decoration removal: CPC7. No external agent, observer or ontic transformation is inferred.

Minimal sufficiency is target-relative: for this CPC4 witness the joint table suffices; in general a continuation behaviour quotient can be smaller than a complete branching realization, while bisimulation may be stronger than a particular terminal-policy observation quotient. No universal minimal branching object is asserted. Current CPG already contains joint slots and their multiplicities, and PF8 already retains joint weight/profile data; they do not supply an arbitrary continuation graph or feedback interpreter. SV/PR closure identities remain valid at their declared reduct.


## 3. Definitions introduced

**DEF CMQ1.** `H` is a declared typed L1 carrier of finite record encodings
(called histories only as module syntax), represented at L0. It has no
absolute temporal identity. `Π` is a declared set of compatible procedures;
each supplies a totalized functional content `b_π:H→Y_π+{⊥_π}`. Different
sorts are treated separately. A set-valued readout uses a declared powerset
as `Y_π`; may, must, winning and trace semantics must not be interchanged.
Undefinedness and inapplicability are distinguished from empty content.
These are non-core declared data, unique only relative to the chosen interface.

**DEF CMQ2.** `α_Π=∩_{π∈Π} ker b_π` and `q_Π:H→S_Π=H/α_Π`.
Type: derived unique L0 diagnostic quotient, up to quotient isomorphism;
dependencies CMQ1; it respects `α_Π`. It is an L2 empirical quotient only
if these procedures/readouts are actually available and have the declared
closure, or independently factor through the stated empirical quotient.

**DEF CMQ3.** A static record `m:H→M` is sufficient for Π iff each
`b_π=d_π m` for a function on `im m`. Record/procedure maps are L1 concrete
or derived L2 only after their own descent. `M` is non-core coding data;
no encoder or preferred code is inferred from existence of the quotient.

## 4. Results

**THM CMQ4 (exact static sufficiency).** Assume CMQ1–3. Then
`m` is sufficient iff `ker m⊆α_Π`, iff a unique surjection
`s:im m→S_Π` satisfies `q_Π=s m`. The quotient itself is sufficient and
is the coarsest sufficient equivalence. This is static operational
minimality, not automatically a recursively updatable controller state.

**PROP CMQ5 (capacity).** Under CMQ4, if `S_Π` is finite of size `n>0`,
any sufficient finite record image has at least `n` values. A fixed-length
binary encoding of that image requires `k≥ceil(log₂ n)` bits. The quotient
admits a mathematical encoding with equality, but no available implementation
is entailed. For arbitrary carriers the choice-free conclusion is the
surjection `im m↠S_Π`; standard infinite cardinal inequality uses the usual
set-theoretic choice convention. Infinite `S_Π` rules out finite `im m`.
No entropy, distribution or average variable-length bound follows.

**PROP CMQ6 (repertoire monotonicity).** For a declared inclusion
`Π₁⊆Π₂` with unchanged content semantics on the shared procedures,
`α_Π₂⊆α_Π₁` and the canonical map `S_Π₂↠S_Π₁` composes along
declared inclusions. Finite minimal static capacities cannot decrease.
An empty carrier has zero capacity classes and no `log₂ 0` bound is asserted.

**THM CMQ7 (recursive update boundary).** Given declared partial append
maps `a_v:D_v⊆H→H`, a deterministic update exists on `S_Π` exactly when
every `D_v` is `α_Π`-saturated and
`h α_Π h' ⇒ a_v(h) α_Π a_v(h')` on its domain. A sufficient condition
is that the declared readouts detect `D_v` and, for every π,v, the totalized
composite `b_π a_v` factors through the Π profile (e.g. it is already an
admissible residual readout). No such closure follows from CMQ4.
Set-valued append instead needs equality of successor-class images and
domain saturation; static kernel inclusion alone is insufficient.

**PROP CMQ8 (changing-carrier continuation interface).** Let two declared
profile maps `β:H→∏_πY_π^⊥` and `β':H'→∏_πY_π^⊥` have the same
image after explicit bijective policy/readout transport. Then their kernel
quotients are canonically isomorphic through that common image, even with
different raw cardinalities. Paired updates transport only with saturated
domains and commuting graph squares. Refinement transport also needs
compatible profile restriction squares. Q-verdict transport still needs CC4;
continuation profiles alone do not compare extension fibres.

**NO-GO CMQ9.** Static continuation sufficiency implies neither available
minimal records nor recursively updatable state nor stronger CC6 Q-status.

## 5. Proofs / proof sketches

CMQ4: factorization forces every equal-record pair to have equal procedure
contents. Conversely define `d_π(m(h))=b_π(h)` on the image; kernel inclusion
makes this independent of h. Define `s(m(h))=[h]_α`; the same argument
makes it well-defined and surjective, and surjectivity of m onto its image
gives uniqueness. No representative-selection function is constructed.
CMQ5 is the pigeonhole consequence of this surjection. CMQ6 is intersection
of additional kernels; coarse maps send a fine class to its containing class.
CMQ7 is T0.4 applied to the declared append graph. Its sufficient condition
preserves every coordinate of the profile. For set-valued append, apply T0.4
to the function sending h to the image of its successor set under q.
CMQ8 sends a class to its profile value; equality of profile images gives
bijective quotient comparison. Evaluate graph and restriction squares to
transport updates/refinement. CC4 remains independent, as CC-CM3 demonstrates.

## 6. Countermodels and failed routes

**CM CMQ-M1 (static state has no update).** `H={a,b,c}`, single readout
`b(a)=b(b)=0,b(c)=1`, total append `a_v(a)=a,a_v(b)=c,a_v(c)=c`.
CMQ4 gives two static classes, but update from class `{a,b}` is ambiguous.
If append's residual readout is available, including it refines the quotient;
it must not be silently inserted. This is T0-C1 specialized to histories.

**CM CMQ-M2 (domain).** Same readout, append defined only at a with output a.
Values agree on every common-domain equivalent pair, but domain is not
saturated. No quotient update exists.

**CM CMQ-M3 (infinite capacity).** `H=ℕ`, declared tests indexed by
`j∈ℕ` with `b_j(n)=1` iff `n=j`. Quotient is equality: no finite sufficient
record. The finite subrepertoire j<k instead yields k+1 classes. Arbitrary
declared size is allowed, without claiming all conceivable continuations.

**CM CMQ-M4 (insufficient record).** Two histories, test values 0 and 1,
constant record m. Any decoder gives the same value on both; sufficiency fails.

**CM CMQ-M5 (partial continuation).** One policy is defined at a and undefined
at b with the same defined-value convention. If comparisons ignore undefined
inputs, they can erroneously merge a,b. Totalization separates them.

**CM CMQ-M6 (changing-carrier failure).** H has profiles 0 and 1, H' only 0.
A collapsing map is not a common-profile interface. Conversely duplicating
each profile produces a different carrier with the same quotient. Unmatched
append graphs break operation transport even in that positive carrier case.

**CM CMQ-M7 (nondeterministic update).** In M1 replace append outputs by
singletons `{a}` and `{c}`. Set-valued terminology does not fix disagreement
of successor-class images. Taking the union over the class changes the raw
operation and is an enclosure, not its descent.

Each essential condition has a finite non-target failure model; M3 additionally
tests finite-to-infinite extrapolation. Larger policy families can demand
additional records; no lower bound is attributed to an intrinsic agent property.
