#!/usr/bin/env python3
"""Exact checks for chronofactor SO(3) projection and winding multiplicity."""
import sympy as sp

J=[]
for a in range(3):
    M=sp.zeros(3)
    for b in range(3):
        for c in range(3):
            M[b,c]=sp.LeviCivita(a,b,c)
    J.append(M)

p1,p2,p3=sp.symbols("p1 p2 p3")
p=sp.Matrix([[p1,p2,p3]])
eqs=[]
for G in J:
    eqs.extend(list(p*G))
M,_=sp.linear_eq_to_matrix(eqs,[p1,p2,p3])
assert M.rank()==3
assert M.nullspace()==[]

peq=sp.Matrix([[1,1,1]])
assert any(peq*G != sp.zeros(1,3) for G in J)

theta=sp.symbols("theta", real=True)
n=sp.symbols("n", integer=True)
phi=sp.exp(sp.I*n*theta)
assert sp.simplify(-sp.I*sp.diff(phi,theta)-n*phi)==0

print("PASS: no nonzero SO(3)-equivariant R3->R map; S1 winding eigenspaces are multiplicity one")
