#!/usr/bin/env python3
"""Exact invariant probe of a nongauge negative tangent near X0=i*r*I."""
import sympy as s
r,v=s.symbols("r v",real=True,nonzero=True)
I=s.I
X=I*r*s.eye(2)-v*s.diag(1,-1)
assert s.factor(X.det())==-r**2-v**2
# H(X)=2 (|z0|^2-|z3|^2), here z0=i*r,z3=i*v
H=2*(r*r-v*v)
assert s.diff(H,v).subs(v,0)==0
assert s.diff(H,v,2)==-4
assert s.diff(X.det(),v).subs(v,0)==0
assert s.diff(X.det(),v,2)==-2
# Boosts of X0 are i*r*sigma_j; real traceless perturbation -v*sigma3
# is independent over real numbers of those directions.
print("H=2*(r**2-v**2), det X=-r**2-v**2")
print("both first derivatives vanish at v=0; second derivatives are nonzero")
print("negative transverse perturbation is not an infinitesimal boost gauge direction")
print("No full nonlinear constraint or physical-spectrum claim")
