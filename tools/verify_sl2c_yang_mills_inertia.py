#!/usr/bin/env python3
"""Exact 6x6 invariant gauge kinetic matrix; independent of full ADM analysis."""
import sympy as s
i=s.I
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-i],[i,0]]),s.diag(1,-1)]
T=[i*p/2 for p in pauli]+[p/2 for p in pauli]
R=s.Matrix(6,6,lambda a,b:s.re(s.trace(T[a]*T[b])).expand(complex=True))
Q=s.Matrix(6,6,lambda a,b:s.im(s.trace(T[a]*T[b])).expand(complex=True))
assert R==s.diag(-s.Rational(1,2),-s.Rational(1,2),-s.Rational(1,2),s.Rational(1,2),s.Rational(1,2),s.Rational(1,2))
assert Q==s.Matrix.vstack(s.Matrix.hstack(s.zeros(3),s.eye(3)/2),s.Matrix.hstack(s.eye(3)/2,s.zeros(3)))
a,b=s.symbols("a b",real=True)
G=a*R+b*Q
assert s.simplify(G*G-(a*a+b*b)*s.eye(6)/4)==s.zeros(6)
assert s.factor(G.det())==-(a*a+b*b)**3/64
print("R inertia (3,3); Q mixes boosts with rotations")
print("G(alpha,beta) eigenvalues +/-sqrt(alpha**2+beta**2)/2, each multiplicity 3")
print("for (alpha,beta)!=(0,0): inertia (3,3)")
print("This checks the internal quadratic form, NOT a full Dirac constraint algebra.")
