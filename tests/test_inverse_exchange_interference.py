"""Conditional exchange-phase selection and two-mode quantum interference.

No claim that the scalar exchange representation or fundamental UBT is derived.
"""
import sympy as sp


def test_one_dimensional_exchange_character():
    eta = sp.symbols("eta")
    assert sp.solve(eta**2 - 1, eta) == [-1, 1]


def test_balanced_bosonic_bunching():
    r = 1/sp.sqrt(2)
    amp20 = sp.sqrt(2)*r*r
    amp02 = -sp.sqrt(2)*r*r
    amp11 = sp.Integer(0)  # commuting c+,d+ cancel in product
    assert sp.simplify(amp20**2) == sp.Rational(1, 2)
    assert sp.simplify(amp02**2) == sp.Rational(1, 2)
    assert amp11 == 0
    assert sp.simplify(amp20**2+amp02**2) == 1


def test_balanced_fermionic_antibunching():
    r = 1/sp.sqrt(2)
    # (c+d)(c-d) = -cd + dc = -2cd for fermionic creation.
    amp11 = -2*r*r
    assert sp.simplify(amp11**2) == 1
    # Squares of identical fermionic creation operators vanish.
    c = sp.Matrix([[0, 1], [0, 0]])
    assert c*c == sp.zeros(2)


def test_fixed_local_occupation_bell_correlations():
    psi = sp.Matrix([1, 0, 0, 1])/sp.sqrt(2)
    X, Z = sp.Matrix([[0, 1], [1, 0]]), sp.diag(1, -1)
    rho = psi*psi.T
    marginal = sp.Matrix(2, 2, lambda i, j:
                         sum(rho[2*i+k, 2*j+k] for k in range(2)))
    assert marginal == sp.eye(2)/2
    def exp(A, B):
        return sp.simplify((psi.T*sp.kronecker_product(A, B)*psi)[0])
    b0, b1 = (Z+X)/sp.sqrt(2), (Z-X)/sp.sqrt(2)
    assert sp.simplify(exp(Z,b0)+exp(Z,b1)+exp(X,b0)-exp(X,b1)) == 2*sp.sqrt(2)
