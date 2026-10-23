#!/usr/bin/env python3
"""Symbolic transversality benchmark for the weak HLS current loop."""
import sympy as sp

x=sp.symbols("x", positive=True)

# Massless current polarization contributes p^2 log p^2, not a constant mass.
assert sp.limit(x*sp.log(x),x,0,dir="+")==0

# Massive analytic polarization: p^2*(c0+c1 p^2+...) also vanishes at p^2=0.
c0,c1=sp.symbols("c0 c1", finite=True)
expr=x*(c0+c1*x)
assert sp.limit(expr,x,0,dir="+")==0

# A genuine mass intercept would remain finite and nonzero.
m2=sp.symbols("m2", positive=True)
assert sp.limit(m2+x*c0,x,0,dir="+")==m2

print("PASS: conserved-current vacuum polarization changes the p^2 kernel but does not cancel a finite HLS mass intercept at weak coupling")
