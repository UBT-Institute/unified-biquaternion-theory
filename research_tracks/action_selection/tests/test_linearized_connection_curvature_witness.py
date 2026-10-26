"""Symbolic witness for non-pure-gauge linearized curvature."""
import unittest
import sympy as s
t=s.symbols("t",real=True)
f=s.Function("f")(t)
h=s.zeros(4);h[1,1]=f;h[2,2]=-f
def derivative(expr,index):
 return s.diff(expr,t) if index==0 else s.S.Zero
def riemann(mu,nu,rho,sigma):
 return s.simplify((derivative(derivative(h[mu,sigma],rho),nu)+derivative(derivative(h[nu,rho],sigma),mu)-derivative(derivative(h[nu,sigma],rho),mu)-derivative(derivative(h[mu,rho],sigma),nu))/2)
class Checks(unittest.TestCase):
 def test_first_curvature(self):
  self.assertEqual(riemann(0,1,0,1),-s.diff(f,t,2)/2)
 def test_second_curvature(self):
  self.assertEqual(riemann(0,2,0,2),s.diff(f,t,2)/2)
 def test_explicit_nonzero(self):
  self.assertEqual(riemann(0,1,0,1).subs(f,t**2).doit(),-1)
if __name__=="__main__":unittest.main()
