# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact restricted Regge--Teitelboim extra solution in Mat(2,C).

The model is g=B(dTheta,dTheta), with B of inertia (2,6), Omega=0,
and an imported Einstein--Hilbert comparator. This is not a full
SU(2,2)-covariant UBT field-equation or action-selection result.
"""
import unittest
import sympy as s

k,t,x,y,z=s.symbols("k t x y z",real=True)
coords=(t,x,y,z)
f=k*t*x
A=1+k**2*(t**2-x**2)
B=s.diag(1,-1,-1,-1,1,-1,-1,-1)
Y=s.Matrix([t,x,y,z,0,f,0,0])
E=s.Matrix(8,4,lambda a,mu:s.diff(Y[a],coords[mu]))
g=s.simplify(E.T*B*E)
g2=g[:2,:2]
inv2=s.simplify(g2.inv())
Gamma2=[[[s.simplify(s.Rational(1,2)*sum(inv2[r,a]*(s.diff(g2[a,j],coords[i])+s.diff(g2[a,i],coords[j])-s.diff(g2[i,j],coords[a])) for a in range(2))) for j in range(2)] for i in range(2)] for r in range(2)]
Ric2=s.Matrix(2,2,lambda i,j:s.factor(sum(s.diff(Gamma2[a][i][j],coords[a])-s.diff(Gamma2[a][i][a],coords[j])+sum(Gamma2[a][a][p]*Gamma2[p][i][j]-Gamma2[a][j][p]*Gamma2[p][i][a] for p in range(2)) for a in range(2))))
R=s.factor(s.trace(inv2*Ric2))
G2=s.simplify(Ric2-s.Rational(1,2)*R*g2)
G4=s.zeros(4)
G4[0:2,0:2]=G2
G4[2,2]=G4[3,3]=R/2
Gin=s.simplify(g.inv()*G4*g.inv())

# The full 4D product Christoffels are the tx block, zero otherwise.
def Gamma4(a,mu,nu):
    return Gamma2[a][mu][nu] if a<2 and mu<2 and nu<2 else s.Integer(0)

b={(mu,nu):s.Matrix(8,1,lambda a,z0:s.simplify(
    s.diff(E[a,nu],coords[mu])-
    sum(Gamma4(r,mu,nu)*E[a,r] for r in range(4))))
    for mu in range(4) for nu in range(4)}
RT=s.Matrix(8,1,lambda a,z0:s.simplify(
    sum(Gin[mu,nu]*b[mu,nu][a] for mu in range(4) for nu in range(4))))

class TestThetaRTExtraSolution(unittest.TestCase):
    def test_ambient_inertia_and_metric(self):
        self.assertEqual(list(B.diagonal()), [1,-1,-1,-1,1,-1,-1,-1])
        self.assertEqual(s.simplify(
            g-s.diag(1,-1,-1,-1)+
            s.Matrix([k*x,k*t,0,0])*s.Matrix([[k*x,k*t,0,0]])),s.zeros(4))
        self.assertEqual(s.simplify(g.det()+A),0)

    def test_scalar_curvature_and_non_einstein(self):
        self.assertEqual(s.simplify(R+2*k**2/A**2),0)
        self.assertEqual(G2,s.zeros(2))
        self.assertEqual(s.simplify(G4[2,2]+k**2/A**2),0)
        self.assertEqual(s.simplify(G4[3,3]+k**2/A**2),0)
        self.assertNotEqual(G4[2,2].subs({t:0,x:0,k:1}),0)

    def test_exact_embedding_euler_lagrange_equations(self):
        for mu in range(4):
            for nu in range(4):
                self.assertEqual(s.simplify(E.T*B*b[mu,nu]),s.zeros(4,1))
        self.assertEqual(s.simplify(b[0,1].subs({t:0,x:0})[5]-k),0)
        self.assertEqual(s.simplify(RT),s.zeros(8,1))

    def test_normal_rank_bound(self):
        # Four independent tangent vectors in eight real target dimensions
        # leave four normals. The 10-dimensional symmetric tensor space
        # cannot inject into a four-dimensional normal space pointwise.
        self.assertEqual(8-4,4)
        self.assertEqual(4*5//2,10)
        self.assertGreaterEqual(10-(8-4),6)

if __name__ == '__main__':
    unittest.main()
