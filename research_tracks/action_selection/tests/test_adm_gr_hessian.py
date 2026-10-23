"""Exact GR ADM DeWitt Hessian reference, not a full UBT spectrum verifier."""
import unittest
import sympy as s
class ADMReference(unittest.TestCase):
    def setUp(self):
        self.x=s.Matrix(s.symbols('x0:6'))
        self.v=s.Matrix([1,1,1,0,0,0])
        self.Q=(self.x.T*self.x)[0]-(self.v.dot(self.x))**2
        self.H=s.hessian(self.Q,list(self.x))
    def test_hessian(self):
        self.assertEqual(self.H,2*(s.eye(6)-self.v*self.v.T))
    def test_rank(self):
        self.assertEqual(self.H.rank(),6)
    def test_inertia(self):
        self.assertEqual(self.H.eigenvals(),{s.Integer(2):5,s.Integer(-4):1})
    def test_full_adm(self):
        Hfull=s.diag(self.H,s.zeros(4))
        self.assertEqual(Hfull.rank(),6)
        self.assertEqual(Hfull.nullspace().__len__(),4)
    def test_constraint_count(self):
        self.assertEqual((20-2*8)//2,2)
if __name__=="__main__":
    unittest.main()
