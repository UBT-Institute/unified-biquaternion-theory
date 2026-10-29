# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact finite algebra checks for a *conditional* SU(2,2) future-tube chart.

These checks do not establish that UBT Theta is a conformal compensator,
do not construct a Cartan connection, and do not analyze physical modes.
"""
import unittest
import sympy as sp

I = sp.I
S0 = sp.eye(2)
S1 = sp.Matrix([[0, 1], [1, 0]])
S2 = sp.Matrix([[0, -I], [I, 0]])
S3 = sp.diag(1, -1)
PAULI = (S0, S1, S2, S3)


def hermitian_minkowski(v):
    return sum((v[i] * PAULI[i] for i in range(4)), sp.zeros(2))


def tube_gram(u, v, Y):
    """Real symmetric part of the positive Hermitian form at Im(W)=Y>0."""
    U = hermitian_minkowski(u[:4]) + I * hermitian_minkowski(u[4:])
    V = hermitian_minkowski(v[:4]) + I * hermitian_minkowski(v[4:])
    return sp.simplify(sp.re(sp.trace(Y.inv() * U * Y.inv() * V.conjugate().T)))


class ConformalChartBoundary(unittest.TestCase):
    def test_minkowski_determinant(self):
        t, x, y, z = sp.symbols('t x y z', real=True)
        H = hermitian_minkowski((t, x, y, z))
        self.assertEqual(sp.simplify(H.det()), t*t-x*x-y*y-z*z)

    def test_full_tube_gram_at_identity_is_euclidean(self):
        Y = sp.eye(2)
        basis = [tuple(int(i == j) for i in range(8)) for j in range(8)]
        gram = sp.Matrix(8, 8, lambda i,j: tube_gram(basis[i], basis[j], Y))
        self.assertEqual(gram, 2*sp.eye(8))
        self.assertEqual(gram[:4,:4], 2*sp.eye(4))
        self.assertNotEqual(gram[:4,:4], 2*sp.diag(1,-1,-1,-1))

    def test_positive_metric_for_nontrivial_tube_imaginary_part(self):
        Y = sp.diag(sp.Rational(2,1), sp.Rational(3,2))
        v = (1, 2, -1, 3, -2, 1, 4, -1)
        self.assertGreater(tube_gram(v, v, Y), 0)
        self.assertEqual(tube_gram((0,) * 8, (0,) * 8, Y), 0)

    def test_lorentz_sl2c_congruence_preserves_cone_and_determinant(self):
        H = hermitian_minkowski((3, 1, 1, 0))
        Y = sp.diag(2, 1)
        S = sp.diag(2, sp.Rational(1,2))
        self.assertEqual(S.det(), 1)
        Hp = S*H*S.conjugate().T
        Yp = S*Y*S.conjugate().T
        self.assertEqual(sp.simplify(Hp.det()-H.det()), 0)
        self.assertTrue(Yp.is_positive_definite)

    def test_scalar_phase_is_not_global_tube_automorphism(self):
        H = sp.diag(1, -1)
        Y = sp.eye(2)
        W = H + I*Y
        rotated = I*W
        imag = (rotated-rotated.conjugate().T)/(2*I)
        self.assertEqual(sp.simplify(imag), H)
        self.assertFalse(imag.is_positive_definite)

    def test_two_homogeneous_spaces_are_not_same(self):
        dim_su22 = 15
        dim_k = 7  # s(u(2) + u(2))
        dim_p = 11 # co(1,3) semidirect R^4
        self.assertEqual(dim_su22-dim_k, 8)
        self.assertEqual(dim_su22-dim_p, 4)
        self.assertGreater(dim_k, 3)  # max compact P dim 3
        # Dimension checks alone are NOT a no-equivariant-map proof.
        # That group-theoretic argument is in RESEARCH.en.md.

if __name__ == "__main__":
    unittest.main()
