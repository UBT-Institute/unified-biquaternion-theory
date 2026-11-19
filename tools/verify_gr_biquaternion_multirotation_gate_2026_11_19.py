"""Exact full-biquaternion multi-rotation gate (research-only).

Uses faithful Mat(2,C) representation, canonical quaternion-sharp as adjugate,
and existing observer relative-information readout. This tests finite algebra,
not UBT on-shell dynamics, Born rule or an actual physical collapse.
"""
import sympy as sp

I=sp.I
eye=sp.eye(2)
sigma1=sp.Matrix([[0,1],[1,0]])
sigma2=sp.Matrix([[0,-I],[I,0]])
sigma3=sp.diag(1,-1)
sigmas=[eye,sigma1,sigma2,sigma3]
quat=[-I*x for x in sigmas[1:]]

def sharp(a):
    return sp.Matrix([[a[1,1],-a[0,1]],[-a[1,0],a[0,0]]])

def zero(a):
    return sp.simplify(a)==sp.zeros(*a.shape)

def g(a,b):
    m=(sharp(a)*b+sharp(b)*a)/2
    assert zero(m-sp.trace(m)/2*eye)
    return sp.simplify(sp.trace(m)/2)

e1,e2,e3=quat
assert zero(e1*e2-e2*e1-2*e3)
assert zero(sharp(e1)*e1-eye)
boost=sp.Rational(5,4)*eye+sp.Rational(3,4)*sigma1
assert sp.det(boost)==1 and zero(sharp(boost)*boost-eye)
assert boost.H==boost and boost.H*boost!=eye

E=[I*x for x in sigmas]
eta=sp.diag(-1,1,1,1)
assert sp.Matrix(4,4,lambda a,b:g(E[a],E[b]))==eta
L=sp.Matrix([[1,1],[0,1]])
Q=sp.diag(2,sp.Rational(1,2))
assert sp.det(L)==sp.det(Q)==1
generic=[L*x*Q for x in E]
assert sp.Matrix(4,4,lambda a,b:g(generic[a],generic[b]))==eta
assert generic[0].H!=-generic[0]

linked=[L*x*L.H for x in E]
assert all(x.H==-x for x in linked)
assert sp.Matrix(4,4,lambda a,b:g(linked[a],linked[b]))==eta

z=(1+I)/sp.sqrt(2)
complexE=[z*E[0]]+E[1:]
complexg=sp.Matrix(4,4,lambda a,b:g(complexE[a],complexE[b]))
assert complexg==sp.diag(-I,1,1,1)
assert sp.Matrix(4,4,lambda a,b:g((L*complexE[a]*Q),(L*complexE[b]*Q)))==complexg

Lg=sp.diag(2,3)
Rg=sp.diag(2,I)
trans=[Lg*x*Rg.inv() for x in complexE]
out=sp.Matrix(4,4,lambda a,b:g(trans[a],trans[b]))
assert zero(out-sp.det(Lg)/sp.det(Rg)*complexg)
assert sp.im(complexg[0,0]/complexg[1,1])==-1

Theta=sp.diag(2,I)
root=1+I
S=Theta/root
P=sp.diag(sp.sqrt(2),1/sp.sqrt(2))
U=sp.diag((1-I)/sp.sqrt(2),(1+I)/sp.sqrt(2))
assert sp.simplify(sp.det(S)-1)==0
assert zero(P*U-S)
assert zero(P*P-S*S.H)
assert zero(U*U.H-eye) and sp.simplify(sp.det(U)-1)==0
assert zero(root*P*U-Theta)
assert zero((-root)*(-S)-Theta)

rho=Theta*Theta.H/sp.trace(Theta*Theta.H)
Theta2=Theta*sigma1
assert zero(Theta2*Theta2.H-Theta*Theta.H)
D=sp.diag(1/sp.sqrt(2),sp.sqrt(2))
T=D*Theta*D
T2=D*Theta2*D
rhoN=sp.simplify(T*T.H/sp.trace(T*T.H))
rhoN2=sp.simplify(T2*T2.H/sp.trace(T2*T2.H))
assert rhoN==sp.diag(sp.Rational(1,5),sp.Rational(4,5))
assert rhoN2==sp.diag(sp.Rational(4,5),sp.Rational(1,5))

print("PASS noncommuting compact rotations versus hyperbolic biquaternion boost")
print("PASS generic two-sided SL(2,C) preserves sharp metric, not real tetrad")
print("PASS linked Lorentz congruence preserves real tetrad")
print("PASS invariant complex metric forbids phase-only real branch selection")
print("PASS GL(2,C) scales all metric entries by one determinant ratio")
print("PASS local complex scale x SL2 decomposition with Z2 sign pairing")
print("PASS observer polar phase hidden at one clock, accessible at another")
print("SCOPE: topological winding parity is analytic; no physical collapse derived")
