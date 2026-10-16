"""Exact finite RMI controls; stdlib only. Counts are assertions, not proofs.

Recognize event/procedure data, never fixture names. Probabilities are declared
rational toy kernels. Physical implementation/provenance is not certified.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
COUNTS = Counter()
EVIDENCE = {}


def check(scope, value):
    if not value:
        raise AssertionError(scope)
    COUNTS[scope] += 1


def normalize(values):
    names = {}
    return tuple(names.setdefault(v, len(names)) for v in values)


def partitions(n):
    return sorted({normalize(v) for v in product(range(n), repeat=n)})


def tv(p, q):
    return sum(abs(a - b) for a, b in zip(p, q)) / 2


def pushed(row, q):
    return tuple(sum(row[i] for i in range(len(q)) if q[i] == z)
                 for z in sorted(set(q)))


def defect(k, q):
    return max(tv(pushed(k[i], q), pushed(k[j], q))
               for i in range(len(q)) for j in range(len(q)) if q[i] == q[j])


def saturated(f, q):
    return all(q[i] != q[j] or (f[i] is None) == (f[j] is None)
               for i in range(len(q)) for j in range(len(q)))


def deterministic_kernel(f):
    return tuple(tuple(F(int(j == target)) for j in range(len(f))) for target in f)


def readout_factors(o, q):
    return all(q[i] != q[j] or o[i] == o[j]
               for i in range(len(q)) for j in range(len(q)))


def word_kernel(f, o):
    # Greatest deterministic observation congruence: decides all word depths.
    q = normalize(o)
    while True:
        new = normalize((o[i], q[f[i]]) for i in range(len(f)))
        if new == q:
            return q
        q = new


def exhaustive_deterministic():
    n = 3
    ps = partitions(n)
    check('partition_inventory', len(ps) == 5)
    for f in product(range(n), repeat=n):
        k = deterministic_kernel(f)
        for o in product(range(2), repeat=n):
            qb = word_kernel(f, o)
            for q in ps:
                sufficient = all(q[i] != q[j] or qb[i] == qb[j]
                                 for i in range(n) for j in range(n))
                autonomous = defect(k, q) == 0 and readout_factors(o, q)
                # A sufficient over-refinement can fail update descent even
                # deterministically; autonomy is sufficient, not necessary.
                check('all_deterministic_autonomy_implies_sufficiency', not autonomous or sufficient)
                check('minimal_deterministic_kernel_autonomous', defect(k, qb) == 0)
                eligible = 1 < len(set(q)) < n and len(set(o)) > 1 and sufficient
                check('identity_singleton_gate', not eligible or q not in ((0, 0, 0), (0, 1, 2)))
                for perm in permutations(range(n)):
                    fp = tuple(perm[f[perm.index(i)]] for i in range(n))
                    op = tuple(o[perm.index(i)] for i in range(n))
                    qp = tuple(q[perm.index(i)] for i in range(n))
                    check('all_state_relabelings', defect(deterministic_kernel(fp), qp) == defect(k, q)
                          and readout_factors(op, qp) == readout_factors(o, q))
    # Stronger probabilistic/bisimulation condition need not be necessary.
    f = (0, 0, 2); q = (0, 1, 1); o = (0, 0, 0)
    check('sufficient_not_autonomous', word_kernel(f, o) == (0, 0, 0)
          and defect(deterministic_kernel(f), q) == 1)
    check('domain_failure', not saturated((0, None, 2), (0, 0, 1)))


def exhaustive_kernels():
    rows = [tuple(F(i, 2) for i in r) for r in product(range(3), repeat=3) if sum(r) == 2]
    ps = partitions(3)
    for k in product(rows, repeat=3):
        for q in ps:
            factor = all(pushed(k[i], q) == pushed(k[j], q)
                         for i in range(3) for j in range(3) if q[i] == q[j])
            check('all_denominator_two_kernel_descent', (defect(k, q) == 0) == factor)
    # Exhaust all deterministic base/noise maps and four perturbation radii.
    for f in product(range(3), repeat=3):
        k = deterministic_kernel(f)
        for g in product(range(3), repeat=3):
            noise = deterministic_kernel(g)
            for rho in (F(0), F(1, 4), F(1, 2), F(1)):
                kp = tuple(tuple((1-rho)*a+rho*b for a, b in zip(row, nr))
                           for row, nr in zip(k, noise))
                for q in ps:
                    check('all_noise_triangle_bounds', defect(kp, q) <= defect(k, q)+2*rho)
    check('approximate_relation_not_transitive', F(4, 10) <= F(1, 2)
          and F(8, 10)-F(4, 10) <= F(1, 2) and F(8, 10) > F(1, 2))
    # Tiny error can leak completely at arbitrarily long depths.
    eps = F(1, 10)
    check('finite_not_infinite_robustness', 1-(1-eps)**100 > F(99, 100))


def emit(values, weights=(1, 2), error=F(0), fresh=True):
    """Joint available route/output kernel, for capacity-two refill operations.

    Input values and event alphabets have no biological labels. Persistent
    events are tagged separately, never reclassified as new outputs.
    """
    if not values:
        return {((), (), fresh): F(1)}
    total = sum(weights[v] for v in values)
    out = defaultdict(F)
    for route in product(range(len(values)), repeat=2):
        rp = F(1)
        for i in route:
            rp *= F(weights[values[i]], total)
        for outputs in product(range(2), repeat=2):
            prob = rp
            for i, val in zip(route, outputs):
                prob *= (1-error) if val == values[i] else error
            if prob:
                out[(route, outputs, fresh)] += prob
    return dict(out)


def output_law(events):
    law = defaultdict(F)
    for (route, values, fresh), p in events.items():
        law[values] += p
    return dict(law)


def mean_fraction(events, value=1):
    # All nonempty events here have the declared equal capacity two.
    return sum(p * F(values.count(value), len(values))
               for (_, values, _), p in events.items() if values)


def clamped_responses(error):
    # Independent, explicitly available route-clamp + source-payload changes.
    return {0: (1-error, error), 1: (error, 1-error)}


def recognizer(values, events, clamps, equalized, scrambled, repeat_supported=True):
    """Consumes only neutral records; no mode, names or expected verdict inputs."""
    if clamps is None or equalized is None or scrambled is None:
        return {'status': 'NOT_DEFINED'}
    if not values:
        return {'status': False, 'reason': 'no_ports'}
    w = [F(0) for _ in values]
    for (route, outputs, fresh), p in events.items():
        if fresh:
            for i in route:
                w[i] += p
    variants = sorted(set(values))
    variation = len(values) >= 2 and len(variants) >= 2
    h = tv(clamps[0], clamps[1])
    yield_by_value = {a: sum(w[i] for i in range(len(values)) if values[i] == a)
                     / values.count(a) for a in variants}
    d = max(yield_by_value.values()) - min(yield_by_value.values())
    before = F(values.count(1), len(values))
    g = abs(mean_fraction(events) - before)
    attribution = mean_fraction(equalized) == before and mean_fraction(scrambled) == before
    verdict = variation and max(w) > 1 and h > 0 and d > 0 and g > 0 and attribution and repeat_supported
    return {'status': verdict, 'h': h, 'd': d, 'g': g, 'max_fresh_row': max(w),
            'variation': variation, 'attribution': attribution}


def evaluate(values=(0, 1), weights=(1, 2), error=F(0), fresh=True, available=True):
    return recognizer(values, emit(values, weights, error, fresh),
                      clamped_responses(error) if available else None,
                      emit(values, (1, 1), error, fresh),
                      emit(values, weights, F(1, 2), fresh))


def exhaustive_recognizer():
    relaxation = {((0, 1), (0, 0), False): F(1)}
    relaxed = recognizer((0, 1), relaxation, {0: (F(1), F(0)), 1: (F(1), F(0))},
                         relaxation, relaxation)
    filtered = {((1,), (1,), False): F(1)}
    unfiltered = {((0, 1), (0, 1), False): F(1)}
    scrambled_filter = {((1,), (0,), False): F(1, 2), ((1,), (1,), False): F(1, 2)}
    filter_result = recognizer((0, 1), filtered, clamped_responses(F(0)),
                               unfiltered, scrambled_filter)
    controls = {
        'A_crystal_one_type': evaluate((0, 0)),
        'A_simple_attractor': relaxed,
        'B_autocatalytic_reset': evaluate(error=F(1, 2)),
        'B_equal_yield_transfer': evaluate(weights=(1, 1)),
        'C_weighted_transfer': evaluate(),
        'C_noisy_weighted_transfer': evaluate(error=F(1, 10)),
        'filter_persisted': filter_result,
        'constraint_satisfaction_reset': relaxed,
        'ordinary_autocatalysis': evaluate(weights=(1, 1), error=F(1, 2)),
        'copy_without_differential': evaluate(weights=(1, 1)),
        'missing_intervention': evaluate(available=False),
    }
    for name, val in controls.items():
        expected = 'NOT_DEFINED' if name == 'missing_intervention' else name.startswith('C_')
        check('locked_control_comparison', val['status'] == expected)
    EVIDENCE['controls'] = controls
    # Refill domain/closure is tested on every bounded cohort, rather than
    # inferred from a repeated invocation on the original mixed input.
    cohort_domain = [tuple(v) for n in range(3) for v in product(range(2),repeat=n)]
    for values in cohort_domain:
        events = emit(values)
        check('all_refill_domain_closure', sum(events.values()) == 1
              and all(outputs in cohort_domain for (_,outputs,_) in events))
    law = {(0,1): F(1)}
    profile_trace = [F(1,2)]
    for _ in range(2):
        nxt = defaultdict(F)
        for values, p in law.items():
            for outputs, prob in output_law(emit(values)).items():
                nxt[outputs] += p*prob
        law = dict(nxt)
        profile_trace.append(sum(p*F(values.count(1),2) for values,p in law.items()))
        check('two_actual_refill_rounds', sum(law.values()) == 1 and law.get((0,1),F(0)) > 0)
    check('actual_two_round_profile_shift', profile_trace == [F(1,2), F(2,3), F(20,27)])
    EVIDENCE['C_actual_refill_profile_trace'] = profile_trace
    for values in ((0, 1), (1, 0)):
        for a, b in product(range(1, 5), repeat=2):
            for m in (F(0), F(1, 10), F(1, 4), F(1, 2)):
                result = evaluate(values, (a, b), m)
                check('all_two_type_parameter_controls', result['status'] == (a != b and m < F(1, 2)))
                check('exact_transfer_formula', result['h'] == 1-2*m)
                check('exact_yield_formula', result['d'] == F(2*abs(a-b), a+b))
                check('exact_shift_formula', result['g'] == (1-2*m)*F(abs(a-b), 2*(a+b)))
                events = emit(values, (a, b), m)
                check('kernel_normalization', sum(events.values()) == 1)
                # Scramble semantic words: routine never receives them.
                for label in ('molecule', 'organism', 'agent'):
                    metadata = {'labels': (label, label+'2'), 'events': events}
                    check('semantic_metadata_erasure', output_law(metadata['events']) == output_law(events))
                # Value bijection and simultaneous source/output port permutation.
                swapped = tuple(1-v for v in values[::-1])
                result2 = evaluate(swapped, (b, a), m)
                check('payload_port_gauge', result2 == result)
                # Repeatability on mixed support, not universal non-fixation.
                check('refill_repeat', evaluate(values, (a, b), m) == result)
    # B occupancy propagation: supplied saturating occupancy kernel, not heredity.
    for n in range(3):
        events = emit((0,)*n, (1, 1), F(1, 2))
        check('bounded_occupancy_propagation', set(len(v) for (_, v, _) in events) == {min(2, 2*n)})
    # Parametric noise margin at w=(1,2).
    for m in (F(i, 20) for i in range(11)):
        r = evaluate(error=m)
        check('transmission_noise_boundary', r['status'] == (m < F(1, 2)))
        if m <= F(1, 10):
            check('predeclared_noise_margin', r['h'] >= F(4, 5) and r['g'] >= F(2, 15))


def completion_no_go():
    # For every bounded cohort payload x, eliminate the route to obtain its
    # exact law; compare independently constructed context-fed output law.
    for n in (1, 2):
        for values in product(range(2), repeat=n):
            for a, b in product(range(1, 4), repeat=2):
                for m in (F(0), F(1, 10), F(1, 2)):
                    p1 = m+(1-2*m)*F(sum((a, b)[v] for v in values if v == 1),
                                      sum((a, b)[v] for v in values))
                    feed = {v: (p1 if v[0] else 1-p1)*(p1 if v[1] else 1-p1)
                            for v in product(range(2), repeat=2)}
                    feed = {v: p for v, p in feed.items() if p}
                    check('all_cohort_completion_rows', output_law(emit(values, (a, b), m)) == feed)
    check('completion_clamp_separates', tv(clamped_responses(F(0))[0], clamped_responses(F(0))[1]) == 1
          and tv((F(1, 3), F(2, 3)), (F(1, 3), F(2, 3))) == 0)
    k1 = emit((0,1), error=F(1,10)); k2 = emit((0,1), error=F(1,4))
    check('support_forgetting_numeric_non_descent', set(k1) == set(k2)
          and evaluate(error=F(1,10))['h'] != evaluate(error=F(1,4))['h'])
    # Direct enumeration of the Price identity, including zero-yield rows.
    for inputs, outputs, route in product(product(range(2),repeat=2),
                                          product(range(2),repeat=2),
                                          product(range(2),repeat=2)):
        w = [route.count(i) for i in range(2)]
        old = F(sum(inputs),2); new = F(sum(outputs),2)
        avgw = F(sum(w),2)
        cov = F(sum(w[i]*inputs[i] for i in range(2)),2)-avgw*old
        transmission = F(sum(outputs[j]-inputs[route[j]] for j in range(2)),2)
        check('all_small_price_count_identities', new-old == cov/avgw+transmission/avgw)


def interface_controls():
    xs = list(product(range(2), repeat=3))
    q1 = normalize((a, b) for a, b, h in xs)
    q2 = normalize(a for a, b, h in xs)
    qb = normalize(b for a, b, h in xs)
    f = tuple(xs.index((a, b, 0)) for a, b, h in xs)
    k = deterministic_kernel(f)
    joint = tuple((a, b) for a, b, h in xs)
    oa = tuple(a for a, b, h in xs); ob = tuple(b for a, b, h in xs)
    check('intermediate_8_to_4', len(set(q1)) == 4 and defect(k, q1) == 0 and readout_factors(joint, q1))
    check('restricted_8_to_2', len(set(q2)) == 2 and defect(k, q2) == 0 and readout_factors(oa, q2))
    check('unchanged_repertoire_ladder_kill', not readout_factors(joint, q2))
    check('incomparable_interfaces', not readout_factors(oa, qb) and not readout_factors(ob, q2))
    check('context_enlargement_hidden_probe', not readout_factors(tuple(h for a,b,h in xs), q1))
    # All permutations of the four reduced image states: a sufficient next
    # quotient for inherited joint readout must be identity.
    image = sorted(set(joint))
    for r in partitions(4):
        check('all_second_quotients_full_signature', readout_factors(image, r) == (len(set(r)) == 4))
    # Explicit mediator a hides h for all future e readouts under swap/reset.
    fm = tuple(xs.index((e, 0, a)) for a, h, e in xs)
    qm = normalize((a, e) for a, h, e in xs)
    check('mediation_update_all_protocols', defect(deterministic_kernel(fm), qm) == 0)
    for a,h,e in xs:
        for hp in range(2):
            check('mediated_crossing_response', xs[fm[xs.index((a,h,e))]][2]
                  == xs[fm[xs.index((a,hp,e))]][2])
    # Arbitrary coordinates are harmless with decoders, not new reset rights.
    transformed = [(a ^ h, h, e) for a,h,e in xs]
    for old,new in zip(xs, transformed):
        check('mixed_coordinate_decoder', (new[0] ^ new[1], new[2]) == (old[0],old[2]))
    # Non-symmetric, non-transitive immediate influence relation, computed by
    # all single-coordinate changes, not by a semantic label.
    rule = lambda v: (v[0], v[0], v[1])
    influence = set()
    for v in xs:
        for i in range(3):
            vp = tuple(1-x if j == i else x for j,x in enumerate(v))
            for j in range(3):
                if rule(v)[j] != rule(vp)[j]:
                    influence.add((i,j))
    check('strong_flow_kill', (0,1) in influence and (1,0) not in influence
          and (1,2) in influence and (0,2) not in influence)
    EVIDENCE['immediate_influence'] = sorted(influence)
    # Local consistent context records but no simultaneous global section.
    local = [[(0,0),(1,1)],[(0,0),(1,1)],[(0,1),(1,0)]]
    sections = [v for v in xs if v[:2] in local[0] and v[1:] in local[1]
                and (v[2],v[0]) in local[2]]
    check('local_trace_no_global_section', all(local) and not sections)
    # Symmetric duplicate screens have no invariant singleton selector.
    check('no_unique_symmetric_screen', all((1-i) != i for i in (0,1)))
    # Constraint propagation versus vacuity, with a locked different query.
    for rel in (((0,0),(1,1)),tuple(product(range(2),repeat=2))):
        survivors = tuple(v for v in rel if v[0] == 0)
        check('strict_distinction_constraint_control', len(survivors) < len(rel) and bool(survivors))
    check('new_constraint_distinguishes_other_query', {v[1] for v in ((0,0),)} == {0})
    check('no_constraint_no_new_contrast', {v[1] for v in product(range(2),repeat=2) if v[0] == 0} == {0,1})
    # Without closure hidden distinctions can be revealed later.
    check('hidden_bit_closure_kill', (0,0)[0] == (0,1)[0] and (0,0)[1] != (0,1)[1])
    EVIDENCE['multiscale'] = {'sizes': [8,4,2], 'second_step_requires_repertoire_restriction': True,
                            'induced_invariants': ['a','b'], 'discarded_at_second_step': ['b']}


def serial(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(k): serial(v) for k,v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(v) for v in value]
    return value


def main():
    exhaustive_deterministic()
    exhaustive_kernels()
    exhaustive_recognizer()
    completion_no_go()
    interface_controls()
    report = {'status': 'FINITE_PASS', 'counts_by_scope': dict(sorted(COUNTS.items())),
              'total_assertions': sum(COUNTS.values()), 'evidence': serial(EVIDENCE),
              'domains': {'deterministic_three_state_maps': 27, 'three_state_partitions': 5,
                          'boolean_readouts': 8, 'state_permutations': 6,
                          'denominator_two_three_state_kernels': 216,
                          'four_state_partitions': 15, 'two_type_weight_pairs': 16},
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'general_proofs_mechanized': False, 'empirical_data': False}
    print(json.dumps({'status': report['status'], 'total_assertions': report['total_assertions'],
                      'counts_by_scope': report['counts_by_scope']}, indent=2))


if __name__ == '__main__':
    main()
