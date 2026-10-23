"""Exact symbolic regular inverse Legendre theorem and inertia checks."""
import unittest
import sympy as s
class InverseLegendre(unittest.TestCase):
    def test_generic_quadratic(self):
        C=s.symbols('C',positive=True)
        k1,k2=s.symbols('k1 k2',nonzero=True,real=True)
        p=s.Matrix(s.symbols('p0:2',real=True))
        v=s.Matrix(s.symbols('v0:2',real=True))
        K=s.diag(k1,k2)
        H=(p.T*K.inv()*p)[0]/(2*C)
        vel=s.Matrix([s.diff(H,x) for x in p])
        self.assertEqual(s.simplify(vel-K.inv()*p/C),s.zeros(2,1))
        L=s.expand((p.T*v)[0]-H).subs({p[i]:(C*K*v)[i] for i in range(2)})
        self.assertEqual(s.simplify(L-C*(v.T*K*v)[0]/2),0)
    def test_ubt_inertia(self):
        K=2*s.diag(1,-1,-1,-1,1,-1,-1,-1)
        self.assertEqual(K.eigenvals(),{s.Integer(2):2,s.Integer(-2):6})
        self.assertEqual((K.inv()*K),s.eye(8))
    def test_linear_congruence_determinant(self):
        K=s.diag(2,-2)
        M=s.Matrix([[1,1],[0,2]])
        transformed=M.T*K*M
        self.assertEqual(s.simplify(transformed.det()-M.det()**2*K.det()),0)
if __name__=='__main__':
    unittest.main()
