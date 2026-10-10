#!/usr/bin/env python3
"""Exact checks for the minimal-bimodule SU(3) no-go.

We represent A = Mat(2,C) on the ordered basis E11,E12,E21,E22 and verify:
1. span{L_A,-R_B} has complex rank 7;
2. the subspace of left/right operators preserving traceless matrices has
   complex dimension 4;
3. imposing zero trace on the induced 3D traceless representation leaves
   dimension 3;
4. those three directions are the adjoint sl2/spin-1 directions.
"""
import sympy as sp

I = sp.I
E11=sp.Matrix([[1,0],[0,0]])
E12=sp.Matrix([[0,1],[0,0]])
E21=sp.Matrix([[0,0],[1,0]])
E22=sp.Matrix([[0,0],[0,1]])
B4=[E11,E12,E21,E22]

def coords4(X):
    return sp.Matrix([X[0,0],X[0,1],X[1,0],X[1,1]])

def op_lr(A,B):
    return sp.Matrix.hstack(*[coords4(A*X-X*B) for X in B4])

ops=[op_lr(A,sp.zeros(2)) for A in B4]
ops += [op_lr(sp.zeros(2),B) for B in B4]
flat=sp.Matrix.hstack(*[M.reshape(16,1) for M in ops])
assert flat.rank()==7

# traceless basis = sigma-like basis over C
X1=sp.Matrix([[0,1],[1,0]])
X2=sp.Matrix([[0,-I],[I,0]])
X3=sp.Matrix([[1,0],[0,-1]])
V=[X1,X2,X3]

# Generic A,B and solve preservation tr(A X - X B)=0 for each X in V.
a=sp.symbols('a0:4')
b=sp.symbols('b0:4')
A=sum((a[k]*B4[k] for k in range(4)),sp.zeros(2))
B=sum((b[k]*B4[k] for k in range(4)),sp.zeros(2))
eqs=[sp.expand(sp.trace(A*X-X*B)) for X in V]
Mpres,_=sp.linear_eq_to_matrix(eqs,list(a)+list(b))
assert Mpres.rank()==3
assert 8-Mpres.rank()==5  # pairs; one common-central kernel acts trivially

# Build restriction matrix on V for solutions using nullspace.
ns=Mpres.nullspace()

def coeffV(Y):
    # Y traceless: coefficients in X1,X2,X3
    return sp.Matrix([
        sp.simplify((Y[0,1]+Y[1,0])/2),
        sp.simplify((Y[1,0]-Y[0,1])/(2*I)),
        sp.simplify((Y[0,0]-Y[1,1])/2),
    ])

restr=[]
for v in ns:
    Av=sum((v[k]*B4[k] for k in range(4)),sp.zeros(2))
    Bv=sum((v[4+k]*B4[k] for k in range(4)),sp.zeros(2))
    R=sp.Matrix.hstack(*[coeffV(Av*X-X*Bv) for X in V])
    restr.append(R)

Rflat=sp.Matrix.hstack(*[R.reshape(9,1) for R in restr])
assert Rflat.rank()==4

# Add trace_V = 0 and verify dimension 3 of operator restrictions.
cols=[]
for R in restr:
    cols.append(R.reshape(9,1))
C=sp.Matrix.hstack(*cols)
trrow=sp.Matrix([[sp.trace(R) for R in restr]])
# Coefficient combinations c with tr=0; map through C.
ker_tr=trrow.nullspace()
Z=sp.Matrix.hstack(*[C*k for k in ker_tr])
assert Z.rank()==3

# Direct commutator adjoint matrices have rank 3 and lie in trace-zero span.
ad=[]
for A0 in V:
    R=sp.Matrix.hstack(*[coeffV(A0*X-X*A0) for X in V])
    ad.append(R)
    assert sp.trace(R)==0
Ad=sp.Matrix.hstack(*[R.reshape(9,1) for R in ad])
assert Ad.rank()==3
assert sp.Matrix.hstack(Z,Ad).rank()==3

print("PASS: minimal V-preserving bimodule = ad(sl2) + scalar; volume-preserving part = ad(sl2) only")
