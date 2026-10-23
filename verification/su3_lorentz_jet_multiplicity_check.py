#!/usr/bin/env python3
"""Exact checks for the Lorentz-commutant and second-jet multiplicity audit."""
import sympy as sp

I=sp.I
s1=sp.Matrix([[0,1],[1,0]])
s2=sp.Matrix([[0,-I],[I,0]])
s3=sp.Matrix([[1,0],[0,-1]])
eye2=sp.eye(2)
basis=[eye2,s1,s2,s3]

def coords(M):
    return sp.Matrix([sp.simplify(sp.trace(B*M)/2) for B in basis])

# Lorentz vector representation from dX=A X + X A^dagger.
gens=[]
for s in (s1,s2,s3):
    for A in (I*s/2,s/2):  # rotation, boost
        gens.append(sp.Matrix.hstack(*[
            coords(sp.simplify(A*B+B*A.H)) for B in basis
        ]))

# Boost K3 mixes scalar and sigma_3.
K3=gens[5]
assert K3*sp.Matrix([1,0,0,0]) == sp.Matrix([0,0,0,1])
assert K3*sp.Matrix([0,0,0,1]) == sp.Matrix([1,0,0,0])

# Common commutant is one-dimensional: scalar identity.
xx=sp.symbols("x0:16")
C=sp.Matrix(4,4,xx)
eqs=[]
for G in gens:
    eqs.extend(list(C*G-G*C))
Aeq,_=sp.linear_eq_to_matrix(eqs,xx)
assert 16-Aeq.rank()==1

# Symmetric second spacetime jet H_{mu nu}^rho has 10*4=40 components.
eta=[-1,1,1,1]
pairs=[(m,n) for m in range(4) for n in range(m,4)]
index={}
k=0
for m,n in pairs:
    for r in range(4):
        index[(m,n,r)]=k
        k+=1

def idx(m,n,r):
    if m>n:
        m,n=n,m
    return index[(m,n,r)]

box=sp.zeros(4,40)
graddiv=sp.zeros(4,40)
for r in range(4):
    for m in range(4):
        box[r,idx(m,m,r)] += eta[m]
    for sig in range(4):
        graddiv[r,idx(r,sig,sig)] += eta[r]

assert box.rank()==4
assert graddiv.rank()==4
assert sp.Matrix.vstack(box,graddiv).rank()==8

# If an independent Lorentz-scalar psi-second-jet vector is appended,
# the three vector channels have total rank 12.
M=sp.zeros(12,44)
M[0:4,0:40]=box
M[4:8,0:40]=graddiv
M[8:12,40:44]=sp.eye(4)
assert M.rank()==12

# Fundamental SU(3) action on one nonzero triplet sees only 5/8 generator
# directions; the stabilizer kernel is su(2), dimension 3.
sqrt3=sp.sqrt(3)
lams=[
sp.Matrix([[0,1,0],[1,0,0],[0,0,0]]),
sp.Matrix([[0,-I,0],[I,0,0],[0,0,0]]),
sp.Matrix([[1,0,0],[0,-1,0],[0,0,0]]),
sp.Matrix([[0,0,1],[0,0,0],[1,0,0]]),
sp.Matrix([[0,0,-I],[0,0,0],[I,0,0]]),
sp.Matrix([[0,0,0],[0,0,1],[0,1,0]]),
sp.Matrix([[0,0,0],[0,0,-I],[0,I,0]]),
sp.Matrix([[1,0,0],[0,1,0],[0,0,-2]])/sqrt3,
]
v=sp.Matrix([1,0,0])
cols=[]
for L in lams:
    y=I*L*v
    cols.append(sp.Matrix([sp.re(z) for z in y]+[sp.im(z) for z in y]))
orbit=sp.Matrix.hstack(*cols)
assert orbit.rank()==5
assert len(orbit.nullspace())==3

print("PASS: raw biquaternion Lorentz commutant is scalar; J2 has the stated vector multiplicities")
