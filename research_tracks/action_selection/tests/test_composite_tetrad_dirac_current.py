"""Necessary flat-spinor checks; not a proof of composite UBT dynamics."""
import unittest
import sympy as s
I=s.I
z=s.zeros(2); e=s.eye(2)
sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
g0=s.diag(e,-e)
gs=[s.BlockMatrix([[z,x],[-x,z]]).as_explicit() for x in sig]
class Checks(unittest.TestCase):
 def test_clifford(self):
  G=[g0]+gs
  eta=[1,-1,-1,-1]
  for a in range(4):
   for b in range(4):
    self.assertEqual(s.simplify(G[a]*G[b]+G[b]*G[a]),2*(eta[a] if a==b else 0)*s.eye(4))
 def test_current_density_positive(self):
  u=s.Matrix(s.symbols('u0:4',complex=True))
  self.assertEqual((u.conjugate().T*g0*g0*u)[0],(u.conjugate().T*u)[0])
 def test_pseudohermiticity(self):
  for G in [g0]+gs: self.assertEqual(s.simplify(G.conjugate().T*g0-g0*G),s.zeros(4))
if __name__=='__main__':unittest.main()
