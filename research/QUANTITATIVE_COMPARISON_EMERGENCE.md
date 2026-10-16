# Quantitative Comparison Emergence

## Status and scope

This is a finite declared-interface comparison module.
Its admitted general result is **`COMPARISON_RELATION_ONLY`**.  The model zoo
contains conditional preorder, partial-order, ordered-partial-composition, and
cancellative controls; those controls do not promote their additional L1 data
to the ordinary S1 signature.

The direction is strictly

`declared L1 comparison -> E_Q,Sigma_Q -> comparison relation -> optional declared composition -> late recognition`.

No magnitude, numerical coordinate, order completion, totality, probability,
or concatenation is primitive.  Comparator outputs are finite procedure labels.

## Typed interface

**DEF QC1 (raw comparison interface).** Let `X0` be an L0-presented L1 raw
carrier, `R_Q` a declared repertoire, `q:X0 -> E_Q=X0/~_Q` its L2 quotient,
and `Ctilde:D_C -> O_C` a declared partial L1 comparator, where
`D_C subseteq X0 x X0` and `O_C` is a declared output-label carrier (for
example `{left,tie,right,undetermined}`). `Ctilde` is derived only as a
concrete procedure; it has no order or numerical semantics. Dependencies:
`X0,R_Q,D_C,Ctilde`.  The domain need not be all pairs.

**THM QC1 (partial comparator descent; T0.4 specialization).** A unique L2
partial map `Cbar:Dbar_C -> O_C`, with
`Cbar([x],[y])=Ctilde(x,y)` and `Dbar_C=(q x q)(D_C)`, exists iff:

1. `D_C` is saturated under `~_Q x ~_Q`; and
2. whenever `(x,y),(x',y') in D_C`, `x~_Qx'`, and `y~_Qy'`, then
   `Ctilde(x,y)=Ctilde(x',y')`.

*Proof.* Necessity pulls back the domain of `Cbar` and its commuting value
square.  Under (1), membership of `Dbar_C` is representative-independent;
under (2), the displayed formula defines a function. Surjectivity of `q x q`
gives uniqueness. **Failure witness:** QC-M2 violates (2), so the verdict is
`COMPARISON NOT DEFINED AT THIS QUOTIENT`, not a selected representative.

**DEF QC2 (interpreted comparison relation).** Given a declared subset
`L_leq subseteq O_C`, define the L2 relation
`x <=_C y iff (x,y) in Dbar_C and Cbar(x,y) in L_leq`. This is derived L2;
it depends on the stated label interpretation and does not reinterpret every
output as comparison. It is representative-independent by QC1.

**PROP QC3 (relation descent form).** A raw declared yes/no relation on a
partial pair domain induces a relation on `E_Q` iff its domain is pair-saturated
and its truth value is constant on every pair fibre. This is QC1 with output
carrier `{yes,no}`.

## Relational-law firewall

**DEF QC4 (law audit).** Reflexivity, transitivity, antisymmetry, and
completeness are separate finite or general L2 predicates of `<=_C`; none is
part of QC1. The weakest accurate status is used:
`COMPARISON_RELATION_ONLY`, `PARTIAL_COMPARISON_RELATION`, `PREORDER`,
`PARTIAL_ORDER`, `TOTAL_PREORDER`, or `TOTAL_ORDER`.

**NO-GO QC5.** Comparison does not imply preorder (QC-M5); preorder does not
imply partial order (QC-M6); partial order does not imply totality (QC-M7).
The transitive closure of a non-transitive descended relation is L0 diagnostic
only whenever it adds pairs.  It is not scientist-level content without an
independent concrete procedure licensing those pairs.

**THM QC6 (preorder quotient).** If `<=_C` is reflexive and transitive, then
`x approx_C y iff x<=_Cy and y<=_Cx` is an L2-defined equivalence and
`E_Q/approx_C` carries the induced partial order. *Proof:* the standard
preorder-quotient argument. **Scope:** this is a derived quantitative quotient;
it does not replace `E_Q`, because QC-M6/QC-M17 retain distinct empirically
distinguishable classes in one `approx_C` class.

## Refinement and realizability

**DEF QC7 (diagnostic comparator refinement).** The greatest equivalence
below `~_Q` on which the selected raw pair-domain and comparator output are
constant is an L0 diagnostic partition `theta_C`. It is a direct binary-data
instance of RR/T0.5 logic, not a repertoire extension.

**THM QC8 (finite realizable comparison refinement).** For finite `X0`, a
declared probe family realizes a proposed comparator repair precisely when
every available probe is sound on its proposed classes and their joint readout
partition separates every pair that `theta_C` separates. *Proof:* equality of
joint readouts is exactly the induced empirical equivalence. QC-M3 supplies an
available discriminator; QC-M4 proves that a set-theoretic splitter without a
declared probe yields `COMPARISON REFINEMENT NOT REALIZED`.

## Optional independent composition

**DEF QC9 (raw combination interface).** `oplustilde:D_oplus -> X0` is an
independently declared partial L1 implementation. It is neither the CP
sequential operation nor “addition.” Its L2 partial operation `oplus` exists
exactly under the ordinary partial-operation domain-saturation and output-fibre
constancy theorem.

**DEF QC10 (ordered partial composition).** If both data descend, right
(respectively left) monotonicity means `x<=_Cy => x oplus z<=_C y oplus z`
(respectively `z oplus x<=_C z oplus y`) whenever all displayed terms are
typed. These are distinct for noncommutative operations.

**NO-GO QC11.** Order plus descended composition does not imply monotonicity
(QC-M8). Monotonicity does not imply cancellation (QC-M9, max/join). Thus no
additive route is licensed. Same comparison reduct with join and meet-like
operations (QC-M10) also proves, by the RD reduct test, that comparison does
not determine composition.

**PROP QC12 (conditional admission).** A signature may be called
`ORDERED_PARTIAL_MAGMA` only when QC1/QC3, operation descent, and the stated
left/right law pass. Add associativity and an actually descended identity only
for `ORDERED_PARTIAL_MONOID`; add the exact typed cancellation law only for
`CANCELLATIVE_ORDERED_STRUCTURE`. QC-M13 and QC-M14 are positive controls,
not generic conclusions.

## Representation and presentation boundaries

**NO-GO QC13 (numerical surplus).** A numerical representation consumes an
already admitted L2 signature. It cannot define `<=_C` or `oplus`. QC-M12
shows that raw numeral strings are syntax; QC-M16 gives two coordinates for
one ordered presentation. Therefore existence, faithfulness, and rigidity are
separate L3 questions, and no coordinate value is an L2 fact unless it factors
through the declared reduct under RD1–RD12.

**REC QC-REC1 (admission rule).** A named numerical theorem may be audited
only by naming it and mapping every external premise to an L2 witness. The
ordinary branch is `BLOCKED`: no independently descended totality, rich
concatenation/difference comparison, cancellation, solvability, Archimedean
scheme, continuity, density, completeness, unit, ratio, or scale coordinate.
No missing premise is added. Finite profile ratios remain record arithmetic,
not an object-magnitude scale.

**THM QC14 (adequate transport).** Two changing-carrier presentations carry
the same QC signature only under explicitly supplied transports of `E_Q`,
comparison domain, comparator outputs or interpreted relation, optional
operation graph, indifference quotient, and relevant probes, commuting with
each claimed map. Bare ordered-set isomorphism, raw-carrier bijection, or
numeric relabelling is insufficient. QC-M11 is the positive full-interface
control; QC-M12 is the label-surplus control.

## Backbone minimization and verdict

Removing numerical labels, totality, composition, identities, indifference
quotient, and scales leaves the irreducible scientist-level signature:

`Sigma_QC = (E_Q, Dbar_C, Cbar, L_leq)`

or its interpreted partial relation `<=_C`. It is a **partial comparison
relation only**.  Preorder, partial-order, and ordered-algebra examples are
conditional extensions with their own L1 interfaces.

Q-audit: PASS — every admitted map/relation factors through `q`; refinement,
closure, quotienting, and coordinates are marked diagnostic/derived/L3 as
appropriate. Presentation audit: conditional PASS only under QC14. Circularity
audit: PASS — there is no `R`-representation-to-L2 edge. No backbone change.
