import unittest
import sympy as s
I=s.I
a,b,c,d,k=s.symbols('a b c d k',real=True)
H=s.Matrix([[a,b+I*c],[b-I*c,d]])
X=I*H
A=s.Matrix([[1+I,2-I],[3+2*I,-1-I]])
def f(X,A,k):return A*X+X*A.H+k*X
class Test(unittest.TestCase):
 def test_lorentz_slice(self):self.assertEqual(s.simplify(f(X,A,k)+f(X,A,k).H),s.zeros(2))
 def test_traceless(self):self.assertEqual(s.trace(A),0)
 def test_determinant_scaling(self):
  z=s.symbols('z',real=True)
  Y=H
  pert=A*Y+Y*A.H+k*Y
  self.assertEqual(s.simplify(s.diff((Y+z*pert).det(),z).subs(z,0)-2*k*Y.det()),0)
 def test_right_relation(self):
  B=-A.H+k*s.eye(2)
  self.assertEqual(s.simplify(A*X-X*B-f(X,A,-k)),s.zeros(2))
if __name__=='__main__':unittest.main()
