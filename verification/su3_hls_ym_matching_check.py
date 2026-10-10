#!/usr/bin/env python3
"""Numerical checks for HLS-to-pure-Yang-Mills threshold matching."""
import math

b0=11.0

def zb_for_ratio(R):
    return b0/(8*math.pi**2)*math.log(R)

def g_for_zb(z):
    return 1/math.sqrt(z)

for R,target in [(10,0.3207),(100,0.6415),(1000,0.9622)]:
    z=zb_for_ratio(R)
    assert abs(z-target)<5e-4
    recovered=math.exp(8*math.pi**2*z/b0)
    assert abs(recovered/R)/R < 1e-12

R=1000.0
required=12*b0*math.log(R)
assert 910 < required < 913

# Weak benchmark a_H=1, L=10.
zweak=10/(96*math.pi**2)
ratio=math.exp(8*math.pi**2*zweak/b0)
assert 1.07 < ratio < 1.09

a_required=math.sqrt(required/10)
assert 9.5 < a_required < 9.6

print("PASS: pure-YM matching requires order-one Z_B for large hierarchy; weak a_H~1 induction gives negligible scale separation")
