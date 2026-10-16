# Compositional Record Realizability Model Zoo

All controls are finite declared L1/L2 tables.  `r` is pair-side, `c` is
composite-side, and no table asserts a temporal order, probability, global
space, or category.  A probe is available only where stated.

| ID | finite control | verdict |
|---|---|---|
| CRS-M1 | `S={x,y}`, `r=(a,b)`, `c=(0,1)`. | Positive CPG7-style factor `a->0,b->1`. |
| CRS-M2 | CRS3: `S={x0}`, expanded to `S'={x0,x1,x2}`, `r=(a,b,b)`, `c=(0,0,1)`. | `SCHEME_LOCAL_RECORD_FACTOR`; expansion fails. |
| CRS-M3 | `S1={x}`, `S2={y}`, common `r=a`, but `c(x)=0,c(y)=1`. | Local factors do not glue. |
| CRS-M4 | `S1={x,z}`, `S2={y,z}`, records `a,b` and values `0,1` consistently. | Positive unique glued union factor. |
| CRS-M5 | `S={u,v,w}`, `r(u)=r(v)=a,r(w)=b`; `c(u)=0,c(v)=1,c(w)=0`. | `alpha={{u},{v},{w}}=ker r intersection ker c`; diagnostic minimal repair. |
| CRS-M6 | CRS-M5 plus independently declared available probe `h(u)=0,h(v)=1,h(w)=0`. | `(r,h)` exactly realizes `alpha` and restores factorization. |
| CRS-M7 | CRS-M5 but declared grammar contains only constant probes. | Diagnostic separator exists but no available refined record: `RECORD SUFFICIENCY NOT REALIZED`. |
| CRS-M8 | CRS-M7 with mathematical candidate `h=c`. | It would tautologically separate, but is composite output and `NOT AVAILABLE AS PAIR RECORD`. |
| CRS-M9 | Wrapped and unwrapped copies have support, pair/composite record maps, and available probe grammar carried by explicit maps; record images are covered. | Underlying transport forces the factor square on the generated image. |
| CRS-M10 | Pair supports and pair records transport but composite records have no compatible map (or map `b` identifies outputs inconsistently). | Factor transport is blocked; process transport alone is insufficient. |
| CRS-M11 | Available `h` separates all three points while `alpha` only needs to split `u,v`. | Strict over-refinement is sufficient but not minimal diagnostic realization. |
| CRS-M12 | Coarse support has one composite label; fine refinement splits two same-pair-record slots into different composite labels. | Coarse factor need not lift; empirical refinement is distinct from support/probe refinement. |
| CRS-M13 | A stable union factor maps a two-point pair cluster set to a two-point composite cluster set. | Set-valued prediction is retained without selection. |
| CRS-M14 | Two supports have identical aggregate output counts but one has a record collision with unequal `c`. | Aggregate coincidence does not establish record sufficiency. |

## Coverage of adversarial claims

CRS-M2 refutes global extension and monotonicity under support growth;
CRS-M3 refutes automatic gluing; CRS-M7/M8 refute availability and leakage
shortcuts; CRS-M10 refutes process-only transport; CRS-M12 refutes automatic
empirical-refinement preservation; CRS-M14 refutes prediction-to-factor
converse.  CRS-M1/M4/M6/M9/M13 are positive controls, while CRS-M11 separates
sufficiency from minimality.

## Audit

Every nonconstant `r`, `c`, or `h` in a positive model is declared as a
descended record/readout.  In M7/M8 it is deliberately not declared available;
the mathematical function is retained only as a diagnostic.  Carrier changes
in M9 preserve support, grammar, records, composition, factors, and predictive
cluster content through explicit interfaces.  The controls are finite witness
fixtures, not proofs over a universal class of protocols.
