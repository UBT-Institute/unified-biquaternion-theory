"""Remove arbitrary 3/5 normalization from canonical Theta Berry witness.

Exact algebra for arbitrary spectral contrast. Finite kinematics only; no
fundamental coupling, quantum collapse, gravity or dynamical beta selector.
"""
import sympy as sp

I=sp.I
Id=sp.eye(2)
sx=sp.Matrix([[0,1],[1,0]])
sy=sp.Matrix([[0,-I],[I,0]])
sz=sp.diag(1,-1)
beta,lam=sp.symbols("beta lam",real=True)
P0=sp.diag(1,0)
Q0=2*P0-Id

# The original I+P is exactly a chosen value of a free amplitude.
Tlin=Id+lam*P0
rho_lin=sp.simplify(Tlin*Tlin.H/sp.trace(Tlin*Tlin.H))
den=2+2*lam+lam**2
assert sp.simplify(rho_lin-(Id+lam*(lam+2)*P0)/den)==sp.zeros(2)
assert rho_lin.subs(lam,1)==sp.diag(sp.Rational(4,5),sp.Rational(1,5))
assert sp.simplify(sp.det(Tlin)-(1+lam))==0

# Natural det-one hyperbolic/boost family.
Tb=sp.cosh(beta/2)*Id+sp.sinh(beta/2)*Q0
assert sp.simplify(sp.det(Tb)-1)==0
rb=sp.simplify(Tb*Tb.H/sp.trace(Tb*Tb.H))
pred=(Id+sp.tanh(beta)*Q0)/2
assert (rb-pred).applyfunc(lambda x:sp.simplify(x.rewrite(sp.exp)))==sp.zeros(2)
assert sp.simplify(sp.sqrt(2)*Tb.subs(beta,sp.log(2))-(Id+P0))==sp.zeros(2)
assert sp.simplify(sp.trace(rb)-1)==0

# Any nonzero real beta retains a spectral line, beta=0 destroys uniqueness.
assert rb.subs(beta,0)==Id/2
assert sp.simplify(sp.diff((pred[0,0]-pred[1,1]),beta)-1/sp.cosh(beta)**2)==0

# Explicit whole parameter sphere eigenbundle P(n): Berry curvature invariant
# under changing beta. No imaginary-time or physical spacetime coordinate used.
th,ph=sp.symbols("theta phi",real=True)
v=sp.Matrix([sp.cos(th/2),sp.exp(I*ph)*sp.sin(th/2)])
P=sp.simplify(v*v.H)
Q=2*P-Id
assert sp.simplify(P*P-P)==sp.zeros(2)
Pt=sp.diff(P,th)
Pp=sp.diff(P,ph)
F=sp.trigsimp(-I*sp.trace(P*(Pt*Pp-Pp*Pt)),method="fu")
assert sp.simplify(F-sp.sin(th)/2)==0
assert sp.integrate(sp.integrate(F,(ph,0,2*sp.pi)),(th,0,sp.pi))==2*sp.pi

# The affine single-Theta lift has the SAME canonical tetrad for all beta:
# only the field value, not its spacetime derivative, changes.
t,x,y,z=sp.symbols("t x y z",real=True)
Theta=sp.cosh(beta/2)*Id+sp.sinh(beta/2)*Q+I*(
    t*Id+x*sx+y*sy+z*sz
)
coords=[t,x,y,z]
for j,var in enumerate(coords):
    assert sp.simplify(sp.diff(Theta,var)-I*[Id,sx,sy,sz][j])==sp.zeros(2)
assert sp.simplify(sp.diff(Theta,th)-sp.sinh(beta/2)*sp.diff(Q,th))==sp.zeros(2)
# Since D_mu=partial_mu and E_mu=i sigma_mu, g=eta in locked central-sharp.
print("PASS all lambda: arbitrary 3/5 example reparameterized")
print("PASS det-one boost amplitude and rho=(I+tanh(beta)*n.sigma)/2")
print("PASS original I+P equals sqrt(2) boost at beta=log(2)")
print("PASS Chern 1 independent of beta on any gapped positive-beta slice")
print("PASS all beta have identical affine Lorentz-real first jets")
print("SCOPE beta NOT dynamically selected; no new UBT constants predicted")
