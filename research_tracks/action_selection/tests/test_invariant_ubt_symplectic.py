"""Exact algebra checks of candidate invariant biquaternion symplectic structure."""
import unittest
import sympy as s
K=s.diag(1,1,-1,-1,-1,-1,-1,-1)
J=s.diag(*([s.Matrix([[0,-1],[1,0]])]*4))
O=K*J
x=s.Matrix(s.symbols("x0:8"))
H=(x.T*K*x)[0]/2
class Symplectic(unittest.TestCase):
    def test_complex_structure(self): self.assertEqual(J*J,-s.eye(8))
    def test_skew(self): self.assertEqual(O.T,-O)
    def test_nondegenerate(self):
        self.assertEqual(O.rank(),8)
        self.assertEqual(O.det(),1)
    def test_orthogonal_j(self): self.assertEqual(J.T*K*J,K)
    def test_phase_flow(self):
        dH=s.Matrix([s.diff(H,z) for z in x])
        self.assertEqual(s.simplify(-O.inv()*dH-J*x),s.zeros(8,1))
if __name__=="__main__":unittest.main()
