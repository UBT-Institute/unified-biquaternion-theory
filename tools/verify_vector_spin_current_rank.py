#!/usr/bin/env python3
"""Algebraic rank of the V-wedge spin current for V timelike."""
import sympy as s
# Pick nonzero timelike V covector, w variable; F_ab=V_a w_b - V_b w_a.
V=s.Matrix([1,0,0,0])
w=s.symbols("w0:4")
M=s.Matrix([V[a]*w[b]-V[b]*w[a] for a in range(4) for b in range(a+1,4)])
J=M.jacobian(w)
assert J.rank()==3
assert M[0]==w[1] and M[1]==w[2] and M[2]==w[3]
assert all(M[j]==0 for j in [3,4,5])
assert s.diag(J,J,J,J).rank()==12
print("one Lorentz-index bivector current rank=3; four spacetime components rank=12")
