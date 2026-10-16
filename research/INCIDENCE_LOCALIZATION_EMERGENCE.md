# Incidence / Localization Emergence — incidence interface

## Status and boundary

The scope of this incidence module is **`INCIDENCE_RELATION_ONLY`**. Its ordinary signature is exactly `Sigma_IL = (E_X, E_R, Dbar_I, Ibar)`, or its declared-label interpretation `Inc subseteq E_X x E_R`. It has no primitive points, regions, topology, metric, order, or geometry.

## Typed interface and descent

**DEF IL1 (two-sort raw interface).** `X0` and `R0` are L0-presented L1 carriers of declared arrangements/records and declared localization contexts. They have independent declared repertoires and quotients `q_X:X0->E_X`, `q_R:R0->E_R`. A raw incidence procedure is a partial L1 map `Itilde:D_I subseteq X0 x R0 -> O_I`, where `O_I` is finite declared output labels such as `{yes,no,undetermined}`. `D_I` need not be total; labels have no geometric meaning. Dependencies: both quotients, declared domain and procedure.

**THM IL1 (two-sort incidence descent; T0.4 specialization).** A unique partial L2 map `Ibar:Dbar_I subseteq E_X x E_R -> O_I`, with `Ibar(q_X(x),q_R(r))=Itilde(x,r)` and `Dbar_I=(q_X x q_R)(D_I)`, exists iff (i) `D_I` is saturated under `~_X x ~_R`, and (ii) `Itilde` is constant on every product fibre in `D_I`. Proof: necessity pulls back the domain/value square; sufficiency gives representative independence; quotient surjectivity gives uniqueness. IL-CM2 violates (ii), therefore `INCIDENCE NOT DEFINED AT THIS QUOTIENT`.

**DEF IL2 (interpreted incidence).** Given declared `O_in subseteq O_I`, set `x Inc r` iff `(x,r) in Dbar_I` and `Ibar(x,r) in O_in`. This is derived L2, dependent on the explicit label interpretation.

## Partial information and extensional structure

**DEF IL3.** For `r`, `Pos(r)`, `Neg(r)`, and `Unknown(r)` collect positive, negative, and undefined/undetermined typed outputs. Only in a stated fully decided yes/no sector define `Ext(r)={x:x Inc r}` and infer negative membership. In a partial sector absence from `Pos(r)` is not negative incidence. **NO-GO IL4:** unknown cannot be converted to `no` (IL-CM15).

**DEF IL5.** In a fully decided sector, `Ext:E_R->P(E_X)` and optionally `Loc:E_X->P(E_R)` are derived L0 presentations of L2 incidence, not primitive regions. Define `r ==ext s` iff `Ext(r)=Ext(s)`.

**THM IL2 (extensional quotient).** `==ext` is an equivalence relation and `E_R/==ext` is bijective with `im(Ext)`. This standard quotient is derived L2 and does not replace `E_R`; IL-CM5 has distinct empirical contexts with equal extent.

**THM IL3 (extensional inclusion).** In a fully decided sector, `r <=ext s iff Ext(r) subseteq Ext(s)` is a preorder and induces a partial order on `E_R/==ext`. This standard set-inclusion result is derived from incidence, not an independently performed inclusion test. IL-CM6 gives incomparability.

**DEF IL6 (direct probes).** An optional direct inclusion/overlap comparator is separate partial L1 data and separately descends by IL1. It is never silently identified with `<=ext` or extensional overlap (IL-CM20).

**PROP IL4 (overlap and co-localization).** In a fully decided sector, `r Ov s` iff `Ext(r) intersect Ext(s)` is nonempty: symmetric and reflexive exactly on nonempty extents, but non-transitive (IL-CM7). `x coLoc y iff exists r (x Inc r and y Inc r)` is likewise non-transitive (IL-CM18). Neither is proximity. Empty-extent contexts remain unless L1 declares them impossible.

## Represented closure, refinement, transport

**THM IL5 (exact represented intersection criterion; corrected scope).** Assume the fully decided sector of DEF IL5 and let `F=im(Ext)`, the existing extensional-quotient presentation. For `A,B in F`, an exact intersection result is represented iff `A intersect B in F`; the result is unique up to `==ext`. Proof: necessity is the stipulated extent equation; sufficiency is a context realizing that extent; uniqueness follows from IL2. Its class is then the order-theoretic meet, since every lower bound is contained in the intersection. The converse is false: in `F={empty,{a,b},{b,c}}`, the relative meet of `{a,b}` and `{b,c}` is `empty`, although `{b}` is absent. Thus the historical verdict `MEET NOT REPRESENTED` means exact intersection not represented, not absence of every ordinary meet (IL-CM8).

**THM IL6 (exact represented union criterion; corrected scope).** Under the same assumptions, an exact union result is represented iff `A union B in F`; it is unique up to `==ext` and is an order-theoretic join. Proof: the extent equation gives necessity and representation gives sufficiency; every upper bound contains the union. Conversely, in `F={{a},{b},{a,b,c}}`, the relative join of `{a}` and `{b}` is `{a,b,c}`, while `{a,b}` is absent. The historical `JOIN NOT REPRESENTED` means exact union not represented (IL-CM9). Complements require a represented complementary extent; lattice-like data is not Boolean (IL-CM17). IL-CM10 remains a stronger positive control.

**PROP (relative bounds; KNOWN).** In the existing order `(F,subseteq)`, a meet exists iff the represented lower bounds have a greatest element; a join exists iff the represented upper bounds have a least element. This is the defining universal property, without exact set closure. Missing bounds are witnessed by `F={{a},{b}}`; multiple incomparable maximal lower bounds by `F={{a},{b},{a,b,c},{a,b,d}}` for the last pair (dual upper-bound obstruction likewise). Total exact intersection/union coverage is sufficient, not necessary, for ordinary semilattice/lattice recognition.

**PROP (procedure availability; T0.4 specialization).** A declared raw binary context procedure `m:D subseteq R0 x R0 -> R0` induces a partial scientist-level operation on `E_R` iff its domain is saturated under the product empirical equivalence and `q_R(m(r,s))` is constant on each input fibre. Necessity and sufficiency are the domain/value descent square of IL1/T0.4. Whether that descended operation realizes exact intersection, exact union or a relative bound is a separate correctness condition. A mathematically represented class does not supply a raw procedure. Equal extents may still be different empirical contexts (IL-CM5); extent-correct output choices can fail empirical descent. No representative selector or physical availability is inferred.

**THM IL7 (finite realizable incidence refinement).** The diagnostic split of offending fibres is only L0. For finite carriers it is realized exactly when independently declared probes are sound for the proposed classes and their joint readouts separate every required split (RR4–RR7 per sort). IL-CM3 is positive; IL-CM4 yields `INCIDENCE REFINEMENT NOT REALIZED`. The desired raw table is not an available discriminator.

**THM IL8 (adequate two-sort transport).** L2 incidence and claimed derived relations transport only with explicit transport of both quotients, domain, outputs/interpretation, probe grammars, optional direct probes, and represented operations. Bare bipartite-graph isomorphism is insufficient. IL-CM11 changes both raw carriers; IL-CM12 blocks coordinate-label surplus.

## Recognition and minimization

**REC IL-REC1.** `EXTENSIONAL_PARTIAL_ORDER` needs a fully decided sector plus IL3. `REPRESENTED_MEET_SEMILATTICE`/`REPRESENTED_LATTICE` retain their historical names for the stronger exact-intersection/exact-union controls and need IL5/IL6 coverage and laws. These are not necessary criteria for ordinary relative order bounds. Scientist-level procedures require the separate availability/descent test above. Ordinary S3 provides no closure or procedure premise. Presentation comparisons require adequate full-interface transport (IL8), not an extra premise for static bound existence.

**NO-GO IL9.** A family of extents is not a topology merely because it is subsets. Finite topology recognition requires L2 empty/full, finite-intersection, and finite-union closure witnesses. IL-CM16 is a stronger control only.

**NO-GO IL10.** Incidence/topology do not determine metric, dimension, manifold, coordinates, causal order, physical symmetry, or locality. IL-CM13/14 give distinct L3 metric/causal extensions. Automorphisms are relabellings, not transformations without descended process structure. IL-CM19 shows process localization has no generic composition rule; no predictive bridge is required.

Backbone minimization removes extensional quotient, order, overlap, closure, and topology from ordinary S3. The irreducible content remains `Sigma_IL`.
