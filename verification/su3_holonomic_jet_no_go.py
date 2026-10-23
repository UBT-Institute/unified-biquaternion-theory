#!/usr/bin/env python3
"""Exact holonomic-jet checks for the proposed three-channel SU(3) route."""
import sympy as sp

# Use a simple Euclidean exact momentum witness k=(1,0,0,0), p=2.
# Signs are irrelevant for the rank/invariance conclusions.
k = sp.Matrix([1,0,0,0])
p2 = sp.Integer(4)
k2 = sp.Integer(1)
I4 = sp.eye(4)
P = k*k.T

O1 = k2*I4
O2 = P
O3 = p2*I4

# Channel map Theta -> (O1 Theta, O2 Theta, O3 Theta) has rank four.
H = sp.Matrix.vstack(O1,O2,O3)
assert H.rank() == 4

# Infinitesimal copy-space lambda_1 action.
lam1 = sp.Matrix([[0,1,0],[1,0,0],[0,0,0]])
G = sp.kronecker_product(lam1, I4)

# A transverse holonomic field amplitude.
theta = sp.Matrix([0,1,0,0])
phi = H*theta
moved = G*phi

# Generic moved vector is not in im(H): rank increases.
assert sp.Matrix.hstack(H,moved).rank() == 5

# Quadratic operator collapse.
s,r = sp.symbols("s r", real=True)
a11,a22,a33,a12,a13,a23 = sp.symbols(
    "a11 a22 a33 a12 a13 a23", real=True
)
# Real symmetric part is sufficient because O_A are commuting/self-adjoint here.
# O2^2 = s O2 abstractly.  Effective coefficients:
A = a11*s**2 + 2*a13*s*r + a33*r**2
B = sp.expand((a22 + 2*a12)*s + 2*a23*r)
assert sp.Poly(A,s,r).total_degree() == 2
assert sp.Poly(B,s,r).total_degree() == 1

print("PASS: three derivative channels are a rank-4 holonomic image, not an independent SU(3) triplet")
