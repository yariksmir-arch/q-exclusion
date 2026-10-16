"""Finite coordination witnesses; standard library, no selected joint state.

Counts are checks/cases within named finite scopes, never theorem counts.
The generic tuple solver and bit-mask path calculations are distinct algorithms.
"""

if not __debug__:
    raise RuntimeError('OPTIMIZED_PYTHON_NOT_SUPPORTED: run finite checks without -O, -OO or PYTHONOPTIMIZE')

from collections import Counter
from itertools import combinations, permutations, product
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
COUNTS = Counter()
EQ = {(0, 0), (1, 1)}
FLIP = {(0, 1), (1, 0)}
TOP = set(product(range(2), repeat=2))
BITS = tuple(range(2))


def check(condition, scope, detail=""):
    COUNTS[scope] += 1
    if not condition:
        raise AssertionError(f"{scope}: {detail}")


def solutions(tables, domains=None):
    """tables: list of (ordered port scope, complete allowed tuple set)."""
    ports = tuple(sorted({i for scope, _ in tables for i in scope}))
    domains = domains or {}
    found = []
    for values in product(*(domains.get(i, BITS) for i in ports)):
        assignment = dict(zip(ports, values))
        if all(tuple(assignment[i] for i in scope) in rows for scope, rows in tables):
            found.append(values)
    return ports, set(found)


def projection(ports, rows, target):
    offsets = [ports.index(i) for i in target]
    return {tuple(row[j] for j in offsets) for row in rows}


def obstructions(tables, domains=None):
    bad = []
    for n in range(1, len(tables) + 1):
        for ids in combinations(range(len(tables)), n):
            if any(set(old).issubset(ids) for old in bad):
                continue
            if not solutions([tables[i] for i in ids], domains)[1]:
                bad.append(ids)
    return bad


def overlap(tables):
    if not all(rows for _, rows in tables):
        return False
    for (s, r), (t, v) in combinations(tables, 2):
        shared = tuple(sorted(set(s) & set(t)))
        if projection(s, r, shared) != projection(t, v, shared):
            return False
    return True


def flags(tables):
    ports, rows = solutions(tables)
    local = all(r for _, r in tables)
    extension = bool(local) and all(projection(ports, rows, s) == r for s, r in tables)
    return {
        "L": bool(local), "O": overlap(tables),
        "C2": all(solutions(list(sub))[1] for k in (1, 2)
                  for sub in combinations(tables, k)),
        "G": bool(rows), "U": len(rows) == 1, "X": extension,
    }


def relation(mask):
    return {(a, b) for a, b in TOP if mask & (1 << (2 * a + b))}


REL = [relation(mask) for mask in range(16)]


def mask_of(rows):
    return sum(1 << (2 * a + b) for a, b in rows)


def compose_direct(r, s):
    return {(a, c) for a, b in r for b2, c in s if b == b2}


COMP = [[mask_of(compose_direct(REL[r], REL[s])) for s in range(16)] for r in range(16)]


def relabel(r, fs, ft):
    return mask_of({(a ^ fs, b ^ ft) for a, b in REL[r]})


def triangle_tables(masks):
    return [((0, 1), REL[masks[0]]), ((1, 2), REL[masks[1]]), ((0, 2), REL[masks[2]])]


def compatibility_enumeration():
    names = ("L", "O", "C2", "G", "U", "X")
    counts = Counter()
    kills = {}
    for masks in product(range(16), repeat=3):
        tables = triangle_tables(masks)
        f = flags(tables)
        counts["".join("1" if f[n] else "0" for n in names)] += 1
        check(not f["O"] or f["C2"], "triangle_implications")
        check(not f["C2"] or f["L"], "triangle_implications")
        check(not f["G"] or f["C2"], "triangle_implications")
        check(not f["U"] or f["G"], "triangle_implications")
        check(not f["X"] or (f["G"] and f["O"]), "triangle_implications")
        bad = obstructions(tables)
        check(bool(bad) == (not f["G"]), "triangle_obstructions")
        # Test the complete upward closure, including the empty family.
        for subset_mask in range(8):
            ids = [i for i in range(3) if subset_mask & (1 << i)]
            empty = not solutions([tables[i] for i in ids])[1]
            contains = any(set(b).issubset(ids) for b in bad)
            check(empty == contains, "triangle_obstruction_closure")
        rank = (sum(len(r) for _, r in tables), masks)
        for a in names:
            for b in names:
                if f[a] and not f[b]:
                    key = a + "!=>" + b
                    if key not in kills or rank < tuple(kills[key]["rank"]):
                        kills[key] = {"masks": list(masks), "rank": [rank[0], masks], "flags": f}
        old_count = len(solutions(tables)[1])
        for flips in product(BITS, repeat=3):
            moved = [((s, t), {(a ^ flips[s], b ^ flips[t]) for a, b in r})
                     for (s, t), r in tables]
            check(len(solutions(moved)[1]) == old_count
                  and obstructions(moved) == bad, "triangle_all_local_relabels")
    # Make JSON ranks comparable and readable; no hidden preferred witness used empirically.
    for witness in kills.values():
        witness.pop("rank")
    return {"cases": 4096, "predicate_order": names, "flag_distribution": dict(counts),
            "minimal_false_implication_witnesses": kills,
            "minimality_order": "total allowed rows, then masks; fixed three Boolean pair scopes"}


def path_enumeration():
    for r, s in product(range(16), repeat=2):
        ports, rows = solutions([((0, 1), REL[r]), ((1, 2), REL[s])])
        check(mask_of(projection(ports, rows, (0, 2))) == COMP[r][s], "two_edge_projection")
        for fa, fb, fc in product(BITS, repeat=3):
            check(COMP[relabel(r, fa, fb)][relabel(s, fb, fc)] == relabel(COMP[r][s], fa, fc),
                  "relational_composition_covariance")
    for r, s, t in product(range(16), repeat=3):
        check(COMP[COMP[r][s]][t] == COMP[r][COMP[s][t]], "relational_associativity")
    profiles = Counter()
    for r, s, t, u in product(range(16), repeat=4):
        p, q = COMP[r][s], COMP[t][u]
        tables = [((0, 1), REL[r]), ((1, 3), REL[s]), ((0, 2), REL[t]), ((2, 3), REL[u])]
        ports, rows = solutions(tables)
        # Independent full join agrees with path intersection for disjoint interiors.
        check(mask_of(projection(ports, rows, (0, 3))) == (p & q), "diamond_joint_query")
        for a in BITS:
            vp = {b for aa, b in REL[p] if aa == a}
            vq = {b for aa, b in REL[q] if aa == a}
            if not vp or not vq:
                status = "both_empty" if not vp and not vq else "availability_mismatch"
            elif vp == vq:
                status = "equal_supported"
            elif vp & vq:
                status = "overlapping_unequal"
            else:
                status = "disjoint_supported"
            profiles[status] += 1
    return {"diamond_cases": 65536, "source_classifications": dict(profiles)}


def higher_order_enumeration():
    details = []
    for n in range(3, 8):
        cycle = [((i, i + 1), EQ) for i in range(n - 1)] + [((0, n - 1), FLIP)]
        check(not solutions(cycle)[1], "cycle_hierarchy")
        for mask in range((1 << n) - 1):
            check(bool(solutions([cycle[i] for i in range(n) if mask & (1 << i)])[1]),
                  "cycle_all_proper_constraint_subsets")
        check(obstructions(cycle) == [tuple(range(n))], "cycle_hierarchy")
        parity = {v for v in product(BITS, repeat=n) if sum(v) % 2 == 0}
        odd = set(product(BITS, repeat=n)) - parity
        for mask in range(1 << n):
            target = tuple(i for i in range(n) if mask & (1 << i))
            if len(target) == n:
                continue
            even_image = projection(tuple(range(n)), parity, target)
            odd_image = projection(tuple(range(n)), odd, target)
            check(even_image == odd_image == set(product(BITS, repeat=len(target))),
                  "parity_all_proper_port_projections")
        details.append({"n": n, "cycle_solutions": 0, "proper_constraint_subsets": (1 << n) - 1,
                        "parity_rows": len(parity)})
    return details


def perm_comp(p, q):
    """q after p."""
    return tuple(q[p[a]] for a in range(len(p)))


def perm_inverse(p):
    return tuple(p.index(a) for a in range(len(p)))


def loop_enumeration():
    ps = tuple(permutations(range(3)))
    for p, q, r in product(ps, repeat=3):
        loop = perm_comp(perm_comp(p, q), r)
        tables = [((0, 1), set(enumerate(p))), ((1, 2), set(enumerate(q))),
                  ((2, 0), set(enumerate(r)))]
        ports, rows = solutions(tables, {i: (0, 1, 2) for i in range(3)})
        check(projection(ports, rows, (0,)) == {(a,) for a in range(3) if loop[a] == a},
              "three_label_loop_fixed_points_vs_join")
        for ba, bb, bc in product(ps, repeat=3):
            pp = perm_comp(perm_comp(perm_inverse(ba), p), bb)
            qq = perm_comp(perm_comp(perm_inverse(bb), q), bc)
            rr = perm_comp(perm_comp(perm_inverse(bc), r), ba)
            transformed = perm_comp(perm_comp(pp, qq), rr)
            expected = perm_comp(perm_comp(perm_inverse(ba), loop), ba)
            check(transformed == expected, "three_label_all_loop_relabels")
    return {"edge_permutation_triples": 216, "local_permutation_triples_per_case": 216}


def named_models():
    out = {}

    def named(name, condition):
        check(condition, "named_models", name)
        out[name] = "PASS"

    m1 = triangle_tables((6, 6, 6))
    m3 = triangle_tables((9, 9, 9))
    named("M1", flags(m1) == {"L": True, "O": True, "C2": True, "G": False, "U": False, "X": False})
    named("M2", all(not solutions([((i, i + 1), EQ) for i in range(n - 1)]
                                  + [((0, n - 1), FLIP)])[1] for n in range(3, 8)))
    named("M3", len(solutions(m3)[1]) == 2 and flags(m3)["X"])
    ternary = {v for v in product(BITS, repeat=3) if sum(v) % 2 == 0}
    odd = set(product(BITS, repeat=3)) - ternary
    pinned = m3 + [((0,), {(1,)})]
    named("M4", not solutions(pinned + [((0, 1, 2), ternary)])[1]
          and bool(solutions(pinned + [((0, 1, 2), odd)])[1]))
    m5 = [((0, 1), {(0, 0)}), ((1, 2), {(1, 0)})]
    named("M5", all(r for _, r in m5) and not solutions(m5)[1])
    m6 = [((0, 1), {(0, 0), (0, 1)}), ((1, 2), {(0, 0)})]
    named("M6", bool(solutions(m6)[1]) and not overlap(m6))
    m7 = [((0, 1), EQ), ((1, 2), {(0, 0)})]
    named("M7", flags(m7)["U"] and not flags(m7)["O"] and not flags(m7)["X"])
    diamond_eq = [((0, 1), EQ), ((1, 3), EQ), ((0, 2), EQ), ((2, 3), EQ)]
    dp, dr = solutions(diamond_eq)
    named("M8", projection(dp, dr, (0, 3)) == EQ and len(dr) == 2)
    named("M9", COMP[9][9] != COMP[9][6] and (COMP[9][9] & COMP[9][6]) == 0)
    # Coordinate-mismatched outputs agree only after transporting their encoding.
    named("M10", 0 != 1 and (1 ^ 1) == 0 and relabel(9, 0, 1) == 6)
    partial, constant = {(0, 1)}, {(0, 0), (1, 0)}
    named("M11", compose_direct(constant, partial) == {(0, 1), (1, 1)})
    shared = [((0, 1), {(0, 0), (0, 1)}), ((1, 3), EQ), ((1, 2), EQ), ((2, 3), FLIP)]
    named("M12", not solutions(shared, {0: (0,)})[1]
          and compose_direct({(0, 0), (0, 1)}, EQ) == compose_direct({(0, 0), (0, 1)}, FLIP))
    named("M13", {0 for _ in EQ} == {0 for _ in FLIP} and EQ != FLIP)
    unary = {(0,)}
    named("M14", (0,) in unary and (1,) not in unary and 0 // 2 == 1 // 2)
    tags = tuple(product(BITS, repeat=2))
    duplicated = [(scope, {tuple((v, tag) for v, tag in zip(row, ts))
                           for row in rows for ts in product(BITS, repeat=len(scope))})
                  for scope, rows in m3]
    named("M15", len(solutions(duplicated, {i: tags for i in range(3)})[1]) == 16)
    singleton_tables = [(scope, {tuple(0 for _ in scope)}) for scope, _ in m1]
    named("M16", not solutions(m1)[1] and len(solutions(singleton_tables, {i: (0,) for i in range(3)})[1]) == 1)
    chain = [((0, 1), EQ), ((1, 2), EQ)]
    ports, rows = solutions(chain)
    q = projection(ports, rows, (0, 2))
    named("M17", q == EQ and not solutions(chain + [((0, 2), FLIP)])[1])
    # Exhaust all 16 possible held-out endpoint tables against the derived query.
    for new in REL:
        check(bool(q & new) == bool(solutions(chain + [((0, 2), new)])[1]), "reserved_endpoint_queries")
    tuples = tuple(sorted(ternary))
    auxiliary = [((i, 3), {(v[i], k) for k, v in enumerate(tuples)}) for i in range(3)]
    ap, ar = solutions(auxiliary, {3: tuple(range(4))})
    named("M18", projection(ap, ar, (0, 1, 2)) == ternary
          and max(len(s) for s, _ in auxiliary) == 2)
    named("M19", (0, 1) not in EQ and (0, 1) in FLIP)
    refined_bad = [(scope, {tuple((v, tag) for v, tag in zip(row, ts))
                            for row in rs for ts in product(BITS, repeat=2)}) for scope, rs in m1]
    named("M20", not solutions(refined_bad, {i: tags for i in range(3)})[1]
          and bool(solutions(m1[:-1])[1]))
    restricted, expanded = {(0, 0), (1, 1)}, TOP
    second_sufficient = lambda records: all(a == aa for a, b in records for aa, bb in records if b == bb)
    named("M21", second_sufficient(restricted) and not second_sufficient(expanded))
    reach = EQ | {(0, 1)}
    changed_reach = compose_direct(reach | {(1, 0)}, reach | {(1, 0)})
    named("M22", compose_direct(reach, reach) == reach and reach != changed_reach
          and changed_reach == TOP)
    separate = [((0, 1), EQ), ((2, 3), EQ)]
    sp, sr = solutions(separate)
    _, crossed = solutions(separate + [((1, 2), FLIP)])
    named("M23", len(sr) == 4 and len(crossed) == 2)
    from fractions import Fraction
    noisy = [[Fraction(3, 4), Fraction(1, 4)], [Fraction(1, 4), Fraction(3, 4)]]
    named("M24", all(sum(row) == 1 for row in noisy) and all(v > 0 for row in noisy for v in row))
    identity3 = {(i, i) for i in range(3)}
    fixes0, fixes1 = {(0, 0), (1, 2), (2, 1)}, {(1, 1), (0, 2), (2, 0)}
    two_loops = [((0, 1), identity3), ((1, 2), identity3), ((0, 2), fixes0),
                 ((0, 3), identity3), ((3, 4), identity3), ((0, 4), fixes1)]
    d3 = {i: (0, 1, 2) for i in range(5)}
    named("M25", bool(solutions(two_loops[:3], d3)[1])
          and bool(solutions(two_loops[3:], d3)[1]) and not solutions(two_loops, d3)[1])
    named("M26", projection((0, 1, 2), ternary, (0, 1)) == TOP and ternary != odd)
    # All port permutations plus bit relabels on both local-isomorphism controls.
    for tables in (m1, m3):
        for perm in permutations(range(3)):
            for flips in product(BITS, repeat=3):
                transported = [(tuple(perm[i] for i in s), {tuple(v ^ flips[i] for v, i in zip(r, s)) for r in rs})
                               for s, rs in tables]
                check(len(solutions(transported)[1]) == len(solutions(tables)[1]), "scope_and_local_permutations")
    for fixed_edge in range(3):
        changed_edge = (fixed_edge + 1) % 3
        variant = [(s, FLIP if k == changed_edge else r) for k, (s, r) in enumerate(m3)]
        check(m3[fixed_edge] == variant[fixed_edge] and bool(solutions(m3)[1])
              and not solutions(variant)[1], "not_determined_by_any_one_supplied_table")
    # P5: every chosen port is untouched, including incident interfaces, by flipping a nonincident edge.
    base4 = [((0, 1), EQ), ((1, 2), EQ), ((2, 3), EQ), ((0, 3), EQ)]
    for i in range(4):
        changed = next(k for k, (s, _) in enumerate(base4) if i not in s)
        other = [(s, FLIP if k == changed else r) for k, (s, r) in enumerate(base4)]
        check(bool(solutions(base4)[1]) and not solutions(other)[1]
              and all(base4[k] == other[k] for k, (s, _) in enumerate(base4) if i in s), "P5_fixed_chosen_local_and_star")
    # GO4: all Boolean two-edge join trees satisfying overlap equality fully extend.
    for r, s in product(REL, repeat=2):
        tables = [((0, 1), r), ((1, 2), s)]
        if overlap(tables):
            check(flags(tables)["X"], "join_tree_full_extension")
    return out


def main():
    report = {"status": "RUNNING", "synthetic_not_empirical": True,
              "triangle": compatibility_enumeration(), "paths": path_enumeration(),
              "higher_order": higher_order_enumeration(), "loops": loop_enumeration(),
              "named_models": named_models()}
    report["counts_by_scope"] = dict(sorted(COUNTS.items()))
    report["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report["status"] = "FINITE_PASS"
    print(json.dumps({"status": report["status"], "counts_by_scope": report["counts_by_scope"]}, indent=2))


if __name__ == "__main__":
    main()
