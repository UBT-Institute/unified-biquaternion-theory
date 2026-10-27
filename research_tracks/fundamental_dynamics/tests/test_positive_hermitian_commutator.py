import unittest
import sympy as s
I=s.I
sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
gens=[x/2 for x in sig]+[I*x/2 for x in sig]
def flat(M):
 return s.Matrix([s.re(M[i,j]) for i in range(2) for j in range(2)]+[s.im(M[i,j]) for i in range(2) for j in range(2)])
def ranks(T):
 R=[a*T+T*a.conjugate().T for a in gens]
 herm=s.Matrix.hstack(*[flat((x+x.conjugate().T)/2) for x in R])
 anti=s.Matrix.hstack(*[flat((x-x.conjugate().T)/2) for x in R])
 N=s.Matrix.hstack(*herm.nullspace())
 return herm.rank(),N.cols,(anti*N).rank()
class TestPositiveHermitianCommutator(unittest.TestCase):
 def test_nonscalar_diagonal(self):
  self.assertEqual(ranks(s.eye(2)+I*s.diag(1,2)),(3,3,2))
 def test_nonscalar_offdiagonal_positive_H(self):
  H=s.Matrix([[2,1],[1,2]])
  self.assertEqual(ranks(H+I*s.diag(1,3)),(3,3,2))
 def test_central_exception(self):
  self.assertEqual(ranks((1+2*I)*s.eye(2)),(3,3,0))
 def test_su2_commutator_rank(self):
  Q=I*s.diag(1,2)
  response=s.Matrix.hstack(*[flat(b*Q-Q*b) for b in gens[3:]])
  self.assertEqual(response.rank(),2)
 def test_general_real_cross_product_identity(self):
  beta=s.Matrix(s.symbols('b1:4',real=True))
  q=s.Matrix(s.symbols('q1:4',real=True))
  q0=s.symbols('q0',real=True)
  b=I*sum((beta[j]*sig[j] for j in range(3)),s.zeros(2))
  Q=I*(q0*s.eye(2)+sum((q[j]*sig[j] for j in range(3)),s.zeros(2)))
  cross=beta.cross(q)
  expected=-2*I*sum((cross[j]*sig[j] for j in range(3)),s.zeros(2))
  self.assertEqual((b*Q-Q*b-expected).applyfunc(s.expand),s.zeros(2))
if __name__=='__main__':unittest.main()
