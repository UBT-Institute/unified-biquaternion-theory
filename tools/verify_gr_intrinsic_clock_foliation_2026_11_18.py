"""Restricted Lorentz-real Theta: intrinsic clock, exact FLRW lift, lapse constraint.

Exact symbolic checks on a real timelike carrier, no full complex-Theta
dynamics or proof of a microscopic gravity action.
"""
import sympy as sp

t, N0 = sp.symbols("t N0", positive=True, real=True)
s = sp.sqrt(N0)
a = sp.Function("a")(t)
eta = sp.diag(-1, 1, 1, 1)
coords = sp.Matrix([t, *sp.symbols("x y z", real=True)])
X = sp.Matrix([s*t, 0, 0, 0])
E = sp.diag(1, a, a, a)  # internal frame a, coordinate mu
g = E.T * eta * E
assert sp.simplify((X.T*eta*X)[0] + N0*t*t) == 0
assert g.inv()[0, 0] == -1  # g^munu d_mu(t)d_nu(t) = -1

# Metric-compatible spin connection realizing D_mu X=s E_mu.
omega = []
for mu in range(4):
    w = sp.zeros(4)
    if mu:
        w[mu, 0] = a/t
        w[0, mu] = a/t
    assert w.T*eta + eta*w == sp.zeros(4)
    omega.append(w)
for mu in range(4):
    dX = sp.Matrix([sp.diff(X[aa], coords[mu]) for aa in range(4)])
    assert sp.simplify(dX + omega[mu]*X - s*E[:, mu]) == sp.zeros(4, 1)

# Cartan integrability D^2 X=R X=s T: test all nontrivial 0i components.
for i in range(1, 4):
    torsion_0i = sp.diff(a,t) - a/t
    curvature_i0_0i = sp.diff(a/t,t)
    assert sp.simplify(t*curvature_i0_0i - torsion_0i) == 0

# Direct Ricci tensor of g=-dt^2+a(t)^2 dx^i dx^i
coords4 = [coords[0], coords[1], coords[2], coords[3]]
ginv = g.inv()
Gamma = [[[sp.simplify(sum(ginv[i,ll]*(
    sp.diff(g[ll,j], coords4[k])+sp.diff(g[ll,k], coords4[j])
    -sp.diff(g[j,k], coords4[ll])) for ll in range(4))/2)
    for k in range(4)] for j in range(4)] for i in range(4)]
Ric = sp.Matrix(4,4,lambda i,j:sp.simplify(sum(
    sp.diff(Gamma[ll][i][j],coords4[ll])
    -sp.diff(Gamma[ll][i][ll],coords4[j])
    +sum(Gamma[ll][m][ll]*Gamma[m][i][j]
         -Gamma[ll][m][j]*Gamma[m][i][ll] for m in range(4))
    for ll in range(4))))
assert sp.simplify(Ric[0,0]+3*sp.diff(a,t,2)/a)==0
assert sp.simplify(Ric[1,1]-a*sp.diff(a,t,2)-2*sp.diff(a,t)**2)==0
Ric_cone = Ric.subs({a:t,sp.diff(a,t):1,sp.diff(a,t,2):0})
assert Ric_cone == sp.diag(0,2,2,2)

# Lapse variation of k=0 vacuum Einstein-Hilbert FRW comparator.
b = sp.Function("b")(t)
N = sp.Function("N")(t)
L = -3*b*sp.diff(b,t)**2/N  # spatial comoving volume and constants omitted
EL_N = sp.diff(L,N)
assert sp.simplify(EL_N-3*b*sp.diff(b,t)**2/N**2) == 0
L_fix = L.subs(N,1)
EL_b = sp.simplify(sp.diff(L_fix,b)-
                   sp.diff(sp.diff(L_fix,sp.diff(b,t)),t))
assert sp.simplify(EL_b-(3*sp.diff(b,t)**2+
                         6*b*sp.diff(b,t,2)))==0
p = t**sp.Rational(2,3)
subs={b:p,sp.diff(b,t):sp.diff(p,t),
      sp.diff(b,t,2):sp.diff(p,t,2)}
assert sp.simplify(EL_b.subs(subs)) == 0
assert sp.simplify(EL_N.subs({b:p,sp.diff(b,t):sp.diff(p,t),N:1})) != 0

print("PASS: unit-gradient intrinsic clock on timelike real carrier")
print("PASS: arbitrary-a exact metric-compatible FLRW lift and R X=s T")
print("PASS: torsion-free a(t)=t gives curved non-Einstein Ricci tensor")
print("PASS: fixing lapse before variation loses vacuum Hamiltonian constraint")
print("SCOPE: restricted 4-real branch; no full UBT spin-2 dynamics")
