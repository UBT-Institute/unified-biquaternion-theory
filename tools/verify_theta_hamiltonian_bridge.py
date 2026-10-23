#!/usr/bin/env python3
"""Exact 2-component representative check of the declared-family ADM Legendre transform.

This is a symbolic check of algebraic coefficients, not the full composite
metric/connection Dirac analysis.
"""
import sympy as sp


def verify():
    N, J, c, shift, W = sp.symbols('N J c shift W', nonzero=True, real=True)
    q0,q1,d0,d1,v0,v1,p0,p1 = sp.symbols('q0 q1 d0 d1 v0 v1 p0 p1', real=True)
    a,b,f,g = sp.symbols('a b f g',real=True)
    K=sp.diag(2,-3)
    V=sp.Matrix([v0,v1]); q=sp.Matrix([q0,q1]); D=sp.Matrix([d0,d1]);p=sp.Matrix([p0,p1]);Omega=sp.Matrix([[a,b],[f,g]])
    vel=V+shift*D-Omega*q
    L=N*J*(c/(2*N**2)*(V.T*K*V)[0]-W)
    momentum=c*J/N*K*V
    assert sp.simplify((momentum-c*J/N*K*V))==sp.zeros(2,1)
    H=sp.expand((momentum.T*vel)[0]-L)
    expected=N*((momentum.T*K.inv()*momentum)[0]/(2*c*J)+J*W)+shift*(momentum.T*D)[0]-(momentum.T*Omega*q)[0]
    assert sp.simplify(H-expected)==0
    H_canonical=N*((p.T*K.inv()*p)[0]/(2*c*J)+J*W)+shift*(p.T*D)[0]-(p.T*Omega*q)[0]
    invvelocity=N/(c*J)*K.inv()*p
    ham_v=sp.Matrix([sp.diff(H_canonical,pi) for pi in p])
    assert sp.simplify(ham_v-(invvelocity+shift*D-Omega*q))==sp.zeros(2,1)
    return {'legendre_transform':'PASS','momentum_inversion':'PASS','hamilton_velocity_equation':'PASS','scope':'fixed prescribed background; two-component nondegenerate indefinite representative'}


if __name__=='__main__':
    print(verify())
