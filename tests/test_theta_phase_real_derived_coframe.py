# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Constructive real coframe from a complex Theta phase-covariant Gram metric.

Trial Mat(2,C) / SL(2,C) realization only: no independent tetrad,
no action/field equations, and no claim of fundamental SU(2,2) closure.
"""
import unittest
import sympy as s

I=s.eye(2)
sigmas=[I,s.Matrix([[0,1],[1,0]]),
        s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
t,x,y,z,k=s.symbols("t x y z k",real=True)
coordinates=(t,x,y,z)
Q=(t+2)*I+x*sigmas[1]+y*sigmas[2]+z*sigmas[3]+s.I*k*t*x*sigmas[1]

def adj(m):
    return s.Matrix([[m[1,1],-m[0,1]],[-m[1,0],m[0,0]]])

def B(a,b):
    return s.factor(s.re(s.trace(adj(a)*b.conjugate().T))/2)

def info(m):
    N=B(m,m)
    j=[s.factor(B(s.I*m,s.diff(m,u))/N) for u in coordinates]
    D=[s.diff(m,u)-s.I*j[i]*m for i,u in enumerate(coordinates)]
    return N,j,D

N,j,D=info(Q)
g=s.Matrix(4,4,lambda i,l:B(D[i],D[l]))
a=s.factor(g[0,0])
b=s.factor(g[0,1])
c=s.factor(g[1,1])
Delta=s.factor(b*b-a*c)

class TestRealCoframeFromComplexTheta(unittest.TestCase):
    def test_complex_field_and_real_gram(self):
        expected=s.diag(1,-1,-1,-1)-k*k*s.Matrix([x,t,0,0])*s.Matrix([[x,t,0,0]])
        expected-=s.diag(k*k*x**4/N,0,0,0)
        self.assertEqual(s.simplify(g-expected),s.zeros(4))
        self.assertEqual(g,g.T)
        self.assertEqual(s.im(g),s.zeros(4))
        self.assertEqual(s.simplify(j[0]+k*x**2/N),0)
        self.assertEqual(j[1:],[0,0,0])

    def test_covariant_phase_projector_exact_nontrivial_local_jet(self):
        realB=s.diag(1,-1,-1,-1,1,-1,-1,-1)
        J=s.zeros(8)
        J[:4,4:]=-s.eye(4)
        J[4:,:4]=s.eye(4)
        R=s.Rational(3,5)*s.eye(8)+s.Rational(4,5)*J
        self.assertEqual(R.T*realB*R,realB)
        q=s.Matrix([2,1,0,0,0,0,1,0])
        v=s.Matrix([3,-1,2,0,0,1,0,2])
        d_alpha=s.symbols("d_alpha",real=True)
        dot=lambda p,w:s.simplify((p.T*realB*w)[0])
        current=lambda p,w:dot(J*p,w)/dot(p,p)
        j0=current(q,v)
        q1=R*q
        v1=R*(v+d_alpha*J*q)
        j1=current(q1,v1)
        self.assertEqual(s.simplify(j1-j0-d_alpha),0)
        U0=v-j0*J*q
        U1=v1-j1*J*q1
        self.assertEqual(s.simplify(U1-R*U0),s.zeros(8,1))
        self.assertEqual(s.simplify(dot(U1,U1)-dot(U0,U0)),0)

    def test_indefinite_gram_real_tetrad_factorization_identity(self):
        aa,bb,cc=s.symbols("aa bb cc",real=True,positive=True)
        # bb may be any real: use independent unconstrained symbol.
        bb=s.symbols("bb",real=True)
        Delta0=bb**2-aa*cc
        # Timelike patch: aa>0 and Delta0>0.
        L=s.sqrt(aa)
        F=s.sqrt(Delta0/aa)
        e=s.eye(4)
        e[0,0]=L
        e[0,1]=bb/L
        e[1,1]=F
        eta=s.diag(1,-1,-1,-1)
        target=s.Matrix([[aa,bb,0,0],[bb,cc,0,0],
                         [0,0,-1,0],[0,0,0,-1]])
        self.assertEqual(s.simplify(e.T*eta*e-target),s.zeros(4))

    def test_curved_patch_real_coframe_non_degenerate(self):
        origin={t:0,x:0,y:0,z:0}
        point={t:1,x:0,y:0,z:0}
        self.assertEqual(s.simplify(a.subs(origin)),1)
        self.assertEqual(s.simplify(Delta.subs(origin)),1)
        self.assertEqual(s.simplify(a.subs(point)),1)
        self.assertEqual(s.simplify(Delta.subs(point)),1+k*k)
        self.assertEqual(s.simplify(g.subs(point)),
                         s.diag(1,-1-k*k,-1,-1))
        # e^0=sqrt(a)dt+(b/sqrt(a))dx, e^1=sqrt(Delta/a)dx
        # e^2=dy, e^3=dz; this is real and local where a,Delta>0.

    def test_nonzero_curvature_at_flat_first_jet_origin(self):
        origin={t:0,x:0,y:0,z:0}
        for i in range(4):
            for l in range(4):
                for coord in coordinates:
                    self.assertEqual(s.simplify(s.diff(g[i,l],coord).subs(origin)),0)
        # All Christoffels vanish at origin. R_tx_tx is the linear
        # Riemann expression at this point with the declared convention.
        R=s.simplify((
            2*s.diff(g[0,1],t,x)-s.diff(g[1,1],t,2)
            -s.diff(g[0,0],x,2))/2).subs(origin)
        self.assertEqual(R,k*k)

    def test_jets_not_hermitian_even_when_real_tetrad_exists(self):
        point={t:1,x:0,y:0,z:0}
        Dx=s.simplify(D[1].subs(point))
        self.assertEqual(Dx,(1+s.I*k)*sigmas[1])
        self.assertEqual(s.simplify((Dx-Dx.conjugate().T)/2),
                         s.I*k*sigmas[1])
        # The real coframe is derived from g, NOT identified with D_xQ.

    def test_no_independent_tetrad_and_local_lorentz_nonuniqueness(self):
        boost=s.Matrix([[s.Rational(5,4),s.Rational(3,4),0,0],
                        [s.Rational(3,4),s.Rational(5,4),0,0],
                        [0,0,1,0],[0,0,0,1]])
        eta=s.diag(1,-1,-1,-1)
        self.assertEqual(boost.T*eta*boost,eta)
        e=s.diag(1,s.sqrt(1+k*k),1,1)
        self.assertEqual(s.simplify(e.T*eta*e),
                         s.simplify((boost*e).T*eta*(boost*e)))

if __name__=="__main__":
    unittest.main()
