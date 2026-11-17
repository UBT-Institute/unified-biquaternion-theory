"""Fixed-point Lorentz-vector test: direct source versus composite chain contribution.

Exact rational 24x16 and 24x4 matrices. Algebraic witness only; the
true composite Euler derivative and inverse implicit jet operator remain open.
"""
import sympy as sp

eta=sp.diag(-1,1,1,1)
pairs=[(a,b) for a in range(4) for b in range(a+1,4)]
v=sp.Matrix([1,0,0,0])
vl=eta*v
# L: delta(omega_{mu}^{ab}) -> delta E_{mu}^{c}; X=v fixed.
L=sp.zeros(16,24)
for mu in range(4):
    for j,(a,b) in enumerate(pairs):
        for c in range(4):
            L[4*mu+c,6*mu+j]=(sp.KroneckerDelta(c,a)*vl[b]
                              -sp.KroneckerDelta(c,b)*vl[a])
# C: Lorentz-vector pure-trace source family.
C=sp.zeros(24,4)
for mu in range(4):
    for j,(a,b) in enumerate(pairs):
        for k in range(4):
            C[6*mu+j,k]=(eta[mu,a]*eta[b,k]-eta[mu,b]*eta[a,k])

assert L.rank()==12
assert C.rank()==4
assert sp.Matrix.hstack(L.T,C).rank()==15
assert len(L.nullspace())==12
assert len(C.T.nullspace())==20
# A generic independent tetrad Euler derivative p can activate an
# off-diagonal boost current unattainable by pure trace C(X).
p=sp.zeros(16,1)
p[1]=1  # p_{mu=0,c=1}
j_chain=L.T*p
assert j_chain[0]==1  # (mu=0; pair a,b=0,1)
assert sp.Matrix.hstack(C,j_chain).rank()==5
# For timelike v, image of L.T includes 12 boosts and no rotations.
assert all(L[:,6*mu+j]==sp.zeros(16,1)
           for mu in range(4) for j,(a,b) in enumerate(pairs) if a!=0)
print("PASS rank(C)=4 rank(L*)=12 rank([C,L*])=15")
print("PASS explicit chain-source outside fixed-E pure-trace current")
