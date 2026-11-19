"""Reverse-engineer a conditional quantum density from single full Theta.

Exact algebra checks. These are NOT a derivation of quantum measurement or Born
weights from the unfinished fundamental UBT action.
"""
import sympy as s

I=s.I
Id=s.eye(2)
sx=s.Matrix([[0,1],[1,0]])
sy=s.Matrix([[0,-I],[I,0]])
sz=s.diag(1,-1)
sigma=[Id,sx,sy,sz]
eta=s.diag(-1,1,1,1)
sharp=lambda A:s.Matrix([[A[1,1],-A[0,1]],[-A[1,0],A[0,0]]])
metric=lambda E:s.Matrix(4,4,lambda a,b:s.simplify(s.trace(
    (sharp(E[a])*E[b]+sharp(E[b])*E[a])/2)/2))
rho=lambda T:s.simplify(T*T.H/s.trace(T*T.H))

# One full complex biquaternion: the observer-Gram tensor is positive.
a,b,c,d,e,f,g,h=s.symbols("a b c d e f g h",real=True)
T=s.Matrix([[a+I*b,c+I*d],[e+I*f,g+I*h]])
Q=s.simplify(T*T.H)
assert s.simplify(Q-Q.H)==s.zeros(2)
assert s.simplify(Q.det()-s.det(T)*s.conjugate(s.det(T)))==0
assert s.simplify(s.trace(Q)-sum(x*x for x in [a,b,c,d,e,f,g,h]))==0
K=s.Matrix([[s.Rational(3,5),I*s.Rational(4,5)],[0,1]])
assert s.simplify(s.trace(Q*K.H*K)-s.trace((K*T).H*(K*T)))==0

# Unique trace representation is finite-dimensional linear algebra.
state=s.Matrix([[s.Rational(2,5),s.Rational(1,5)+I*s.Rational(1,10)],
                [s.Rational(1,5)-I*s.Rational(1,10),s.Rational(3,5)]])
assert s.trace(state)==1 and state.det()>0
for j in range(2):
    for k in range(2):
        E=s.Matrix(2,2,lambda r,t:int(r==j and t==k))
        assert s.trace(state*E)==state[k,j]

# Equivariant local (1,1)-quadratic response general form:
# Q_AB(T)=A TTdag+B tr(TTdag)I. The support axiom kills B.
A,B=s.symbols("A B",real=True)
Trank=s.diag(1,0)
Pempty=s.diag(0,1)
QAB=A*Trank*Trank.H+B*s.trace(Trank*Trank.H)*Id
assert s.simplify(s.trace(Pempty*QAB)-B)==0
assert s.solve(s.Eq(s.trace(Pempty*QAB),0),B)==[0]
# Rank-one purity alone is not enough: an orthogonal complement survives.
assert s.trace(Trank*Trank.H)*Id-Trank*Trank.H==Pempty

# Observer-frame covariance, right-unitary basis blindness.
U=(Id+I*sx)/s.sqrt(2)
V=s.diag(I,-I)
T0=s.Matrix([[1+I,2],[I,3-I]])
assert s.simplify(rho(U*T0*V)-U*rho(T0)*U.H)==s.zeros(2)
H=s.diag(2,s.Rational(1,2))
S=H*U
Np=S*S.H
Nm=s.diag(s.Rational(1,2),2)
assert s.det(S)==1
assert s.simplify(Nm*Np*Nm-Id)==s.zeros(2)
assert s.simplify(Nm*S*T0*S.H*Nm-U*T0*U.H)==s.zeros(2)

# Higher powers satisfy positivity, support and unitary covariance but
# give different probabilities. Thus quadraticity is an additional principle.
D=s.diag(2,1)
W=D*D.H
assert W/s.trace(W)==s.diag(s.Rational(4,5),s.Rational(1,5))
assert (W*W)/s.trace(W*W)==s.diag(s.Rational(16,17),s.Rational(1,17))

# The canonical quaternion sharp is NOT the observer's positive dagger.
Z=s.diag(1,I)
assert sharp(Z)*Z==I*Id
assert sharp(Z)*Z != (sharp(Z)*Z).H

# Mixed->pure candidate local readout can coexist with SAME regular
# canonical real tetrad: no physical quantum collapse has been derived.
t,x,y,z,lam=s.symbols("t x y z lambda",real=True)
Theta=s.diag(1,lam)+I*(t*Id+x*sx+y*sy+z*sz)
E=[s.diff(Theta,q) for q in [t,x,y,z]]
assert all(E[k]==I*sigma[k] for k in range(4))
assert metric(E)==eta and s.det(metric(E))==-1
Torigin=Theta.subs({t:0,x:0,y:0,z:0})
assert s.simplify(rho(Torigin)-s.diag(1,lam**2)/(1+lam**2))==s.zeros(2)
assert rho(Torigin).subs(lam,1)==Id/2
assert rho(Torigin).subs(lam,0)==s.diag(1,0)
assert s.simplify(s.det(Torigin)-lam)==0

# Nonlinear p-Born alternatives have the SAME eigenprojector / Berry Chern
# on the nondegenerate observer parameter sphere; topology does not pick p.
beta=s.symbols("beta",positive=True,real=True)
n=s.symbols("n",real=True)
P0=s.diag(1,0)
Gbeta=s.diag(s.exp(beta),s.exp(-beta))
rho_beta=Gbeta/s.trace(Gbeta)
rho_beta2=Gbeta*Gbeta/s.trace(Gbeta*Gbeta)
assert (rho_beta-(Id+s.tanh(beta)*(2*P0-Id))/2).applyfunc(lambda z:s.simplify(z.rewrite(s.exp)))==s.zeros(2)
assert (rho_beta2-(Id+s.tanh(2*beta)*(2*P0-Id))/2).applyfunc(lambda z:s.simplify(z.rewrite(s.exp)))==s.zeros(2)
assert s.simplify(rho_beta[0,0]-rho_beta2[0,0])!=0

print("PASS: positivity, normalized trace, observer covariance and support gate")
print("PASS: pure-rank complement and nonlinear-power uniqueness counterexamples")
print("PASS: sharp-vs-dagger distinction and rank-one Theta value with regular metric")
print("OPEN: operational effect algebra, quadratic principle and Born law from Theta dynamics")
