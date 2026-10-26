import unittest
import sympy as s
I=s.I
sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
gens=[G/2 for G in sig]+[I*G/2 for G in sig]
def response(Theta):
 cols=[]
 for A in gens:
  M=A*Theta+Theta*A.conjugate().T
  cols.append(s.Matrix([s.re(M[i,j]) for i in range(2) for j in range(2)]+[s.im(M[i,j]) for i in range(2) for j in range(2)]))
 return s.Matrix.hstack(*cols)
class TestFullThetaRank(unittest.TestCase):
 def test_real_slice_rank_three(self):
  self.assertEqual(response(I*s.eye(2)).rank(),3)
  self.assertEqual(response(s.eye(2)).rank(),3)
 def test_complex_generic_witness_rank_five(self):
  self.assertEqual(response(s.diag(1,I)).rank(),5)
  self.assertEqual(response(s.Matrix([[1,2+I],[3-I,2*I]])).rank(),5)
 def test_det_invariance_in_direction(self):
  T=s.diag(1,I)
  for A in gens:
   X=A*T+T*A.conjugate().T
   self.assertEqual(s.simplify(s.trace(T.inv()*X)),0)
if __name__=='__main__':unittest.main()
