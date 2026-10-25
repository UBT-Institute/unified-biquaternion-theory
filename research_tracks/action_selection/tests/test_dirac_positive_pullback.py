import unittest
import sympy as s
I=s.I
sx=s.Matrix([[0,1],[1,0]])
sy=s.Matrix([[0,-I],[I,0]])
sz=s.diag(1,-1)
x=s.Matrix(s.symbols('x0:8',real=True))
def theta(v):return s.Matrix([[v[0]+I*v[1],v[4]+I*v[5]],[v[2]+I*v[3],v[6]+I*v[7]]])
def reim(z):return s.Matrix([a for w in z for a in s.expand_complex(w).as_real_imag()])
X=theta(x)
u=s.Matrix([X[0,0],X[1,0],s.conjugate(X[1,1]),-s.conjugate(X[0,1])])
Q=reim(u).jacobian(x)
J=s.diag(*([s.Matrix([[0,-1],[1,0]])]*4))
Omega=Q.T*J*Q
p1,p2,p3,m=s.symbols('p1 p2 p3 m',real=True)
P=p1*sx+p2*sy+p3*sz
H=s.BlockMatrix([[-P,m*s.eye(2)],[m*s.eye(2),P]]).as_explicit()
A=Q.inv()*reim(-I*H*u).jacobian(x)
class DiracPullback(unittest.TestCase):
 def test_invertible(self):self.assertNotEqual(Omega.det(),0)
 def test_positive_metric(self):self.assertEqual(Q.T*Q,s.eye(8))
 def test_skew(self):self.assertEqual(Omega.T,-Omega)
 def test_hamiltonian_flow(self):self.assertEqual(s.simplify(A.T*Omega+Omega*A),s.zeros(8))
 def test_dirac_square(self):self.assertEqual(s.simplify(H*H-(p1*p1+p2*p2+p3*p3+m*m)*s.eye(4)),s.zeros(4))


def _numeric_dirac_flow(z, momentum, mass):
    p1,p2,p3=momentum
    u=[z[0],z[1],z[3].conjugate(),-z[2].conjugate()]
    def pauli(v):
        return [p3*v[0]+(p1-1j*p2)*v[1],(p1+1j*p2)*v[0]-p3*v[1]]
    a,b=pauli(u[:2]),pauli(u[2:])
    du=[-1j*(-a[k]+mass*u[k+2]) for k in range(2)]
    du += [-1j*(mass*u[k]+b[k]) for k in range(2)]
    return [du[0],du[1],-du[3].conjugate(),du[2].conjugate()]

class NumericDiracChannel(unittest.TestCase):
    def test_direct_complex_flow_pairing(self):
        import random
        rng=random.Random(20261025)
        def f(z):return [z[0],z[1],z[3].conjugate(),-z[2].conjugate()]
        def omega(z,w):return -sum(a.conjugate()*b for a,b in zip(f(z),f(w))).imag
        for _ in range(50):
            x=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(4)]
            y=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(4)]
            p=[rng.uniform(-1,1) for _ in range(3)];mass=rng.uniform(-1,1)
            dx=_numeric_dirac_flow(x,p,mass);dy=_numeric_dirac_flow(y,p,mass)
            self.assertAlmostEqual(omega(dx,y)+omega(x,dy),0.0,places=12)
            self.assertAlmostEqual(sum(a.conjugate()*b for a,b in zip(f(x),f(dx))).real,0.0,places=12)

if __name__=='__main__':unittest.main()
