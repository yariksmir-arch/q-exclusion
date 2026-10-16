"""Finite witnesses for BCS1--BCS6. No external dependencies."""

if not __debug__:
    raise RuntimeError('OPTIMIZED_PYTHON_NOT_SUPPORTED: run finite checks without -O, -OO or PYTHONOPTIMIZE')

from itertools import product


def bisim(obs, trans):
    relation = {(x, y) for x in obs for y in obs if obs[x] == obs[y]}
    actions = {a for x, a in trans}
    while True:
        updated = {
            (x, y) for x, y in relation
            if all(
                ((x, a) in trans) == ((y, a) in trans)
                and all(any((s, t) in relation for t in trans.get((y, a), ()))
                    for s in trans.get((x, a), ()))
                and all(any((s, t) in relation for s in trans.get((x, a), ()))
                        for t in trans.get((y, a), ()))
                for a in actions)
        }
        if updated == relation:
            return relation
        relation = updated


def traces(obs, trans, root, word):
    frontier = {(root, (obs[root],))}
    for action in word:
        frontier = {(n, history + (obs[n],)) for s, history in frontier
                    for n in trans.get((s, action), ())}
    return {history for _, history in frontier}


def policies(obs, trans, root, choose, depth):
    frontier = {(root, (obs[root],), ())}
    for _ in range(depth):
        frontier = {(n, history + (obs[n],), word + (choose(history),))
                    for s, history, word in frontier
                    for n in trans.get((s, choose(history)), ())}
    return {(word, history) for _, history, word in frontier}


def main():
    # Depth-two typed grammar: u then a or b. Eight nodes, not a minimality claim.
    obs = {'x': 'root', 'y': 'root', 'x0': 0, 'y0': 0,
           'x1': 1, 'y1': 1, 'zero': 0, 'one': 1}
    t = {('x', 'u'): {'x0', 'x1'}, ('y', 'u'): {'y0', 'y1'}}
    for side, flip in [('x', False), ('y', True)]:
        for bit, action in product(range(2), ['a', 'b']):
            success = ((bit == 0) == (action == 'a')) != flip
            t[(side + str(bit), action)] = {'one' if success else 'zero'}
    for word in [(), ('u',), ('u', 'a'), ('u', 'b')]:
        assert {h[-1] for h in traces(obs, t, 'x', word)} == {
            h[-1] for h in traces(obs, t, 'y', word)}
    choose = lambda h: 'u' if len(h) == 1 else ('a' if h[-1] == 0 else 'b')
    px, py = [policies(obs, t, s, choose, 2) for s in ['x', 'y']]
    assert {h[-1] for _, h in px} == {1}
    assert {h[-1] for _, h in py} == {0}
    assert traces(obs, t, 'x', ('u', 'a')) != traces(obs, t, 'y', ('u', 'a'))
    assert ('x', 'y') not in bisim(obs, t)
    for root in ['x', 'y']:
        filtered = {(w, h) for w in [('u', 'a'), ('u', 'b')]
                    for h in traces(obs, t, root, w)
                    if all(w[i] == choose(h[:i + 1]) for i in range(2))}
        assert filtered == policies(obs, t, root, choose, 2)

    # Full finite trace/policy equality does not imply bisimulation.
    obs2 = {'p': 'root', 'q': 'root', 'r': 'mid', 's': 'mid',
            'v': 'mid', 'zero': 0, 'one': 1}
    t2 = {('p', 'u'): {'r', 's'}, ('q', 'u'): {'v'}}
    for a in ['a', 'b']:
        t2[('r', a)] = {'zero'}
        t2[('s', a)] = {'one'}
        t2[('v', a)] = {'zero', 'one'}
    for word in [(), ('u',), ('u', 'a'), ('u', 'b')]:
        assert traces(obs2, t2, 'p', word) == traces(obs2, t2, 'q', word)
    for action in ['a', 'b']:
        choose2 = lambda h: 'u' if len(h) == 1 else action
        assert policies(obs2, t2, 'p', choose2, 2) == policies(obs2, t2, 'q', choose2, 2)
    assert ('p', 'q') not in bisim(obs2, t2)

    # A new separately declared composition need not respect branching equivalence.
    obs3 = {'x': 0, 'y': 0, 'z': 1}
    relation = bisim(obs3, {})
    compose = lambda a, b: 'z' if (a, b) == ('y', 'x') else 'x'
    assert ('x', 'y') in relation
    assert (compose('x', 'x'), compose('y', 'x')) not in relation
    # Defined empty output is not undefined input.
    assert ('a', 'b') not in bisim({'a': 0, 'b': 0}, {('a', 'u'): set()})
    print('PASS: terminal-vs-feedback separation, trace filtering, nonnecessity, composition failure, domain saturation')


if __name__ == '__main__':
    main()
