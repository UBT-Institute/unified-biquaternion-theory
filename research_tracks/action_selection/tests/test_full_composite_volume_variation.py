import unittest
import sympy as s
h=s.symbols('h',real=True)
E=s.Matrix([[2,1,0,0],[0,3,1,0],[0,0,2,1],[1,0,0,2]])
dE=s.Matrix([[1,2,0,0],[0,0,3,0],[0,1,0,0],[1,0,2,1]])
q,a=s.symbols('q a')
class Checks(unittest.TestCase):
 def test_jacobi_formula(self):
  lhs=s.diff((E+h*dE).det(),h).subs(h,0)
  rhs=s.simplify(E.det()*s.trace(E.inv()*dE))
  self.assertEqual(s.simplify(lhs-rhs),0)
 def test_composite_connection_variation(self):
  q0=s.symbols('q0')
  aa=s.Function('a')
  source=aa(q0)*q0
  self.assertEqual(s.diff(source,q0),aa(q0)+q0*s.diff(aa(q0),q0))
if __name__=='__main__':unittest.main()
