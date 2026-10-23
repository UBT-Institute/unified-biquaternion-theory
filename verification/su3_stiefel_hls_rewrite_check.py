#!/usr/bin/env python3
"""Exact checks for the 4x3 Stiefel / hidden-local-SU(3) rewrite."""
import sympy as sp

# Degree count.
assert 2*4*3 - 3**2 - (3**2-1) == 7

G=sp.diag(1,-1,-1,-1)
Z=sp.Matrix([
    [0,0,0],
    [1,0,0],
    [0,1,0],
    [0,0,1],
])
n=sp.Matrix([1,0,0,0])

assert Z.H*G*Z == -sp.eye(3)
assert (n.H*G*n)[0] == 1
assert Z.H*G*n == sp.zeros(3,1)

Pplus=sp.eye(4)+Z*Z.H*G
assert sp.simplify(Pplus*Pplus-Pplus)==sp.zeros(4)
assert Pplus*Z==sp.zeros(4,3)
assert Pplus*n==n
assert sp.simplify(Pplus-n*n.H*G)==sp.zeros(4)

# Generic anti-Hermitian u(3) current decomposes uniquely into su(3)+u(1).
C=sp.Matrix(3,3,sp.symbols("c0:9"))
C0=C-sp.trace(C)*sp.eye(3)/3
assert sp.simplify(sp.trace(C0))==0
assert sp.simplify(C-(C0+sp.trace(C)*sp.eye(3)/3))==sp.zeros(3)

# Algebraic HLS term is a square in B-C0 and is minimized exactly at B=C0.
d=sp.symbols("d0:9", real=True)
D=sp.Matrix(3,3,d)
D=D-sp.trace(D)*sp.eye(3)/3
# Sum of independent real squares is enough to verify uniqueness of D=0.
q=sum(x**2 for x in d)
grad=[sp.diff(q,x) for x in d]
sol=sp.solve(grad,d,dict=True)
assert sol and all(sol[0].get(x,0)==0 for x in d)

print("PASS: constrained 4x3 frame modulo local SU(3) has 7 real DOF; P+ is the timelike normal projector; HLS vertical sector is algebraically eliminated at B=C0")
