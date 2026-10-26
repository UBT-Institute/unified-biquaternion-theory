#!/usr/bin/env python3
"""Four-speed determinant Hessian and cofactor test (auxiliary connection fixed)."""
import sympy as s
v=s.symbols("v0:4")
z=s.symbols("z0:12")
Q=s.Matrix([list(v)]+[list(z[i*4:(i+1)*4]) for i in range(3)])
F,N=s.symbols("F N",nonzero=True)
L=F*Q.det()/N**2
p=s.Matrix([s.diff(L,x) for x in v])
H=s.hessian(L,v)
assert H==s.zeros(4)
assert all(not p[j].has(*v) for j in range(4))
for j in range(4):
    assert s.expand(p[j]-F*Q.cofactor(0,j)/N**2)==0
print("4x4 Hessian exactly zero; four velocity-independent cofactor momenta")
