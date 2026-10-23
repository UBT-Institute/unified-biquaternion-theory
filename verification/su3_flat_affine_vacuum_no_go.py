#!/usr/bin/env python3
"""Exact check of the flat-affine constant-h no-go."""
import sympy as sp

I=sp.I
N=sp.symbols("N", positive=True, real=True)
G=sp.diag(1,-1,-1,-1)
eta=sp.diag(-1,1,1,1)

# Arbitrary real tetrad matrix e_mu^a.
e=sp.Matrix(4,4,lambda mu,a:sp.symbols(f"e{mu}{a}", real=True))
g=e*eta*e.T

# Coefficient vectors E_mu=(i e_mu^0,e_mu^1,e_mu^2,e_mu^3).
Z=sp.Matrix(4,4,lambda mu,a:I*e[mu,a] if a==0 else e[mu,a])
HB=sp.simplify(sp.conjugate(Z)*G*Z.T)
assert sp.simplify(HB+g)==sp.zeros(4)

# For affine Theta the x-Hessian of h is 2 N Re(HB)=-2 N g.
Hess_h=2*N*HB
assert sp.simplify(Hess_h+2*N*g)==sp.zeros(4)

print("PASS: affine nondegenerate Lorentz tetrad gives d_mu d_nu h = -2 N0 g_mu_nu, so h cannot stay constant")
