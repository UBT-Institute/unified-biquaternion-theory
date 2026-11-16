"""Exact gauge-rank and projective-compatibility audit for the GR/UBT branch.

Checks a local orthonormal coframe. These are standard geometrical identities,
not the full canonical UBT field equations or a Hamiltonian degree-of-freedom count.
"""
import sympy as s

eta=s.diag(-1,1,1,1)
pairs=[(a,b) for a in range(4) for b in range(a+1,4)]
variables=[(a,mu) for a in range(4) for mu in range(4)]
metric_indices=[(mu,nu) for mu in range(4) for nu in range(mu,4)]
J=s.zeros(10,16)
E=s.eye(4)
for col,(a,mu) in enumerate(variables):
    de=s.zeros(4,4);de[a,mu]=1
    dg=de.T*eta*E+E.T*eta*de
    for row,(i,j) in enumerate(metric_indices):
        J[row,col]=dg[i,j]
assert J.rank()==10
assert len(J.nullspace())==6

generators=[]
for a,b in pairs:
    W=s.zeros(4,4)
    W[a,b]=1
    W[b,a]=-eta[a,a]/eta[b,b]
    assert W.T*eta+eta*W==s.zeros(4,4)
    generators.append(s.Matrix([W[x,mu] for x,mu in variables]))
G=s.Matrix.hstack(*generators)
assert G.rank()==6
assert J*G==s.zeros(10,6)

# delta Gamma^rho_(mu nu)=delta^rho_nu xi_mu
# delta(nabla_mu g_nu rho)=-xi_mu g_nu rho-xi_mu g_nu rho
xi=s.symbols("xi0:4")
for mu in range(4):
    for nu in range(4):
        for rho in range(4):
            shift=-sum(s.KroneckerDelta(k,nu)*xi[mu]*eta[k,rho]
                       +s.KroneckerDelta(k,rho)*xi[mu]*eta[nu,k]
                       for k in range(4))
            assert s.simplify(shift+2*xi[mu]*eta[nu,rho])==0
# Formal projective curvature shift delta R^rho_(sigma mu nu)
#   = delta^rho_sigma (partial_mu xi_nu-partial_nu xi_mu).
# Ricci contraction is antisymmetric, so symmetric metric kills it.
A=s.Matrix(4,4, lambda i,j: (i-j) if i!=j else 0)
assert A+A.T==s.zeros(4,4)
assert s.trace(eta.inv()*A)==0

print("PASS: tetrad->metric rank 10, six independent Lorentz gauge generators")
print("PASS: projective shift produces nonmetricity -2 xi_mu g_nu_rho")
print("PASS: antisymmetric Ricci projective shift leaves scalar curvature unchanged")
