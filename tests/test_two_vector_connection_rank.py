"""Two-vector Lorentz connection reconstruction: rank 5 and one stabilizer."""
import unittest
import sympy as sp

eta=sp.diag(-1,1,1,1)
v=sp.Matrix([2,0,0,0]);w=sp.Matrix([1,1,0,0])
u=sp.Matrix([0,1,2,0]);z=sp.Matrix([sp.Rational(1,2),sp.Rational(1,2),3,-1])

def dot(a,b):
    return (a.T*eta*b)[0]

def wedge_map(a,b):
    return a*(b.T*eta)-b*(a.T*eta)

A=dot(v,v)
s=w-dot(v,w)/A*v
B=dot(s,s)
Omegav=wedge_map(u,v)/A
r=z-Omegav*w
Omega=Omegav+wedge_map(r,s)/B
G=[]
for a in range(4):
    for b in range(a+1,4):
        m=sp.zeros(4)
        m[a,b]=eta[a,a]
        m[b,a]=-eta[b,b]
        G.append(m)
rank=sp.Matrix.vstack(
    sp.Matrix.hstack(*[m*v for m in G]),
    sp.Matrix.hstack(*[m*w for m in G])
).rank()

class TestTwoVector(unittest.TestCase):
    def test_compatibility(self):
        self.assertEqual(dot(v,u),0)
        self.assertEqual(dot(w,z),0)
        self.assertEqual(dot(v,z)+dot(w,u),0)

    def test_constructive_solution(self):
        self.assertEqual(Omega.T*eta+eta*Omega,sp.zeros(4))
        self.assertEqual(Omega*v,u)
        self.assertEqual(Omega*w,z)

    def test_rank_and_residual_stabilizer(self):
        self.assertEqual(rank,5)
        J=sp.zeros(4);J[2,3]=1;J[3,2]=-1
        self.assertEqual(J*v,sp.zeros(4,1))
        self.assertEqual(J*w,sp.zeros(4,1))
        self.assertEqual((Omega+7*J)*v,u)
        self.assertEqual((Omega+7*J)*w,z)

    def test_norm_and_orthogonality(self):
        self.assertEqual(dot(v,s),0)
        self.assertGreater(B,0)
        self.assertEqual(dot(v,r),0)
        self.assertEqual(dot(s,r),0)

if __name__=="__main__":
    unittest.main()
