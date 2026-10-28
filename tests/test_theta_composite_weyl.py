# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""G1: composite Weyl 1-forms from a declared Mat(2,C) trial carrier.

All checks are exact restricted algebra. This is NOT an SU(2,2) connection,
a proof of strict tetrad reality, an action, or a graviton spectrum.
"""
import unittest
import sympy as s

t, x, a = s.symbols("t x a", real=True)
B = s.diag(1, -1, -1, -1, 1, -1, -1, -1)
J = s.zeros(8)
J[:4, 4:] = -s.eye(4)
J[4:, :4] = s.eye(4)
q = s.Matrix([1, x, 0, 0, t, 0, 0, 0])
coordinates = (t, x)


def pairing(v, w):
    return s.simplify((v.T * B * w)[0])


def norm(q_):
    return pairing(q_, q_)


def current(q_):
    n = norm(q_)
    return s.Matrix([s.simplify(pairing(J*q_, q_.diff(c))/n)
                     for c in coordinates])


def exact_weyl(q_):
    n = norm(q_)
    return s.Matrix([-s.diff(n, c)/(2*n) for c in coordinates])


def curl_xt(one_form):
    return s.factor(s.diff(one_form[0], x)-s.diff(one_form[1], t))


class TestCompositeWeylG1(unittest.TestCase):
    def test_target_J_orthogonality(self):
        self.assertEqual(J.T*B*J, B)
        self.assertEqual(J.T*B+B*J, s.zeros(8))
        self.assertEqual(norm(q), 1+t*t-x*x)

    def test_uniqueness_of_norm_only_weyl_ansatz(self):
        N = s.symbols("N", positive=True)
        f = s.symbols("f", real=True)
        self.assertEqual(s.solve(2*N*f+1, f), [-1/(2*N)])

    def test_norm_only_curvature_zero(self):
        self.assertEqual(curl_xt(exact_weyl(q)), 0)

    def test_nonexact_shape_current_and_curvature(self):
        n = 1+t*t-x*x
        self.assertEqual(current(q), s.Matrix([1/n, 0]))
        self.assertEqual(s.simplify(curl_xt(current(q))-2*x/n**2), 0)
        self.assertEqual(s.simplify(
            curl_xt(exact_weyl(q)+a*current(q))-2*a*x/n**2), 0)

    def test_real_scale_transformation(self):
        lam = t*x
        qp = s.exp(lam)*q
        self.assertEqual(s.simplify(norm(qp)-s.exp(2*lam)*norm(q)), 0)
        self.assertEqual(s.simplify(current(qp)-current(q)), s.zeros(2,1))
        desired = s.Matrix([s.diff(lam, c) for c in coordinates])
        self.assertEqual(s.simplify(exact_weyl(qp)-exact_weyl(q)+desired),
                         s.zeros(2,1))

    def test_local_complex_phase_transformation(self):
        alpha = t*x
        qp = s.cos(alpha)*q+s.sin(alpha)*J*q
        dalpha = s.Matrix([s.diff(alpha, c) for c in coordinates])
        self.assertEqual(s.trigsimp(s.simplify(norm(qp)-norm(q))), 0)
        self.assertEqual(s.trigsimp(s.simplify(current(qp)-current(q)-dalpha)),
                         s.zeros(2,1))
        self.assertEqual(s.trigsimp(s.simplify(exact_weyl(qp)-exact_weyl(q))),
                         s.zeros(2,1))
        # u_a transforms with an unwanted a*dalpha if local U(1) is independent.

    def test_constant_lorentz_boost_invariance(self):
        boost = s.eye(4)
        boost[0,0] = boost[1,1] = s.Rational(5,4)
        boost[0,1] = boost[1,0] = s.Rational(3,4)
        L = s.diag(boost, boost)
        self.assertEqual(L.T*B*L, B)
        self.assertEqual(L*J, J*L)
        self.assertEqual(s.simplify(current(L*q)-current(q)), s.zeros(2,1))

    def test_hermitian_reality_obstruction_on_trial_patch(self):
        # Theta=(1+i*t)I+x*sigma1+y*sigma2+z*sigma3.
        # At origin, N=1, u_norm=0, j=dt and D_t Theta=iI+aI.
        I2 = s.eye(2)
        D_t_theta = s.I*I2+a*I2
        anti = s.simplify((D_t_theta-D_t_theta.conjugate().T)/2)
        self.assertEqual(anti, s.I*I2)
        herm = s.simplify((D_t_theta+D_t_theta.conjugate().T)/2)
        self.assertEqual(herm, a*I2)


if __name__ == "__main__":
    unittest.main()
