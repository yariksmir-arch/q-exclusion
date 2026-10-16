# Compositional Record Transport

## Scope

This finite specialised L2 module consumes declared generated pair supports,
descended records, and their induced factors. It changes neither the Phase-I
frozen core nor CP/CPG. It introduces no L1 probe, generator, probability, or
category. All statements are restricted to stated supports and record images.

## Typed transport datum

**DEF CRS-T0 (record-interface transport datum).** Let `S' subseteq E'_pair`
and `S subseteq E_pair` be declared generated supports. Let
`H:S'->S`, `r':S'->L'_pair`, `c':S'->L'_comp`, `r:S->L_pair`, and
`c:S->L_comp` be derived L2 maps; let `a:L'_pair->L_pair` and
`b:L'_comp->L_comp` be declared label transports. The datum is adequate when
`a o r'=r o H` and `b o c'=c o H` on `S'`. Maps need not be injective or
surjective. In a changing-carrier application, `H` must be supplied by
adequate transport of the pair support, protocol family, and partial
composition; a bare carrier comparison does not provide it.

## Derived factor transport

**THM CRS-T1 (derived factor transport on generated record image).** Assume
CRS-T0 and factors `c=kappa o r` on `S` and `c'=kappa' o r'` on `S'`, where
`kappa:im(r)->L_comp` and `kappa':im(r')->L'_comp`. Then
`a(im r') subseteq im r` and

`b o kappa' = kappa o a : im(r')->L_comp`.

*Proof.* For `ell'=r'(x)`, `a(ell')=r(Hx)`, so it lies in `im r`; and
`b(kappa'(ell'))=b(c'(x))=c(Hx)=kappa(r(Hx))=kappa(a(ell'))`. This is
independent of `x`. Equivalently, both maps factor the same map through the
surjection `r':S'->im(r')`, which yields uniqueness. No all-label-space
extension follows.

**COR CRS-T2 (specialized transport compression).** The `kappa` square is
redundant as an independent premise on `im(r')` when CRS-T1 holds. The support
map, pair-record square, composite-record square, and factor identities remain
independent interfaces. This does not remove PF8's distinct requirements for
generation, profiles, joint data, or clusters.

**PROP CRS-T3 (changing-carrier invariance).** Given an adequate complete raw
carrier interface which descends to CRS-T0 and transports the declared protocol
family supports, available pair-probe grammar, composite records, and refined
record factors, record sufficiency transports on generated images. Thus it is
presentation-invariant only relative to that complete interface; a raw-carrier
bijection, quotient isomorphism, or chosen section is insufficient.

## Refinement and predictive boundary

**PROP CRS-T4.** For a declared process map `rho_E:E'_P->E_P` with induced
support map, coarse factorization does not imply fine factorization: the fine
condition remains `ker(r'|S') subseteq ker(c'|S')`. Conversely, a fine factor
coarsens only under an explicit record transport satisfying the corresponding
kernel condition. Process refinement, pair-probe repertoire refinement, and
generated-support expansion are distinct axes.

**COR CRS-T5.** CPG8/PF1 give the image of pair-cluster content only in the
certified scheme/family and transport scope of the record factor. No stochastic
kernel, conditional probability, Markov condition, linear operator, or
enriched category follows.

## Finite controls

**CM CRS-CM9 (positive derived transport).** Take `S'={x',y'}`, `S={x,y}`
and `H(x')=x,H(y')=y`; records `r'(x')=u,r'(y')=v,r(x)=p,r(y)=q` and
`c'(x')=0,c'(y')=1,c(x)=A,c(y)=B`; label maps `a(u)=p,a(v)=q` and
`b(0)=A,b(1)=B`. With the evident factors, both underlying record squares
hold, hence so does the factor square without postulating it. Wrapping every
raw realization in a finite tag gives a nontrivially different raw carrier;
the tags and any section are surplus.

**CM CRS-CM10 (missing composite-record transport).** Retain the pair data of
CRS-CM9 but set `c(H(y'))=A` while `b(c'(y'))=B`. Process and pair-record
transport may still hold, yet the composite-record square and factor transport
fail. Process transport or pair-record transport alone is therefore insufficient.

**CM CRS-CM11 (many-to-one boundary).** Let `r'(x')=u,r'(y')=v`,
`a(u)=a(v)=p`, and `r(Hx')=r(Hy')=p`; set `c'(x')=0,c'(y')=1` and take `b`
identity. A coarse factor forces `c(Hx')=c(Hy')=kappa(p)`, while
composite-record transport would require `0=kappa(p)=1`. Hence non-injective
`a` does not defeat CRS-T1: if fine values disagree after `b`, either the
composite-record square or coarse factor identity is missing.

**CM CRS-CM12 (support expansion).** Let `S={x}` with `r(x)=p,c(x)=0`; expand
to `S'={x,y,z}` with `r(y)=r(z)=q,c(y)=0,c(z)=1`, retaining the same partial
composition. The factor remains correct on `S` but fails on `S'`; no process
quotient need change.

## Audits

Q-audit: conditional PASS. Factors are induced only on actual record images;
no representative, global extension, hidden coupling, probability, time, or
outcome-shaped pair probe is selected. Presentation audit: conditional PASS
only under CRS-T0/CRS-T3, including support/protocol family and available-probe
grammar. Labels alone have no invariant role. Dependency:
`CP1 -> CPG3/CPG5 -> record factor -> CRS-T1 -> CPG8/PF1`. No frozen result
changes.
