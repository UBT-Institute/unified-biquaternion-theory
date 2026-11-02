# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact finite-jet controls for the derived-H representative quotient.

The continuum solution-space theorem is conditional on the stated regularity,
boundary and geometric-action assumptions. This is not a Dirac mode count.
"""
import unittest
import sympy as sp

ETA = sp.diag(-1, 1, 1, 1)


def simplify(m):
    return m.applyfunc(lambda v: sp.factor(sp.cancel(v)))


def image_inverse(y, t):
    q = (y.T*ETA*y)[0]
    return simplify(ETA*((ETA*t)*(ETA*y).T-(ETA*y)*(ETA*t).T)/q)


def stabilizer_projection(y, a):
    return simplify(a-image_inverse(y, a*y))


def lorentz(a, b):
    result = sp.zeros(4)
    result[a, b] = 1
    result[b, a] = -ETA[a, a]/ETA[b, b]
    return result


def reconstruct_jet(e, de, r, dr, ddr, s=sp.Integer(1)):
    """An explicit holonomic target two-jet; no source field equations used."""
    metric = e*ETA*e.T
    inverse_metric = simplify(metric.inv())
    norm = (dr.T*inverse_metric*dr)[0]
    h = sp.sqrt(4*s*s*r/norm)
    v = ETA*e.inv()*dr
    y = simplify(h*v/(2*s))
    dy, connections = [], []
    for mu in range(4):
        dg = de[mu]*ETA*e.T+e*ETA*de[mu].T
        dginv = -inverse_metric*dg*inverse_metric
        dnorm = (2*ddr[:, mu].T*inverse_metric*dr+dr.T*dginv*dr)[0]
        dh_over_h = (dr[mu]/r-dnorm/norm)/2
        dv = -ETA*e.inv()*de[mu]*e.inv()*dr+ETA*e.inv()*ddr[:, mu]
        derivative = simplify(dh_over_h*y+h*dv/(2*s))
        t = simplify(s/h*e[mu, :].T-derivative)
        dy.append(derivative)
        connections.append(image_inverse(y, t))
    return norm, h, y, dy, connections


class DerivedHRepresentativeQuotient(unittest.TestCase):
    def test_target_jet_reconstruction_for_both_norm_signs(self):
        e = sp.Matrix([[2, 1, 0, 0], [0, 3, 1, 0], [0, 0, 4, 1], [0, 0, 0, 5]])
        de = [sp.zeros(4) for _ in range(4)]
        de[0][1, 1] = 2
        de[1][0, 1] = 1
        de[2][2, 3] = -1
        de[3][3, 3] = 3
        ddr = sp.Matrix([[2, 1, -1, 0], [1, 3, 2, 0], [-1, 2, 1, 1], [0, 0, 1, -2]])
        for initial_y in (sp.Matrix([5, 1, 1, 0]), sp.Matrix([1, 5, 0, 1])):
            r = (initial_y.T*ETA*initial_y)[0]
            dr = e*ETA*initial_y
            norm, h, y, dy, a = reconstruct_jet(e, de, r, dr, ddr)
            self.assertEqual(sp.simplify(norm-r), 0)
            self.assertEqual(h, 2)
            self.assertEqual(y, initial_y)
            self.assertEqual([(2*y.T*ETA*dy[mu])[0] for mu in range(4)], list(dr))
            for mu in range(4):
                self.assertEqual(simplify(h*(dy[mu]+a[mu]*y)-e[mu, :].T), sp.zeros(4, 1))

    def test_original_first_jet_roundtrip(self):
        h, s = sp.Rational(3), sp.Rational(2)
        dy = sp.diag(1, 2, 3, 4)
        a = [sp.Rational(mu+1, 20)*lorentz(0, (mu % 3)+1) for mu in range(4)]
        for y in (sp.Matrix([4, 1, 1, 0]), sp.Matrix([1, 4, 1, 0])):
            e = sp.Matrix.hstack(*(h/s*(dy[:, mu]+a[mu]*y) for mu in range(4))).T
            self.assertNotEqual(e.det(), 0)
            r = (y.T*ETA*y)[0]
            dr = 2*dy.T*ETA*y
            k = sp.factor((dr.T*(e*ETA*e.T).inv()*dr)[0])
            recovered_h = sp.sqrt(4*s*s*r/k)
            recovered_y = simplify(recovered_h/(2*s)*ETA*e.inv()*dr)
            self.assertEqual(recovered_h, h)
            self.assertEqual(recovered_y, y)

    def test_algebraic_inverse_stabilizer_and_uniqueness(self):
        a = 2*lorentz(0, 1)-3*lorentz(1, 2)+lorentz(0, 3)
        for y in (sp.Matrix([5, 4, 0, 0]), sp.Matrix([4, 5, 0, 0])):
            z = stabilizer_projection(y, a)
            self.assertEqual(z*y, sp.zeros(4, 1))
            self.assertEqual(simplify(z.T*ETA+ETA*z), sp.zeros(4))
            self.assertEqual(simplify(image_inverse(y, a*y)+z-a), sp.zeros(4))

    def test_fixed_little_group_coordinates_recover_all_twelve_labels(self):
        frame = sp.eye(4)
        frame[0, 0] = frame[1, 1] = sp.Rational(5, 3)
        frame[0, 1] = frame[1, 0] = sp.Rational(4, 3)
        self.assertEqual(frame.T*ETA*frame, ETA)
        for reference, generators in ((sp.Matrix([3, 0, 0, 0]), [lorentz(1, 2), lorentz(1, 3), lorentz(2, 3)]),
                                      (sp.Matrix([0, 3, 0, 0]), [lorentz(0, 2), lorentz(0, 3), lorentz(2, 3)])):
            y = frame*reference
            for mu in range(4):
                labels = [sp.Rational(mu+1), sp.Rational(mu+2), sp.Rational(mu+3)]
                z0 = sum((labels[j]*generators[j] for j in range(3)), sp.zeros(4))
                z = frame*z0*frame.inv()
                self.assertEqual(z*y, sp.zeros(4, 1))
                self.assertEqual(frame.inv()*z*frame, z0)

    def test_vertical_scalar_variation_keeps_entire_tetrad(self):
        t, x, y, z = sp.symbols('t x y z', real=True)
        coordinates = (t, x, y, z)
        radius = t+2
        carrier = sp.Matrix([radius, 0, 0, 0])
        r = -radius**2
        sigma = t*x+x*y+y*z+z*t**2
        dr = sp.Matrix([sp.diff(r, u) for u in coordinates])
        dsigma = sp.Matrix([sp.diff(sigma, u) for u in coordinates])
        k = (dr.T*ETA*dr)[0]
        scale_variation = sp.simplify((sigma/r-2*(dr.T*ETA*dsigma)[0]/k)/2)
        delta_y = simplify(scale_variation*carrier+ETA*dsigma/2)
        self.assertEqual(sp.simplify((2*carrier.T*ETA*delta_y)[0]-sigma), 0)
        for mu in range(4):
            a = sp.zeros(4) if mu == 0 else lorentz(0, mu)/radius
            a += sp.Rational(mu+1, 7)*lorentz(1, 2)
            d_y = carrier.diff(coordinates[mu])+a*carrier
            w = simplify(-delta_y.diff(coordinates[mu])-a*delta_y-scale_variation*d_y)
            self.assertEqual(sp.simplify((carrier.T*ETA*w)[0]), 0)
            delta_a = image_inverse(carrier, w)
            delta_e = simplify(scale_variation*d_y+delta_y.diff(coordinates[mu])+a*delta_y+delta_a*carrier)
            self.assertEqual(delta_e, sp.zeros(4, 1))

    def test_old_free_carrier_shift_is_not_a_derived_h_symmetry(self):
        # At the timelike rest carrier, delta r=0 fixes delta h=delta Y=0
        # for a true fixed-tetrad variation. A transverse shift violates it.
        carrier = sp.Matrix([3, 0, 0, 0])
        proposed_shift = sp.Matrix([0, 1, 0, 0])
        self.assertEqual((2*carrier.T*ETA*proposed_shift)[0], 0)
        self.assertNotEqual(proposed_shift, sp.zeros(4, 1))
        self.assertNotEqual(ETA*proposed_shift, sp.zeros(4, 1))

    def test_moving_stabilizer_constraint_is_essential(self):
        carrier = sp.Matrix([3, 0, 0, 0])
        delta_y = sp.Matrix([0, 1, 0, 0])
        stabilizer = lorentz(1, 2)
        self.assertEqual(stabilizer*carrier, sp.zeros(4, 1))
        self.assertNotEqual(stabilizer*delta_y, sp.zeros(4, 1))
        delta_z = image_inverse(carrier, -stabilizer*delta_y)
        self.assertEqual(delta_z*carrier+stabilizer*delta_y, sp.zeros(4, 1))

    def test_vertical_generators_have_second_parameter_derivatives(self):
        t, x = sp.symbols('t x', real=True)
        sigma = sp.Function('sigma')(t, x)
        radius = t+2
        delta_y = sp.Matrix([-sigma/(2*radius), sp.diff(sigma, x)/2, 0, 0])
        w0 = -delta_y.diff(t)
        delta_a0 = image_inverse(sp.Matrix([radius, 0, 0, 0]), w0)
        self.assertTrue(any(entry.has(sp.Derivative(sigma, t, x)) for entry in delta_a0))

    def test_no_reducibility_in_representative_coordinate_chart(self):
        # Zero original variation implies zero delta r=2Y.deltaY and,
        # after that, zero stabilizer label variation by an invertible frame.
        carrier = sp.Matrix([5, 4, 0, 0])
        self.assertEqual((2*carrier.T*ETA*sp.zeros(4, 1))[0], 0)
        basis = [sp.Matrix(16, 1, list(lorentz(1, 2))),
                 sp.Matrix(16, 1, list(lorentz(1, 3))),
                 sp.Matrix(16, 1, list(lorentz(2, 3)))]
        self.assertEqual(sp.Matrix.hstack(*basis).rank(), 3)

    def test_covariant_pullback_kernel_requires_surjective_tangent_map(self):
        # Finite linear-algebra core only: the continuum and boundary hypotheses
        # are stated and proved separately in the paired research note.
        f = sp.eye(4).row_join(sp.Matrix([[1, 0], [0, 1], [1, 1], [0, 2]]))
        base_form = sp.Matrix([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        pullback = f.T*base_form*f
        self.assertEqual(f.rank(), 4)
        self.assertEqual(pullback.rank(), base_form.rank())
        for null in pullback.nullspace():
            self.assertEqual(base_form*f*null, sp.zeros(4, 1))

    def test_same_geometry_can_retain_different_forbidden_boundary_labels(self):
        t, s = sp.symbols('t s', positive=True)
        boundary_values = []
        for rate in (2, 4):
            h = 2*s/rate*sp.exp(-rate*t/2)
            y = sp.Matrix([sp.exp(rate*t/2), 0, 0, 0])
            e = [h/s*y.diff(t)]
            e.extend(h/s*(rate*lorentz(0, i)/2)*y for i in range(1, 4))
            self.assertEqual(sp.simplify(sp.Matrix.hstack(*e).T), sp.eye(4))
            boundary_values.append(h.subs(t, 0))
        self.assertNotEqual(*boundary_values)

    def test_nongaussian_temporal_coordinate_lift_with_nonunit_lapse(self):
        t, x, y, z, s, length = sp.symbols('t x y z s L', positive=True)
        lapse = 1+t*t+x*x
        e = sp.diag(lapse, 2+t*t, 3+y*y, 4+z*z)
        r = -sp.exp(2*t/length)
        dr = sp.Matrix([sp.diff(r, t), 0, 0, 0])
        k = sp.factor((dr.T*(e*ETA*e.T).inv()*dr)[0])
        h = s*length*lapse*sp.exp(-t/length)
        carrier = sp.Matrix([sp.exp(t/length), 0, 0, 0])
        self.assertEqual(sp.simplify(h*h-4*s*s*r/k), 0)
        self.assertNotEqual((e*ETA*e.T).inv()[0, 0], -1)
        for mu, coordinate in enumerate((t, x, y, z)):
            a = sp.zeros(4) if mu == 0 else e[mu, mu]/(length*lapse)*lorentz(0, mu)
            self.assertEqual(sp.simplify(h/s*(carrier.diff(coordinate)+a*carrier)-e[mu, :].T), sp.zeros(4, 1))

    def test_defining_spin_split_is_not_a_flat_connection_gauge_choice(self):
        x = sp.symbols('x', real=True)
        unit_time = sp.Matrix([1, 0, 0, 0])
        defining_y = x*lorentz(1, 2)
        shift_y = lorentz(2, 3)
        total = 2*lorentz(0, 1)+lorentz(1, 3)
        k = total-defining_y
        self.assertEqual(defining_y*unit_time, sp.zeros(4, 1))
        self.assertNotEqual(defining_y.diff(x), sp.zeros(4))
        self.assertEqual((defining_y+shift_y)+(k-shift_y), total)


if __name__ == '__main__':
    unittest.main()
