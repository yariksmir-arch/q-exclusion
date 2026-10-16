# Independent Constraint Convergence (ICC) — exploratory audit

## Scope and status

This is a finite, protocol-relative L0/L1-to-L2 audit.  It does not change
the frozen core or the other optional modules.  `A`, `B`, and `C` are names of typed
local predictive systems, not agents, observers, persistent objects, or
components of a global history.  Every finite candidate class below belongs
to one declared protocol; it is not a space of all continuations or worlds.

**Main verdict: `ICC_PREDICTIVE_PASS` (restricted, standard mathematical
mechanism).**  The basic two-system effect is `STANDARD_CONSTRAINT_INTERSECTION`
and, as a repertoire change, `JUST_REFINEMENT`.  The three-system control
does yield a pre-verification AC prediction, but only after an independently
declared operational compatibility interface makes the two B-side constraints
jointly usable.  ICC is consequently a useful Q-exclusion admission rule for
ordinary constraint intersection, not a new general mathematical principle
and not a solution of the Input/Boundary Problem.

## Typed definitions

**DEF ICC1 (local predictive system).**  A local system is the IPN1-shaped
tuple `T_i=(X_i,q_i,H_i,prec_i,Pred_i,V_i)`: local raw records, its quotient,
finite local histories, local precedence, set-valued predictions, and a local
verification grammar.  Type/level: L0 presentation of declared L1 content;
quotient-stable readouts are derived L2.  Dependencies: Frozen Core §§3–8;
Formal Language A–D.  Status: derived/diagnostic.  `prec_i` is local only.

**DEF ICC2 (formation-isolation certificate).**  For a claim role `f_i` in
`T_i`, a certificate `I_i` is a finite declared formation graph listing every
typed input role on which `Pred_i(f_i)` and its relevant distinction depend.
For two systems, `Ind_form(A,B;F)` holds when: (a) each graph contains a
prediction role and its local precedence witness; (b) neither graph has an
input edge from a record/prediction/output role of the other system; (c) no
role of the later joint-verification interface occurs in either graph; and
(d) no cross-translation needed to state `F` occurs in both formation graphs.
All listed local maps must descend through their local quotients.

Type/level: a finite L0 audit predicate on declared L1 procedure graphs;
diagnostic, not an L2 relation.  Dependencies: ICC1 and explicitly declared
role typing.  It certifies *non-importation in the declared protocol*, not
absolute causal independence.  Calling it an absolute fact about unrecorded
provenance is `HIDDEN_Q_DEFECT`: two extensions may retain all listed graphs
while differ in an undeclared common source or prior consultation.

**DEF ICC3 (joint relevance interface).**  Let `P_AB` be a finite, newly
obtained interface record/procedure with typed A and B role addresses,
quotient-descended interface readouts, and a finite compatibility table
`C_AB`.  It is jointly relevant to a finite target alphabet `Y` when it
licenses comparison of the two prediction-output roles, without identifying
any A role with a B role.  Its output need not contain a member of `Y`.
Type/level: declared L1 interface; its fibre-constant relation is derived L2.
Dependencies: ICC1; product-fibre saturation and constancy.  Derived,
not core.

**DEF ICC4 (ICC determinacy).**  Let `J` be the nonempty finite class of
assignments to only the named protocol roles satisfying local prediction
rules and interface tables.  A target `F:J->Y` has ICC determinacy when
`Ind_form(A,B;F)` holds, neither local projected constraint makes `F`
constant, `F` is constant on `J`, and the new interface payload does not
itself equal or encode a selected value of `F`.  `F` is L2 only if it is
constant on every stated product empirical fibre and under adequate transport.
This is a bounded factorization test, never a selected realization.

**DEF ICC5 (operational composability certificate).**  For AB and BC
interfaces to constrain an AC prediction, an independently declared B-local
compatibility procedure `K_B` must have two named B role inputs and a
fibre-constant output saying which paired bridge readouts may be used
together.  Its formation graph must predate AC verification and may not use
the AC result.  Type/level: L1 procedure / derived L2 relation; diagnostic.
Absent `K_B`, relational composition is `NOT DEFINED AT THIS QUOTIENT`.

## Basic finite control

**PROP ICC6 (two-system joint narrowing).**  Assume ICC1–ICC4, target labels
`Y={F1,F2,F3}`, and locally formed predictive contents
`P_A={F1,F2}` and `P_B={F1,F3}`.  A newly obtained interface record `r` has
the sole payload `compatible(A-predict-role,B-predict-role)` and its declared
table permits exactly equal target labels; `r` contains no `F1`, `F2`, or
`F3` field.  Then `F=F1` is constant on the compatible class
`J={(F1,F1)}` although neither local content alone fixes it.

*Proof.*  The table restricts assignments to
`(P_A x P_B) intersect {(y,y):y in Y}`.  The only element is `(F1,F1)`.
Projection to either factor instead has two values.  Since the payload is
the compatibility tag/table rather than `F1`, the result is not direct answer
transmission.  Fibre constancy of the prediction and table is assumed; then
the constant target factors to the declared joint signature.  □

`r` adds a new jointly usable distinction, so the theorem is also exactly a
finite refinement of the *joint protocol repertoire*.  It is not refinement
of either local repertoire alone.  Therefore “ICC is more than refinement”
is false at this level; its precise role is to forbid calling arbitrary or
externally matched intersections an empirical refinement.

## Strong predictive control

**THM ICC7 (three-system pre-verification prediction).**  Assume ICC1–ICC5.
Each local prediction role has the binary output alphabet `{0,1}`.  Before
AC verification, independently verified interfaces declare:

`R_AB={(0,0),(1,1)}` and `R_BC={(0,1),(1,0)}`.

Their B roles are jointly usable only because a pre-existing B-local `K_B`
returns `compatible` exactly when their B readouts agree.  The separately
declared AC verification procedure will output one of `{equal,different}`
from named A/C roles; its interface table and output are not yet available.
Then every assignment satisfying AB, BC, and `K_B` has A/C pair in
`{(0,1),(1,0)}`.  Thus the system may fix, before AC verification, the
prediction `different` for that *new AC record*, provided the subsequently
obtained AC procedure is independently audited to read only this declared
equal/different relation.

*Proof.*  Enumerate the compatible assignments.  AB makes `a=b`; BC makes
`b != c`; the certified common B role gives `a != c`.  This is finite
constraint elimination, not arithmetic offset addition.  The AC procedure
is a distinct future interface; its eventual record independently checks the
prediction.  A coordinate presentation such as `0/1` is only a label
presentation: swapping both labels preserves `different`.  □

This is a real pre-verification prediction only under the final italicized
admission condition.  If AC's procedure is known in advance to output a
prewritten field from AB or BC, it is transfer; if `K_B` is absent, it is an
unjustified composition; if the AC result is used to choose the relation, it
is postdiction.

## Classification and boundary relevance

**NO-GO ICC8 (no absolute provenance from local records).**  No local-only
signature decides whether two formation graphs had an undeclared common
source or whether B was formed after learning A's result.  Proof: retain all
declared local graphs/readouts and add/remove an external provenance edge;
the local signature is unchanged.  Hence absolute causal independence fails
the Q-exclusion test.  The admissible replacement is ICC2's explicit,
falsifiable non-importation certificate.

**PROP ICC9 (boundary effect).**  Independently generated constraints can
force adoption of a distinction in the *joint interface signature* that no
one local signature selected: ICC6 forces `F1`; ICC7 forces the AC
`different` prediction.  They do not determine a uniquely correct initial
repertoire or theory boundary: an extension can retain all protocol facts
while add unused tests or alternative internal presentations.  The strongest
licensed reading is `ROBUSTNESS_UNDER_INDEPENDENT_CONSTRAINTS`.

The four phenomena remain distinct:

| phenomenon | diagnostic condition |
|---|---|
| replication | each local prediction already fixes the same `F`; no new joint restriction |
| information transfer | the new record contains `F` or an answer-equivalent field |
| refinement | an admitted new record refines an empirical quotient/signature |
| ICC | a formation-isolation certificate plus an answer-free, descended joint interface makes independently retained constraints jointly constant |

Every ICC instance is a type of joint refinement/constraint intersection;
not every refinement is ICC (it may be a local probe, transfer, or lack the
isolation certificate).

## Dependency and provenance

No backbone change is proposed.  New dependency path only:
`local signatures + ICC2 formation certificates + answer-free interface ->
finite joint constraint class -> optional L2 invariant/prediction`.

Mathematically ICC6 is ordinary intersection of constraint sets; ICC7 is
finite constraint satisfaction / relational composition after compatibility
is supplied.  It is close to independent confirmation and robustness
(separate support), identifiability and multi-view/data fusion (jointly
narrowed candidate class), distributed consistency (compatibility of local
constraints), and calibration/synchronization (only when a concrete bridge
supplies the relation).  No theorem novelty is claimed.  The Q-exclusion
contribution is architectural: it demands that cross-use, composability,
and the claimed invariant descend from a declared interface rather than be
silently supplied by a correspondence table or global representation.
