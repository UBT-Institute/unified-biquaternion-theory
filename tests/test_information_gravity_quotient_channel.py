"""Conditional gravity-quotient obstruction for the chosen full-Theta information channel.

No physical UBT state, action, gauge fixing or observer coupling is selected here.
The positive-H graded comparator is an ALREADY DEFINED restricted model.
"""
import unittest
import sympy as sp

I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
ETA = sp.diag(-1, 1, 1, 1)


def flat_gravity_lift(cosh, sinh):
    """Original full-Theta local Gaussian lift with the same exact coframe."""
    cosh, sinh = sp.sympify(cosh), sp.sympify(sinh)
    du = sp.Matrix([cosh, sinh, 0, 0])
    x = ETA * du
    q = (x.T * ETA * x)[0]
    assert sp.simplify(q + 1) == 0
    # At the common origin u=0, h=exp(u)=1 and w_mu=-partial_mu u.
    w = -du
    k_matrices = []
    for mu in range(4):
        e = sp.eye(4)[:, mu]
        r = e + du[mu] * x  # d_mu X=0, w_mu X=-du_mu X
        x_lower = ETA * x
        r_lower = ETA * r
        k_lower = (r_lower * x_lower.T - x_lower * r_lower.T) / q
        k = ETA * k_lower
        assert sp.simplify(k.T * ETA + ETA * k) == sp.zeros(4)
        assert sp.simplify(k * x - r) == sp.zeros(4, 1)
        # Whole original sharp-real coframe: dX + K X + w X = e.
        assert sp.simplify(k * x + w[mu] * x - e) == sp.zeros(4, 1)
        k_matrices.append(k)
    # X = i(x^0 I - x^1 sigma_x) is the EXISTING anti-Hermitian
    # part of the SAME complex biquaternion; no second dynamical field.
    theta = (1 + sp.I * x[0]) * I2 - sp.I * x[1] * SX
    rho = sp.simplify(theta * theta.H / sp.trace(theta * theta.H))
    return theta, rho, k_matrices


class GravityQuotientInformationTests(unittest.TestCase):
    def test_same_exact_sharp_tetrad_but_distinct_full_theta(self):
        theta_a, rho_a, ka = flat_gravity_lift(1, 0)
        theta_b, rho_b, kb = flat_gravity_lift(sp.Rational(5, 4), sp.Rational(3, 4))
        self.assertNotEqual(theta_a, theta_b)
        self.assertEqual(rho_a, I2 / 2)
        self.assertEqual(rho_b, (I2 + sp.Rational(3, 5) * SX) / 2)
        self.assertEqual(theta_a.det(), -2 * sp.I)
        self.assertEqual(theta_b.det(), -sp.Rational(5, 2) * sp.I)
        self.assertNotEqual(ka[0], kb[0])

    def test_identical_geometric_observer_predicts_different_probabilities(self):
        effect = (I2 + SX) / 2
        pa = sp.trace(effect * flat_gravity_lift(1, 0)[1])
        pb = sp.trace(effect * flat_gravity_lift(sp.Rational(5, 4), sp.Rational(3, 4))[1])
        self.assertEqual(pa, sp.Rational(1, 2))
        self.assertEqual(pb, sp.Rational(4, 5))

    def test_all_rapidity_family_at_common_spacetime_point(self):
        chi = sp.symbols("chi", real=True)
        C, S = sp.cosh(chi), sp.sinh(chi)
        theta = (1 - sp.I * C) * I2 - sp.I * S * SX
        rho = sp.simplify(theta * theta.H / sp.trace(theta * theta.H))
        self.assertEqual(sp.simplify(sp.trigsimp(rho - (I2 + sp.tanh(chi) * SX) / 2)), sp.zeros(2))
        self.assertEqual(sp.simplify(sp.trigsimp(C ** 2 - S ** 2)), 1)

    def test_statistical_fisher_metric_is_positive_on_gravity_vertical_direction(self):
        chi = sp.symbols("chi", real=True)
        p = (1 + sp.tanh(chi)) / 2
        F = sp.simplify(sp.trigsimp(sp.diff(p, chi) ** 2 / (p * (1 - p))))
        self.assertEqual(sp.simplify(F - sp.sech(chi) ** 2), 0)
        self.assertEqual(F.subs(chi, 0), 1)

    def test_relative_entropy_reference_does_not_select_physical_label(self):
        chi = sp.symbols("chi", real=True)
        b = sp.tanh(chi)
        D = ((1 + b) * sp.log(1 + b) + (1 - b) * sp.log(1 - b)) / 2
        self.assertEqual(sp.simplify(sp.diff(D, chi).subs(chi, 0)), 0)
        self.assertEqual(sp.simplify(sp.diff(D, chi, 2).subs(chi, 0)), 1)
        exact = sp.Rational(4, 5) * sp.log(sp.Rational(8, 5)) + sp.Rational(1, 5) * sp.log(sp.Rational(2, 5))
        self.assertAlmostEqual(float(exact), 0.19274475702175742, places=12)

    def test_exact_clock_chain_rule_det_one(self):
        z = sp.symbols("z", real=True)
        n = sp.diag(sp.exp(z), sp.exp(-z))
        B = (I2 + n.inv()) / sp.sqrt(sp.trace(n) + 2)
        dn = sp.diff(n, z)
        dB = -n.inv() * dn * n.inv() / sp.sqrt(sp.trace(n) + 2) - (
            (I2 + n.inv()) * sp.trace(dn) / (2 * (sp.trace(n) + 2) ** sp.Rational(3, 2))
        )
        self.assertEqual(sp.simplify(sp.diff(B, z) - dB), sp.zeros(2))
        self.assertEqual(sp.simplify(sp.diff(B, z).subs(z, 0)), sp.diag(sp.Rational(-1, 2), sp.Rational(1, 2)))


if __name__ == "__main__":
    unittest.main()
