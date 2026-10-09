#!/usr/bin/env python3
"""Rank benchmark for one-biquaternion versus physical SU(3) gluon residues."""
import sympy as sp

N_theta=8
N_colour=8

# In a physical gauge for a fixed null momentum, one massless vector has two
# transverse polarizations.  Represent the physical projector by rank-2 diag.
PT=sp.diag(0,1,1,0)
assert PT.rank()==2

Pgluon=sp.kronecker_product(sp.eye(N_colour),PT)
assert Pgluon.rank()==16

# Any residue of an 8x8 microscopic propagator has rank at most 8.
R=sp.MatrixSymbol("R",N_theta,N_theta)
assert N_theta < Pgluon.rank()

print("PASS: one biquaternion has at most rank-8 linearized residue, while eight physical massless gluons require rank 16")
