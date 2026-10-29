"""SU2-covariant entangled CAR correlation axis and ADM sign obstruction."""
import sympy as s

I2 = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -s.I], [s.I, 0]])
Z = s.diag(1, -1)
PAULI = (X, Y, Z)


def expectation(state, operator):
    return s.simplify((state.conjugate().T * operator * state)[0])


def entangled(p):
    return s.Matrix([s.sqrt(p), 0, 0, s.sqrt(1-p)])


def correlation(state):
    return s.Matrix(
        3, 3,
        lambda j, k: expectation(
            state, s.kronecker_product(PAULI[j], PAULI[k])))


def test_exact_entangled_t_matrix_eigenaxis():
    p = s.Rational(3, 4)
    t = correlation(entangled(p))
    assert t == s.diag(s.sqrt(3)/2, -s.sqrt(3)/2, 1)
    assert t*t.T == s.diag(s.Rational(3, 4), s.Rational(3, 4), 1)
    assert (t*t.T - s.eye(3)).nullspace() == [s.Matrix([0, 0, 1])]


def test_spin_direction_changes_covariantly_under_simultaneous_rotation():
    v = entangled(s.Rational(3, 4))
    U = (I2 + s.I*X) / s.sqrt(2)
    assert s.simplify(U*U.conjugate().T-I2) == s.zeros(2)
    vr = s.kronecker_product(U, U)*v
    t = correlation(v)
    tr = correlation(vr)
    R = s.Matrix(
        3, 3,
        lambda a, b: s.simplify(
            s.trace(PAULI[a]*U*PAULI[b]*U.conjugate().T)/2))
    assert s.simplify(tr - R*t*R.T) == s.zeros(3)
    assert s.simplify(tr*tr.T-R*(t*t.T)*R.T) == s.zeros(3)


def test_isotropic_singlet_has_no_polarization():
    singlet = s.Matrix([0, 1, -1, 0])/s.sqrt(2)
    h = sum(
        (s.kronecker_product(sig, sig) for sig in PAULI),
        s.zeros(4))
    assert h.eigenvals() == {-3: 1, 1: 3}
    assert h*singlet == -3*singlet
    assert correlation(singlet) == -s.eye(3)
    for mat in PAULI:
        assert expectation(singlet, s.kronecker_product(mat, I2)) == 0


def test_no_su2_invariant_nonzero_one_spin_polarization():
    a, b, c = s.symbols("a b c", real=True)
    magnetization = a*X+b*Y+c*Z
    constraints = []
    for sig in PAULI:
        constraints.extend(list(magnetization*sig-sig*magnetization))
    assert list(s.linsolve(constraints, [a, b, c])) == [(0, 0, 0)]


def test_entangled_bloch_determinant_ccr_tradeoff():
    p = s.symbols("p", real=True)
    r = 2*p-1
    determinant = p*(1-p)
    assert s.expand(r*r+4*determinant) == 1
    assert determinant.subs(p, s.Rational(3, 4)) == s.Rational(3, 16)
    assert r.subs(p, s.Rational(1, 2)) == 0
    assert determinant.subs(p, s.Rational(1, 2)) == s.Rational(1, 4)


def test_positive_oscillator_not_adm_negative_kinetic_unitary_equivalent():
    frequency, kappa = s.symbols("frequency kappa", real=True, positive=True)
    Q = X/s.sqrt(2)
    P = Y/s.sqrt(2)
    vacuum = s.Matrix([1, 0])
    K = (I2-Z)/2
    oscillator = frequency*K
    exp_minus_3q = s.cosh(3/s.sqrt(2))*I2-s.sinh(3/s.sqrt(2))*X
    gravity_kinetic = -kappa*P*exp_minus_3q*P/12
    assert oscillator == s.diag(0, frequency)
    assert expectation(vacuum, oscillator) == 0
    assert s.simplify(
        expectation(vacuum, gravity_kinetic)
        + kappa*s.cosh(3/s.sqrt(2))/24) == 0
    assert gravity_kinetic.is_hermitian
    assert gravity_kinetic.det() != 0


def test_su2_invariant_ferromagnet_has_entangled_polarized_degenerate_ground():
    J = s.symbols("J", real=True, positive=True)
    exchange = sum(
        (s.kronecker_product(sig, sig) for sig in PAULI),
        s.zeros(4))
    h = -J*exchange
    assert h.eigenvals() == {-J: 3, 3*J: 1}
    for sig in PAULI:
        total = s.kronecker_product(sig, I2)+s.kronecker_product(I2, sig)
        assert h*total-total*h == s.zeros(4)
    target = entangled(s.Rational(3, 4))
    assert h*target == -J*target
    assert correlation(target) == s.diag(s.sqrt(3)/2, -s.sqrt(3)/2, 1)
    assert expectation(target, s.kronecker_product(Z, I2)) == s.Rational(1, 2)


def test_isotropic_pair_collective_quadratures_are_zero_frequency():
    J = s.symbols("J", real=True, positive=True)
    h = -J*sum(
        (s.kronecker_product(sig, sig) for sig in PAULI),
        s.zeros(4))
    qpair = (s.kronecker_product(X, I2)+s.kronecker_product(I2, X))/2
    ppair = (s.kronecker_product(Y, I2)+s.kronecker_product(I2, Y))/2
    assert h*qpair-qpair*h == s.zeros(4)
    assert h*ppair-ppair*h == s.zeros(4)
    total_z = (s.kronecker_product(Z, I2)+s.kronecker_product(I2, Z))/2
    assert s.simplify(
        qpair*ppair-ppair*qpair-s.I*total_z) == s.zeros(4)
