# Correlation-Induced Structural Identity — exploratory non-baseline audit

## Status and scope

This is an L0 diagnostic calculus over a **finite, declared** record theory.
This is an optional diagnostic module. A slot
is a syntactic address in one record, never a bearer or a persistent object.
The calculus may report forced co-reference facts, but it never chooses a
completion or promotes one to L1/L2.

## 1. Primitive vocabulary

**DEF CI1 (record theory).** A finite record theory is
`T=(C,(S_c)_c,L,Gamma)`, where `C` is a finite declared context family,
`S_c` is a finite L0 set of local slot addresses with `S_c cap S_d=emptyset`
for `c != d`, `L` is the finite declared L1 table of outputs, typed procedures,
relations, explicit same/distinct readouts, and `Gamma` is its finite generated
probe grammar.  Let `S=disjoint-union_c S_c`.

Type/level: `C,S_c,S` are L0 syntax carriers; `L,Gamma` are representations of
declared L1 content.  `T` is diagnostic, depends on the frozen concrete
repertoire discipline, and contains no individual carrier, world-state, order,
or global continuation.

**DEF CI2 (declared identity-extension language).** `Lambda_id` is a finite
typed language of *gluing predicates*, with an explicitly supplied satisfaction
relation `models_T` between equivalence relations on `S` and the declared
constraints in `L,Gamma`.  Its atoms can only inspect: declared readouts;
declared relation/procedure tables after the quotient map `q_J:S -> S/J`; and
explicit same/distinct readouts.  Every functionality, uniqueness, persistence,
or cross-record compatibility clause must occur as a named formula in
`Lambda_id` and be tested for descent from the concrete L1 procedure that
licenses it.  This language is an L0 diagnostic choice, not a universal
language of continuations.

**DEF CI3 (admissible co-reference completion).**
`J(T,Lambda_id)={J subseteq S x S | J is an equivalence relation and J models_T
(L,Gamma)}`.  Write `mathfrak J(T)` only with this declared `Lambda_id`
understood.  Each `J` is an L0 diagnostic extension datum.  It is not a
possible world, an ontology, or a selected partition; the set may be empty.

In particular, a repeated label is merely an L0 token unless `Lambda_id`
contains a separately declared, descended constraint relating its occurrences.
Likewise, relational-profile equality is not an admissibility rule unless it
is explicitly declared and justified.

## 2. Verdicts

**DEF CI4 (non-vacuous verdicts).** Only if `mathfrak J(T)` is nonempty, for
`x,y in S` define

`x equiv_T y iff forall J in mathfrak J(T), x J y`,

`x #_T y iff forall J in mathfrak J(T), not x J y`.

If neither holds, return `COREFERENCE_UNDERDETERMINED`; if the class is empty,
return `NO_COHERENT_IDENTITY_EXTENSION`.  Thus no universal statement is
evaluated over the empty class.

**THM CI5 (exact verdict trichotomy).** Assume CI1--CI4 and
`mathfrak J(T) != emptyset`.  For every pair `x,y`, exactly one of forced
co-reference, forced distinction, and `COREFERENCE_UNDERDETERMINED` holds.
Moreover `equiv_T` is an equivalence relation, while `#_T` is symmetric and
irreflexive but need not be transitive.

*Proof.* Each completion gives exactly one binary verdict.  Universal agreement
on yes gives `equiv_T`, universal agreement on no gives `#_T`, and disagreement
gives the third case.  The first relation is the intersection of nonempty many
equivalence relations.  A three-slot completion class allowing only the
partitions `ab|c`, `a|bc`, and `a|b|c` has `a #_T c` and `c #_T b`, but not
`a #_T b`, proving the final qualification.

**THM CI6 (joint-gluing criterion).** Let `P` be a finite set of requested
same/different literals on slots.  One simultaneous co-reference claim is
admitted exactly when some one `J in mathfrak J(T)` satisfies every literal in
`P`.  Pairwise satisfiability of the literals is necessary but not sufficient.

*Proof.* This is the definition of conjunction under one equivalence relation.
CI-CM7 supplies the strict counterexample.

## 3. Refinement and transport

**DEF CI7 (conservative record refinement).** A declared refinement
`i:T -> T'` is identity-conservative when it preserves old slots and extension
language, and restriction sends every `J' in mathfrak J(T')` to an element of
`mathfrak J(T)`.  Equivalently on a fixed slot set it has the exact inclusion
`mathfrak J(T') subseteq mathfrak J(T)`.  This is a condition to prove from
the new L1 procedures/readouts; merely calling data a refinement does not give
it.

**THM CI8 (monotonicity, with the nonempty hypothesis).** Under CI7, if both
completion classes are nonempty, every old forced co-reference and every old
forced distinction remains forced in `T'`.  An underdetermined verdict can
resolve either way.  If `mathfrak J(T')=emptyset`, the only verdict is
`NO_COHERENT_IDENTITY_EXTENSION`, so no monotonicity assertion is typed.

*Proof.* Universal predicates remain true after restricting their nonempty
quantifier domain to a subset.  CI-CM8/CI-CM9 show respectively why the two
qualifications are needed.

**DEF CI9 (adequate presentation transport).** An adequate relabelling from
`T` to `T'` is a sort/context-preserving bijection `h:S -> S'` carrying all
declared records, procedure graphs, grammar productions, and every
`Lambda_id` constraint to its named transport, such that
`J models_T L` iff `h_*J models_T' L'`, where
`h_*J={(h x,h y):(x,y) in J}`.

**THM CI10 (transport of verdicts).** Under CI9, `J -> h_*J` is a bijection of
completion classes.  Thus `x equiv_T y iff hx equiv_T' hy`, and similarly for
`#` and underdetermination; emptiness is also preserved.

*Proof.* `h` bijects equivalence relations and CI9 preserves satisfaction.
Apply the bijection to the nonempty universal quantifiers in CI4.  For a
categorical/global factorization claim about an entire presentation groupoid,
this pointwise theorem is insufficient: the required extension transport and
morphism coherence must instead be supplied under RD1--RD4.

## 4. Strategic no-go and admission

**NO-GO CI11 (bare correlations do not supply identity).** Assume
`Lambda_id` contains no constraint whose truth changes with a gluing relation
(`J models_T L` for every equivalence relation `J` on `S`).  If `|S|>=2`, no
two distinct slots are forced co-referent or forced distinct.

*Proof.* Both the discrete equivalence and the equivalence merging any chosen
two slots are admissible.  Hence their verdicts disagree.  This proves that
correlation tables alone force identity only through declared, gluing-sensitive
compatibility content.  It does not reduce that content to role equivalence:
CI-CM2 has different roles but forced co-reference.

**PROP CI12 (where information enters).** Explicit distinctness readouts,
or descended uniqueness/functionality/persistence constraints, can make
`mathfrak J(T)` smaller and hence force a verdict.  They are identity-like
L1 content only when their concrete procedures/readouts independently descend.
Their mere mathematical formulation is diagnostic and cannot be promoted.

**Admission.** CI5--CI10 are finite partition/fibre-constancy mathematics:
`REDUNDANT_WITH_EXISTING_Q_CALCULUS` at theorem level (T0/RR/RD specialized to
a newly declared extension datum).  The nontrivial architectural result is
interpretive: record theories can be read without primitive persistent
individuals, retaining only forced/forbidden/underdetermined gluings.  It is
not yet a new baseline theorem, because every positive force is relative to
`Lambda_id` and no independently motivated target has supplied it.
