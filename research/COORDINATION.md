# Finite coordination and global extension

# Neutral coordination formalism

## DEF CO-D1 — supplied many-sort relation record

Work on one declared finite inventory I, not all perspectives. Each A_i is a
typed local carrier, optionally with an independently supplied signature S_i.
Let E be a finite inventory of relation identifiers alpha with finite nonempty
scope J_alpha subset I and supplied R_alpha subset product_{i in J_alpha} A_i.
The user's R_J is the subcase with at most one identifier per scope. Repeated
scopes may record distinct procedures; none of our principal witnesses require
them. All coordinate roles are declared, not inferred identity of entities.

An extensional relation table is a complete allowed-tuple specification for
its stated sector. A sampled positive tuple is not a negative-membership oracle.
If a test is partial, carry its supplied domain D_alpha and its defined output;
unknown tuples stay unknown. A missing interface differs from a supplied empty
relation. Optional unary admissibility D_i subset A_i is supplied; by default
the synthetic fixtures explicitly use D_i=A_i. Products express finitely
typed input ports; no common raw source, world state or selected tuple is
postulated. Equality of reused ports is itself part of this encoding.

| Object | Type / level / dependencies / role / uniqueness / equivalence |
|---|---|
| I,E,J_alpha | Finite role/interface inventory and scope map; L0 chosen diagnostic syntax; supplied boundary; transported with roles |
| A_i,S_i,D_i | Typed sets/signatures/subsets; L0 representational fixture, or L1 supplied local procedure sector; chosen, not core; local empirical equivalence when provided |
| R_alpha,D_alpha | Finite-arity relation / optional decision domain; L0 diagnostic fixture or L1 supplied interface; chosen; product empirical equivalence in every port |
| q_i:A_i -> X_i | Optional surjective local empirical quotient; L2 derived from represented tests using T0; unique up to adequate quotient isomorphism |
| C=(A,R) | Inventory record; L0 diagnostic, or a declared L1 record of already supplied data; never an additional carrier of arrangements |
| b_i:A_i -> A'_sigma(i) | Adequate bijections preserving S_i, D_i, every relation and domain, with inventory permutation sigma; L0 representational, chosen |
| s_i:A'_i -> A_i | Optional changing-carrier quotient legs; L0/L1 supplied, their empirical use separately admitted; not assumed inverses |
| Sol(S), Q_S^L | Join witnesses / projected query relation for finite S subset E and named ports L; L0 derived diagnostic, unique; whole diagram transport |
| B,Z,F,U | Named finite comparison class, record alphabet, query B -> Y and forgetful B -> Z; L0 diagnostic, chosen contrast and class; not a universal model space |

Other symbols and optional enrichments are typed in their individual documents.
No new core primitive is introduced. L3 appears only in recognition, not here.

## PROP CO1 — exact relational empirical descent (standard T0.4)

Assumptions: surjective q_i, complete typed relation R_alpha and, for partial
decisions, a declared domain. R_alpha descends *exactly* as membership iff it is
saturated on product q-fibres; the decision domain must also be saturated.
Then R_alpha=(product q_i)^(-1)(bar R_alpha), uniquely on occupied quotient
tuples. Proof: membership is fibre-constant iff the inverse-image equation
holds; surjectivity gives uniqueness. The image relation alone is always a
set but is only an existential weakening when saturation fails.

CM M14: A={0,1}, q constant, R={0}. Its image is nonempty but raw membership
does not descend. This prevents importing L0 tables as scientist-level facts.

## THM CO2 — adequate diagram transport

Assumptions: CO-D1 and bijections b_i plus a scope-preserving inventory map
carrying every table/domain/signature. Coordinatewise transport gives a
bijection Sol(S) -> Sol'(sigma S), commutes with named projections, and
transports minimal incompatible supports and computed query relations.
Proof: a tuple satisfies each table exactly when its transported tuple satisfies
the corresponding table. Apply the inverse bijections. This also covers empty
solution sets; no choice of a solution is needed. CM M10: relabel one port
without transporting its incident table and the conclusion can fail.

This is invariance under *declared adequate* re-presentation, not all encodings.
Local isomorphisms without coherent interface transport are insufficient.

## PROP CO3 — changing carriers without selecting representatives

Assumptions: supplied surjections s_i and exact inverse-image equations
R'_alpha=(product s_i)^(-1)R_alpha, with domains likewise and local signatures
adequately compared. Coordinatewise s induces a surjection Sol'(S)->Sol(S)
for finite scopes: choose a preimage of each of finitely many coordinates.
Emptiness, and query relations after applying s to their endpoints, are
preserved. Raw solution count/uniqueness need not be: M15 duplicates labels.
Theorem uses finite choice only as proof of existence, never an empirical
selector. For section-preserving refinements with only inclusion of images,
empty coarse solutions still imply empty rich solutions, but converse fails.

CM M16 drops exact inverse-image coverage: rich anti-parity tables project
individually to coarse universal tables, yet the rich join is empty. Coarse
existence does not lift. The finite common quotient equations certify only
these properties; they are not a claim of unrestricted Morita equivalence.

## Q-audit and empirical firewall

Use a *separate* extension-forgetting U on a named comparison class. CO2 is
coordinate invariance, not Q-descent under arbitrary loss of content.
For U_local forgetting every interface, parity-cycle obstruction varies while
each A_i and S_i is fixed: NEW THEORY REQUIRED relative to that local reduct.
For U_pair forgetting supplied higher-arity tables, M4 has different full joins
with identical binary information: NEW THEORY REQUIRED. Relative to the whole
declared C, Sol and query projections are deterministic diagnostics and pass
the no-free-fact test. They cannot select a tuple, guarantee an executable joint
procedure or determine ontology. Saturated L2 tables license derived abstract
relations; access to their derived answers still needs RR/CRS availability.

All positive claims are conditional on an inventory with independently
motivated operational provenance when used empirically. No physical claim is
made for the synthetic inventory. Dependency: T0/T1 + supplied tables -> CO;
no reverse L3 edge and no backbone change.

# Positive obstruction content

## DEF GO-D1 — obstruction supports and extension queries

For finite supplied E, the obstruction antichain
`M(C)={S subset E: Sol(S)=empty and every proper subset has nonempty Sol}`
is L0 derived diagnostic, unique, CO2-invariant up to identifier transport.
It retains which interfaces jointly conflict, their scope incidence and each
deleted-interface witness. It is not a numerical curvature or cohomology class.
For a named subinventory S and endpoint ports L subset V(S), define
`Q_S^L=projection_L Sol(S)`; L0 diagnostic, uniquely derived; output role
equivalence is transported. This query is NEVER called prediction when Sol(S)
is empty. For disconnected added ports, supply their unary carriers explicitly.

## THM GO1 — complete finite obstruction certificate

Assumptions: finite E, complete tables/decision sectors, diagnostic conjunction
semantics CO-D2. Sol(E) is empty iff M(C) is nonempty. More generally Sol(S) is
empty iff S contains an element of M(C). Proof: descend through the finite
subsets to a minimal empty one; upward closure of incompatibility gives the
converse. Hence M(C), not just one Boolean failure, predicts which deletions
leave an inconsistent subinventory. Its members can be transported by CO2.

CM: finite assumption removal is substantive. On one declared integer carrier,
R_n={x:x>=n}, every finite subfamily is nonempty but their infinite intersection
is empty, so no finite obstruction support exists. This is a diagnostic countable
countermodel, not a universal repertoire or infinite core completion. On partial
positive-only data no certificate of empty joins follows (M19). Invariance
requires transporting scopes and tables (M10). No proof assistant is claimed.

## THM GO2 — independent further coordination query

Assumptions: complete finite S, nonempty Sol(S), new supplied relation T on
L subset V(S), and fixed joint port semantics. Then
`Sol(S union {T}) != empty iff Q_S^L intersection T != empty`.
Proof: restrict a joint witness; conversely any tuple in the intersection has
an extension witnessing its membership in Q_S^L. This is an exact query law,
not a claim that T is inferable or physically implementable. An empty Q yields
INCONSISTENT_INPUT rather than vacuous universal prediction. M17 withholds T
while deriving Q from two independent binary tables. Each alone has universal
projection to the two endpoints, while their composition forces endpoint
agreement. Add the independently specified anti-table: incompatibility follows.
Changing either original table changes the query with the other fixed.

This satisfies the four formal conditions of the user's strongest box under
the declared comparison class: multi-table invariant; no local or single-table
determination; independently computed consequences for later queries.
Its status is standard join/projection inference, not mathematical novelty
or new physical emergence. Query selection is synthetic and known in advance.

## THM GO3 — persistence class, and a forbidden repair

Assumptions: a refinement supplies per-port maps s_i and every refined allowed
tuple projects to an old allowed tuple on the corresponding scopes. A refined
section would project to an old section. Hence an old empty join stays empty
under EVERY refinement in this stated class. Proof: apply each s_i to the tuple
and check each old constraint. This proves a whole class result, not merely
tested examples. M16 shows converse failure. M20 changes a table or drops
constraint preservation and emptiness can disappear.

With carriers/tables fixed, adding a constraint only shrinks Sol. A strict old
obstruction cannot disappear by adding an interface alone. This kills a literal
required-zoo scenario; M19 supplies its legitimate epistemic variant: an
*apparent* obstruction resulted from comparing different unbridged labels.
New supplied comparison evidence corrects that formerly undefined question.
It does not make an inconsistent old conjunction consistent. A new bridge
replacing old port-equality semantics is an enriched theory, not refinement.

## Taxonomy of failure (DEF diagnostic classification)

| Diagnosis | Exact test / limitation |
|---|---|
| Insufficient information | Named extension class gives multiple query answers; not empty input; positive-only observations cannot establish complete tables |
| Inconsistent table | One effective supplied table empty; minimal support size one |
| Inconsistent interface pair | Two nonempty tables with disjoint shared images; minimal support size two |
| Contextual support obstruction | Nonempty overlap-consistent measurement-cover support tables with no section; qualified recognition, not arbitrary noisy-data contradiction |
| Missing interface | Comparison graph/domain/bridge absent; requested operation NOT DEFINED, not a false membership |
| Representation surplus | Answer varies on a declared reduct/adequate quotient fibre; Q says NEW THEORY REQUIRED |
| Higher-order incompatibility | Minimal obstruction of >=3 constraints, or irreducible arity >=3 table; distinguish these two axes |

## PROP GO4 — join-tree positive control (standard)

Assumptions: finite nonempty tables on scopes admitting a supplied or proved
tree with the running-intersection property (for every port, containing scopes
form a connected subtree); adjacent overlap projections equal. Then every table
tuple extends to Sol(E). Proof: root at that tuple's table, choose an adjacent
matching tuple by equal projections, and traverse the finite tree. Running
intersection ensures every already assigned port in a new table occurs in its
parent, so no extra clash occurs. This proves G and X, not U. No tree or cover
is assumed for the neutral framework.

Removal models: empty table defeats positivity; M5 defeats overlap equality;
M1 violates running intersection on any scope tree and defeats G; M3 shows
no uniqueness even with coherent tables. A derived join tree is diagram syntax,
not a spatial topology. Conditional recognition: acyclic database joins/CSP,
not universal sheaf gluing. Q-audit: topology/geometric interpretation does
not descend from these tables. Dependencies GO use CO only; backbone unchanged.
