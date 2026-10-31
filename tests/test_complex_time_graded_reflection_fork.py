# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact complex-time gate for the previously constructed real-linear graded jet.

On a reflection-invariant complex-time domain, Schwarz-reflected star is
holomorphy preserving but nonlocal on the imaginary-time fiber. This is a
restricted mathematical compatibility result, NOT physical time dynamics.
"""
import unittest
import sympy as s

z=s.symbols("tau")
t,psi=s.symbols("t psi",real=True)
I=s.I
ONE=s.eye(2)
ZERO=s.zeros(2)
P=(s.Matrix([[0,1],[1,0]]),
   s.Matrix([[0,-I],[I,0]]),
   s.diag(1,-1))

def reflected(A):
    """F*(tau)=F(conjugate(tau))^dagger (holomorphic polynomial/entire case)."""
    return s.simplify(s.conjugate(A.subs(z,s.conjugate(z))).T)

def pplus(A):
    return (A+reflected(A))/2

def pminus(A):
    return (A-reflected(A))/2

def graded(A,K):
    X=pminus(A)
    return s.simplify(K*X+X*reflected(K))

def w_from_h(H):
    q=s.det(H)
    return s.simplify(-s.diff(q,z)/(2*q))

def jet(A,Omega,K):
    H=pplus(A)
    w=w_from_h(H)
    return s.simplify(s.diff(A,z)+Omega*A+A*reflected(Omega)
                      +w*A+graded(A,K))

class ComplexTimeGradedFork(unittest.TestCase):
    def test_reflected_involution(self):
        A=s.Matrix([[1+I*z,z*z],[I*z**2,s.exp(z)]])
        self.assertEqual(s.simplify(reflected(reflected(A))-A),ZERO)

    def test_reflected_antiautomorphism(self):
        A=s.Matrix([[z,I],[0,1]])
        B=s.Matrix([[2,z],[I*z,1+z]])
        self.assertEqual(s.simplify(reflected(A*B)-reflected(B)*reflected(A)),ZERO)

    def test_reflected_is_conjugate_linear_in_constants(self):
        A=s.Matrix([[z,1],[2,I*z]])
        self.assertEqual(s.simplify(reflected(I*A)+I*reflected(A)),ZERO)

    def test_reflected_commutes_with_complex_derivative(self):
        A=s.Matrix([[I*z**3,s.exp(z)],[z*z,1+I*z]])
        self.assertEqual(s.simplify(reflected(s.diff(A,z))-s.diff(reflected(A),z)),ZERO)

    def test_holomorphic_stardagger_decomposition(self):
        A=(1+z*z)*ONE+I*z*P[2]+I*z*ONE
        H=pplus(A)
        X=pminus(A)
        self.assertEqual(s.simplify(H+X-A),ZERO)
        self.assertEqual(s.simplify(reflected(H)-H),ZERO)
        self.assertEqual(s.simplify(reflected(X)+X),ZERO)
        self.assertEqual(s.simplify(s.diff(H,s.conjugate(z))),ZERO)

    def test_plain_dagger_is_antiholomorphic_off_real_axis(self):
        A=I*z*ONE
        pointwise=s.conjugate(A).T
        self.assertEqual(pointwise,-I*s.conjugate(z)*ONE)
        self.assertNotEqual(pointwise,reflected(A))
        self.assertEqual(reflected(A),-I*z*ONE)

    def test_graded_star_reality(self):
        A=ONE+I*z*(ONE+P[0])
        K=P[2]+I*P[1]
        Q=graded(A,K)
        self.assertEqual(s.simplify(reflected(Q)+Q),ZERO)
        self.assertNotEqual(Q,ZERO)

    def test_parallel_H_and_full_star_reality_of_jet(self):
        u=s.symbols("u",real=True)
        H=s.diag(s.exp(u*z),s.exp(-u*z))
        X=I*z*ONE
        Omega=-u*P[2]/2
        K=P[0]
        self.assertEqual(s.simplify(H-reflected(H)),ZERO)
        self.assertEqual(s.simplify(s.diff(H,z)+Omega*H+
                                  H*reflected(Omega)),ZERO)
        self.assertEqual(s.det(H),1)
        E=jet(H+X,Omega,K)
        self.assertEqual(s.simplify(reflected(E)+E),ZERO)
        self.assertNotEqual(E,ZERO)

    def test_local_holomorphic_boost_equivariance(self):
        u=s.symbols("u",real=True)
        S=s.diag(s.exp(u*z),s.exp(-u*z))
        A=ONE+I*z*(ONE+P[0])
        O=ZERO
        K=P[2]
        T=S*A*reflected(S)
        Op=s.simplify(S*O*S.inv()-s.diff(S,z)*S.inv())
        Kp=s.simplify(S*K*S.inv())
        self.assertEqual(s.simplify(jet(T,Op,Kp)-
                                  S*jet(A,O,K)*reflected(S)),ZERO)

    def test_reflection_real_scale_and_compensator(self):
        a=s.symbols("a",real=True)
        A=ONE+I*z*ONE
        eps=a*z
        L=s.exp(eps)
        self.assertEqual(reflected(L*ONE),L*ONE)
        self.assertEqual(s.simplify(w_from_h(pplus(L*A))+s.diff(eps,z)),0)
        self.assertEqual(s.simplify(jet(L*A,ZERO,P[2])-L*jet(A,ZERO,P[2])),ZERO)

    def test_reflection_is_not_finite_jet_local_off_real_slice(self):
        z0=1+I
        for N in range(5):
            f=(z-z0)**(N+1)
            for k in range(N+1):
                self.assertEqual(s.diff(f,z,k).subs(z,z0),0)
            mirrored=s.conjugate(f.subs(z,s.conjugate(z0)))
            self.assertNotEqual(s.simplify(mirrored),0)

    def test_reflected_operation_is_local_on_real_slice(self):
        A=s.Matrix([[1+I*z,z**2],[z,2]])
        self.assertEqual(s.simplify(reflected(A).subs(z,t)-
                       s.conjugate(A.subs(z,t)).T),ZERO)

    def test_pointwise_antihermitian_holomorphy_freezes_linear_time_mode(self):
        a,b=s.symbols("a b",real=True)
        E=I*(a+b*z)*ONE
        ordinary=s.simplify(E.subs(z,t+I*psi)+
                       s.conjugate(E.subs(z,t+I*psi)).T)
        self.assertEqual(s.simplify(ordinary+2*b*psi*ONE),ZERO)
        self.assertEqual(s.diff(ordinary[0,0],psi),-2*b)

    def test_smooth_scalar_fiber_can_be_nonholomorphic_and_local(self):
        A=I*(t+psi**2)*ONE
        self.assertEqual(A+s.conjugate(A).T,ZERO)
        self.assertNotEqual(s.diff(A,psi),I*s.diff(A,t))
        self.assertEqual(s.diff(A,psi),2*I*psi*ONE)

    def test_global_imaginary_circle_w_holonomy(self):
        R=s.symbols("R",positive=True,real=True)
        for n in (1,2,3):
            H=s.diag(s.exp(n*z/R),1)
            self.assertEqual(s.simplify(reflected(H)-H),ZERO)
            self.assertEqual(s.simplify(w_from_h(H)+s.Rational(n,2)/R),0)
            holonomy=s.exp(-s.pi*I*n)
            self.assertEqual(s.simplify(holonomy-(-1)**n),0)
            self.assertEqual(s.simplify(H.subs(z,z+2*s.pi*I*R)-H),ZERO)

    def test_square_root_monodromy_for_odd_winding(self):
        R=s.symbols("R",positive=True,real=True)
        H=s.diag(s.exp(z/R),1)
        hhat=s.diag(s.exp(z/(2*R)),s.exp(-z/(2*R)))
        self.assertEqual(s.simplify(hhat.det()),1)
        self.assertEqual(s.simplify(hhat.subs(z,z+2*s.pi*I*R)+hhat),ZERO)
        self.assertEqual(s.simplify(H.subs(z,z+2*s.pi*I*R)-H),ZERO)

    def test_central_complex_phase_is_still_not_gauge(self):
        A=I*ONE
        sharp=lambda M:s.trace(M)*ONE-M
        metric=lambda M:s.simplify(sharp(M)*M)
        self.assertEqual(s.simplify(metric(I*A)+metric(A)),ZERO)
        self.assertNotEqual(metric(I*A),metric(A))
        self.assertNotEqual(pminus(I*ONE),I*pminus(ONE))

if __name__=="__main__":
    unittest.main()
