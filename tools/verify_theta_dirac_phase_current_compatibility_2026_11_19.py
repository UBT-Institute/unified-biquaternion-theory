"""Exact UBT Noether / positive Dirac pullback phase-mismatch regression.

Uses the existing selected real-linear mapping F([psi,chi])=(psi,eps chi*).
Does not assume a physical UBT Dirac action or a second fundamental field.
"""
import sympy as s
I=s.I
one=s.eye(2)
eps=s.Matrix([[0,1],[-1,0]])
sx=s.Matrix([[0,1],[1,0]])
sz=s.diag(1,-1)
eta=s.diag(-1,1,1,1)
sharp=lambda A:s.Matrix([[A[1,1],-A[0,1]],[-A[1,0],A[0,0]]])
g=lambda E:s.Matrix(4,4,lambda j,k:s.simplify(s.trace(
    (sharp(E[j])*E[k]+sharp(E[k])*E[j])/2)/2))
simp=lambda M:M.applyfunc(s.simplify)

def F(Theta):
    return s.Matrix.vstack(Theta[:,0],eps*Theta[:,1].applyfunc(s.conjugate))

T=s.Matrix([[1+I,2-I],[3,4+2*I]])
u=F(T)
assert s.simplify((u.H*u)[0]-s.trace(T.H*T))==0

alpha=s.symbols("alpha",real=True)
z=s.exp(I*alpha)
R=s.diag(z,1/z)
axial=s.diag(z,z,1/z,1/z)
assert s.simplify(s.det(R)-1)==0
assert simp(R.H*R-one)==s.zeros(2)
assert simp(F(T*R)-z*u)==s.zeros(4,1)
assert simp(F(z*T)-axial*u)==s.zeros(4,1)

# Dirac mass bilinear in chiral basis is NOT invariant under axial phase.
gamma0=s.Matrix.vstack(s.Matrix.hstack(s.zeros(2),one),
                        s.Matrix.hstack(one,s.zeros(2)))
u0=s.Matrix([1,0,1,0])
mass=lambda v:s.simplify((v.H*gamma0*v)[0])
assert mass(u0)==2
assert s.simplify(s.expand_complex(mass(axial*u0))-2*s.cos(2*alpha))==0
assert s.simplify(mass(z*u0)-mass(u0))==0

# The ordinary vector U(1) pulled back to right SU2 cannot be physical
# homogeneous gauge of the entire Lorentz-real tetrad.
E=[I*one,I*sx,I*s.Matrix([[0,-I],[I,0]]),I*sz]
assert g(E)==eta
Er=[s.simplify(e*R) for e in E]
assert simp(g(Er)-eta)==s.zeros(4)
assert simp((Er[0]+Er[0].H).subs(alpha,s.pi/2))!=s.zeros(2)
Ecentral=[s.simplify(z*e) for e in E]
assert simp(g(Ecentral)-z**2*eta)==s.zeros(4)

print("PASS real-linear Dirac pullback is isometric for Hilbert-Schmidt norm")
print("PASS Dirac vector U1 acts as right SU2 on full Theta; central phase acts axially")
print("PASS central Theta phase rotates standard Dirac mass bilinear")
print("PASS Dirac-vector right phase preserves sharp metric but not W_L first jets")
print("OPEN fundamental UBT spinor action, current, covariance and measurement dynamics")
