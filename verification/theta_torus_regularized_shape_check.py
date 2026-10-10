#!/usr/bin/env python3
"""High-precision diagnostic for the fixed-area torus determinant shape."""
import mpmath as mp

mp.mp.dps=60

def eta(tau):
    q=mp.e**(2j*mp.pi*tau)
    prod=mp.mpc(1)
    for n in range(1,5000):
        qn=q**n
        prod *= (1-qn)
        if abs(qn) < mp.mpf("1e-55"):
            break
    return mp.e**(mp.pi*1j*tau/12)*prod

def f(x,y):
    return mp.log(y)+4*mp.log(abs(eta(mp.mpc(x,y))))

def hessian(x,y,h=mp.mpf("1e-5")):
    f0=f(x,y)
    fxx=(f(x+h,y)-2*f0+f(x-h,y))/h**2
    fyy=(f(x,y+h)-2*f0+f(x,y-h))/h**2
    fxy=(f(x+h,y+h)-f(x+h,y-h)-f(x-h,y+h)+f(x-h,y-h))/(4*h**2)
    return mp.matrix([[fxx,fxy],[fxy,fyy]])

square=f(0,1)
hexy=mp.sqrt(3)/2
hexv=f(mp.mpf("0.5"),hexy)
assert hexv > square

Hs=hessian(mp.mpf("0"),mp.mpf("1"))
es=sorted([mp.re(v) for v in mp.eig(Hs)[0]])
assert es[0] < 0 < es[1]
assert abs(es[0]-mp.mpf("-1.298211")) < mp.mpf("2e-4")
assert abs(es[1]-mp.mpf("0.298211")) < mp.mpf("2e-4")

Hh=hessian(mp.mpf("0.5"),hexy)
eh=sorted([mp.re(v) for v in mp.eig(Hh)[0]])
assert eh[1] < 0
for v in eh:
    assert abs(v+mp.mpf(2)/3) < mp.mpf("2e-4")

# Rectangular square is a determinant maximum.
assert f(0,mp.mpf("1.2")) < square
assert f(0,mp.mpf("0.8")) < square

print("PASS: zeta-determinant shape has square saddle in full moduli, square rectangular maximum, and hexagonal local maximum")
