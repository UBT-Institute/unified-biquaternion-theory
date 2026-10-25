#!/usr/bin/env python3
"""Exact tangent orbit and quadratic inertia at X0=i*r*I.
This is NOT a complete Dirac/Hamiltonian constraint calculation.
"""
import sympy as sp

I=sp.I
sigma=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-I],[I,0]]),sp.diag(1,-1)]
X0=I*sp.eye(2)
gens=[I*s/2 for s in sigma]+[s/2 for s in sigma]

def vec(M):
    entries=[M[0,0],M[0,1],M[1,0],M[1,1]]
    return sp.Matrix([sp.re(v).expand(complex=True) for v in entries]+
                     [sp.im(v).expand(complex=True) for v in entries])

orbit=sp.Matrix.hstack(*(vec(T*X0+X0*T.conjugate().T) for T in gens))
assert orbit.rank()==3
assert all(orbit[:,i]==sp.zeros(8,1) for i in range(3))
# H(X)=2(|z0|²-|z1|²-|z2|²-|z3|²), X=z0 I+sum(zj * i*sigma_j)
basis=[sp.eye(2)]+[I*s for s in sigma]
real_basis=[vec(M) for M in basis]+[vec(I*M) for M in basis]
transform=sp.Matrix.hstack(*real_basis)
assert transform.det()!=0
# In coordinates (Re z0..Re z3, Im z0..Im z3)
metric_z=sp.diag(2,-2,-2,-2,2,-2,-2,-2)
metric_matrix=transform.inv().T*metric_z*transform.inv()
gram=sp.simplify(orbit[:,3:].T*metric_matrix*orbit[:,3:])
assert gram==sp.diag(-2,-2,-2)
# Orthogonal complement signature by Sylvester inertia: (2,6) minus (0,3) => (2,3).
print("orbit rank=3, stabilizer dimension=3 (rotations)")
print("boost-orbit Gram matrix:",gram)
print("full signature=(2,6); tangent-orthogonal signature=(2,3)")
print("WARNING: kinematic inertia only; not complete gauge-fixed physical spectrum")
