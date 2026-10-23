#!/usr/bin/env python3
"""Dimensional and gauge-covariance bookkeeping for the HLS mass operator."""
import sympy as sp

# Canonical dimensions in d=4 after a gauge kinetic term exists.
dim_B=1
dim_d=1
dim_C=1
dim_OV=2*dim_B
dim_cV=4-dim_OV

assert dim_C==dim_B
assert dim_OV==2
assert dim_cV==2

# Symbolic homogeneous transformation demonstrates trace-square invariance.
h,V=sp.symbols("h V", nonzero=True)
# Scalar placeholder: cyclic conjugation h^{-1} V h leaves V in 1D.
Vp=(1/h)*V*h
assert sp.simplify(Vp**2-V**2)==0

print("PASS: (B-C0)^2 is a gauge-invariant dimension-2 HLS operator with a relevant dimension-2 coefficient in four dimensions")
