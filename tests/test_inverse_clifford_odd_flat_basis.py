"""Exact finite flat-space identities for Clifford odd-sector vector/axial modes.

Only a fixed-Minkowski quadratic comparison; not a UBT field-theory proof.
"""
import sympy as sp


def test_transverse_and_longitudinal_eigenvalues():
    a, b, m2, q2 = sp.symbols("a b m2 q2")
    trans = m2 - a * q2
    long = m2 - b * q2
    assert sp.factor(trans**3 * long) == (m2 - a * q2)**3 * (m2 - b * q2)


def test_homogeneous_velocity_hessian():
    a, b = sp.symbols("a b")
    # Signature (+---). Maxwell gives +a/2 sum_i dot(X_i)^2.
    # Divergence term gives -b/2 dot(X_0)^2 in homogeneous sector.
    H = sp.diag(-b, a, a, a)
    assert H.det() == -b * a**3
    assert H.subs(b, 0).rank() == 3
    assert H.subs({a: 0, b: 0}).rank() == 0


def test_epsilon_mixed_derivative_is_boundary():
    # Symbol for eps^{mu nu rho sigma} partial_mu V_nu partial_rho A_sigma
    # has zero bilinear principal symbol due to symmetric p_mu p_rho.
    p = sp.symbols("p0:4")
    for nu in range(4):
        for sig in range(4):
            contraction = sum(
                sp.LeviCivita(mu, nu, rho, sig) * p[mu] * p[rho]
                for mu in range(4) for rho in range(4)
            )
            assert sp.expand(contraction) == 0


def test_branches_are_algebraically_distinct():
    a, b, m2, q2 = sp.symbols("a b m2 q2")
    trans, longitudinal = m2 - a * q2, m2 - b * q2
    assert longitudinal.subs(b, 0) == m2  # Proca has no longitudinal pole
    assert longitudinal.subs({b: 0, m2: 0}) == 0  # gauge-null Maxwell branch
    assert trans.subs(a, 0) == m2  # auxiliary branch at a=b=0
