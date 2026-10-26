import unittest
import sympy as s
I=s.I
sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
gens=[x/2 for x in sig]+[I*x/2 for x in sig]
def flat(M):
 return s.Matrix([s.re(M[i,j]) for i in range(2) for j in range(2)]+[s.im(M[i,j]) for i in range(2) for j in range(2)])
def ranks(T):
 R=[a*T+T*a.conjugate().T for a in gens]
 full=s.Matrix.hstack(*map(flat,R))
 herm=s.Matrix.hstack(*[flat((x+x.conjugate().T)/2) for x in R])
 anti=s.Matrix.hstack(*[flat((x-x.conjugate().T)/2) for x in R])
 ns=herm.nullspace()
 restricted=anti*s.Matrix.hstack(*ns) if ns else s.zeros(8,0)
 return full.rank(),herm.rank(),len(ns),restricted.rank(),len(ns)-restricted.rank()
class TestRealityRanks(unittest.TestCase):
 def test_unit(self): self.assertEqual(ranks(s.eye(2)),(3,3,3,0,3))
 def test_imaginary_unit(self): self.assertEqual(ranks(I*s.eye(2)),(3,0,6,3,3))
 def test_mixed_phase(self): self.assertEqual(ranks(s.diag(1,I)),(5,3,3,2,1))
 def test_generic_witness(self): self.assertEqual(ranks(s.Matrix([[1,2+I],[3-I,2*I]])),(5,3,3,2,1))
if __name__=='__main__':unittest.main()
