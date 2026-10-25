import unittest
import sympy as s
eps=s.Matrix([[0,1],[-1,0]])
sig3=s.diag(1,-1)
theta=s.Matrix([[1,0],[0,0]])
def axial(M):return s.simplify(-s.trace(M.conjugate().T*M*sig3))
def norm(M):return s.simplify(s.trace(M.conjugate().T*M))
class Test(unittest.TestCase):
 def test_axial_flip(self):
  self.assertEqual(axial(theta),-1)
  self.assertEqual(axial(theta*eps),1)
 def test_norm_invariance(self):
  self.assertEqual(norm(theta),norm(theta*eps))
 def test_right_su2(self):
  self.assertEqual(eps.conjugate().T*eps,s.eye(2))
  self.assertEqual(eps.det(),1)
if __name__=="__main__":unittest.main()
