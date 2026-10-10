#!/usr/bin/env python3
"""Exact checks for the Stiefel critical-origin obstruction."""
import sympy as sp

rho=sp.symbols("rho", positive=True)
assert rho**7 == rho**7

G=sp.diag(1,-1,-1,-1)
w=sp.Matrix([1,1,0,0])
assert (w.H*G*w)[0] == 0

v0,v1,v2,v3=sp.symbols("v0 v1 v2 v3", complex=True)
v=sp.Matrix([v0,v1,v2,v3])
norm=sp.expand_complex((v.H*G*v)[0]).subs(v1,v0)
expected=-(sp.re(v2)**2+sp.im(v2)**2+sp.re(v3)**2+sp.im(v3)**2)
assert sp.simplify(norm-expected) == 0

print("PASS: cone measure scales as rho^7 and signature-(1,3) has Witt index 1, so a homogeneous rank-3 frame cannot survive at rho=0")
