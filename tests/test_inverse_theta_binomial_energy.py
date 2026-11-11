"""Numerical and exact finite checks, not a proof of Jacobi triple product."""
import math


def theta_sum(q, cutoff=60):
    return 1.0 + 2.0 * sum(q ** (n * n) for n in range(1, cutoff + 1))


def theta_product(q, cutoff=100):
    p = 1.0
    for m in range(1, cutoff + 1):
        p *= (1 - q ** (2*m)) * (1 + q ** (2*m - 1)) ** 2
    return p


def test_jacobi_triple_product_examples():
    for q in (0.1, 0.3, 0.7):
        assert math.isclose(theta_sum(q), theta_product(q), rel_tol=1e-12, abs_tol=1e-12)


def test_odd_weights_yield_quadratic_energy():
    for n in range(80):
        assert sum(2*k+1 for k in range(n)) == n*n


def test_thermal_energy_monotonicity_examples():
    def moments(t):
        terms = [math.exp(-t*n*n) for n in range(-30,31)]
        z = sum(terms)
        u = sum(n*n*x for n,x in zip(range(-30,31),terms))/z
        e2 = sum(n**4*x for n,x in zip(range(-30,31),terms))/z
        return u,e2-u*u
    u0,v0 = moments(0.3)
    u1,v1 = moments(1.0)
    u2,v2 = moments(3.0)
    assert u0 > u1 > u2 > 0
    assert min(v0,v1,v2) > 0


def test_two_mode_cross_coupling_changes_partition():
    t=0.7
    def z(koff):
        return sum(math.exp(-t*(2*n*n+3*m*m+2*koff*n*m))
                   for n in range(-5,6) for m in range(-5,6))
    assert not math.isclose(z(0),z(0.5),rel_tol=1e-6)
    # Positive-definite 2x2 K = [[2,0.5],[0.5,3]].
    assert 2*3 - 0.5**2 > 0
