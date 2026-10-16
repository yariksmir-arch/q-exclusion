# Protocol Generation Theory

## Scope

This derived L2 module introduces neither trial order, selected realizations, distributions on fibres, nor global generation families.

**DEF DG1 (protocol carrier).** Let `q:X -> E` be a declared empirical quotient. A raw protocol carrier is a declared L1 sort `P0` with concrete typing `tauTilde:X -> P0`. When `tauTilde` is constant on `q`-fibres, its unique L2 descent is `tau:E -> P0`. Thus `P0` is a declared carrier, not an ambiguously L1/L2 object. Dependencies: T0.4, PR1. Status: derived.

**DEF DG2 (fibre and profile).** For `p in P0`, `E_p={e in dom(g):tau(e)=p}`. A descended record map is `g:E -> Batch(L)` and `v(e,i)` is the finite profile of the declared batch at generation index `i`. These are L2 data relative to declared maps; no element of `E_p` is selected.

**DEF DG3 (finite generated content).** `M_f(E_p)` is the free commutative monoid of finite multisets: finitely supported maps `m:E_p -> N`, added pointwise. It is diagnostic L2 arithmetic. Every map from `E_p` to a commutative monoid extends uniquely to a homomorphism from `M_f(E_p)`.

**DEF DG4 (declared generation scheme).** `Gamma_p` is a specified directed set `I_p` and a specified net `m:I_p -> M_f(E_p)`. The index compares declared batch growth only; it is not time or a trial list. No undeclared schemes are quantified over.

**DEF DG5 (concrete realization).** A concrete L1 implementation realizes `Gamma_p` only when its domain is saturated and its induced multiset is constant on empirical-equivalence fibres. Otherwise its L2 arrow is `NOT DEFINED AT THIS QUOTIENT`. Arithmetic on `M_f(E_p)` does not establish concrete realizability.

**LEMMA DG6 (exact aggregation).** For nonzero `m`, set `N_m=sum_e m(e)` and `A_i(m)=sum_e m(e)v(e,i)/N_m`. Then `A_i(m)` is exactly the rational barycenter with weights `m(e)/N_m`.

*Proof.* Finite-multiset addition adds each count coordinate; division by the total gives the displayed equality. Ratios are finite arithmetic, not primitive chances.

**NO-GO DG7 (ordered implementation is surplus).** A list-sensitive implementation is not a descended aggregate operation unless all declared readouts and implementations are permutation-invariant. An ordered-list formulation otherwise adds content.

## Audits

Q-audit: DG1–DG6 use only declared maps, fibres, directed families, and finite supports. New fibre elements, schemes, or list-sensitive implementations are new content. Presentation audit: transport requires `E`, `P0`, `tau`, `g`, the directed index, and the multiset net; bare relabelling is insufficient.
