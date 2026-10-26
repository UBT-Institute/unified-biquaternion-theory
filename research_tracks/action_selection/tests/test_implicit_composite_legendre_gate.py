import unittest
import sympy as s
v,z,a,m,b,c=s.symbols('v z a m b c',real=True,nonzero=True)
class Check(unittest.TestCase):
 def test_composite_not_stationary(self):
  l=(v*v+z*z)/2
  L=s.expand(l.subs(z,a*v))
  self.assertEqual(s.diff(L,v,2),1+a*a)
  self.assertEqual(s.diff(l,v,2),1)
 def test_auxiliary_schur_complement(self):
  l=m*v*v/2+b*v*z+c*z*z/2
  L=s.expand(l.subs(z,-b*v/c))
  self.assertEqual(s.simplify(s.diff(L,v,2)-(m-b*b/c)),0)
 def test_implicit_derivative(self):
  F=z-a*v
  self.assertEqual(s.solve(F,z)[0].diff(v),-s.diff(F,v)/s.diff(F,z))
if __name__=='__main__':unittest.main()
