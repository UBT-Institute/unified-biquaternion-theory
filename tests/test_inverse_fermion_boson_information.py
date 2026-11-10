"""Finite CAR/CCR and no-signalling regression checks (not UBT quantum closure)."""
import sympy as sp


def test_single_mode_fermionic_car():
    c = sp.Matrix([[0, 1], [0, 0]])
    cd = c.T
    assert c*c == sp.zeros(2)
    assert cd*cd == sp.zeros(2)
    assert c*cd + cd*c == sp.eye(2)


def test_bosonic_commutator_on_finite_truncation_interior():
    # Truncated oscillator has a boundary anomaly, as it must by trace.
    n = 6
    b = sp.zeros(n)
    for k in range(1, n):
        b[k-1, k] = sp.sqrt(k)
    comm = b*b.T - b.T*b
    assert comm == sp.diag(1, 1, 1, 1, 1, -(n-1))


def partial_trace_A(rho):
    return sp.Matrix(2, 2, lambda i, j: sum(rho[2*a+i,2*a+j] for a in range(2)))


def test_bell_state_local_unitary_no_signalling():
    v = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    rho = v * v.T
    Z = sp.diag(1, -1)
    U = sp.kronecker_product(Z, sp.eye(2))
    assert partial_trace_A(U*rho*U.T) == partial_trace_A(rho) == sp.eye(2)/2


def test_bell_state_nonselective_measurement_no_signalling():
    v = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    rho = v * v.T
    P0 = sp.diag(1, 0)
    P1 = sp.diag(0, 1)
    E = sum((sp.kronecker_product(P, sp.eye(2))*rho*
             sp.kronecker_product(P, sp.eye(2)) for P in (P0, P1)), sp.zeros(4))
    assert partial_trace_A(E) == partial_trace_A(rho) == sp.eye(2)/2
