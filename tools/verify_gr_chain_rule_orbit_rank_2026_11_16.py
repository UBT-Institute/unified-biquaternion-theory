"""Exact Lorentz-orbit chain-rule rank for a non-null Lorentz vector.
Does not verify full biquaternionic Theta or implicit composite connection.
"""
import sympy as s
eta=s.diag(-1,1,1,1)
pairs=[(a,b) for a in range(4) for b in range(a+1,4)]
def orbit(X):
    x=s.Matrix(X); low=eta*x
    L=s.Matrix.hstack(*(s.eye(4)[:,a]*low[b]-s.eye(4)[:,b]*low[a] for a,b in pairs))
    return x,L
for X in [(1,0,0,0),(0,1,0,0),(2,1,0,0)]:
    x,L=orbit(X)
    assert (x.T*eta*x)[0]!=0
    assert L.rank()==3
    assert len(L.nullspace())==3
    assert x.T*eta*L==s.zeros(1,6)
    print(X,"rank",L.rank(),"stabilizer",len(L.nullspace()))
print("PASS: four independent spacetime slots give rank 12, stabilizer 12")
