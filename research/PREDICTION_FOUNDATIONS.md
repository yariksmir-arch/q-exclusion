# Finite records and predictive foundations

Existing conditional results; no probability ontology or theorem-level novelty is asserted. Later precise protocol/generation/cluster conditions are in PREDICTIVE_CERTIFICATION_FINALIZATION.md.

## 3. Definitions introduced

**DEF SP1 (finite-record protocol).** Let `X subseteq A_K` be a declared arrangement type and `L` a finite declared readout alphabet. A protocol is a specified family `b_m:X->Batch(L)` of nonempty finite batches. Type: L0/L1 declared procedure data; dependencies: `X,L`; diagnostic until SP3; it is not a universal future-record assertion.

**DEF SP2 (rational aggregate interface).** For positive integers `m,n`, a declared partial operation `alpha_mn:D_mn subseteq X x X -> X` is an aggregate interface when, on its domain,
`nu_(b_(m+n)(alpha_mn(x,y)))=(m/(m+n))nu_(b_m(x))+(n/(m+n))nu_(b_n(y))`.
It is L0/L1 concrete process data; it is a scientist-level aggregate only if it descends at `R` under T0.4. No total mixture operation is presumed.

**DEF SP3 (stable quotient-compatible protocol).** SP1 is quotient-compatible at `R` if every `nu_(b_m(-))` is constant on `~_R`. It is stable if each profile sequence is Cauchy in `Delta(L)`. Type: diagnostic; dependencies `q_R`; its prospective output must respect `~_R`.

**DEF SP4 (stable predictive functional).** When SP3 holds, write `P_R([x])=lim_m nu_(b_m(x))`. Type: L2 derived map `E_R|_X->Delta(L)`; dependencies SP1–SP3; unique if it exists; respects empirical equivalence by SP3.

## 4. Results

**THM SP5 (stable descended predictive-functional theorem).** Assume:

1. a finite declared alphabet `L` and finite-record protocol SP1;
2. quotient compatibility and stability SP3 at a repertoire whose empirical relation is an equivalence;
3. for a stated family of positive pairs `(m,n)`, a rational aggregate interface SP2 whose operation descends at `R`; and
4. for each claimed fixed aggregate alpha_mn and every input in its declared domain, the scaled identity holds for every positive integer k:
   nu_(b_(k(m+n))(alpha_mn(x,y))) = (m/(m+n)) nu_(b_(km)(x)) + (n/(m+n)) nu_(b_(kn)(y)).
   The same aggregate and domain are retained as k grows. A single finite-index SP2 identity alone is insufficient.

Then there is a unique L2 map `P_R:E_R|_X->Delta(L)`. For every descended aggregate input pair,
`P_R(alphaBar_mn([x],[y]))=(m/(m+n))P_R([x])+(n/(m+n))P_R([y])`.

This is a conditional limit and factorization result in known mathematics. It constructs neither an objective probability nor an aggregation operation outside the declared domains.

**PROP SP6 (minimality of hypotheses).** Removing stability, quotient compatibility, descent of the aggregate, or the stated aggregation identity invalidates respectively uniqueness, L2 definability, L2 additivity, or the displayed barycentric conclusion.

## 5. Proofs / proof sketches

By finite-dimensional completeness, stability gives a unique limit `p_x` for every `x`. Quotient compatibility at every finite stage makes `p_x=p_y` whenever `x~_R y`; T0.4/P5 therefore give the unique descended map `P_R([x])=p_x`. For a fixed aggregate alpha_mn, take k to infinity in assumption 4. The three batch indices k(m+n), km and kn all tend to infinity, while the aggregate input and rational ratio remain fixed. Addition and rational scalar multiplication in the finite vector space are continuous, yielding the formula in SP5. Because the aggregate itself descends, the left side is a class-defined input. No limit is taken over repertoires or global sample spaces.

## 6. Countermodels and failed routes

**CM SP0 (finite-index identity is insufficient).** Let the quotient be discrete on {x,y,z}, with the only aggregate alpha_11(x,y)=z. Every profile at x and y is delta_0. At z the second batch has profile delta_0, but every batch from index 3 onward has profile delta_1. All sequences are stable and the sole SP2 identity at (1,1) holds; nevertheless P(z)=delta_1 differs from (P(x)+P(y))/2=delta_0. The scaled identity fails. This refutes the unqualified finite-index-to-limit inference.

**CM SP1 (remove stability).** Alternating singleton batches `0,1,0,1,...` have two cluster profiles; the limit functional is not unique.

**CM SP2 (remove quotient compatibility).** With `x~_R y`, assign constant batches `0` to `x` and `1` to `y`. Each limit exists, but the assignment fails fibre constancy and is `NOT DEFINED AT THIS QUOTIENT`.

**CM SP3 (remove aggregate descent).** M5 has a concrete constructor distinguishing a coarse class. A finite arithmetic identity for its representatives cannot define a quotient aggregate; representative choice would be hidden content.

**CM SP4 (remove exact aggregate identity).** Let all component profile sequences converge but stipulate a declared operation with limiting output profile different from the barycenter. Stability alone cannot prove additivity.

**Failed route.** Replacing the declared aggregate interface by arbitrary real convex combinations introduces an undeclared completion/operation. SP5 proves rational affine structure only where the concrete aggregate already descends.


## 3. Definitions introduced

**DEF RG1 (identity-free finite batch).** For a finite declared readout alphabet `L`, a batch is a nonzero count vector `n:L->N`. Its size is `|n|=sum_l n(l)` and its profile is `nu(n)=n/|n|`. Type: L0 arithmetic record shape; dependencies finite `L`; diagnostic. It is not an indexed family of trials: two finite enumerations with the same counts denote the same batch.

**DEF RG2 (record-generation interface).** For a declared arrangement subtype `X` with quotient `q:X->E`, an interface is a partial concrete map `g:D_g subseteq X->Batch(L)` together with the requirement of fibre constancy:
`x~_R y` and `x,y in D_g` implies `g(x)=g(y)`, and `D_g` is saturated. Type: `g` L0/L1 procedure data; its induced `gBar:E|_D->Batch(L)` is L2 derived by T0.4. Dependencies `q,L`; no temporal or trial identity is introduced.

**DEF RG3 (same-type collection).** A finite collection is a finite multiset `M` of generated batch values equipped with a common `e in E` such that every member is in the image of `gBar(e)`, or, for a family of interfaces, is explicitly tagged by the same descended type `e`. Type: L2 derived/diagnostic collection; dependencies RG2; unique only modulo permutation and multiplicity; it respects `E` equality. The tag is an empirical class, not a concrete representative.

**DEF RG4 (batch aggregate).** For a nonempty same-type finite multiset `M`, define
`Agg_e(M)=sum_{n in M} n in Batch(L)`.
Type: L2 derived arithmetic operation on RG3 collections; dependencies RG1–RG3. It is commutative and associative because `M` is a multiset, not an ordered trial list. Its profile is defined only after the nonzero-size condition, automatic for a nonempty collection of batches.

**DEF RG5 (concrete realization of aggregation).** A concrete process `a` realizes RG4 at `e` only if its input collection encoding and output record map descend and their output count vector equals `Agg_e(M)`. Type: L0/L1 realization predicate; diagnostic; it respects the relevant collection quotient. If it fails, `a` is not a scientist-level aggregate operation even though RG4 remains an L2 count-vector construction over already generated values.

## 4. Results

**THM RG6 (identity-free aggregate descent).** Under RG1–RG4, `Agg_e` is a well-defined L2 operation on nonempty finite same-type multisets. It is invariant under every re-enumeration of record occurrences and satisfies
`nu(Agg_e(M union N))=(|Agg_e(M)|/(|Agg_e(M)|+|Agg_e(N)|))nu(Agg_e(M)) + (|Agg_e(N)|/(|Agg_e(M)|+|Agg_e(N)|))nu(Agg_e(N))`
for nonempty `M,N`.

**THM RG7 (generation/descent criterion).** Under RG2, `gBar` exists uniquely iff the domain of `g` is saturated and `g` is fibre-constant. Hence a collection of concrete generated records can be asserted to have one empirical type only after its type assignment descends through `q`. If this fails, it is `NOT DEFINED AT THIS QUOTIENT`.

**PROP RG8 (concrete aggregate criterion).** Under RG5, a concrete aggregation implementation is scientist-level iff its encoding/output map is invariant on the stated input/output collection equivalences and realizes the vector sum. The existence of `Agg_e` alone does not certify an implementation.

## 5. Proofs / proof sketches

RG6 is well-defined because a finite multiset is determined by multiplicities, and finite vector addition is independent of enumeration and associative/commutative. The profile equation follows by writing the vector sum as `u+v` and dividing by `|u|+|v|`. RG7 is T0.4 applied to the partial map `g`. RG8 is the empirical-descent principle applied to its concrete encoding/output operation, followed by equality to RG4.

## 6. Countermodels and failed routes

**CM RG1 (representative-dependent generation).** Let `x~_R y` but a purported generator give count vector `(1,0)` at `x` and `(0,1)` at `y`. A common empirical-type tag cannot be assigned; the generator and any aggregate using it are `NOT DEFINED AT THIS QUOTIENT`.

**CM RG2 (mixed types).** Let `e!=e'` in `E` and take one batch tagged `e`, another tagged `e'`. Their numerical sum exists at L0, but it is not an aggregate *of one empirical type* under RG3. Declaring a common type without a descended relation is new content.

**CM RG3 (ordered-list route).** If a proposed aggregate is an ordered tuple of records and changes when two entries are swapped, it does not factor through the multiset quotient. It relies on an undeclared ordering/identity distinction and is not RG4.

**CM RG4 (implementation non-descent).** M5 supplies concrete inputs identified at a coarse quotient but distinguished by a constructor. An implementation using that constructor is not a scientist-level aggregate at the coarse level even if its numerical output happens to be a count vector.

**Failed route.** Starting from an infinite sequence of labelled trials would make identity/order available before it descends. RG1 instead starts from finite count vectors; no limit or continuation relation is built into the interface.


## 3. Definitions introduced

**DEF SV1 (cluster content).** Let `V` be a declared compact metric L0 representation space (for finite records, `V=Delta(L)`) and `h_m:E->V` a sequence of descended L2 assignments. Define
`Cl(h,e)=intersection_N closure({h_m(e):m>=N})`.
Type: a nonempty compact subset of `V`, L0/L2 derived diagnostic; dependencies compact `V`, `h`; unique; it respects `E` equality by typing. It selects no point.

**DEF SV2 (closed set-valued coarsening).** For a concrete refinement map `pi:E'->E` and `H:E'->K(V)` into nonempty closed subsets, define
`Coarsen_pi(H)(e)=closure(union_{e' in pi^{-1}(e)} H(e'))`.
Type: L2 derived set-valued map, relative to this declared `pi`; dependencies SV1 or another H; no inverse limit or universal repertoire family is used.

**DEF SV3 (asymptotic enclosure).** A closed-valued map `Q:E->K(V)` asymptotically encloses `h` when every open neighbourhood of `Q(e)` contains `h_m(e)` for all sufficiently large `m`, separately for each declared `e`. Type: L2 diagnostic; it is not a claim about all future sequences.

## 4. Results

**THM SV4 (minimal cluster prediction).** Under SV1, `Cl(h,-)` is the unique smallest closed-valued asymptotic enclosure: for every closed-valued `Q` asymptotically enclosing `h`, `Cl(h,e) subseteq Q(e)` for every `e`.

**THM SV5 (refinement coarsening universal property).** Under SV2, `Coarsen_pi(H)` is the least closed-valued map `Q:E->K(V)` such that `H(e') subseteq Q(pi(e'))` for every `e'`. If `E'` is finite, its values are compact whenever H has compact values.

**THM SV6 (refinement composition).** For concrete refinement maps `E'' --rho--> E' --pi--> E`,
`Coarsen_pi(Coarsen_rho(H))=Coarsen_(pi o rho)(H)`.
Thus uncertainty coarsens monotonically along a concrete refinement chain without a selected profile.

**PROP SV7 (stable collapse).** If `h_m(e)` converges, then `Cl(h,e)` is its singleton limit; hence SV4 recovers SP5’s unique predictive value under stability.

## 5. Proofs / proof sketches

For SV4, compactness makes every tail closure nonempty compact, and their nested intersection nonempty compact. If `Q(e)` asymptotically encloses the sequence and `z` is outside its closed value, an open neighbourhood of `Q(e)` whose closure excludes `z` (available in the compact metric carrier) contains every sufficiently late term; hence `z` cannot belong to every tail closure. This proves minimality and uniqueness.

For SV5, every `Q` satisfying the containment condition contains the union over each fibre and, being closed, its closure. Conversely SV2 is closed and satisfies the condition. SV6 follows by expanding both sides: nested union over `rho` then `pi` is the union over the fibre of `pi o rho`; taking closures on either nesting yields the same closed set. SV7 is the elementary cluster-set characterization of convergence in a metric space.

## 6. Countermodels and failed routes

**CM SV1 (multiple clusters).** The alternating profiles `delta_0,delta_1,...` have cluster content `{delta_0,delta_1}`. Selecting either point violates SV4’s non-selective construction.

**CM SV2 (no fine descent).** If `x~_R' y` but `h_m(x)` and `h_m(y)` have different cluster sets, no map `H:E_R'->K(V)` exists. The correct status is `NOT DEFINED AT THIS QUOTIENT` before coarsening.

**CM SV3 (wrong refinement direction).** A finer class can have singleton cluster content while its coarse class has the closed union of several fine contents. Requiring equality rather than SV5’s fibre union discards declared distinctions or selects one fine class.

**Failed route.** An inverse limit over all repertoires would not be SV2: only a stated finite/generated refinement map occurs in the construction.


## 3. Definitions introduced

Point-valued protocol conclusions below use only the active image im(tau). Unoccupied raw protocol labels keep empty residual content; no point-valued extension there is asserted. Nonempty closed-valued coarsening likewise requires occupied fibres.

**DEF PR1 (concrete realization sector).** `X_real` is a declared L1 arrangement sort of concrete realizations with a concrete repertoire `R_real`, quotient `q:X_real->E_real`, and no interpretation as a global state. Type: `X_real` L0/L1; `E_real` L2; dependencies frozen core; `E_real` is unique up to quotient equivalence and respects `~_Rreal`.

**DEF PR2 (concrete protocol typing).** A protocol typing is a declared concrete map `tauTilde:X_real->P_protocol` into a declared L1/L2 type carrier `P_protocol`. It is admissible at `E_real` iff it is fibre-constant on `q`; then its unique descended map is `tau:E_real->P_protocol`. Type: `tauTilde` L0/L1, `tau` L2; dependencies PR1; no canonical realization in a fibre is specified.

**DEF PR3 (record generator).** For finite declared alphabet `L`, a record generator is a declared partial map `gTilde:D_g subseteq X_real->Batch(L)` in the identity-free sense of RG1. It is admissible iff its domain is saturated and it is fibre-constant; its descended partial map is `g:E_real|_D->Batch(L)`. Type: concrete L0/L1 map and derived L2 map; dependencies PR1 and RG1; it respects empirical equivalence.

**DEF PR4 (protocol batch content).** For `p in P_protocol`, define
`B_P(p)={g(e): e in dom(g), tau(e)=p}`.
Type: L2 set-valued finite-record content, relative to the declared `tau` and `g`; dependencies PR2–PR3; it is unique and selects no element. Its fibre is the concrete fibre of this declared map, not a set of all realizations.

**DEF PR5 (protocol profile-cluster content).** For a declared sequence of descended generators `g_m:E_real->Batch(L)`, define
`P_P(p)=closure(union_{tau(e)=p} Cl(nu(g_m(e)),e)) subseteq Delta(L)`
whenever the cluster contents are defined as in SV1. Type: L2 set-valued predictive content; dependencies PR2, PR3, SV1; no point or probability law is selected.

## 4. Results

**THM PR6 (descended protocol/record diagram).** Under PR1–PR3, the diagram

```text
     E_real
     /     \
  tau/       \g
   v           v
P_protocol   Batch(L)
```

exists exactly when `tauTilde` and `gTilde` satisfy their respective empirical-descent criteria. If either fails, the corresponding arrow is `NOT DEFINED AT THIS QUOTIENT`.

**THM PR7 (minimal protocol batch content).** Under PR2–PR4, `B_P` is the unique least set-valued map `H:P_protocol->Power(Batch(L))` with `g(e) in H(tau(e))` for every declared `e` in the domain of `g`. Thus it is the direct image along a concrete protocol fibre, not a hidden distribution.

**THM PR8 (protocol-level set-valued prediction).** Under PR5 and compact finite-profile representation, `P_P` is the least closed-valued map on `P_protocol` containing every realization-level cluster content in the corresponding `tau` fibre. If `tau` is a refinement/coarsening map, this is exactly SV5’s `Coarsen_tau` construction; composition follows from SV6.

**PROP PR9 (stable specialization).** If every realization-level profile sequence converges and all limits in a protocol fibre agree, `P_P(p)` is a singleton, recovering a protocol-level SP5 value. If limits differ, the correct output remains the non-singleton `P_P(p)`.

**THM PR10 (protocol-fibred SP5/SV rewrite).** Assume a sequence of PR3-descended generators `g_m`, stable at every `e in E_real`, and the declared protocol map `tau`. Then the protocol-level predictive object is
`P_protocol(p)=closure({lim_m nu(g_m(e)) : tau(e)=p})`.
It is the SV5 coarsening of realization-level singleton SP5 limits. A single-valued map `P_protocol:P_protocol->Delta(L)` exists exactly when this set is singleton at every declared protocol class; otherwise the set-valued object is the complete admissible conclusion.

## 5. Proofs / proof sketches

PR6 is two applications of the necessary-and-sufficient partial-map descent theorem T0.4. For PR7, any `H` satisfying the containment condition contains all values in the displayed fibre image; hence it contains `B_P(p)`, while `B_P` itself satisfies the condition. PR8 is SV5 applied to `tau:E_real->P_protocol` and realization-level cluster content; PR9 follows because the closure of a union of identical singleton limits is that singleton. PR10 combines realization-level SP5 with SV5; its necessity is immediate because a single point cannot equal a non-singleton fibre closure.

## 6. Countermodels and failed routes

**CM PR1 (non-descended protocol typing).** Let `x~_R y`, but `tauTilde(x)!=tauTilde(y)`. Then no protocol type can be assigned to `[x]=[y]`; treating the names as protocol types is hidden content.

**CM PR2 (non-descended record).** Let `x~_R y`, but `gTilde(x)=(1,0)` and `gTilde(y)=(0,1)`. The right arrow of PR6 does not exist, so no protocol-level content may be constructed.

**CM PR3 (same protocol, distinct realizations).** Let `E_real={e_1,e_2}`, `tau(e_1)=tau(e_2)=p`, and `g(e_1)=(1,0)`, `g(e_2)=(0,1)`. A map `P_protocol->Batch(L)` is not determined, but `B_P(p)={(1,0),(0,1)}` is. Selecting `e_1` is a forbidden selector; no stochastic variable has been invoked.

**CM PR4 (undeclared fibre enlargement).** Adding a new realization class over `p` with another batch changes `B_P(p)`. Under the forgetful map erasing that realization, the larger content does not descend to the prior presentation; it is new content, not an old protocol prediction.

**Failed route.** Identifying all batches in one protocol fibre, or introducing a probability distribution over the fibre, adds structure not fixed by `tau` and `g`.
