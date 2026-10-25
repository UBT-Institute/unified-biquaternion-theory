import unittest
import sympy as s
alpha,beta,gamma=s.symbols('alpha beta gamma',nonzero=True)
t=s.symbols('t0:4');a=s.symbols('a0:4');q=s.symbols('q0:16')
variables=t+a+q
L=alpha*sum(x*x for x in t)/2+beta*sum(x*x for x in a)/2+gamma*sum(x*x for x in q)/2
H=s.hessian(L,variables)
class Checks(unittest.TestCase):
 def test_full_rank(self):self.assertEqual(H.rank(),24)
 def test_unique_stationary(self):
  grad=[s.diff(L,x) for x in variables]
  self.assertEqual(s.solve(grad,variables),{x:0 for x in variables})
 def test_sources(self):
  jt,ja,jq=s.symbols('jt ja jq')
  x,y,z=s.symbols('x y z')
  V=alpha*x*x/2+jt*x+beta*y*y/2+ja*y+gamma*z*z/2+jq*z
  self.assertEqual(s.solve([s.diff(V,v) for v in (x,y,z)],(x,y,z)),{x:-jt/alpha,y:-ja/beta,z:-jq/gamma})
if __name__=='__main__':unittest.main()
