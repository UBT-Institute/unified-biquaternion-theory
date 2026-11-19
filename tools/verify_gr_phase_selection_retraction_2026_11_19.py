"""Exact off-shell reality-selection obstructions in one full biquaternion.

Checks regular complex-sharp metric loss under naive anti-Hermitian projection,
path of nondegenerate complex jets across real orientations, and observer
readout blindness to distinct canonical real metrics at a point.

This does NOT test an on-shell fundamental UBT action or quantum collapse.
"""
import sympy as s

I=s.I
one=s.eye(2)
sigmas=[one,s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
eta=s.diag(-1,1,1,1)

def sharp(m):
    return s.Matrix([[m[1,1],-m[0,1]],[-m[1,0],m[0,0]]])

def metric(E):
    return s.Matrix(4,4,lambda mu,nu:s.simplify(
        s.trace((sharp(E[mu])*E[nu]+sharp(E[nu])*E[mu])/2)/2))

def coeff_jets(L):
    return [s.simplify(I*sum((L[mu,a]*sigmas[a] for a in range(4)),s.zeros(2)))
            for mu in range(4)]

assert metric(coeff_jets(s.eye(4)))==eta
L=s.eye(4)
L[0,0]=L[1,1]=0
L[0,1]=L[1,0]=I
assert s.simplify(L.T*eta*L-eta)==s.zeros(4)
assert s.simplify(s.det(L)-1)==0
E=coeff_jets(L)
assert metric(E)==eta
assert all(s.simplify(E[k]+E[k].H)==s.zeros(2) for k in [2,3])
assert all(s.simplify(E[k]-E[k].H)==s.zeros(2) for k in [0,1])
E_proj=[s.simplify((M-M.H)/2) for M in E]
assert E_proj[0]==E_proj[1]==s.zeros(2)
assert metric(E_proj)==s.diag(0,0,1,1)
assert metric(E).det()==-1 and metric(E_proj).det()==0

u=s.symbols("u",real=True)
path=s.diag(s.exp(I*s.pi*u),1,1,1)
assert s.simplify(s.det(path)-s.exp(I*s.pi*u))==0
assert s.simplify(path.subs(u,0)-s.eye(4))==s.zeros(4)
assert s.simplify(path.subs(u,1)-s.diag(-1,1,1,1))==s.zeros(4)
assert s.simplify(metric(coeff_jets(path)).det()+s.exp(2*I*s.pi*u))==0

t,x,y,z,a=s.symbols("t x y z a",real=True)
Theta=one+I*(t*one+x*sigmas[1]+y*sigmas[2]+z*sigmas[3])
U=s.diag(s.exp(I*a*t),s.exp(-I*a*t))
Phi=Theta*U
assert s.simplify(U*U.H-one)==s.zeros(2)
assert s.simplify(Phi*Phi.H-Theta*Theta.H)==s.zeros(2)
coords=[t,x,y,z]
origin={t:0,x:0,y:0,z:0}
JT=[s.simplify(s.diff(Theta,v).subs(origin)) for v in coords]
JP=[s.simplify(s.diff(Phi,v).subs(origin)) for v in coords]
assert all(s.simplify(M+M.H)==s.zeros(2) for M in JT+JP)
assert metric(JT)==eta
G=metric(JP)
target=s.Matrix([[-1+a**2,0,0,a],[0,1,0,0],[0,0,1,0],[a,0,0,1]])
assert s.simplify(G-target)==s.zeros(4)
assert s.simplify(G.det()+1)==0

print("PASS: real Minkowski metric with complex jets; simple anti-Herm projection drops rank 4 to 2")
print("PASS: invertible complex jet path connects real coframes of opposite orientation")
print("PASS: identical candidate one-clock rho across a patch, distinct real metric jets at one point")
print("No on-shell or objective-collapse claim.")


# Positive comparison invariant for two noncommuting relative quaternionic phases.
# This is not an electromagnetic or physical-U(1) prediction.
sx=sigmas[1]
sy=sigmas[2]
alpha,beta=s.symbols("alpha beta",real=True)
Ua=s.cos(alpha)*one+I*s.sin(alpha)*sx
Vb=s.cos(beta)*one+I*s.sin(beta)*sy
W=Ua*Vb*Ua.H*Vb.H
chi=s.simplify(s.trigsimp(s.trace(W)/2))
assert s.trigsimp(chi-(1-2*s.sin(alpha)**2*s.sin(beta)**2))==0
assert s.simplify(chi.subs({alpha:s.pi/4,beta:s.pi/4})-s.Rational(1,2))==0
S=s.Matrix([[0,1],[-1,0]])
assert S*S.H==one and s.det(S)==1
assert s.simplify(s.trace(S*W*S.H)-s.trace(W))==0
print("PASS: noncommuting quaternion phase-loop trace invariant (gauge-base conjugation)")
