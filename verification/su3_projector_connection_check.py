#!/usr/bin/env python3
"""Exact local curvature-span test for the rank-three projector connection.

At n=e0 in C^4, tangent directions to CP^3 identify with C^3.
The universal quotient curvature on two tangent vectors u,v is
F(u,v)=u v^dagger - v u^dagger (up to an overall sign convention).
We verify over the reals that:
- these curvature values span u(3): rank 9;
- their traceless parts span su(3): rank 8.
"""
import sympy as sp

I=sp.I
e=[
    sp.Matrix([1,0,0]),
    sp.Matrix([0,1,0]),
    sp.Matrix([0,0,1]),
]
tangent=e+[I*x for x in e]

def F(u,v):
    return sp.simplify(u*v.conjugate().T-v*u.conjugate().T)

def realvec(M):
    out=[]
    for z in list(M):
        out.extend([sp.re(z).expand(complex=True),sp.im(z).expand(complex=True)])
    return sp.Matrix(out)

# Verify the projector-curvature formula directly at n=e0 in C^4.
n=sp.Matrix([1,0,0,0])
P4=sp.eye(4)-n*n.conjugate().T
assert P4*P4==P4
assert P4.rank()==3

def embed(u):
    return sp.Matrix([0,u[0],u[1],u[2]])

def dP(u):
    u4=embed(u)
    return -(u4*n.conjugate().T+n*u4.conjugate().T)

curv=[]
for a in range(len(tangent)):
    for b in range(a+1,len(tangent)):
        C=F(tangent[a],tangent[b])
        assert sp.simplify(C.H + C)==sp.zeros(3)
        comm=sp.simplify(dP(tangent[a])*dP(tangent[b])
                         -dP(tangent[b])*dP(tangent[a]))
        projected=sp.simplify(P4*comm*P4)
        assert sp.simplify(projected[1:4,1:4]-C)==sp.zeros(3)
        curv.append(C)

M=sp.Matrix.hstack(*[realvec(C) for C in curv])
assert M.rank()==9

I3=sp.eye(3)
traceless=[sp.simplify(C-sp.trace(C)*I3/3) for C in curv]
for C in traceless:
    assert sp.simplify(sp.trace(C))==0
    assert sp.simplify(C.H+C)==sp.zeros(3)

M0=sp.Matrix.hstack(*[realvec(C) for C in traceless])
assert M0.rank()==8

print("PASS: projector curvature spans u(3); traceless curvature spans su(3)")
