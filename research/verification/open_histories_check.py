"""Finite witnesses for OPEN_HISTORICAL_MULTIPLICITY.md; stdlib, read-only."""
import itertools
import json
import sys

if not __debug__:
    raise SystemExit("Run without Python optimization: assertions are required")


def factors(obs, target):
    # Independently enumerate every decoder on the occupied record image.
    image = sorted(set(obs))
    values = sorted(set(target))
    return any(all(d[image.index(x)] == y for x, y in zip(obs, target))
               for d in itertools.product(values, repeat=len(image)))


def kernel_inclusion(obs, target):
    return all(x != y or target[i] == target[j]
               for i, x in enumerate(obs) for j, y in enumerate(obs))


def exact_update_exists(m, a):
    image = sorted(set(m))
    # -1 marks unavailable; enumerate partial updates, including domain.
    for outputs in itertools.product([-1] + image, repeat=len(image)):
        if all(outputs[image.index(m[h])] == (-1 if t == -1 else m[t])
               for h, t in enumerate(a)):
            return True
    return False


def main():
    cases = {"factorizations": 0, "partial_updates": 0, "retention": 0,
             "relabellings": 0}
    for n in range(1, 4):
        for m in itertools.product(range(2), repeat=n):
            for r in itertools.product(range(2), repeat=n):
                assert factors(m, r) == kernel_inclusion(m, r)
                cases["factorizations"] += 1
            for a in itertools.product(range(-1, n), repeat=n):
                saturated = all(m[i] != m[j] or (a[i] == -1) == (a[j] == -1)
                                for i in range(n) for j in range(n))
                constant = all(m[i] != m[j] or m[a[i]] == m[a[j]]
                               for i in range(n) for j in range(n)
                               if a[i] != -1 and a[j] != -1)
                exists = exact_update_exists(m, a)
                assert exists == (saturated and constant)
                cases["partial_updates"] += 1
                for r in itertools.product(range(2), repeat=n):
                    obs = tuple(m[t] for t in a if t != -1)
                    past = tuple(r[i] for i, t in enumerate(a) if t != -1)
                    assert factors(obs, past) == kernel_inclusion(obs, past)
                    cases["retention"] += 1
                for p in itertools.permutations(range(n)):
                    inverse = {old: new for new, old in enumerate(p)}
                    mm = tuple(1 - m[old] for old in p)
                    aa = tuple(-1 if a[old] == -1 else inverse[a[old]] for old in p)
                    assert exact_update_exists(mm, aa) == exists
                    cases["relabellings"] += 1

    assert exact_update_exists((0, 1), (0, 0))
    assert not factors((0, 0), (0, 1))  # erasure despite exact update
    assert not exact_update_exists((0, 0, 1), (0, 2, 2))
    assert not exact_update_exists((0, 0, 1), (0, -1, -1))
    assert set((0,)) == set((0, 0))  # same profile image, different carriers
    assert not factors((0, 0), (0, 1))  # forgotten provenance / selector
    histories = list(itertools.product(range(2), repeat=2))
    first = tuple(x for x, y in histories)
    joint = tuple(histories)
    assert len(set(zip(first, first))) == 2  # redundant channels
    assert len(set(joint)) == 4  # jointly usable complementary probes
    assert not factors(first, tuple(y for x, y in histories))
    assignments = list(itertools.product(range(2), repeat=3))
    constraints = [lambda x,y,z: x == y, lambda x,y,z: y == z,
                   lambda x,y,z: z != x]
    assert all(any(c(*v) for v in assignments) for c in constraints)
    assert all(any(c(*v) and d(*v) for v in assignments)
               for c, d in itertools.combinations(constraints, 2))
    assert not any(all(c(*v) for c in constraints) for v in assignments)
    assert not any(p.index(0) < p.index(1) and p.index(1) < p.index(0)
                   for p in itertools.permutations(range(2)))
    print(json.dumps({"status": "OPEN_HISTORIES_PASS", "cases": cases,
                      "semantic_controls": "explicit finite witnesses only",
                      "general_proofs_mechanized": False}, sort_keys=True))


if __name__ == "__main__":
    main()
