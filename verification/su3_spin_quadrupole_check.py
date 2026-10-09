#!/usr/bin/env python3
"""Exact verification of the UBT SU(3) spin–quadrupole decomposition."""
import sympy as sp

I = sp.I
sqrt3 = sp.sqrt(3)

l1 = sp.Matrix([[0,1,0],[1,0,0],[0,0,0]])
l2 = sp.Matrix([[0,-I,0],[I,0,0],[0,0,0]])
l3 = sp.Matrix([[1,0,0],[0,-1,0],[0,0,0]])
l4 = sp.Matrix([[0,0,1],[0,0,0],[1,0,0]])
l5 = sp.Matrix([[0,0,-I],[0,0,0],[I,0,0]])
l6 = sp.Matrix([[0,0,0],[0,0,1],[0,1,0]])
l7 = sp.Matrix([[0,0,0],[0,0,-I],[0,I,0]])
l8 = (1/sqrt3)*sp.Matrix([[1,0,0],[0,1,0],[0,0,-2]])

S = [l7, -l5, l2]

for a in range(3):
    for b in range(3):
        lhs = sp.simplify(S[a]*S[b]-S[b]*S[a])
        rhs = sp.zeros(3)
        for c in range(3):
            rhs += I*sp.LeviCivita(a,b,c)*S[c]
        assert sp.simplify(lhs-rhs) == sp.zeros(3)

Id = sp.eye(3)
def Q(a,b):
    return sp.simplify((S[a]*S[b]+S[b]*S[a])/2
                       - sp.Rational(2,3)*(1 if a==b else 0)*Id)

Q11,Q22,Q33 = Q(0,0),Q(1,1),Q(2,2)
Q12,Q13,Q23 = Q(0,1),Q(0,2),Q(1,2)

assert sp.simplify(Q11+Q22+Q33) == sp.zeros(3)

relations = [
    (l1,-2*Q12),
    (l3,Q22-Q11),
    (l4,-2*Q13),
    (l6,-2*Q23),
    (l8,sqrt3*Q33),
]
for lhs,rhs in relations:
    assert sp.simplify(lhs-rhs) == sp.zeros(3)

basis = S + [Q12,Q13,Q23,Q22-Q11,Q33]
M = sp.Matrix.hstack(*[x.reshape(9,1) for x in basis])
assert M.rank() == 8

for x in basis:
    assert sp.simplify(x.trace()) == 0
    assert sp.simplify(x.H-x) == sp.zeros(3)

print("PASS: quaternion-adjoint spin triplet + five quadrupoles span su(3)")
