# Predictive Certification Finalization


## Scope

This is a derived L2 calculus for declared protocol fibres, realized generation, joint asymptotics, aggregation, and transport. Its exact domain and joint-image requirements take precedence over less qualified summaries.

## 1. Common topological lemma

**LEMMA PF1 (continuous image of tail-cluster content).** Let `X` be compact, `Y` Hausdorff, `f:X->Y` continuous, `I` directed, and `x:I->X`. Then

`Cl_I(f∘x)=f(Cl_I(x))`.

*Proof.* Write `C_i=closure(x(I_{>=i}))`. If `a` belongs to every `C_i`, continuity gives `f(a) in closure(f(x(I_{>=i})))` for every `i`; hence `f(Cl_I(x)) subseteq Cl_I(f∘x)`.

Conversely, take `y in Cl_I(f∘x)`. Since `f(X)` is compact and therefore closed in Hausdorff `Y`, `y` lies in the compact Hausdorff subspace `f(X)`. In that subspace, the closed sets `C_i` together with `f^{-1}(closure(U))`, for every open neighbourhood `U` of `y`, have the finite-intersection property: for finitely many neighbourhoods replace them by their intersection, and use that `y` lies in the closure of the corresponding image tail. Compactness gives `a` in their intersection. Thus `a in Cl_I(x)`, while `f(a)` belongs to the closure of every neighbourhood of `y` in the compact Hausdorff space `f(X)`. Its regularity makes that intersection `{y}`, so `f(a)=y`. Therefore `Cl_I(f∘x) subseteq f(Cl_I(x))`.

**THM PF2 (polished PC3).** With PC1–PC2, `Cl_I(x)` is the unique least closed neighbourhood-asymptotic enclosure, is nonempty compact, and is singleton exactly when `x` converges. It does not generally contain a tail.

*Proof.* Put `C_i=closure(x(I_{>=i}))`. The nonempty closed family `(C_i)` is decreasing, so compactness gives nonempty compact `C=intersection_i C_i`. If an open `U` contains `C` but no tail is contained in `U`, then every `C_i` meets the closed set `V\U`; compactness gives a point in `C∩(V\U)`, contradiction. Hence `C` is an asymptotic enclosure.

If a closed asymptotic enclosure `D` omitted `y in C`, compact Hausdorff regularity gives an open `U` with `D subseteq U` and `y notin closure(U)`. Eventual membership in `U` would put some tail closure inside `closure(U)`, contradicting `y in C`. Hence `C subseteq D`, proving leastness. If `C={v}`, the enclosure condition is exactly convergence to `v`. Conversely, a convergent net has no cluster point other than its Hausdorff-unique limit. CM PC4 remains the required failure case when “neighbourhood-asymptotic” is replaced by tail containment.

## 2. Protocol-level generation descent

**DEF PF3 (two-stage generation typing).** Let `q:X->E` be an empirical quotient and let `tau:E->P0` be a descended protocol map onto its declared **active** protocol carrier `P0=im(tau)`; this restriction excludes uninstantiated raw labels from the domain of protocol generation. Let `I` be a declared directed index. A raw generator is

`gammaTilde:D subseteq X x I -> M_f(X)`.

If every `D_i` is `q`-saturated and `q_# gammaTilde(-,i)` is constant on `q`-fibres, it has an empirical descent on the explicitly descended domain

`D_E={(q(x),i):(x,i) in D} subseteq E x I`, `Gamma_E:D_E -> M_f(E)`.

It has a protocol-level descent on `D_P=(tau x id_I)(D_E) subseteq P0 x I` exactly when, in addition, its domain is saturated along active protocol fibres,

`(e,i) in D_E` and `tau(e')=tau(e)` imply `(e',i) in D_E`,

and its values are fibre-constant,

`tau(e1)=tau(e2)=p => Gamma_E(e1,i)=Gamma_E(e2,i)`

whenever both pairs lie in `D_E`; the common value is supported in `E_p`. The resulting unique partial map is

`Gamma:D_P -> M_f(E)`, `Gamma(p,i)=Gamma_E(e,i)` for any `(e,i)` over `(p,i)`. It is total on `P0 x I` only under the additional declared coverage condition `D_P=P0 x I`.

Types: `gammaTilde` L0/L1; `Gamma_E`, `Gamma` L2 derived maps. Dependencies: T0.4, PR2, DG3. No representative is selected.

**THM PF4 (protocol-generation descent).** The conditions in PF3 are necessary and sufficient for the displayed partial `Gamma:D_P -> M_f(E)` to exist and factor the raw generator through `q` and `tau`. Failure of either protocol-domain saturation or protocol-fibre constancy is `NOT DEFINED AT THIS QUOTIENT` for the relevant protocol/index pair. Total protocol generation needs the extra coverage condition stated in PF3.

*Proof.* T0.4 gives the first partial factorization on `D_E`. A partial function on `D_P` exists exactly when its source domain is a union of `tau`-fibres at each index and its proposed value is constant on each such fibre. Support makes its codomain the declared fibre multiset carrier. Uniqueness follows from active-carrier surjectivity.

**CM PF5 (q-descent without protocol descent).** Let `X={a1,a1',a2,a2'}`, let `q` have classes `e1={a1,a1'}` and `e2={a2,a2'}`, and let `tau(e1)=tau(e2)=p`. At every `i`, set `q_#gammaTilde(a1,i)=q_#gammaTilde(a1',i)=delta_e1` and `q_#gammaTilde(a2,i)=q_#gammaTilde(a2',i)=delta_e2`. The raw map descends through `q`; both outputs are supported in `E_p`; but the two values differ. Thus no `Gamma(p,i)` exists. This is the required protocol-fibre Q-test.

**CM PF5b (active protocol, absent generator).** In the same two-class fibre, let `D_E` contain `(e1,i)` but not `(e2,i)`. This can arise from a q-saturated raw domain. The active protocol `p` has a generator value at one realization class, but `D_E` is not `tau`-saturated, so `(p,i)` is not in a protocol-level domain `D_P`. Assigning `Gamma(p,i)` would add a value for an absent generator; it is `NOT DEFINED AT THIS QUOTIENT`.

**NO-GO PF6 (abstract scheme is not realized).** An abstract `I->M_f(E_p)` cannot be called a protocol generation without a raw realization satisfying PF3. PC14 is retained under this stronger boundary.

## 3. General joint base change

**DEF PF7 (joint transport datum).** For a refinement map `rho_E:E'->E`, a protocol square `tau rho_E=rho_P tau'`, finite fibres, and profile carriers `V',V`, define

`Z' = Delta(E'_{p'}) x (V')^{E'_{p'}}`, `Z = Delta(E_{rho_P(p')}) x V^{E_{rho_P(p')}}`.

The multiplicity pushforward is the declared map `rho_*:Delta(E'_{p'})->Delta(E_{rho_P(p')})`. A profile-merger may be a declared continuous map `K:Z'->V^{E_{rho_P(p')}}`; it may depend on the declared weight coordinate, but may not be inferred merely because `rho_E` is many-to-one. The joint transport is `H(w,v)=(rho_*(w),K(w,v)):Z'->Z`. The weight-independent merger is a special case. The barycentric compatibility square is

`B H = c B'`,

for a declared continuous `c:V'->V`.

**THM PF8 (general joint base change).** Assume PF7; compactness of `Z'` and `V'`; Hausdorffness of `Z` and `V`; a common declared index `I`; and joint nets satisfying `z_i=H(z'_i)`. Then

`J_Gamma(rho_P(p'))=H(J_Gamma'(p'))`

and

`Pred_Gamma(rho_P(p'))=c(Pred_Gamma'(p'))`.

*Proof.* PF1 applied to `H` yields `Cl(z)=H(Cl(z'))`, the first equality. For prediction,

`Pred_Gamma = Cl(B∘H∘z') = Cl(c∘B'∘z') = c(Cl(B'∘z')) = c(Pred_Gamma')`.

The first and last equalities are PF1 (respectively for `B∘H` and `c`); the middle equality is `BH=cB'`. PC9 is the special case with no refinement, where `H` is the identity and PF1 is applied to `B`.

**Cases.** Bijective `rho_E` has coordinate transport as a possible `K`. In the many-to-one case, `rho_*` is canonical finite-multiset arithmetic, but `K` and `BH=cB'` are additional declared conditions. Incompatible merged profiles or a broken square block PF8. Common index is a hypothesis, not an interpretation as time.

**PROP PF9 (tail-equivalent extension).** PF8 remains valid after reindexing the fine net by `h:J->I` when `h` is tail-adherence equivalent relative to `z'` (PC6) and the corresponding coarse net is reindexed compatibly. Then the two joint cluster contents agree by definition, and PF8 applies to the reindexed nets. Mere cofinality is insufficient by PC5.

**CM PF10 (many-to-one boundaries).** (a) Two fine classes can merge with no declared continuous `K`; then base change is untyped. (b) Even with correct `rho_*`, choose `K` and profiles for which `BH != cB'`; then the barycentric square fails. (c) A common-index compatible example with identity `K` and `c` satisfies PF8. These are distinct failure/success cases, not one generic refinement claim.

## Audits

Q-audit: PF4 blocks promotion from empirical to protocol content without fibre invariance. PF8 quantifies only over declared maps, indexes, and joint carriers. Presentation audit: `rho_*`, `K`, `H`, `B`, and `c` must be transported; no carrier-only comparison suffices. Dependency impact: no core change. Finite witnesses are checked by the canonical regression; general proofs remain textual.
