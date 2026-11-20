#!/usr/bin/env python3
"""Deterministic standard-library checks; numerical sanity, not proof of UBT."""
import math
import random

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def check_qubit():
    rng=random.Random(20261120)
    for _ in range(2000):
        s=[rng.uniform(-1,1) for i in range(3)]
        radius=math.sqrt(dot(s,s))
        if radius>1: s=[x/radius*rng.random() for x in s]
        a=[rng.uniform(-2,2) for i in range(3)]
        b=[rng.uniform(-2,2) for i in range(3)]
        c=cross(a,b)
        va=dot(a,a)-dot(a,s)**2
        vb=dot(b,b)-dot(b,s)**2
        cov=dot(a,b)-dot(a,s)*dot(b,s)
        lhs=va*vb-cov**2
        rhs=dot(c,s)**2+(1-dot(s,s))*dot(c,c)
        assert abs(lhs-rhs)<1e-9*(1+abs(lhs)+abs(rhs)), (lhs,rhs)
        assert rhs+1e-10>=0
    return "qubit: 2000 identity checks passed"

def check_hermitian():
    for t in [0,0.2,0.7,1.3]:
        n=[math.cosh(t),1j*math.sinh(t),0j]
        bilinear=sum(x*x for x in n)
        hermitian=sum(abs(x)**2 for x in n)
        assert abs(bilinear-1)<1e-10
        assert abs(hermitian-math.cosh(2*t))<1e-10
        assert hermitian>=1
    return "Hermitian: SO(3,C) norm counterexample verified"

def check_lorentz_congruence():
    # Diagonal invertible tetrads provide exact eigenvalue-sign checks;
    # general case follows by Sylvester inertia theorem, NOT this sampling.
    rng=random.Random(19)
    for _ in range(500):
        diag=[rng.choice([-1,1])*rng.uniform(0.1,3) for i in range(4)]
        metric_diag=[diag[0]**2]+[-x*x for x in diag[1:]]
        assert sum(x>0 for x in metric_diag)==1
        assert sum(x<0 for x in metric_diag)==3
    return "signature: 500 Lorentz-slice tautology checks passed"

if __name__=="__main__":
    for check in (check_lorentz_congruence,check_hermitian,check_qubit):
        print(check())
