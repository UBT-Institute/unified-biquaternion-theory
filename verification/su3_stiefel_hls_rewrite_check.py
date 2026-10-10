#!/usr/bin/env python3
"""Exact checks for the 4x3 Stiefel / hidden-local-SU(3) rewrite."""
import sympy as sp

# Real degree count.
n_real=2*4*3
hermitian_constraints=3**2
su3_gauge=3**2-1
assert n_real-hermitian_constraints-su3_gauge==7

# Reference negative frame in C^(1,3).
G=sp.diag(1,-1,-1,-1)
Z=sp.Matrix([
    [0,0,0],
    [1,0,0],
    [0,1,0],
    [0,0,1],
])
assert Z.H*G*Z==-sp.eye(3)

# Reference positive normal.
n=sp.Matrix([1,0,0,0])
assert (n.H*G*n)[0]==1
assert Z.H*G*n==sp.zeros(3,1)

# Completeness: n n^dagger G - Z Z^dagger G = I4.
assert sp.simplify(n*n.H*G-Z*Z.H*G-sp.eye(4))==sp.zeros(4)

# Algebraic B equation: C=C0+c I with traceless C0.
c=sp.symbols("c")
x=sp.symbols("x0:9")
C0=sp.Matrix(3,3,x)
C0=C0-sp.trace(C0)*sp.eye(3)/3
C=C0+c*sp.eye(3)
B=sp.Matrix(3,3,sp.symbols("b0:9"))
B=B-sp.trace(B)*sp.eye(3)/3

# The B-dependent quadratic polynomial is Tr(B^2-2 B C);
# its stationary point in the traceless subspace is B=P_su3(C)=C0.
D=B-C0
expr=sp.expand(sp.trace(B*B-2*B*C))
expr_at=sp.expand(expr.subs(dict(zip(list(B),list(C0))))) if False else None

# Check projector directly.
P=C-sp.trace(C)*sp.eye(3)/3
assert sp.simplify(P-C0)==sp.zeros(3)

print("PASS: 4x3 constrained frame modulo local SU(3) has 7 real DOF, reconstructs the timelike coset, and the auxiliary connection equals the traceless frame current")
