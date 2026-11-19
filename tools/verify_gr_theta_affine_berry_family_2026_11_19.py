"""Exact affine canonical-Lorentz lift of observer eigenbundle parameter family.

Research C_working. Independent parameter labels do not add spacetime
coordinates or independent fields. No common UBT on-shell action is derived.
"""
import sympy as s

I=s.I
sig=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
zeros=lambda m:m.applyfunc(
    lambda e:s.trigsimp(s.expand_trig(e),method="fu")
)==s.zeros(*m.shape)
sharp=lambda a:s.Matrix([[a[1,1],-a[0,1]],[-a[1,0],a[0,0]]])
def g(E):
    return s.Matrix(4,4,lambda m,n:s.simplify(
        s.trace((sharp(E[m])*E[n]+sharp(E[n])*E[m])/2)/2
    ))

t,x,y,z,th,ph=s.symbols("t x y z theta phi",real=True)
v=s.Matrix([s.cos(th/2),s.exp(I*ph)*s.sin(th/2)])
P=s.simplify(v*v.H)
coords=[t,x,y,z]
Theta=s.eye(2)+P+I*sum((q*sig[a] for a,q in enumerate(coords)),s.zeros(2))
E=[s.simplify(s.diff(Theta,q)) for q in coords]
assert all(zeros(E[a]-I*sig[a]) for a in range(4))
assert all(zeros(E[a].H+E[a]) for a in range(4))
eta=s.diag(-1,1,1,1)
assert g(E)==eta
assert s.det(g(E))==-1
assert all(zeros(s.diff(E[m],q)) for m in range(4) for q in coords)

Theta0=s.simplify(Theta.subs({q:0 for q in coords}))
assert zeros(Theta0-s.eye(2)-P)
assert s.simplify(s.det(Theta0)-2)==0
rho0=s.simplify(Theta0*Theta0.H/s.trace(Theta0*Theta0.H))
assert zeros(rho0-(s.eye(2)+3*P)/5)
pt=s.diff(P,th)
pp=s.diff(P,ph)
F=s.trigsimp(-I*s.trace(P*(pt*pp-pp*pt)),method="fu")
assert s.simplify(F-s.sin(th)/2)==0
assert s.integrate(s.integrate(F,(ph,0,2*s.pi)),(th,0,s.pi))==2*s.pi
assert s.simplify(s.diff(Theta,th)-s.diff(P,th))==s.zeros(2)

print("PASS: full original Theta produces Lorentz-real canonical tetrad for every S2 label")
print("PASS: entire label family has the same nondegenerate Minkowski geometry")
print("PASS: field-value observer spectral line at x=0 has Chern number +1")
print("SCOPE: on-shell action, phase connection, physical collapse and Born rule OPEN")
