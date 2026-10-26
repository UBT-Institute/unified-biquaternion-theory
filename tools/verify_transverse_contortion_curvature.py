#!/usr/bin/env python3
"""Transverse spatial rotation: preserves DV and metric, changes curvature."""
import sympy as s
t=s.symbols("t",real=True)
f=s.Function("f")(t)
J=s.zeros(4)
J[1,2]=1
J[2,1]=-1
V=s.Matrix([1,0,0,0])
assert J*V==s.zeros(4,1)
eta=s.diag(-1,1,1,1)
assert J.T*eta+eta*J==s.zeros(4)
C1=f*J
F01=C1.diff(t)
assert F01[1,2]==s.diff(f,t)
assert F01[2,1]==-s.diff(f,t)
assert F01!=s.zeros(4)
print("metric compatible and transverse: yes")
print("same covariant derivative of V: yes")
print("changed curvature F_01=f'(t) J_12: verified")
print("Bianchi constraints automatic geometric identities, not uniqueness equations")
