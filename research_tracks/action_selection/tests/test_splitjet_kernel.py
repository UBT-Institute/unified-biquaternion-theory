"""Pointwise split-jet auxiliary Jacobian and stabilizer kernel."""
import unittest
import sympy as s
r,q=s.symbols('r q',nonzero=True,real=True)
J=s.Matrix.hstack((r/q)*s.eye(4),s.zeros(4,3))
class TestKernel(unittest.TestCase):
    def test_rank(self): self.assertEqual(J.rank(),4)
    def test_nullity(self): self.assertEqual(len(J.nullspace()),3)
    def test_full_columns(self):
        self.assertEqual(J[:,0:4].det(),r**4/q**4)
    def test_kernel(self):
        for v in J.nullspace(): self.assertEqual(J*v,s.zeros(4,1))
    def test_four_spacetime_blocks(self):
        full=s.diag(J,J,J,J)
        self.assertEqual(full.rank(),16)
        self.assertEqual(len(full.nullspace()),12)
if __name__=='__main__': unittest.main()
