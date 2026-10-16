# Presentation and changing-carrier transport

Existing conditional results in known quotient mathematics. Comparisons are L0 data; they introduce no process unless separately represented.

## 3. Definitions introduced

**DEF PI1 (operational presentation).**  An *operational presentation* is the L0 tuple

`P=(S,(A_s),Omega,(D_omega), C, (V_c), (hat c))`,

where `S`, `A`, and the typed partial operations are as in the declared typed partial-algebra data in INTEGRATED_THEORY.md, `C=C_R` is the declared sort-indexed contextual closure, and every `hat c:A_s -> V_c + {bot}` is a totalized functional observation as in the declared-data paragraph of INTEGRATED_THEORY.md.  Its L1 declared content is written `B_P`; its derived L2 objects are `E_P=E_R` and `Sigma_P=Sigma_R`.  Type: L0 finite or infinite typed data; dependencies: frozen-core §§3–8 and the typed partial-algebra data in INTEGRATED_THEORY.md, T0.2/T0.4; status: derived formalization, not core; unique only up to adequate transport below; equivalence respected: `~_R`.

**DEF PI2 (strict adequate presentation isomorphism).**  A strict adequate isomorphism `T:P -> P'` consists of:

1. a sort bijection `sigma:S -> S'` and carrier bijections `t_s:A_s -> A'_{sigma(s)}`;
2. a bijection `j:C -> C'` preserving source sorts, together with bijections `ell_c:V_c -> V'_{j(c)}` satisfying, for every `a in A_s`,

   `hat{j(c)}'(t_s(a)) = ell_c^bot(hat c(a))`,

   where `ell_c^bot` extends `ell_c` and fixes `bot`;
3. a bijection between the *declared* partial-operation symbols, preserving arity and output sort, for which operation domains and values commute with the carrier bijections; and
4. preservation of the declared closure rule: `j` takes exactly the tests generated from the transported seed repertoire by the transported listed compositions to `C'`.  It neither imports ambient arrows nor deletes generated tests.

This is L0 metatheoretic comparison data, not a process in `B_P`.  Dependencies: PI1.  Status: diagnostic/derived.  It is chosen, not canonical.  Clause 2 respects observational equality; clause 3 respects typed operation graphs.

**DEF PI3 (transport).**  For `T` in PI2, transport sends an arrangement `a` to `T_A(a)=t_s(a)`, a seed repertoire and its closure to their images under `j`, a context/readout pair `(c,hat c)` to `(j(c),hat{j(c)}')`, and a partial operation `omega` to the operation specified by PI2(3).  A concrete `n`-ary relation or operation is transported by conjugating its graph with the appropriate `t_s`.  A candidate fact is transported only when its target carries a specified bijection `eta:Y -> Y'`, in the formula `F'=eta o F o (T^+)^{-1}` below.  Type: L0 maps between the displayed typed data; dependencies: PI2; status: derived.  The transport is defined only for declared data; there is no transport of an unspecified “all contexts” family.

**DEF PI4 (adequate extension transport).**  Let `U:B_{P+}->B_P` and `U':B_{P'+}->B_{P'}` be forgetful maps.  An adequate extension transport over `T` is a fiber-bijective map of the explicitly declared extension data `T^+:B_{P+}->B_{P'+}` such that

`U' o T^+ = T_B o U`,

where `T_B` is the L1 transport induced by PI2, and such that extensions in a fiber of `U` are carried bijectively to the corresponding fiber of `U'`.  Type: L0 comparison datum for two *declared* extension families; dependencies: PI2 and specified `U,U'`; status: diagnostic.  It respects the equality relation in each forgetful fiber.  A categorical variant must supply a quasi-inverse and commuting natural isomorphisms that induce this fiber-bijective comparison.  This definition deliberately does not quantify over a universal class of extensions.

**DEF PI5 (signature transport and empirical equivalence).**  The induced quotient carrier map is

`bar t_s:E_{P,s}->E_{P',sigma(s)},   bar t_s([a]_R)=[t_s(a)]_{R'}`.

The signature transport `bar T:Sigma_P -> Sigma_P'` consists of these maps and the conjugates of exactly the operations and relations that descend at `R`; a quantitative assignment is included only with a specified transport isomorphism of its declared codomain.  Two presentations are *empirically equivalent at their transported repertoires*, written `P ≃emp P'`, when such a signature isomorphism exists.  Type: L2 sorted isomorphism; dependencies: PI2 and descent; status: derived.  It respects all and only declared L2 structure.

**DEF PI6 (transport-compatible refinement).**  Given `C_R subseteq C_{R+}` and `C'_{R'} subseteq C'_{R+'}`, a pair of strict adequate isomorphisms is refinement-compatible when it uses the same sort and carrier bijections at the coarse and fine levels, and its context bijections and readout-codomain transports restrict from the fine closures to the coarse closures. These are explicit sufficient compatibility data; context restriction alone does not suffice (CM PI4 below).  Type: L0 predicate; dependencies: PI2 and frozen-core §7; status: diagnostic.  It respects `~_{R+} subseteq ~_R` and its transported counterpart.

## 4. Results

**THM T1.1 (presentation-equivalence transport).**  Assume PI1–PI3 and a strict adequate presentation isomorphism `T:P -> P'`.  Then, for every sort `s` and `a,b in A_s`,

`a ~_R b  iff  t_s(a) ~_{R'} t_s(b)`.

The maps `bar t_s` of PI5 are consequently well-defined sorted bijections.  A declared partial operation/relation is `R`-compatible (hence descends by T0.2/T0.4) iff its transport is `R'`-compatible.  Thus arrangements, repertoires, closure contexts, readouts, candidate concrete operations, and every descended operation transport without selecting representatives.

**THM T1.2 (Q-status invariance).**  Assume T1.1; forgetful maps `U,U'`; adequate extension transport PI4; and candidate facts related by `F'=eta o F o (T^+)^{-1}`, with `eta` bijective.  Then

`F factors through U  iff  F' factors through U'`.

Hence the verdicts `ADMISSIBLE RELATIVE TO THE BASE` and `NEW THEORY REQUIRED` are invariant under this adequate transport.  This theorem concerns Q-descent along stated forgetful maps, not merely descent to `E_R`.

**THM T1.3 (quotient, signature, and refinement invariance).**  Assume T1.1 and, for each quantitative assignment being compared, a specified isomorphism of its declared codomain.  Then `bar T` is an isomorphism of the empirical signatures: it transports each and only each L2 relation, operation, and such quantitative assignment satisfying the empirical-descent condition.  If, additionally, PI6 holds, then

`bar t_R o pi_{R+ R} = pi_{R+' R'} o bar t_{R+}`.

Therefore the quotient/signature and every declared refinement map are invariant up to this commuting L2 isomorphism.  No claim is made about refinements whose arrangements, closure rule, or transport map have not been declared.

**PROP PI7 (strength of comparison required).**

| Comparison at L0 | Sufficient conclusions | Insufficient without extra data |
| --- | --- | --- |
| Strict adequate isomorphism PI2 | T1.1 and the signature part of T1.3, with declared quantitative target transports | T1.2 additionally requires PI4 and transported candidate facts; the refinement square additionally requires PI6 |
| Concrete equivalence of presentation categories | T1.1 and signature transport if it supplies quasi-inverse concrete comparisons satisfying PI2; Q-status additionally needs PI4, and refinement needs PI6 | An abstract categorical equivalence alone, or concrete equivalence without the corresponding extension/refinement data |
| Morita-like equivalence | Signature equivalence only if it identifies the designated concrete-arrangement, context/readout, and descended-operation functors (and is refinement-compatible for maps) | Q-status, or concrete-operation descent, from equivalence of model categories alone |
| Weak observational equivalence `Sigma_P ≅ Sigma_P'` | Equality of already formed empirical predictions/relations expressed wholly in the displayed signatures | Transport of raw arrangements/contexts, empirical-descent verdicts for new concrete operations, Q-status, or refinement maps |

Here “concrete” means relative to the declared carriers and readout-evaluation functors, not an assertion that those carriers are ontology.  In particular, equivalence of abstract categories can add/remove a syntactically available arrow whose evaluation is not controlled; it does not meet PI2 by itself.

**NO-GO PI8 (syntax-relative selector).**  A selector that is definable only from presentation names, an external enumeration, or undeclared ambient structure is neither an L2 operation nor a presentation-independent candidate fact.  It may be introduced only as new declared content, in which case its Q-status must be tested against the forgetful map deleting that content.

## 5. Proofs / proof sketches

**Proof of T1.1.**  Let `c` have source `s`.  PI2(2) gives equality of `hat c(a)` and `hat c(b)` iff equality of the transported totalized observations on `t_s(a),t_s(b)`, because `ell_c^bot` is bijective.  Taking the intersection over `C_R`, and using PI2(4) to identify this family exactly with `C_{R'}`, proves the equivalence claim.  It makes `bar t_s` well-defined; its inverse is induced by `t_s^{-1}`.

For a partial operation, PI2(3) identifies corresponding input tuples, domains, and output classes.  The two clauses of partial-operation descent in INTEGRATED_THEORY.md (domain saturation and output fiber constancy) are therefore equivalent before and after transport.  The same tuplewise argument proves invariance of relation descent.  The descended squares commute by construction, so no class representative is chosen.

**Proof of T1.2.**  Suppose `F=Fbar o U`.  Define

`Fbar' = eta o Fbar o T_B^{-1}`.

The PI4 square gives `F'=Fbar' o U'`.  Conversely apply the same argument to the inverse extension transport and `eta^{-1}`.  Equivalently, PI4 maps every fiber pair of `U` bijectively to a fiber pair of `U'`; the fiber-constancy Q test has the same truth value.  The assumptions are necessary in role: without a lift over the forgetful maps, the compared fibers need not correspond.

**Proof of T1.3.**  T1.1 supplies carrier bijections on the quotients.  Its operation/relation conclusion says precisely that every structure admitted into `Sigma_R` has one and only one conjugate admitted into `Sigma_{R'}`; inverses give fullness in the displayed signature language.  For refinement, evaluate both sides on `[a]_{R+}`.  The left side is `[t(a)]_{R'}`; the right side is also `[t(a)]_{R'}`.  PI6 supplies one common carrier map t at both levels, as well as the restricting context/readout transports. Thus both displayed values use the same t(a), and both quotient maps are defined. Separate carrier maps cannot be substituted merely because their context-name bijections restrict.

**Proof of PI7.**  PI2 gives T1.1 and signature transport with the stated target transports. T1.2 also needs PI4 and the candidate-fact square; refinement in T1.3 also needs PI6. For example, identical base presentations can have respectively two extensions with candidate values 0,1 and one extension with value 0. Their Q verdicts differ; a base isomorphism alone supplies no extension comparison.  A concrete category equivalence satisfying the stated carrier/readout conditions yields PI2 after choosing its concrete comparison maps.  A Morita-like equivalence that identifies only model categories need not identify evaluation at a declared context, so it cannot prove the fiber-constancy assertions in T1.1 or the extension-fiber assertion in T1.2.  Finally an L2 signature isomorphism begins after quotienting, so it lacks the data to reconstruct a raw operation or a refinement quotient map.

## 6. Countermodels and failed routes

**CM PI1 (spurious numeral selector).**  Let `P` have one arrangement sort `A={a,b}`, no declared operations, and one constant total test `c(a)=c(b)=*`.  Thus `a~_R b` and `E_R` has one class.  Present the same bare two-point carrier as `P'` with names `{0,1}` and the same constant test.  The L0 expression “choose the least numeral” returns `0`.  Relabeling by the bijection `0 <-> 1` is an adequate presentation isomorphism of the declared data, but it carries the proposed selected element to `1`, whereas applying the numeral rule again returns `0`.  Thus the selector is not transported by PI3.  This is a failure of transport-naturality, not nonexistence of a set-theoretic section: q:{0,1}-> {*} has sections s(*)=0 and s(*)=1. Either uses an externally chosen representative and neither commutes with the swap. A constant chosen representative can factor as a raw set map; factorization alone does not make that choice canonical or supply it as declared empirical content.  This is a direct counterexample to “definable in one encoding implies an empirical fact.”

If an order `0<1` is instead declared in `B_{P'}`, it is new content, so `P` and the ordered `P'` fail PI2(3).  Let `U` forget the order.  The two order extensions `0<1` and `1<0` have the same image under `U` but opposite least-element selectors.  The selector fails Q-descent and is **NEW THEORY REQUIRED** relative to the unordered base.

**CM PI2 (abstract equivalence without readout adequacy).**  Take two one-object abstract categories equivalent as categories, and equip their concrete presentations with carrier `{0,1}`.  In the first, the only declared readout is constant; in the second, a designated readout is the identity.  The underlying one-object categories can be equivalent after forgetting designated evaluations, yet their empirical quotients have respectively one and two classes.  Hence abstract category equivalence without PI2(2) and PI2(4) does not prove T1.3.

**CM PI3 (signature equivalence cannot transport a raw operation).**  Let `A={0,1}` with a constant repertoire, so `E_R` is singleton.  Compare a presentation with no operation and one declaring only the partial unary operation f:{0}->{0,1}, f(0)=0, undefined at 1. In both presentations the declared test closure contains only the constant observation: no plug-in of f or definedness test is supplied. The domain {0} is not saturated under the single empirical class, so f does not descend and both empirical signatures have the same singleton carrier and no operation. Their raw operation availability nevertheless differs. By contrast, the total identity on {0,1} always descends and would add an operation symbol; it cannot witness equality of the full empty-operation signature.  A weak signature comparison cannot decide whether a proposed later concrete operation is available, or whether a new repertoire makes it descend.  It therefore cannot establish T1.1 or T1.2.

**CM PI4 (context restriction without common carrier transport).** Let A=A'={0,1}, with no operations. The coarse closure has c(x)=x and the fine closure has c(x)=x,d(x)=x; no other compositions are declared. Both quotients are discrete and each refinement map is the identity. Choose the coarse carrier/readout transports as identity, and the fine carrier transport x|->1-x with the same swap on both readout alphabets. Each level separately satisfies PI2, and both context-name bijections are identities and restrict. Yet on [0] the proposed T1.3 square has values [0] and [1]. The missing common carrier transport is therefore substantive. Requiring the same carrier map as in PI6 makes the square commute; this is an L0 compatibility condition, not additional ontology.

**Failed route.**  Replacing PI2(4) by closure under every morphism of an ambient category makes the result depend on the ambient syntax and violates frozen-core §4.  It also converts a missing test into hidden content rather than proving an invariant fact.

## 7. Q-audit

- PI1–PI3 are metatheoretic comparison data.  They do not state an old-theory fact about arbitrary extensions and do not select an arrangement or quotient representative.
- T1.2 explicitly tests Q-descent fiberwise.  PI4 is the sufficient condition that identifies the fibers being compared.  If an alleged correspondence of extensions does not commute with `U`, no invariance conclusion follows; the candidate is assessed separately in its own base theory.
- T1.1/T1.3 use only transported declared carriers, operation graphs, closure contexts, and readout equality.  Added test symbols or added orders may change the result only by changing the declared base; CM PI1 shows the appropriate verdict is **NEW THEORY REQUIRED**, not a hidden invariant.
- A descended operation is transported only after T0.2/T0.4 domain saturation and output fiber constancy.  When that condition fails in either presentation, it is **NOT DEFINED AT THIS QUOTIENT** in both under T1.1.

Q-audit status: PASS under the stated hypotheses; no untested selector or extension family is used.

## 8. Presentation-invariance audit

T1.1 re-expresses the INTEGRATED_THEORY.md quotient construction in arbitrary transported typed partial-algebra presentations.  CM PI2 separately tests the category language and identifies the extra concrete-evaluation data it must carry.  The invariant is not syntax, carrier names, factorization spelling, or an ambient-category arrow set; it is the transported family of totalized observations, declared operation graphs, and declared closure generation.

The symbols `T`, `bar T`, and categorical equivalences are L0 comparison maps.  They are not asserted to be transformations/processes in `B_P`.  There is no canonical isomorphism or representative: every theorem is relative to a supplied adequate transport, and changing it may change a syntactic selector while leaving `Sigma_R` unchanged.

Audit status: PASS for strict adequate transports; deliberately NOT CLAIMED for weaker comparisons listed in PI7.


## 3. Definitions introduced

**DEF CC1 (common quotient interface).** Let presentations have typed carriers `A,A'` and repertoires `R,R'`. A common quotient interface is a typed set `E` with surjections `u:A->E`, `u':A'->E` satisfying `ker(u)=~_R` and `ker(u')=~_R'`. Type: L0 comparison datum presenting L2 `E`; dependencies declared repertoires; chosen, not canonical; respects both empirical equivalences. It need not relate individual representatives.

**DEF CC2 (readout adequacy).** CC1 is readout-adequate if every declared closure observation on either carrier factors through its corresponding map to `E`, and the two resulting declared readout families are identified by specified readout transports. Type: L0 predicate; diagnostic; no ambient tests are added.

**DEF CC3 (operation compatibility).** Declared partial operations `f` on `A` and `f'` on `A'` are compatible over `E` when their saturated domains correspond through `u,u'` and there is one partial operation `f_E` on `E` with `u∘f=f_E∘u` and `u'∘f'=f_E∘u'` on domains. Type: L0/L2 comparison predicate; it respects quotient fibres; it is not assumed for unpaired operations.

**DEF CC4 (extension-fibre transport).** For stated forgetful maps `U:B_+->B`, `U':B'_+->B'`, an adequate changing-carrier extension comparison is a pair of base transports through CC1 and a bijection between each corresponding declared extension fibre, commuting with the common quotient interface. Type: L0 diagnostic; it concerns only stated extension families.

## 4. Results

**THM CC5 (changing-carrier quotient/signature invariance).** Under CC1–CC2, the maps induced by `u,u'` give canonical isomorphisms `E_R≈E≈E_R'`; with CC3 they transport exactly the paired descended operations, relations, and quantitative assignments. Hence the corresponding signatures are isomorphic without a bijection `A≈A'`.

**THM CC6 (Q-status invariance with changing carriers).** Under CC5 and CC4, a transported candidate fact factors through `U` iff its counterpart factors through `U'`. Thus `NEW THEORY REQUIRED` is invariant for the stated extension comparison.

**PROP CC7 (refinement transport).** If coarse and fine common quotient interfaces share compatible maps `E_fine->E_coarse`, then the two presentation refinement maps commute through them. No conclusion is available when only carrier maps, but no common quotient maps, are supplied.

## 5. Proofs / proof sketches

`ker(u)=~_R` makes `[a]↦u(a)` a well-defined bijection `E_R->E`; similarly for `A'`. CC2 transports the readout-defined signature data. CC3 states exactly the two descent squares through the same `f_E`, so paired descended structures coincide. CC4 identifies the fibres tested in the Q criterion; fibre constancy is therefore equivalent. CC7 follows by evaluating each composite on a representative and using the common quotient maps.

## 6. Countermodels and failed routes

**CM CC1 (carrier collapse without quotient adequacy).** Let `A={a,b}` with identity readout, while `A'={*}` has only a constant readout. A relation may send both `a,b` to `*`, but no common `E` has the required kernels (two quotient classes versus one). A non-bijective carrier map alone is insufficient.

**CM CC2 (same quotient, unmatched operation).** Two presentations may have the same singleton quotient while only one declares a concrete operation. CC1 does not transport availability of that operation; CC3 is necessary.

**CM CC3 (unmatched extension fibres).** If one base has two stated extensions with different candidate-fact values and the other has only one, a quotient comparison cannot establish Q-status invariance. CC4 is necessary.

**Failed route.** Choosing a representative section of `u` or `u'` to compare operations is a privileged selector and fails the Q/presentation audits.

## 7. Q-audit

CC1 compares quotient fibres only; it selects no representative. CC4 is explicitly the fibre condition required for Q-exclusion. CM CC3 blocks an unsupported Q comparison. Any extra carrier distinction absent from `u` can vary in a forgetful fibre and is representational surplus unless separately descended.

## 8. Presentation-invariance audit

This is the changing-carrier version of T1.1–T1.3. It is strictly stronger in scope than carrier bijection transport but stronger in hypotheses than weak observational equivalence: explicit common quotient/readout/operation/extension data remain required.
