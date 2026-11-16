"""Symmetry versus physical coupling: exact symbolic checks.
A formal test of parity and action normalization, not UBT dynamics.
"""
import sympy as s
a,b,R,P,lam,J=s.symbols('a b R P lam J',real=True)
L=a*R+b*P
assert s.simplify(L.subs(P,-P)-L)==-2*b*P
assert s.solve(s.Eq(s.expand(L.subs(P,-P)-L),0),b)==[0]
# The vacuum equation from an overall curvature coefficient is proportional
# to a, but a matter source held fixed makes the relative coupling observable.
vac=a*R
coupled=a*R+J
assert s.diff(vac,R)==a
assert s.simplify(s.diff(coupled,R)/s.diff(coupled,J)-a)==0
assert s.diff(L,a)==R
print("PASS: parity selects b=0; a remains free and is not an additive gauge constant")
