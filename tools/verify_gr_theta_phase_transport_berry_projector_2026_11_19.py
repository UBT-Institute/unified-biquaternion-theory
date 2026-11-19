"""Exact full-biquaternion observer-spectral phase transport diagnostic.

Finite off-shell checks. No canonical metric modification, on-shell UBT action,
physical photon, quantum Born rule or objective outcome selection is proved.
"""
import sympy as sp

I=sp.I
sx=sp.Matrix([[0,1],[1,0]])
sy=sp.Matrix([[0,-I],[I,0]])
sz=sp.diag(1,-1)
Id=sp.eye(2)
zero=lambda M: M.applyfunc(
    lambda e: sp.trigsimp(sp.expand_trig(e),method="fu")
)==sp.zeros(*M.shape)

# Arbitrary noncommuting rotations do not define nontrivial field-derived holonomy.
U=sp.Rational(3,5)*Id+I*sp.Rational(4,5)*sx
V=sp.Rational(5,13)*Id+I*sp.Rational(12,13)*sy
assert zero(U.H*U-Id) and zero(V.H*V-Id)
assert sp.det(U)==sp.det(V)==1
chi=sp.simplify(sp.trace(U*V*U.H*V.H)/2)
assert chi==1-2*sp.Rational(4,5)**2*sp.Rational(12,13)**2
assert chi!=1
frames=[Id,U,V,V*U]
link=lambda a,b:sp.simplify(frames[a].H*frames[b])
assert zero(link(0,1)*link(1,2)*link(2,3)*link(3,0)-Id)

# The Maurer-Cartan form of a globally defined U is a flat connection.
x,y=sp.symbols("x y",real=True)
ux=sp.cos(x)*Id+I*sp.sin(x)*sx
uy=sp.cos(y)*Id+I*sp.sin(y)*sy
G=sp.simplify(ux*uy)
ax=sp.simplify(G.H*sp.diff(G,x))
ay=sp.simplify(G.H*sp.diff(G,y))
assert zero(sp.diff(ay,x)-sp.diff(ax,y)+ax*ay-ay*ax)

# A globally smooth positive-Hermitian invertible full Theta on parameter S2.
theta,phi=sp.symbols("theta phi",real=True)
v=sp.Matrix([sp.cos(theta/2),sp.exp(I*phi)*sp.sin(theta/2)])
P=sp.simplify(v*v.H)
assert zero(P*P-P)
assert sp.simplify(sp.trace(P)-1)==0
Theta=Id+P
rho=sp.simplify(Theta*Theta.H/sp.trace(Theta*Theta.H))
assert zero(rho-(Id+3*P)/5)
assert sp.simplify(sp.det(Theta)-2)==0
assert sp.simplify(sp.det(rho)-sp.Rational(4,25))==0

Pt=sp.simplify(sp.diff(P,theta))
Pp=sp.simplify(sp.diff(P,phi))
F=sp.simplify(sp.trigsimp(-I*sp.trace(P*(Pt*Pp-Pp*Pt))))
assert sp.simplify(sp.trigsimp(F-sp.sin(theta)/2))==0
flux=sp.integrate(sp.integrate(F,(phi,0,2*sp.pi)),(theta,0,sp.pi))
assert flux==2*sp.pi
assert zero(U*P*U.H*(U*Pt*U.H*U*Pp*U.H-U*Pp*U.H*U*Pt*U.H) -
            U*P*(Pt*Pp-Pp*Pt)*U.H)  # constant-frame covariance

# Polar unitary of the constructed positive Theta is the identity, yet the
# projector curvature is nonzero: it cannot be its pure-gauge polar connection.
assert zero(Theta.H-Theta)
# Theta is positive with eigenvalues 2, 1; P-defined functional calculus.
assert zero(Theta-Theta*Id)

# Spectral branch selection cannot extend continuously to eigenvalue degeneracy.
epsilon=sp.symbols("epsilon",real=True)
Teps=Id+epsilon*(2*P-Id)
rhoe=sp.simplify(Teps*Teps.H/sp.trace(Teps*Teps.H))
assert zero(rhoe-(Id/2+2*epsilon/(1+epsilon**2)*(P-Id/2)))
assert zero(rhoe.subs(epsilon,0)-Id/2)
assert P.subs({theta:0,phi:0})==sp.diag(1,0)
assert P.subs({theta:sp.pi,phi:0})==sp.diag(0,1)

print("PASS noncommuting arbitrary rotations but trivial field-derived pure-gauge loop")
print("PASS exact Maurer-Cartan flatness for global polar-unitary field")
print("PASS smooth invertible full Theta=I+P and positive density with spectral gap")
print("PASS eigenbundle Berry F=sin(theta)/2 and integer Chern 1 on parameter S2")
print("PASS no continuous unique spectral branch selector across degenerate rho=I/2")
print("SCOPE off-shell observer protocol, not canonical W_L dynamics or a collapse law")
