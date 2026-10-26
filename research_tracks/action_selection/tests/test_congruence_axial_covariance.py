import unittest
import sympy as s
eps=s.Matrix([[0,1],[-1,0]])
X=s.diag(1,0)
sigma3=s.diag(1,-1)
def j(X):return -s.trace(X.conjugate().T*X*sigma3)
class Check(unittest.TestCase):
 def test_rotation(self):
  self.assertEqual(eps.det(),1)
  self.assertEqual(eps.conjugate().T*eps,s.eye(2))
 def test_axial_time_flip_under_congruence(self):
  self.assertEqual(j(X),-1)
  self.assertEqual(j(eps*X*eps.H),1)
 def test_norm_preserved(self):
  self.assertEqual(s.trace(X.H*X),s.trace((eps*X*eps.H).H*(eps*X*eps.H)))
if __name__=="__main__":unittest.main()
