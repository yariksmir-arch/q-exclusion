"""Independent finite checks for DCS3/DCS5 and their domain/composition boundary."""
from itertools import product


def equivalence(labels):
    return {(x, y) for x in range(len(labels)) for y in range(len(labels))
            if labels[x] == labels[y]}


def word_kernel(labels, controls):
    n = len(labels)
    words = [tuple(range(n))]
    seen = set(words)
    for w in words:
        for u in controls:
            z = tuple(None if x is None else u[x] for x in w)
            if z not in seen:
                seen.add(z)
                words.append(z)
    return {(x, y) for x in range(n) for y in range(n)
            if all((None if w[x] is None else labels[w[x]]) ==
                   (None if w[y] is None else labels[w[y]]) for w in words)}


def congruence(r, controls):
    return all((u[x] is None) == (u[y] is None)
               and (u[x] is None or (u[x], u[y]) in r)
               for x, y in r for u in controls)


def policy_trace(labels, controls, x, table):
    hist = (labels[x],)
    actions = ()
    for _ in range(2):
        a = table[hist]
        actions += (a,)
        x = controls[a][x]
        if x is None:
            return actions, hist, 'failure'
        hist += (labels[x],)
    return actions, hist, 'leaf'


def main():
    # Enumerate all 3-point partial unary maps and all 3-point equivalences.
    partitions = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (0, 1, 2)]
    checked = 0
    for u in product((None, 0, 1, 2), repeat=3):
        for labels in partitions:
            alpha = word_kernel(labels, (u,))
            assert alpha <= equivalence(labels)
            assert congruence(alpha, (u,))
            for finer in partitions:
                beta = equivalence(finer)
                if beta <= equivalence(labels) and congruence(beta, (u,)):
                    assert beta <= alpha
            checked += 1

    # Distinct representative copies stay equivalent under all finite words;
    # enumerate every depth-two binary-observation feedback decision table.
    labels = (0, 0, 1, 1)
    controls = ((2, 3, 0, 1), (None, None, 2, 3))
    alpha = word_kernel(labels, controls)
    histories = [(0,), (1,), (0, 0), (0, 1), (1, 0), (1, 1)]
    policies = 0
    for choices in product((0, 1), repeat=len(histories)):
        table = dict(zip(histories, choices))
        for x, y in alpha:
            assert policy_trace(labels, controls, x, table) == policy_trace(labels, controls, y, table)
        policies += 1

    # Missing success/failure distinctions and insufficient word depth.
    assert (0, 1) not in word_kernel((0, 0), ((0, None),))
    labels = (0, 0, 0, 1)
    u = (0, 2, 3, 3)
    assert labels[0] == labels[1] and labels[u[0]] == labels[u[1]]
    assert (0, 1) not in word_kernel(labels, (u,))

    # Unary control descent does not imply binary composition descent.
    labels = (0, 0, 1)
    alpha = word_kernel(labels, ((0, 1, 2),))
    f = lambda x, y: 2 if (x, y) == (1, 0) else 0
    assert (0, 1) in alpha and (f(0, 0), f(1, 0)) not in alpha
    # Unrestricted leaf output creates a new distinction at depth zero.
    alpha = word_kernel((0, 0), ((0, 1),))
    leaf = (0, 1)
    assert (0, 1) in alpha and leaf[0] != leaf[1]
    print(f'DCS PASS: {checked} partial-map/equivalence cases; {policies} feedback tables; 4 kill tests')


if __name__ == '__main__':
    main()
