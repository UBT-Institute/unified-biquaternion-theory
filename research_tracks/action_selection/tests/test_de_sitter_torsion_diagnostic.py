"""Exact symbolic closed de Sitter / torsion trace diagnostic."""
import unittest
import sympy as s
V,h=s.symbols('V h',positive=True)
a=s.cosh(h*V)/h
H=s.diff(a,V)/a
t0=3*(H-1/V)
R=6*(s.diff(a,V,2)/a+H**2+1/a**2)
def eq(x,y):
    return s.simplify(s.trigsimp(x-y)) == 0
class ExactDiagnostic(unittest.TestCase):
    def test_curvature(self):
        self.assertTrue(eq(R,12*h**2))
    def test_trace(self):
        self.assertTrue(eq(t0,3*(h*s.tanh(h*V)-1/V)))
    def test_norm(self):
        self.assertTrue(eq(-t0*t0,-9*(h*s.tanh(h*V)-1/V)**2))
    def test_at_one_h(self):
        self.assertTrue(eq(t0.subs(V,1/h),3*h*(s.tanh(1)-1)))
    def test_asymptotic(self):
        self.assertTrue(eq(s.limit(-t0*t0,V,s.oo),-9*h*h))
    def test_nonconstant(self):
        self.assertNotEqual(s.simplify(s.diff(-t0*t0,V)),0)
if __name__=='__main__':
    unittest.main()
