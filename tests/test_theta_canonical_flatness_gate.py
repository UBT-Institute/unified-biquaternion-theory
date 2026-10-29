# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact local sharp-metric gradient flatness and flat connection controls.

All claims are conditional: 4 complex components, regular central sharp
metric, SL(2,C)xSL(2,C) determinant-preserving gauge connections.
"""
import unittest
import sympy as s

I=s.eye(2)
S=(I,s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1))
ETA=s.diag(1,-1,-1,-1)

def sharp(A):return s.trace(A)*I-A

def C(A,B):return s.simplify(s.trace(sharp(A)*B)/2)

class TestCanonicalFlatnessGate(unittest.TestCase):
    def test_central_identity_for_generic_complex_jets(self):
        a,b,c,d,e,f,g,h=s.symbols('a b c d e f g h')
        A=s.Matrix([[a,b],[c,d]])
        B=s.Matrix([[e,f],[g,h]])
        self.assertEqual(s.simplify((sharp(A)*B+sharp(B)*A)/2-C(A,B)*I),s.zeros(2))

    def test_non_degenerate_metric_requires_invertible_complex_jacobian(self):
        aa,bb,cc,dd=s.symbols('aa bb cc dd')
        J=s.Matrix([[1,aa,0,0],[0,bb,cc,0],[0,0,1,dd],[0,0,0,1]])
        G=J.T*ETA*J
        self.assertEqual(s.factor(G.det()),-bb**2)
        self.assertEqual(s.factor(J.det()),bb)

    def test_rank_two_real_projection_real_lorentz_central_metric(self):
        t,x,y,z=s.symbols('t x y z',real=True)
        Q=s.I*z*I+x*S[1]+y*S[2]+s.I*t*S[3]
        j=[s.diff(Q,w) for w in (t,x,y,z)]
        g=s.Matrix(4,4,lambda i,k:C(j[i],j[k]))
        self.assertEqual(g,ETA)
        self.assertEqual(s.Matrix(4,4,lambda i,k:s.re(s.trace(S[i]*j[k])/2)).rank(),2)
        self.assertNotEqual(j[0].conjugate().T,j[0])

    def test_nonconstant_flat_metric_with_rank_two_real_projection(self):
        t,x,y,z=s.symbols('t x y z',real=True)
        X=x+y*z;T=t+x*x
        Q=s.I*z*I+X*S[1]+y*S[2]+s.I*T*S[3]
        w=(t,x,y,z)
        JJ=s.Matrix(4,4,lambda i,j:s.diff((T,X,y,z)[i],w[j]))
        G=JJ.T*ETA*JJ
        Cmat=s.Matrix(4,4,lambda i,j:C(s.diff(Q,w[i]),s.diff(Q,w[j])))
        self.assertEqual(s.simplify(Cmat-G),s.zeros(4))
        self.assertEqual(s.simplify(G.det()),-1)
        self.assertNotEqual(s.diff(G[0,1],x),0)
        Gam=[s.simplify(JJ.inv()*s.diff(JJ,w[mu])) for mu in range(4)]
        self.assertTrue(any(M!=s.zeros(4) for M in Gam))
        for mu in range(4):
            for nu in range(mu+1,4):
                R=s.simplify(s.diff(Gam[nu],w[mu])-s.diff(Gam[mu],w[nu])
                             +Gam[mu]*Gam[nu]-Gam[nu]*Gam[mu])
                self.assertEqual(R,s.zeros(4))

    def test_complex_jacobian_pure_gradient_curvature_zero_identity(self):
        t,x,y,z,a=s.symbols('t x y z a',real=True)
        w=(t,x,y,z)
        Z=(t+s.I*a*x,x+s.I*a*t+y*z,y,z)
        JJ=s.Matrix(4,4,lambda i,j:s.diff(Z[i],w[j]))
        self.assertNotEqual(s.factor(JJ.det()),0)
        connection=[s.simplify(JJ.inv()*s.diff(JJ,k)) for k in w]
        for mu in range(4):
            for nu in range(mu+1,4):
                curve=s.simplify(s.diff(connection[nu],w[mu])
                                -s.diff(connection[mu],w[nu])
                                +connection[mu]*connection[nu]
                                -connection[nu]*connection[mu])
                self.assertEqual(curve,s.zeros(4))

    def test_left_right_sl2_gauge_keeps_sharp_metric(self):
        aa,bb,tt=s.symbols('aa bb tt',real=True)
        A=(1+s.I*aa)*I+bb*S[1]
        B=S[2]+tt*S[3]
        L=s.diag(2,s.Rational(1,2))
        R=s.Matrix([[1,3],[0,1]])
        self.assertEqual(s.simplify(C(L*A*R.inv(),L*B*R.inv())-C(A,B)),0)

    def test_nonzero_flat_connections_can_be_pure_gauge(self):
        t,x=s.symbols('t x',real=True)
        Q=s.Matrix([[s.exp(t),x],[0,s.exp(-t)]])
        K=[s.simplify(s.diff(Q,w)*Q.inv()) for w in (t,x)]
        A=[-M for M in K]
        self.assertTrue(any(M!=s.zeros(2) for M in A))
        self.assertEqual(s.simplify(s.diff(A[1],t)-s.diff(A[0],x)
                                    +A[0]*A[1]-A[1]*A[0]),s.zeros(2))
        for i,w in enumerate((t,x)):
            self.assertEqual(s.simplify(s.diff(Q,w)+A[i]*Q),s.zeros(2))

    def test_unimodular_maurer_cartan_traceless_gives_rank_one(self):
        t,x=s.symbols('t x',real=True)
        Q=s.Matrix([[2+t,x],[x,3+t]])
        D=[]
        for w in (t,x):
            K=s.simplify(s.diff(Q,w)*Q.inv())
            A=-(K-s.trace(K)*I/2)
            D.append(s.simplify(s.diff(Q,w)+A*Q))
            self.assertEqual(s.simplify(D[-1]-s.trace(K)*Q/2),s.zeros(2))
        G=s.Matrix(2,2,lambda i,j:C(D[i],D[j]))
        self.assertEqual(s.simplify(G.det()),0)
        self.assertEqual(s.simplify(G[0,0]).subs({t:0,x:0}),s.Rational(25,24))

    def test_nonzero_connection_curvature_not_sufficient(self):
        t,x,y,z=s.symbols('t x y z',real=True)
        w=(t,x,y,z)
        Q=t*I+x*S[1]+y*S[2]+z*S[3]
        Z=x*S[1]+y*S[2]+z*S[3]
        Omega=(s.zeros(2),s.I*t*Z,s.zeros(2),s.zeros(2))
        jets=[s.simplify(s.diff(Q,v)+Omega[i]*Q+Q*Omega[i].conjugate().T)
              for i,v in enumerate(w)]
        self.assertEqual(jets,[I,S[1],S[2],S[3]])
        self.assertEqual(s.Matrix(4,4,lambda i,j:C(jets[i],jets[j])),ETA)
        Ft_x=s.diff(Omega[1],t)
        self.assertEqual(Ft_x,s.I*Z)
        self.assertEqual(s.simplify(Ft_x*Q-Q*Ft_x),s.zeros(2))
        self.assertNotEqual(Ft_x.subs({t:0,x:1,y:0,z:0}),s.zeros(2))

    def test_metric_blind_to_nontrivial_spin_holonomy(self):
        lam,dt,dx,x0=s.symbols('lam dt dx x0',real=True)
        phase=lam*dt*(x0*dx+dx**2/2)
        # Along y=z=0, Omega_x=i*lam*t*x*sigma1; rectangular
        # holonomy consists of commuting parallel transports.
        hol=s.cos(phase)*I+s.I*s.sin(phase)*S[1]
        self.assertEqual(s.simplify(s.trace(hol)-2*s.cos(phase)),0)
        self.assertEqual(s.simplify(hol.det()),1)
        values={lam:1,dt:s.Rational(1,3),dx:s.Rational(1,2),x0:1}
        self.assertEqual(phase.subs(values),s.Rational(5,24))
        self.assertNotEqual(s.simplify(s.trace(hol).subs(values)),2)
        rotation=s.diag(s.I,-s.I)
        self.assertEqual(s.simplify(s.trace(rotation*hol*rotation.inv())
                                    -s.trace(hol)),0)
        # The canonical metric is exactly eta, independently of lam.

    def test_two_sided_covariant_derivative_transform_exactly(self):
        t=s.symbols('t',real=True)
        Q=s.Matrix([[2,t],[0,3]])
        dQ=s.diff(Q,t)
        A=s.Matrix([[0,1],[0,0]])
        B=s.Matrix([[0,0],[1,0]])
        L=s.diag(s.exp(t),s.exp(-t))
        R=s.Matrix([[1,t],[0,1]])
        Qnew=L*Q*R.inv()
        Anew=L*A*L.inv()-s.diff(L,t)*L.inv()
        Bnew=R*B*R.inv()-s.diff(R,t)*R.inv()
        old=dQ+A*Q-Q*B
        new=s.diff(Qnew,t)+Anew*Qnew-Qnew*Bnew
        self.assertEqual(s.simplify(new-L*old*R.inv()),s.zeros(2))

if __name__=='__main__':unittest.main()
