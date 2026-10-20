"""Unit tests for the algebraic quotient spectrum and test-field Hamiltonian.

Run: python -m unittest discover -s research_tracks/dodecahedral_action_cmb -p 'test_*.py'
No external dependencies.
"""
import math
import unittest

from spectral_dodecahedron import (
    character_dimension,
    eigenvalue,
    hamiltonian,
    heat_trace,
    invariant_dimension,
    nonconstant_spectral_proxy,
    scalar_multiplicity,
)


class TestDodecahedralSpectrum(unittest.TestCase):
    def test_two_independent_spectrum_methods(self):
        for n in range(0, 121):
            with self.subTest(n=n):
                self.assertEqual(invariant_dimension(n), character_dimension(n))

    def test_spectral_gap(self):
        self.assertEqual(scalar_multiplicity(0), 1)
        self.assertTrue(all(scalar_multiplicity(n) == 0 for n in range(1, 12)))
        self.assertEqual(eigenvalue(12), 168)

    def test_selected_multiplicities(self):
        expected = {0: 1, 12: 13, 20: 21, 24: 25,
                    30: 31, 32: 33, 36: 37, 60: 122}
        for n, mult in expected.items():
            with self.subTest(n=n):
                self.assertEqual(scalar_multiplicity(n), mult)
        self.assertTrue(all(invariant_dimension(n) == 0 for n in range(1, 121, 2)))

    def test_heat_trace_cutoff_convergence(self):
        self.assertAlmostEqual(heat_trace(0.05, 80), heat_trace(0.05, 160), places=10)
        self.assertAlmostEqual(heat_trace(0.05, 80, False),
                               heat_trace(0.05, 160, False), places=10)

    def test_large_scale_proxy_not_cmb(self):
        ratio = nonconstant_spectral_proxy(0.05, 150)
        self.assertGreater(ratio, 0)
        self.assertLess(ratio, 0.02)

    def test_hamiltonian_and_legendre_derivatives(self):
        u, p, a, rc, m, n = 0.2, 1.7, 1.5, 2.0, 0.4, 12
        h = lambda q, v: hamiltonian(q, v, a, rc, m, n)
        eps = 1e-6
        qdot = (h(u, p + eps) - h(u, p - eps)) / (2 * eps)
        minus_pdot = (h(u + eps, p) - h(u - eps, p)) / (2 * eps)
        omega2 = eigenvalue(n) / (a * rc) ** 2 + m * m
        self.assertAlmostEqual(qdot, p / a ** 3, places=7)
        self.assertAlmostEqual(minus_pdot, a ** 3 * omega2 * u, places=7)
        self.assertGreater(h(u, p), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            nonconstant_spectral_proxy(0.0)
        with self.assertRaises(ValueError):
            hamiltonian(1, 0, 0, 1, 0, 12)


if __name__ == "__main__":
    unittest.main()
