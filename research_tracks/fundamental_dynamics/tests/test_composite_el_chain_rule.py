import unittest
import sympy as s
a,v,z,acc,p=s.symbols('a v z acc p', real=True, nonzero=True)
Lext=(v*v+z*z)/2
Lred=s.expand(Lext.subs(z,a*v))
class TestCompositeElimination(unittest.TestCase):
 def test_correct_momentum(self):
  self.assertEqual(s.diff(Lred,v),(1+a*a)*v)
  self.assertEqual(s.diff(Lext,v),v)
 def test_reduced_hessian(self):
  self.assertEqual(s.diff(Lred,v,2),1+a*a)
 def test_el_chain_rule(self):
  # E_q=-q_ddot; (DZ)^* E_z = -a dot(z) = -a^2 q_ddot.
  explicit=-acc
  connection=-a*a*acc
  self.assertEqual(s.simplify(explicit+connection+(1+a*a)*acc),0)
 def test_reduced_hamiltonian(self):
  H=s.expand(p*v-Lred).subs(v,p/(1+a*a))
  self.assertEqual(s.simplify(H-p*p/(2*(1+a*a))),0)
if __name__=='__main__':unittest.main()
