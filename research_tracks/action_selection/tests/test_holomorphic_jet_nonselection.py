"""Exact holomorphic-jet counterexample, not a dynamical solution."""
import unittest
import sympy as s
t,p,lam=s.symbols("t p lam",real=True)
tau=t+s.I*p
f0=s.I*tau
f1=f0+s.I*lam*tau**2
def at_origin(f): return s.simplify(f.subs({t:0,p:0}))
class Holomorphic(unittest.TestCase):
 def test_cr(self):
  for f in [f0,f1]: self.assertEqual(s.simplify(s.diff(f,p)-s.I*s.diff(f,t)),0)
 def test_same_first_jet(self):
  self.assertEqual(at_origin(f0),at_origin(f1))
  self.assertEqual(at_origin(s.diff(f0,t)),at_origin(s.diff(f1,t)))
 def test_distinct_second_jet(self):
  self.assertEqual(s.simplify(at_origin(s.diff(f1,t,2))-at_origin(s.diff(f0,t,2))),2*s.I*lam)
 def test_flat_slice_lorentz_tetrad(self):
  self.assertEqual(s.simplify(s.diff(f1,t).subs(p,0)),s.I*(1+2*lam*t))
if __name__=="__main__":unittest.main()
