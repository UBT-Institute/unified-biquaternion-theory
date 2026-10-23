"""Exact matching of the existing independent-Cartan trace comparator to closed de Sitter."""
import unittest
import sympy as s
V,h,K,q=s.symbols('V h K q', positive=True)
a=s.cosh(h*V)/h
H=s.diff(a,V)/a
F=s.simplify(K*V**2/a**2)
class Checks(unittest.TestCase):
    def test_matching(self):
        self.assertEqual(s.simplify(s.diff(s.log(F),V)+2*(H-1/V)),0)
    def test_explicit_form(self):
        self.assertEqual(s.simplify(F-K*h**2*V**2/s.cosh(h*V)**2),0)
    def test_early_limit(self):
        self.assertEqual(s.limit(F,V,0,dir='+'),0)
    def test_late_limit(self):
        self.assertEqual(s.limit(F,V,s.oo),0)
    def test_strict_positivity_sample(self):
        self.assertTrue(s.N(F.subs({V:1,h:2,K:3}))>0)
    def test_rho_mapping(self):
        rho=s.symbols('rho',positive=True)
        target=K*h**2*rho**2/q**2/s.cosh(h*rho/q)**2
        self.assertEqual(s.simplify(F.subs(V,rho/q)-target),0)
if __name__=='__main__':
    unittest.main()
