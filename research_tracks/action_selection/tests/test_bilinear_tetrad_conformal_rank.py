import unittest
import sympy as s
I=s.I
pauli=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
Th=s.Matrix([[2+I,3],[1,1+2*I]])
E=[I*Th*P*Th.H for P in pauli]
def sharp(X):return X.adjugate()
def met(A,B):return s.simplify((sharp(A)*B+sharp(B)*A)/2)
eta=s.diag(-1,1,1,1)
f=s.simplify(Th.det()*s.conjugate(Th.det()))
class Checks(unittest.TestCase):
 def test_conformal_metric(self):
  for a in range(4):
   for b in range(4):
    self.assertEqual(s.simplify(met(E[a],E[b])-f*eta[a,b]*s.eye(2)),s.zeros(2))
 def test_real_lorentz_slice(self):
  for X in E:self.assertEqual(s.simplify(X+X.H),s.zeros(2))
 def test_nonzero_det(self):self.assertNotEqual(Th.det(),0)
if __name__=="__main__":unittest.main()
