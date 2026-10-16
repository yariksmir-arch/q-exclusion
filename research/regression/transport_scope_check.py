"""Finite transport, noncanonical-section and signature countermodels; stdlib only."""
from itertools import permutations, product


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def partitions(n):
    found = set()
    for labels in product(range(n), repeat=n):
        names = {}
        canonical = tuple(names.setdefault(x, len(names)) for x in labels)
        found.add(canonical)
    return sorted(found)


def refines(fine, coarse):
    return all(fine[x] != fine[y] or coarse[x] == coarse[y]
               for x in range(len(fine)) for y in range(len(fine)))


def main():
    cases = 0
    # Every small refinement chain and every common carrier relabelling.
    # Quotient classes are represented as sets, without selecting representatives.
    for n in range(1, 5):
        for coarse in partitions(n):
            for fine in partitions(n):
                if not refines(fine, coarse):
                    continue
                coarse_cells = {frozenset(i for i in range(n) if coarse[i] == c)
                                for c in coarse}
                fine_cells = {frozenset(i for i in range(n) if fine[i] == c)
                              for c in fine}
                for t in permutations(range(n)):
                    image = lambda cell: frozenset(t[i] for i in cell)
                    target_coarse = {image(cell) for cell in coarse_cells}
                    for cell in fine_cells:
                        containing = [c for c in coarse_cells if cell <= c]
                        target_containing = [c for c in target_coarse if image(cell) <= c]
                        require(len(containing) == len(target_containing) == 1,
                                'refinement must have a unique coarse class')
                        require(image(containing[0]) == target_containing[0],
                                'common carrier transport must commute with refinement')
                    cases += 1

    # CM PI4: coarse context c(x)=x; fine adds d(x)=x. Context maps
    # are identities and restrict, but carrier/readout maps need not agree.
    xs = (0, 1)
    contexts = {'c': lambda x: x, 'd': lambda x: x}
    coarse_t, fine_t = lambda x: x, lambda x: 1 - x
    coarse_ell, fine_ell = lambda x: x, lambda x: 1 - x
    require(all(contexts['c'](coarse_t(x)) == coarse_ell(contexts['c'](x))
                for x in xs), 'coarse adequate square')
    require(all(contexts[c](fine_t(x)) == fine_ell(contexts[c](x))
                for c in contexts for x in xs), 'fine adequate squares')
    require({'c': 'c'} == {k: v for k, v in {'c': 'c', 'd': 'd'}.items()
                                  if k == 'c'}, 'context-only restriction holds')
    require(coarse_t(0) != fine_t(0), 'old PI6 does not imply T1.3 square')

    # CM PI1: a section exists; no section is invariant under the swap.
    q = lambda x: '*'
    for chosen in xs:
        section = lambda cell: chosen
        require(q(section('*')) == '*', 'noncanonical section exists')
        require(fine_t(section('*')) != section('*'), 'section is not swap-natural')

    # CM PI3: total identity descends, but a domain {0} is not saturated
    # for the constant observation. Only c is in the declared test grammar.
    observation = lambda x: '*'
    identity = lambda x: x
    require(all(observation(identity(x)) == observation(identity(y))
                for x in xs for y in xs), 'total identity descends')
    domain = {0}
    require(any(observation(x) == observation(y) and ((x in domain) != (y in domain))
                for x in xs for y in xs), 'partial-domain countermodel fails descent')

    # PI7: the same base presentation gives no comparison of extensions.
    def factors(values):
        return len(set(values)) <= 1
    require(not factors((0, 1)) and factors((0,)),
            'PI2 without PI4 cannot transport Q-status')
    print(f'TRANSPORT_SCOPE_PASS ({cases} refinement/relabelling diagrams; '
          'context-only compatibility, sections, domains and extension-fibre controls)')


if __name__ == '__main__':
    main()
