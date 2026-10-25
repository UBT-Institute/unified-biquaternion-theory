import unittest
import sympy as s
n=12
c=s.symbols('c0:'+str(n))
p=s.symbols('p0:'+str(n))
m=s.symbols('m',nonzero=True)
j=s.symbols('j0:'+str(n))
L=sum(m*c[i]**2/s.Integer(2)+j[i]*c[i] for i in range(n))
V=s.symbols('v0:'+str(n))
K=s.symbols('k',nonzero=True)
Ld=sum(K*V[i]**2/s.Integer(2) for i in range(n))
class Checks(unittest.TestCase):
 def test_aux_no_velocity_hessian(self):self.assertEqual(s.hessian(L,V),s.zeros(n))
 def test_aux_equations(self):
  for i in range(n):self.assertEqual(s.solve(s.diff(L,c[i]),c[i])[0],-j[i]/m)
 def test_regular_velocity_hessian(self):
  self.assertEqual(s.hessian(Ld,V),K*s.eye(n))
 def test_second_class_aux_pairs(self):
  self.assertEqual(s.hessian(L,c),m*s.eye(n))
if __name__=='__main__':unittest.main()
