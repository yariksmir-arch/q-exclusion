# Articulation / information / record interface — optional integration note

Status: `STANDARD_REPACKAGING_WITH_SCOPED_ACCESS_INTERFACE`. This is one
integration note, not three new theory modules. No frozen assumption changes.
The arguments and failure cases are below; see ARTICULATION_MODEL_ZOO.md.

## Declared types and boundary

**DEF AI-D1.** X is a finite declared structural/discriminability carrier,
represented at L0; never raw phenomenality. A:X→Z and a finite family
F_i:X→Y_i are total functional maps on the stated support, with explicit
failure tags when totalizing declared partial procedures. Coding alphabets
are chosen interface data. Concrete procedures are L1; their maps are L2
only after the raw input/output empirical descent squares. Maps here are
otherwise L0 diagnostics, not automatically available records. Kernels and
quotients are unique relative to these inputs, up to adequate transport.
Dependencies include target semantics, generated support and actual grammar.
If X itself is an empirical quotient, representatives must give well-defined
A and F_i on it. No carrier or target repertoire is inferred from interpretation.

## Static and operational sufficiency

**PROP AI1 — standard image factorization.** For AI-D1,
F=d∘A with d:im A→Y iff ker A⊆ker F. The factor is unique on im A;
no extension over unused Z labels is asserted. Define
theta_F=⋂_i ker F_i and q_F:X→X/theta_F. A preserves every F_i iff
q_F=s∘A for a unique surjection s:im A→X/theta_F.
Thus q_F is coarsest static sufficient articulation. For a refinement of an
existing A, the diagnostic minimum is ker A∩theta_F instead.

Proof: equal A-values must have equal target-values; conversely each image
value has a unique common target tuple/class. Surjectivity gives uniqueness,
without a selected representative function. This is T0.3, CRS1/2/5, CMQ4.

**PROP AI2 — standard kernel order.** For declared B:Z→W,
ker A⊆ker(B∘A). A target failing AI1 cannot be recovered by downstream
forgetting. An independently available, jointly executable descended probe
H:X→O gives ker(A,H)=ker A∩ker H. Restoration uses new access, not inversion
of A. Increasing a fixed-semantics target family refines theta_F (CMQ6).
Bijective A preserves every target; articulation need not be lossy.
Support expansion requires a new kernel test on the expanded support/union
(CRS10); local factors need not agree on overlapping record images.

**PROP AI3 — existing operational universal property.** For explicitly
declared finite-arity partial operations and Boolean relations K, with T0.5
strong stability (domains saturated, outputs class-invariant, relations
product-fibre invariant), C_K(theta_F) is the greatest K-stable equivalence
below theta_F. Any statically sufficient K-stable record kernel lies below
it, hence its image maps onto this operational quotient. The quotient is
mathematical, not an implemented record. If A must also be preserved, use
C_K(ker A∩theta_F). This is T0.5 plus CMQ4, not a new universal property.

Available realization still requires RR4–7/CRS7 sound separating probes and
their actual closure. Recursive deterministic updates additionally need
CMQ7 domain saturation and record-output invariance. Branching successor
class-image descent and trace sufficiency differ (BCS3/5); unrelated protocol
composition still requires CPC5. Static sufficiency implies none of these.

## Optional probability interface

**DEF AI-D2.** Independently declare a probability assignment p:X→[0,1],
sum p=1, on nonempty finite X. S=supp p. It is optional quantitative
interface data (L1 assignment, L2 only with its own descended interface;
otherwise an L3/L0 representation). It is not derived from frequencies.
Transport includes pushforward of p. Entropies below use base-2 logarithms.

**PROP AI4 — standard finite conditional entropy.**
H_p(F(X)|A(X))=0 iff ker(A|S)⊆ker(F|S).
If S=X this is AI1. Structural factorization on X is equivalent to zero
conditional entropy for every p on X, and equivalently for any one fixed
full-support p. A conflicting pair can be assigned positive masses to refute
the universal claim. Conditional entropy is a positive weighted sum of fibre
entropies; each is zero exactly for a point-mass target distribution.

For W=B(A(X)), H_p(F|W)≥H_p(F|A); for Z+=(A(X),H(X)),
H_p(F|Z+)≤H_p(F|A). Conditional entropy chain rule/nonnegativity proves
both. Equality in the first means conditional independence of F and A given
W on this p-support; it need not mean that A itself is recoverable from W.

**PROP AI5 — fibre-size bound.**
H_p(X|A(X))≤Σ_z p(A=z) log₂|A⁻¹(z)∩S|.
Equality iff p conditioned on every positive-mass A-fibre is uniform.
For uniform p on X equality holds, giving expected log fibre cardinality.
Proof: entropy of a distribution on n points is at most log₂n, with equality
exactly at uniformity (nonnegative divergence from the uniform distribution).
Zero-mass fibres contribute nothing; no log of an empty fibre is used.

**DEF AI-D3 — optional relevance weighting.**
L_F^p(A)=(H_p(F_i|A))_i for the fixed declared targets. This vector depends
on p, support and targets. It is not absolute semantic loss or a measure of
the Boundary Problem. It adds quantitative weighting, not new structural
distinctions; the weights themselves are additional declared content.

“Q-descent = distribution-free zero-error sufficiency” is exact only as a
description of factorization along the **specified set-level forgetful map U**:
take A=U, F total with equality as the target comparison, finite nonempty
extension carrier for AI4, and all extensions in the tested carrier. It is
not an identity between Q-exclusion and generic Statistical/Structural
Sufficiency. Groupoid/morphism coherence (RD3b), partial domains and quotient
target equality require their original separate tests. A different A or
restricted positive support changes the question. Descent failure means
additional content required, not nonexistence of F.

## Retained source and controller accessibility

**DEF AI-D4.** Declare a finite L1 record-writing interface with generation,
readout, explicit controller input ports and actual downstream composition
grammar. A retained-source implementation w:X→X×Z has w(x)=(x,A(x)) on its
declared domain. This product represents named subsystem ports of one finite
procedure diagram, not a global world carrier. Non-destructive source
retention is an assumption of this implementation, not a consequence of A.

**PROP AI6 — standard retained-source identity.** w is injective, with source
projection π_Xw=id_X. The record projection π_Zw=A can be lossy while w
is injective. On optional p, H_p(w(X))=H_p(X). No physical destruction,
reversibility of the writer, thermodynamic conclusion or available inverse
procedure follows merely from this mathematical identity.

**PROP AI7 — scoped access criterion.** Fix explicitly declared controller
grammars G₀⊆G₁, and let D_G be their actually executable, record-only
decoders d:im A→Y. A deterministic record-only controller can realize F
exactly when some d∈D_G satisfies d∘A=F. In particular ker A⊆ker F is
necessary; it is sufficient only when the unique image factor is available
with its required routing/composition. Every such output is constant on
ker A. Suppose G₀ has no route realizing F, and G₁ independently supplies
write/read/decoder composition realizing that factor. Then F gains controller
accessibility. Along the retained-source graph, exact-data distinctions have
not increased (AI6). The route is new interface content, not a fact recovered
from the old availability-forgetting reduct. This is a useful architecture
check, but standard factorization plus explicit reachability, not novel theory.

For an **empirical** no-gain statement, fix the complete old contextual source
profile s:X→V whose kernel defines the old empirical equivalence, retain all
old readouts, and include all new complete contextual probes P'. The source
quotient remains unchanged iff each P' is ker s-constant. In particular adding A alone requires
ker s⊆ker A. Sound seeds are insufficient if their actual closure splits a
class. This is RR/T0 quotient-versus-signature separation. Exact injectivity
of w does not by itself establish empirical no-gain. Operational signature,
routes or costs can change despite equal quotient carriers.

Combined access (A,H) preserves parallel distinctions only when its probes and
joint readout are concretely available and descend. Reuse/update still needs
CMQ7; nondeterministic policies retain BCS codomain distinctions. Self,
subject, agency, inner speech and consciousness supply no theorem here.
An inner-speech reading is only a later interpretive hypothesis.

## Attacks and admission

Countermodels: equal-size bit partitions have equal H(X|A) and incompatible
preserved targets; p=(1,0) hides F=(0,1) behind constant A; changing p changes
entropy without changing ker A; one-point support factors cease factoring on
expansion; a three-point sufficient static record has inconsistent update or
unsaturated domain; an unavailable separator/decoder exists mathematically;
sound added seeds can have unsound closure; unary stability does not preserve
an independent binary operation. See ARTICULATION_MODEL_ZOO.md.

All formulas transport under adequate carrier/label/support/target/operation/
grammar comparison, with probability transported where used. No natural
articulation, canonical encoder, selector, final target family, probability,
primitive chronology, bearer or phenomenality is reconstructed. Initial
boundary/repertoire remains input. General/infinite entropy statements are
not claimed. No theorem-level novelty or core-change necessity is established.
