"""Exact checks for a conditional, covariant rank-one splitting in B≅M2(C)."""
import unittest
import sympy as s

class TimeQubitAlgebra(unittest.TestCase):
    def test_weighted_projectors(self):
        N=s.diag(s.Integer(2),s.Rational(1,2))
        B=s.Matrix([[0,1],[1,0]])
        self.assertEqual(s.trace(N.inv()*B),0)
        c=s.sqrt(-N.det()/B.det())
        Q=c*N.inv()*B
        Pp=(s.eye(2)+Q)/2
        Pm=(s.eye(2)-Q)/2
        self.assertEqual(Q*Q,s.eye(2))
        self.assertEqual(Pp*Pp,Pp)
        self.assertEqual(Pm*Pm,Pm)
        self.assertEqual(Pp*Pm,s.zeros(2))
        self.assertEqual(Q.conjugate().T*N,N*Q)

    def test_sl2_covariance(self):
        N=s.diag(2,s.Rational(1,2))
        B=s.Matrix([[0,1],[1,0]])
        L=s.diag(2,s.Rational(1,2))  # det=1 Lorentz boost
        Q=N.inv()*B
        N1=L*N*L.conjugate().T
        B1=L*B*L.conjugate().T
        Q1=N1.inv()*B1
        self.assertEqual(s.simplify(Q1-(L.conjugate().T).inv()*Q*L.conjugate().T),s.zeros(2))

    def test_generic_connection_mixes_projectors(self):
        sig1=s.Matrix([[0,1],[1,0]])
        sig3=s.diag(1,-1)
        P=(s.eye(2)+sig3)/2
        self.assertNotEqual(sig1*P-P*sig1,s.zeros(2))

    def test_holomorphic_cross_section(self):
        t,psi=s.symbols("t psi",real=True)
        V=t*t-psi*psi
        W=2*t*psi
        self.assertEqual(s.diff(V,psi),-s.diff(W,t))
        self.assertEqual(s.diff(W,psi),s.diff(V,t))
        self.assertEqual(W.subs(psi,0),0)
        self.assertEqual(s.diff(W,psi).subs(psi,0),s.diff(V,t).subs(psi,0))

    def test_periodic_imaginary_time_exponential_growth(self):
        t,psi,L=s.symbols("t psi L",real=True, positive=True)
        z=s.exp(2*s.pi*(t+s.I*psi)/L)
        self.assertEqual(s.simplify(z.subs(psi,psi+L)-z),0)
        self.assertEqual(s.simplify(z.subs(psi,0)),s.exp(2*s.pi*t/L))

if __name__=="__main__":
    unittest.main()
