"""Metric-compatible connection with nonzero torsion trace: exact check."""
import unittest
import sympy as s
eta=s.diag(-1,1,1,1)
v=s.symbols("v0:4")
up=eta.inv()*s.Matrix(v)
def G(l,mu,nu):
 return (1 if l==mu else 0)*v[nu]-eta[mu,nu]*up[l]
def T(l,mu,nu):return G(l,mu,nu)-G(l,nu,mu)
class Torsion(unittest.TestCase):
 def test_metric_compatibility(self):
  for a in range(4):
   for b in range(4):
    for mu in range(4):
     self.assertEqual(s.simplify(sum(G(k,mu,a)*eta[k,b]+G(k,mu,b)*eta[a,k] for k in range(4))),0)
 def test_trace(self):
  for nu in range(4):
   self.assertEqual(s.expand(sum(T(mu,mu,nu) for mu in range(4))),3*v[nu])
 def test_volume_trace(self):
  for nu in range(4):
   self.assertEqual(s.expand(sum(G(mu,nu,mu) for mu in range(4))),0)
   self.assertEqual(s.expand(sum(G(mu,mu,nu) for mu in range(4))),3*v[nu])
if __name__=="__main__":unittest.main()
