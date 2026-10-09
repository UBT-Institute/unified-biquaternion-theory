#!/usr/bin/env python3
"""Exact checks for the SU(1,3)-enhanced lambda_2=0 potential branch."""
import sympy as sp

# Complex biquaternion coefficients in real variables.
x=sp.symbols("x0:8", real=True)
z0=x[0]+sp.I*x[1]
z1=x[2]+sp.I*x[3]
z2=x[4]+sp.I*x[5]
z3=x[6]+sp.I*x[7]

X=sp.Matrix([
    [z0+sp.I*z1, z2+sp.I*z3],
    [-z2+sp.I*z3, z0-sp.I*z1]
])
a,b,c,d=X[0,0],X[0,1],X[1,0],X[1,1]
H=sp.expand_complex(2*sp.re(a*sp.conjugate(d))-abs(b)**2-abs(c)**2)
HB=2*(sp.expand_complex(z0*sp.conjugate(z0))
      -sp.expand_complex(z1*sp.conjugate(z1))
      -sp.expand_complex(z2*sp.conjugate(z2))
      -sp.expand_complex(z3*sp.conjugate(z3)))
assert sp.simplify(H-HB)==0

# Same h_B norm, different determinant norm: q=(1,0,0,0), q'=(sqrt2,1,0,0).
subs1={x[0]:1,x[1]:0,x[2]:0,x[3]:0,x[4]:0,x[5]:0,x[6]:0,x[7]:0}
subs2={x[0]:sp.sqrt(2),x[1]:0,x[2]:1,x[3]:0,x[4]:0,x[5]:0,x[6]:0,x[7]:0}
detnorm=sp.expand_complex(sp.det(X)*sp.conjugate(sp.det(X)))
assert sp.simplify(H.subs(subs1)-H.subs(subs2))==0
assert sp.simplify(detnorm.subs(subs1)-1)==0
assert sp.simplify(detnorm.subs(subs2)-9)==0

# lambda2=0, lambda1=1, choose r=1 => mu=-4 so H*=2.
V=-4*H+H**2
vac={x[0]:1,x[1]:0,x[2]:0,x[3]:0,x[4]:0,x[5]:0,x[6]:0,x[7]:0}
grad=sp.Matrix([sp.diff(V,t) for t in x]).subs(vac)
assert grad==sp.zeros(8,1)
Hess=sp.hessian(V,x).subs(vac)
assert Hess.rank()==1
assert len(Hess.nullspace())==7

# Add determinant term with the existing vacuum tuning lambda1=lambda2=r=1:
# mu=-(4 lambda1 + lambda2)=-5.  The known pointwise Hessian has rank 4.
V2=-5*H+H**2+detnorm
Hess2=sp.hessian(V2,x).subs(vac)
assert Hess2.rank()==4
assert len(Hess2.nullspace())==4

print("PASS: H=2 h_B; lambda2=0 gives a rank-1 Hessian with 7-dimensional timelike coset vacuum, while lambda2>0 lifts three directions")
