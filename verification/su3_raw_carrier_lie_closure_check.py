#!/usr/bin/env python3
"""Exact Lie closure of lower-right su(3) plus three minimal bimodule boosts."""
import sympy as sp

I=sp.I
G=sp.diag(1,-1,-1,-1)
sqrt3=sp.sqrt(3)

def qmul(a,b):
    a0,a1,a2,a3=a
    b0,b1,b2,b3=b
    return sp.Matrix([
        a0*b0-a1*b1-a2*b2-a3*b3,
        a0*b1+a1*b0+a2*b3-a3*b2,
        a0*b2-a1*b3+a2*b0+a3*b1,
        a0*b3+a1*b2-a2*b1+a3*b0
    ])

basis=[
sp.Matrix([1,0,0,0]),
sp.Matrix([0,1,0,0]),
sp.Matrix([0,0,1,0]),
sp.Matrix([0,0,0,1])
]

L=[]
R=[]
for e in basis:
    L.append(sp.Matrix.hstack(*[qmul(e,b) for b in basis]))
    R.append(sp.Matrix.hstack(*[qmul(b,e) for b in basis]))

K=[sp.simplify(I*(L[j]+R[j])/2) for j in range(1,4)]

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

su3=[]
for M3 in lam:
    X=sp.zeros(4)
    X[1:4,1:4]=I*M3
    su3.append(X)

def realvec(M):
    z=list(M.reshape(16,1))
    return sp.Matrix([sp.re(x) for x in z]+[sp.im(x) for x in z])

def rank(mats):
    if not mats:
        return 0
    return sp.Matrix.hstack(*[realvec(M) for M in mats]).rank()

initial=su3+K
assert rank(initial)==11

for X in initial:
    assert sp.simplify(X.H*G+G*X)==sp.zeros(4)
    assert sp.trace(X)==0

closure=[]
def add(M):
    M=sp.simplify(M)
    if M==sp.zeros(4):
        return False
    r0=rank(closure)
    r1=rank(closure+[M])
    if r1>r0:
        closure.append(M)
        return True
    return False

for X in initial:
    add(X)

ranks=[rank(closure)]
changed=True
while changed:
    changed=False
    current=list(closure)
    for i in range(len(current)):
        for j in range(i+1,len(current)):
            C=sp.simplify(current[i]*current[j]-current[j]*current[i])
            if add(C):
                changed=True
    ranks.append(rank(closure))

assert ranks[0]==11
assert 14 in ranks
assert rank(closure)==15
assert len(closure)==15

for X in closure:
    assert sp.simplify(X.H*G+G*X)==sp.zeros(4)
    assert sp.trace(X)==0

print("PASS: Lie closure of raw-carrier su(3) plus the three minimal boost directions is all su(1,3), real dimension 15")
