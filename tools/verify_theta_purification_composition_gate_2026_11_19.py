"""Exact mathematical purification of one observer's biquaternion density.

The Hilbert tensor-factor interpretation, effects, filter, and composition
are CONDITIONAL mathematical comparators, not a finalized UBT quantum action.
"""
import sympy as sp

I=sp.I
one=sp.eye(2)
sx=sp.Matrix([[0,1],[1,0]])
sy=sp.Matrix([[0,-I],[I,0]])
sz=sp.diag(1,-1)
sigma=[one,sx,sy,sz]
eta=sp.diag(-1,1,1,1)
sharp=lambda m:sp.Matrix([[m[1,1],-m[0,1]],[-m[1,0],m[0,0]]])
g=lambda E:sp.Matrix(4,4,lambda a,b:sp.simplify(sp.trace(
    (sharp(E[a])*E[b]+sharp(E[b])*E[a])/2)/2))
simplify=lambda m:m.applyfunc(sp.simplify)

def vec(T):
    return sp.Matrix([T[0,0],T[0,1],T[1,0],T[1,1]])

def reduce_right(A):
    return sp.Matrix(2,2,lambda i,k:sp.simplify(
        sum(A[2*i+j,2*k+j] for j in range(2))))

T=sp.Matrix([[1,2+I],[3-I,4]])
v=vec(T)
norm2=sp.simplify((v.H*v)[0])
assert norm2==sp.trace(T*T.H)
rho=sp.simplify(T*T.H/norm2)
pure=sp.simplify(v*v.H/norm2)
assert simplify(reduce_right(pure)-rho)==sp.zeros(2)

# A positive effect M produces a conditional quadratic response.
M=sp.diag(sp.Rational(1,4),sp.Rational(3,4))
p=sp.simplify(sp.trace(T.H*M*T)/norm2)
expect=sp.simplify((v.H*sp.kronecker_product(M,one)*v)[0]/norm2)
assert p==expect
assert p>0 and p<1
assert sp.simplify(p+(1-p)-1)==0
R=sp.diag(sp.Rational(1,2),sp.sqrt(3)/2)
assert simplify(R.H*R-M)==sp.zeros(2)
filterprob=sp.simplify(sp.trace((R*T).H*(R*T))/norm2)
assert filterprob==p

# Two equal left reduced densities can have different joint phase coherence.
Theta_plus=one
Theta_minus=I*sz
assert sp.det(Theta_minus)==1 and simplify(Theta_minus.H*Theta_minus-one)==sp.zeros(2)
v_plus=vec(Theta_plus)/sp.sqrt(2)
v_minus=vec(Theta_minus)/sp.sqrt(2)
assert reduce_right(v_plus*v_plus.H)==one/2
assert reduce_right(v_minus*v_minus.H)==one/2
XX=sp.kronecker_product(sx,sx)
assert sp.simplify((v_plus.H*XX*v_plus)[0])==1
assert sp.simplify((v_minus.H*XX*v_minus)[0])==-1

# The examples also fit the unchanged canonical Lorentz-flat first jet.
t,x,y,z=sp.symbols('t x y z',real=True)
coords=[t,x,y,z]
for base in (Theta_plus,Theta_minus):
    Theta=base+I*sum((q*sigma[a] for a,q in enumerate(coords)),sp.zeros(2))
    E=[sp.diff(Theta,q) for q in coords]
    assert all(simplify(e+e.H)==sp.zeros(2) for e in E)
    assert g(E)==eta

# One observer frame transforms with a correlated U tensor Ubar.
U=(one+I*sx)/sp.sqrt(2)
assert simplify(U.H*U-one)==sp.zeros(2)
assert simplify(vec(U*T*U.H)-sp.kronecker_product(U,sp.conjugate(U))*vec(T))==sp.zeros(4,1)

# Invertible boost+rotation Lorentz-congruence observer covariance.
B=sp.diag(2,sp.Rational(1,2))
S=B*U
Nprime=S*S.H
Nprime_invhalf=sp.diag(sp.Rational(1,2),2)
assert sp.det(S)==1
assert simplify(Nprime_invhalf*Nprime*Nprime_invhalf-one)==sp.zeros(2)
Tprime=sp.simplify(Nprime_invhalf*(S*T*S.H)*Nprime_invhalf)
assert simplify(Tprime-U*T*U.H)==sp.zeros(2)
assert simplify(Tprime*Tprime.H/sp.trace(Tprime*Tprime.H)-U*rho*U.H)==sp.zeros(2)

# A single matrix algebra M2 has scalar commutant, no second faithful
# independent commuting M2 algebra inside that SAME output algebra.
a,b,c,d=sp.symbols('a b c d')
X=sp.Matrix([[a,b],[c,d]])
constraints=list(X*sx-sx*X)+list(X*sz-sz*X)
ans=sp.solve(constraints,[a,b,c,d],dict=True)
assert ans==[{a:d,b:0,c:0}]

# Matrix algebra dimensions: M2 ⊗ M2 ≅ M4 is 16 complex-dimensional,
# while M2 itself is only 4 complex-dimensional. This does not rule out
# the vec(T) TWO-FACTOR mathematical encoding in C4.
assert 4*4==16 and 2*2==4
# The canonical biquaternion sharp determinant controls the mathematical
# two-index Schmidt concurrence for this CHOSEN Hilbert factorization.
detT=sp.simplify(sp.det(T))
C2=sp.simplify(4*detT*sp.conjugate(detT)/norm2**2)
purity=sp.simplify(sp.trace(rho*rho))
assert sp.simplify(purity+2*detT*sp.conjugate(detT)/norm2**2-1)==0
assert sp.simplify(C2-2*(1-purity))==0
assert sp.simplify(sharp(T)*T-detT*one)==sp.zeros(2)
assert sp.simplify(C2-sp.Rational(5,128))==0
assert sp.simplify(purity-sp.Rational(251,256))==0
assert sp.simplify(4*sp.det(T*T.H)/norm2**2-C2)==0
assert sp.simplify(4*sp.det(Tprime*Tprime.H)/sp.trace(Tprime*Tprime.H)**2-C2)==0

# Full right-U2 gauge invariance would make every allowed joint observable
# commute with I tensor V. Its full commutant is M2 tensor I (Schur's lemma).
zz=sp.symbols('z0:16')
O=sp.Matrix(4,4,zz)
I_x=sp.kronecker_product(one,sx)
I_z=sp.kronecker_product(one,sz)
equations=list(O*I_x-I_x*O)+list(O*I_z-I_z*O)
sol=sp.linsolve(equations,zz)
assert len(sol)==1
fixed=list(sol)[0]
K=sp.Matrix([[zz[0],zz[2]],[zz[8],zz[10]]])
# Solve with specific free variables to show every solution = K tensor I.
assert sp.simplify(O.subs(dict(zip(zz,fixed)))-sp.kronecker_product(
    sp.Matrix([[fixed[0],fixed[2]],[fixed[8],fixed[10]]]),one
))==sp.zeros(4)

Vright=sp.kronecker_product(one,I*sz)
assert sp.simplify(Vright.H*XX*Vright+XX)==sp.zeros(4)
# The Bell comparison is NOT right-gauge invariant.
assert sp.simplify((v_plus.H*XX*v_plus)[0]-
    (v_minus.H*XX*v_minus)[0])==2

print("PASS normalized sharp determinant determines conditional concurrence and reduced purity")
print("PASS the full right-U2 commutant contains only left-index effects")
print("PASS hidden-phase Bell correlator is forbidden as an observable if right U2 is gauged")

print("PASS vectorized full biquaternion yields partial-trace observer rho")
print("PASS conditional positive-effect probability is quadratic filter fraction")
print("PASS same rho and canonical Minkowski metric, different two-index coherences")
print("PASS observer Lorentz frame acts as U tensor conjugate(U)")
print("PASS two independent full matrix algebras cannot both live inside one M2 output")
print("OPEN physical tensor-factor split, detector law, outcome selection, and multi-body UBT quantization")
