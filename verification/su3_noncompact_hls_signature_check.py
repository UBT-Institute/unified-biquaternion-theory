#!/usr/bin/env python3
"""Exact tangent-signature check for the naive noncompact Stiefel kinetic."""
import sympy as sp

G=sp.diag(1,-1,-1,-1)
Z0=sp.Matrix([
    [0,0,0],
    [1,0,0],
    [0,1,0],
    [0,0,1],
])

# Six real triplet directions: Re/Im of the three top-row entries.
trip=[]
for j in range(3):
    M=sp.zeros(4,3)
    M[0,j]=1
    trip.append(M)
    M=sp.zeros(4,3)
    M[0,j]=sp.I
    trip.append(M)

# One common phase singlet.
sing=sp.I*Z0

def q(M):
    return sp.simplify(sp.trace(M.H*G*M))

vals=[q(M) for M in trip]
assert vals==[1,1,1,1,1,1]
assert q(sing)==-3

print("PASS: naive Tr(dZ^dagger G dZ) has physical target signature (6+,1-); no overall sign makes the noncompact 7D coset kinetic positive")
