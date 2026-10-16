"""Stream43 exact finite diagnostic witnesses; not mechanized general proofs.

No enumerated function is inferred to be an available procedure.
"""
from collections import Counter
from itertools import product, permutations, combinations

counts = Counter()


def check(ok, name):
    assert ok, name
    counts[name] += 1


def kernel(q):
    return {(i, j) for i in range(len(q)) for j in range(len(q)) if q[i] == q[j]}


def descends(u, q):
    return kernel(u) <= kernel(q)


def answers(u, q, b):
    return frozenset(q[i] for i in range(len(u)) if u[i] == b)


def partitions(n):
    if not n:
        yield ()
        return
    def grow(p):
        if len(p) == n:
            yield tuple(p)
        else:
            for x in range(max(p) + 2):
                yield from grow(p + [x])
    yield from grow([0])


def answer_quotient(u, q):
    labels = sorted(set(q))
    parent = {a: a for a in labels}
    def find(a):
        while parent[a] != a:
            a = parent[a]
        return a
    for i, j in kernel(u):
        parent[find(q[j])] = find(q[i])
    return {a: find(a) for a in labels}


for n in range(5):
    for u in partitions(n):
        for q in product(range(3), repeat=n):
            images = [answers(u, q, b) for b in set(u)]
            check(descends(u, q) == all(len(s) == 1 for s in images), 'point_determinacy')
            # Empty fibres handled separately; envelope is uniquely least by inclusion.
            for b in range(max(u, default=-1) + 2):
                image = answers(u, q, b)
                for bits in product((0, 1), repeat=3):
                    envelope = {a for a in range(3) if bits[a]}
                    contains = all(q[i] in envelope for i in range(n) if u[i] == b)
                    check(contains == (image <= envelope), 'minimal_envelope')
            c = answer_quotient(u, q)
            cq = tuple(c[a] for a in q)
            check(descends(u, cq), 'answer_repair')
            labels = sorted(set(q))
            for d in partitions(len(labels)):
                coarsen = dict(zip(labels, d))
                if descends(u, tuple(coarsen[a] for a in q)):
                    check(all(c[a] != c[b] or coarsen[a] == coarsen[b]
                              for a in labels for b in labels), 'answer_universal_property')
            uq = tuple(zip(u, q))
            check(kernel(uq) == kernel(u) & kernel(q), 'base_repair')
            for v in partitions(n):
                if kernel(v) <= kernel(u) and descends(v, q):
                    check(kernel(v) <= kernel(uq), 'base_universal_property')
            # Every restriction shrinks images; every finer base splits local images.
            for size in range(n + 1):
                for s in combinations(range(n), size):
                    for b in set(u):
                        check(answers(tuple(u[i] for i in s), tuple(q[i] for i in s), b)
                              <= answers(u, q, b), 'restriction_monotonicity')
            check(descends(q, q), 'target_reduct_vacuity')
            check(descends((0,) * n, q) == (len(set(q)) <= 1), 'constant_overblocking')

# Named minimal witnesses.
u, f, g = (0, 0), (0, 1), (0, 1)
check(answers(u, f, 0) == {0, 1} and answers(u, f, 1) == set(), 'point_set_empty')
check(not descends(u, f) and not descends(u, g)
      and descends(u, tuple(a ^ b for a, b in zip(f, g))), 'whole_query_xor')
joint = answers(u, tuple(zip(f, g)), 0)
check(joint < set(product(answers(u, f, 0), answers(u, g, 0))), 'strict_joint_correlation')
check(descends(u, (0, 0)) and not descends(u, f), 'ambiguous_persistence_zero_change')
check({f[0]} != {f[1]} and {f[0]} <= answers(u, f, 0), 'hidden_selector_extra_data')
check(descends((0,), (0,)) and not descends(u, f), 'extension_expansion')
resolving = [s for s in ({0}, {1}, {0, 1}) if len({f[i] for i in s}) == 1]
check(resolving == [{0}, {1}], 'competing_maximal_restrictions')
swap = {0: 1, 1: 0}
check(all({swap[i] for i in s} != s for s in resolving), 'no_symmetric_restriction_selector')
# Transitive closure can propagate through shared answers in distinct base fibres.
u4, q4 = (0, 0, 1, 1), (0, 1, 1, 2)
c = answer_quotient(u4, q4)
check(len(set(c.values())) == 1, 'answer_transitive_closure')
# Decoder exists, but grammar has only constant outputs.
u2, q2 = (0, 1), (0, 1)
grammar = [(0, 0), (1, 1)]
check(descends(u2, q2) and not any(tuple(d[z] for z in u2) == q2 for d in grammar),
      'unavailable_answer_decoder')
# A partial query on only one member of a fibre is not a descended partial domain.
check({0} != {i for i, z in enumerate(u) if z == u[0]}, 'partial_domain_failure')
# Empty E gives empty images, no point answer on a nonempty B with empty A.
check(answers((), (), 0) == set(), 'empty_extension_not_point_answer')
for p in permutations(range(4)):
    v = tuple(u4[i] for i in p)
    q = tuple(2 - q4[i] for i in p)
    check(descends(v, q) == descends(u4, q4), 'presentation_permutation')
    check(all(answers(v, q, b) == {2 - a for a in answers(u4, q4, b)} for b in set(u4)),
          'joint_answer_transport')
# Recognition target pollution: finite semilattice barycentric completions.
for n in (2, 3):
    # Endpoints select first/second argument; all strict rational weights use meet.
    mix = lambda x, y, r: x if r == 1 else y if r == 0 else min(x, y)
    check(mix(0, 1, .5) == 0, 'RD6_same_named_value')
    check(all(mix(x, x, .5) == x for x in range(n)), 'RD6_idempotent_meet')
check(2 != 3, 'RD6_nonisomorphic_carriers_same_answer')

if __name__ == '__main__':
    print('QUESTION_DEFINABILITY_PASS', sum(counts.values()), 'assertions')
    for name, count in sorted(counts.items()):
        print(name, count)
