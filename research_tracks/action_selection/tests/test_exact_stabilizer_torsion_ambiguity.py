import unittest
import sympy as s
eta=s.diag(-1,1,1,1)
v=s.Matrix([2,0,0,0])
J=s.zeros(4);J[1,3]=1;J[3,1]=-1
# e_mu^a=delta_mu^a and connection one-form C=J dx^2
def C(mu):return J if mu==2 else s.zeros(4)
def T(a,mu,nu):return (C(mu)[a,nu]-C(nu)[a,mu])
class Test(unittest.TestCase):
 def test_metric_compatible(self):self.assertEqual(J.T*eta+eta*J,s.zeros(4))
 def test_preserves_theta_and_e(self):self.assertEqual(J*v,s.zeros(4))
 def test_changes_torsion(self):self.assertEqual(T(1,2,3),1)
 def test_stabilizer_rank(self):
  gens=[]
  for a in range(4):
   for b in range(a+1,4):
    G=s.zeros(4);G[a,b]=eta[a,a];G[b,a]=-eta[b,b]
    gens.append(G*v)
  self.assertEqual(s.Matrix.hstack(*gens).rank(),3)
if __name__=='__main__':unittest.main()
