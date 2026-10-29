import unittest
import sympy as s
eta=s.diag(-1,1,1,1)
class Tests(unittest.TestCase):
 def test_massive_three_spatial_polarizations(self):
  m=s.symbols('m',positive=True)
  k=s.Matrix([m,0,0,0])
  C=k.T*eta
  self.assertEqual(C.rank(),1)
  B=s.Matrix.hstack(*C.nullspace())
  self.assertEqual(B.T*eta*B,s.eye(3))
 def test_massless_two_after_gauge_quotient(self):
  k=s.Matrix([1,0,0,1])
  C=k.T*eta
  self.assertEqual(C.rank(),1)
  self.assertEqual((C*k)[0],0)
  self.assertEqual(len(C.nullspace())-1,2)
 def test_positive_fisher_versus_indefinite_eta(self):
  p=s.symbols('p',real=True)
  fisher=s.simplify(p*(1/p)**2+(1-p)*(-1/(1-p))**2)
  self.assertEqual(s.simplify(fisher-1/(p*(1-p))),0)
  self.assertEqual([eta[i,i] for i in range(4)],[-1,1,1,1])
if __name__=='__main__':unittest.main()
