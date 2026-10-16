"""Optional Stream42 finite witnesses; counts independent of baseline suites.

Exact kernel assertions, floating-point entropy sanity checks (not formal proof).
No probability is generated from profiles, and no function is deemed available
merely by being included in this L0 fixture.
"""

if not __debug__:
    raise RuntimeError('OPTIMIZED_PYTHON_NOT_SUPPORTED: run finite checks without -O, -OO or PYTHONOPTIMIZE')

from collections import defaultdict
from itertools import product
from itertools import permutations
from math import log2, isclose

COUNTS = defaultdict(int)


def check(value, group):
    assert value, group
    COUNTS[group] += 1


def kernel(a):
    return frozenset((i, j) for i in range(len(a)) for j in range(len(a)) if a[i] == a[j])


def factors(a, f, support=None):
    s = range(len(a)) if support is None else support
    return all(a[i] != a[j] or f[i] == f[j] for i in s for j in s)


def entropy(values, p):
    masses = defaultdict(float)
    for v, mass in zip(values, p):
        masses[v] += mass
    return -sum(v * log2(v) for v in masses.values() if v > 0)


def conditional(f, a, p):
    return entropy(tuple(zip(f, a)), p) - entropy(a, p)


def partitions(n):
    # Restricted-growth strings: all equivalences exactly once.
    if n == 0:
        yield ()
        return
    def extend(prefix):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for label in range(max(prefix) + 2):
            yield from extend(prefix + [label])
    yield from extend([0])


def stable(a, op):
    return all(a[i] != a[j] or a[op[i]] == a[op[j]] for i in range(len(a)) for j in range(len(a)))


def static_entropy_audit():
    for n in range(1, 5):
        xs = tuple(range(n))
        probabilities = [tuple(1 / n for _ in xs), tuple((i + 1) / sum(range(1, n + 1)) for i in xs)]
        if n > 1:
            probabilities.append(tuple(1 / (n - 1) if i < n - 1 else 0 for i in xs))
        for a in partitions(n):
            for f in product(range(2), repeat=n):
                check(factors(a, f) == (kernel(a) <= kernel(f)), 'kernel')
                sufficient = [b for b in partitions(n) if factors(b, f)]
                for b in sufficient:
                    check(kernel(b) <= kernel(f), 'static_universal')
                for p in probabilities:
                    support = tuple(i for i in xs if p[i] > 0)
                    h = conditional(f, a, p)
                    check(isclose(h, 0, abs_tol=1e-10) == factors(a, f, support), 'support_entropy')
                    coarse = tuple(0 for _ in xs)
                    check(conditional(f, coarse, p) + 1e-10 >= h, 'data_processing')
                    refined = tuple(zip(a, f))
                    check(conditional(f, refined, p) <= h + 1e-10, 'refinement')
                    bound = sum(p[i] * log2(sum(a[j] == a[i] for j in support)) for i in support)
                    check(conditional(xs, a, p) <= bound + 1e-10, 'fibre_bound')
                    eq = all(isclose(p[i], p[j], abs_tol=1e-12) for i in support for j in support if a[i] == a[j])
                    check(isclose(conditional(xs, a, p), bound, abs_tol=1e-10) == eq, 'fibre_equality')
                # Forgetting cannot restore a failed target.
                if not factors(a, f):
                    check(not factors(tuple(0 for _ in xs), f), 'no_recovery')


def operational_audit():
    n = 3
    ps = list(partitions(n))
    for f in product(range(2), repeat=n):
        for op in product(range(n), repeat=n):
            candidates = [a for a in ps if factors(a, f) and stable(a, op)]
            greatest = [a for a in candidates if all(kernel(b) <= kernel(a) for b in candidates)]
            check(len(greatest) == 1, 'operational_universal')
            # Independently compute unary residual normal form by refinement.
            labels = f
            while True:
                profile = tuple((labels[i], labels[op[i]]) for i in range(n))
                if kernel(profile) == kernel(labels):
                    break
                labels = profile
            check(kernel(labels) == kernel(greatest[0]), 'residual_normal_form')


def witnesses():
    x = tuple(range(4))
    first, second = (0, 0, 1, 1), (0, 1, 0, 1)
    uniform = (.25,) * 4
    check(kernel(x) == kernel(tuple(3-i for i in x)), 'witness_bijection')
    check(conditional(x, x, uniform) == 0, 'witness_injective')
    check(isclose(conditional(x, first, uniform), conditional(x, second, uniform)), 'witness_equal_entropy')
    check(factors(first, first) and not factors(second, first), 'witness_different_targets')
    check(not factors(first, second) and factors(tuple(zip(first, second)), second), 'witness_new_probe')
    check(not factors((0, 0), (0, 1)) and conditional((0, 1), (0, 0), (1, 0)) == 0, 'witness_zero_mass')
    check(factors((0, 0), (0, 1), (0,)) and not factors((0, 0), (0, 1)), 'witness_support_expansion')
    check(not isclose(conditional((0, 1), (0, 0), (.5,.5)), conditional((0, 1), (0, 0), (.9,.1))), 'witness_reweighting')
    written = tuple(zip(x, first))
    check(len(set(written)) == len(x) and len(set(first)) < len(x), 'witness_source_retention')
    check(isclose(entropy(written, uniform), entropy(x, uniform)), 'witness_entropy_retention')
    # Exhaust all binary deterministic record-only controllers on im A.
    for decoder in product(range(2), repeat=2):
        output = tuple(decoder[v] for v in first)
        check(kernel(first) <= kernel(output), 'record_only_controller')
        check(output != second, 'record_only_lost_target')
    # Concrete finite routing grammar: routes are declared implementations.
    g0 = {'constant': (0, 0, 0, 0)}
    g1 = dict(g0, write_read_decode=first)
    check(first not in g0.values() and first in g1.values(), 'accessibility_gain')
    check(kernel(written) == kernel(x), 'no_source_distinction_gain')
    check(factors(first, first) and first not in g0.values(), 'unavailable_decoder')
    # Finite represented port graphs with executable edge tables, not all maps.
    retained = tuple((i, ('z0','z1')[first[i]]) for i in x)
    edges = {
        ('source','written'): dict(zip(x,retained)),
        ('written','record_port'): {v:v[1] for v in retained},
        ('record_port','controller_output'): {'z0':0,'z1':1},
    }
    def run(route, inputs):
        values = inputs
        for source, target in zip(route,route[1:]):
            if (source,target) not in edges:
                return None
            table = edges[source,target]
            values = tuple(table[v] for v in values)
        return values
    check(run(('source','controller_output'),x) is None, 'port_route_absent')
    check(run(('source','written','record_port','controller_output'),x) == first, 'port_route_execution')
    check(tuple(v[0] for v in run(('source','written'),x)) == x, 'port_source_retained')
    check(not stable((0, 0, 1), (0, 2, 2)), 'static_update_failure')
    domain = {0}
    check(any((i in domain) != (j in domain) for i,j in kernel((0,0,1))), 'update_domain_failure')
    check(not factors((0,0), (0,1)), 'unavailable_separator')
    check(not (kernel(first) <= kernel(second)) and not (kernel(second) <= kernel(first)), 'competing_families')
    # Unary identity stability cannot validate independent binary operation.
    theta = (0, 0, 1)
    check(stable(theta, (0,1,2)) and theta[0] != theta[2], 'unary_not_binary')
    binary = {(i,j): (2 if (i,j)==(1,0) else 0) for i in range(3) for j in range(3)}
    check(theta[binary[0,0]] != theta[binary[1,0]], 'binary_composition_failure')
    # Missing write descent: empirical twins cannot have different records.
    check(not factors((0,0), (0,1)), 'write_descent_failure')
    check(factors(first, first) and factors(second, second)
          and kernel(tuple(zip(first, second))) <= kernel(first), 'target_family_monotonicity')
    # Exact and empirical no-gain differ: raw injectivity is not the quotient.
    old_profile = (0,0)
    new_record = (0,1)
    check(len(set(zip(range(2),new_record))) == 2
          and not (kernel(old_profile) <= kernel(new_record)), 'empirical_no_gain_failure')
    check(kernel(tuple(zip(first,first))) == kernel(first), 'empirical_no_gain_positive')
    # A constant new seed need not have sound contextual closure.
    seed, closure = (0,0), (0,1)
    check(kernel(seed) == kernel(old_profile) and kernel(closure) < kernel(old_profile), 'unsound_closure')
    # A and the specified Q forgetful map can ask opposite questions.
    check(factors((0,1),(0,1)) and not factors((0,0),(0,1)), 'A_not_U')
    check(isclose(conditional(first,second,uniform),conditional(first,(0,0,0,0),uniform)), 'DPI_equality_nonrecovery')
    check(not factors(second,first), 'DPI_equality_no_factor')
    # Target-uniform and source-uniform equality conditions must differ.
    a3, f3, p3 = (0,0,0), (0,0,1), (.25,.25,.5)
    check(isclose(conditional(f3,a3,p3),1) and conditional(tuple(range(3)),a3,p3) < log2(3), 'target_vs_carrier_bound')
    check(isclose(conditional((0,0,1),(0,1,1),(.5,.25,.25)),.5), 'average_not_max_bound')
    for order in permutations(range(4)):
        a = tuple(first[i] for i in order)
        f = tuple(second[i] for i in order)
        p = tuple(uniform[i] for i in order)
        check(factors(a,f) == factors(first,second), 'presentation_factor')
        check(isclose(conditional(f,a,p),conditional(second,first,uniform),abs_tol=1e-10), 'probability_transport')


if __name__ == '__main__':
    static_entropy_audit()
    operational_audit()
    witnesses()
    print('ARTICULATION_PASS ' + ', '.join(f'{k}={v}' for k,v in sorted(COUNTS.items())))
    print(f'OPTIONAL_ARTICULATION_CHECKS={sum(COUNTS.values())}; baseline counts unchanged')
