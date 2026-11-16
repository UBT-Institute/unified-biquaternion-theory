"""Exact 24x4 accessible pure-vector spin-current rank in a fixed tetrad.

This is the restricted fixed-E Lorentz-vector kinetic source J_{mu ab}
= e_{mu a} X_b - e_{mu b} X_a, with e_mu^a = delta_mu^a.
It is NOT the full 8-real-dimensional composite UBT source.
"""
import sympy as s
eta=s.diag(-1,1,1,1)
pairs=[(a,b) for a in range(4) for b in range(a+1,4)]
M=s.Matrix(24,4,lambda row,c:
    eta[row//6,pairs[row%6][0]]*eta[pairs[row%6][1],c]
   -eta[row//6,pairs[row%6][1]]*eta[pairs[row%6][0],c])
assert M.rank()==4
assert M.T.nullspace() and len(M.T.nullspace())==20
# Each 4-vector X maps to one 24-component current; zero current iff X=0.
X=s.Matrix(s.symbols('X0:4',real=True))
assert M*X != s.zeros(24,1)
assert s.linsolve(list(M*X),list(X))==s.FiniteSet((0,0,0,0))
# Trace projection J^a_(a b) = 3 X_b under the stated index layout.
for b in range(4):
    trace=0
    for a in range(4):
        if a==b:continue
        i=pairs.index((min(a,b),max(a,b)))
        term=sum(eta[a,mu]*M[mu*6+i,c]*X[c] for mu in range(4) for c in range(4))
        trace += (1 if a<b else -1)*term
    assert s.simplify(trace-3*sum(eta[b,c]*X[c] for c in range(4)))==0
print("PASS fixed-tetrad vector spin current: 24x4 rank 4, codim 20, pure trace")
