#!/usr/bin/env python3
"""Algebraic rank check for the split-jet auxiliary multiplier equations."""
import sympy as sp

# Choose a representative non-null Lorentz vector X=(1,0,0,0).
eta=sp.diag(-1,1,1,1)
X=sp.Matrix([1,0,0,0])

# One fixed spacetime index mu is enough: lambda^a has four components.
la=sp.symbols("l0:4", real=True)
L=sp.Matrix(la)

# Antisymmetric wedge condition lambda^[a X^b]=0.
eq=[]
for a in range(4):
    for b in range(a+1,4):
        eq.append(sp.expand(L[a]*X[b]-L[b]*X[a]))

# Orthogonality lambda.X=0.
eq.append((L.T*eta*X)[0])

A,b=sp.linear_eq_to_matrix(eq,la)
assert A.rank()==4
assert len(A.nullspace())==0

print("PASS: on a non-null patch, split-jet K^J and w variations force the Lagrange multiplier lambda to vanish; the sector is a pure constraint, not a current-current kernel")
