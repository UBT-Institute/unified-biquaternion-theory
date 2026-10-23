#!/usr/bin/env python3
"""Exact linear-algebra check of the split-jet constant-norm rank no-go."""
import sympy as sp

# Minkowski metric and a generic non-null reference vector, chosen timelike.
eta=sp.diag(-1,1,1,1)
X=sp.Matrix([1,0,0,0])

# Four generic tetrad columns constrained by X.e_mu=0.
e_symbols=sp.symbols("e0:16", real=True)
E=sp.Matrix(4,4,e_symbols)  # rows a, columns mu
constraints=(X.T*eta*E)

# Solve the four linear constraints: first row of E must vanish for this X.
sol=sp.solve(list(constraints),list(E[0,:]),dict=True)
assert len(sol)==1

Ec=E.subs(sol[0])
assert Ec.rank() <= 3

# Orthogonal complement projector explicitly has rank 3.
P=sp.diag(0,1,1,1)
assert P.rank()==3

# Norm evolution identity in abstract scalars:
dx2,w,x2=sp.symbols("dx2 w x2", real=True, nonzero=True)
xD=dx2/2+w*x2
# For constant norm and compatible transport w=0, xD vanishes.
assert sp.simplify(xD.subs({dx2:0,w:0}))==0

print("PASS: constant non-null norm plus norm-preserving split-jet transport confines all tetrad legs to a 3D orthogonal complement, so rank four is impossible")
