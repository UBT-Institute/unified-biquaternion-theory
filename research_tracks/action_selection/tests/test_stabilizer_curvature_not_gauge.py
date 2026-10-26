import unittest
import sympy as s
t,x,y,z=s.symbols('t x y z',real=True)
eta=s.diag(-1,1,1,1)
J=s.zeros(4);J[1,3]=1;J[3,1]=-1
class Checks(unittest.TestCase):
 def test_spin_lie_algebra(self):self.assertEqual(J.T*eta+eta*J,s.zeros(4))
 def test_stabilizer_at_point(self):
  v=s.Matrix([2,0,0,0]);self.assertEqual(J*v,s.zeros(4))
 def test_zero_connection_at_point_nonzero_curvature(self):
  Cx=s.zeros(4);Cy=x*J
  Fxy=Cy.diff(x)-Cx.diff(y)+Cx*Cy-Cy*Cx
  self.assertEqual(Fxy,J)
  self.assertEqual(Cy.subs(x,0),s.zeros(4))
 def test_nonzero_spin_curvature(self):self.assertNotEqual(J,s.zeros(4))
if __name__=='__main__':unittest.main()
