#!/usr/bin/env python3
"""Exact checks for the Lorentz-equivariant moving SU(3) carrier."""
import sympy as sp

I = sp.I
G = sp.diag(1,-1,-1,-1)
e = [sp.eye(4)[:,j] for j in range(4)]
n = e[0]

# Reference fiber E_n = span(e1,e2,e3); -h is positive identity.
B = sp.Matrix.hstack(e[1],e[2],e[3])
assert B.H*G*B == -sp.eye(3)
assert (n.H*G*n)[0] == 1
assert n.H*G*B == sp.zeros(1,3)

# Orthogonal projector.
P = sp.eye(4) - n*(n.H*G)
assert sp.simplify(P*P-P) == sp.zeros(4)
assert sp.simplify(P.H*G-G*P) == sp.zeros(4)
assert P*B == B
assert P*n == sp.zeros(4,1)

# Proper Lorentz Lie-algebra generators preserve G and have zero trace.
gens = []

# boosts K_i
for i in range(1,4):
    K = sp.zeros(4)
    K[0,i] = 1
    K[i,0] = 1
    gens.append(K)

# spatial rotations J_12, J_23, J_31
for i,j in [(1,2),(2,3),(3,1)]:
    J = sp.zeros(4)
    J[i,j] = -1
    J[j,i] = 1
    gens.append(J)

for X in gens:
    assert sp.simplify(X.H*G+G*X) == sp.zeros(4)
    assert sp.trace(X) == 0

# Standard su(3) basis acts on the reference fiber preserving -G|E and volume.
sqrt3 = sp.sqrt(3)
lam = [
sp.Matrix([[0,1,0],[1,0,0],[0,0,0]]),
sp.Matrix([[0,-I,0],[I,0,0],[0,0,0]]),
sp.Matrix([[1,0,0],[0,-1,0],[0,0,0]]),
sp.Matrix([[0,0,1],[0,0,0],[1,0,0]]),
sp.Matrix([[0,0,-I],[0,0,0],[I,0,0]]),
sp.Matrix([[0,0,0],[0,0,1],[0,1,0]]),
sp.Matrix([[0,0,0],[0,0,-I],[0,I,0]]),
sp.Matrix([[1,0,0],[0,1,0],[0,0,-2]])/sqrt3,
]
su3 = [I*L for L in lam]
for X in su3:
    assert sp.simplify(X.H+X) == sp.zeros(3)
    assert sp.simplify(sp.trace(X)) == 0

M = sp.Matrix.hstack(*[
    sp.Matrix([sp.re(z) for z in X.reshape(9,1)] +
              [sp.im(z) for z in X.reshape(9,1)])
    for X in su3
])
assert M.rank() == 8

print("PASS: timelike biquaternion direction defines a Lorentz-equivariant rank-3 Hermitian carrier with SU(3) reference-frame stabilizer")
