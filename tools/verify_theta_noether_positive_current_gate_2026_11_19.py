"""Noether-versus-positive observer current for full biquaternion Theta.

Exact algebra in off-shell flat comparator sectors. Not a physical UBT
action, photon, selected Dirac limit, or measurement/quantum collapse proof.
"""
import sympy as s

I=s.I
one=s.eye(2)
sx=s.Matrix([[0,1],[1,0]])
sy=s.Matrix([[0,-I],[I,0]])
sz=s.diag(1,-1)
eta=s.diag(-1,1,1,1)
sharp=lambda A:s.Matrix([[A[1,1],-A[0,1]],[-A[1,0],A[0,0]]])
metric=lambda E:s.Matrix(4,4,lambda j,k:s.simplify(s.trace(
    (sharp(E[j])*E[k]+sharp(E[k])*E[j])/2)/2))
simp=lambda M:M.applyfunc(s.simplify)
t,m,w,lam=s.symbols("t m w lambda",real=True,positive=True)
B=s.diag(2,1)
norm=s.trace(B.H*B)
assert norm==5

def j0(T):
    return s.simplify(I*s.trace(T.H*s.diff(T,t)-s.diff(T.H,t)*T))

# Lorentz-scalar Klein-Gordon comparator: opposite frequencies, same Q>0.
Tplus=s.exp(-I*m*t)*B
Tminus=s.exp(I*m*t)*B
Tsum=s.simplify(Tplus+Tminus)
assert s.simplify(j0(Tplus)-2*m*norm)==0
assert s.simplify(j0(Tminus)+2*m*norm)==0
assert s.simplify(j0(Tsum))==0
assert s.simplify(s.diff(s.trace(Tsum.H*Tsum),t)+4*m*s.sin(2*m*t)*norm)==0
assert s.simplify(s.diff(j0(Tplus),t))==0
assert s.simplify(s.diff(j0(Tminus),t))==0

# A scalar central phase is not a physical symmetry of the locked sharp
# geometry: g has phase weight TWO and physical W_L only allows signs.
E=[I*one,I*sx,I*sy,I*sz]
assert metric(E)==eta
phase=s.exp(I*s.pi/4)
assert simp(metric([phase*e for e in E])-I*eta)==s.zeros(4)
assert simp((phase*E[0]).H+phase*E[0])!=s.zeros(2)

# The simple positive unitary information evolution is a *comparator*:
# h=i dot T = H T with H=H^dag gives constant tr(Q) and constant purity.
U=s.cos(w*t)*one-I*s.sin(w*t)*sx
assert simp(U.H*U-one)==s.zeros(2)
assert s.simplify(s.det(U)-1)==0
TT=s.simplify(U*B)
Q=s.simplify(TT*TT.H)
Q0=B*B.H
assert s.simplify(s.trace(Q)-5)==0
assert s.simplify(s.trace(Q*Q)-17)==0
assert s.simplify(s.det(Q)-4)==0
assert simp(s.diff(Q,t)+I*w*(sx*Q-Q*sx))==s.zeros(2)
assert s.simplify(s.trace((Q/5)*(Q/5))-s.Rational(17,25))==0

# Linked conjugation preserves Lorentz-real tetrads at every t;
# merely multiplying from the LEFT does not.
congr=[s.simplify(U*e*U.H) for e in E]
assert all(simp(e+e.H)==s.zeros(2) for e in congr)
assert simp(metric(congr)-eta)==s.zeros(4)
left=[s.simplify(U*e) for e in E]
assert simp(metric(left)-eta)==s.zeros(4)
assert simp((left[0]+left[0].H).subs(t,s.pi/(4*w)))!=s.zeros(2)

# Positive observer response need not be time-independent if N changes.
Nhalf_inv=s.diag(s.exp(-lam*t),s.exp(lam*t))
N=s.diag(s.exp(2*lam*t),s.exp(-2*lam*t))
assert s.simplify(s.det(N)-1)==0
assert simp(Nhalf_inv*N*Nhalf_inv-one)==s.zeros(2)
TN=s.simplify(Nhalf_inv*B*Nhalf_inv)
hN=s.simplify(s.trace(TN.H*TN))
assert s.simplify(hN-(4*s.exp(-4*lam*t)+s.exp(4*lam*t)))==0
assert s.simplify(s.diff(hN,t))!=0

print("PASS conserved scalar-U1 Klein-Gordon comparator current has indefinite sign")
print("PASS pointwise positive Gram can vary for a superposition of KG solutions")
print("PASS central phase rotates canonical sharp metric by phase weight two")
print("PASS positive unitary evolution conserves trace, purity and rank; no collapse")
print("PASS linked spin action keeps Lorentz-real jets; left unitary alone may not")
print("PASS observer reference N(t) affects norm without compatible transport")
print("SCOPE all these are comparator gates; no selected UBT Noether current")
