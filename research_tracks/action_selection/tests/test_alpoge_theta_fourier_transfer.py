"""Exact finite Fourier transfer sanity checks for UBT (research only).

This is NOT a theta lift, physical UBT dynamics, or a Lean proof.
"""
import unittest
from sympy import I, Matrix, Rational, diag, eye, kronecker_product, zeros, re, expand_complex


def matrices():
    # Matrix coefficient v=(a,b,c,d) for [[a,b],[c,d]].
    # B(X,Y)=Re Tr(adj(X)*Y^dagger) in real/imag coefficient blocks.
    h = Matrix([[0, 0, 0, 1], [0, -1, 0, 0],
                [0, 0, -1, 0], [1, 0, 0, 0]])
    n = 4
    f = Matrix(n, n, lambda k, j: I**(-k*j) / 2)
    a = f.applyfunc(lambda z: re(expand_complex(z)))
    b = f.applyfunc(lambda z: re(expand_complex(-I*z)))
    aa = kronecker_product(a, eye(4))
    bb = kronecker_product(b, eye(4))
    t = Matrix.vstack(Matrix.hstack(aa, -bb),
                      Matrix.hstack(bb, aa))
    k = diag(kronecker_product(eye(n), h),
             kronecker_product(eye(n), h))
    j = Matrix.vstack(Matrix.hstack(zeros(16), -eye(16)),
                      Matrix.hstack(eye(16), zeros(16)))
    omega = k * j
    w = diag(*(Rational(1, 2)**(j*j) for j in range(n)))
    w16 = kronecker_product(w, eye(4))
    g = diag(w16, w16)
    return h, f, t, k, j, omega, g


class FourierThetaTransferTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.h, cls.f, cls.t, cls.k, cls.j, cls.omega, cls.g = matrices()

    def test_indefinite_signature(self):
        self.assertEqual(self.h.eigenvals(), {1: 1, -1: 3})
        self.assertEqual(self.k.rank(), 32)
        # Per mode: 2 positive and 6 negative real directions.
        # Four modes: 8 positive and 24 negative real directions.

    def test_exact_dft_order_four(self):
        self.assertEqual(self.f**4, eye(4))
        self.assertEqual(self.t**4, eye(32))
        self.assertEqual(self.t*self.j, self.j*self.t)

    def test_exact_bilinear_and_symplectic_invariance(self):
        self.assertEqual(self.t.T*self.k*self.t, self.k)
        self.assertEqual(self.omega.T, -self.omega)
        self.assertEqual(self.t.T*self.omega*self.t, self.omega)

    def test_gaussian_smoothing_is_not_symplectic(self):
        self.assertNotEqual(self.g.T*self.omega*self.g, self.omega)
        self.assertNotEqual(self.g.T*self.k*self.g, self.k)

    def test_lorentz_boost_preserves_forms_but_blocks_positive_norm(self):
        # X -> S X S^dagger, S=diag(2,1/2), det(S)=1.
        # Complex coefficients (a,b,c,d) -> (4a,b,c,d/4).
        boost = diag(4, 1, 1, Rational(1, 4))
        r = diag(boost, boost)
        k8 = diag(self.h, self.h)
        j8 = Matrix.vstack(Matrix.hstack(zeros(4), -eye(4)),
                           Matrix.hstack(eye(4), zeros(4)))
        self.assertEqual(r.T*k8*r, k8)
        self.assertEqual(r.T*k8*j8*r, k8*j8)
        x = zeros(8, 1)
        x[0] = 1  # X=diag(1,0).
        self.assertEqual(r*x, 4*x)
        # A positive invariant norm P would require
        # P(x,x)=P(4x,4x)=16 P(x,x), contradiction.

    def test_negative_direction_survives(self):
        # Real b=1 in mode zero has B=-1.
        x = zeros(32, 1)
        x[1] = 1
        self.assertEqual((x.T*self.k*x)[0], -1)
        y = self.t*x
        self.assertEqual((y.T*self.k*y)[0], -1)

    def test_metric_not_preserved_at_fixed_psi(self):
        sx = Matrix([[0, 1], [1, 0]])
        sy = Matrix([[0, -I], [I, 0]])
        sz = diag(1, -1)
        e = [I*eye(2), I*sx, I*sy, I*sz]
        eta = [-1, 1, 1, 1]
        for mu in range(4):
            for nu in range(4):
                pairing = (e[mu].adjugate()*e[nu]
                           + e[nu].adjugate()*e[mu]) / 2
                expected = eta[mu]*eye(2) if mu == nu else zeros(2)
                self.assertEqual(pairing, expected)
        # Pure zero psi-mode -> four output modes of amplitude 1/2 each.
        # Their sum at psi=0 scales the tetrad by two and the metric by four.
        scale = sum(self.f[k, 0] for k in range(4))
        self.assertEqual(scale, 2)
        for mu in range(4):
            pairing = (scale*e[mu]).adjugate()*(scale*e[mu])
            self.assertEqual(pairing, 4*eta[mu]*eye(2))


if __name__ == "__main__":
    unittest.main()
