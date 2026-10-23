#!/usr/bin/env python3
"""Exact commutant check for the complexified Lorentz four-vector carrier.

Basis: (1,I,J,K).  Rotations act on the spatial triplet.  Boosts mix the
scalar direction with one spatial direction.  We solve for all complex 4x4
matrices commuting with the six generators and verify that the commutant is
one-dimensional, hence scalar.
"""
import sympy as sp

I=sp.I

J=[]
for a in range(3):
    M=sp.zeros(4)
    for b in range(3):
        for c in range(3):
            M[1+b,1+c]=sp.LeviCivita(a,b,c)
    J.append(M)

K=[]
for a in range(3):
    M=sp.zeros(4)
    M[0,1+a]=I
    M[1+a,0]=-I
    K.append(M)

x=sp.symbols("x0:16")
C=sp.Matrix(4,4,x)
eqs=[]
for G in J+K:
    eqs.extend(list(C*G-G*C))

M,_=sp.linear_eq_to_matrix(eqs,x)
assert M.rank()==15
ns=M.nullspace()
assert len(ns)==1

C0=sp.Matrix(4,4,ns[0])
# The surviving matrix is proportional to identity.
lam=C0[0,0]
assert sp.simplify(C0-lam*sp.eye(4))==sp.zeros(4)

# Exhibit failure of a generic colour generator extended by zero on scalar.
lambda5=sp.Matrix([[0,0,-I],[0,0,0],[I,0,0]])
Ccol=sp.zeros(4)
Ccol[1:4,1:4]=lambda5
assert any(sp.simplify(Ccol*G-G*Ccol)!=sp.zeros(4) for G in K)

print("PASS: full Lorentz commutant on same C^4 carrier is scalar only")
