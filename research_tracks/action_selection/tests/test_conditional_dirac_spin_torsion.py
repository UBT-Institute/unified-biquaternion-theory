import unittest
import sympy as s
I=s.I; z=s.zeros(2)
sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
G=[s.diag(s.eye(2),-s.eye(2))]+[s.BlockMatrix([[z,x],[-x,z]]).as_explicit() for x in sig]
def comm(a,b):return a*b-b*a
def anti(a,b):return a*b+b*a
def three(a,b,c):return (G[a]*G[b]*G[c]+G[b]*G[c]*G[a]+G[c]*G[a]*G[b]-G[a]*G[c]*G[b]-G[c]*G[b]*G[a]-G[b]*G[a]*G[c])/6
class Checks(unittest.TestCase):
 def test_clifford_three_form(self):
  for c in range(4):
   for a in range(4):
    for b in range(4):
     self.assertEqual(s.simplify(anti(G[c],comm(G[a],G[b])/2)-2*three(c,a,b)),s.zeros(4))
 def test_totally_antisymmetric(self):
  for a in range(4):
   for b in range(4):
    self.assertEqual(three(a,a,b),s.zeros(4))
if __name__=='__main__':unittest.main()
