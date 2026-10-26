import unittest
import sympy as s
k=s.symbols('k',real=True)
# omega[a,b,m], corresponding to omega^a_b = omega[a,b,m] dx^m
w=s.MutableDenseNDimArray.zeros(4,4,4)
w[0,1,2]=k;w[1,0,2]=k
eta=[-1,1,1,1]
class Checks(unittest.TestCase):
 def test_metric_compatibility(self):
  for a in range(4):
   for b in range(4):
    for m in range(4):
     self.assertEqual(eta[a]*w[a,b,m]+eta[b]*w[b,a,m],0)
 def test_nonzero_torsion(self):
  def tors(a,m,n):return sum(w[a,b,m]*int(b==n)-w[a,b,n]*int(b==m) for b in range(4))
  self.assertEqual(tors(0,2,1),k)
  self.assertEqual(tors(1,2,0),k)
 def test_flat_spin_curvature(self):
  for a in range(4):
   for b in range(4):
    for m in range(4):
     for n in range(4):
      R=sum(w[a,c,m]*w[c,b,n]-w[a,c,n]*w[c,b,m] for c in range(4))
      self.assertEqual(R,0)
if __name__=="__main__":unittest.main()
