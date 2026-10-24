"""Exact rotation/boost chirality representation tests."""
import unittest
import sympy as s
u,v=s.symbols('u v',real=True)
I=s.eye(2);PL=s.diag(1,0);PR=s.diag(0,1)
def S(a): return s.diag(s.exp(a/2),s.exp(-a/2))
def D(X,a): return S(a)*X*PL+S(a).inv()*X*PR
X=s.Matrix([[1,2],[3,4]])
class TestBoost(unittest.TestCase):
 def test_group_law(self): self.assertEqual(s.simplify(D(D(X,u),v)-D(X,u+v)),s.zeros(2))
 def test_left_not_dirac(self): self.assertNotEqual(s.simplify(S(u)*X-D(X,u)),s.zeros(2))
 def test_rotation_2pi(self):
  U=-I
  self.assertEqual(U*X*PL+U*X*PR,-X)
 def test_right_boost_not_same(self): self.assertNotEqual(s.simplify(S(u)-S(u).inv()),s.zeros(2))
 def test_intertwiner_rotational_blocks_fail_boost(self):
  a=s.symbols('a')
  z=s.simplify(a*(S(u)-S(u).inv()))
  self.assertNotEqual(z,s.zeros(2))
  self.assertEqual(s.solve([z[0,0]],[a]),{a:0})
if __name__=="__main__": unittest.main()
