"""Exact log-scale Wheeler-DeWitt reference constraint with finite CAR matter."""
import sympy as sp


def test_no_finite_dimensional_exact_heisenberg_ccr_by_trace():
    a, b, c, d, e, f, g, h = sp.symbols("a b c d e f g h")
    A = sp.Matrix([[a, b], [c, d]])
    B = sp.Matrix([[e, f], [g, h]])
    assert sp.trace(A*B-B*A) == 0
    assert sp.trace(sp.I*sp.eye(2)) == 2*sp.I


def test_logarithmic_scale_is_exact_canonical_coordinate():
    a, p_a, d_a, k, lam, mass, n = sp.symbols(
        "a p_a d_a k lam mass n", real=True, positive=True)
    q = sp.log(a)
    p_q = a*p_a
    assert sp.simplify(p_q*sp.diff(q, a)*d_a-p_a*d_a) == 0
    old = -k*p_a**2/(12*a)+lam*a**3/k+mass*n
    new = -k*p_q**2/(12*a**3)+lam*a**3/k+mass*n
    assert sp.simplify(old-new) == 0


def test_logarithmic_wdw_operator_and_ccr_on_test_function():
    q, k, lam, m, n = sp.symbols("q k lam m n", real=True)
    f = sp.Function("f")(q)
    p = lambda x: -sp.I*sp.diff(x, q)
    assert sp.simplify(q*p(f)-p(q*f)-sp.I*f) == 0
    leading = -k*p(sp.exp(-3*q)*p(f))/12
    wanted = k*sp.diff(sp.exp(-3*q)*sp.diff(f, q), q)/12
    assert sp.simplify(leading-wanted) == 0
    potential = (lam*sp.exp(3*q)/k+m*n)*f
    assert sp.simplify(leading+potential-wanted-potential) == 0


def test_formal_symmetry_is_total_derivative():
    q = sp.symbols("q", real=True)
    f, g = sp.Function("f")(q), sp.Function("g")(q)
    weight = sp.exp(-3*q)
    D = lambda x: sp.diff(weight*sp.diff(x, q), q)
    local = f*D(g)-D(f)*g
    flux = sp.diff(
        weight*(f*sp.diff(g, q)-sp.diff(f, q)*g), q)
    assert sp.simplify(local-flux) == 0


def test_four_mode_fermion_number_sector_multiplicities():
    eye = sp.eye(2)
    a = sp.Matrix([[0, 1], [0, 0]])
    parity = sp.diag(1, -1)

    def kron(parts):
        x = sp.eye(1)
        for y in parts:
            x = sp.kronecker_product(x, y)
        return x

    cs = [
        kron([parity]*j+[a]+[eye]*(3-j))
        for j in range(4)
    ]
    N = sum((c.conjugate().T*c for c in cs), sp.zeros(16))
    assert N.eigenvals() == {0: 1, 1: 4, 2: 6, 3: 4, 4: 1}
    assert N == N.conjugate().T
    other = sp.eye(16)*3+N
    assert N*other == other*N


def test_classical_logarithmic_hamilton_equations():
    q, p, k, lam, L, m, n = sp.symbols(
        "q p k lam L m n", real=True)
    C = -k*sp.exp(-3*q)*p**2/12+lam*sp.exp(3*q)/k+m*n
    dotq = sp.diff(L*C, p)
    a = sp.exp(q)
    pa = p/a
    adot = sp.simplify(a*dotq)
    assert sp.simplify(adot+L*k*pa/(6*a)) == 0
