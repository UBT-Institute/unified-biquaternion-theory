#!/usr/bin/env python3
"""Exact checks that the determinant-induced tangent form has SO(3) stabilizer."""
import sympy as sp

I=sp.I
sqrt3=sp.sqrt(3)

# Gell-Mann matrices.
lam=[
sp.Matrix([[0,1,0],[1,0,0],[0,0,0]]),
sp.Matrix([[0,-I,0],[I,0,0],[0,0,0]]),
sp.Matrix([[1,0,0],[0,-1,0],[0,0,0]]),
sp.Matrix([[0,0,1],[0,0,0],[1,0,0]]),
sp.Matrix([[0,0,-I],[0,0,0],[I,0,0]]),
sp.Matrix([[0,0,0],[0,0,1],[0,1,0]]),
sp.Matrix([[0,0,0],[0,0,-I],[0,I,0]]),
sp.Matrix([[1,0,0],[0,1,0],[0,0,-2]])/sqrt3,
]
gens=[I*L for L in lam]

# Realification z=x+i y. Q(z)=y^T y.
Q=sp.diag(0,0,0,1,1,1)

def realify(A):
    Re=A.applyfunc(sp.re)
    Im=A.applyfunc(sp.im)
    return Re.row_join(-Im).col_join(Im.row_join(Re))

pres=[]
for j,A in enumerate(gens):
    R=realify(A)
    condition=sp.simplify(R.T*Q+Q*R)
    if condition==sp.zeros(6):
        pres.append(j+1)

assert pres==[2,5,7]

# These three generators are real antisymmetric and have rank 3 as a Lie basis.
cols=sp.Matrix.hstack(*[
    gens[j-1].reshape(9,1) for j in pres
])
assert cols.rank()==3
for j in pres:
    A=gens[j-1]
    assert A.applyfunc(sp.im)==sp.zeros(3)
    assert sp.simplify(A.T+A)==sp.zeros(3)

print("PASS: Q=||Im z||^2 preserves exactly the lambda_2, lambda_5, lambda_7 SO(3) subalgebra inside su(3)")
