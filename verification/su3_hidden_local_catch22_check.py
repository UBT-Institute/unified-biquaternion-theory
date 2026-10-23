#!/usr/bin/env python3
"""Exact algebraic check of the minimal hidden-local SU(3) catch-22."""
import sympy as sp

# Generic 4x4 symbolic matrix and a traceless lower-right 3x3 H element.
x=sp.symbols("x0:16")
X=sp.Matrix(4,4,x)

b=sp.symbols("b0:9")
B3=sp.Matrix(3,3,b)
B3=B3-sp.trace(B3)*sp.eye(3)/3
B=sp.zeros(4)
B[1:4,1:4]=B3

def Ph(M):
    out=sp.zeros(4)
    C=M[1:4,1:4]
    out[1:4,1:4]=C-sp.trace(C)*sp.eye(3)/3
    return sp.simplify(out)

def Pm(M):
    return sp.simplify(M-Ph(M))

# H-valued auxiliary field disappears from the coset projection.
assert sp.simplify(Pm(X-B)-Pm(X)) == sp.zeros(4)

# H projection shifts exactly by -B.
assert sp.simplify(Ph(X-B)-(Ph(X)-B)) == sp.zeros(4)

# At constant representative X=0, the auxiliary mismatch is -B, nonzero
# for a generic H field: this is the algebraic mass/Stueckelberg square.
assert sp.simplify(Ph(-B)+B) == sp.zeros(4)

print("PASS: H-valued auxiliary field drops from coset kinetic projection; coupling it through the H mismatch yields a quadratic B term around a constant representative")
