# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact rational unitary-gauge checks for the *Cartan comparator*.

Does NOT validate any equivariant Theta -> five-vector map, Dirac analysis,
physical ghost freedom, or UBT gravity closure.
"""

from fractions import Fraction
import unittest

ETA = (-1, 1, 1, 1, 1)


def connection_from_tetrad(e, ell):
    """A_mu^A_B in so(1,4); e[I][mu] is an arbitrary rational tetrad."""
    ell = Fraction(ell)
    if not ell:
        raise ValueError("nonzero compensator norm required")
    a = [[[Fraction(0) for _ in range(5)] for _ in range(5)]
         for _ in range(4)]
    for mu in range(4):
        for i in range(4):
            a[mu][i][4] = Fraction(e[i][mu]) / ell
            a[mu][4][i] = -ETA[i] * Fraction(e[i][mu]) / ell
    return a


def compensated_tetrad(a, ell):
    """E_mu^A = A_mu^A_B V^B, V^B=ell delta^B_4."""
    return [[Fraction(ell) * a[mu][i][4] for mu in range(4)]
            for i in range(5)]


class CartanCompensatorSeedChecks(unittest.TestCase):
    def test_exact_rank_sixteen(self):
        ell = Fraction(7, 3)
        outputs = []
        for i in range(4):
            for mu in range(4):
                e = [[Fraction(0) for _ in range(4)] for _ in range(4)]
                e[i][mu] = 1
                a = connection_from_tetrad(e, ell)
                E = compensated_tetrad(a, ell)
                self.assertEqual(E[:4], e)
                self.assertEqual(E[4], [0] * 4)
                outputs.append(tuple(E[j][nu] for j in range(4)
                                     for nu in range(4)))
        # Each input basis direction maps to its matching output basis vector.
        self.assertEqual(outputs, [
            tuple(int(i == j) for j in range(16)) for i in range(16)
        ])

    def test_connection_is_so_1_4(self):
        e = [[Fraction((i + 2) * (mu + 1), mu + 2)
              for mu in range(4)] for i in range(4)]
        a = connection_from_tetrad(e, Fraction(5, 2))
        for mu in range(4):
            for i in range(5):
                for j in range(5):
                    self.assertEqual(
                        ETA[i] * a[mu][i][j] + ETA[j] * a[mu][j][i],
                        0,
                    )

    def test_broken_curvature_quadratic_sign(self):
        ell = Fraction(3, 2)
        e = [[Fraction((i + 1) * (mu + 3), mu + i + 1)
              for mu in range(4)] for i in range(4)]
        a = connection_from_tetrad(e, ell)
        for i in range(4):
            for j in range(4):
                for mu in range(4):
                    for nu in range(4):
                        # F^{IJ} from A^I_4 ∧ A^{4J} only
                        from_a = (a[mu][i][4] * ETA[j] * a[nu][4][j]
                                  - a[nu][i][4] * ETA[j] * a[mu][4][j])
                        expected = -(e[i][mu] * e[j][nu]
                                     - e[i][nu] * e[j][mu]) / ell**2
                        self.assertEqual(from_a, expected)

    def test_pure_lorentz_connection_zero_jet_for_constant_v(self):
        a = [[[Fraction(0) for _ in range(5)] for _ in range(5)]
             for _ in range(4)]
        self.assertEqual(compensated_tetrad(a, 2),
                         [[0] * 4 for _ in range(5)])


if __name__ == "__main__":
    unittest.main()
