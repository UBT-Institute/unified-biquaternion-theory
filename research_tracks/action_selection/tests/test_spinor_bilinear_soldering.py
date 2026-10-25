import unittest
import sympy as s
r=s.symbols('r',real=True)
S=s.diag(s.exp(r),s.exp(-r))
Th=s.Matrix([[1+s.I,2],[3,s.I]])
X=Th*Th.H
class Check(unittest.TestCase):
 def test_hermitian(self):self.assertEqual(s.simplify(X-X.H),s.zeros(2))
 def test_covariance(self):self.assertEqual(s.simplify((S*Th)*(S*Th).H-S*X*S.H),s.zeros(2))
 def test_positive_det(self):self.assertEqual(s.simplify(X.det()-Th.det()*s.conjugate(Th.det())),0)
 def test_right_frame_invariance(self):
  U=s.Matrix([[0,1],[-1,0]])
  self.assertEqual(s.simplify((Th*U)*(Th*U).H-X),s.zeros(2))
if __name__=='__main__':unittest.main()
