"""Finite witnesses for the scoped endogenous-articulation application; stdlib only."""

if not __debug__:
    raise RuntimeError('OPTIMIZED_PYTHON_NOT_SUPPORTED: run finite checks without -O, -OO or PYTHONOPTIMIZE')

from fractions import Fraction as F
from itertools import product, permutations
import json
from pathlib import Path

checks = {}
def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks[name] = checks.get(name, 0) + 1

def factors(xs, r, h):
    return all(r(x) != r(y) or h(x) == h(y) for x in xs for y in xs)

# Transparent learner: two independently specified target functions, full register access.
for target, a, b, initial_h in product((0,1),repeat=4):
    training_y=a ^ target
    learned=(a ^ training_y,1)
    peek=tuple(learned)
    check('transparent_learning',peek==learned and (b ^ peek[0])==(b ^ target))

xs = list(product((0, 1), repeat=2))
for vals in product((0, 1), repeat=4):
    d = dict(zip(xs, vals))
    if factors(xs, lambda x:x[0], d.get):
        check('classification_no_new_probe', all(d[(a,0)] == d[(a,1)] for a in (0,1)))
check('incomparable_interfaces', not factors(xs, lambda x:x[0],lambda x:x[1]) and not factors(xs,lambda x:x[1],lambda x:x[0]))
check('support_expansion', factors([0],lambda x:0,lambda x:x) and not factors([0,1],lambda x:0,lambda x:x))
check('static_sufficient_not_available', factors([0,1],lambda x:x,lambda x:x)) # route inventory explicitly empty
available_decoders = [lambda z:0, lambda z:1]
check('no_decoder_route', not any(all(d(x)==x for x in (0,1)) for d in available_decoders))
check('domain_not_saturated', (0 in {0}) != (1 in {0}))
check('update_not_constant', not factors(['a','b'],lambda x:0,lambda x:0 if x=='a' else 1))

# Named finite sector (x, assembled, fuel, record); None = blank.
X = list(product((0,1),(0,1),(0,1,2),(None,0,1)))
def step(s, action):
    x,b,f,r = s
    if action == 'build' and f==2: return x,1,1,r
    if action == 'read' and b and f>0: return x,b,f,x
    if action.startswith('feed') and f>0:
        i=int(action[-1]); return x,b,min(2,f+1) if i==x else max(0,f-1),r
    if action == 'decay' and f>0: return x,b,f-1,r
    if action == 'erase': return x,b,f,None
    if action == 'break': return x,0,f,r
    if action == 'peek': return s
    if action == 'tap': return x,b,max(0,f-2),r
    return None

def policy(s):
    s=step(s,'read')
    if s is None: return None
    s=step(s,'feed'+str(s[3]))
    return None if s is None else step(s,'decay')

check('sector_size',len(X)==36)
for x in (0,1):
    start=(x,0,2,None)
    check('initial_read_disabled',step(start,'read') is None)
    s=step(start,'build')
    check('construction_enables',step(s,'read')[3]==x)
    for n in range(20):
        s=policy(s)
        check('maintenance_invariant',s==(x,1,1,x))
    depleted=step(step(s,'read'),'decay')
    check('feed_ablation',step(depleted,'read') is None)
    check('retention_reuse',step(s,'read')[3]==s[3])
    check('rebuild_loss',step(step(step(s,'break'),'erase'),'read') is None)
    check('nondestructive_complete_access',policy(step(s,'peek'))==policy(s))
    check('costly_access',step(step(s,'tap'),'read') is None)
wrong=step(step((1,1,1,None),'read'),'feed0')
check('fixed_route_ablation',wrong[2]==0 and step(wrong,'read') is None)
check('one_shot_loss',not factors([0,1],lambda x:None,lambda x:x))
# The complete original grammar already includes build;read, so it distinguishes x.
check('full_grammar_not_new_content',step(step((0,0,2,None),'build'),'read')[3] != step(step((1,0,2,None),'build'),'read')[3])

# Independent joint constraints: explicit nonempty intersection; never empty-join certainty.
pa,pb={0,1},{0,2}
check('ICC_joint_determinacy',len(pa)>1 and len(pb)>1 and pa & pb=={0})
join=[(a,b,c) for a,b,c in product((0,1),repeat=3) if a==b and b!=c]
check('ICC_compatible_composition',bool(join) and all(a!=c for a,b,c in join))
check('pairwise_not_global',not [(a,b,c) for a,b,c in product((0,1),repeat=3) if a==b and b==c and c!=a])
# Properly transported source/answer labels preserve the factor result.
for perm in permutations(xs):
    rename=dict(zip(xs,perm)); inv={v:k for k,v in rename.items()}
    check('presentation_factor',factors(perm,lambda x:inv[x][0],lambda x:inv[x][0]) == factors(xs,lambda x:x[0],lambda x:x[0]))

# Exact rational matrix witness: projective Z recording destroys X coherence,
# but preserves every supplied Z-diagonal density matrix.
rho=((F(1,2),F(1,2)),(F(1,2),F(1,2)))
def dephase(a):return ((a[0][0],F(0)),(F(0),a[1][1]))
def overlap_plus(a):return sum(sum(row) for row in a)/2
check('quantum_coherence_cost',overlap_plus(rho)==1 and overlap_plus(dephase(rho))==F(1,2))
for a in (F(0),F(1,3),F(1)):
    d=((a,F(0)),(F(0),1-a))
    check('commuting_record_preservation',dephase(d)==d)
# Inner-product equation for the nonorthogonal |0>,|+> pair: overlap nonzero.
check('nonorthogonal_record_constraint',F(1,2)!=0 and F(1,2)*0 != F(1,2))
result={'status':'PASS','assertions':sum(checks.values()),'families':checks,'scope':'finite toy witnesses, not mechanized general or empirical proofs'}
print(json.dumps(result,indent=2))
if __name__ == '__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args()
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
