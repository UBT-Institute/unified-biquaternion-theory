import unittest
import sympy as s
eta=s.diag(-1,1,1,1)
v=s.Matrix([2,1,0,0]);u=s.Matrix([1,2,0,0]);vv=(v.T*eta*v)[0]
w=(u*(v.T*eta)-v*(u.T*eta))/vv
class Tests(unittest.TestCase):
 def test_compatibility(self):self.assertEqual((v.T*eta*u)[0],0)
 def test_solution_nonzero(self):
  self.assertEqual(w*v,u)
  self.assertNotEqual(w,s.zeros(4))
 def test_lorentz_algebra(self):self.assertEqual(w.T*eta+eta*w,s.zeros(4))
 def test_incompatible_vector(self):
  wrong=s.Matrix([1,0,0,0]);self.assertNotEqual((v.T*eta*wrong)[0],0)
 def test_stabilizer_rank(self):
  gens=[]
  for a in range(4):
   for b in range(a+1,4):
    G=s.zeros(4);G[a,b]=eta[a,a];G[b,a]=-eta[b,b]
    gens.append(G*v)
  self.assertEqual(s.Matrix.hstack(*gens).rank(),3)
if __name__=='__main__':unittest.main()
