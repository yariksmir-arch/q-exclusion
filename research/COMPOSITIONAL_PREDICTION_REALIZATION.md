# Compositional Prediction Realization

## Scope and status

This finite module assumes the `CP1` partial process calculus.  It proves
the exact conditions for a *declared L1 paired procedure* to become L2 data,
and distinguishes this from the arithmetic pushforward of a descended
composition.  It adds neither probability, trial identity, time, a product,
nor a category.

`E_P=P_0/{\sim_P}` and `Comp\subseteq E_P\times E_P` are the L2 quotient and
relation of CP1/CP2.  All multisets below are finite multiplicity functions;
their ratios, when formed, are arithmetic profiles only.

## Typed data

**DEF CPG1 (composable-pair carrier).**  Define

`E_pair = {(g,f) in E_P x E_P : Comp(g,f)}`.

It is a derived L2 relation with its L0 subset presentation, not a new core
carrier or a claim that every pair is composable.  With the CP1-saturated raw
domain `D_circ subseteq P_0 x P_0`, the restriction

`q_pair=(q_P x q_P)|D_circ : D_circ -> E_pair`

is a surjection.  Its well-defined target uses precisely CP1 domain
saturation.  The descended map `circ:E_pair->E_P` is CP1's partial operation
viewed on this typed carrier.

**DEF CPG2 (raw paired-generation interface).**  Let `S_0` be a declared L1
control/realization carrier, `q_S:S_0->E_S` its empirical quotient,
`tau_2:E_S->P_2` an optional declared active pair-protocol map, and `I` a
declared directed batch-growth index (not a temporal order).  A raw procedure
is a partial L1 map

`GammaTilde2:D2 subseteq S_0 x I -> M_f(P_0 x P_0)`.

Every output claimed to be compositional must have support in `D_circ`.  This
is an independently declared procedure producing composition slots `(g,f)`;
its two projections are only its marginal generated multisets.

## Paired descent and concrete composition

**THM CPG3 (paired-generation descent).**  A unique partial L2 map

`Gamma2:D_P2 -> M_f(E_pair)`

factoring `q_pair# GammaTilde2` exists exactly when:

1. `D2` is `q_S x id_I`-saturated and `q_pair#GammaTilde2` is constant on
   every `q_S` fibre;
2. its resulting domain in `E_S x I` is `tau_2 x id_I`-saturated and its
   values are constant on each `tau_2` fibre (when `tau_2` is used);
3. every raw output is supported in `D_circ`.

`D_P2` is the image of the explicitly saturated domain.  A total protocol
generator needs the extra coverage hypothesis `D_P2=P_2 x I`.  If profiles
are normalized, every batch in their stated domain must be nonempty.

*Proof.*  Support makes `q_pair#` typed.  T0.4 gives the first factorisation
iff condition 1 holds.  The partial-function argument of PF4 gives the second
iff condition 2 holds.  Surjectivity of the quotient maps gives uniqueness.
Conversely, pull back the domain and value squares of a purported descended
map.  This is PF4's two-stage proof with the additional `q_pair` typing step;
it is not an invocation of PF4 on an untyped product.

**LEMMA CPG4 (finite composition pushforward).**  For every
`m in M_f(E_pair)`,

`(circ#m)(h)=sum_{(g,f) in E_pair, g circ f=h} m(g,f)`.

Consequently `m_comp=circ#m` is a well-defined finite multiset and
`q_P#(c0#n)=circ#(q_pair#n)` for every raw multiset `n` supported in
`D_circ`.  This is ordinary finite-multiset arithmetic, not a concrete
generator, probability law, expectation, or linear dynamics.

**THM CPG5 (composite-generation realization).**  In addition to CPG3,
assume that a declared L1 batch implementation executes `c0` on every slot
in each output of `GammaTilde2`, preserves each slot multiplicity, performs
no undeclared deduplication or selection, and has declared composite-record
production.  Then its output `GammaTildeComp=c0#GammaTilde2` descends and

`GammaComp=circ# Gamma2`.

*Proof.*  The raw identity in CPG4 and CPG3's fibre constancy prove both
empirical and protocol-fibre constancy.  The stated implementation clauses
identify the arithmetic output with an L1 generated batch.  Dropping that
implementation leaves only CPG4: an L2 multiset pushforward does **not**
create a concrete composite-generation procedure (CPG-CM7).

## Derived record and profile bridge

**DEF CPG6 (record interface).**  Declared raw pair and composite record maps
`rPair0:D_circ->LPair0` and `rComp0:P_0->LComp0` descend, when their own
fibre tests pass, to `rPair:E_pair->LPair` and `rComp:E_P->LComp`.  They are
L2 derived maps; labels remain record interfaces, not process identities.

**THM CPG7 (derived record factor and exact profile square).**  Suppose CPG5
holds and a concrete record rule `kappa0` satisfies, on every generated raw
slot,

`rComp0(c0(g,f)) = kappa0(rPair0(g,f))`.

If equal descended pair records on the generated support have equal right-hand
composite records, then `kappa` is a well-defined descended map from the
generated pair-record image to `LComp`, and

`rComp# circ# m = kappa# rPair# m`

for every generated `m`.  For normalized finite count profiles,
`Phi=kappa_*:VPair->VComp` is therefore a descended continuous finite-profile
map and `vComp=Phi(vPair)`.

*Proof.*  The displayed concrete equality plus the equality-of-records clause
makes `kappa([ell])` representative-independent.  Summing it slot by slot
gives the count identity; division by the common nonzero total gives the
profile identity.  Thus the square is derived from declared concrete records,
not inserted because a prediction theorem requests it.  The equality-of-
records clause is necessary: CPG-CM6 has equal pair profiles and unequal
composite profiles, hence no `Phi` on those profiles.

**COR CPG8 (set-valued compositional prediction).**  Let a realised CPG3
scheme yield a net `vPair:I->VPair`, and assume CPG5, CPG7, compact `VPair`,
Hausdorff `VComp`, and continuous `Phi`.  Then

`PredComp=Cl_I(vComp)=Phi(Cl_I(vPair))=Phi(PredPair)`.

This is a specialization of PF1, not a new cluster theorem.  It is a
scientist-level L2 predictive assignment only after paired generation,
composite generation, both record maps, `Phi`, and the certified PF hypotheses
have descended.  Otherwise the relevant verdict is `NOT REALIZED` or
`COMPOSITIONAL PROFILE TRANSPORT NOT DEFINED`.

## Principal no-go boundaries

**NO-GO CPG9 (marginals do not determine composite prediction).**  Marginal
generators and marginal predictions do not determine `Gamma2`, `circ#m`, a
composite profile, or its cluster content.  CPG-M2 has equal two marginal
multisets but `m+ != m-` and `circ#m+ != circ#m-`; constant nets give distinct
singleton composite predictions.  Thus

`process composition + marginal prediction => composite prediction`

is false. No product formula from the two marginal generators is a typing rule
or an L2 operation; CPG-M10 is only a declared product-like pairing control.

**NO-GO CPG10 (transport firewall).**  A process-refinement map and
composition at each level do not imply that generation, records, profiles, or
cluster content commute with refinement.  The required squares are independent
interfaces.  CPG-M8 violates the generation square despite valid process
refinement and composition at both levels.  CPG-M9 shows that changing raw
carriers needs the full pair/generator/record/profile/cluster interface, not
only process-quotient equivalence.

## Audit and maturity

Q-audit: PASS.  Every admitted datum is a factor of a declared concrete map;
failed factors are retained as no-go results.  No probability, independence,
time, history, tensor, global process space, selector, or L3 representation is
used.  Presentation invariance holds only under the complete CPG-M9 interface.
The finite pushforward and PF1 corollary are standard mathematics; the
specialized content is the L1-to-L2 realization and record-factor audit.

Smallest irreducible addition beyond `circ` is a **realized joint generated
multiset interface**; to obtain prediction rather than only composite batches,
it must be accompanied by a descended composite-record factor.  `E_pair`
itself is eliminable notation for `Comp`, not a new primitive.
