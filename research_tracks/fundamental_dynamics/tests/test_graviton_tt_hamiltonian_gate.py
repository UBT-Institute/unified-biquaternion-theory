import unittest
import sympy as s
k=s.Matrix([0,0,1]);P=s.eye(3)-k*k.T
basis=[]
for i in range(3):
 for j in range(i,3):
  B=s.zeros(3);B[i,j]=1;B[j,i]=1
  basis.append(B)
def tt(H):return s.simplify(P*H*P-s.trace(P*H)*P/2)
def pack(H):return s.Matrix([H[i,j] for i in range(3) for j in range(i,3)])
M=s.Matrix.hstack(*[pack(tt(b)) for b in basis])
hp,hx,pp,px,kk=s.symbols('hp hx pp px kk',real=True)
Ham=(pp**2+px**2+kk**2*(hp**2+hx**2))/2
class GravitonBenchmark(unittest.TestCase):
 def test_tt_projector_rank(self):self.assertEqual(M.rank(),2)
 def test_tt_projector_idempotent(self):self.assertEqual(M*M,M)
 def test_tt_traceless_transverse(self):
  for B in basis:
   H=tt(B)
   self.assertEqual(s.trace(H),0)
   self.assertEqual(H*k,s.zeros(3,1))
 def test_canonical_hamilton_equations(self):
  self.assertEqual(s.diff(Ham,pp),pp)
  self.assertEqual(s.diff(Ham,px),px)
  self.assertEqual(-s.diff(Ham,hp),-kk**2*hp)
  self.assertEqual(-s.diff(Ham,hx),-kk**2*hx)
if __name__=='__main__':unittest.main()
