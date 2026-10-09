#!/usr/bin/env python3
"""Exact symbolic verification for the UBT SU(3) spin--quadrupole bridge.

Checks finite-dimensional identities only. The accompanying research note contains
the analytic simplicity argument for the minimal left/right no-go.
"""

import sympy as sp

I = sp.I
sqrt3 = sp.sqrt(3)
ZERO3 = sp.zeros(3)

lam = [
    sp.Matrix([[0,1,0],[1,0,0],[0,0,0]]),
    sp.Matrix([[0,-I,0],[I,0,0],[0,0,0]]),
    sp.Matrix([[1,0,0],[0,-1,0],[0,0,0]]),
    sp.Matrix([[0,0,1],[0,0,0],[1,0,0]]),
    sp.Matrix([[0,0,-I],[0,0,0],[I,0,0]]),
    sp.Matrix([[0,0,0],[0,0,1],[0,1,0]]),
    sp.Matrix([[0,0,0],[0,0,-I],[0,I,0]]),
    (1/sqrt3)*sp.diag(1,1,-2),
]

adI = sp.Matrix([[0,0,0],[0,0,-2],[0,2,0]])
adJ = sp.Matrix([[0,0,2],[0,0,0],[-2,0,0]])
adK = sp.Matrix([[0,-2,0],[2,0,0],[0,0,0]])
S = [I*adI/2, I*adJ/2, I*adK/2]

assert S[0] == lam[6]
assert S[1] == -lam[4]
assert S[2] == lam[1]

for a in range(3):
    for b in range(3):
        lhs = sp.simplify(S[a]*S[b]-S[b]*S[a])
        rhs = sum((I*sp.LeviCivita(a,b,c)*S[c] for c in range(3)), sp.zeros(3))
        assert sp.simplify(lhs-rhs) == ZERO3

Id3 = sp.eye(3)
Q = {}
for a in range(3):
    for b in range(3):
        Q[a,b] = sp.simplify(
            (S[a]*S[b]+S[b]*S[a])/2
            - (sp.Rational(2,3) if a == b else 0)*Id3
        )

assert sp.simplify(Q[0,0]+Q[1,1]+Q[2,2]) == ZERO3
assert sp.simplify(-2*Q[0,1]-lam[0]) == ZERO3
assert sp.simplify(Q[1,1]-Q[0,0]-lam[2]) == ZERO3
assert sp.simplify(-2*Q[0,2]-lam[3]) == ZERO3
assert sp.simplify(-2*Q[1,2]-lam[5]) == ZERO3
assert sp.simplify(sqrt3*Q[2,2]-lam[7]) == ZERO3

basis8 = [
    S[0], S[1], S[2],
    Q[0,1], Q[0,2], Q[1,2],
    Q[1,1]-Q[0,0], Q[2,2],
]
vecs = [m.reshape(9,1) for m in basis8]
assert sp.Matrix.hstack(*vecs).rank() == 8

# Exact rank of the linear operator family X -> AX-XB on M_2(C).
E = []
for a in range(2):
    for b in range(2):
        m = sp.zeros(2)
        m[a,b] = 1
        E.append(m)

I2 = sp.eye(2)
superops = []
for A in E:
    superops.append(sp.kronecker_product(I2, A))
for B in E:
    superops.append(-sp.kronecker_product(B.T, I2))

rank_lr = sp.Matrix.hstack(*[M.reshape(16,1) for M in superops]).rank()
assert rank_lr == 7

print("PASS: exact SU(3) 3+5 identities and minimal left/right rank=7.")
