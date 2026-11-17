"""Exact finite-dimensional check of the implicit-composite chain rule.
This toy validates the algebra only; it is not the canonical UBT functional
derivative, connection reconstruction or an infinite-dimensional inverse.
"""
import sympy as s

x,y,k = s.symbols("x y k", real=True)
a,b,c,d,e = s.symbols("a b c d e", real=True)
# Implicit jet y = a*x + b*y + c*k and a general quadratic action.
jet = a*x + b*y + c*k
action = s.Rational(1,2)*d*y**2 + e*x*y + s.Rational(1,2)*k**2
A = 1-b
ystar = (a*x+c*k)/A
red = action.subs(y,ystar)
indep_x = s.diff(action,x)
indep_y = s.diff(action,y)
indep_k = s.diff(action,k)
for variable, direct, Jvar in [(x,indep_x,a),(k,indep_k,c)]:
    reduced_derivative = s.diff(red,variable)
    implicit_chain = (direct + Jvar*indep_y/A).subs(y,ystar)
    assert s.simplify(reduced_derivative-implicit_chain)==0
# The inverse fails at b=1; consistency requires a*x+c*k=0.
assert s.simplify((y-jet).subs(b,1)) == -a*x-c*k
print("PASS: implicit Schur complement and singular compatibility")
