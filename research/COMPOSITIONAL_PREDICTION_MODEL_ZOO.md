# Compositional Prediction Model Zoo

All entries are finite declared L1 controls.  A pair is a composition slot,
not a temporal succession; multiplicities are finite arithmetic, not chances.
`F_i,G_j,H_k` denote separated quotient classes unless a row states a collapse.

| ID | finite declaration | certified result / failed claim |
|---|---|---|
| **CPG-M1 / CPG-CM1** | Raw duplicates `f0~f1`, `g0~g1`, `h0~h1`; all `(gj,fi)` compose to `h_(i xor j)`.  Equivalent controls emit the two raw slots `(g0,f0),(g1,f1)`, whose quotient batch is twice `(G,F)`. | Positive paired descent: `Gamma2` is derived and supported in `E_pair`. |
| **CPG-M2 / CPG-CM2** | Discrete `{f0,f1,g0,g1,h0,h1}` with `gj circ fi=h0` iff `i=j`, else `h1`.  `m+={(g0,f0),(g1,f1)}` and `m-={(g0,f1),(g1,f0)}`. | Same projections `{g0,g1}` and `{f0,f1}`, but `circ#m+=2h0`, `circ#m-=2h1`; equal marginal predictions do not determine composite prediction. |
| **CPG-M3 / CPG-CM3** | Equivalent controls `s~s'` emit quotient-distinct composable pair multisets, e.g. `{(G0,F0)}` and `{(G1,F1)}`. In the protocol variant, two `tau_2`-equivalent realization classes do the same; in the support variant, one lacks a batch at an active index. | q-fibre variation, protocol-fibre variation, and protocol-domain non-saturation respectively block descent; no value is selected. |
| **CPG-M4 / CPG-CM4** | Only `(G,F)` is in `Comp`; a declared raw output contains `(F,G)`. | Support failure: pair generation is not typed as `M_f(E_pair)`. |
| **CPG-M5 / CPG-CM5** | Use CPG-M2 and declare pair record `same` for equal indices and `cross` otherwise, composite record `zero` on `h0`, `one` on `h1`.  The raw record rule is `same->zero`, `cross->one`. | Positive derived square: `kappa# nPair=nComp`, hence `Phi=kappa_*`; no profile square is postulated. |
| **CPG-M6 / CPG-CM6** | Use CPG-M2 but declare the only pair record `slot`; retain composite records `zero/one`. | Both finite profiles exist, but both pair batches have profile `delta_slot` while composites differ.  `COMPOSITIONAL PROFILE TRANSPORT NOT DEFINED`. |
| **CPG-M7 / CPG-CM7** | A declared pair procedure and CP1 operation give `circ#m` as an L0 finite multiset; the presentation declares no batch execution/record-production implementation. | Mathematical pushforward exists, but no concrete composite generator is licensed. |
| **CPG-M8 / CPG-CM8** | Fine `f0,f1` both coarse-grain to `F`, while `gk,hk` retain labels and `gk circ fi=hk`; composition therefore commutes pointwise with refinement. Yet `GammaFine=n delta_(g0,f0)` and independently declared `GammaCoarse=n delta_(G1,F)` differ after pair pushforward. | Pair-generation/refinement square fails although process refinement and composition both pass; no prediction-transport theorem. |
| **CPG-M9 / CPG-CM9** | Wrap every raw `f,g,h` implementation by a finite tag.  A declared forgetful interface preserves readouts, pair domain, composition, pair/composite records, `kappa`, and each generated batch/net. | Positive changing-carrier transport.  Wrapper tags and any section are surplus. |
| **CPG-M10** | A concrete device rule emits every member of `{g0,g1} x {f0,f1}` once, with all four slots declared composable. | Positive *declared product-like pairing control* only; no independence or tensor is inferred. |
| **CPG-M11** | Reuse CPG-M2 with a natural-number batch-growth index and no before/after readout or relation. | The full algebraic signature and pair batches exist without an independent temporal readout. |
| **CPG-M12** | Alternate CPG-M5's all-`same` and all-`cross` batches. | `PredPair={delta_same,delta_cross}` and `PredComp={delta_zero,delta_one}=Phi(PredPair)`; set-valued output is retained without selection. |

### Required descent controls

For protocol use, CPG-M3 also has a version in which two quotient realization
classes share one `tau_2` value but yield different batches; it fails
protocol-fibre constancy.  A version whose generator is present over one such
class but absent over the other fails protocol-domain saturation.  These are
the paired analogues of PF5 and PF5b, not assumptions repairable by choosing a
realization.

### Model-zoo verdict

CPG-M1/M5/M9/M12 establish the full finite positive route.  CPG-M2 refutes
claims 1, 2, 5, 6, and 10 in the requested attack list; M3/M4/M7/M8/M9 refute
3, 4, 8, and 9; M11 refutes 7.  No model contains an identity, second mode,
interchange, product operation, stochastic process, probability distribution,
or temporal interpretation.
