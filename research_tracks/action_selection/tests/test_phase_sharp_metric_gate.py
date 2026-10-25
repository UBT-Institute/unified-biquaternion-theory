import unittest
import sympy as s
a=s.symbols("a",real=True)
z=s.exp(s.I*a)
eta=s.diag(-1,1,1,1)
class PhaseMetric(unittest.TestCase):
 def test_phase_metric_weight_two(self):
  self.assertEqual(s.simplify(z*z*eta-s.exp(2*s.I*a)*eta),s.zeros(4))
 def test_pi_phase_preserves(self):
  self.assertEqual(s.simplify((z*z*eta-eta).subs(a,s.pi)),s.zeros(4))
 def test_half_pi_not_real_metric(self):
  self.assertEqual(s.simplify((z*z*eta).subs(a,s.pi/2)),-eta)
 def test_infinitesimal_changes_metric(self):
  self.assertEqual(s.diff(z*z,a).subs(a,0),2*s.I)
if __name__=="__main__":unittest.main()
