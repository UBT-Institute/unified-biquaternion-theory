#!/usr/bin/env python3
"""Exact spectral check: S1_psi compactification quantizes n, not spatial k."""
import sympy as sp

k,R=sp.symbols("k R", positive=True, real=True)
n=sp.symbols("n", integer=True)

lam=k**2+n**2/R**2

# Zero KK mode has arbitrarily small positive spatial eigenvalue.
lam0=sp.simplify(lam.subs(n,0))
assert lam0==k**2
assert sp.limit(lam0,k,0,dir="+")==0

# First nonzero internal mode has a mass gap, not a spatial momentum cutoff.
lam1=sp.simplify(lam.subs(n,1))
assert sp.limit(lam1,k,0,dir="+")==1/R**2

print("PASS: compact S1_psi creates KK masses n/R but leaves zero-mode spatial momentum continuous down to k=0")
