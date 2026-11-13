# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""OI-6: No universal Theta-only SL(2,C) gauge connection on a nonfree orbit.

Standard finite-dimensional gauge geometry. These tests are illustrative,
not a proof of UBT dynamics or a uniqueness theorem for physical physics.
Run: python3 verify_theta_stabilizer_obstruction.py
"""
import cmath
from fractions import Fraction
from itertools import product
from math import cos, sin
import unittest

I = ((1+0j, 0j), (0j, 1+0j))
X = ((0j, 1+0j), (1+0j, 0j))
Y = ((0j, -1j), (1j, 0j))
Z = ((1+0j, 0j), (0j, -1+0j))
P = ((0j, 1+0j), (0j, 0j))
Q = ((0j, 0j), (1+0j, 0j))


def add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))


def sc(a, z):
    return tuple(tuple(a[i][j] * z for j in range(2)) for i in range(2))


def mm(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def dagger(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(2)) for i in range(2))


def det(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]


def inv(a):
    d = det(a)
    return ((a[1][1]/d, -a[0][1]/d), (-a[1][0]/d, a[0][0]/d))


def tr(a):
    return a[0][0] + a[1][1]


def commute(a, b):
    return add(mm(a,b), sc(mm(b,a), -1))


def close(a, b, tol=1e-10):
    return all(abs(a[i][j]-b[i][j])<tol for i,j in product(range(2),repeat=2))


def stabilizer_variation(k, theta):
    return add(mm(k, theta), mm(theta, dagger(k)))


def rank_real(rows, tol=1e-9):
    a = [list(float(x) for x in r) for r in rows]
    row = 0
    for j in range(len(a[0])):
        pivot = max(range(row, len(a)),key=lambda i:abs(a[i][j]),default=None)
        if pivot is None or abs(a[pivot][j]) < tol:
            continue
        a[row],a[pivot] = a[pivot],a[row]
        fac = a[row][j]
        a[row] = [x/fac for x in a[row]]
        for i in range(len(a)):
            if i != row:
                fac = a[i][j]
                if fac:
                    a[i]=[v-fac*w for v,w in zip(a[i],a[row])]
        row+=1
        if row==len(a):
            break
    return row


def stabilizer_rank(theta):
    generators = (X,Y,Z,sc(X,1j),sc(Y,1j),sc(Z,1j))
    rows = []
    for g in generators:
        d = stabilizer_variation(g,theta)
        rows.append([d[i][j].real for i,j in product(range(2),repeat=2)] +
                    [d[i][j].imag for i,j in product(range(2),repeat=2)])
    return rank_real(rows)


def positive_hermitian_part(theta):
    return sc(add(theta, dagger(theta)),0.5)


def antihermitian_imag_part(theta):
    return sc(add(theta,sc(dagger(theta),-1)),1/(2j))


def generic_isotropy_generator(theta):
    """i(K H^-1 - (trace(K H^-1)/2) I) for Theta=H+iK."""
    h=positive_hermitian_part(theta)
    k=antihermitian_imag_part(theta)
    kh=mm(k,inv(h))
    return sc(add(kh,sc(I,-tr(kh)/2)),1j)


def exp_diagonal_stabilizer(x,alpha=1):
    z=cmath.exp(1j*alpha*x)
    return ((z,0j),(0j,1/z))


def connection_transformed_at_origin(a, tangent_g):
    """At h(0)=I, local gauge law A'=h A h^-1 - (dh)h^-1."""
    return add(a,sc(tangent_g,-1))


def raw_abelian_q(x,y):
    """Theta=diag(exp(x*y+x), exp(x*x+y)); q=1/2 d log det Theta."""
    return ((y+1+2*x)/2,(x+1)/2)


def pure_gauge(x):
    """S=(I+xP)(I+yQ), A=-(dS) S^-1; A is flat."""
    ep=add(I,sc(P,x))
    ep_inv=add(I,sc(P,-x))
    ay=sc(mm(mm(ep,Q),ep_inv),-1)
    ax=sc(P,-1)
    return ax,ay


class ThetaStabilizerObstruction(unittest.TestCase):
    def test_identity_has_three_dimensional_stabilizer(self):
        self.assertEqual(stabilizer_rank(I),3)
        for k in (sc(X,1j),sc(Y,1j),sc(Z,1j)):
            self.assertTrue(close(stabilizer_variation(k,I),sc(I,0)))

    def test_generic_complex_theta_has_one_stabilizer_direction(self):
        h = ((2+0j,0.2+0j),(0.2+0j,1.5+0j))
        k = ((0.3+0j,0.1+0.2j),(0.1-0.2j,-0.1+0j))
        theta=add(h,sc(k,1j))
        generator=generic_isotropy_generator(theta)
        self.assertAlmostEqual(abs(tr(generator)),0)
        self.assertTrue(close(stabilizer_variation(generator,theta),sc(I,0)))
        self.assertGreater(max(abs(v) for row in generator for v in row),0.05)
        self.assertEqual(stabilizer_rank(theta),5)

    def test_generic_diagonal_complex_field_fixed_by_local_u1(self):
        theta=((2+1j,0j),(0j,1-2j))
        for x in (0,0.3,1):
            g=exp_diagonal_stabilizer(x)
            self.assertTrue(close(mm(mm(g,theta),dagger(g)),theta))
            self.assertAlmostEqual(abs(det(g)-1),0)
        self.assertEqual(stabilizer_rank(theta),5)

    def test_local_isotropy_contradicts_theta_only_connection_covariance(self):
        theta=((2+1j,0j),(0j,1-2j))
        # h(x) leaves theta, including ALL of its spacetime jets, invariant.
        alpha=1.7
        tangent_g=sc(Z,1j*alpha)
        a=add(sc(X,0.3),sc(Y,-0.7)) # arbitrary Theta-only value
        predicted=connection_transformed_at_origin(a,tangent_g)
        self.assertTrue(close(stabilizer_variation(tangent_g,theta),sc(I,0)))
        self.assertFalse(close(a,predicted))
        self.assertTrue(close(add(predicted,sc(a,-1)),sc(tangent_g,-1)))

    def test_variable_scalar_theta_still_has_local_su2_isotropy(self):
        for x in (-0.6,0,0.7):
            theta=sc(I,2+x*x)
            g=exp_diagonal_stabilizer(x,2)
            self.assertTrue(close(mm(mm(g,theta),dagger(g)),theta))
        self.assertFalse(close(connection_transformed_at_origin(I,sc(Z,2j)),I))

    def test_determinant_is_invariant_but_dlog_connection_is_flat(self):
        theta=((2+1j,0j),(0j,3-1j))
        for x in (0,0.4):
            g=exp_diagonal_stabilizer(x)
            self.assertAlmostEqual(abs(det(mm(mm(g,theta),dagger(g)))-det(theta)),0)
        x,y=0.4,0.7
        dy_qx = (raw_abelian_q(x,y+0.1)[0]-raw_abelian_q(x,y-0.1)[0])/0.2
        dx_qy = (raw_abelian_q(x+0.1,y)[1]-raw_abelian_q(x-0.1,y)[1])/0.2
        self.assertAlmostEqual(dy_qx,dx_qy)
        self.assertAlmostEqual(dy_qx,0.5)

    def test_pure_gauge_maurer_cartan_curvature_zero(self):
        for x in (0,0.2,1.0):
            ax,ay=pure_gauge(x)
            dp=add(commute(P,Q),sc(mm(mm(P,Q),P),-2*x))
            dx_ay=sc(dp,-1)
            f=add(dx_ay,commute(ax,ay))
            self.assertTrue(close(f,sc(I,0)))

    def test_pure_gauge_kills_group_valued_field_derivative(self):
        for x,y in product((0,0.25,1),repeat=2):
            s=mm(add(I,sc(P,x)),add(I,sc(Q,y)))
            dsx=mm(P,add(I,sc(Q,y)))
            dsy=mm(add(I,sc(P,x)),Q)
            ax,ay=pure_gauge(x)
            self.assertTrue(close(add(dsx,mm(ax,s)),sc(I,0)))
            self.assertTrue(close(add(dsy,mm(ay,s)),sc(I,0)))

    def test_no_go_does_not_imply_every_composite_connection_flat(self):
        # Non-pure-gauge counterexample: explicit chosen A_x=P, A_y=Q.
        # This is NOT a function selected solely by Theta.
        self.assertFalse(close(commute(P,Q),sc(I,0)))

    def test_stabilizer_generator_is_tracefree_for_generic_field(self):
        for r in (0.1,0.4,1):
            theta=((2+0.3j,r+0.1j),(r+0.2j,1-0.3j))
            # Hermitian part is positive definite in all three cases.
            h=positive_hermitian_part(theta)
            self.assertGreater(h[0][0].real,0)
            self.assertGreater(det(h).real,0)
            q=generic_isotropy_generator(theta)
            self.assertAlmostEqual(abs(tr(q)),0)
            self.assertTrue(close(stabilizer_variation(q,theta),sc(I,0)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
