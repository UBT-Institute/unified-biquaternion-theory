"""Exact algebraic test: affine carrier cannot extremize the pure volume action
when all metric-compatible auxiliary contortions respecting E=D X/s are allowed.

Conditional Lorentz-vector branch; this is NOT the dynamics of a selected
single-Theta torsion law K[Theta] or the full eight-real carrier.
"""
import sympy as s
eta = s.diag(-1, 1, 1, 1)
X = s.Matrix(s.symbols("x0:4", real=True))
norm2 = (X.T * eta * X)[0]
P = s.eye(4) - X * (X.T * eta) / norm2
z = s.symbols("z", real=True)

assert s.simplify(P * P - P) == s.zeros(4)
assert s.simplify(P * X) == s.zeros(4, 1)
assert s.simplify(X.T * eta * P) == s.zeros(1, 4)
assert s.simplify(s.trace(P) - 3) == 0
assert s.factor((s.eye(4) + z * P).det(method="berkowitz")) == (1 + z)**3
assert s.diff((1 + z)**3, z).subs(z, 0) == 3

# Exact right inverse: for any Y perpendicular to nonnull X,
# K^a{}_b=(Y^a X_b-X^a Y_b)/(X.X) is metric-compatible and K X=Y.
q = s.Matrix(s.symbols("q0:4", real=True))
Y = P * q
K = (Y * (X.T * eta) - X * (Y.T * eta)) / norm2
assert s.simplify(K * X - Y) == s.zeros(4, 1)
assert s.simplify(K.T * eta + eta * K) == s.zeros(4)

# Necessary condition X_a e_mu^a=(2s)^-1 d_mu(X^2):
# X_a omega_mu^a{}_b X^b=0 for every so(1,3)-valued connection.
W = s.zeros(4)
gens = s.symbols("w01 w02 w03 w12 w13 w23")
for (a, b), t in zip(((0,1), (0,2), (0,3), (1,2), (1,3), (2,3)), gens):
    W[a, b] = t
    W[b, a] = -eta[a,a] / eta[b,b] * t
assert s.simplify(W.T * eta + eta * W) == s.zeros(4)
assert s.simplify((X.T * eta * W * X)[0]) == 0
print("PASS projector, exact volume det, Lorentz contortion right inverse")
print("PASS pure volume first variation: 6*N0*integral f != 0 for nonzero integral")
print("SCOPE: auxiliary/unselected K only; no physical UBT K-selector proved")
