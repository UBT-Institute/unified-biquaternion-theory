#!/usr/bin/env python3
"""Exact checks for the composite UBT colour projector connection."""

import sympy as sp

G = sp.Matrix([
    [0,0,0,1],
    [0,-1,0,0],
    [0,0,-1,0],
    [1,0,0,0],
])

# Signature certificate: characteristic polynomial is (lambda-1)(lambda+1)^3.
lam = sp.symbols("lam")
assert sp.factor(G.charpoly(lam).as_expr()) == (lam - 1)*(lam + 1)**3

sqrt2 = sp.sqrt(2)
e0 = sp.Matrix([1,0,0,1]) / sqrt2
e1 = sp.Matrix([1,0,0,-1]) / sqrt2
e2 = sp.Matrix([0,1,0,0])
e3 = sp.Matrix([0,0,1,0])
E = sp.Matrix.hstack(e0,e1,e2,e3)
assert sp.simplify(E.conjugate().T * G * E) == sp.diag(1,-1,-1,-1)

# Orthogonal complement of the scalar line is the traceless subspace a+d=0.
a,b,c,d = sp.symbols("a b c d")
z = sp.Matrix([a,b,c,d])
scalar_pairing = sp.simplify((e0.conjugate().T*G*z)[0])
assert sp.simplify(scalar_pairing - (a+d)/sqrt2) == 0

# Work in the orthonormal signature basis for a curvature witness.
eta = sp.diag(1,-1,-1,-1)
u0 = sp.Matrix([1,0,0,0])
u1 = sp.Matrix([0,1,0,0])
u2 = sp.Matrix([0,0,1,0])

P = sp.eye(4) - u0*(u0.conjugate().T*eta)
assert P*P == P
assert P*u0 == sp.zeros(4,1)
assert P.conjugate().T*eta == eta*P

Px = -(u1*(u0.conjugate().T*eta) + u0*(u1.conjugate().T*eta))
Py = -(u2*(u0.conjugate().T*eta) + u0*(u2.conjugate().T*eta))
Fxy = sp.simplify(P*(Px*Py-Py*Px)*P)

colour = Fxy[1:4,1:4]
lambda2 = sp.Matrix([[0,-sp.I,0],[sp.I,0,0],[0,0,0]])
assert colour == -sp.I*lambda2
assert sp.trace(colour) == 0
assert colour != sp.zeros(3)

print("PASS: timelike colour complement and non-flat SU(3) projector-curvature witness.")
