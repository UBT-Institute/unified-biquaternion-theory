"""Exact restricted-volume and gradient-Jacobian (Piola) audit.
Not a verifier for the implicit torsionful composite-Theta dynamics.
"""
import sympy as sp
from itertools import product

N0=sp.symbols("N0",positive=True)
E=sp.Matrix(4,4,lambda a,mu:sp.Symbol(f"e{a}{mu}",real=True))
detE=E.det(method="berkowitz")
# Volume locked kinetic = (1/2)*N0*tr(g^{-1}g)*det E
assert sp.simplify(sp.Rational(1,2)*N0*4*detE-2*N0*detE)==0
# Cofactor first variation of determinant; test at a generic invertible tetrad
E0=sp.Matrix([[2,1,0,0],[0,2,1,0],[0,0,3,1],[1,0,0,2]])
for a,mu in product(range(4),repeat=2):
    lhs=sp.diff(detE,E[a,mu]).subs(dict(zip(E,E0)),simultaneous=True)
    rhs=E0.det()*(E0.inv())[mu,a]
    assert sp.simplify(lhs-rhs)==0
# Piola identity (divergence of cofactor of a gradient).
x=sp.symbols("x0:4",real=True)
Y=sp.Matrix([
  x[0]+x[1]*x[2],
  x[1]+x[0]*x[3],
  x[2]+x[1]*x[3],
  x[3]+x[0]*x[2]
])
F=Y.jacobian(x)
C=F.cofactor_matrix()
for a in range(4):
    div=sp.expand(sum(sp.diff(C[a,mu],x[mu]) for mu in range(4)))
    assert div==0,(a,div)
print("PASS volume normalization; all 16 tetrad first variations; 4D gradient Piola identity")
