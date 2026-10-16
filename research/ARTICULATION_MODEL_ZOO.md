# Articulation finite model zoo

Executable: `python research/regression/articulation_check.py` (stdlib).
Status: 6850 separately counted finite assertions PASS. Exact structural
kernel checks; entropy calculations use floats and tolerance 1e-10, not a
proof-assistant certificate. No fixture function is thereby an available probe.

All X below are declared finite structural carriers (L0 presentations of
L1 data); maps/partitions are diagnostic until actual descent and availability
interfaces admit them. Each probability is independently chosen test data.

| Witness | Data | Verdict |
|---|---|---|
| Bijective/no loss | X={0,1,2,3}, A(x)=3−x | ker A is equality; all targets preserved |
| Equal entropy, distinct targets | Uniform binary pairs; A=i, B=j | H(X|A)=H(X|B)=1; i factors only through A, j only through B |
| Preserved/lost target | Same A=i; F=i, G=j | Static target dependence, not absolute semantic loss |
| New refinement | Joint probe (i,j) | G restored only by independently added j access |
| Zero probability | X={0,1}, A constant, F=id, p=(1,0) | H(F|A)=0 while all-X descent fails |
| Support expansion | Same maps; S={0} enlarged to X | Current support factor fails on expansion |
| Downstream forgetting | Any partition A then B constant | Conditional target entropy cannot decrease on same p |
| Reweighting | Binary constant A, F=id; p=(.5,.5) vs (.9,.1) | Same kernel, different entropy |
| Source retained | w(x)=(x,i) | Projection loses j; w injective; H(w)=H(X) |
| Record-only controller | All four binary decoders on i | Every output constant on ker i; none realizes j |
| Access route | G0 constant output; G1 explicitly adds i write/read/decoder route | i newly accessible to this controller, retained-source distinctions unchanged |
| Executable port route | Edge tables source→written→record_port→controller_output | Finite path evaluates i; direct path absent; source retained |
| Unavailable decoder | i factors through i; G0 lacks typed i-output route | Mathematical factor is insufficient for implementation |
| Failed update | r=(0,0,1), u=(0,2,2) on three points | Static sufficient record cannot update from class {0,1} |
| Failed update domain | Same r; u defined only at 0 | Common-domain agreement misses unsaturated domain |
| Unavailable separator | Two points, constant grammar, target identity | Mathematical separator exists, declared grammar cannot realize it |
| Competing families | Target families {i} and {j} | Coarsest static quotients incomparable; joint family refines both |
| Unary vs composition | Unary identity stable for r=(0,0,1); binary op differs at (0,0),(1,0) | Independent binary composition fails descent |
| Write leakage | Empirical twins, write outputs0/1 | Writer fails its own descent test |
| Empirical vs exact retention | Old constant profile, new identity readout, injective retained-source writer | Raw injectivity does not imply unchanged empirical quotient |
| Unsound closure | Constant seed, represented contextual identity probe | Seed soundness does not imply closure soundness |
| A versus Q-U | A=id,F=id,U=constant | A-factorization passes; stated Q-forgetful test fails |
| Presentation | All24 permutations of four inputs, transported maps and p | Factor verdict and entropy unchanged |
| DPI equality | Uniform pairs, target i, fine articulation j, coarse constant | Equal loss without target determination |
| Entropy equalities | Three-point F=(0,0,1), p=(.25,.25,.5) | Uniform target, nonuniform carrier |

Exhaustive small-model blocks:

- All partitions and binary targets on 1–4 points: 290 kernel tests; 1534
  static sufficient-quotient comparison assertions.
- 868 declared partition/target/probability cases each for support-entropy
  equivalence, data processing, refinement, carrier-fibre bound and its
  conditional-uniform equality criterion. Probabilities: uniform,
  positive unequal masses, and a separately declared last-point-zero vector.
- 216 three-point binary-target/total-unary-operation cases: independently
  enumerate stable sufficient partitions and compare greatest member with
  residual refinement normal form (216 further assertions).
- Remaining assertions are named kills, access witnesses, monotonicity and
  transport. Counts are assertions, not distinct theorems or models.

Unavailable records/decoders are tested against the explicitly listed tiny
grammar, never against all mathematical algorithms. Once finite lookup is
declared available, that availability countermodel no longer applies. The
root routing witness has a complete equality source profile and named executable
edge tables; it does not
certify empirical no-gain for arbitrary old repertoires. General partial,
multi-sort, relation and unbounded grammar claims use existing proofs, not
this finite total-unary enumeration. No probability admission, global state,
physical implementation, consciousness or mechanized general proof follows.

Dependency impact: optional fixture only. Preserved178-check baseline,
control suites and semantic suite are counted and replayed separately.
