import unittest
import sympy as s
theta=s.pi/4
S=s.Matrix([[s.cos(theta),s.sin(theta)],[-s.sin(theta),s.cos(theta)]])
E=s.I*s.eye(2)
def sharp(X):return X.adjugate()
def metric(X,Y):return s.simplify((sharp(X)*Y+sharp(Y)*X)/2)
class Test(unittest.TestCase):
 def test_sl2(self):self.assertEqual(S.det(),1)
 def test_left_preserves_metric(self):self.assertEqual(metric(S*E,S*E),metric(E,E))
 def test_left_breaks_fixed_slice(self):self.assertNotEqual(s.simplify(S*E+(S*E).H),s.zeros(2))
 def test_congruence_preserves_slice(self):
  X=S*E*S.H
  self.assertEqual(s.simplify(X+X.H),s.zeros(2))
if __name__=="__main__":unittest.main()
