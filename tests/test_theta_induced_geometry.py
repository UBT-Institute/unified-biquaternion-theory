# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact tests for a RESTRICTED Mat(2,C) induced-metric Theta construction.

No independent tetrad is supplied. This demonstrates nonzero curvature on a
Lorentz-real patch, but NOT full SU(2,2) covariance, propagation of gravitons,
a full UBT action, or evasion of PR #807's *stated* bare-action theorem.
"""
import unittest
import sympy as s

I = s.I
ID = s.eye(2)
SIGMA = (
    ID, s.Matrix([[0, 1], [1, 0]]),
    s.Matrix([[0, -I], [I, 0]]), s.diag(1, -1),
)


def sharp(A):
    return s.Matrix([[A[1, 1], -A[0, 1]], [-A[1, 0], A[0, 0]]])


def H(A):
    return s.simplify(s.trace(sharp(A) * A.conjugate().T))


def bilinear(A, B):
    """H polarization normalized to the (+---+---) real matrix."""
    return s.simplify((H(A + B) - H(A) - H(B)) / 4)


k, t, x, y, z = s.symbols("k t x y z", real=True)
coords = (t, x, y, z)
eta = s.diag(1, -1, -1, -1)
Theta = sum((coords[i] * SIGMA[i] for i in range(4)), s.zeros(2))
Theta += I * k * t * x * SIGMA[1]
jet = [Theta.diff(v) for v in coords]
metric = s.Matrix(4, 4, lambda a, b: bilinear(jet[a], jet[b]))
df = s.Matrix([k * x, k * t, 0, 0])
expected = eta - df * df.T


class TestThetaInducedGeometry(unittest.TestCase):
    def test_pairing_inertia_and_minkowski(self):
        basis = SIGMA + tuple(I * m for m in SIGMA)
        gram = s.Matrix(8, 8, lambda a, b: bilinear(basis[a], basis[b]))
        self.assertEqual(gram, s.diag(1, -1, -1, -1, 1, -1, -1, -1))

    def test_lorentz_and_global_phase_invariance(self):
        S = s.diag(2, s.Rational(1, 2))
        phase = -I
        basis = SIGMA + tuple(I * m for m in SIGMA)
        for a in range(8):
            for b in range(8):
                A = phase * S * basis[a] * S.conjugate().T
                B = phase * S * basis[b] * S.conjugate().T
                self.assertEqual(s.simplify(
                    bilinear(A, B) - bilinear(basis[a], basis[b])), 0)

    def test_metric_and_nondegenerate_patch(self):
        self.assertEqual(s.simplify(metric - expected), s.zeros(4))
        self.assertEqual(s.factor(metric.det()), k**2*x**2-k**2*t**2-1)

    def test_explicit_real_lorentz_coframe(self):
        D = 1-k**2*x**2
        A = 1+k**2*t**2-k**2*x**2
        frame = s.Matrix([
            [s.sqrt(D), -k**2*t*x/s.sqrt(D), 0, 0],
            [0, s.sqrt(A/D), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ])
        self.assertEqual(s.simplify(frame.T*eta*frame-metric), s.zeros(4))

    def test_exact_nonzero_curvature_at_origin(self):
        # The (y,z) product block is flat. Compute the (t,x) block.
        q = (t, x)
        g2 = metric[:2, :2]
        inv = s.simplify(g2.inv())
        Gamma = [[[
            s.simplify(s.Rational(1, 2) * sum(
                inv[r, a] * (
                    s.diff(g2[a, j], q[i]) +
                    s.diff(g2[a, i], q[j]) -
                    s.diff(g2[i, j], q[a])
                ) for a in range(2)))
            for j in range(2)] for i in range(2)] for r in range(2)]
        R = s.factor(
            s.diff(Gamma[0][1][1], t) -
            s.diff(Gamma[0][0][1], x) +
            sum(Gamma[0][0][a]*Gamma[a][1][1] -
                Gamma[0][1][a]*Gamma[a][0][1] for a in range(2)))
        self.assertEqual(s.simplify(
            R-k**2*(1+k**2*t**2)/(1+k**2*(t**2-x**2))**2), 0)
        self.assertEqual(R.subs({t:0, x:0}), k**2)

    def test_jet_to_metric_rank_ten_not_tetrad_rank_sixteen(self):
        # 32 free first-jet numbers: 8 target directions x 4 spacetime.
        # On affine flat embedding only the first four target
        # directions affect g at first order.
        target_signs = [1, -1, -1, -1, 1, -1, -1, -1]
        pairs = [(a, b) for a in range(4) for b in range(a, 4)]
        linear_map = s.zeros(len(pairs), 32)
        for row, (mu, nu) in enumerate(pairs):
            linear_map[row, mu*4+nu] += target_signs[mu]
            linear_map[row, nu*4+mu] += target_signs[nu]
        self.assertEqual(linear_map.rank(), 10)
        self.assertEqual(linear_map[:, 16:], s.zeros(10, 16))

    def test_no_linearized_metric_graviton_on_affine_background(self):
        eps = s.symbols("eps", real=True)
        normal_metric = eta - eps**2*df*df.T
        self.assertEqual(
            s.diff(normal_metric, eps).subs(eps, 0), s.zeros(4))
        # Tangential deviations produce the Lie derivative of eta.
        u = (t*x, t**2, y*z, x*z)
        frame = s.Matrix(4, 4, lambda a, mu:
            int(a == mu) + eps*s.diff(u[a], coords[mu]))
        g = s.expand(frame.T * eta * frame)
        linear = s.simplify(g.diff(eps).subs(eps, 0))
        Lie = s.Matrix(4, 4, lambda a, b:
            sum(eta[a, c]*s.diff(u[c], coords[b])
                + eta[b, c]*s.diff(u[c], coords[a])
                for c in range(4)))
        self.assertEqual(s.simplify(linear - Lie), s.zeros(4))


if __name__ == "__main__":
    unittest.main()
