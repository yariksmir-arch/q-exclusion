# Models, exact assumptions and applications of existing results

## Typed data and status

**DEFINITION EA-D2.** Each example supplies its own finite carrier X (L0 representation of optional L1 sector data), partial procedure tables u:X⇀X, functional readouts p:X→O on declared domains, finite protocol words or bounded policies, and record map r:X→L. Alphabets, named ports and preparation support are chosen; no canonical decomposition is inferred. Kernels and quotient factors are derived L0 diagnostics, unique up to adequate transport; they are L2 only after domain and output descent. A diagnostic map need not be a physically implemented procedure. All examples are models, not empirical confirmations.

**DEFINITION EA-D3.** Availability at a configuration means that the named partial procedure is enabled there with declared input resources and routing. Enabled immediate probes, executable finite words, and the full contextual closure are three different repertoires. Construction steps are ordinary represented operations. Their finite dependency order is local to this toy and supplies no fundamental time. The examples use no common carrier of all future procedures.

## PROP EA-A1 — record and update applications (KNOWN)

Assume declared support S, descended functional record r:S→L and target h:S→Y. Then h factors through im r iff ker r⊆ker h, uniquely on that image (CRS1/2, AI1). For a partial update u:S⇀S, a partial update on im r with bar_u r=r u exists iff dom u is r-saturated and r u is constant on each enabled r-fibre (T0.4, CMQ7). Implementing either factor additionally requires an available decoder/update route (AI7, RR4–7).

Proof: necessity follows by applying the alleged factor to equal record values, including definedness. Conversely equal values specify one output and one domain flag, independent of a witnessed preimage. This is an application of existing factorization, not a renamed new theorem.

Failure witnesses: r constant and h(0)=0,h(1)=1 blocks sufficiency; identity r with no read route factors mathematically but is unavailable; r(0)=r(1) with u enabled only at 0 blocks domain descent; on {a,b,c}, r=(0,0,1), u(a)=a,u(b)=c blocks update descent. Retaining just one support point hides failures; expansion requires rechecking CRS10. Unbounded carriers do not inherit finite encoding bounds.

## CM EA-M1 — static closed and fully transparent controls

X={0,1}, read(x)=x, update=id, nondestructive copy x↦(x,x), a fixed grammar closed under these procedures. All declared distinctions are locally readable and the repertoire is final relative to this grammar. No self-reorganization follows. An explicit learner has readable registers (h,seen)∈{0,1}², predicts y=a XOR h for input a, and on an available labelled example (a,y) sets h:=a XOR y, seen:=1. For the supplied two-function task y=a XOR t, one correct labelled example sets h=t, so every subsequent input is classified correctly. Initial h, the training record and the learned h are all nondestructively readable. Learning changes the classifier without concealing any current internal register; labelled-example access is a supplied interaction, not a perfect universal teacher. Copying the complete current tuple preserves every subsequent transition in this classical model. Full specification and full nondestructive access are compatible with organization.

## CM EA-M2 — new labels without new interaction

X={00,01,10,11}; the sole source observation is a. Any new classifier d(a), however learned or named, is constant on ker a. It cannot determine b. Replicated records and injective recoding of a preserve this kernel (AI2). Adding b as a mathematical function is not implementing it (RR7). This kills classification-only creation of source distinctions. Richer statistical estimates from repeated noisy observations would require a separate independently justified observation law.

## CM EA-M3 — new access without reusable retention

A one-shot gate reads b on X={0,1}² and then resets the sole record to blank and disables itself. A transient readout distinguishes b, but no later record-only decoder recovers it. If a downstream receiver stores the output, that receiver is an added retention channel in the joint signature. Novel enabled access does not imply reusable articulation.

## CM EA-M4 — supplied self-maintenance and repertoire change

Named ports: x∈{0,1} is a preparation/context label; b∈{0,1} means sensor assembled; fuel f∈{0,1,2}; register r∈{blank,0,1}. X is their 36-element product, only this bounded sector. These values describe the toy's named ports, not an ontic global state. Available procedures:

| Procedure | Domain | Update/readout |
|---|---|---|
| build | f=2 | b:=1, f:=1 |
| read | b=1 and f>0 | r:=x; expose r |
| feed_i, i=0,1 | f>0 | f:=min(2,f+1) if i=x; otherwise f:=max(0,f−1) |
| decay | f>0 | f:=f−1 |
| erase | every configuration | r:=blank |
| break | every configuration | b:=0 |

Feed includes a supplied external resource channel with two selective routes. No energy conservation or autonomous origin is claimed. Starting with b=0,f=2,r=blank, build enables immediate read. The bounded recorded policy read;feed_r;decay maps any b=1,f=1 state to b=1,f=1,r=x. A subsequent read obtains the retained value, and the loop can be repeated in the specified deterministic table. This establishes an invariant fuel balance and actual use of the recorded discriminator within the toy.

**PROP EA-A2 (KNOWN invariant/finite induction).** Under exactly these tables, both x preparations and the supplied record-dependent controller, the preceding invariant holds for each finite number of loop repetitions. Proof: read leaves f=1; correct feed makes f=2; decay returns f=1. Induction uses only this local loop. It is not a theorem of biological closure or unlimited physical lifetime.

Ablations: omit feed and one decay exhausts f, disabling read; replace feed_r with feed_0 and the x=1 preparation exhausts f; omit build and the initial read stays disabled; delete routing from r and the required adaptive controller is unavailable. These failures independently test resource response, discrimination, construction and usable composition. They do not define destruction as removing the definition of organization: the measured output is successful later read availability under unchanged resource accounting. An external correct open-loop feed can sustain each fixed x, so hidden information and record-dependent feedback are not universally necessary.

The initial immediate repertoire does not distinguish x, while the post-build read does. But the full pre-build grammar containing build;read already distinguishes x. Calling this a refinement of a previously complete behavioural quotient would be wrong (RMI8). It is enabling a represented procedure. A genuinely absent operation cannot be explained by writing an enlarged lookup table; implementation evidence would be an additional premise.

Reading r is retained reuse; erase loses the record, while read can restore it when enabled. After break;erase with no rebuild resources, that contrast is lost. Switching tasks from a to b in EA-M2 gives incomparable equivalences. Neither supplies monotonic universal refinement.

## PROP EA-A3 — comparison across interfaces (KNOWN)

Assume a declared comparison support S with maps a:S→X_old, c:S→X_new and descended target readouts h_old,h_new into a common contrast Y. Old and new readouts are comparable on S only after the chosen target translation and equality h_old a=h_new c are independently checked. A coarse map X_new/ker p_new→X_old/ker p_old via these rows requires equal new profiles to determine equal old profiles; changing carriers requires the full common-interface and operation-domain squares of CC5–7. No canonical map follows just from the word articulation.

Proof: factorization on the named comparison image, EA-A1. Countermodels: old a/new b on four rows has neither coarse map; duplicate carriers admit a common quotient without a bijection; inconsistent target relabelling breaks the square. Separate empirical Q-status requires transported extension fibres, not only isomorphic quotient carriers (T1.2).

## CM EA-M5 — disclosure with a specified classical cost

Extend EA-M4 with a probe peek that returns the complete tuple without changing it. All maintenance outputs remain unchanged: the proposed universal destruction theorem fails. A different specified probe tap returns the tuple and consumes two fuel units, truncated at zero. At f=1, tap disables later read. Its disclosure task conflicts with this maintenance loop because its measured resource cost exceeds the replenishment buffer; a zero-cost peek or replenishment before tapping removes this counterexample. This is a conditional resource constraint, not a general bound on external knowledge. Device description, current-state access, removal of coupling selectivity and loss of maintenance are four separate operations.

## REC EA-Q1 — quantum information versus nondisturbance (external known result)

Assume, only in this L3 example, ordinary complex finite-dimensional quantum mechanics, a fixed pure-ready apparatus, a common isometric interaction, and a promise that each input pure state |ψ_i⟩ is retained exactly while a pure apparatus record |a_i⟩ is produced. Inner-product preservation gives

⟨ψ_i|ψ_j⟩ = ⟨ψ_i|ψ_j⟩⟨a_i|a_j⟩.

For a nonorthogonal pair, apparatus records coincide up to the relevant trivial phase and cannot distinguish the pair. Orthogonal inputs allow distinct records. This is the standard nondisturbance/copying argument, not derived from Q-exclusion. Removing nonorthogonality admits a controlled-copy construction; removing exact retention admits destructive discrimination with its usual quantum limits; supplying the preparation label is an independent classical channel. No access to an arbitrary unknown quantum state is supplied by knowing its device description.

A concrete cost witness: start |+⟩⟨+|, retain coherence as the task, and record Z by projective dephasing. The source becomes I/2, and an X+ test changes from probability 1 to 1/2. In the Z-diagonal sector the same recording preserves the source and can yield reusable classical records. The incompatibility concerns coherence versus this record channel; it does not say that every public record destroys quantum organization. Protecting one encoded subsystem while reading a specified error syndrome needs a separately supplied code and correctable error class; no universal secrecy condition follows.

## Kill-test verdicts

| Alternative | Verdict against a universal strong thesis |
|---|---|
| Static, fully closed | EA-M1 refutes necessary repertoire growth |
| Classical learning, full internal access | EA-M1 refutes necessary hiddenness and destructive disclosure |
| New classifiers, fixed interactions | EA-M2 refutes new source distinctions from relabelling |
| New articulation without storage | EA-M3 refutes automatic reuse |
| Self-maintenance with changed enabled repertoire | EA-M4 supports the limited mechanism under supplied construction/resources |
| Additional access with organization cost | EA-M5 and EA-Q1 support conditional incompatibility; zero-cost and commuting controls defeat universality |

The executable fixtures in [finite checks](verification/endogenous_check.py) check these finite tables, ablations, transported labels, classical access and exact rational quantum matrices. They do not certify general proofs or physical realizability.
