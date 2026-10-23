#!/usr/bin/env python3
"""Exact Lie-algebra checks for SU(1,3)/SU(3) collective Theta rewrite."""
import sympy as sp

I=sp.I
G=sp.diag(1,-1,-1,-1)
e0=sp.Matrix([1,0,0,0])

# Eight su(3) stabilizer generators embedded in lower-right block.
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
stab=[]
for L in lam:
    X=sp.zeros(4)
    X[1:4,1:4]=I*L
    stab.append(X)

# Seven coset directions: six complex boosts + one relative phase.
coset=[]
for j in range(1,4):
    X=sp.zeros(4)
    X[0,j]=1
    X[j,0]=1
    coset.append(X)

    Y=sp.zeros(4)
    Y[0,j]=I
    Y[j,0]=-I
    coset.append(Y)

H=sp.diag(3*I,-I,-I,-I)
coset.append(H)

gens=stab+coset
assert len(gens)==15

for X in gens:
    assert sp.simplify(X.H*G+G*X)==sp.zeros(4)
    assert sp.simplify(sp.trace(X))==0

# Stabilizer kills e0; coset orbit spans the seven-real-dimensional tangent.
for X in stab:
    assert X*e0==sp.zeros(4,1)

cols=[]
for X in gens:
    y=X*e0
    cols.append(sp.Matrix([sp.re(z) for z in y]+[sp.im(z) for z in y]))
orbit=sp.Matrix.hstack(*cols)
assert orbit.rank()==7

# Stabilizer basis has real rank 8.
scols=[]
for X in stab:
    v=X.reshape(16,1)
    scols.append(sp.Matrix([sp.re(z) for z in v]+[sp.im(z) for z in v]))
assert sp.Matrix.hstack(*scols).rank()==8

print("PASS: su(1,3) orbit of a unit timelike vector has rank 7 with su(3) stabilizer rank 8")
