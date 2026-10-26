import unittest
import sympy as s
u=s.symbols("u0:4",real=True)
k,v1,N,c=s.symbols("k v1 N c",real=True,nonzero=True)
# Temporal coframe components include a nonzero boost connection contribution.
trow=[(u[0]+k*v1)/s.sqrt(N),u[1]/s.sqrt(N),u[2]/s.sqrt(N),u[3]/s.sqrt(N)]
e=s.Matrix([trow,[0,1,0,0],[0,0,1,0],[0,0,0,1]])
L=c*e.det()
p=[s.diff(L,x) for x in u]
class Checks(unittest.TestCase):
 def test_no_velocity_hessian(self):self.assertEqual(s.hessian(L,u),s.zeros(4))
 def test_primary_momenta(self):
  self.assertEqual(p[0],c/s.sqrt(N))
  self.assertEqual(p[1:], [0,0,0])
 def test_nonzero_connection_in_hamiltonian(self):
  H=s.expand(sum(p[i]*u[i] for i in range(4))-L)
  self.assertEqual(s.simplify(H+c*k*v1/s.sqrt(N)),0)
if __name__=="__main__":unittest.main()
