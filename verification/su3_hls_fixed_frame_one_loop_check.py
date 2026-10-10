#!/usr/bin/env python3
"""Algebraic checks for the weak fixed-frame HLS leading-log scaling."""
import sympy as sp

cV,c3,L=sp.symbols("cV c3 L", positive=True)
pi=sp.pi

g0=cV/c3
ZB=sp.simplify(g0**2*L/(96*pi**2))
m2=sp.simplify(cV/ZB)
gH2=sp.simplify(1/ZB)

assert sp.simplify(ZB-cV**2*L/(96*pi**2*c3**2))==0
assert sp.simplify(m2-96*pi**2*c3**2/(cV*L))==0
assert sp.simplify(gH2-96*pi**2*c3**2/(cV**2*L))==0

# Large-cV: mass and coupling both vanish.
assert sp.limit(m2,cV,sp.oo)==0
assert sp.limit(gH2,cV,sp.oo)==0

# Small-cV: no finite induced gauge description.
assert sp.limit(ZB,cV,0,dir="+")==0
assert sp.limit(gH2,cV,0,dir="+")==sp.oo

print("PASS: weak fixed-frame HLS generates positive Z_B, but finite-cV vectors remain massive; the massless cV->infinity limit is free/decoupled")
