#!/usr/bin/env python3
"""Exact Lorentz commutant check on the value + first jet of Theta."""
import sympy as sp

I=sp.I
s1=sp.Matrix([[0,1],[1,0]])
s2=sp.Matrix([[0,-I],[I,0]])
s3=sp.Matrix([[1,0],[0,-1]])
eye2=sp.eye(2)
basis=[eye2,s1,s2,s3]

def coords(M):
    return sp.Matrix([sp.simplify(sp.trace(B*M)/2) for B in basis])

gens=[]
for s in (s1,s2,s3):
    for A in (I*s/2,s/2):
        gens.append(sp.Matrix.hstack(*[
            coords(sp.simplify(A*B+B*A.H)) for B in basis
        ]))

I4=sp.eye(4)
G20=[]
for G in gens:
    first=sp.kronecker_product(G,I4)+sp.kronecker_product(I4,G)
    G20.append(sp.diag(G,first))

I20=sp.eye(20)
constraints=[]
for G in G20:
    # vec(C G - G C) = (G^T kron I - I kron G) vec(C)
    constraints.append(
        sp.kronecker_product(G.T,I20)-sp.kronecker_product(I20,G)
    )

M=sp.Matrix.vstack(*constraints)
commutant_dim=400-M.rank()
assert commutant_dim==5

print("PASS: J^1 Theta Lorentz commutant has dimension 5 (multiplicity-free, no M3 block)")
