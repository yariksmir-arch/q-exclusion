# Compositional Record Sufficiency

## Scope

**Status:** certified finite, declared-support calculus.  Phase I and CP/CPG
remain unchanged.  This module asks whether already declared pair-side records
are enough to determine already declared composite-side records.  It neither
creates a probe nor extends a record value outside a generated image.

Let `S subseteq E_pair` be a declared generated support (or the union of an
explicitly declared family), `r:S -> L_pair` a descended pair-record map, and
`c:S -> L_comp`, `c(g,f)=r_comp(g circ f)`, a descended composite record map.
All maps are derived L2 maps; `S` is derived from a declared L1 procedure;
label carriers are record interfaces, not process identities.  No object here
is core or representational.

## Exact factorization

**LEMMA CRS1 (typed image factorization).**  A map
`kappa:im(r)->L_comp` with `c=kappa o r` exists iff
`ker(r) subseteq ker(c)` on `S`, equivalently iff
`r(x)=r(y) => c(x)=c(y)` for `x,y in S`.  If it exists it is unique on
`im(r)`.

*Proof.*  Necessity follows after applying `kappa` to equal record values.
Conversely define `kappa(ell)=c(x)` for any `x in S` with `r(x)=ell`.
The kernel inclusion makes this independent of the witnessed preimage.  The
definition proves the factor identity and every factor has this value.  No
value is defined on `L_pair minus im(r)`; an extension there is new, unused
label content.

**THM CRS2 (record sufficiency).**  Under the typed descended data above,
the pair-record interface is sufficient for the declared composite records
exactly under the condition in CRS1.  Its only certified factor is the unique
image factor `kappa_S`.

This is standard kernel/quotient factorization, not theorem-level novelty.
CPG7 is its generated-support instance; it must therefore be read as
`SCHEME_LOCAL_RECORD_FACTOR` unless a larger declared support is separately
checked.

**NO-GO CRS3 (support-relative boundary).**  Let `S={x0}`, `S'={x0,x1,x2}`,
with `r(x0)=a`, `r(x1)=r(x2)=b`, and `c(x0)=0,c(x1)=0,c(x2)=1`.
Then `kappa_S(a)=0` exists, whereas no factor exists on `S'`.  Thus a factor
does not extend from generated support by selecting representatives or label
values: the exact status outside `S` is `SUPPORT_RELATIVE_ONLY`.

## Diagnostic versus available refinement

**DEF CRS4 (diagnostic kernel refinement).**  Put
`theta_r=ker(r)`, `theta_c=ker(c)`, and
`alpha=theta_r intersection theta_c` on `S`.  This is a diagnostic L0/L2
equivalence partition, derived from the two descended record maps.  It is not
a newly available pair observation.

**PROP CRS5 (minimal diagnostic sufficiency).**  `alpha` is an equivalence,
is contained in `theta_r`, makes `c` constant on each of its classes, and is
the greatest equivalence below `theta_r` with that property.  Hence the
quotient `S/alpha` admits a unique diagnostic factor to `L_comp`.  For a
finite family `c_j`, replace it by
`alpha=ker(r) intersection intersection_j ker(c_j)`.

*Proof.*  Kernels and intersections of equivalences are equivalences.  The
definition gives `alpha subseteq ker(c)`.  If `beta subseteq ker(r)` and
`beta subseteq ker(c)`, then `beta subseteq alpha`; quotient factorization is
CRS1.  “Coarsest refinement” is partition language for this greatest
subequivalence, not a claim that the quotient is concretely observable.

**DEF CRS6 (declared available probe grammar).**  `A_pair` is an explicitly
declared L1 grammar of pair-side probes whose readouts independently descend
to maps `h:S->O_h`.  It is a derived availability interface, never the class
of all set-theoretic functions on `S`.  For finite declared probes,
`rhat=(r,h1,...,hn)` is a descended L2 record precisely when the joint raw
readout passes empirical descent; its kernel is
`ker(rhat)=ker(r) intersection intersection_i ker(hi)`.

**THM CRS7 (concrete sufficient-record realization).**  Under CRS6, `rhat`
is sufficient exactly when `ker(rhat) subseteq ker(c)`.  It realizes the
minimal diagnostic repair exactly when `ker(rhat)=alpha`; strict containment
is sufficient over-refinement, not minimal repair.  On finite `S`, a finite
subfamily realizes a required separation only if such separating probes are
actually grammar-generated; finiteness never turns a mathematical function
into a probe.

*Proof.*  Apply CRS1 to `rhat`.  Equality with `alpha` is the definition of
exact realization.  The finite statement is merely finite selection from an
already declared separating family.

**NO-GO CRS8 (unavailable discriminator).**  On `S={u,v}`, take constant
`r`, `c(u)=0,c(v)=1`; then `alpha` is equality and the function separating
`u,v` exists mathematically.  If every member of declared `A_pair` is
constant, every available joint record remains constant and is insufficient.
Verdict: `RECORD SUFFICIENCY NOT REALIZED`.

**NO-GO CRS9 (outcome leakage).**  The same model has `h=c` as a mathematical
separator, and adding it makes factorization tautological.  Since `c` is a
composite-output record, it is not a pair probe merely by being definable.  In
the absence of an independent declared L1 pair-side implementation whose
readout descends to `h`, the verdict is `NOT AVAILABLE AS PAIR RECORD`.

## Protocol families and refinement axes

**THM CRS10 (stable family factor).**  For a declared family of supports
`{S_gamma}`, set `S_G=union_gamma S_gamma`.  One factor
`kappa_G:im(r|S_G)->L_comp` works for every member iff
`ker(r|S_G) subseteq ker(c|S_G)`.  It is unique on its image.

Per-support factors do not suffice: with `S1={x}`, `S2={y}`, `r(x)=r(y)=a`
and `c(x)=0,c(y)=1`, both local factors exist but no union factor does.
Conversely, if local factors agree wherever their record images overlap, their
common values define the unique factor on the union.  This is ordinary
pasting consistency; its project-specific force is that `S_G` must be
declared rather than silently enlarged.

Three distinct axes must be retained: (E1) empirical process refinement
`rho_E:E'_P->E_P`, (E2) enlargement of the declared pair-probe repertoire,
and (E3) support/protocol expansion.  CRS3 shows E3 can destroy sufficiency
with unchanged composition.  E2 can restore it only through CRS7.  Under E1,
a coarse factor need not lift when fine composite records split a coarse
value; a fine factor descends only with declared record transports.  These are
not interchangeable operations.

## Predictive and admission consequence

When CRS10 and CRS7 hold on the exact declared support family, CPG5/CPG7 give
the count identity and CPG8/PF1 give `Pred_comp=Phi(Pred_pair)` in their
existing finite topological scope.  The predictive label is then
`ROBUST_COMPOSITIONAL_PREDICTION_INTERFACE` only after the transport theorem
in `COMPOSITIONAL_RECORD_TRANSPORT.md` applies.  Otherwise it is
`SCHEME_LOCAL_COMPOSITIONAL_PREDICTION` or the earlier CPG-certified scope;
no probability, kernel, Markov property, linear operator, category, or
monoidal structure follows.

## Audits

**Q-audit:** PASS.  `r`, `c`, and every admitted `h` are required to descend;
`alpha` is explicitly diagnostic.  No representative, support, extension, or
outcome-shaped coordinate is selected.

**Presentation audit:** all claims are invariant under adequate transport of
the stated supports, record maps, and available grammar—not under bare label
renaming or raw-carrier comparison alone.  See CRS-T1.

**Dependency impact:** `CPG5 -> CPG7 -> CRS1/2 -> CRS7/10 -> CRS-T1 -> PF1`.
No Phase-I or CP/CPG repair, and no backbone change, is proposed.
