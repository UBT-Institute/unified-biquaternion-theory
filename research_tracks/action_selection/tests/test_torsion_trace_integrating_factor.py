"""Exact differential-form integrating-factor tests for torsion-trace flux."""
import unittest
import sympy as s
x,y=s.symbols('x y',real=True)
phi=x*x*y
t=[s.diff(phi,x),s.diff(phi,y)]
jx,jy=s.symbols('jx jy',real=True)
w=s.exp(phi)
class TestIntegratingFactor(unittest.TestCase):
 def test_exact_trace(self):
  self.assertEqual(s.diff(t[1],x)-s.diff(t[0],y),0)
 def test_weight_condition(self):
  self.assertEqual(s.simplify(s.diff(w,x)-w*t[0]),0)
  self.assertEqual(s.simplify(s.diff(w,y)-w*t[1]),0)
 def test_arbitrary_current_cancellation(self):
  self.assertEqual(s.simplify((s.diff(w,x)-w*t[0])*jx+(s.diff(w,y)-w*t[1])*jy),0)
 def test_nonclosed_example(self):
  tx,ty=-y, x
  self.assertEqual(s.diff(ty,x)-s.diff(tx,y),2)
if __name__=='__main__':unittest.main()
