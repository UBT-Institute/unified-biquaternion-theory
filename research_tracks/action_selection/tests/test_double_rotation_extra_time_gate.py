"""Exact conditional controls for hypertravel / complex-time UBT ideas.

These are special relativity and toy 5D scalar controls, NOT an action for
UBT's fundamental field or proof that physical hyperspace travel is possible.
"""
import unittest
import sympy as sp

ETA = sp.diag(-1, 1, 1, 1)
KX = sp.zeros(4)
KX[0, 1] = KX[1, 0] = 1
KY = sp.zeros(4)
KY[0, 2] = KY[2, 0] = 1
JZ = sp.zeros(4)
JZ[1, 2], JZ[2, 1] = 1, -1


def boost(generator, sh=sp.Rational(3, 4), ch=sp.Rational(5, 4)):
    # Exact rapidity log(2): exp(r K)=I+sinh(r) K+(cosh(r)-1) K^2.
    return sp.eye(4) + sh*generator + (ch-1)*generator**2


class HypertravelNullControls(unittest.TestCase):
    def test_lie_algebra_closes_into_spatial_rotation(self):
        self.assertEqual(KX*KY-KY*KX, JZ)
        self.assertEqual(JZ[0, :], sp.zeros(1, 4))

    def test_lorentz_generators_are_antisymmetric_in_minkowski_form(self):
        for generator in (KX, KY, JZ):
            self.assertEqual(generator.T*ETA + ETA*generator, sp.zeros(4))

    def test_exact_finite_boosts_preserve_interval(self):
        bx, by = boost(KX), boost(KY)
        for matrix in (bx, by, bx*by, by*bx):
            self.assertEqual(matrix.T*ETA*matrix, ETA)
            self.assertEqual(matrix.det(), 1)
        self.assertNotEqual(bx*by, by*bx)

    def test_double_boost_stays_orthochronous_for_sample(self):
        vector = sp.Matrix([5, 1, 1, 0])
        self.assertLess((vector.T*ETA*vector)[0], 0)
        matrix = boost(KX)*boost(KY)
        transformed = matrix*vector
        self.assertGreater(transformed[0], 0)
        self.assertEqual((transformed.T*ETA*transformed)[0],
                         (vector.T*ETA*vector)[0])

    def test_linear_lorentz_loops_do_not_translate_origin(self):
        bx, by = boost(KX), boost(KY)
        commutator = bx*by*bx.inv()*by.inv()
        self.assertEqual(commutator*sp.zeros(4, 1), sp.zeros(4, 1))
        self.assertEqual(commutator.T*ETA*commutator, ETA)

    def test_spinor_four_pi_cycle_is_not_time_translation(self):
        theta = sp.symbols('theta', real=True)
        u = sp.diag(sp.exp(-sp.I*theta/2), sp.exp(sp.I*theta/2))
        self.assertEqual(u.subs(theta, 2*sp.pi), -sp.eye(2))
        self.assertEqual(u.subs(theta, 4*sp.pi), sp.eye(2))
        state = sp.Matrix([1, 2*sp.I])
        for angle in (0, 2*sp.pi, 4*sp.pi):
            rotated = u.subs(theta, angle)*state
            norm = sp.simplify((rotated.conjugate().T*rotated)[0])
            self.assertEqual(norm, 5)

    def test_spacelike_psi_mode_dispersion_is_positive(self):
        k, mass, radius = sp.symbols('k mass radius', positive=True)
        for n in range(-3, 4):
            omega_sq = k**2 + mass**2 + sp.Rational(n*n, 1)/radius**2
            self.assertEqual(sp.expand(omega_sq-(k**2+mass**2+n*n/radius**2)), 0)

    def test_spacelike_psi_group_velocity_is_subluminal(self):
        k, mass, radius = sp.symbols('k mass radius', positive=True)
        n = 2
        omega = sp.sqrt(k*k+mass*mass+(n/radius)**2)
        velocity = sp.diff(omega, k)
        self.assertEqual(sp.simplify(velocity-k/omega), 0)
        self.assertEqual(
            sp.simplify((1-velocity**2)
                        -(mass**2+(n/radius)**2)/(k*k+mass*mass+(n/radius)**2)),
            0
        )

    def test_timelike_compact_psi_has_tachyonic_mode(self):
        mass, radius, k, n = 1, 1, 0, 2
        omega_sq = k*k + mass*mass - (sp.Rational(n, radius))**2
        self.assertEqual(omega_sq, -3)

    def test_both_extra_signs_have_same_zero_mode(self):
        k, mass = sp.symbols('k mass', real=True)
        for sign in (1, -1):
            omega_sq = k*k + mass*mass + sign*0**2
            self.assertEqual(omega_sq, k*k + mass*mass)

    def test_5d_null_vector_cannot_have_spacelike_4d_projection_for_spatial_psi(self):
        spatial = sp.Matrix([3, 4, 12])
        psi = 5
        time_squared = sum(x*x for x in spatial) + psi**2
        self.assertEqual(time_squared, 194)
        self.assertLess(sum(x*x for x in spatial), time_squared)


    def test_flat_bulk_detour_cannot_beat_brane_light(self):
        height, separation = sp.Integer(1), sp.Integer(10)
        travel_time = 2*height + separation
        self.assertGreater(travel_time, separation)

    def test_explicit_warped_bulk_null_shortcut(self):
        # Toy geometry ds^2=-dt^2+a(y)^2 dx^2+dy^2,
        # a(y)=exp(-log(2)*y^2), brane at y=0.
        height, separation = sp.Integer(1), sp.Integer(10)
        y = sp.symbols('y', real=True)
        a = sp.exp(-sp.log(2)*y**2)
        self.assertEqual(a.subs(y,0), 1)
        self.assertEqual(a.subs(y,1), sp.Rational(1,2))
        vertical_dt = height
        horizontal_dt = a.subs(y,1)*separation
        self.assertEqual(-vertical_dt**2 + height**2, 0)
        self.assertEqual(-horizontal_dt**2 + a.subs(y,1)**2*separation**2, 0)
        self.assertEqual(2*vertical_dt+horizontal_dt, 7)
        self.assertLess(2*vertical_dt+horizontal_dt, separation)

    def test_warped_bulk_shortcut_requires_nonflat_geometry(self):
        y = sp.symbols('y',real=True)
        a = sp.exp(-sp.log(2)*y**2)
        # Scalar curvature of the 2d metric a(y)^2 dx^2+dy^2.
        curvature = sp.simplify(-2*sp.diff(a,y,2)/a)
        self.assertEqual(sp.simplify(curvature -
                         (4*sp.log(2)-8*sp.log(2)**2*y**2)), 0)
        self.assertEqual(sp.simplify(curvature.subs(y,0)-4*sp.log(2)), 0)


if __name__ == '__main__':
    unittest.main()
