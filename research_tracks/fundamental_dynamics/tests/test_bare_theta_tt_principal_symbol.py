import unittest
import sympy as s
kx=s.Matrix([0,0,1])
u=s.Matrix(s.symbols('u0:3', real=True))
P=s.eye(3)-kx*kx.T
H=kx*u.T+u*kx.T
TT=s.simplify(P*H*P-s.trace(P*H)*P/2)
class TestBareThetaPrincipalSymbol(unittest.TestCase):
 def test_bare_gradient_tt_zero(self):self.assertEqual(TT,s.zeros(3))
 def test_map_to_plus_cross_rank_zero(self):
  tt_plus=s.simplify(TT[0,0]-TT[1,1])
  tt_cross=TT[0,1]
  jac=s.Matrix([tt_plus,tt_cross]).jacobian(u)
  self.assertEqual(jac.rank(),0)
 def test_metric_symbol_not_identically_zero(self):self.assertNotEqual(H,s.zeros(3))
if __name__=='__main__':unittest.main()
