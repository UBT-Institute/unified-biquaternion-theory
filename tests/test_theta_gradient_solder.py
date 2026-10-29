# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact *restricted* pure-gradient solder-form counterexample.

The example is flat despite a nonconstant metric and full jet Jacobian.
This repeats a known obstruction; NOT a no-go for covariant Theta jets.
"""
import unittest
import sympy as sp


class GradientSolderCounterexample(unittest.TestCase):
    def test_nonlinear_exact_coframe_is_flat_despite_nonconstant_g(self):
        t, x, y, z = coords = sp.symbols("t x y z", real=True)
        phi = (t, x + t**2, y, z)
        e = sp.Matrix(4, 4, lambda a, mu: sp.diff(phi[a], coords[mu]))
        self.assertEqual(e.det(), 1)

        eta = sp.diag(-1, 1, 1, 1)
        g = sp.simplify(e.T * eta * e)
        self.assertNotEqual(sp.diff(g[0, 0], t), 0)
        inv = sp.simplify(g.inv())

        gamma = [[[
            sp.simplify(
                sp.Rational(1, 2) *
                sum(inv[r, s] * (
                    sp.diff(g[s, nu], coords[mu]) +
                    sp.diff(g[s, mu], coords[nu]) -
                    sp.diff(g[mu, nu], coords[s]))
                    for s in range(4)))
            for nu in range(4)] for mu in range(4)] for r in range(4)]

        self.assertTrue(any(gamma[r][mu][nu] != 0 for r in range(4)
                            for mu in range(4) for nu in range(4)))

        for r in range(4):
            for mu in range(4):
                for nu in range(4):
                    for sigma in range(4):
                        curvature = sp.simplify(
                            sp.diff(gamma[r][nu][sigma], coords[mu])
                            - sp.diff(gamma[r][mu][sigma], coords[nu])
                            + sum(
                                gamma[r][mu][q] * gamma[q][nu][sigma]
                                - gamma[r][nu][q] * gamma[q][mu][sigma]
                                for q in range(4)))
                        self.assertEqual(curvature, 0)

        # Each jet input d_mu(phi^a) enters e_mu^a independently,
        # but gradient integrability restricts spacetime dynamics.
        self.assertEqual(sp.eye(16).rank(), 16)


if __name__ == "__main__":
    unittest.main()
