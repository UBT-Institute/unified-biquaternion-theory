#!/usr/bin/env python3
"""Exact rank-five Gell-Mann Higgs pattern for Sigma=I symmetric spurion."""
import sympy as sp

I=sp.I
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
T=[L/2 for L in lam]

norms=[]
for A in T:
    B=I*A
    M=sp.simplify(B+B.T)
    norms.append(sp.simplify(sp.trace(M.H*M)))

assert [i+1 for i,n in enumerate(norms) if n==0]==[2,5,7]
nonzero=[n for n in norms if n!=0]
assert len(nonzero)==5
assert all(sp.simplify(n-nonzero[0])==0 for n in nonzero)
assert sp.simplify(nonzero[0]-2)==0

print("PASS: Sigma=I leaves lambda_2,lambda_5,lambda_7 massless and gives equal nonzero norm to the five symmetric Gell-Mann directions")
