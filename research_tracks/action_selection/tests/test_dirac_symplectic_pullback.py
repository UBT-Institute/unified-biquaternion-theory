"""Exact flat Fourier-mode Dirac symplectic-pullback obstruction."""
import unittest
import sympy as s
I=s.I
sx=s.Matrix([[0,1],[1,0]]); sy=s.Matrix([[0,-I],[I,0]]); sz=s.diag(1,-1)
x=s.Matrix(s.symbols('x0:8',real=True))
Y=s.Matrix(s.symbols('y0:8',real=True))
def theta(v):
    return s.Matrix([[v[0]+I*v[1],v[4]+I*v[5]],[v[2]+I*v[3],v[6]+I*v[7]]])
def realvec(z):
    return s.Matrix([a for w in z for a in s.expand_complex(w).as_real_imag()])
X=theta(x); W=theta(Y)
B=s.expand_complex(s.trace(X.adjugate()*W.conjugate().T)).as_real_imag()[0].expand()
K=s.Matrix(8,8,lambda a,b:s.diff(B,x[a],Y[b]))
J=s.diag(*([s.Matrix([[0,-1],[1,0]])]*4))
O=K*J
p1,p2,p3,m=s.symbols('p1 p2 p3 m',real=True)
P=p1*sx+p2*sy+p3*sz
Hd=s.BlockMatrix([[-P,m*s.eye(2)],[m*s.eye(2),P]]).as_explicit()
u=s.Matrix([X[0,0],X[1,0],s.conjugate(X[1,1]),-s.conjugate(X[0,1])])
du=-I*Hd*u
dx_complex=s.Matrix([du[0],du[1],-s.conjugate(du[3]),s.conjugate(du[2])])
A=realvec(dx_complex).jacobian(x)
C=s.simplify(A.T*O+O*A)
class Test(unittest.TestCase):
 def test_omega(self):
    self.assertEqual(O.T,-O)
    self.assertEqual(O.det(),1)
 def test_mass_obstruction(self):
    self.assertEqual(s.simplify(C[2,4].subs({p1:0,p2:0,p3:0})),2*m)
 def test_spatial_obstruction(self):
    self.assertNotEqual(C.subs({m:0,p1:1,p2:0,p3:0}),s.zeros(8))
 def test_zero_generator(self):
    self.assertEqual(C.subs({m:0,p1:0,p2:0,p3:0}),s.zeros(8))


def _numeric_dirac_flow(z, momentum, mass):
    p1,p2,p3=momentum
    u=[z[0],z[1],z[3].conjugate(),-z[2].conjugate()]
    def pauli(v):
        return [p3*v[0]+(p1-1j*p2)*v[1],(p1+1j*p2)*v[0]-p3*v[1]]
    a,b=pauli(u[:2]),pauli(u[2:])
    du=[-1j*(-a[k]+mass*u[k+2]) for k in range(2)]
    du += [-1j*(mass*u[k]+b[k]) for k in range(2)]
    return [du[0],du[1],-du[3].conjugate(),du[2].conjugate()]

class NumericCounterexample(unittest.TestCase):
    def test_native_mass_obstruction_without_cas_matrices(self):
        def omega(z,w):
            # Direct trace(adj(X) Y^dagger), X=[z0,z2;z1,z3].
            adj=[z[3],-z[1],-z[2],z[0]]
            return sum(a*b.conjugate() for a,b in zip(adj,w)).imag
        x=[0j,1+0j,0j,0j];y=[0j,0j,1+0j,0j]
        value=omega(_numeric_dirac_flow(x,(0,0,0),1),y)+omega(x,_numeric_dirac_flow(y,(0,0,0),1))
        self.assertAlmostEqual(value,2.0)

if __name__=='__main__': unittest.main()
