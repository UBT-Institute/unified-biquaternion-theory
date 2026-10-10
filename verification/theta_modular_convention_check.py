#!/usr/bin/env python3
"""Finite exact checks for theta convention identities.

These checks do not replace the standard Poisson/Jacobi transformation theorem;
they verify the elementary T/T^2 convention relations term-by-term.
"""
import sympy as sp

n=sp.symbols("n", integer=True)
# exp(pi*i*n^2)=(-1)^n because n^2 and n have the same parity.
for k in range(-20,21):
    assert sp.simplify(sp.exp(sp.pi*sp.I*k*k)-(-1)**k)==0
    assert sp.simplify(sp.exp(2*sp.pi*sp.I*k*k)-1)==0

# With q=e^(2*pi*i*tau), shifting tau by one leaves every q^(n^2) term fixed.
tau=sp.symbols("tau")
for k in range(-8,9):
    lhs=sp.exp(2*sp.pi*sp.I*(tau+1)*k*k)
    rhs=sp.exp(2*sp.pi*sp.I*tau*k*k)
    assert sp.simplify(sp.expand_complex(lhs/rhs)-1)==0

print("PASS: theta T/T^2 convention identities are consistent")
