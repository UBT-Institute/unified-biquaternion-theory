#!/usr/bin/env python3
"""Exact stationary vacuum and 8-real Hessian of the classified quartic."""
import sympy as s
x=s.symbols("x0:4",real=True); y=s.symbols("y0:4",real=True)
r,m2,l1,l2=s.symbols("r m2 lambda1 lambda2",real=True)
z=[x[j]+s.I*y[j] for j in range(4)]
H=2*sum(([1,-1,-1,-1][j])*(x[j]**2+y[j]**2) for j in range(4))
det=sum(t*t for t in z)
V=m2*H+l1*H**2+l2*s.expand(det*s.conjugate(det))
q=list(x)+list(y); vacuum={a:0 for a in q};vacuum[y[0]]=r
grad=[s.factor(s.diff(V,t).subs(vacuum)) for t in q]
expected_grad=[0,0,0,0,4*r*(m2+(4*l1+l2)*r**2),0,0,0]
# Compare polynomial identities, not SymPy's choice of factored expression tree.
assert all(s.expand(actual-expected)==0 for actual,expected in zip(grad,expected_grad))
hess=s.hessian(V,q).subs(vacuum).subs(m2,-(4*l1+l2)*r**2).applyfunc(s.simplify)
expect=s.diag(0,0,0,0,8*r**2*(4*l1+l2),8*r**2*l2,8*r**2*l2,8*r**2*l2)
assert hess==expect
G=s.diag(2,-2,-2,-2,2,-2,-2,-2)
assert s.simplify((G.inv()*hess)[5,5])==-4*l2*r*r
print("stationarity: m²+(4 lambda1+lambda2)r²=0")
print("vacuum Hessian: 4 zeros, 1 radial, 3 transverse positive potential curvatures")
print("generalized mass² for three nongauge negative-kinetic directions=-4 lambda2 r²")
