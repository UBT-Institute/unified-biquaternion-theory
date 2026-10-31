# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact *restricted* full-Clifford torsion and squared-Dirac audit.

Constant orthonormal tetrad, metric-compatible arbitrary antisymmetric Lorentz
spin coefficients (24), not a selected single-Theta action. Distinguishes the
8 Dirac-visible vector/3-vector channels from 16 invisible tensor channels.
"""
import itertools
import unittest
import sympy as sp

I = sp.I
id2, zero2 = sp.eye(2), sp.zeros(2)
sigma = (sp.Matrix([[0, 1], [1, 0]]),
         sp.Matrix([[0, -I], [I, 0]]), sp.diag(1, -1))

def block(a, b, c, d):
    return sp.BlockMatrix([[a, b], [c, d]]).as_explicit()

GAMMA = (block(zero2, id2, -id2, zero2),) + tuple(
    block(zero2, x, x, zero2) for x in sigma)
ID4 = sp.eye(4)
ETA = sp.diag(-1, 1, 1, 1)
PAIRS = tuple(itertools.combinations(range(4), 2))
TRIPLES = tuple(itertools.combinations(range(4), 3))
GRADE13 = GAMMA + tuple(GAMMA[a] * GAMMA[b] * GAMMA[c]
                        for a, b, c in TRIPLES)

def omega_matrix(omega, mu):
    return sum((omega.get((mu, a, b), 0) * GAMMA[a] * GAMMA[b] / 2
                for a, b in PAIRS), sp.zeros(4))

def dirac_zero_order(omega):
    return sum((GAMMA[mu] * omega_matrix(omega, mu)
                for mu in range(4)), sp.zeros(4))

def pack(m):
    return sp.Matrix(m).reshape(16, 1)

def affine_gamma(omega, mu, nu, rho):
    # Gamma^rho_{mu,nu}=eta^{rho,a} omega_{mu,a,nu}.
    return sum((ETA[rho, a] * (omega.get((mu, a, nu), 0)
                                   if a < nu else
                                   -omega.get((mu, nu, a), 0))
                for a in range(4) if a != nu), sp.Integer(0))

def verify_square(omega):
    Om = [omega_matrix(omega, mu) for mu in range(4)]
    V = dirac_zero_order(omega)
    Gamma = [[[affine_gamma(omega, mu, nu, rho)
               for rho in range(4)] for nu in range(4)] for mu in range(4)]
    T = [[[Gamma[mu][nu][rho] - Gamma[nu][mu][rho]
           for rho in range(4)] for nu in range(4)] for mu in range(4)]
    biv = [[(GAMMA[mu]*GAMMA[nu]-GAMMA[nu]*GAMMA[mu])/2
            for nu in range(4)] for mu in range(4)]
    F = [[Om[mu]*Om[nu]-Om[nu]*Om[mu]
          for nu in range(4)] for mu in range(4)]
    for mu in range(4):
        for nu in range(4):
            bracket = Om[mu]*GAMMA[nu]-GAMMA[nu]*Om[mu]
            bracket += sum((Gamma[mu][rho][nu]*GAMMA[rho]
                            for rho in range(4)),sp.zeros(4))
            assert sp.simplify(bracket) == sp.zeros(4), (mu,nu,'compat')
    for rho in range(4):
        derivative = GAMMA[rho]*V+V*GAMMA[rho]
        laplace = 2*ETA[rho,rho]*Om[rho] - sum(
            (ETA[mu,mu]*Gamma[mu][mu][rho]*ID4 for mu in range(4)),sp.zeros(4))
        torsion_term = -sum((biv[mu][nu]*T[mu][nu][rho]/2
                             for mu in range(4) for nu in range(4)),sp.zeros(4))
        assert sp.simplify(derivative-laplace-torsion_term)==sp.zeros(4), (rho,'derivative')
    zeroth = V*V
    laplace_zero = sum((ETA[mu,mu]*Om[mu]*Om[mu]
                       for mu in range(4)),sp.zeros(4))
    laplace_zero -= sum((ETA[mu,mu]*Gamma[mu][mu][rho]*Om[rho]
                         for mu in range(4) for rho in range(4)),sp.zeros(4))
    F_T = sum((biv[mu][nu]*(F[mu][nu]-sum((
        T[mu][nu][rho]*Om[rho] for rho in range(4)),sp.zeros(4)))/2
               for mu in range(4) for nu in range(4)),sp.zeros(4))
    assert sp.simplify(zeroth-laplace_zero-F_T)==sp.zeros(4), 'zeroth'

class CliffordTorsionOperatorGate(unittest.TestCase):
    def test_full_clifford_vector_generators(self):
        for mu in range(4):
            for nu in range(4):
                self.assertEqual(GAMMA[mu]*GAMMA[nu]+GAMMA[nu]*GAMMA[mu],
                                 2*ETA[mu,nu]*ID4)

    def test_full_24_to_8_rank_and_tensor_kernel(self):
        cols=[pack(GAMMA[mu]*GAMMA[a]*GAMMA[b]/2)
              for mu in range(4) for a,b in PAIRS]
        M=sp.Matrix.hstack(*cols)
        self.assertEqual(M.rank(),8)
        self.assertEqual(len(M.nullspace()),16)
        grades=sp.Matrix.hstack(*[pack(m) for m in GRADE13])
        self.assertEqual(grades.rank(),8)
        self.assertEqual(M.row_join(grades).rank(),8)

    def test_all_eight_vector_and_trivector_channels(self):
        grades=sp.Matrix.hstack(*[pack(m) for m in GRADE13])
        self.assertEqual(grades.rank(),8)
        self.assertEqual(sp.Matrix.hstack(grades,*[pack(
            GAMMA[mu]*GAMMA[a]*GAMMA[b]/2)
            for mu in range(4) for a,b in PAIRS]).rank(),8)

    def test_tensor_kernel_connection_nonzero(self):
        w={(0,1,2):sp.Integer(1),(1,0,2):sp.Integer(1)}
        self.assertEqual(dirac_zero_order(w),sp.zeros(4))
        om0,om1=omega_matrix(w,0),omega_matrix(w,1)
        self.assertNotEqual(om0,sp.zeros(4))
        self.assertNotEqual(om0*om1-om1*om0,sp.zeros(4))
        verify_square(w)

    def test_trace_only_connection_yields_vector_grade(self):
        w={(0,0,1):sp.Integer(2)}
        self.assertEqual(dirac_zero_order(w),-GAMMA[1])
        verify_square(w)

    def test_axial_only_connection_yields_trivector_grade(self):
        w={(0,1,2):1,(1,0,2):-1,(2,0,1):1}
        self.assertEqual(dirac_zero_order(w),sp.Rational(3,2)*GAMMA[0]*GAMMA[1]*GAMMA[2])
        verify_square(w)

    def test_random_rational_connection_exact_dirac_square(self):
        w={(mu,a,b):sp.Rational((2*mu+3*a+5*b)%7-3,5)
           for mu in range(4) for a,b in PAIRS}
        verify_square(w)
        self.assertNotEqual(dirac_zero_order(w),sp.zeros(4))

    def test_principal_symbol_preserves_metric_cone(self):
        k=sp.symbols('k0:4')
        P=sum((k[i]*GAMMA[i] for i in range(4)),sp.zeros(4))
        q=sum((ETA[i,i]*k[i]**2 for i in range(4)),sp.Integer(0))
        self.assertEqual(sp.simplify(P*P),q*ID4)
        self.assertEqual(sp.factor(P.det()-q**2),0)

if __name__=='__main__':
    unittest.main()
