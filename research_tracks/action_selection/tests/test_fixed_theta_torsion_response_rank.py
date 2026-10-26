import unittest
import sympy as s
eta=s.diag(-1,1,1,1)
pairs=[(a,b) for a in range(4) for b in range(a+1,4)]
v=s.Matrix([1,0,0,0])
M=s.zeros(16,24)
for mu in range(4):
 for j,(a,b) in enumerate(pairs):
  generator=s.zeros(4)
  generator[a,b]=eta[a,a]
  generator[b,a]=-eta[b,b]
  col=generator*v
  for row in range(4): M[4*mu+row,6*mu+j]=col[row]
class Checks(unittest.TestCase):
 def test_lorentz_generators(self):
  for a,b in pairs:
   W=s.zeros(4);W[a,b]=eta[a,a];W[b,a]=-eta[b,b]
   self.assertEqual(W.T*eta+eta*W,s.zeros(4))
 def test_rank_and_kernel(self):
  self.assertEqual(M.rank(),12)
  self.assertEqual(len(M.nullspace()),12)
 def test_orthogonal_output(self):
  self.assertEqual((v.T*eta*M[:4,:6]),s.zeros(1,6))
if __name__=='__main__':unittest.main()
