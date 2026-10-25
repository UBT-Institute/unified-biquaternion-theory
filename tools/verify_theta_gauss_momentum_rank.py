#!/usr/bin/env python3
"""Exact Theta Gauss momentum Jacobian at X0=iI (not full ADM constraints)."""
import sympy as s
i=s.I
sigma=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-i],[i,0]]),s.diag(1,-1)]
gens=[i*x/2 for x in sigma]+[x/2 for x in sigma]
X0=i*s.eye(2)
def realvec(M):
    vals=[M[0,0],M[0,1],M[1,0],M[1,1]]
    return s.Matrix([s.re(t).expand(complex=True) for t in vals]+
                    [s.im(t).expand(complex=True) for t in vals])
orbit=s.Matrix.hstack(*(realvec(T*X0+X0*T.conjugate().T) for T in gens))
assert orbit.rank()==3
assert orbit[:,:3]==s.zeros(8,3)
# Linear momentum derivative d Gauss_a/d p_A is transpose of the orbit.
J=orbit.T
assert J.shape==(6,8) and J.rank()==3
print("linearized Theta Gauss momentum Jacobian rank=3 of 6")
print("three unbroken rotation generators have zero Theta-momentum gradient")
print("residual Theta kinetic inertia (2,3), conditional on regular tangent reduction")
