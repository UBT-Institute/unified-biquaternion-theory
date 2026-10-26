"""Exact rank and determinant of torsion-vs-spin-connection linear map."""
import unittest
import sympy as s
N=4
eta=(-1,1,1,1)
pairs=[(a,b) for a in range(N) for b in range(a+1,N)]
cols=[(mu,a,b) for mu in range(N) for a,b in pairs]
rows=[(a,mu,nu) for a in range(N) for mu,nu in pairs]
def omega(mu,a,b,col):
 m,c,d=col
 return int(mu==m)*eta[a]*(int(a==c and b==d)-int(a==d and b==c))
M=s.Matrix([[omega(mu,a,nu,col)-omega(nu,a,mu,col) for col in cols] for a,mu,nu in rows])
class TestTorsionMap(unittest.TestCase):
 def test_size(self): self.assertEqual(M.shape,(24,24))
 def test_rank(self): self.assertEqual(M.rank(),24)
 def test_det(self): self.assertEqual(M.det(),16)
if __name__=="__main__":unittest.main()
