#!/usr/bin/env python3
"""Exact degree-count checks for SU(3) versus U(3) Stiefel quotients."""

def d_su3(N):
    return 6*N - 9 - 8

def d_u3(N):
    return 6*N - 9 - 9

assert d_su3(4)==7
assert d_u3(4)==6

# Unique integer N with SU3 quotient dimension 7.
solutions=[N for N in range(3,20) if d_su3(N)==7]
assert solutions==[4]

# Adding one radial variable recovers one biquaternion = 8 real components.
assert d_su3(4)+1==8

print("PASS: 4x3/SU(3) gives exactly 7 normalized real modes, while 4x3/U(3) gives 6 and removes the phase direction")
