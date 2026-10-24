"""Exact antilinear SL2 Weyl-dual identity in a determinant-one test family."""
import unittest
import sympy as s
e=s.Matrix([[0,1],[-1,0]])
a,b,z=s.symbols('a b z',real=True,nonzero=True)
# Nonunitary boost and a non-real determinant-one SL2 example.
S=s.Matrix([[a,s.I*b],[0,1/a]])
chi=s.Matrix([z,1+s.I])
class Tests(unittest.TestCase):
 def test_det(self): self.assertEqual(s.simplify(S.det()),1)
 def test_dual_identity(self):
  self.assertEqual(s.simplify(e*S.conjugate()*e.inv()-(S.conjugate().T).inv()),s.zeros(2))
 def test_intertwiner(self):
  self.assertEqual(s.simplify(e*(S*chi).conjugate()-(S.conjugate().T).inv()*e*chi.conjugate()),s.zeros(2,1))
 def test_phase_conjugation(self):
  t=s.symbols('t',real=True)
  self.assertEqual(s.simplify(e*(s.exp(s.I*t)*chi).conjugate()-s.exp(-s.I*t)*e*chi.conjugate()),s.zeros(2,1))
if __name__=='__main__':unittest.main()
