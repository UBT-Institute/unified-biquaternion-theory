"""Exact conditional full-biquaternion observer readout tests (NOT physical UBT selection)."""
import unittest
import sympy as sp

I2 = sp.eye(2)
SZ = sp.diag(1, -1)
SX = sp.Matrix([[0, 1], [1, 0]])


def rho(theta, observer):
    """Positive two-level observer-reference readout: det observer = 1."""
    if sp.simplify(observer.det() - 1):
        raise ValueError("test observer determinant must be one")
    n_isqrt = (observer.inv() + I2) / sp.sqrt(sp.trace(observer) + 2)
    t = n_isqrt * theta * n_isqrt
    q = sp.simplify(t * t.H)
    return sp.simplify(q / sp.trace(q))


class InformationChannelTests(unittest.TestCase):
    def test_full_complex_matrix_and_normalization(self):
        theta = sp.Matrix([[2, sp.I], [1 - sp.I, 1]])
        out = rho(theta, I2)
        self.assertEqual(sp.simplify(out - out.H), sp.zeros(2))
        self.assertEqual(sp.simplify(sp.trace(out)), 1)
        self.assertEqual(out, sp.Matrix([
            [sp.Rational(5, 8), sp.Rational(1, 4) + 3 * sp.I / 8],
            [sp.Rational(1, 4) - 3 * sp.I / 8, sp.Rational(3, 8)],
        ]))
        self.assertEqual(sp.simplify(out.det() - sp.Rational(1, 32)), 0)

    def test_nontrivial_lorentz_congruence_transport(self):
        theta = sp.Matrix([[2, sp.I], [1 - sp.I, 1]])
        s = sp.Matrix([[1, 1], [0, 1]])
        n1 = s * s.H
        u = sp.simplify((n1.inv() + I2) / sp.sqrt(sp.trace(n1) + 2) * s)
        self.assertEqual(sp.simplify(u * u.H - I2), sp.zeros(2))
        self.assertNotEqual(u, I2)
        self.assertEqual(
            sp.simplify(rho(s * theta * s.H, n1) - u * rho(theta, I2) * u.H),
            sp.zeros(2),
        )
        proj = sp.diag(1, 0)
        self.assertEqual(
            sp.simplify(
                sp.trace(rho(theta, I2) * proj)
                - sp.trace(rho(s * theta * s.H, n1) * u * proj * u.H)
            ),
            0,
        )

    def test_wrong_fixed_observer_breaks_covariance(self):
        s = sp.diag(2, sp.Rational(1, 2))
        boosted = s * s.H
        self.assertEqual(rho(I2, I2), I2 / 2)
        self.assertNotEqual(rho(boosted, I2), I2 / 2)
        self.assertEqual(rho(boosted, boosted), I2 / 2)

    def test_pure_rank_boundary_still_normalized(self):
        theta = sp.diag(1, 0)
        self.assertEqual(rho(theta, I2), theta)
        self.assertEqual(rho(theta, I2).det(), 0)

    def test_normalized_state_determinant(self):
        a, b = sp.symbols("a b", positive=True)
        theta = sp.diag(a, b)
        d = sp.simplify(rho(theta, I2).det())
        self.assertEqual(sp.simplify(d - a * a * b * b / (a * a + b * b) ** 2), 0)

    def test_observer_choice_changes_spectrum(self):
        theta = sp.diag(2, 1)
        self.assertEqual(rho(theta, I2), sp.diag(sp.Rational(4, 5), sp.Rational(1, 5)))
        b = sp.sqrt(2)
        n = sp.diag(b, 1 / b)
        self.assertEqual(rho(theta, n), I2 / 2)

    def test_right_unitary_phase_winding_invisible(self):
        psi, radius = sp.symbols("psi R", real=True, positive=True)
        n = sp.symbols("n", integer=True)
        theta = sp.diag(2, 1)
        v = sp.diag(sp.exp(sp.I * n * psi / radius), 1)
        self.assertEqual(sp.simplify(rho(theta * v, I2) - rho(theta, I2)), sp.zeros(2))
        self.assertEqual(
            sp.simplify((theta * v).det() / theta.det() - sp.exp(sp.I * n * psi / radius)),
            0,
        )

    def test_kernel_of_tangent_map_is_five_real_dimensions(self):
        theta = sp.diag(2, 1)
        sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
        directions = [I2, sp.I * I2, sp.I * SX, sp.I * sy, sp.I * SZ]
        q = theta * theta.H
        for a in directions:
            v = theta * a
            dq = v * theta.H + theta * v.H
            drho = sp.simplify(dq / sp.trace(q) - q * sp.trace(dq) / sp.trace(q) ** 2)
            self.assertEqual(drho, sp.zeros(2))

        def coords(m):
            return sp.Matrix([
                sp.re(m[0, 0]), sp.re(m[0, 1]), sp.re(m[1, 0]), sp.re(m[1, 1]),
                sp.im(m[0, 0]), sp.im(m[0, 1]), sp.im(m[1, 0]), sp.im(m[1, 1]),
            ])
        self.assertEqual(sp.Matrix.hstack(*(coords(theta * a) for a in directions)).rank(), 5)

    def test_channel_map_jacobian_has_rank_three(self):
        theta = sp.diag(2, 1)
        directions = []
        for i in range(2):
            for j in range(2):
                m = sp.zeros(2)
                m[i, j] = 1
                directions.extend([m, sp.I * m])
        q = theta * theta.H

        def differential(v):
            dq = v * theta.H + theta * v.H
            return sp.simplify(dq / sp.trace(q) - q * sp.trace(dq) / sp.trace(q) ** 2)

        def bloch(m):
            return sp.Matrix([
                sp.re(m[0, 1] + m[1, 0]),
                sp.im(m[1, 0] - m[0, 1]),
                m[0, 0] - m[1, 1],
            ])
        jacobian = sp.Matrix.hstack(*(bloch(differential(v)) for v in directions))
        self.assertEqual(jacobian.rank(), 3)

    def test_different_hamiltonians_both_preserve_readout_axioms(self):
        r, omega, t = sp.symbols("r omega t", real=True)
        evolution = sp.diag(sp.exp(-sp.I * omega * t), sp.exp(sp.I * omega * t))
        rho0 = (I2 + r * SX) / 2
        evolved = sp.simplify(evolution * rho0 * evolution.H)
        p = sp.simplify(sp.trace((I2 + SX) * evolved / 2))
        self.assertEqual(
            sp.trigsimp(sp.expand_complex(p) - (1 + r * sp.cos(2 * omega * t)) / 2),
            0,
        )
        self.assertEqual(sp.simplify(sp.trace(evolved)), 1)
        self.assertEqual(sp.simplify(evolved.det() - rho0.det()), 0)
        self.assertNotEqual(sp.simplify(sp.diff(p, t)), 0)
        self.assertEqual(sp.simplify(p.subs(omega, 0)), (1 + r) / 2)

    def test_fisher_does_not_select_frequency(self):
        r, omega, t = sp.symbols("r omega t", real=True)
        p = (1 + r * sp.cos(2 * omega * t)) / 2
        fisher = sp.diff(p, omega) ** 2 / (p * (1 - p))
        expected = (
            4 * r * r * t * t * sp.sin(2 * omega * t) ** 2
            / (1 - r * r * sp.cos(2 * omega * t) ** 2)
        )
        self.assertEqual(sp.trigsimp(fisher - expected), 0)



class MultiObserverTests(unittest.TestCase):
    def test_three_clock_matrix_commutant_is_only_scalars(self):
        n2 = sp.diag(2, sp.Rational(1, 2))
        n3 = sp.Matrix([[2, 1], [1, 1]])
        self.assertEqual(n2.det(), 1)
        self.assertEqual(n3.det(), 1)
        a, b, c, d = sp.symbols("a b c d")
        u = sp.Matrix([[a, b], [c, d]])
        conditions = list(n2 * u - u * n2) + list(n3 * u - u * n3)
        matrix = sp.linear_eq_to_matrix(conditions, [a, b, c, d])[0]
        self.assertEqual(matrix.rank(), 3)
        self.assertEqual(matrix.nullspace(), [sp.Matrix([1, 0, 0, 1])])

    def test_two_clocks_leave_relative_phase_invisible(self):
        n2 = sp.diag(2, sp.Rational(1, 2))
        n3 = sp.Matrix([[2, 1], [1, 1]])
        theta = I2
        theta2 = sp.diag(-1, 1)
        self.assertEqual(rho(theta, I2), rho(theta2, I2))
        self.assertEqual(rho(theta, n2), rho(theta2, n2))
        self.assertNotEqual(rho(theta, n3), rho(theta2, n3))

    def test_all_clocks_still_blind_to_complex_scalar(self):
        theta = sp.Matrix([[2, sp.I], [1 - sp.I, 1]])
        clocks = [I2, sp.diag(2, sp.Rational(1, 2)), sp.Matrix([[2, 1], [1, 1]])]
        for n in clocks:
            self.assertEqual(sp.simplify(rho(theta, n) - rho(3 * sp.I * theta, n)), sp.zeros(2))

    def test_joint_three_clock_readout_has_rank_six(self):
        theta = I2
        clocks = [I2, sp.diag(2, sp.Rational(1, 2)), sp.Matrix([[2, 1], [1, 1]])]
        directions = []
        for i in range(2):
            for j in range(2):
                m = sp.zeros(2)
                m[i, j] = 1
                directions.extend([m, sp.I * m])
        columns = []
        for v in directions:
            combined = []
            for n in clocks:
                b = (n.inv() + I2) / sp.sqrt(sp.trace(n) + 2)
                t = b * theta * b
                dt = b * v * b
                q = t * t.H
                dq = dt * t.H + t * dt.H
                derivative = sp.simplify(
                    dq / sp.trace(q) - q * sp.trace(dq) / sp.trace(q) ** 2
                )
                combined.extend([
                    sp.re(derivative[0, 1] + derivative[1, 0]),
                    sp.im(derivative[1, 0] - derivative[0, 1]),
                    sp.simplify(derivative[0, 0] - derivative[1, 1]),
                ])
            columns.append(sp.Matrix(combined))
        self.assertEqual(sp.Matrix.hstack(*columns).rank(), 6)


class InformationalCompletenessTests(unittest.TestCase):
    def test_tetrahedral_povm_local_fisher_metric(self):
        sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
        directions = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
        effects = [
            (I2 + (x * SX + y * sy + z * SZ) / sp.sqrt(3)) / 4
            for x, y, z in directions
        ]
        self.assertEqual(sp.simplify(sum(effects, sp.zeros(2)) - I2), sp.zeros(2))
        for effect in effects:
            self.assertEqual(sorted(effect.eigenvals()), [0, sp.Rational(1, 2)])
        r1, r2, r3 = sp.symbols("r1 r2 r3", real=True)
        density = (I2 + r1 * SX + r2 * sy + r3 * SZ) / 2
        probabilities = [sp.simplify(sp.trace(effect * density)) for effect in effects]
        self.assertEqual(sum(probabilities), 1)
        fisher = sp.zeros(3)
        for p in probabilities:
            derivative = sp.Matrix([sp.diff(p, r) for r in (r1, r2, r3)])
            fisher += sp.simplify(
                derivative * derivative.T
                / p.subs({r1: 0, r2: 0, r3: 0})
            )
        self.assertEqual(sp.simplify(fisher - sp.eye(3) / 3), sp.zeros(3))

if __name__ == "__main__":
    unittest.main()
