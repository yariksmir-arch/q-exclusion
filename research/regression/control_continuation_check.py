"""Finite kernel/capacity/domain/transport controls for CMQ and CPC. Stdlib only."""
from itertools import product, combinations
import sys

sys.dont_write_bytecode = True


def kernel(carrier, record):
    return {(x, y) for x in carrier for y in carrier if record(x) == record(y)}


def partitions(items):
    if not items:
        yield []
        return
    first, *tail = items
    for blocks in partitions(tail):
        yield [{first}] + blocks
        for i in range(len(blocks)):
            yield blocks[:i] + [blocks[i] | {first}] + blocks[i + 1:]


def main():
    count = 0
    h = tuple(range(3))
    # All 3-value record functions and binary procedure readouts on 3 inputs.
    for bits in product(range(2), repeat=3):
        alpha = kernel(h, lambda x: bits[x])
        for values in product(range(3), repeat=3):
            km = kernel(h, lambda x: values[x])
            enough = all(len({bits[x] for x in h if values[x] == m}) == 1
                         for m in set(values))
            assert enough == (km <= alpha)
            if enough:
                assert len(set(values)) >= len(set(bits))
            count += 1
    # Complete finite append graphs: descent iff saturated domain + class values.
    b = (0, 0, 1)
    alpha = kernel(h, lambda x: b[x])
    for outputs in product((None, 0, 1, 2), repeat=3):
        saturated = all((outputs[x] is None) == (outputs[y] is None)
                        for x, y in alpha)
        invariant = all(b[outputs[x]] == b[outputs[y]] for x, y in alpha
                        if outputs[x] is not None and outputs[y] is not None)
        encoded = {x: None if outputs[x] is None else b[outputs[x]] for x in h}
        factors = all(encoded[x] == encoded[y] for x, y in alpha)
        assert factors == (saturated and invariant)
        count += 1
    assert b[0] == b[1] and b[0] != b[2]  # CMQ-M1 update obstruction
    # Policy-family refinement; class counts and coarse maps.
    for bits in product(range(2), repeat=3):
        coarse = kernel(h, lambda x: b[x])
        fine = kernel(h, lambda x: (b[x], bits[x]))
        assert fine <= coarse
        assert len({(b[x], bits[x]) for x in h}) >= len(set(b))
        count += 1
    # Different raw carriers, equal complete profiles; arbitrary collapse fails.
    wrappers = [(x, k) for x in h for k in range(x + 1)]
    assert {b[x] for x in h} == {b[x] for x, k in wrappers}
    assert {b[x] for x in h} != {0}
    count += 2
    # Minimal binary correlation table witness, exhaustive table pairs.
    cells = tuple(product(range(2), repeat=2))
    tables = [set(c) for n in range(5) for c in combinations(cells, n)]
    def marginal(j):
        return ({o for o, c in j}, {c for o, c in j})
    def fixed(j, u):
        return {int(c == u) for o, c in j}
    def adaptive(j):
        return {int(c == o) for o, c in j}
    witnesses = [(j, k) for j in tables for k in tables
                 if marginal(j) == marginal(k)
                 and all(fixed(j, u) == fixed(k, u) for u in range(2))
                 and adaptive(j) != adaptive(k)]
    assert witnesses
    assert min(max(len(j), len(k)) for j, k in witnesses) == 2
    assert all(len(j) >= 2 and len(k) >= 2 for j, k in witnesses)
    count += len(tables) ** 2
    # BCS3: independent enumeration of all equivalence candidates, including
    # disabled versus enabled-empty; compare against fixed-point elimination.
    from control_branching_check import bisim
    subsets = [set(c) for n in range(4) for c in combinations(h, n)]
    candidates = []
    for blocks in partitions(list(h)):
        labels = {x: i for i, block in enumerate(blocks) for x in block}
        candidates.append((labels, kernel(h, lambda x: labels[x])))
    for bits in product(range(2), repeat=3):
        for outputs in product([None] + subsets, repeat=3):
            trans = {(x, 'u'): outputs[x] for x in h if outputs[x] is not None}
            upper = kernel(h, lambda x: bits[x])
            stable = []
            for labels, relation in candidates:
                if relation <= upper and all(
                    (outputs[x] is None) == (outputs[y] is None)
                    and (outputs[x] is None or
                         {labels[z] for z in outputs[x]} ==
                         {labels[z] for z in outputs[y]})
                    for x, y in relation):
                    stable.append(relation)
            assert set().union(*stable) == bisim(dict(enumerate(bits)), trans)
            count += 1
    print(f'REGRESSION_PASS ({count} finite continuation/control checks)')


if __name__ == '__main__':
    main()
