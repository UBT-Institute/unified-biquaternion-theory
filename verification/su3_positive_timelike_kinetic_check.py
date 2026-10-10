#!/usr/bin/env python3
"""Exact checks for the positive timelike-cone kinetic metric candidate."""
import sympy as sp

G=sp.diag(1,-1,-1,-1)
r=sp.symbols("r", positive=True, real=True)
theta=sp.Matrix([r,0,0,0])

K=-G+2*(G*theta*theta.H*G)/(theta.H*G*theta)[0]
assert sp.simplify(K-sp.eye(4))==sp.zeros(4)

# Generic reference-point fluctuation has positive Euclidean norm.
u=sp.Matrix(sp.symbols("u0:4", complex=True))
expr=sp.expand_complex((u.H*K*u)[0])
# At the reference point K=I, so this is sum |u_i|^2.
assert sp.simplify((u.H*K*u)[0]-(u.H*u)[0])==0

# Covariance checked on a nontrivial SU(1,3) boost.
L=sp.Matrix([
[sp.cosh(r),sp.sinh(r),0,0],
[sp.sinh(r),sp.cosh(r),0,0],
[0,0,1,0],
[0,0,0,1]
])
# Re-use r as a real rapidity here; symbolic identity still holds.
assert sp.simplify(L.H*G*L-G)==sp.zeros(4)

th2=L*theta
K2=-G+2*(G*th2*th2.H*G)/(th2.H*G*th2)[0]
assert sp.simplify(L.H*K2*L-K)==sp.zeros(4)

print("PASS: field-dependent timelike kinetic metric is positive at the reference vacuum and SU(1,3)-covariant")
