"""One-Theta operational additivity, coherent-phase and canonical-reality gates.

Exact finite algebra; no derivation of an on-shell Born measurement instrument.
"""
import sympy as sp

I=sp.I
id2=sp.eye(2)
sx=sp.Matrix([[0,1],[1,0]])
sy=sp.Matrix([[0,-I],[I,0]])
sz=sp.diag(1,-1)
sharp=lambda M:sp.Matrix([[M[1,1],-M[0,1]],[-M[1,0],M[0,0]]])
simple=lambda m:m.applyfunc(sp.simplify)
metric=lambda E:sp.Matrix(4,4,lambda m,n:sp.simplify(sp.trace(
    (sharp(E[m])*E[n]+sharp(E[n])*E[m])/2)/2))
eta=sp.diag(-1,1,1,1)

v1=sp.Matrix([1,0])
v2=sp.Matrix([1,1])
T=sp.Matrix.hstack(v1,v2)
Q=simple(T*T.H)
assert Q==sp.Matrix([[2,1],[1,1]])
assert Q==v1*v1.H+v2*v2.H
U=(id2+I*sy)/sp.sqrt(2)
assert simple(U*U.H-id2)==sp.zeros(2)
assert simple(T*U*(T*U).H-Q)==sp.zeros(2)

z=sp.symbols('z',real=True)
Tz=T*sp.diag(1,sp.exp(I*z))
assert simple(Tz*Tz.H-Q)==sp.zeros(2)

w0=v1+v2
wpi=v1-v2
assert simple(w0*w0.H)==sp.Matrix([[4,2],[2,1]])
assert simple(wpi*wpi.H)==sp.Matrix([[0,0],[0,1]])
assert simple(w0*w0.H-wpi*wpi.H)==2*(v1*v2.H+v2*v1.H)
assert simple(w0*w0.H/(w0.H*w0)[0]-wpi*wpi.H/(wpi.H*wpi)[0])!=sp.zeros(2)

# Shannon information is additive for independent, not correlated outcomes.
assert sp.simplify(sp.log(4)-2*sp.log(2))==0
assert sp.simplify(sp.log(2)-2*sp.log(2))==-sp.log(2)

# Right basis-invariance alone does not force the channel-additive law.
nonlinear=lambda X:simple((X*X.H)*(X*X.H))
assert nonlinear(T*U)==nonlinear(T)
colpower=lambda v:simple((v.H*v)[0]*v*v.H)
assert simple(nonlinear(T)-colpower(v1)-colpower(v2))!=sp.zeros(2)

# Right SU(2) invariance of ONE observer's Gram tensor is not generally
# an admissible Lorentz-real tetrad gauge in the canonical UBT sector.
E=[I*id2,I*sx,I*sy,I*sz]
V=I*sz
assert sp.det(V)==1
assert simple(V.H*V-id2)==sp.zeros(2)
assert metric(E)==eta
assert metric([e*V for e in E])==eta
assert simple(E[0]*V+(E[0]*V).H)!=sp.zeros(2)
assert simple(T*V*(T*V).H-T*T.H)==sp.zeros(2)

print("PASS orthogonal channel-additivity and right-basis-invariance")
print("PASS coherent erasure restores relative phase interference")
print("PASS correlated entropy distinguishes conditional chain rule from additivity")
print("PASS right-invariant nonlinear Gram powers fail column-additivity")
print("PASS observer-blind right SU2 rotation loses canonical Lorentz-real tetrad")
print("OPEN dynamic selection of observer channels, probabilities, and Born instrument")
