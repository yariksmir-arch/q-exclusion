"""Negative controls for specific invalid semantic inferences; not metaphysical tests."""
from itertools import product

def factors(xs, u, f):
    return all(u(x) != u(y) or f(x) == f(y) for x in xs for y in xs)

def main():
    xs = tuple(product((0, 1), repeat=2))
    assert not factors(xs, lambda x: x[0], lambda x: x[1])
    # Richer declared discrimination remains consistent with the coarse report.
    assert factors(xs, lambda x: x, lambda x: x[1])
    # Exact readout factor exists on the occupied image, not uniquely off it.
    u = {0: 'used', 1: 'used'}
    factors_off_image = [{'used': 0, 'unused': y} for y in (0, 1)]
    assert all(all(d[u[x]] == 0 for x in u) for d in factors_off_image)
    assert factors_off_image[0] != factors_off_image[1]
    # Same declared instrument interface admits either uninterpreted decoration.
    # Neither decoration is evidence about consciousness.
    interface = ('read', (0, 1))
    packages = [(interface, tag) for tag in (0, 1)]
    assert not factors(packages, lambda p: p[0], lambda p: p[1])
    # Compression cannot infer equality of richer discriminations from reports.
    assert not factors(('a', 'b'), lambda x: 'report', lambda x: x)
    # Mathematical availability and represented executable availability differ.
    decoders = [lambda x: 0, lambda x: 1]
    assert factors((0, 1), lambda x: x, lambda x: x)
    assert not any(all(d(x) == x for x in (0, 1)) for d in decoders)
    # Pairwise-consistent Boolean constraints have no joint solution.
    assert all({r[0] for r in rel} == {0, 1} and {r[1] for r in rel} == {0, 1}
               for rel in ({(0, 0), (1, 1)}, {(0, 1), (1, 0)}))
    assert not [(a, b, c) for a, b, c in product((0, 1), repeat=3)
                if a == b and b == c and a != c]
    # Covering the desired rational weights does not exclude other profile clusters.
    fixed_profile_hull = {0}
    family_predictions = {0, 1}
    assert 0 in family_predictions and family_predictions != fixed_profile_hull
    # A fixed finite batch equation does not determine a later profile limit.
    def z_profile(n):
        return 0 if n <= 2 else 1
    assert z_profile(2) == (0 + 0) / 2
    assert z_profile(4) != (0 + 0) / 2
    print('SEMANTIC_TRANSITION_CONTROLS_PASS (finite counterexamples; no test confirms SS)')

if __name__ == '__main__':
    main()
