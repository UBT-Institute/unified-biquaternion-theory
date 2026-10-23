import unittest
import sympy as s
I=s.eye(2);Z=s.zeros(2)
X=s.Matrix([[1+2*s.I,3],[4*s.I,5]])
U=-I
class Spin(unittest.TestCase):
 def test_left_spin_2pi(self): self.assertEqual(U*X,-X)
 def test_congruence_2pi(self): self.assertEqual(U*X*U.H,X)
 def test_carrier_central_characters(self):
  self.assertEqual(s.diag(U,U),-s.eye(4))
  self.assertEqual(s.kronecker_product(U,U.conjugate()),s.eye(4))
 def test_distinct_actions(self): self.assertNotEqual(U*X,U*X*U.H)
if __name__=="__main__":unittest.main()
