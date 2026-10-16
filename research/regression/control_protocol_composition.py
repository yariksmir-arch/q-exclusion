"""Finite CPC4/CPC5 witnesses; not mechanized proofs of general theorems."""

if not __debug__:
    raise RuntimeError('OPTIMIZED_PYTHON_NOT_SUPPORTED: run finite checks without -O, -OO or PYTHONOPTIMIZE')

from itertools import combinations, product


def run():
    joint_plus = {(0, 0), (1, 1)}
    joint_minus = {(0, 1), (1, 0)}

    def marginals(joint):
        return ({o for o, c in joint}, {c for o, c in joint})

    def terminal(joint, policy):
        return {int(c == policy[o]) for o, c in joint}

    assert marginals(joint_plus) == marginals(joint_minus)
    for u in (0, 1):
        assert terminal(joint_plus, (u, u)) == terminal(joint_minus, (u, u)) == {0, 1}
    assert terminal(joint_plus, (0, 1)) == {1}
    assert terminal(joint_minus, (0, 1)) == {0}

    universe = list(product((0, 1), repeat=2))
    tables = [set(rows) for k in range(5) for rows in combinations(universe, k)]
    witnesses = [
        (left, right) for left in tables for right in tables
        if marginals(left) == marginals(right)
        and all(terminal(left, (u, u)) == terminal(right, (u, u)) for u in (0, 1))
        and any(terminal(left, policy) != terminal(right, policy)
                for policy in product((0, 1), repeat=2))
    ]
    assert len(tables) == 16 and len(witnesses) == 22
    assert min(len(left) for left, right in witnesses) == 2
    assert min(len(right) for left, right in witnesses) == 2
    assert all(len(marginals(left)[0]) == len(marginals(left)[1]) == 2
               for left, right in witnesses)

    carrier = (0, 1, 2)
    quotient = (0, 0, 1)
    pairs = list(product(carrier, repeat=2))
    domains = [set(), set(product((0, 1), repeat=2)), {(0, 0)}]
    checked = 0
    for domain in domains:
        for outputs in product(carrier, repeat=len(domain)):
            operation = dict(zip(sorted(domain), outputs))
            def qpair(pair):
                return quotient[pair[0]], quotient[pair[1]]
            saturated = all(
                (left in domain) == (right in domain)
                for left in pairs for right in pairs if qpair(left) == qpair(right)
            )
            constant = all(
                quotient[operation[left]] == quotient[operation[right]]
                for left in domain for right in domain if qpair(left) == qpair(right)
            )
            projected_domain = {qpair(pair) for pair in domain}
            pullback = {pair for pair in pairs if qpair(pair) in projected_domain}
            factor = pullback == domain and all(
                len({quotient[operation[pair]] for pair in domain if qpair(pair) == target}) == 1
                for target in projected_domain
            )
            assert factor == (saturated and constant)
            checked += 1
    print(f"CPC4 PASS (16 tables, 22 ordered witnesses; minimum 2 branches); "
          f"CPC5 finite truth-table controls PASS ({checked})")


if __name__ == "__main__":
    run()
