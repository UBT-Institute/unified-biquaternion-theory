"""Exact 2pi central-element and SU(2) carrier obstruction checks."""
import unittest
import sympy as s
I=s.eye(2); z=s.zeros(2); m=-I
sx=s.Matrix([[0,1],[1,0]])
sy=s.Matrix([[0,-s.I],[s.I,0]])
sz=s.diag(1,-1)
basis=[I,sx,sy,sz]
def coords(M):
    return s.Matrix([s.trace(v*M)/2 for v in basis])
R=s.Matrix.hstack(*(coords(m*v*m.H) for v in basis))
D=s.diag(m,m)
class TestObstruction(unittest.TestCase):
    def test_congruence_central(self): self.assertEqual(R,s.eye(4))
    def test_spinor_central(self): self.assertEqual(D,-s.eye(4))
    def test_intertwiner_only_zero(self):
        T=s.Matrix(4,4,lambda i,j:s.symbols(f't{i}{j}'))
        self.assertEqual(s.solve(list(T*R-D*T),list(T)),{v:0 for v in T})
    def test_pauli_components(self):
        self.assertEqual(s.trace(sx*sy),0)
        self.assertEqual(s.trace(sx*sx),2)
if __name__=='__main__':unittest.main()
