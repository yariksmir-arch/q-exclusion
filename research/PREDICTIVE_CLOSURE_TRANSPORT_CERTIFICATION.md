# Predictive Closure & Transport Certification


## Status and scope

This derived L2 calculus states the scope required for closure, aggregation and transport. All indexes, fibres, profile maps, generation schemes, and transports below are declared finite/generated data in the presentation.

**Scope clarification.** For every compactness-based conclusion below, the weight carrier is separately declared compact Hausdorff (for example an explicitly supplied closed real simplex), and the joint net takes values there. Finite rational multiplicities provide weights inside that carrier; they do not derive its completion or compactness. Without this extra interface the compact-domain step is unavailable.

## 1. Topological closure

**DEF PC1 (tail-cluster content).** For a declared directed set `I`, a net `x:I -> V`, and a compact Hausdorff space `V`, set

`Cl_I(x) = intersection_{i in I} closure(x(I_{>=i}))`.

**DEF PC2 (closed asymptotic enclosure).** A closed `C subseteq V` asymptotically encloses `x` iff for every open `U` with `C subseteq U`, there is `i0` such that `x(i) in U` for all `i>=i0`. This is not the assertion that `C` contains a tail pointwise.

**THM PC3 (correct cluster theorem).** Under PC1, `Cl_I(x)` is nonempty compact, is the unique least closed asymptotic enclosure in the sense of PC2, and is a singleton iff `x` converges.

*Proof.* The tail closures form a nonempty decreasing family of closed subsets of compact `V`; their intersection is nonempty and compact. If `U` contains the intersection but no tail lies in `U`, choose one point outside `U` in every tail. Compactness of `V\U` gives a cluster point outside `U`, contradicting the definition. Hence the intersection is an enclosure. Every closed asymptotic enclosure contains every cluster point, proving minimality. The singleton criterion follows from the enclosure property and Hausdorff uniqueness of limits.

**CM PC4 (`1/n`).** In `[0,1]`, `x_n=1/n` has `Cl_N(x)={0}`. It is an asymptotic enclosure, but it contains no tail. Thus “least closed set containing a tail” cannot replace neighbourhood-asymptotic enclosure.

**NO-GO PC5 (reindexing).** A monotone cofinal reindexing need not preserve cluster content: for `x_n=0,1,0,1,...` and `h(k)=2k`, `Cl_N(x)={0,1}` but `Cl_N(x∘h)={0}`.

**DEF PC6 (tail-adherence equivalence).** Reindexings `h:J->I` and the identity are tail-adherence equivalent relative to `x` iff

`intersection_i closure(x(I_{>=i})) = intersection_j closure(x(h(J_{>=j})))`.

This is the exact necessary-and-sufficient condition for preservation of the declared cluster content. A stronger checkable sufficient condition is mutual cofinality, under inclusion, of the two families of closed tail images. Cofinality alone gives only `Cl_J(x∘h) subseteq Cl_I(x)`.

## 2. Typed barycentric calculus

**DEF PC7 (separated types).** For finite `E_p`, `Delta(E_p)` is the L2 finite-weight simplex produced by normalized finite multiplicities. A profile carrier is a separately declared compact Hausdorff `V` equipped with a declared continuous finite barycentric map

`B_p: Delta(E_p) x V^{E_p} -> V`.

Its required exactness is `B_p(w,(nu_e))=sum_e w_e nu_e` when `V` is the declared finite-profile simplex. Outside this interface, neither the expression `sum_e w_e v_e` nor its continuity is licensed. `B_p` is late quantitative L2 structure (or L3 representational structure with a stated descent interface), not a consequence of compactness.

**DEF PC8 (joint generation net).** A realized generation scheme gives `w_i(e)=m_i(e)/N_{m_i}` and a declared jointly typed profile tuple `v_i=(v_{e,i})_e`. Its joint net is `z_i=(w_i,v_i):I_p -> Z_p=Delta(E_p) x V^{E_p}` and

`J_Gamma(p)=Cl_I(z)`.

**THM PC9 (joint-cluster master theorem).** Assume finite `E_p`, a separately declared compact Hausdorff weight carrier, compact Hausdorff `V`, PC7 with continuous `B_p` on their compact joint product, and a realized `Gamma_p`. If its aggregate profile is `a_i=B_p(z_i)`, then

`Pred_Gamma(p)=Cl_I(a)=B_p(J_Gamma(p))`.

*Proof.* `Z_p` is compact Hausdorff and `B_p` is continuous. Every cluster point of `z` maps to a cluster point of `a`. Conversely, a subnet converging in the compact space `Z_p` may be chosen along any aggregate cluster subnet; continuity maps its limit to that aggregate cluster point. Thus the two compact sets agree.

**COR PC10 (stable barycenter; repaired DP3).** If `z_i` converges to `(w,(v_e)_e)`, then `Pred_Gamma(p)={B_p(w,(v_e)_e)}`. The former coordinate formula is available only under PC7's finite-profile exactness clause.

**COR PC11 (set-valued weights; repaired DP5).** If `v_i` converges to `v` and `W_p=Cl_I(w)`, then `J_Gamma(p)=W_p x {v}` and `Pred_Gamma(p)=B_p(W_p x {v})`. With variable profiles, the correct object is `B_p(J_Gamma(p))`, not a Cartesian product of independently chosen clusters.

**THM PC12 (conditional convex closure; explicit scope).** Let `V` be a separately declared finite-dimensional real profile simplex with PC7's continuous exact finite barycenter on the compact real weight simplex. Supply a descended, realized family of schemes whose profile tuples all converge to the same fixed tuple `v`, so every joint cluster belongs to `Delta(E_p) x {v}`. Require that the family jointly includes `(w,v)` for every rational simplex weight `w`. Then the closure of the union of their predictions is the closed convex hull of `{v_e}`.

*Proof.* PC9 and the fixed-profile restriction put every prediction in that hull. The coverage assumption includes every rational barycenter of the fixed tuple; density of rational weights and continuity give the whole closed hull after closure. Both inclusions are needed. No real simplex is derived from rational records.

**CM (missing fixed-profile restriction).** On a singleton fibre let the named fixed profile be 0. A constant profile-0 scheme supplies its only rational weight, while an additional constant profile-1 scheme adds prediction 1. Coverage holds, yet the union closure is {0,1}, not the required hull {0}. Thus coverage alone is insufficient.

## 3. Concrete generation admission

**THM PC13 (sufficient descent criterion).** Let `q:X->E` be the realization quotient and `I` a declared index. A concrete generator `gammaTilde:D subseteq X x I -> M_f(X)` admits the L2 scheme

`Gamma([x],i)=q_#(gammaTilde(x,i))`

when: (i) every section `D_i` is `q`-saturated; (ii) `q_#gammaTilde(-,i)` is constant on each `q`-fibre; (iii) its output is supported in the declared `tau`-fibre; and (iv) the resulting nonzero multisets and profile interface are declared. These conditions make the displayed formula well-defined; they do not posit a hidden concrete process.

**NO-GO PC14 (abstract is not realizable).** A map `I->M_f(E_p)` with no `gammaTilde` satisfying PC13 is diagnostic arithmetic only. It cannot be promoted to a scientist-level generation operation. A generator with two raw representatives of one `q`-class inducing different `q_#` multisets witnesses failure.

## 4. Refinement × generation transport

Refinement transport uses PF7–PF8 in PREDICTIVE_CERTIFICATION_FINALIZATION.md: one declared joint map, compatible profile merger, common index and commuting barycentric square are required.

**CM PC16 (noncommuting transport).** Let two refined realisation classes coarsen to one class. If the fine scheme generates the first class while a purported coarse scheme generates a different profile, then `m_i != rho_#m'_i`; the aggregate square fails and no base-change conclusion is typed.

## Audits

Q-audit: the calculus quantifies only over declared `E_p`, `I`, schemes, and transport maps. It selects no realization and infers no distribution. Presentation-invariance audit: PC9 and PF7–PF8 require transport of `B`, joint nets, and tail-adherence; carrier equivalence alone does not suffice. Dependency impact: no backbone change. Regression risk: PC13 is sufficient, not necessary; infinite fibres require a separately typed measure/barycenter interface and are not claimed here.
