"""Exact test of the Hamiltonian-selector obstruction, not a theta lift."""
import unittest
import sympy as sp


class SelectorNonuniqueness(unittest.TestCase):
    def setUp(self):
        self.x = sp.Matrix(sp.symbols("x0:8"))
        self.lam = sp.symbols("lam", real=True)
        self.k = sp.diag(1, -1, -1, -1, 1, -1, -1, -1)
        self.j = sp.Matrix.vstack(
            sp.Matrix.hstack(sp.zeros(4), -sp.eye(4)),
            sp.Matrix.hstack(sp.eye(4), sp.zeros(4))
        )
        self.omega = self.k * self.j
        self.b = (self.x.T * self.k * self.x)[0]
        self.h = self.b / 2 + self.lam * self.b**2 / 4
        self.flow = (1 + self.lam * self.b) * self.j * self.x

    def test_symplectic_structure(self):
        self.assertEqual(self.j**2, -sp.eye(8))
        self.assertEqual(self.omega.T, -self.omega)
        self.assertNotEqual(self.omega.det(), 0)

    def test_hamilton_equation(self):
        gradient = sp.Matrix([sp.diff(self.h, x) for x in self.x])
        # Omega(dot X,Y) = Y.T Omega.T dot X.
        self.assertEqual(sp.simplify(self.omega.T * self.flow - gradient), sp.zeros(8, 1))

    def test_conservation(self):
        gradient = sp.Matrix([sp.diff(self.b, x) for x in self.x])
        self.assertEqual(sp.simplify((gradient.T * self.flow)[0]), 0)

    def test_different_symmetry_compatible_flows(self):
        x0 = {v: int(i == 0) for i, v in enumerate(self.x)}
        f0 = self.flow.subs({**x0, self.lam: 0})
        f1 = self.flow.subs({**x0, self.lam: 1})
        self.assertNotEqual(f0, f1)
        self.assertEqual(f1, 2 * f0)

    def test_indefinite_carrier(self):
        self.assertEqual(self.k.eigenvals(), {1: 2, -1: 6})


if __name__ == "__main__":
    unittest.main()
