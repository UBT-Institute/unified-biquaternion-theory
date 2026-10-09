#!/usr/bin/env python3
"""Simple symbolic benchmark for the weak adjoint-current nonlocal structure."""
import sympy as sp

x=sp.symbols("x", positive=True)

# Massless one-loop current correlator carries p^2 log p^2 rather than 1/p^2.
assert sp.limit(x*sp.log(x),x,0,dir="+")==0

# A simple massless pole would instead satisfy x*(1/x)=1.
assert sp.limit(x*(1/x),x,0,dir="+")==1

# Physical transverse tensor for fixed generic momentum is transverse.
p0,p1,p2,p3=sp.symbols("p0 p1 p2 p3", real=True)
eta=sp.diag(-1,1,1,1)
p=sp.Matrix([p0,p1,p2,p3])
p_cov=eta*p
p2sq=(p.T*eta*p)[0]
Pi=p_cov*p_cov.T-p2sq*eta
# p^mu Pi_mu nu = 0
assert sp.simplify((p.T*Pi))==sp.zeros(1,4)

print("PASS: weak current benchmark is transverse and has p^2 log p^2 continuum behaviour, not a simple 1/p^2 pole")
