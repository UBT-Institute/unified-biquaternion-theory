#!/usr/bin/env python3
"""Exact Lorentz-centralizer dimensions with multiplicity m=1,2,3."""
import sympy as sp

I=sp.I
gens=[]
for a in range(3):
    J=sp.zeros(4)
    for b in range(3):
        for c in range(3):
            J[1+b,1+c]=sp.LeviCivita(a,b,c)
    gens.append(J)
for a in range(3):
    K=sp.zeros(4)
    K[0,1+a]=I
    K[1+a,0]=-I
    gens.append(K)

def commutant_dimension(m):
    reps=[sp.kronecker_product(G,sp.eye(m)) for G in gens]
    n=4*m
    In=sp.eye(n)
    blocks=[]
    for G in reps:
        blocks.append(
            sp.kronecker_product(G.T,In)-sp.kronecker_product(In,G)
        )
    M=blocks[0]
    for B in blocks[1:]:
        M=M.col_join(B)
    return n*n-M.rank()

assert commutant_dimension(1)==1
assert commutant_dimension(2)==4
assert commutant_dimension(3)==9

print("PASS: Lorentz commutant dimensions are 1,4,9 for multiplicities 1,2,3")
