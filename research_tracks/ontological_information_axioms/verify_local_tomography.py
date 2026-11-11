# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""OI-6: Local tomography of real versus complex two-level systems.

Elementary established quantum foundations, not proof of complex physics from
information alone, and not a new UBT dynamical theorem. Standard library only.
"""
from fractions import Fraction
from itertools import product
import unittest


def eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a))) for i in range(len(a)))


def scale(a, factor):
    return tuple(tuple(factor * value for value in row) for row in a)


def multiply(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0])))


def adjoint(a):
    return tuple(tuple(complex(a[j][i]).conjugate() for j in range(len(a)))
                 for i in range(len(a[0])))


def kron(a, b):
    return tuple(tuple(a[i // len(b)][j // len(b[0])] *
                       b[i % len(b)][j % len(b[0])]
                       for j in range(len(a[0]) * len(b[0])))
                 for i in range(len(a) * len(b)))


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def real_rank(vectors):
    """Exact row rank of integer or rational vectors using Gaussian elimination."""
    rows = [[Fraction(x) for x in row] for row in vectors]
    if not rows:
        return 0
    pivot_row = 0
    for column in range(len(rows[0])):
        pivot = next((r for r in range(pivot_row, len(rows))
                      if rows[r][column] != 0), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        factor = rows[pivot_row][column]
        rows[pivot_row] = [x / factor for x in rows[pivot_row]]
        for row in range(len(rows)):
            if row != pivot_row:
                factor = rows[row][column]
                if factor:
                    rows[row] = [x - factor * y for x, y in zip(rows[row], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def flatten(a):
    return [value for row in a for value in row]


I2 = eye(2)
I4 = eye(4)
X = ((0, 1), (1, 0))
Z = ((1, 0), (0, -1))
J = ((0, -1), (1, 0))
Y = scale(J, 1j)
REAL_LOCAL = (I2, X, Z)
COMPLEX_LOCAL = (I2, X, Y, Z)
W = kron(J, J)
PROJ_PLUS = scale(add(I4, W), Fraction(1, 2))
PROJ_MINUS = scale(add(I4, scale(W, -1)), Fraction(1, 2))
RHO_PLUS = scale(PROJ_PLUS, Fraction(1, 2))
RHO_MINUS = scale(PROJ_MINUS, Fraction(1, 2))


class LocalTomographyTests(unittest.TestCase):
    def test_real_holistic_operator_is_symmetric_involution(self):
        self.assertEqual(transpose(J), scale(J, -1))
        self.assertEqual(transpose(W), W)
        self.assertEqual(multiply(W, W), I4)
        self.assertEqual(trace(W), 0)

    def test_two_distinct_valid_global_states(self):
        self.assertEqual(trace(RHO_PLUS), 1)
        self.assertEqual(trace(RHO_MINUS), 1)
        self.assertNotEqual(RHO_PLUS, RHO_MINUS)
        self.assertEqual(multiply(PROJ_PLUS, PROJ_PLUS), PROJ_PLUS)
        self.assertEqual(multiply(PROJ_MINUS, PROJ_MINUS), PROJ_MINUS)
        self.assertEqual(multiply(PROJ_PLUS, PROJ_MINUS), scale(I4, 0))
        # Symmetric projectors are positive semidefinite; each rho is P/2.

    def test_product_measurements_cannot_distinguish_rebit_states(self):
        difference = add(RHO_PLUS, scale(RHO_MINUS, -1))
        self.assertEqual(difference, scale(W, Fraction(1, 2)))
        for a, b in product(REAL_LOCAL, repeat=2):
            effect = kron(a, b)
            self.assertEqual(trace(multiply(effect, difference)), 0)
        # Genuine positive local projective effects also cannot distinguish.
        effects = [scale(add(I2, scale(op, sign)), Fraction(1, 2))
                   for op in (X, Z) for sign in (-1, 1)]
        for a, b in product(effects, repeat=2):
            self.assertEqual(trace(multiply(kron(a, b), difference)), 0)

    def test_global_real_measurement_does_distinguish(self):
        self.assertEqual(trace(multiply(RHO_PLUS, PROJ_PLUS)), 1)
        self.assertEqual(trace(multiply(RHO_MINUS, PROJ_PLUS)), 0)
        self.assertEqual(trace(multiply(RHO_MINUS, PROJ_MINUS)), 1)
        self.assertEqual(trace(multiply(RHO_PLUS, PROJ_MINUS)), 0)

    def test_real_product_span_is_nine_global_dimension_is_ten(self):
        local_products = [flatten(kron(a, b)) for a, b in product(REAL_LOCAL, repeat=2)]
        self.assertEqual(real_rank(local_products), 9)
        self.assertEqual(real_rank(local_products + [flatten(W)]), 10)
        self.assertTrue(all(trace(multiply(W, kron(a, b))) == 0
                            for a, b in product(REAL_LOCAL, repeat=2)))

    def test_complex_product_hermitian_basis_has_full_rank(self):
        basis = [kron(a, b) for a, b in product(COMPLEX_LOCAL, repeat=2)]
        self.assertEqual(len(basis), 16)
        for i, a in enumerate(basis):
            self.assertEqual(adjoint(a), a)
            for j, b in enumerate(basis):
                self.assertAlmostEqual(trace(multiply(a, b)).real, 4 if i == j else 0)
                self.assertAlmostEqual(trace(multiply(a, b)).imag, 0)
        # 16 nonzero orthogonal Hermitian matrices form a real basis of Herm(4,C).

    def test_complex_local_y_correlations_recover_missing_rebit_bit(self):
        yy = kron(Y, Y)
        self.assertEqual(yy, scale(W, -1))
        self.assertEqual(trace(multiply(RHO_PLUS, yy)), -1)
        self.assertEqual(trace(multiply(RHO_MINUS, yy)), 1)
        self.assertEqual(adjoint(Y), Y)
        self.assertNotEqual(transpose(Y), Y)

    def test_parameter_counts_and_classical_countermodel(self):
        for parties in range(1, 5):
            dim = 2 ** parties
            real_global = dim * (dim + 1) // 2
            complex_global = dim ** 2
            self.assertEqual(complex_global, 4 ** parties)
            if parties == 1:
                self.assertEqual(real_global, 3 ** parties)
            else:
                self.assertGreater(real_global, 3 ** parties)
        self.assertEqual((10 - 9, 36 - 27, 136 - 81), (1, 9, 55))
        classical_basis = (
            ((1, 0), (0, 0)),
            ((0, 0), (0, 1)),
        )
        vectors = [flatten(kron(a, b)) for a, b in product(classical_basis, repeat=2)]
        self.assertEqual(real_rank(vectors), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
