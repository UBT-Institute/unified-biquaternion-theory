"""Exact local split-jet variation rank certificate; not dynamics verification."""
import sympy as s
import unittest
r,q=s.symbols("r q",nonzero=True,real=True)
J=(r/q)*s.eye(4)
class RankTests(unittest.TestCase):
    def test_rank(self):
        self.assertEqual(J.rank(),4)
    def test_determinant(self):
        self.assertEqual(s.factor(J.det()),r**4/q**4)
    def test_pullback_injectivity(self):
        p=s.Matrix(s.symbols('p0:4'))
        self.assertEqual(s.solve(list(J.T*p),list(p)),{x:0 for x in p})
if __name__=="__main__":
    unittest.main()
