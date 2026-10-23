import unittest
import sympy as s
J=s.Matrix([[0,-1],[1,0]])
K=s.eye(2)
O=K*J
k,c,m=s.symbols("k c m",real=True)
x=s.Matrix(s.symbols("x0:2"))
A=(c*k*k+m*m)*K
class Dispersion(unittest.TestCase):
    def test_symplectic(self):
        self.assertEqual(O.T,-O)
        self.assertNotEqual(O.det(),0)
    def test_mode_flow(self):
        flow=-O.inv()*A*x
        self.assertEqual(s.simplify(flow-J*(c*k*k+m*m)*x),s.zeros(2,1))
    def test_phase_preserves_norm(self):
        flow=J*x
        self.assertEqual(s.expand((x.T*K*flow)[0]),0)
    def test_quadratic_frequency(self):
        self.assertEqual(s.det(s.Symbol("freq")*s.eye(2)-(c*k*k+m*m)*J),
                         s.Symbol("freq")**2+(c*k*k+m*m)**2)
if __name__=="__main__": unittest.main()
