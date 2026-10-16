"""Exact finite diagnostics for corrected IL5/IL6; no physical validation."""
from itertools import permutations

checks = 0
def check(value):
    global checks
    assert value
    checks += 1

def lower(family, a, b):
    return [c for c in family if c <= a and c <= b]

def upper(family, a, b):
    return [c for c in family if a <= c and b <= c]

def greatest(elements):
    return [c for c in elements if all(d <= c for d in elements)]

def least(elements):
    return [c for c in elements if all(c <= d for d in elements)]

def descends(domain, values, q):
    raw = tuple(q)
    pairs = [(a, b) for a in raw for b in raw]
    for a, b in pairs:
        for c, d in pairs:
            if (q[a], q[b]) == (q[c], q[d]):
                if ((a, b) in domain) != ((c, d) in domain):
                    return False
                if (a, b) in domain and q[values[a, b]] != q[values[c, d]]:
                    return False
    return True

def main():
    universe = frozenset(range(3))
    subsets = [frozenset(i for i in universe if bits & (1 << i)) for bits in range(8)]
    pairs = 0
    for bits in range(1, 256):
        family = frozenset(subsets[i] for i in range(8) if bits & (1 << i))
        for a in family:
            for b in family:
                pairs += 1
                meets, joins = greatest(lower(family, a, b)), least(upper(family, a, b))
                check(len(meets) <= 1 and len(joins) <= 1)
                # Exact representation iff an output with the stipulated extent exists.
                check((a & b in family) == any(c == a & b for c in family))
                check((a | b in family) == any(c == a | b for c in family))
                check(a & b not in family or meets == [a & b])
                check(a | b not in family or joins == [a | b])
                for perm in permutations(range(3)):
                    rename = lambda s: frozenset(perm[i] for i in s)
                    renamed = frozenset(rename(s) for s in family)
                    check(set(greatest(lower(renamed, rename(a), rename(b)))) == set(map(rename, meets)))
                    check(set(least(upper(renamed, rename(a), rename(b)))) == set(map(rename, joins)))
                    check((a & b in family) == (rename(a) & rename(b) in renamed))
                    check((a | b in family) == (rename(a) | rename(b) in renamed))
    a, b, c = map(lambda i: frozenset([i]), range(3))
    f = frozenset([frozenset(), a | b, b | c])
    check(greatest(lower(f, a | b, b | c)) == [frozenset()] and b not in f)
    g = frozenset([a, b, universe])
    check(least(upper(g, a, b)) == [universe] and a | b not in g)
    check(greatest(lower(frozenset([a, b]), a, b)) == [])
    check(least(upper(frozenset([a, b]), a, b)) == [])
    # Relative lattice without exact union closure: diamond in supplied extent family.
    lattice = frozenset([frozenset(), a, b, universe])
    check(all(greatest(lower(lattice, x, y)) and least(upper(lattice, x, y))
              for x in lattice for y in lattice))
    check(a | b not in lattice)
    # Raw procedure with two equal-extent but empirically distinct outputs.
    q = {'r0': 'R', 'r1': 'R', 's': 'S', 'u': 'U', 'v': 'V'}
    domain = {('r0', 's'), ('r1', 's')}
    good = {('r0', 's'): 'u', ('r1', 's'): 'u'}
    bad = {('r0', 's'): 'u', ('r1', 's'): 'v'}
    ext = {'R': a | b, 'S': b | c, 'U': b, 'V': b}
    check(all(ext[q[bad[p]]] == ext[q[p[0]]] & ext[q[p[1]]] for p in domain))
    check(not descends(domain, bad, q))
    check(descends(domain, good, q))
    check(not descends({('r0', 's')}, {('r0', 's'): 'u'}, q))
    # Descending operation can have the wrong extent equation.
    wrong = {p: 's' for p in domain}
    check(descends(domain, wrong, q))
    check(not all(ext[q[wrong[p]]] == ext[q[p[0]]] & ext[q[p[1]]] for p in domain))
    print(f'INCIDENCE_BOUNDS_PASS {checks} assertions; 255 families; {pairs} ordered pairs; 6 renamings')

if __name__ == '__main__':
    main()
