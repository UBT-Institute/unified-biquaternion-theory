"""Fixed-background Hilbert/canonical energy agreement, exact ADM spot checks."""
import unittest
import sympy as s
N,rt,c,k,v,w,shift,U,omega,q=s.symbols('N rt c k v w shift U omega q', real=True, nonzero=True)
p=c*rt*k*v/N
lag=N*rt*(c*k*v*v/(2*N*N)-c*k*w*w/2-U)
rho=c*k*v*v/(2*N*N)+c*k*w*w/2+U
j=c*k*v*w/N
ham=s.expand(p*(v+shift*w-omega*q)-lag)
class Tests(unittest.TestCase):
    def test_exact_charge_identity(self):
        self.assertEqual(s.simplify(ham-(N*rt*rho+shift*rt*j-p*omega*q)),0)
    def test_vanish_temporal_connection(self):
        self.assertEqual(s.simplify(ham.subs(omega,0)-(N*rt*rho+shift*rt*j)),0)
    def test_momentum_flux(self):
        self.assertEqual(s.simplify(rt*j-p*w),0)
if __name__=="__main__":
    unittest.main()
