"""Verify the local integrand algebra underlying the 1D functional bracket."""
import unittest
import sympy as s
a,b,N,M,Nx,Mx,p,qx,qxx,vprime=s.symbols("a b N M Nx Mx p qx qxx vprime")
dNq=Nx*qx+N*qxx
dMq=Mx*qx+M*qxx
expr=s.expand((-b*dNq+N*vprime)*(M*a*p)-(N*a*p)*(-b*dMq+M*vprime))
target=a*b*p*qx*(N*Mx-M*Nx)
class TestGradientClosure(unittest.TestCase):
 def test_local_identity(self):self.assertEqual(s.expand(expr-target),0)
 def test_potential_independence(self):self.assertEqual(s.diff(expr,vprime),0)
 def test_ultralocal_limit(self):self.assertEqual(expr.subs(b,0),0)
 def test_normalized(self):self.assertEqual(s.expand((expr-target).subs(b,1/a)),0)
if __name__=="__main__":unittest.main()
