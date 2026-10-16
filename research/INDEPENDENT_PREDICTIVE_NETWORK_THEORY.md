# Independent Predictive Networks — exploratory non-baseline theory

## Scope and status

This is a finite L0/L1-to-L2 exploration over separately declared local
predictive theories.  It supplies no global carrier,
or a theory of persistent agents.  `A`, `B`, and `C` name typed local
predictive systems only.  All quantification below is over the finite,
explicitly declared joint-realization language of one protocol; it is never a
space of all worlds, experiments, or continuations.

## 1. Minimal local predictive theory

**DEF IPN1 (local predictive theory).** A local theory is
`T_i=(X_i,q_i:E_i, H_i, prec_i, Pred_i, V_i)`, where `X_i` is a declared raw
record carrier, `q_i:X_i -> E_i` is its empirical quotient, `H_i` is a
finite declared family of local record histories, `prec_i` is a partial
precedence relation on slots of each history, `Pred_i(h)` is a nonempty finite
set of admissible subsequent record readouts for a declared prediction slot
of `h`, and `V_i` is a finite declared local verification grammar.  The
operational clause is: the antecedent slots of `h` are `prec_i`-below its
verification slot.  `prec_i` need not be total and is not called time.

Type/level: `X_i,H_i,prec_i,Pred_i,V_i` are L0 presentations of L1 content;
their quotient-descended parts are derived L2.  Dependencies: Frozen Core
§§3–8 and T0.4-style descent.  Status: derived, not core.  Each local map,
domain, and prediction readout must separately descend through `q_i`.

**NO-GO IPN2 (independent product firewall).** From two IPN1 theories alone,
`E_A x E_B`, a map between its factors, a common index, and a common event
carrier are not L2 data.  They are bookkeeping at most.

*Proof.* No L1 procedure has been declared whose saturated graph could factor
to any of these objects.  Choosing a pairing of two unchanged local carriers
varies an extension inside the fibre of the forgetful map erasing that
pairing.  This is the declared-interface requirement specialized to the local
predictive setting.

## 2. Endogenous interaction datum and admission

**DEF IPN3 (finite challenge–response interface).** A bridge declaration
`P_AB` consists only of: a finite code alphabet `C`; named A-side roles
`make(c)`, `send(c)`, and `receive(r)`; named B-side roles `receive(c)` and
`respond(r)`; finite local procedure graphs producing those records; and a
finite verification grammar saying which response records are accepted for
which code records.  Every stated role has a local precedence witness
(`make(c) prec_A send(c) prec_A receive(r)` or
`receive(c) prec_B respond(r)`).  The declaration does **not** assert that
an A send-slot and a B receive-slot are one event, nor that equal labels are
one record.

**DEF IPN4 (admissible bridge realization).** Fix finite role-address sets in
the two local histories and a finite interface language `Lambda_P` generated
by IPN3.  An admissible realization `j` is a tuple of maps from only the
named role-addresses to `C` and response labels, satisfying:

1. each component is a quotient-descended local readout and obeys its own
   local precedence and `Pred_i` rule;
2. each declared send/receive and response/verification clause of `P_AB`
   holds as an interface constraint;
3. a relation or map claimed from the interface is constant on every product
   of local empirical fibres on its stated domain.

`J(P_AB;T_A,T_B)` is the finite set of such tuples.  It is a diagnostic L0
class, not a joint world or a selected realization.  If clause 3 fails for a
claimed translation, that translation is `HIDDEN_Q_DEFECT / NOT DEFINED AT
THIS QUOTIENT`.

**DEF IPN5 (shared bridge fact).** For a finite target `Y`, a candidate
`F:J(P_AB;T_A,T_B)->Y` is a shared fact precisely when it is constant on the
nonempty declared class `J` and invariant under adequate transport of all
local quotients, role graphs, code and verification tables.  A local fact is
one of `Sigma_i`; a bridge fact is a descended interface relation; a derived
shared invariant is an IPN5 fact; a global representation is an optional L0
simultaneous coordinate realization of several bridge facts.  Any coordinate
property that varies between such representations is global surplus.

This is a bounded, protocol-relative version of fibre invariance, not a
postulate about every translation one could imagine.

## 3. Two-theory results

**THM IPN6 (relative translation admission).** Assume IPN1–IPN4, a finite
role translation candidate `tau_tilde` on raw named records, and quotient
saturation plus fibre constancy in every local input/output.  Then it has a
unique partial L2 bridge translation `tau` on the image of the declared role
records.  Conversely, a variation on one such fibre blocks `tau`.

*Proof.* Apply empirical descent to the finite, typed graph of
`tau_tilde`; partial domain saturation gives the exact domain.  Neither an
off-image extension nor a pairing of unnamed records follows.  Dropping
fibre constancy is IPN-CM7.

**THM IPN7 (asymmetric-word relative synchronization).** Let each of `T_A`
and `T_B` have a declared cyclic predictive sector of length `n`, whose local
coordinate is ambiguous under cyclic relabelling.  Assume a declared bridge
`P_AB` carries the finite word `w` from an A send-role sequence to B receive-
role sequence, and that its observed placements are `a` and `b` in the two
cycles.  If the only cyclic shift stabilizing `w` is zero, then every
admissible bridge realization induces the same relative offset
`delta_AB=b-a (mod n)`.  No absolute origin is induced.

*Proof.* A candidate alignment with shift `d` sends the observed A word to
the B word rotated by `d-(b-a)`.  Equality of the declared code records and
trivial stabilizer force `d=b-a`.  Simultaneously adding `s` to both local
coordinates leaves `d` unchanged and yields another global coordinate
realization.  Thus the conclusion is relative and has IPN5 descent.  The
nonperiodicity is a property of a recorded code word, not a preassigned
offset.  For `n=6`, `w=001011` is a finite control with trivial cyclic
stabilizer.

**CM IPN8 (periodic ambiguity).** For `n=4` and `w=0101`, shifts `0` and `2`
both stabilize the word.  With the same local prediction rules and bridge
grammar, placements permit two offsets.  Hence periodic correlation does not
license synchronization.

**CM IPN9 (orientation ambiguity).** If `P_AB` records only an unordered
cyclic multiset of code labels, or if both orientations of the receive-role
precedence are declared admissible, a word and its reversal give distinct
forward/reverse alignments.  No orientation fact descends.  Direction is
available only when the declared send/receive precedence graph distinguishes
it; it is not supplied by correlation.

**CM IPN10 (labels and bare correlation).** Equal labels in `E_A,E_B`, or
equal marginal predictive profiles without IPN3, admit every bijection of
the relevant finite slots.  There is no bridge fact.  This is CI11 applied to
cross-theory syntax: it establishes neither correspondence nor identity.

**PROP IPN11 (joint rigidity without absolute rigidity).** In IPN7 each
local cyclic sector separately leaves its phase origin undetermined, while
the interaction records fix `delta_AB`.  A simultaneous coordinate pair
still has the surplus transformation `(x_A,x_B) -> (x_A+s,x_B+s)`.  Thus
the positive datum is not an origin, event identity, or global clock.

## 4. Finite networks

**DEF IPN12 (network realization).** For a finite declared graph of local
theories and IPN3 bridges, a network realization is a compatible selection
of bridge realizations from their declared finite classes, with each shared
local role readout assigned one value.  It contains no added global carrier.
A global phase representation, when requested, is an L0 choice of phase
coordinates `x_i` realizing every admitted edge equation
`x_j-x_i=delta_ij`.

**THM IPN13 (three-node cycle criterion).** Assume three cyclic sectors over
`Z_n` and admitted orientation-preserving bridge offsets.  A global phase
representation exists iff

`delta_AC = delta_AB + delta_BC (mod n)`.

When it exists, its simultaneous common shifts are surplus; every edge
offset and every cycle sum is invariant across the representations.

*Proof.* Necessity follows by substituting the three edge equations.  For
sufficiency set `x_A=0`, `x_B=delta_AB`, and
`x_C=delta_AB+delta_BC`; the displayed equality realizes AC.  Adding a
constant to all three produces all origin changes.  This coordinate proof is
L0 only; the L2 conclusion is the relation among already admitted bridge
facts.

**CM IPN14 (pairwise bridges, no global phase representation).** Over
`Z_5`, let the three individually verified bridge offsets be
`delta_AB=1`, `delta_BC=1`, and `delta_AC=1`.  Each pair has a valid finite
bridge, but IPN13 fails (`1 != 2 mod 5`), so there is no global phase
representation.  This is not automatically a contradiction in any local
theory; it reports a network-level incompatibility of these declared bridge
claims.

**CM IPN15 (global representation nonuniqueness).** With
`delta_AB=1`, `delta_BC=2`, and `delta_AC=3` over `Z_5`, global phase
representations exist, but `(0,1,3)` and `(4,0,2)` encode the same bridge
facts.  Absolute origins are Q-relative to the bridge signature.

## 5. Verdict

**VERDICT: `SHARED_INVARIANT_EMERGENCE_PASS` (finite conditional scope).**
The results concern relative translation/calibration and cycle constraints only.
It has a positive witness (IPN7/IPN11): neither local theory fixes the offset,
declared interaction records jointly fix it, the bridge does not contain an
offset field, global coordinates retain a common-shift surplus, and adequate
transport preserves the fact.  It does not derive event identity, a global
world, global time, or a canonical synchronization.  The underlying theorem
is standard finite synchronization/constraint satisfaction; the distinctive
Q-exclusion contribution is the admission boundary separating endogenous,
descended interaction constraints from external matching and global surplus.
