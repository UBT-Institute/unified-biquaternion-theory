#!/usr/bin/env python3
"""Exact cofactor/Legendre check for Proposition-9 timelike composite branch."""
import sympy as s
r,N,c,U,v=s.symbols("rho N0 c U v", real=True, nonzero=True)
b=s.symbols("b0:12")
g=s.symbols("g1:4")
Q=s.Matrix([[v,*[r*b[j] for j in range(3)]],
    *[[g[k],*[r*b[3+3*k+j] for j in range(3)]] for k in range(3)]])
D=s.factor(Q.det())
minor=s.Matrix([[b[3+3*k+j] for j in range(3)] for k in range(3)]).det()
assert s.simplify(s.diff(D,v)-r**3*minor)==0
F=4*c*N-U
L=s.expand(F*D/N**2)
pi=s.diff(L,v)
assert s.simplify(pi-F*r**3*minor/N**2)==0
assert s.diff(L,v,2)==0
print("cofactor coefficient rho^3 det(b_i^j): verified")
print("velocity Hessian: zero")
print("primary scalar momentum constraint: pi_rho-F(rho)rho^3 det(b_i^j)/N0^2=0 (oriented patch)")
print("no full constraint classification claimed")
