# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""OI-6: exact sharp/adjugate central-metric covariance and a bimodule connection.

Conditional comparator: sharp is represented by quaternionic/Pauli adjugate;
the proposed two-sided connection is NOT established as canonical UBT dynamics.
Only the Python standard library is used.
"""
from itertools import product
from math import cos, exp, pi, sin
import unittest


I = ((1+0j, 0j), (0j, 1+0j))
X = ((0j, 1+0j), (1+0j, 0j))
Y = ((0j, -1j), (1j, 0j))
Z = ((1+0j, 0j), (0j, -1+0j))
A = ((0.2+0.1j, 0.3-0.2j), (0.1+0.4j, -0.2-0.1j))
SAMPLES = (I, X, Y, Z, ((1+1j, 2-1j), (3+0j, -1+2j)),
           ((0j, 1j), (2+0j, 1-1j)))


def mm(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def add(a, b):
    return tuple(tuple(a[i][j]+b[i][j] for j in range(len(a[0])))
                 for i in range(len(a)))


def sc(a, z):
    return tuple(tuple(z*v for v in row) for row in a)


def dagger(a):
    return tuple(tuple(complex(a[j][i]).conjugate()
                       for j in range(len(a))) for i in range(len(a[0])))


def trace(a):
    return a[0][0] + a[1][1]


def det(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]


def inverse(a):
    d = det(a)
    return ((a[1][1]/d, -a[0][1]/d), (-a[1][0]/d, a[0][0]/d))


def sharp(a):
    """Complex-linear quaternionic conjugation: adj(X) = Tr(X)I-X."""
    return add(sc(I, trace(a)), sc(a, -1))


def central(a, b):
    """The UBT-type polarized central metric as a matrix."""
    return sc(add(mm(sharp(a), b), mm(sharp(b), a)), 0.5)


def scalar_polar(a, b):
    return (det(add(a, b))-det(a)-det(b))/2


def congruence(g, a):
    return mm(mm(g, a), dagger(g))


def boost(eta):
    return ((exp(eta/2)+0j, 0j), (0j, exp(-eta/2)+0j))


def rotation(theta):
    return ((cos(theta/2)-1j*sin(theta/2), 0j),
            (0j, cos(theta/2)+1j*sin(theta/2)))


def shear():
    return ((1+0j, 0.3+0.2j), (0j, 1+0j))


def close(a, b, tol=1e-10):
    return all(abs(a[i][j]-b[i][j]) < tol
               for i in range(len(a)) for j in range(len(a[0])))


def bimodule_derivative(a, x, dx):
    """D X = partial X + A X + X A-dagger."""
    return add(add(dx, mm(a, x)), mm(x, dagger(a)))


def transformed_connection(g, dg, a):
    return add(mm(mm(g, a), inverse(g)), sc(mm(dg, inverse(g)), -1))


def transformed_derivative_inputs(g, dg, x, dx):
    return add(add(mm(mm(dg, x), dagger(g)),
                   mm(mm(g, dx), dagger(g))),
               mm(mm(g, x), dagger(dg)))


class SharpLorentzComparator(unittest.TestCase):
    def test_sharp_is_quaternion_conjugation_of_pauli_basis(self):
        self.assertTrue(close(sharp(I), I))
        for s in (X, Y, Z):
            self.assertTrue(close(sharp(s), sc(s, -1)))
            self.assertTrue(close(sharp(sc(s, -1j)), sc(s, 1j)))

    def test_sharp_is_an_involution_and_anti_automorphism(self):
        for a, b in product(SAMPLES, repeat=2):
            self.assertTrue(close(sharp(sharp(a)), a))
            self.assertTrue(close(sharp(mm(a, b)), mm(sharp(b), sharp(a))))

    def test_sharp_norm_is_determinant(self):
        for a in SAMPLES:
            self.assertTrue(close(mm(a, sharp(a)), sc(I, det(a))))
            self.assertTrue(close(mm(sharp(a), a), sc(I, det(a))))

    def test_central_polar_metric_is_scalar_for_full_complex_carrier(self):
        for a, b in product(SAMPLES, repeat=2):
            self.assertTrue(close(central(a, b), sc(I, scalar_polar(a, b))))

    def test_lorentz_congruence_preserves_central_polar_metric(self):
        for g in (boost(0.7), rotation(0.6), shear()):
            self.assertAlmostEqual(abs(det(g)-1), 0)
            for a, b in product(SAMPLES, repeat=2):
                self.assertTrue(close(central(congruence(g, a), congruence(g, b)),
                                      central(a, b)))

    def test_sharp_transforms_in_inverse_adjoint_contragredient(self):
        for g in (boost(0.7), rotation(0.6), shear()):
            for a in SAMPLES:
                lhs = sharp(congruence(g, a))
                rhs = mm(mm(inverse(dagger(g)), sharp(a)), inverse(g))
                self.assertTrue(close(lhs, rhs))

    def test_antihermitian_lorentz_paravector_slice_is_preserved(self):
        for g in (boost(0.7), rotation(0.6), shear()):
            a = sc(add(sc(I, 2), add(sc(X, -1), add(Y, Z))), 1j)
            b = sc(add(I, sc(Z, 2)), 1j)
            for e in (a, b):
                self.assertTrue(close(dagger(e), sc(e, -1)))
                transformed = congruence(g, e)
                self.assertTrue(close(dagger(transformed), sc(transformed, -1)))
            self.assertTrue(close(central(congruence(g, a), congruence(g, b)),
                                  central(a, b)))

    def test_local_bimodule_connection_covariant_for_constant_g(self):
        zero = sc(I, 0)
        for g in (boost(0.6), rotation(0.6), shear()):
            ap = transformed_connection(g, zero, A)
            for x, dx in product(SAMPLES[:4], repeat=2):
                lhs = bimodule_derivative(ap, congruence(g, x),
                                          congruence(g, dx))
                rhs = congruence(g, bimodule_derivative(A, x, dx))
                self.assertTrue(close(lhs, rhs))

    def test_nonconstant_gauge_transformation_cancels_derivative_terms(self):
        eta = 0.6
        g = boost(eta)
        dg = mm(sc(Z, 0.5), g)
        ap = transformed_connection(g, dg, A)
        for x, dx in product(SAMPLES[:4], repeat=2):
            xp = congruence(g, x)
            dxp = transformed_derivative_inputs(g, dg, x, dx)
            lhs = bimodule_derivative(ap, xp, dxp)
            rhs = congruence(g, bimodule_derivative(A, x, dx))
            self.assertTrue(close(lhs, rhs))

    def test_right_connection_is_adjoint_of_left_connection(self):
        g, dg = boost(0.6), mm(sc(Z, 0.5), boost(0.6))
        ap = transformed_connection(g, dg, A)
        bp = add(mm(mm(inverse(dagger(g)), dagger(A)), dagger(g)),
                 sc(mm(inverse(dagger(g)), dagger(dg)), -1))
        self.assertTrue(close(bp, dagger(ap)))

    def test_boost_generator_is_anticommutator_not_derivation(self):
        k = sc(Z, 0.5)
        delta_i = add(mm(k, I), mm(I, dagger(k)))
        self.assertTrue(close(delta_i, Z))
        # A derivation must annihilate identity, so boost action is not one.
        self.assertFalse(close(delta_i, sc(I, 0)))
        r = sc(Z, 0.5j)
        delta_rotation = add(mm(r, I), mm(I, dagger(r)))
        self.assertTrue(close(delta_rotation, sc(I, 0)))

    def test_det_one_is_necessary_for_exact_invariance_under_congruence(self):
        g = ((2+0j, 0j), (0j, 1+0j))
        for a, b in product(SAMPLES[:4], repeat=2):
            lhs = central(congruence(g, a), congruence(g, b))
            rhs = sc(central(a, b), abs(det(g))**2)
            self.assertTrue(close(lhs, rhs))

    def test_metric_signature_of_antihermitian_paravectors(self):
        basis = (sc(I, 1j), sc(X, -1j), sc(Y, -1j), sc(Z, -1j))
        signature = (-1, 1, 1, 1)
        for i, a in enumerate(basis):
            for j, b in enumerate(basis):
                expected = signature[i] if i == j else 0
                self.assertTrue(close(central(a, b), sc(I, expected)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
