#!/usr/bin/env python3
"""Symbolic benchmark for the composite-gluon massless-pole criterion."""
import sympy as sp

x,Z=sp.symbols("x Z", positive=True)

# Weak continuum/log form factor: no isolated massless residue.
Gweak=sp.log(x)
assert sp.limit(x*Gweak,x,0,dir="+")==0

# Genuine simple massless pole.
Gpole=Z/x
assert sp.limit(x*Gpole,x,0,dir="+")==Z

# A threshold-like square-root singularity also fails the simple pole test.
Gthreshold=1/sp.sqrt(x)
assert sp.limit(x*Gthreshold,x,0,dir="+")==0

print("PASS: p^2 G_T -> Z>0 isolates a simple massless pole; weak logarithmic/threshold continua fail the criterion")
