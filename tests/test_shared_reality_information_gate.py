# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact shared-reality/information control tests (not UBT action derivations)."""
import unittest
from fractions import Fraction
import sympy as sp

ETA=sp.diag(1,-1,-1,-1)


class TestSharedRealityInformationG1(unittest.TestCase):
    def test_massive_transverse_three_dim_positive_after_sign(self):
        k=sp.Matrix([2,0,0,0])
        E=sp.Matrix.hstack(*[sp.eye(4)[:,i] for i in (1,2,3)])
        self.assertEqual(k.T*ETA*E,sp.zeros(1,3))
        self.assertEqual(-E.T*ETA*E,sp.eye(3))

    def test_lorentz_boost_preserves_physical_norm(self):
        boost=sp.eye(4)
        boost[0,0]=boost[3,3]=sp.Rational(5,4)
        boost[0,3]=boost[3,0]=sp.Rational(3,4)
        self.assertEqual(boost.T*ETA*boost,ETA)
        k=sp.Matrix([2,0,0,0])
        E=sp.Matrix.hstack(*[sp.eye(4)[:,i] for i in (1,2,3)])
        self.assertEqual((boost*k).T*ETA*(boost*E),sp.zeros(1,3))
        self.assertEqual(-(boost*E).T*ETA*(boost*E),sp.eye(3))

    def test_massless_transverse_quotient_two_dim(self):
        k=sp.Matrix([1,0,0,1])
        E=sp.Matrix.hstack(sp.eye(4)[:,1],sp.eye(4)[:,2],k)
        self.assertEqual((k.T*ETA*k)[0],0)
        self.assertEqual(k.T*ETA*E,sp.zeros(1,3))
        self.assertEqual(-E.T*ETA*E,sp.diag(1,1,0))
        self.assertEqual((-E.T*ETA*E).rank(),2)

    def test_same_equations_opposite_energy_sign(self):
        tm,omega=sp.symbols("tm omega",real=True)
        q=sp.Function("q")(tm)
        v=sp.diff(q,tm)
        L=(v**2-omega**2*q**2)/2
        EL=lambda lag: sp.simplify(sp.diff(sp.diff(lag,v),tm)-sp.diff(lag,q))
        self.assertEqual(EL(L),sp.diff(q,tm,2)+omega**2*q)
        self.assertEqual(EL(-L),-EL(L))
        H=lambda lag: sp.simplify(v*sp.diff(lag,v)-lag)
        self.assertEqual(H(L),(v**2+omega**2*q**2)/2)
        self.assertEqual(H(-L),-H(L))

    def test_local_marginals_do_not_fix_joint_state(self):
        same={(0,0):Fraction(1,2),(1,1):Fraction(1,2)}
        independent={(i,j):Fraction(1,4) for i in (0,1) for j in (0,1)}
        marginal=lambda state,axis,val:sum(prob for bits,prob in state.items() if bits[axis]==val)
        for axis in (0,1):
            for val in (0,1):
                self.assertEqual(marginal(same,axis,val),marginal(independent,axis,val))
        self.assertNotEqual(same,independent)
        self.assertEqual(sum(p for ij,p in same.items() if ij[0]==ij[1]),1)
        self.assertEqual(sum(p for ij,p in independent.items() if ij[0]==ij[1]),Fraction(1,2))

    def test_relative_entropy_local_information_hessian(self):
        epsilon=sp.symbols("epsilon",real=True)
        D=(sp.Rational(1,2)+epsilon)*sp.log(1+2*epsilon)+(sp.Rational(1,2)-epsilon)*sp.log(1-2*epsilon)
        self.assertEqual(sp.limit(D,epsilon,0),0)
        self.assertEqual(sp.diff(D,epsilon).subs(epsilon,0),0)
        self.assertEqual(sp.diff(D,epsilon,2).subs(epsilon,0),4)
        self.assertEqual(sp.series(D,epsilon,0,5).removeO().expand(),
                         2*epsilon**2+sp.Rational(4,3)*epsilon**4)

    def test_causal_principal_symbol_does_not_fix_mass(self):
        cov=sp.symbols("w kx ky kz",real=True)
        principal=cov[0]**2-sum(c*c for c in cov[1:])
        for mass in (sp.Integer(0),sp.Integer(1),sp.Integer(3)):
            poly=sp.Poly(principal-mass**2,*cov)
            leading=sum(coeff*sp.prod(v**power for v,power in zip(cov,powers))
                        for powers,coeff in poly.terms() if sum(powers)==2)
            self.assertEqual(sp.expand(leading),principal)
        self.assertNotEqual(principal-1,principal-9)


if __name__=="__main__":
    unittest.main()
