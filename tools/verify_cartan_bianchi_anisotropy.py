#!/usr/bin/env python3
"""Verify Bianchi-I Gaussian W tensor and its anisotropic witness."""
import sympy as s
t=s.symbols("t",positive=True,real=True)
a=[s.Integer(1),s.exp(t/2),s.exp(t/3)]
H=[s.simplify(s.diff(ai,t)/ai) for ai in a]
W=s.diag(*[s.simplify(1-t*h) for h in H])
assert W.subs(t,1)==s.diag(1,s.Rational(1,2),s.Rational(2,3))
assert W[0,0]!=W[1,1] and W[1,1]!=W[2,2]
# Coordinate expression: spatial W_ii = a_i² - t a_i a_i'
for i in range(3):
    assert s.simplify(a[i]**2*W[i,i]-(a[i]**2-t*a[i]*s.diff(a[i],t)))==0
print("Gaussian W orthonormal spatial diag at t=1: (1, 1/2, 2/3)")
print("Not SO(3)-invariant; unique isotropic Cartan tensor cannot equal it")
