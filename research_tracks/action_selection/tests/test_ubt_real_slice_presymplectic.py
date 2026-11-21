"""Exact UBT carrier/flat-jet presymplectic diagnostic (not UBT dynamics).

The locked Lorentz reality requirement applies to D_mu Theta, not necessarily
to Theta's values. The value-space real-slice restriction is an additional
mathematical test, not a new canonical axiom.
"""
import unittest
import sympy as sp


ETA = sp.diag(1, -1, -1, -1)
I4 = sp.eye(4)
Z4 = sp.zeros(4)
J = sp.BlockMatrix([[Z4, -I4], [I4, Z4]]).as_explicit()
K = sp.diag(2, -2, -2, -2, 2, -2, -2, -2)
OMEGA = K * J
P = sp.BlockMatrix([[Z4], [I4]]).as_explicit()
C = sp.BlockMatrix([[I4, Z4]]).as_explicit()


class RealSlicePresymplecticGateTests(unittest.TestCase):
    def test_nondegenerate_full_eight_real_carrier(self):
        self.assertEqual(OMEGA.rank(), 8)
        self.assertEqual(OMEGA.T, -OMEGA)
        self.assertEqual(J*J, -sp.eye(8))

    def test_real_slice_is_maximal_isotropic(self):
        self.assertEqual(P.T*OMEGA*P, sp.zeros(4))
        self.assertEqual(P.rank(), 4)

    def test_slice_symplectic_complement_is_itself(self):
        h = P.T*OMEGA
        self.assertEqual(h.rank(), 4)
        self.assertEqual(h*P, sp.zeros(4))

    def test_u_constraints_poisson_commute_in_toy_system(self):
        self.assertEqual(C*OMEGA.inv()*C.T, sp.zeros(4))
        fields = -OMEGA.inv()*C.T
        self.assertEqual(fields[:4, :], sp.zeros(4))
        self.assertEqual(fields[4:, :].rank(), 4)

    def test_phase_rotation_exits_restricted_value_slice(self):
        v = sp.Matrix([1, 2, 3, 4])
        self.assertEqual(C*J*(P*v), -v)

    def test_gram_casimir_has_zero_flow_on_real_value_slice(self):
        u = sp.Matrix(sp.symbols("u0:4"))
        v = sp.Matrix(sp.symbols("v0:4"))
        q = (u.T*ETA*u)[0]
        r = (v.T*ETA*v)[0]
        s = (u.T*ETA*v)[0]
        delta = q*r - s**2
        gradient = sp.Matrix([sp.diff(delta, x) for x in list(u)+list(v)])
        flow = -OMEGA.inv()*gradient
        self.assertEqual(flow.subs({x: 0 for x in u}), sp.zeros(8, 1))

    def test_flat_derivative_reality_kills_nonzero_hermitian_fourier_mode(self):
        # D_mu=partial_mu, E_mu in W_L -> partial_mu U=0.
        # The linear map U_k -> (k_mu U_k)_mu is injective when k != 0.
        k = sp.Matrix([0, 1, 2, 0])
        matrix = sp.Matrix.vstack(*[k[i]*I4 for i in range(4)])
        self.assertEqual(matrix.rank(), 4)

    def test_compact_support_variations_pair_to_zero(self):
        # In a connected flat patch, d_mu(delta U)=0. Compact spatial
        # support implies delta U=0. Delta Theta then lies in P(R4).
        a = sp.Matrix(sp.symbols("a0:4"))
        b = sp.Matrix(sp.symbols("b0:4"))
        self.assertEqual(((P*a).T*OMEGA*(P*b))[0], 0)

    def test_assumed_jet_kinetic_action_has_nonzero_distinct_current(self):
        # For a *toy* L=1/2 dot(v).T eta dot(v), not a selected UBT action.
        e0 = sp.Matrix([1, 0, 0, 0])
        d1v, d2v = sp.zeros(4, 1), e0
        d1dv, d2dv = e0, sp.zeros(4, 1)
        current = (d1dv.T*ETA*d2v - d2dv.T*ETA*d1v)[0]
        self.assertEqual(current, 1)
        self.assertEqual(((P*e0).T*OMEGA*(P*e0))[0], 0)

    def test_lorentz_symmetry_preserves_real_lagrangian_slice(self):
        boost = sp.eye(4)
        boost[0, 0] = boost[1, 1] = sp.Rational(5, 4)
        boost[0, 1] = boost[1, 0] = sp.Rational(3, 4)
        lift = sp.diag(boost, boost)
        self.assertEqual(boost.T*ETA*boost, ETA)
        self.assertEqual(lift.T*OMEGA*lift, OMEGA)
        self.assertEqual(C*lift*P, sp.zeros(4))


if __name__ == "__main__":
    unittest.main()
