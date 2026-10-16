"""Finite semantic kill witnesses, not mechanized general proofs (stdlib only)."""
from itertools import product, combinations


def partitions(n):
    def visit(prefix):
        if len(prefix) == n:
            yield tuple(prefix)
        else:
            for v in range(max(prefix, default=-1) + 2):
                yield from visit(prefix + [v])
    yield from visit([])


def forced(js):
    n = len(js[0])
    return {(i, j) for i in range(n) for j in range(n)
            if all(p[i] == p[j] for p in js)}


def main():
    # CI skeleton: every completion obeys a=b OR b=c; their intersection does not.
    js = [p for p in partitions(3) if p[0] == p[1] or p[1] == p[2]]
    f = forced(js)
    assert f == {(0, 0), (1, 1), (2, 2)}
    assert not ((0, 1) in f or (1, 2) in f)
    xor_js = [p for p in partitions(3) if (p[0] == p[1]) ^ (p[1] == p[2])]
    joint = {(p[0] == p[1], p[1] == p[2]) for p in xor_js}
    assert joint == {(True, False), (False, True)}
    assert (True, True) not in joint
    # Universal co-reference alone cannot carry varying interaction availability.
    same_pair = [p for p in partitions(2) if p[0] == p[1]]
    assert forced(same_pair) == set(product(range(2), repeat=2))
    packages = [(same_pair[0], available) for available in (False, True)]
    assert len({x[1] for x in packages}) == 2
    # Difference, persistence and process are three independent declared bits.
    classify = lambda process, persist, diff: bool(process and persist and diff)
    assert not classify(0, 1, 1)  # difference without represented change
    assert not classify(1, 1, 0)  # persistence without difference
    assert not classify(1, 0, 1)  # process without persistence
    assert classify(1, 1, 1)
    ambiguous = [p for p in partitions(2)]
    assert {classify(1, p[0] == p[1], 1) for p in ambiguous} == {False, True}
    edges = {(0, 1), (1, 0)}
    assert all(classify(1, 1, a != b) for a, b in edges)  # reversible/cyclic
    assert classify(1, 1, 0 != 1) and classify(1, 1, 1 != 0)
    assert not classify(1, 1, 0 != 0)  # composite change cancels
    assert [(p, c) for p, c in product((0, 1), repeat=2)
            if p == c and c == (p and 1)] == [(0, 0), (1, 1)]
    # Law scope / prediction / modal decoration.
    records = {'a': 0, 'b': 1}
    assert all(records[x] == 0 for x in ('a',))
    assert not all(records[x] == 0 for x in records)
    assert all(records[x] in (0, 1) for x in records)
    assert len(set(records.values())) == 2  # constant input is insufficient
    assert all([])  # vacuity is not an empirical certificate
    assert len({(tuple(records.items()), tag) for tag in (0, 1)}) == 2
    # Context tables are explicitly separate locally executable procedures.
    contexts = ((0, 1), (1, 2), (0, 2))
    def family(bits):
        return {c: {(a, b) for a, b in product((0, 1), repeat=2)
                    if (a ^ b) == bit} for c, bit in zip(contexts, bits)}
    def projection(c, table, common):
        return {tuple(row[c.index(i)] for i in common) for row in table}
    def overlap_ok(tables):
        return all(projection(c, tables[c], tuple(sorted(set(c) & set(d)))) ==
                   projection(d, tables[d], tuple(sorted(set(c) & set(d))))
                   for c, d in combinations(contexts, 2))
    def join(tables):
        return {v for v in product((0, 1), repeat=3)
                if all(tuple(v[i] for i in c) in tables[c] for c in contexts)}
    anti = family((1, 1, 1))
    assert overlap_ok(anti) and not join(anti)
    # The concrete local generators/projections ignore empirical fibre tags.
    raw = list(product((0, 1), ('tag0', 'tag1')))
    generator = lambda item: (item[0], 1 - item[0])
    assert {generator(item) for item in raw} == {(0, 1), (1, 0)}
    for x, y in product(raw, repeat=2):
        if x[0] == y[0]:
            assert generator(x) == generator(y)
    defective = lambda item: item[0] ^ (item[1] == 'tag1')
    assert defective((0, 'tag0')) != defective((0, 'tag1'))
    # All eight parity triangles have exact overlap agreement; parity is obstruction.
    parity_cases = 0
    for bits in product((0, 1), repeat=3):
        tables = family(bits)
        assert overlap_ok(tables)
        assert bool(join(tables)) == (bits[0] ^ bits[1] ^ bits[2] == 0)
        assert len(join(tables)) in (0, 2)
        parity_cases += 1
        # Independent coordinate bijections preserve sections/obstructions and projections.
        for flips in product((0, 1), repeat=3):
            moved = {c: {tuple(v ^ flips[i] for v, i in zip(row, c))
                         for row in table} for c, table in tables.items()}
            assert overlap_ok(moved)
            assert join(moved) == {tuple(v ^ t for v, t in zip(row, flips))
                                   for row in join(tables)}
    # Pair-valid but overlap-incompatible: singleton tables disagree on role 1.
    broken = {(0, 1): {(0, 0)}, (1, 2): {(1, 0)}, (0, 2): {(0, 0)}}
    assert all(broken.values()) and not overlap_ok(broken)
    # ICC7 composition requires joint middle role; empty all-context join has no verdict.
    partial = {(a, b, c) for a, b, c in product((0, 1), repeat=3)
               if a == b and b != c}
    assert partial and all(a != c for a, b, c in partial)
    assert not {v for v in partial if v[0] == v[2]}
    print(f'SEMANTIC_ROLES_PASS: CI/package/change/law kill witnesses; '
          f'{parity_cases} parity families, 64 transported network cases')


if __name__ == '__main__':
    main()
