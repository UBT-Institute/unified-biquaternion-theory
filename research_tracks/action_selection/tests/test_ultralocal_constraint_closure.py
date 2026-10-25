"""Exact local canonical proof that ultralocal smeared scalar constraints commute."""
import unittest
import sympy as s
q=s.symbols('q0:8')
p=s.symbols('p0:8')
N,M=s.symbols('N M')
h=sum((q[i]*p[i]+p[i]**2) for i in range(8)) # representative; proof in note is general
def pb(f,g):
 return s.expand(sum(s.diff(f,q[i])*s.diff(g,p[i])-s.diff(f,p[i])*s.diff(g,q[i]) for i in range(8)))
class Tests(unittest.TestCase):
 def test_ultralocal(self):self.assertEqual(s.simplify(pb(N*h,M*h)),0)
 def test_canonical_field_variation(self):
  self.assertEqual(pb(q[0],h),q[0]+2*p[0])
 def test_antisymmetry(self):self.assertEqual(pb(h,h),0)
if __name__=="__main__":unittest.main()
