# Recognition Definability & Completion

## Scope

This is a metatheoretic L0/L3 recognition calculus over a fixed declared L2 signature. Its classes of representations and completions are mathematical comparison classes, not collections of physical continuations. It adds no L1/L2 primitive.

## 1. Recognition/reduct interface

**DEF RD1 (signature groupoid).** `S` is the declared groupoid of admissible L2 signatures and adequate signature isomorphisms. Fix `Sigma in S`. Its objects are only already descended carriers, operations, relations, and quantitative assignments.

**DEF RD2 (admissible representation groupoid).** `R` is a specified L3 groupoid of representations `(Sigma,X,iota)` with signature-preserving morphisms. The reduct functor is

`U:R -> S`, `U(Sigma,X,iota)=Sigma`.

The homotopy fibre `R_Sigma` has objects `(r,alpha:U(r) ~= Sigma)`. This formulation compares isomorphic reducts without choosing a representative.

**DEF RD3 (recognition datum and descent).** A candidate L3 datum is an isomorphism-invariant functor `D:R -> T` into a declared target groupoid `T`. It is defined by `Sigma` exactly when there is a functor `Dbar:S->T` and natural isomorphism

`D ~= Dbar o U`.

This global factorization is the full coherent descent condition. Constancy up to isomorphism on every homotopy fibre `R_Sigma` is necessary for it, but is not sufficient in general: fibrewise object values need not supply compatible action on morphisms or lifting coherence. Type: `Dbar` is L2 only when its value is a declared signature fact; otherwise this is an L3 diagnostic condition.

**CM RD3b (fibre invariance without coherent factorization).** Let `U:BC2 -> BC4` be induced by the inclusion of the order-two subgroup of the cyclic group `C4`, and let `D:BC2 -> BC2` be the identity group homomorphism. Every object value of `D` is the sole object of `BC2`, so the objectwise homotopy-fibre test is vacuous/constant. But a factorization through `BC4` would be a homomorphism `phi:C4->C2` whose restriction sends the subgroup generator `g^2` to the nontrivial element. This is impossible because `phi(g^2)=2phi(g)=0` in `C2`. Thus fibrewise object invariance alone does not yield `Dbar`; morphism coherence is indispensable. This is an L0 category-theoretic countermodel, not an L2 signature or a physical completion.

**PROP RD3c (one sufficient coherence interface).** If a declared section functor `s:S->R` and a declared natural isomorphism `epsilon:sU=>Id_R` are supplied, then every functor `D:R->T` factors coherently as `D ~= (D o s) o U`, via `D(epsilon)`. This is only a sufficient L0 comparison interface and is never selected or postulated by the frozen core.

**THM RD4 (Recognition-Q/descent theorem).** Under RD1–RD3, if `r1,r2` lie over isomorphic reducts and `D(r1)` and `D(r2)` are not isomorphic in `T`, then `D` does not descend to a fact of `Sigma`. In factorization form, no `Dbar` and natural isomorphism as in RD3 exist.

*Proof.* A factorization carries isomorphic reducts to isomorphic `Dbar` values, and naturality identifies these with `D(r1),D(r2)`. The displayed non-isomorphism contradicts this. Thus the datum varies inside one reduct fibre and is new content relative to the signature.

## 2. Completion over a partial barycentric sector

**DEF RD5 (pointed completion fibre and evaluation target).** Fix a partial rational barycentric L2 algebra `S`. `Comp_S` is the declared L0 groupoid whose objects are pairs `(C,j)` where `C` is a total rational barycentric algebra and `j:S->Red(C)` is an injective partial-algebra homomorphism preserving every *defined* operation of `S`; morphisms are total-algebra isomorphisms `h:C->C'` satisfying `h o j=j'`. Thus `Comp_S` is already the pointed/slice fibre over the fixed reduct `S`; no completion representative or embedding is selected.

For a missing typed triple `(x,y,r)`, the evaluation target `Val_S(x,y,r)` is the groupoid of triples `(C,j,v)` with `(C,j) in Comp_S` and `v=mix_r^C(jx,jy)`, with morphisms the pointed-over-`S` algebra isomorphisms that also carry `v` to `v'`. The evaluation functor is `Ev_(x,y,r):Comp_S->Val_S(x,y,r)`, `(C,j)|->(C,j,mix_r^C(jx,jy))`. These are L0/L3 comparison objects; `S` remains the fixed L2 reduct.

**THM RD6 (contrast-relative completion no-go; value-contrast criterion).** Fix a declared value contrast `D` on the pointed completion evaluations and its target comparison. Require an explicit interface showing that any proposed reduct-defined queried answer would induce a coherent factorization of `D` through the reduct. If two completions over the same reduct have non-isomorphic `D`-values, no such reduct-defined contrasted answer exists (RD4). Non-isomorphism of the ambient triples `(C,j,v)` alone establishes surplus of that full datum, not disagreement of the queried value. This supplies neither a missing concrete mixing procedure nor its availability.

The correct verdict is `NEW THEORY REQUIRED` for any proposal to add that value to the signature. Calling either choice a “mathematical completion” does not alter the descent failure.

*Proof.* The specified factorization interface makes the two `D`-values isomorphic if the queried answer is reduct-defined; their disagreement contradicts RD4. Constancy of `v` does not imply constancy of the entire `(C,j,v)` datum. **CM:** endpoint-only `S={a,b}` has two- and three-element chain meet completions with different ambient sizes but identical strict `mix(a,b)=j(a)`; the self-mix `mix(a,a)=j(a)` is fixed in every total barycentric completion by idempotence. Thus ambient evaluation non-isomorphism is too strong a test for value ambiguity. See `QUESTION_DEFINABILITY.md` for the full contrast argument; no converse to RD4 is used.

**CM RD7 (two completions).** Let partial `S={a,b}` have only endpoint operations. Completion `C_join` defines every strict rational mix as `join`; completion `C_meet` defines every strict rational mix as `meet` on the two-element chain `a<b`. Both preserve the endpoint reduct, but

`mix_(1/2)^C_join(a,b)=b`, while `mix_(1/2)^C_meet(a,b)=a`.

The declared named-value contrast distinguishes `j(a)` from `j(b)` over `S`, so contrast-relative RD6 applies. Ambient non-isomorphism alone is not the reason.

## 3. Generated-core normalization and rigidity

**DEF RD8 (generated representation core).** For a representation `(Sigma,X,iota)` in a class with a specified closure operation, `Core(r)` is the smallest declared L3 subrepresentation containing `iota(Sigma)` and closed under the representation operations required by the class. `N:R->R_core`, `N(r)=Core(r)`, is normalization. Ambient data outside `Core(r)` are decorative extension data.

**DEF RD9 (core surplus and rigidity).** A datum is decorative surplus if it changes before normalization but not in `R_core`. It is core surplus if it changes between two normalized objects in `R_Sigma` and fails RD3. A representation class is rigid over `Sigma` when its normalized fibre is contractible: it is nonempty and any two cores have a unique isomorphism over `Sigma`.

**PROP RD10 (normalization test).** Singleton point representations in an affine line and affine plane have different ambient dimensions but isomorphic zero-dimensional generated cores; this is decorative, not core, surplus. Conversely, a bare three-point L2 carrier represented as three collinear affine points and as three affinely independent affine points has non-isomorphic generated affine cores. Affine dimension is then genuine core surplus because the bare reduct does not determine it.

**THM RD11 (positive rigid example).** Let `I_Q=Q cap [0,1]` carry all standard rational barycentric operations. In the category of faithful rational-affine representations generated by the image, `I_Q` is rigid over its L2 algebra: every representation is determined by the distinct images of `0,1`, and every rational `t` is their declared mixture. The unique affine map carrying the two endpoint images to the two endpoint images intertwines the full image and its generated affine core.

This is an example only. The current predictive sector is partial and has not established the totality, cancellation, or separation needed to instantiate RD11.

## 4. Recognition distinction

**REC RD12 (four-way criterion).**

`representation exists != representation is faithful != representation is rigid != its extra data are facts of Sigma_R`.

Existence concerns nonemptiness of `R_Sigma`; faithfulness is a specified reflection condition; rigidity is RD9; L2 facthood is RD3/RD4. Each requires its own proof. Failure at any stage cannot be repaired by adding the desired L3 datum as an L2 premise.

## Audits

Q-audit: RD4 is the reduct-fibre form of Q-exclusion. RD6 explicitly returns `NEW THEORY REQUIRED` rather than a selected completion. Presentation audit: all comparisons occur in homotopy fibres over adequate signature isomorphism; no representative is chosen. Circularity audit: `R` consumes `Sigma` and has no defining edge back into it. Dependency impact: no frozen-core change.
