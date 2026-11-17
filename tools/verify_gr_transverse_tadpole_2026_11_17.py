"""Exact local transverse stationarity and constant-volume tadpole checks.

The first-order Palatini/Holst boundary statement is analytic, not tested
by this finite-dimensional SymPy script. Restricted real Lorentz carrier,
fixed nonnull X, freely auxiliary metric-compatible contortion only.
"""
import sympy as sp

eta = sp.diag(-1, 1, 1, 1)
x = sp.Matrix([2, 1, 0, 0])
x2 = (x.T * eta * x)[0]
assert x2 == -3
P = sp.eye(4) - x * (x.T * eta) / x2
assert P * P == P
assert P * x == sp.zeros(4, 1)
assert P.rank() == sp.trace(P) == 3
assert sp.kronecker_product(sp.eye(4), P).rank() == 12

# The annihilator of the allowed fixed-X coframe variations is span(X_flat)
# independently for each of the four spacetime coframe columns.
xflat = eta * x
assert P.T * xflat == sp.zeros(4, 1)
for mu in range(4):
    Z = sp.zeros(4, 4)
    Z[:, mu] = xflat
    assert P.T * Z == sp.zeros(4, 4)

alpha = sp.symbols("alpha", real=True, nonzero=True)
force = alpha * sp.eye(4)
assert (P.T * force).rank() == 3
f, eps = sp.symbols("f eps", real=True)
assert sp.factor((sp.eye(4) + eps * f * P).det()) == (1 + eps * f)**3
assert sp.diff((1 + eps * f)**3, eps).subs(eps, 0) == 3*f

# Flat stationarity on an open X^2 interval requires zero total local
# volume coefficient: a nonconstant polynomial potential cannot accomplish it.
z,u0,u1,u2=sp.symbols("z u0 u1 u2",real=True)
F=alpha+u0+u1*z+u2*z*z
assert sp.solve(sp.Poly(F,z).all_coeffs(),(u0,u1,u2)) == {
    u0:-alpha,u1:0,u2:0}

# Invariants quadratic in any zero-background torsion/curvature variables
# have zero first variation on that background.
t=sp.symbols("t0:24",real=True)
b=sp.symbols("b0:24",real=True)
quadratic=sum((eps*b[j])**2 for j in range(24))
assert sp.diff(quadratic,eps).subs(eps,0)==0

# Compare to existing HT postulate: shift of integration constant
# removes a constant volume term up to an exact 3-form derivative.
kappa,lam,lam_prime,nu,dC=sp.symbols(
    "kappa lam lam_prime nu dC",nonzero=True)
initial=-lam*(nu-dC)/kappa+alpha*nu
shifted=-lam_prime*(nu-dC)/kappa+alpha*dC
assert sp.simplify(initial.subs(lam,lam_prime+kappa*alpha)-shifted)==0

print("PASS: projected stationarity rank and volume tadpole")
print("PASS: polynomial-potential tuning and zero quadratic first variation")
print("PASS: HT integration-constant shift (known comparator)")
print("NOT TESTED: full Theta/PDE Hessian, independent Palatini boundary proof")
