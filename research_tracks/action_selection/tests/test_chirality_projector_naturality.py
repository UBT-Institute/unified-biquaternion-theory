"""Conditional commutant obstruction for fixed right chirality projectors."""
import unittest
import sympy as s
a,b,c,d=s.symbols('a b c d')
G=s.Matrix([[a,b],[c,d]])
sx=s.Matrix([[0,1],[1,0]])
sz=s.diag(1,-1)
class Projector(unittest.TestCase):
 def test_commutant(self):
  equations=list(G*sx-sx*G)+list(G*sz-sz*G)
  self.assertEqual(s.solve(equations,[a,b,c,d]),{a:d,b:0,c:0})
 def test_fixed_projector_not_natural(self):
  P=s.diag(1,0)
  self.assertNotEqual(P*sx,sx*P)
 def test_only_scalar_involutions(self):
  z=s.symbols('z')
  self.assertEqual(s.solve(z*z-1,z),[-1,1])
if __name__=='__main__':unittest.main()
