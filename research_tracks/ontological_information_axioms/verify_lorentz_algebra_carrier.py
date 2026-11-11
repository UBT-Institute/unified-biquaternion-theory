# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""OI-6: Lorentz congruence vs biquaternion automorphism vs SU(4).

Standard finite-dimensional matrix identities and counterexamples.
The complex 2x2 matrix carrier is assumed; no UBT dynamics are derived.
Run: python3 research_tracks/ontological_information_axioms/
verify_lorentz_algebra_carrier.py
"""
from itertools import product
from math import cos, cosh, exp, pi, sin
import unittest


I = ((1+0j, 0j), (0j, 1+0j))
X = ((0j, 1+0j), (1+0j, 0j))
Y = ((0j, -1j), (1j, 0j))
Z = ((1+0j, 0j), (0j, -1+0j))
E00 = ((1+0j, 0j), (0j, 0j))
E11 = ((0j, 0j), (0j, 1+0j))
SAMPLES = (I, X, Y, Z, E00, E11, ((1+1j, 2-1j), (3+0j, -1+2j)))


def mm(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def add(a, b):
    return tuple(tuple(a[i][j]+b[i][j] for j in range(len(a[0])))
                 for i in range(len(a)))


def mul(a, c):
    return tuple(tuple(c*a[i][j] for j in range(len(a[0])))
                 for i in range(len(a)))


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0])))


def conj(a):
    return tuple(tuple(complex(x).conjugate() for x in row) for row in a)


def dagger(a):
    return transpose(conj(a))


def det(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def inv(a):
    d=det(a)
    return ((a[1][1]/d,-a[0][1]/d),(-a[1][0]/d,a[0][0]/d))


def close(a, b, tol=1e-11):
    return all(abs(a[i][j]-b[i][j]) < tol
               for i in range(len(a)) for j in range(len(a[0])))


def vec(a):
    """Column-major vectorization (row factor, column factor)."""
    return tuple(a[i][j] for j in range(len(a[0])) for i in range(len(a)))


def unvec(v):
    return ((v[0],v[2]),(v[1],v[3]))


def kron(a, b):
    return tuple(tuple(a[i//len(b)][j//len(b[0])]*
                       b[i%len(b)][j%len(b[0])]
                       for j in range(len(a[0])*len(b[0])))
                 for i in range(len(a)*len(b)))


def matvec(a, v):
    return tuple(sum(a[i][j]*v[j] for j in range(len(v))) for i in range(len(a)))


def boost(eta):
    return ((exp(eta/2)+0j,0j),(0j,exp(-eta/2)+0j))


def rotation(theta):
    # SU(2) rotation around Z
    return ((cos(theta/2)-1j*sin(theta/2),0j),
            (0j,cos(theta/2)+1j*sin(theta/2)))


def lorentz(g, a):
    return mm(mm(g,a),dagger(g))


def inner(g, a):
    return mm(mm(g,a),inv(g))


def frob2(a):
    return sum(abs(z)**2 for row in a for z in row)


def concurrence_of_vec(a):
    """Normalized pure two-qubit concurrence under the chosen vec split."""
    return 2*abs(det(a))/frob2(a)


class ThreeActionComparator(unittest.TestCase):
    def test_hermitian_paravector_determinant_is_minkowski(self):
        for t,x,y,z in ((2,1,1,0),(1,0,0,1),(3,-2,1,0),(0,1,0,0)):
            a=add(add(mul(I,t),mul(X,x)),add(mul(Y,y),mul(Z,z)))
            self.assertTrue(close(a,dagger(a)))
            self.assertAlmostEqual(det(a).real,t*t-x*x-y*y-z*z)
            self.assertAlmostEqual(det(a).imag,0)

    def test_sl2_boost_congruence_preserves_hermitian_and_determinant(self):
        for eta in (0.0,0.4,1.0):
            g=boost(eta)
            self.assertAlmostEqual(det(g).real,1)
            for a in (I,X,Y,Z,add(mul(I,2),add(X,Y))):
                out=lorentz(g,a)
                self.assertTrue(close(out,dagger(out)))
                self.assertAlmostEqual(abs(det(out)-det(a)),0)

    def test_nonunitary_lorentz_boost_is_not_unital_or_multiplicative(self):
        g=boost(0.8)
        gi=lorentz(g,I)
        self.assertFalse(close(gi,I))
        self.assertFalse(close(lorentz(g,mm(I,I)),mm(gi,gi)))
        self.assertTrue(close(gi,((exp(0.8)+0j,0j),(0j,exp(-0.8)+0j))))

    def test_similarity_is_algebra_automorphism(self):
        g=boost(0.8)
        self.assertTrue(close(inner(g,I),I))
        for a,b in product(SAMPLES,repeat=2):
            self.assertTrue(close(inner(g,mm(a,b)),mm(inner(g,a),inner(g,b))))
            self.assertAlmostEqual(abs(det(inner(g,a))-det(a)),0)

    def test_nonunitary_similarity_does_not_preserve_hermitian_subspace(self):
        out=inner(boost(0.8),X)
        self.assertFalse(close(out,dagger(out)))
        self.assertAlmostEqual(out[0][1].real,exp(0.8))
        self.assertAlmostEqual(out[1][0].real,exp(-0.8))

    def test_unitary_rotation_is_overlap_of_two_actions(self):
        for theta in (0.0,pi/7,pi/3):
            g=rotation(theta)
            self.assertTrue(close(inv(g),dagger(g)))
            for a in SAMPLES:
                self.assertTrue(close(lorentz(g,a),inner(g,a)))

    def test_column_major_vectorization_of_two_actions(self):
        for g in (boost(0.8),rotation(0.4)):
            for a in SAMPLES:
                expected_lorentz=matvec(kron(conj(g),g),vec(a))
                expected_inner=matvec(kron(transpose(inv(g)),g),vec(a))
                self.assertTrue(close(unvec(expected_lorentz),lorentz(g,a)))
                self.assertTrue(close(unvec(expected_inner),inner(g,a)))

    def test_rank_one_null_matrix_remains_rank_one(self):
        g=boost(0.8)
        for out in (lorentz(g,E00),inner(g,E00)):
            self.assertAlmostEqual(abs(det(out)),0)
            self.assertAlmostEqual(concurrence_of_vec(out),0)

    def test_boost_preserves_det_but_changes_normalized_vec_concurrence(self):
        eta=0.8
        out=lorentz(boost(eta),I)
        self.assertAlmostEqual(det(out).real,1)
        self.assertAlmostEqual(concurrence_of_vec(I),1)
        self.assertAlmostEqual(concurrence_of_vec(out),1/cosh(2*eta))
        self.assertLess(concurrence_of_vec(out),1)

    def test_unitary_inner_action_preserves_normalized_vec_concurrence(self):
        g=rotation(0.8)
        for a in SAMPLES:
            self.assertAlmostEqual(concurrence_of_vec(inner(g,a)),
                                   concurrence_of_vec(a))

    def test_su4_entangler_breaks_lorentz_null_and_hermitian_structure(self):
        # Vectorization of E00 is |00>; U=exp(-it X tensor X).
        t=pi/4
        xx=kron(X,X)
        u=add(mul(kron(I,I),cos(t)),mul(xx,-1j*sin(t)))
        out=unvec(matvec(u,vec(E00)))
        self.assertAlmostEqual(abs(det(E00)),0)
        self.assertGreater(abs(det(out)),0.49)
        self.assertFalse(close(out,dagger(out)))
        self.assertAlmostEqual(concurrence_of_vec(out),1)

    def test_boost_infinitesimal_commutator_vs_anticommutator(self):
        # d/deta at eta=0: Lorentz -> {Z,a}/2; inner -> [Z,a]/2.
        epsilon=1e-6
        g=boost(epsilon)
        ag=lorentz(g,I)
        ai=inner(g,I)
        derivative_g=mul(add(ag,mul(I,-1)),1/epsilon)
        derivative_i=mul(add(ai,mul(I,-1)),1/epsilon)
        self.assertTrue(close(derivative_g,Z,1e-5))
        self.assertTrue(close(derivative_i,mul(I,0),1e-5))


if __name__ == "__main__":
    unittest.main(verbosity=2)
