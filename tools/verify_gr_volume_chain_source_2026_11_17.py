"""Exact local rank test for the canonical locked-volume tetrad force.

Derivation on the real Lorentz-vector slice at an orthonormal coframe.
It computes the DIRECT connection-to-tetrad chain term only.
No inversion of the derivative-valued implicit operator A=I-J_E is assumed.
"""
import sympy as s

eta=s.diag(-1,1,1,1)
pairs=[(a,b) for a in range(4) for b in range(a+1,4)]
C=s.zeros(24,4)
for mu in range(4):
    for j,(a,b) in enumerate(pairs):
        for c in range(4):
            C[mu*6+j,c]=(s.KroneckerDelta(mu,a)*eta[b,c]
                          -s.KroneckerDelta(mu,b)*eta[a,c])
assert C.rank()==4
v=s.Matrix([1,0,0,0])
vl=eta*v
L=s.zeros(16,24)
for mu in range(4):
    for j,(a,b) in enumerate(pairs):
        for c in range(4):
            L[4*mu+c,mu*6+j]=(s.KroneckerDelta(c,a)*vl[b]
                               -s.KroneckerDelta(c,b)*vl[a])
assert L.rank()==12
p=s.Matrix([s.KroneckerDelta(mu,a)
            for mu in range(4) for a in range(4)])
assert L.T*p==C*v
# The formal combined span still has rank 15 for arbitrary tetrad forces:
assert s.Matrix.hstack(C,L.T).rank()==15
# The directly varied determinant selects ONE tetrad force, not all 16.
for X in [s.Matrix([1,0,0,0]),s.Matrix([2,1,0,0])]:
    w=eta*X
    L_X=s.zeros(16,24)
    for mu in range(4):
        for j,(a,b) in enumerate(pairs):
            for c in range(4):
                L_X[4*mu+c,mu*6+j]=(s.KroneckerDelta(c,a)*w[b]
                                   -s.KroneckerDelta(c,b)*w[a])
    assert L_X.T*p==C*X
print("PASS: direct locked-volume current lies in rank-4 pure-vector image")
print("PASS: generic tetrad-force image rank 12, formal combined span rank 15")
print("NOT TESTED: full implicit A inverse, physical on-shell Theta action")
