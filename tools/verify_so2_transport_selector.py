#!/usr/bin/env python3
"""SO(2) one-form selector and exact transport compatibility in an adapted frame."""
import sympy as s
J=s.zeros(4);J[2,3]=1;J[3,2]=-1
eta=s.diag(-1,1,1,1)
a,b,f2,f3=s.symbols("a b f2 f3",real=True)
u=s.Matrix([0,0,a,b]); z=J*u
Delta=s.Matrix([0,0,f2,f3])
num=(z.T*eta*Delta)[0]; den=(z.T*eta*z)[0]
assert s.simplify(den-a*a-b*b)==0
alpha=s.factor(num/den)
residual=(Delta-alpha*z).applyfunc(s.factor)
assert all(s.factor((r*(a*a+b*b)))==0 for r in residual) == False
# All residuals vanish iff the 2D scalar wedge vanishes.
assert s.factor(residual[2]*(a*a+b*b))==s.factor(a*(a*f2+b*f3))
assert s.factor(residual[3]*(a*a+b*b))==s.factor(b*(a*f2+b*f3))
good=s.Matrix([0,0,-b,a])*s.symbols("lambda",real=True)
ag=s.factor((z.T*eta*good)[0]/den)
assert s.simplify((good-ag*z))==s.zeros(4,1)
print("selected alpha=",alpha)
print("compatibility requires Delta parallel to J u; projected component alone insufficient")
