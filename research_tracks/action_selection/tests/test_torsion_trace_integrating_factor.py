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

class IndependentWeightChannel(unittest.TestCase):
    def test_direct_density_finite_differences(self):
        import math, random
        rng=random.Random(20261025)
        for _ in range(50):
            a,b=[rng.uniform(-1,1) for _ in range(2)];step=1e-5
            def weight(x,y):return math.exp(x*x*y)
            w=weight(a,b)
            dx=(weight(a+step,b)-weight(a-step,b))/(2*step)
            dy=(weight(a,b+step)-weight(a,b-step))/(2*step)
            self.assertAlmostEqual(dx-2*a*b*w,0.0,places=7)
            self.assertAlmostEqual(dy-a*a*w,0.0,places=7)
    def test_single_current_can_survive_nonclosed_trace(self):
        # t=(0,x), j=(1,0), e=w=1: both divergences vanish although dt=dx^dy.
        self.assertEqual(s.diff(x,x)-s.diff(0,y),1)
        self.assertEqual(0*1+x*0,0)

if __name__=='__main__':unittest.main()
