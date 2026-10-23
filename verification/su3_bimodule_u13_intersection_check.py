#!/usr/bin/env python3
"""Exact intersection of minimal left/right biquaternion operators with u(1,3)."""
import sympy as sp

I=sp.I
G=sp.diag(1,-1,-1,-1)

def qmul(a,b):
    a0,a1,a2,a3=a
    b0,b1,b2,b3=b
    return sp.Matrix([
        a0*b0-a1*b1-a2*b2-a3*b3,
        a0*b1+a1*b0+a2*b3-a3*b2,
        a0*b2-a1*b3+a2*b0+a3*b1,
        a0*b3+a1*b2-a2*b1+a3*b0
    ])

basis=[
sp.Matrix([1,0,0,0]),
sp.Matrix([0,1,0,0]),
sp.Matrix([0,0,1,0]),
sp.Matrix([0,0,0,1])
]

L=[]
R=[]
for e in basis:
    L.append(sp.Matrix.hstack(*[qmul(e,b) for b in basis]))
    R.append(sp.Matrix.hstack(*[qmul(b,e) for b in basis]))

# Complex A,B represented by 16 real parameters.
ar=sp.symbols("ar0:4", real=True)
ai=sp.symbols("ai0:4", real=True)
br=sp.symbols("br0:4", real=True)
bi=sp.symbols("bi0:4", real=True)
vars=list(ar)+list(ai)+list(br)+list(bi)
a=[ar[j]+I*ai[j] for j in range(4)]
b=[br[j]+I*bi[j] for j in range(4)]

T=sp.zeros(4)
for j in range(4):
    T += a[j]*L[j]-b[j]*R[j]

def real_equations(M):
    out=[]
    for z in list(M):
        out.extend([sp.re(z),sp.im(z)])
    return out

# u(1,3)
eq_u=real_equations(sp.expand(T.H*G+G*T))
Au,_=sp.linear_eq_to_matrix(eq_u,vars)
null_u=Au.nullspace()

def op_from_param(v):
    return sp.simplify(T.subs(dict(zip(vars,v))))

def realvec(M):
    z=list(M.reshape(16,1))
    return sp.Matrix([sp.re(x) for x in z]+[sp.im(x) for x in z])

ops_u=[op_from_param(v) for v in null_u]
image_u=sp.Matrix.hstack(*[realvec(M) for M in ops_u])
assert image_u.rank()==7

# su(1,3)
tr=sp.trace(T)
eq_su=eq_u+[sp.re(tr),sp.im(tr)]
Asu,_=sp.linear_eq_to_matrix(eq_su,vars)
ops_su=[op_from_param(v) for v in Asu.nullspace()]
image_su=sp.Matrix.hstack(*[realvec(M) for M in ops_su])
assert image_su.rank()==6

J=[sp.simplify((L[j]-R[j])/2) for j in range(1,4)]
K=[sp.simplify(I*(L[j]+R[j])/2) for j in range(1,4)]
Q=I*sp.eye(4)

cand=J+K+[Q]
assert sp.Matrix.hstack(*[realvec(M) for M in cand]).rank()==7
for M in cand:
    assert sp.simplify(M.H*G+G*M)==sp.zeros(4)
for M in J+K:
    assert sp.trace(M)==0
assert sp.trace(Q)==4*I

# Exact Lorentz commutators.
for i in range(3):
    for j in range(3):
        JJ=sp.simplify(J[i]*J[j]-J[j]*J[i])
        JK=sp.simplify(J[i]*K[j]-K[j]*J[i])
        KK=sp.simplify(K[i]*K[j]-K[j]*K[i])
        rhsJJ=sp.zeros(4)
        rhsJK=sp.zeros(4)
        rhsKK=sp.zeros(4)
        for k in range(3):
            eps=sp.LeviCivita(i,j,k)
            rhsJJ += eps*J[k]
            rhsJK += eps*K[k]
            rhsKK -= eps*J[k]
        assert sp.simplify(JJ-rhsJJ)==sp.zeros(4)
        assert sp.simplify(JK-rhsJK)==sp.zeros(4)
        assert sp.simplify(KK-rhsKK)==sp.zeros(4)

# At Theta0=i e0: K_i give real spatial directions; Q gives real scalar.
theta0=I*basis[0]
for j in range(3):
    assert sp.simplify(K[j]*theta0 + basis[j+1])==sp.zeros(4,1)
assert sp.simplify(Q*theta0 + basis[0])==sp.zeros(4,1)

# Real dilation gives the canonical imaginary scalar time direction but is not u(1,3).
D=sp.eye(4)
assert D*theta0==theta0
assert sp.simplify(D.H*G+G*D-2*G)==sp.zeros(4)

print("PASS: minimal bimodule intersect u(1,3) = so(1,3) plus central u(1); traceless intersection is exactly so(1,3)")
