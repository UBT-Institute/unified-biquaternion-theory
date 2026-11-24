"""Mathematical transport/lattice gates for a Lorentzian positive theta majorant.

Uses only real Lorentz carrier data. These tests do not derive a physical
connection, arithmetic theta lift, UBT action, or positive physical energy.
"""
import unittest
import sympy as sp

eta = sp.diag(1, -1, -1, -1)


def varying_normal():
    a = sp.symbols("a", real=True)
    n = sp.Matrix([sp.cosh(a), sp.sinh(a), 0, 0])
    dn = n.diff(a)
    majorant = 2 * (eta*n)*(eta*n).T - eta
    correction = dn*(n.T*eta) - n*(dn.T*eta)
    return a, n, dn, majorant, correction


class ThetaTransportLatticeGates(unittest.TestCase):
    def test_unit_normal_and_orthogonal_derivative(self):
        _, n, dn, _, _ = varying_normal()
        self.assertEqual(sp.simplify((n.T*eta*n)[0]), 1)
        self.assertEqual(sp.simplify((n.T*eta*dn)[0]), 0)

    def test_correction_is_a_lorentz_generator(self):
        _, n, dn, _, c = varying_normal()
        self.assertEqual(sp.simplify(c.T*eta+eta*c), sp.zeros(4))
        self.assertEqual(sp.simplify(c*n-dn), sp.zeros(4, 1))

    def test_adjusted_connection_parallelizes_normal(self):
        _, n, dn, _, c = varying_normal()
        self.assertEqual(sp.simplify(dn-c*n), sp.zeros(4, 1))

    def test_adjusted_connection_parallelizes_majorant(self):
        a, _, _, majorant, c = varying_normal()
        self.assertEqual(
            sp.simplify(majorant.diff(a)+c.T*majorant+majorant*c),
            sp.zeros(4)
        )
        self.assertNotEqual(sp.simplify(majorant.diff(a)).subs(a, 0), sp.zeros(4))

    def test_majorant_has_unit_determinant(self):
        a, _, _, majorant, _ = varying_normal()
        self.assertEqual(sp.simplify(majorant.det()), 1)
        self.assertEqual(sp.simplify(majorant.subs(a, 0)), sp.eye(4))

    def test_generic_boost_does_not_preserve_fixed_integer_lattice(self):
        boost = sp.eye(4)
        boost[0, 0] = boost[1, 1] = sp.Rational(5, 4)
        boost[0, 1] = boost[1, 0] = sp.Rational(3, 4)
        self.assertEqual(boost.T*eta*boost, eta)
        vector = boost*sp.Matrix([1, 0, 0, 0])
        self.assertNotEqual(vector[0].q, 1)  # not a member of Z^4

    def test_continuum_gaussian_forgets_normal(self):
        _, _, _, majorant, _ = varying_normal()
        y, s = sp.symbols("y s", real=True)
        kernel = y*majorant-sp.I*s*eta
        self.assertEqual(
            sp.simplify(sp.expand_trig(sp.expand(kernel.det()))),
            (y-sp.I*s)*(y+sp.I*s)**3
        )
        self.assertEqual(sp.simplify(kernel.det().subs(s, 0)), y**4)
        # For y>0, integral_R4 exp(-pi*y*k.T*R_n*k)dk = y**(-2).

    def test_torsion_is_changed_in_flat_tetrad(self):
        _, _, _, _, c = varying_normal()
        # Choose rapidity alpha=t and original Cartesian inertial tetrad e^a=dx^a.
        # New omega_hat= -c dt has T_hat^0 = -c^0_1 dt wedge dx.
        self.assertEqual(sp.simplify(c[0, 1]), 1)
        self.assertNotEqual(sp.simplify(-c[0, 1]), 0)

    def test_connection_correction_does_not_select_so3_part(self):
        _, n, _, _, c = varying_normal()
        rotation = sp.zeros(4)
        rotation[2, 3], rotation[3, 2] = 1, -1
        self.assertEqual(rotation*n, sp.zeros(4, 1))
        self.assertEqual(rotation.T*eta+eta*rotation, sp.zeros(4))
        self.assertNotEqual(c, c+rotation)

    def test_lorentz_connection_commutes_with_copy_space_sl2(self):
        _, _, _, _, c = varying_normal()
        lorentz = sp.diag(c, c)
        eye, zero = sp.eye(4), sp.zeros(4)
        t = sp.Matrix.vstack(
            sp.Matrix.hstack(2*eye, eye),
            sp.Matrix.hstack(eye, eye)
        )  # det [[2,1],[1,1]]=1
        self.assertEqual(t*lorentz-lorentz*t, sp.zeros(8))

    def test_complex_central_connection_obstructs_noncompact_sl2(self):
        eye, zero = sp.eye(4), sp.zeros(4)
        phase = sp.Matrix.vstack(
            sp.Matrix.hstack(zero, -eye),
            sp.Matrix.hstack(eye, zero)
        )
        squeeze = sp.Matrix.vstack(
            sp.Matrix.hstack(2*eye, zero),
            sp.Matrix.hstack(zero, sp.Rational(1, 2)*eye)
        )
        self.assertNotEqual(squeeze*phase-phase*squeeze, sp.zeros(8))


if __name__ == "__main__":
    unittest.main()
