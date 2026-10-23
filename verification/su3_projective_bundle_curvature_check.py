#!/usr/bin/env python3
"""Exact local curvature-span check for the projective-biquaternion SU(3) seed."""
import sympy as sp

I=sp.I
eye=sp.eye(3)
e=[sp.Matrix([1,0,0]),sp.Matrix([0,1,0]),sp.Matrix([0,0,1])]

def curv(a,b):
    F=a*b.H-b*a.H
    return sp.simplify(F-sp.trace(F)*eye/3)

# Eight explicit real tangent-plane curvature directions.
pairs=[
    (e[0],e[1]),
    (e[0],I*e[1]),
    (e[0],e[2]),
    (e[0],I*e[2]),
    (e[1],e[2]),
    (e[1],I*e[2]),
    (e[0],I*e[0]),
    (e[1],I*e[1]),
]
Fs=[curv(a,b) for a,b in pairs]

for F in Fs:
    assert sp.simplify(F.H+F)==sp.zeros(3)
    assert sp.simplify(sp.trace(F))==0

# Real-linear rank: flatten real and imaginary parts.
cols=[]
for F in Fs:
    v=list(F)
    cols.append(sp.Matrix([sp.re(x) for x in v]+[sp.im(x) for x in v]))
M=sp.Matrix.hstack(*cols)
assert M.rank()==8

# Check generated span equals standard anti-Hermitian Gell-Mann span.
sqrt3=sp.sqrt(3)
lams=[
sp.Matrix([[0,1,0],[1,0,0],[0,0,0]]),
sp.Matrix([[0,-I,0],[I,0,0],[0,0,0]]),
sp.Matrix([[1,0,0],[0,-1,0],[0,0,0]]),
sp.Matrix([[0,0,1],[0,0,0],[1,0,0]]),
sp.Matrix([[0,0,-I],[0,0,0],[I,0,0]]),
sp.Matrix([[0,0,0],[0,0,1],[0,1,0]]),
sp.Matrix([[0,0,0],[0,0,-I],[0,I,0]]),
sp.Matrix([[1,0,0],[0,1,0],[0,0,-2]])/sqrt3,
]
target=[I*L for L in lams]
allcols=[]
for F in Fs+target:
    v=list(F)
    allcols.append(sp.Matrix([sp.re(x) for x in v]+[sp.im(x) for x in v]))
assert sp.Matrix.hstack(*allcols).rank()==8

print("PASS: projective-biquaternion curvature is su(3)-valued and spans all 8 local directions")
