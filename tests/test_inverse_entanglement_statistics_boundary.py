"""Finite algebra boundary tests for the inverse boson/fermion reconstruction.

Exact finite matrix identities, not spin-statistics theorem or UBT emergence.
"""
import sympy as sp


def test_one_mode_majorana_clifford_algebra():
    c = sp.Matrix([[0, 1], [0, 0]])
    cd = c.T
    q1 = c + cd
    q2 = sp.I*(cd - c)
    qs = [q1, q2]
    for i in range(2):
        for j in range(2):
            assert qs[i]*qs[j] + qs[j]*qs[i] == (2*sp.eye(2) if i==j else sp.zeros(2))


def test_fermion_parity_is_not_matrix_grade():
    c = sp.Matrix([[0, 1], [0, 0]])
    parity = sp.diag(1, -1)
    assert parity*c*parity == -c
    assert parity*(c.T*c)*parity == c.T*c


def test_finite_dimensional_ccr_trace_obstruction():
    for n in (1, 2, 3, 5):
        Q = sp.diag(*range(n))
        P = sp.Matrix(n, n, lambda i, j: 1 if i+1==j else 0)
        assert sp.trace(Q*P-P*Q)==0
        assert sp.trace(sp.I*sp.eye(n))==sp.I*n


def test_entanglement_bell_marginal_remains_mixed():
    bell = sp.Matrix([1, 0, 0, 1])/sp.sqrt(2)
    density = bell*bell.T
    marginal = sp.Matrix(2, 2, lambda i,j:
                         sum(density[2*a+i,2*a+j] for a in range(2)))
    assert marginal == sp.eye(2)/2
    assert marginal*marginal != marginal
