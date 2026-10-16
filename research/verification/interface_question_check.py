"""Stream45 finite witnesses only: no general proof or physical availability.

Run from root; stdlib only. All probability profiles are declared test inputs.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product, permutations


counts = Counter()


def check(condition, name):
    if not condition:
        raise AssertionError(name)
    counts[name] += 1


def kernel(values):
    return {(i, j) for i in range(len(values)) for j in range(len(values))
            if values[i] == values[j]}


def residual(u, q, label):
    return {q[i] for i in range(len(u)) if u[i] == label}


def descends(u, q):
    return kernel(u) <= kernel(q)


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def kron(a, b):
    return [[a[i][j] * b[k][l] for j in range(len(a[0]))
             for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def cmul(a, b):
    """Exact complex pair arithmetic over rational coordinates."""
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def effect(obs, bit):
    return [[(F(i == j) + (-1) ** bit * obs[i][j]) / 2
             for j in range(len(obs))] for i in range(len(obs))]


def profile_from_correlations(c):
    return {(x, y, a, b): (1 + (-1) ** (a + b) * c[x][y]) / 4
            for x, y, a, b in product(range(2), repeat=4)}


def valid_nonsignalling(p):
    if any(v < 0 for v in p.values()):
        return False
    for x, y in product(range(2), repeat=2):
        if sum(p[x, y, a, b] for a, b in product(range(2), repeat=2)) != 1:
            return False
    return (all(sum(p[x, 0, a, b] for b in range(2)) ==
                sum(p[x, 1, a, b] for b in range(2))
                for x, a in product(range(2), repeat=2)) and
            all(sum(p[0, y, a, b] for a in range(2)) ==
                sum(p[1, y, a, b] for a in range(2))
                for y, b in product(range(2), repeat=2)))


def chsh(c):
    return c[0][0] + c[0][1] + c[1][0] - c[1][1]


def main():
    # IQ1: exhaustive total binary U,Q on 0..4 entries, all binary bridges.
    for n in range(5):
        for u in product(range(2), repeat=n):
            for q in product(range(2), repeat=n):
                for bridge in product(range(2), repeat=2):
                    fu = tuple(bridge[i] for i in u)
                    for j in range(2):
                        union = set().union(*(residual(u, q, i)
                                              for i in range(2) if bridge[i] == j))
                        check(residual(fu, q, j) == union, 'IQ1_exhaustive')

    u, q = (0, 0), (0, 1)
    check(residual(u, q, 0) == {0, 1} and not descends(u, q), 'same_reduct')
    check(descends((0, 1), q) and not descends(u, q), 'lossy_bridge')
    check(residual(u, q, 1) == set(), 'empty_not_point')
    check(not descends(u, (1, 0)) and descends(u, (0, 0)), 'changed_contrast')
    # A record unrelated to F U invalidates IQ1's comparison square.
    check(residual((0, 1), q, 0) != residual(u, q, 0), 'missing_square')
    check({0} != {i for i, z in enumerate(u) if z == u[0]}, 'partial_domain')
    check(descends((0, 1), q) and q not in ((0, 0), (1, 1)), 'unavailable_decoder')

    u4, q4 = (0, 0, 1, 1), (0, 1, 2, 3)
    check(not descends(u4, q4) and descends(u4, tuple(a // 2 for a in q4)),
          'weakening')
    grid = tuple(product(range(2), repeat=2))
    row, col = tuple(x[0] for x in grid), tuple(x[1] for x in grid)
    check(len(kernel(row) & kernel(col)) == 4 and
          not descends(row, tuple(range(4))), 'independent_refinement')
    # Provenance cannot be inferred from this tautological diagram.
    check(descends(q4, q4), 'target_encoding_mathematical_control')
    binary_q = (0, 0, 1, 1)
    coarse, v, w = (0, 0, 0, 0), (0, 0, 1, 2), (0, 1, 2, 2)
    kv, kw = kernel(v), kernel(w)
    check(descends(v, binary_q) and descends(w, binary_q) and
          not descends(coarse, binary_q) and not kv <= kw and not kw <= kv,
          'incomparable_repairs')
    check(kernel(binary_q) > kv and kernel(binary_q) > kw,
          'unrestricted_diagnostic_minimum')
    cw, dw = (0, 0, 0, 1), (0, 0, 1, 0)
    check(len(set(cw[:2])) == len(set(dw[:2])) == 1 and
          not kernel(cw) <= kernel(dw) and not kernel(dw) <= kernel(cw),
          'incomparable_useful_weakenings')

    # Full finite homomorphism search, not just counting answer objects.
    homs = [h for h in product(range(2), repeat=4)
            if all(h[(a + b) % 4] == (h[a] + h[b]) % 2
                   for a, b in product(range(4), repeat=2))]
    check(len(homs) == 2 and all(h[2] == 0 for h in homs), 'coherence_failure')
    check(all((h[2] + t - t) % 2 != 1 for h in homs for t in range(2)),
          'natural_isomorphism_cannot_repair')
    c2_homs = [h for h in product(range(2), repeat=2)
               if all(h[(a + b) % 2] == (h[a] + h[b]) % 2
                      for a, b in product(range(2), repeat=2))]
    check((0, 1) in c2_homs, 'identity_coherent_factor')

    duplicated_u = tuple(a for a in u4 for _ in range(2))
    duplicated_q = tuple(a for a in q4 for _ in range(2))
    check(all(residual(duplicated_u, duplicated_q, b) == residual(u4, q4, b)
              for b in range(2)), 'carrier_duplication')
    for perm in permutations(range(4)):
        up, qp = tuple(u4[i] for i in perm), tuple(3 - q4[i] for i in perm)
        check(all(residual(up, qp, b) == {3 - a for a in residual(u4, q4, b)}
                  for b in range(2)), 'adequate_transport')
    check(descends((0,), (0,)) and not descends(u, q), 'local_not_final')
    # Discrete representation fibres over a terminal reduct: one then two objects.
    local_objects, expanded_objects = ('r0',), ('r0', 'r1')
    hom_count = lambda a, b: int(a == b)
    locally_rigid = all(hom_count(a, b) == 1
                        for a, b in product(local_objects, repeat=2))
    expanded_rigid = all(hom_count(a, b) == 1
                         for a, b in product(expanded_objects, repeat=2))
    check(locally_rigid and not expanded_rigid, 'local_categorical_rigidity_not_final')
    check(residual((0,), (0,), 0) < residual(u, q, 0), 'class_restriction')
    joint = residual(u, tuple(zip(q, q)), 0)
    check(joint < set(product(residual(u, q, 0), repeat=2)), 'joint_not_product')
    check(descends(u, tuple(a ^ b for a, b in zip(q, q))) and not descends(u, q),
          'invariant_composite')

    memory, report, experience_q = (0, 0, 1, 1), (0, 0, 0, 0), ('warm',) * 2 + ('cool',) * 2
    check(descends(memory, experience_q) and not descends(report, experience_q),
          'experiential_compression')
    check(not descends(memory, tuple(range(4))), 'finer_experiential_contrast')
    check(descends(memory, experience_q) and not descends(report, experience_q),
          'neural_bridge_positive_and_negative')
    richer_a, richer_b = (('r', 0), ('r', 0)), (('r', 0), ('r', 1))
    check({a[0] for a in richer_a} == {a[0] for a in richer_b} and
          len({a[1] for a in richer_a}) != len({a[1] for a in richer_b}),
          'same_report_different_richer_structure')

    # Classical Bell local-response class, exact 16 assignments.
    for a0, a1, b0, b1 in product((-1, 1), repeat=4):
        check(abs(a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1) == 2, 'classical')
    z, x = [[F(1), F(0)], [F(0), F(-1)]], [[F(0), F(1)], [F(1), F(0)]]
    bs = [[[ (3 * z[i][j] + sign * 4 * x[i][j]) / 5 for j in range(2)]
           for i in range(2)] for sign in (1, -1)]
    rho = [[F(1, 2) if i in (0, 3) and j in (0, 3) else F(0)
            for j in range(4)] for i in range(4)]
    check(trace(rho) == 1 and matmul(rho, rho) == rho, 'real_state')
    for obs in [z, x] + bs:
        check(matmul(obs, obs) == identity(2), 'real_projective_measurements')
    c = [[F(3, 5), F(3, 5)], [F(4, 5), F(-4, 5)]]
    p = profile_from_correlations(c)
    for ix, iy, a, b in product(range(2), repeat=4):
        value = trace(matmul(rho, kron(effect([z, x][ix], a), effect(bs[iy], b))))
        check(value == p[ix, iy, a, b], 'real_QM')
        # Recompute the trace in exact rational complex-pair coordinates.
        operator = kron(effect([z, x][ix], a), effect(bs[iy], b))
        complex_terms = [cmul((rho[i][j], F(0)), (operator[j][i], F(0)))
                         for i, j in product(range(4), repeat=2)]
        complex_value = tuple(sum(t[k] for t in complex_terms) for k in range(2))
        check(complex_value == (value, F(0)),
              'complex_QM_embedding')
    check(valid_nonsignalling(p) and chsh(c) == F(14, 5) > 2, 'Bell_separator')
    pr_c = [[F(1), F(1)], [F(1), F(-1)]]
    pr = profile_from_correlations(pr_c)
    check(valid_nonsignalling(pr) and chsh(pr_c) == 4, 'boxworld')
    check(set(p.values()) != set(pr.values()), 'class_specific_separator')
    uniform = profile_from_correlations([[F(0)] * 2 for _ in range(2)])
    local_uniform = {(ix, iy, a, b): sum(F(outputs[ix] == a and outputs[2 + iy] == b, 16)
                                       for outputs in product(range(2), repeat=4))
                     for ix, iy, a, b in product(range(2), repeat=4)}
    check(valid_nonsignalling(uniform) and uniform == local_uniform,
          'almost_quantum_common_classical_control')

    supports = {(0, 1): {(0, 1), (1, 0)}, (1, 2): {(0, 1), (1, 0)},
                (0, 2): {(0, 1), (1, 0)}}
    join = [a for a in product(range(2), repeat=3)
            if all((a[i], a[j]) in s for (i, j), s in supports.items())]
    check(not join and all({a for a, b in s} == {0, 1} and
                          {b for a, b in s} == {0, 1} for s in supports.values()),
          'contextual_non_globalizable')

    # Same orthogonality graph and sparse behaviour, different ranks.
    ranks, projectors = (1, 2), ((1, 0, 0, 0), (1, 1, 0, 0))
    for rank, proj in zip(ranks, projectors):
        complement = tuple(1 - a for a in proj)
        check(sum(proj) == rank and all(a * b == 0 for a, b in zip(proj, complement)),
              'rank_orthogonality')
    sparse = tuple((proj[0], proj[3]) for proj in projectors)
    rich = tuple((proj[0], proj[1], proj[3]) for proj in projectors)
    check(not descends(sparse, ranks) and descends(rich, ranks), 'theoretical_representation')
    check(residual(sparse, ranks, sparse[0]) == {1, 2}, 'IQ1_quantum_instance')
    check(residual(report, experience_q, 0) == {'warm', 'cool'}, 'IQ1_consciousness_instance')

    # Diagonal quaternionic/Jordan sector via four-copy real embedding.
    rho_q = [[F(1, 2) if i == j else F(0) for j in range(8)] for i in range(8)]
    eff_q = [[F(i == j and i < 4) for j in range(8)] for i in range(8)]
    check(trace(rho_q) / 4 == 1 and trace(matmul(rho_q, eff_q)) / 4 == F(1, 2),
          'quaternionic_Jordan_commuting_sector')
    # Ordinary classical pure bipartite distributions are point masses.
    pure_marginals = {tuple(sum(dist[2 * a + b] for b in range(2)) for a in range(2))
                      for dist in identity(4)}
    check((F(1, 2), F(1, 2)) not in pure_marginals and
          pure_marginals == {(F(1), F(0)), (F(0), F(1))},
          'classical_no_mixed_pure_purification')
    check(4 * 5 // 2 == 10 and (2 * 3 // 2) ** 2 == 9, 'real_local_tomography_failure')
    print('INTERFACE_QUESTION_FINITE_PASS', sum(counts.values()), 'assertions')
    for name, count in sorted(counts.items()):
        print(name, count)


if __name__ == '__main__':
    main()
