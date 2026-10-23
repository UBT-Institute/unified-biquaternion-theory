#!/usr/bin/env python3
"""Symbolic checks for radial HLS critical scaling."""
import sympy as sp

rho,mu,lam1,aH,L=sp.symbols("rho mu lam1 aH L", positive=True)
pi=sp.pi

# Sigma-model coefficients scale with rho^2.
c3=rho**2
cV=aH*rho**2
ratio=sp.simplify(cV/c3)
assert ratio==aH

ZB=sp.simplify(ratio**2*L/(96*pi**2))
m2=sp.simplify(cV/ZB)
g2=sp.simplify(1/ZB)

assert not ZB.has(rho)
assert sp.limit(m2,rho,0,dir="+")==0
assert not g2.has(rho)

# Enhanced-potential minimum rho0^2=-mu_phys/(4 lambda1).
# Use eps=-mu_phys>0 approaching zero from the broken side.
eps=sp.symbols("eps", positive=True)
rho2=eps/(4*lam1)
assert sp.limit(rho2,eps,0,dir="+")==0

print("PASS: if c3 and cV share the radial rho^2 scale, induced Z_B stays finite while the HLS mass vanishes as rho->0")
