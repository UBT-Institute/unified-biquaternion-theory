"""Derive quadratic observer response from additive unresolved channels.

Finite exact checks for the conditional proof. The functional equation
h(x+y)=h(x)+h(y), h>=0 => h(s)=c*s is proved analytically in the companion
research note, not inferred from finitely many test cases.
"""
import sympy as s

I=s.I
c=s.symbols("c",positive=True,real=True)
v=s.Matrix([2,I])
norm2=s.simplify((v.H*v)[0])
assert norm2==5
U=s.Matrix([[s.sqrt(2)/2,s.sqrt(2)/2],
            [-s.sqrt(2)/2,s.sqrt(2)/2]])
assert s.simplify(U.T*U-s.eye(2))==s.zeros(2)
T=v*s.Matrix([[1,0]])
Tmix=T*U
assert s.simplify(Tmix*Tmix.H-T*T.H)==s.zeros(2)

def channel(v,p):
    norm=s.simplify((v.H*v)[0])
    if norm==0:
        return s.zeros(2)
    return s.simplify(norm**(p-1)*v*v.H)

def aggregate(T,p):
    return s.simplify(channel(T[:,0],p)+channel(T[:,1],p))

assert s.simplify(aggregate(T,1)-T*T.H)==s.zeros(2)
assert s.simplify(aggregate(Tmix,1)-T*T.H)==s.zeros(2)
assert s.simplify(aggregate(Tmix,2)-aggregate(T,2)/2)==s.zeros(2)
assert s.simplify(aggregate(Tmix,2)-aggregate(T,2))!=s.zeros(2)

# A right-unitary-invariant nonlinear Gram POWER map is not additive by columns:
pow2=lambda m:s.simplify((m*m.H)*(m*m.H))
assert s.simplify(pow2(Tmix)-pow2(T))==s.zeros(2)
assert s.simplify(pow2(T)-aggregate(T,2))==s.zeros(2)
assert s.simplify(pow2(Tmix)-aggregate(Tmix,2))!=s.zeros(2)

# For an unresolved column q(v)=h(||v||²) P_v, right-basis rotations of
# [v,0] into [sqrt(x/s)v,sqrt(y/s)v] force h(x+y)=h(x)+h(y).
# Positivity -> monotonicity -> h(s)=c*s without continuity assumptions.
x,y=s.symbols("x y",positive=True,real=True)
hlin=lambda t:c*t
assert s.simplify(hlin(x+y)-hlin(x)-hlin(y))==0
hpow=lambda t:t*t
assert s.simplify(hpow(x+y)-hpow(x)-hpow(y))==2*x*y

print("PASS: quadratic channel rule independent of unresolved basis")
print("PASS: nonlinear degree-four responses violate column additivity")
print("PASS: positivity + Cauchy channel identity selects quadratic intensity")
print("SCOPE: UBT physical channel additivity and observer effects remain OPEN")
