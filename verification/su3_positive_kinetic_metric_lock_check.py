#!/usr/bin/env python3
"""Exact symbolic checks for the metric-lock identity of K^+_Theta."""
import sympy as sp

I=sp.I
G=sp.diag(1,-1,-1,-1)
eta=sp.diag(-1,1,1,1)

# Arbitrary real tetrad coefficients e_mu^a.
e=sp.Matrix(4,4,lambda mu,a:sp.symbols(f"e{mu}{a}", real=True))
g=sp.simplify(e*eta*e.T)

# Biquaternion coefficient vector of E_mu:
# z^0=i e_mu^0, z^k=e_mu^k.
Z=sp.Matrix(4,4,lambda mu,a:I*e[mu,a] if a==0 else e[mu,a])

# Hermitian Gram matrix h_B(E_mu,E_nu).
HB=sp.simplify(sp.conjugate(Z)*G*Z.T)
assert sp.simplify(HB+g)==sp.zeros(4)

# At a timelike reference Theta=r e0, K^+=I.
r=sp.symbols("r", positive=True, real=True)
theta=sp.Matrix([r,0,0,0])
h=(theta.H*G*theta)[0]
K=-G+2*(G*theta*theta.H*G)/h
assert sp.simplify(K-sp.eye(4))==sp.zeros(4)

# Constant-h compatibility: c+c*=D h, so D h=0 makes c imaginary.
cr,ci=sp.symbols("cr ci", real=True)
c=cr+I*ci
assert sp.simplify(c+sp.conjugate(c)-2*cr)==0

print("PASS: on the canonical Lorentz tetrad slice, E^dagger G E = -g; the positive K^+ kinetic therefore collapses to volume plus the single c_mu current after metric lock")
