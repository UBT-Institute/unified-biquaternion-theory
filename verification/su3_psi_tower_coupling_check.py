#!/usr/bin/env python3
"""Numerical checks for the compact-psi induced SU(3) coupling benchmark."""
import mpmath as mp

mp.mp.dps=50

def delta(a):
    nmax=max(80,int(10*a+40))
    return 2*mp.fsum(mp.e1((mp.mpf(n)/a)**2) for n in range(1,nmax+1))

d1=delta(mp.mpf(1))
assert abs(d1-mp.mpf("0.4463514816011386642361721821886799925")) < mp.mpf("1e-35")

# Solve benchmark tower-only hierarchy targets.
def solve_target(target):
    lo=mp.mpf("0.1")
    hi=mp.mpf("1000")
    for _ in range(100):
        mid=(lo+hi)/2
        if delta(mid) < target:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

a947=solve_target(96*mp.pi**2)
assert abs(a947-mp.mpf("271.315")) < mp.mpf("0.01")

a636=solve_target(mp.mpf("636.6"))
assert abs(a636-mp.mpf("183.396")) < mp.mpf("0.02")

# Large-a leading asymptotic should approach 2 sqrt(pi) a.
a=mp.mpf("100")
ratio=delta(a)/(2*mp.sqrt(mp.pi)*a)
assert ratio > mp.mpf("0.95") and ratio < mp.mpf("1.01")

print("PASS: compact-psi KK tower benchmark verified; self-dual enhancement is 0.44635148 and O(10^2) Lambda R is needed for strong induced coupling")
