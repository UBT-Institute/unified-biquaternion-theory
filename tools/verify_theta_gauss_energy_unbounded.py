#!/usr/bin/env python3
"""Exact Gauss constraints and negative energy on a family of momenta."""
import sympy as s
I=s.I
r,lam=s.symbols("r lam",real=True,nonzero=True)
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
T=[I*z/2 for z in pauli]+[z/2 for z in pauli]
X0=I*r*s.eye(2)
def coords(M):
    # z0=Tr(X)/2, zj=Tr(X*sigma_j)/(2i)
    zs=[s.trace(M)/2]+[s.trace(M*p)/(2*I) for p in pauli]
    return s.Matrix([s.expand_complex(s.re(z)) for z in zs]+[s.expand_complex(s.im(z)) for z in zs])
orb=s.Matrix.hstack(*(coords(t*X0+X0*t.conjugate().T) for t in T))
p=s.zeros(8,1);p[7]=lam
assert orb.rank()==3
assert p.T*orb==s.zeros(1,6)
G=s.diag(2,-2,-2,-2,2,-2,-2,-2)
energy=s.simplify((p.T*G.inv()*p)[0]/2)
assert energy==-lam**2/4
print("Exact Gauss charges:",list(p.T*orb))
print("Kinetic Hamiltonian density:",energy)
print("Unbounded below for real lambda on Gauss constraint surface")
