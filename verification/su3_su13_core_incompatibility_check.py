#!/usr/bin/env python3
"""Exact checks for the SU(1,3) pairing and sharp/determinant obstruction."""
import sympy as sp

I=sp.I
G=sp.diag(1,-1,-1,-1)

# su(1,3) basis: 8 lower-right su3 + 6 off-diagonal + 1 diagonal.
sqrt3=sp.sqrt(3)
lam=[
sp.Matrix([[0,1,0],[1,0,0],[0,0,0]]),
sp.Matrix([[0,-I,0],[I,0,0],[0,0,0]]),
sp.Matrix([[1,0,0],[0,-1,0],[0,0,0]]),
sp.Matrix([[0,0,1],[0,0,0],[1,0,0]]),
sp.Matrix([[0,0,-I],[0,0,0],[I,0,0]]),
sp.Matrix([[0,0,0],[0,0,1],[0,1,0]]),
sp.Matrix([[0,0,0],[0,0,-I],[0,I,0]]),
sp.Matrix([[1,0,0],[0,1,0],[0,0,-2]])/sqrt3,
]
gens=[]
for L in lam:
    X=sp.zeros(4)
    X[1:4,1:4]=I*L
    gens.append(X)
for j in range(1,4):
    X=sp.zeros(4); X[0,j]=1; X[j,0]=1; gens.append(X)
    Y=sp.zeros(4); Y[0,j]=I; Y[j,0]=-I; gens.append(Y)
gens.append(sp.diag(3*I,-I,-I,-I))

# General Hermitian K with 16 real parameters.
r=sp.symbols("r0:16", real=True)
K=sp.zeros(4)
idx=0
for a in range(4):
    K[a,a]=r[idx]; idx+=1
for a in range(4):
    for b in range(a+1,4):
        K[a,b]=r[idx]+I*r[idx+1]
        K[b,a]=r[idx]-I*r[idx+1]
        idx+=2
assert idx==16

eq=[]
for X in gens:
    M=sp.expand(X.H*K+K*X)
    for z in M:
        eq.extend([sp.re(z),sp.im(z)])
A,_=sp.linear_eq_to_matrix(eq,r)
null=A.nullspace()
assert len(null)==1
K0=K.subs(dict(zip(r,null[0])))
# Proportional to G.
scale=sp.simplify(K0[0,0])
assert sp.simplify(K0-scale*G)==sp.zeros(4)

# Explicit SU(1,3) element preserving G but changing biquaternion determinant.
L=sp.Matrix([
[sp.sqrt(2),1,0,0],
[1,sp.sqrt(2),0,0],
[0,0,1,0],
[0,0,0,1]
])
assert sp.simplify(L.H*G*L-G)==sp.zeros(4)
assert sp.simplify(L.det()-1)==0
q=sp.Matrix([1,0,0,0])
qp=L*q
assert sp.simplify((q.H*G*q)[0]-(qp.H*G*qp)[0])==0

def det_biquat(v):
    z0,z1,z2,z3=v
    X=sp.Matrix([[z0+I*z1,z2+I*z3],[-z2+I*z3,z0-I*z1]])
    return sp.simplify(X.det())

assert det_biquat(q)==1
assert det_biquat(qp)==3

print("PASS: the only constant SU(1,3)-invariant Hermitian pairing is indefinite G, and SU(1,3) does not preserve the biquaternion sharp/determinant structure")
