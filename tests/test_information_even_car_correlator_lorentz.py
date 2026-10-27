"""Two-mode CAR density generates an algebraic Lorentz carrier, not a tetrad."""
import sympy as sp

I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.diag(1, -1)
A = sp.Matrix([[0, 1], [0, 0]])
C1 = sp.kronecker_product(A, I2)
C2 = sp.kronecker_product(SZ, A)
OPS = [C1, C2]
PAULI = [I2, SX, SY, SZ]


def correlator(state):
    return sp.Matrix(
        2, 2, lambda i, j: sp.simplify(
            (state.conjugate().T*OPS[j].conjugate().T*OPS[i]*state)[0]))


def test_car_algebra():
    for i in range(2):
        for j in range(2):
            assert OPS[i]*OPS[j]+OPS[j]*OPS[i] == sp.zeros(4)
            assert OPS[i]*OPS[j].conjugate().T+OPS[j].conjugate().T*OPS[i] == (
                sp.eye(4) if i == j else sp.zeros(4))


def test_correlation_matrix_generic_pure_state_determinant():
    alp, beta, gamma, delta = sp.symbols(
        "alp beta gamma delta", complex=True)
    state = sp.Matrix([alp, gamma, beta, delta])
    C = correlator(state)
    d = delta*sp.conjugate(delta)
    rhs = d*(beta*sp.conjugate(beta)+gamma*sp.conjugate(gamma)+d)
    assert sp.simplify(sp.expand(C.det()-rhs)) == 0
    assert sp.simplify(C.conjugate().T-C) == sp.zeros(2)
    B = [sp.simplify(sp.trace(sig*C)) for sig in PAULI]
    reconstructed = sum(
        (B[i]*PAULI[i] for i in range(4)), sp.zeros(2))/2
    assert sp.simplify(reconstructed-C) == sp.zeros(2)
    norm = (B[0]**2-sum(x*x for x in B[1:]))/4
    assert sp.simplify(norm-C.det()) == 0


def test_car_vacuum_one_particle_and_double_occupancy():
    states = [
        sp.Matrix([1, 0, 0, 0]),
        sp.Matrix([0, 0, 1, 0]),
        sp.Matrix([0, 0, 0, 1]),
    ]
    expected = [sp.zeros(2), sp.diag(1, 0), sp.eye(2)]
    for state, X in zip(states, expected):
        assert correlator(state) == X
    assert [x.det() for x in expected] == [0, 0, 1]


def test_even_bcs_like_superposition_has_timelike_carrier():
    state = sp.Matrix([1, 0, 0, 1])/sp.sqrt(2)
    assert correlator(state) == sp.eye(2)/2
    assert correlator(state).det() == sp.Rational(1, 4)


def test_correlator_factorization_has_right_unitary_fiber():
    p, q = sp.symbols("p q", real=True, positive=True)
    X = sp.diag(p, q)
    theta = sp.diag(sp.sqrt(p), sp.sqrt(q))
    U = sp.Matrix([[0, 1], [-1, 0]])
    assert U*U.conjugate().T == sp.eye(2)
    assert theta*theta.conjugate().T == X
    assert (theta*U)*(theta*U).conjugate().T == X
    assert sp.simplify(
        theta.det()*sp.conjugate(theta.det())-X.det()) == 0
