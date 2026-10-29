"""Exact CAR-to-collective bosonic CCR identities, finite cutoff checks.

Proof-level identities hold for all N by the local su(2) algebra; tests check
representative N<=5 and exact Dicke matrix elements without taking a false
operator-norm limit on the full finite Hilbert space.
"""
from itertools import combinations

import sympy as s

I2 = s.eye(2)
SX = s.Matrix([[0, 1], [1, 0]])
SY = s.Matrix([[0, -s.I], [s.I, 0]])
SZ = s.diag(1, -1)


def kron(xs):
    z = s.eye(1)
    for x in xs:
        z = s.kronecker_product(z, x)
    return z


def embed(M, j, N):
    return kron([M if k == j else I2 for k in range(N)])


def collective(N):
    Q = sum((embed(SX, j, N) for j in range(N)), s.zeros(2**N))/s.sqrt(2*N)
    P = sum((embed(SY, j, N) for j in range(N)), s.zeros(2**N))/s.sqrt(2*N)
    Zsum = sum((embed(SZ, j, N) for j in range(N)), s.zeros(2**N))
    K = (N*s.eye(2**N) - Zsum)/2
    A = (Q+s.I*P)/s.sqrt(2)
    return Q, P, K, A, Zsum


def dicke(N, k):
    state = s.zeros(2**N, 1)
    for flips in combinations(range(N), k):
        index = sum(2**(N-1-j) for j in flips)
        state[index] = 1
    return state/s.sqrt(s.binomial(N, k))


def test_even_schwinger_bilinears_come_from_two_biquaternion_cars():
    annihilator = s.Matrix([[0, 1], [0, 0]])
    parity = SZ
    cs = [kron([annihilator, I2]), kron([parity, annihilator])]
    vac = s.Matrix([1, 0, 0, 0])
    W = s.Matrix.hstack(
        *[op.conjugate().T*vac for op in cs]
    )
    for pauli in [I2, SX, SY, SZ]:
        B = sum(
            (cs[i].conjugate().T*cs[j]*pauli[i, j]
             for i in range(2) for j in range(2)),
            s.zeros(4),
        )
        assert W.conjugate().T*B*W == pauli


def test_collective_finite_n_commutators_are_exact():
    for N in range(1, 5):
        Q, P, K, A, _ = collective(N)
        expected = s.eye(2**N)-2*K/N
        assert s.simplify(Q*P-P*Q-s.I*expected) == s.zeros(2**N)
        assert s.simplify(A*A.conjugate().T-A.conjugate().T*A-expected) == s.zeros(2**N)


def test_dicke_bosonic_ladder_coefficients_and_number_operator():
    for N in range(1, 5):
        _, _, K, A, _ = collective(N)
        for k in range(N+1):
            state = dicke(N, k)
            assert K*state == k*state
            if k < N:
                amp = s.sqrt(s.Rational((k+1)*(N-k), N))
                assert s.simplify(A.conjugate().T*state-amp*dicke(N, k+1)) == s.zeros(2**N, 1)
            if k > 0:
                amp = s.sqrt(s.Rational(k*(N-k+1), N))
                assert s.simplify(A*state-amp*dicke(N, k-1)) == s.zeros(2**N, 1)


def test_commutator_low_occupation_error_is_exact_2k_over_n():
    for N in range(1, 6):
        Q, P, _, _, _ = collective(N)
        for k in range(min(N, 2)+1):
            state = dicke(N, k)
            bracket = (state.conjugate().T*(Q*P-P*Q)*state)[0]
            assert s.simplify(bracket-s.I*(1-s.Rational(2*k, N))) == 0


def test_positive_collective_spin_hamiltonian_heisenberg_equation():
    frequency = s.symbols("frequency", real=True, positive=True)
    for N in range(1, 5):
        _, _, K, A, _ = collective(N)
        H = frequency*K
        assert s.simplify(H*A-A*H+frequency*A) == s.zeros(2**N)
        assert sorted(K.eigenvals()) == list(range(N+1))


def test_no_exact_finite_matrix_ccr_including_collective_truncations():
    for N in (1, 2, 4):
        Q, P, _, _, _ = collective(N)
        assert s.trace(Q*P-P*Q) == 0
        assert s.trace(s.I*s.eye(2**N)) == s.I*2**N
