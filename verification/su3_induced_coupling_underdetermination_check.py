#!/usr/bin/env python3
"""Checks for monotonic KK-tower induced-coupling underdetermination."""
import mpmath as mp

mp.mp.dps=50

def delta(a):
    nmax=max(100,int(12*a+60))
    return 2*mp.fsum(mp.e1((mp.mpf(n)/a)**2) for n in range(1,nmax+1))

def deriv_formula(a):
    nmax=max(100,int(12*a+60))
    return (4/a)*mp.fsum(mp.e**(-(mp.mpf(n)/a)**2) for n in range(1,nmax+1))

for a in [mp.mpf("0.3"),1,2,10,100]:
    h=mp.mpf("1e-6")*max(1,a)
    num=(delta(a+h)-delta(a-h))/(2*h)
    ana=deriv_formula(a)
    assert ana > 0
    assert abs(num-ana)/ana < mp.mpf("1e-8")

vals=[delta(mp.mpf(x)) for x in ["0.3","1","2","10","100"]]
assert all(vals[i] < vals[i+1] for i in range(len(vals)-1))

# Large-a leading coefficient tends toward 2 sqrt(pi).
a=mp.mpf("200")
ratio=delta(a)/a
assert abs(ratio-2*mp.sqrt(mp.pi))/(2*mp.sqrt(mp.pi)) < mp.mpf("0.03")

print("PASS: KK enhancement is strictly increasing in Lambda*Rpsi and hence cannot predict g without an independent scale determination")
