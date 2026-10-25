"""SymPy regression for formal H,H structure selector on a nondegenerate 1D patch."""
import unittest
import sympy as s
a,qx,p,N,M,Nx,Mx,Vp,Uprime=s.symbols('a qx p N M Nx Mx Vp Uprime', nonzero=True)
# Bracket after distributional integration by parts
integrand=s.expand((-Nx*Uprime+N*Vp)*(M*a*p)-(N*a*p)*(-Mx*Uprime+M*Vp))
class Tests(unittest.TestCase):
 def test_bracket(self):
  self.assertEqual(s.simplify(integrand-a*p*Uprime*(N*Mx-M*Nx)),0)
 def test_composite_selector(self):
  self.assertEqual(s.simplify((a*Uprime/qx-1/qx**2).subs(Uprime,1/(a*qx))),0)
 def test_log_derivative(self):
  z=s.symbols('z',positive=True)
  self.assertEqual(s.diff(s.log(z)/a,z),1/(a*z))
 def test_potential_cancels(self):
  self.assertEqual(s.diff(integrand,Vp),0)
if __name__=='__main__':unittest.main()
