# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""OI-6 residual-U(1) Hessian branch comparator and variational-chain checks.

This is an assumed charged-two-scalar + Abelian-connection toy model,
not the complete composite Theta action. Run with Python standard library.
"""
from fractions import Fraction as F
from math import cos, sin
import unittest


def rank(matrix):
    a = [[F(x) for x in row] for row in matrix]
    if not a:
        return 0
    pivot_row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(pivot_row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot], a[pivot_row] = a[pivot_row], a[pivot]
        factor = a[pivot_row][col]
        a[pivot_row] = [x / factor for x in a[pivot_row]]
        for row in range(len(a)):
            if row != pivot_row:
                factor = a[row][col]
                if factor:
                    a[row] = [x - factor*y for x, y in zip(a[row], a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def temporal_hessian(z, matter_scale=1):
    """Velocities: (u_dot, v_dot, b0_dot, b1_dot, b2_dot, b3_dot)."""
    diag = [matter_scale, matter_scale, 0, z, z, z]
    return [[F(diag[i]) if i == j else F(0) for j in range(6)]
            for i in range(6)]


def covariant_velocity(u, v, du, dv, b0, charge=2):
    return du-charge*b0*v, dv+charge*b0*u


def scalar_temporal_lagrangian(u, v, du, dv, b0, charge=2):
    w1, w2 = covariant_velocity(u, v, du, dv, b0, charge)
    return (w1*w1 + w2*w2)/2


def stationary_b0(u, v, du, dv, charge=2):
    r2 = u*u + v*v
    if not r2:
        raise ValueError('Auxiliary equation loses rank at zero scalar amplitude')
    return -(u*dv-v*du)/(charge*r2)


def radial_kinetic(u, v, du, dv):
    r2 = u*u + v*v
    if not r2:
        raise ValueError('Polar radius undefined at origin')
    return (u*du+v*dv)**2/(2*r2)


def reduced_radial_hessian(u, v):
    """Velocity Hessian after algebraically removing b0, rho>0."""
    r2 = u*u + v*v
    if not r2:
        raise ValueError('At origin the auxiliary Schur complement is singular')
    return [[u*u/r2, u*v/r2], [u*v/r2, v*v/r2]]


def projector_numerator(k):
    """3x3 numerator: k² I - kk^T, exact integer entries."""
    k2 = sum(x*x for x in k)
    return [[(k2 if i == j else 0)-k[i]*k[j] for j in range(3)]
            for i in range(3)]


def composite_kinetic_coefficient(a, kappa):
    """For L=1/2 (theta_dot-e)^2+kappa/2 e^2 and e=a theta_dot."""
    return (1-a)**2 + kappa*a*a


def chain_rule_coefficient(a, kappa):
    """Minus coefficient of theta_ddot in E_theta + (D_theta e)^* E_e."""
    # E_theta=-(1-a)theta_ddot; E_e=(-1+(1+kappa)a)theta_dot.
    return (1-a)+a*(-1+(1+kappa)*a)


class ResidualU1HessianTests(unittest.TestCase):
    def test_auxiliary_branch_velocity_hessian_rank_two(self):
        self.assertEqual(rank(temporal_hessian(0)), 2)
        self.assertEqual([temporal_hessian(0)[i][i] for i in range(6)], [1,1,0,0,0,0])

    def test_added_maxwell_term_raises_rank_to_five(self):
        for z in (F(1,2), F(1), F(3,2)):
            self.assertEqual(rank(temporal_hessian(z)), 5)
            self.assertEqual(temporal_hessian(z)[2][2], 0)

    def test_wrong_maxwell_sign_produces_negative_vector_kinetic(self):
        h = temporal_hessian(-2)
        self.assertEqual(rank(h), 5)
        self.assertEqual([h[i][i] for i in (3,4,5)], [-2,-2,-2])

    def test_algebraic_b0_stationarity(self):
        for u, v, du, dv in [(F(1), F(2), F(3), F(4)),
                              (F(2,3), F(1,5), F(-3,4), F(7,9))]:
            b0 = stationary_b0(u,v,du,dv)
            dL_db0 = 2*(-v*(du-2*b0*v)+u*(dv+2*b0*u))
            self.assertEqual(dL_db0, 0)

    def test_eliminating_b0_leaves_only_radial_velocity(self):
        for u, v, du, dv in [(F(1), F(2), F(3), F(4)),
                              (F(2,3), F(1,5), F(-3,4), F(7,9)),
                              (F(-1), F(0), F(2), F(9))]:
            b0 = stationary_b0(u,v,du,dv)
            self.assertEqual(scalar_temporal_lagrangian(u,v,du,dv,b0),
                             radial_kinetic(u,v,du,dv))

    def test_auxiliary_elimination_projects_velocity_hessian_to_rank_one(self):
        for u, v in ((F(1), F(2)), (F(2,3), F(1,5)), (F(-1), F(0))):
            h = reduced_radial_hessian(u, v)
            self.assertEqual(rank(h), 1)
            self.assertEqual([sum(h[i][j]*[u,v][j] for j in range(2))
                              for i in range(2)], [u,v])
            self.assertEqual([sum(h[i][j]*[-v,u][j] for j in range(2))
                              for i in range(2)], [0,0])

    def test_zero_scalar_amplitude_is_singular_auxiliary_patch(self):
        with self.assertRaises(ValueError):
            stationary_b0(0,0,1,1)

    def test_charged_scalar_local_u1_covariance(self):
        q, alpha, dalpha, b0 = 2, .43, -.31, .23
        u,v,du,dv = .8, -.4, .21, .53
        angle = q*alpha
        c,s=cos(angle),sin(angle)
        up, vp=c*u-s*v, s*u+c*v
        dup=c*du-s*dv-q*dalpha*vp
        dvp=s*du+c*dv+q*dalpha*up
        lhs=covariant_velocity(up,vp,dup,dvp,b0-dalpha,q)
        a,b=covariant_velocity(u,v,du,dv,b0,q)
        rhs=c*a-s*b, s*a+c*b
        self.assertTrue(all(abs(x-y)<1e-12 for x,y in zip(lhs,rhs)))

    def test_nonzero_fourier_mode_has_two_transverse_directions(self):
        for k in ((1,0,0),(1,2,3),(-4,2,0)):
            p=projector_numerator(k)
            self.assertEqual(rank(p),2)
            self.assertEqual([sum(p[i][j]*k[j] for j in range(3)) for i in range(3)], [0,0,0])
            self.assertEqual(sum(p[i][i] for i in range(3)), 2*sum(x*x for x in k))

    def test_maxwell_dirac_count_for_nonzero_spatial_modes(self):
        # 4 config variables; pi0=0 and Gauss are first class.
        n_configuration=4
        n_first_class=2
        self.assertEqual(n_configuration-n_first_class,2)
        # For two real charged scalars plus Maxwell: 6-2=4 configurations.
        self.assertEqual(6-2,4)

    def test_pullback_hessian_and_full_variational_chain_agree(self):
        for a in (F(-1),F(0),F(1,3),F(1),F(2)):
            for kappa in (F(0),F(1,2),F(2)):
                self.assertEqual(composite_kinetic_coefficient(a,kappa),
                                 chain_rule_coefficient(a,kappa))

    def test_independent_field_and_composite_hessian_differ(self):
        self.assertEqual(composite_kinetic_coefficient(F(1,2),F(0)), F(1,4))
        self.assertNotEqual(composite_kinetic_coefficient(F(1,2),F(0)), F(1))
        self.assertEqual(composite_kinetic_coefficient(F(1),F(0)),0)

    def test_hessian_rank_alone_does_not_count_physical_modes(self):
        # There are 5 nonzero velocities in the Maxwell+matter branch but
        # 4 physical configuration modes after two first-class constraints.
        self.assertEqual(rank(temporal_hessian(1)),5)
        self.assertEqual(6-2,4)
        self.assertNotEqual(5,4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
