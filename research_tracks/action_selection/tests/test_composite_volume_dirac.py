"""Exact Dirac check of the existing reduced composite-volume FLRW Lagrangian."""
import sympy as s
import unittest
a,r,ad,rd,pa,pr,V,q=s.symbols("a r ad rd pa pr V q",real=True)
F=s.Function("F")
f=F(r)
L=V*a**3*f*rd/q
phi_a=pa
phi_r=pr-V*a**3*f/q
def pb(x,y):
    return s.diff(x,a)*s.diff(y,pa)-s.diff(x,pa)*s.diff(y,a)+s.diff(x,r)*s.diff(y,pr)-s.diff(x,pr)*s.diff(y,r)
class TestDirac(unittest.TestCase):
    def test_momenta(self):
        self.assertEqual(s.diff(L,ad),0)
        self.assertEqual(s.simplify(s.diff(L,rd)-V*a**3*f/q),0)
    def test_poisson(self):
        self.assertEqual(s.simplify(pb(phi_a,phi_r)-3*V*a*a*f/q),0)
    def test_hamiltonian(self):
        self.assertEqual(s.simplify(s.diff(L,rd)*rd+s.diff(L,ad)*ad-L),0)
    def test_a_euler(self):
        self.assertEqual(s.simplify(s.diff(L,a)-s.diff(s.diff(L,ad),r)*rd),3*V*a*a*f*rd/q)
    def test_r_euler(self):
        e=s.diff(L,r)-s.diff(s.diff(L,rd),r)*rd-s.diff(s.diff(L,rd),a)*ad
        self.assertEqual(s.simplify(e),-3*V*a*a*f*ad/q)
if __name__=="__main__":
    unittest.main()
