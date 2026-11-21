"""Exact local O(1,3) x SL(2,R) Howe-pair gates on one UBT biquaternion.

This implements the real symplectic representation and tests only algebraic
compatibility and off-shell canonical-metric counterexamples. No global
automorphic theta lift, quantized UBT, physical energy or GR action is proved.
"""
import unittest
import sympy as sp


def lift2(t):
    eye, zero = sp.eye(4), sp.zeros(4)
    return sp.Matrix.vstack(
        sp.Matrix.hstack(t[0, 0] * eye, t[0, 1] * eye),
        sp.Matrix.hstack(t[1, 0] * eye, t[1, 1] * eye),
    )


def sharp(x):
    return x.adjugate()


class LocalHowePairTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.eta = sp.diag(1, -1, -1, -1)
        cls.z4 = sp.zeros(4)
        cls.b = 2 * sp.diag(cls.eta, cls.eta)
        cls.omega = 2 * sp.Matrix.vstack(
            sp.Matrix.hstack(cls.z4, -cls.eta),
            sp.Matrix.hstack(cls.eta, cls.z4),
        )
        cls.lie = []
        for j in (1, 2, 3):
            k = sp.zeros(4)
            k[0, j] = k[j, 0] = 1
            cls.lie.append(k)
        for j, k in ((1, 2), (1, 3), (2, 3)):
            r = sp.zeros(4)
            r[j, k], r[k, j] = 1, -1
            cls.lie.append(r)

    def test_full_sl2_symplectic_multiplier(self):
        a, b, c, d = sp.symbols("a b c d")
        t = sp.Matrix([[a, b], [c, d]])
        lift = lift2(t)
        self.assertEqual(
            sp.simplify(lift.T * self.omega * lift),
            (a * d - b * c) * self.omega,
        )

    def test_lorentz_and_sl2_commute(self):
        t = sp.Matrix([[2, 1], [1, 1]])  # determinant 1
        lift = lift2(t)
        for g in self.lie:
            self.assertEqual(g.T * self.eta + self.eta * g, sp.zeros(4))
            glift = sp.diag(g, g)
            self.assertEqual(glift.T * self.omega + self.omega * glift, sp.zeros(8))
            self.assertEqual(lift * glift, glift * lift)

    def test_lorentz_commutant_dimension_four(self):
        vars_ = sp.symbols("m0:64")
        m = sp.Matrix(8, 8, vars_)
        comms = []
        for g in self.lie:
            glift = sp.diag(g, g)
            comms.extend(list(m * glift - glift * m))
        linear, _ = sp.linear_eq_to_matrix(comms, vars_)
        self.assertEqual(linear.rank(), 60)  # 64 - 60 = 4

    def test_symplectic_part_of_commutant_is_sl2(self):
        a, b, c, d = sp.symbols("a b c d")
        t = lift2(sp.Matrix([[a, b], [c, d]]))
        self.assertEqual(
            sp.simplify(t.T * self.omega + self.omega * t),
            (a + d) * self.omega,
        )

    def test_sl2_symplectic_commutant_dimension_six(self):
        # Full SL(2,R) commutant has the form I2 ⊗ A, with A a 4x4
        # matrix. Symplecticity reduces to A.T eta + eta A = 0.
        z = sp.symbols("a0:16")
        a = sp.Matrix(4, 4, z)
        equations = list(a.T*self.eta + self.eta*a)
        linear, _ = sp.linear_eq_to_matrix(equations, z)
        self.assertEqual(linear.rank(), 10)  # 16 - 10 = 6 = dim so(1,3).

    def test_bilinear_invariant_only_under_orthogonal_sl2(self):
        phase = lift2(sp.Matrix([[0, -1], [1, 0]]))
        squeeze = lift2(sp.diag(2, sp.Rational(1, 2)))
        shear = lift2(sp.Matrix([[1, 1], [0, 1]]))
        self.assertEqual(phase.T * self.b * phase, self.b)
        for transform in (squeeze, shear):
            self.assertEqual(transform.T * self.omega * transform, self.omega)
            self.assertNotEqual(transform.T * self.b * transform, self.b)

    def test_squeeze_scales_canonical_metric(self):
        sigmas = [
            sp.eye(2),
            sp.Matrix([[0, 1], [1, 0]]),
            sp.Matrix([[0, -sp.I], [sp.I, 0]]),
            sp.diag(1, -1),
        ]
        jets = [sp.I * x for x in sigmas]
        eta_gr = sp.diag(-1, 1, 1, 1)
        for mu in range(4):
            for nu in range(4):
                metric = (sharp(jets[mu]) * jets[nu]
                          + sharp(jets[nu]) * jets[mu]) / 2
                self.assertEqual(metric, eta_gr[mu, nu] * sp.eye(2))
                transformed = [x / 2 for x in jets]  # u->2u, v->v/2; u=0
                new_metric = (
                    sharp(transformed[mu]) * transformed[nu]
                    + sharp(transformed[nu]) * transformed[mu]
                ) / 2
                self.assertEqual(new_metric, eta_gr[mu, nu] * sp.eye(2) / 4)

    def test_shear_breaks_lorentz_real_slice(self):
        # Starting at E0=i I, the u -> u+v shear changes E0 to (1+i) I.
        e0 = (1 + sp.I) * sp.eye(2)
        self.assertNotEqual(e0.conjugate().T, -e0)
        self.assertEqual(sp.simplify(sharp(e0) * e0), 2 * sp.I * sp.eye(2))

    def test_lorentz_invariant_fourier_kernel_phase(self):
        boost = sp.eye(4)
        boost[0, 0] = boost[1, 1] = sp.Rational(5, 4)
        boost[0, 1] = boost[1, 0] = sp.Rational(3, 4)
        self.assertEqual(boost.T * self.eta * boost, self.eta)
        q = sp.Matrix([1, 2, 3, 4])
        y = sp.Matrix([5, -1, 0, 2])
        self.assertEqual(
            (q.T * self.eta * y)[0],
            ((boost * q).T * self.eta * (boost * y))[0],
        )

    def test_full_dual_pair_invariant_gram_determinant(self):
        u, v = sp.Matrix(sp.symbols("u0:4")), sp.Matrix(sp.symbols("v0:4"))
        q = (u.T * self.eta * u)[0]
        r = (v.T * self.eta * v)[0]
        s = (u.T * self.eta * v)[0]
        delta = sp.expand(q * r - s**2)
        t = sp.Matrix([[2, 1], [1, 1]])
        u1, v1 = 2*u + v, u + v
        q1 = (u1.T * self.eta * u1)[0]
        r1 = (v1.T * self.eta * v1)[0]
        s1 = (u1.T * self.eta * v1)[0]
        self.assertEqual(sp.expand(q1*r1-s1**2-delta), 0)

    def test_indefinite_gaussian_diverges_on_spacelike_integer_ray(self):
        # Bare exp(-pi*y*Q(u)) grows when Q(u)<0.
        for k in range(1, 6):
            spacelike = sp.Matrix([0, k, 0, 0])
            self.assertEqual((spacelike.T*self.eta*spacelike)[0], -k*k)
        # The term magnitude is exp(+pi*y*k^2), not decaying.

    def test_tetrad_normal_majorant_positive(self):
        n = sp.Matrix([1, 0, 0, 0])
        r = 2*(self.eta*n)*(self.eta*n).T-self.eta
        self.assertEqual((n.T*self.eta*n)[0], 1)
        self.assertEqual(r, sp.eye(4))
        for k in range(1, 6):
            spacelike = sp.Matrix([0, k, 0, 0])
            self.assertEqual((spacelike.T*r*spacelike)[0], k*k)

    def test_positive_majorant_covariant_under_boost(self):
        boost = sp.eye(4)
        boost[0, 0] = boost[1, 1] = sp.Rational(5, 4)
        boost[0, 1] = boost[1, 0] = sp.Rational(3, 4)
        n = sp.Matrix([1, 0, 0, 0])
        normal = boost*n
        r0 = 2*(self.eta*n)*(self.eta*n).T-self.eta
        rn = 2*(self.eta*normal)*(self.eta*normal).T-self.eta
        self.assertEqual(boost.T*rn*boost, r0)
        self.assertEqual((normal.T*self.eta*normal)[0], 1)

    def test_even_full_dual_pair_does_not_select_hamiltonian(self):
        u, v = sp.Matrix(sp.symbols("u0:4")), sp.Matrix(sp.symbols("v0:4"))
        z = u.col_join(v)
        q = (u.T*self.eta*u)[0]
        r = (v.T*self.eta*v)[0]
        s = (u.T*self.eta*v)[0]
        delta = sp.expand(q*r - s**2)
        flow = (s*u-q*v).col_join(r*u-s*v)
        grad = sp.Matrix([sp.diff(delta, zi) for zi in z])
        self.assertEqual(
            sp.Matrix([sp.expand(x) for x in self.omega.T*flow-grad]),
            sp.zeros(8, 1),
        )
        for inv in (q, r, s):
            derivative = sp.Matrix([sp.diff(inv, zi) for zi in z])
            self.assertEqual(sp.expand((derivative.T*flow)[0]), 0)
        # H1=Delta and H2=Delta+Delta^2/2 both preserve the full dual pair.
        # Their Hamilton flows differ by the constant-on-orbits factor 1+Delta.
        sample = {**{u[i]: int(i == 0) for i in range(4)},
                  **{v[i]: int(i == 1) for i in range(4)}}
        self.assertEqual(delta.subs(sample), -1)
        self.assertNotEqual(flow.subs(sample), sp.zeros(8, 1))
        self.assertEqual(((1+delta)*flow).subs(sample), sp.zeros(8, 1))


if __name__ == "__main__":
    unittest.main()
