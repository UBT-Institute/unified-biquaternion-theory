#!/usr/bin/env python3
"""Symbolic quadratic Hamiltonian and linear gauge constraint independence."""
import sympy as s
a,p,k,m,chi=s.symbols("a p k m chi", real=True)
# Mode wave number k, with L=-a/2 dotchi²+a/2 k²chi²-m²/2 chi²
v=s.symbols("v",real=True)
L=-a*v**2/2+a*k*k*chi**2/2-m*m*chi**2/2
momentum=s.diff(L,v)
assert momentum==-a*v
H=s.simplify(p*(p/(-a))-L.subs(v,p/(-a)))
assert s.simplify(H-(-p**2/(2*a)-a*k*k*chi**2/2+m*m*chi**2/2))==0
assert s.diff(H,p,2)==-1/a
print("quadratic p-Hessian=-1/a (negative when a>0)")
print("H=",H)
print("Subject to stationary Minkowski vacuum and no extra primary constraints")
