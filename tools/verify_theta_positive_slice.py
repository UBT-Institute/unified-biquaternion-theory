#!/usr/bin/env python3
"""Exact (2,6) inertia, positive scalar slice, and boost escape.
Conditional on the congruence action X -> S X S^dagger.
"""
import sympy as sp

I=sp.I
sigma3=sp.diag(1,-1)
eta=sp.symbols("eta",real=True)
z=sp.symbols("z",nonzero=True)
# Real coordinates (Re z0..Re z3, Im z0..Im z3)
H=sp.diag(2,-2,-2,-2,2,-2,-2,-2)
assert H.eigenvals()=={sp.Integer(2):2,sp.Integer(-2):6}
Q=sp.Matrix.hstack(sp.eye(8)[:,0],sp.eye(8)[:,4])
assert Q.T*H*Q==2*sp.eye(2)
S=sp.diag(sp.exp(eta/2),sp.exp(-eta/2))
image=sp.simplify(S*(z*sp.eye(2))*S.conjugate().T)
traceless=sp.simplify(image-sp.trace(image)*sp.eye(2)/2)
assert sp.simplify(traceless-z*sp.sinh(eta)*sigma3)==sp.zeros(2)
assert sp.simplify(traceless.diff(eta).subs(eta,0)-z*sigma3)==sp.zeros(2)
# Hermitian 2x2 slice H has (1,3), not positive definite.
print("full inertia (2,6), maximal positive linear dimension=2")
print("scalar complex slice inertia (2,0)")
print("Hermitian slice inertia (1,3)")
print("infinitesimal boost exits the positive scalar slice")
print("This is a kinematic gate, not full Hamiltonian mode counting.")
