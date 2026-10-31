# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact Lorentz-equivariant real-linear full-Theta graded jet.

A candidate auxiliary tensor K acts on the already existing anti-Hermitian
sector of ONE biquaternion. This is NOT a complex-linear canonical D,
fundamental action, or central-phase U(1) symmetry selector.
"""
import unittest
import sympy as s

I=s.I
ONE=s.eye(2)
ZERO=s.zeros(2)
P=(s.Matrix([[0,1],[1,0]]),
   s.Matrix([[0,-I],[I,0]]),
   s.diag(1,-1))
ETA=s.diag(-1,1,1,1)

def adj(A):
    return A.conjugate().T

def plus(A):
    return (A+adj(A))/2

def minus(A):
    return (A-adj(A))/2

def sharp(A):
    return s.trace(A)*ONE-A

def auxiliary(A,K):
    X=minus(A)
    return s.simplify(K*X+X*adj(K))

def density_w(H,u):
    return -s.diff(s.det(H),u)/(2*s.det(H))

class GradedFullThetaJet(unittest.TestCase):
    def setUp(self):
        self.H=2*ONE+P[2]
        self.X=I*(3*ONE+P[0])
        self.Theta=self.H+self.X
        self.K=P[2]+I*P[0]

    def test_decomposition_is_original_one_field(self):
        self.assertEqual(plus(self.Theta),self.H)
        self.assertEqual(minus(self.Theta),self.X)
        self.assertEqual(self.H.det(),3)

    def test_auxiliary_does_not_touch_hermitian_sector(self):
        for H in (ONE,self.H,P[0],P[1],P[2]):
            self.assertEqual(auxiliary(H,self.K),ZERO)

    def test_auxiliary_is_antihermitian(self):
        M=auxiliary(self.Theta,self.K)
        self.assertEqual(s.simplify(M+adj(M)),ZERO)
        self.assertNotEqual(M,ZERO)

    def test_real_linearity(self):
        a,b=s.symbols('a b',real=True)
        M=I*P[0]+P[1]
        N=3*ONE+I*P[2]
        self.assertEqual(s.simplify(auxiliary(a*M+b*N,self.K)
                            -a*auxiliary(M,self.K)-b*auxiliary(N,self.K)),ZERO)

    def test_lorentz_congruence_equivariance_for_boost(self):
        S=s.diag(2,s.Rational(1,2))
        KP=S*self.K*S.inv()
        T=S*self.Theta*adj(S)
        self.assertEqual(s.simplify(auxiliary(T,KP)
                                  -S*auxiliary(self.Theta,self.K)*adj(S)),ZERO)

    def test_local_lorentz_connection_transformation(self):
        t,u=s.symbols('t u',real=True)
        S=s.diag(s.exp(u*t),s.exp(-u*t))
        Omega=-s.diff(S,t)*S.inv()
        Theta=self.H+I*(t*ONE+P[0])
        ThetaPrime=S*Theta*adj(S)
        KPrime=S*P[2]*S.inv()
        lhs=s.diff(ThetaPrime,t)+Omega*ThetaPrime
        lhs+=ThetaPrime*adj(Omega)+auxiliary(ThetaPrime,KPrime)
        rhs=S*(s.diff(Theta,t)+auxiliary(Theta,P[2]))*adj(S)
        self.assertEqual(s.simplify(lhs-rhs),ZERO)
        self.assertEqual(s.simplify(Omega.trace()),0)

    def test_hermitian_reality_unchanged_by_K(self):
        t=s.symbols('t',real=True)
        Theta=self.H+I*(t*ONE+P[0])
        self.assertEqual(plus(s.diff(Theta,t)+auxiliary(Theta,self.K)),ZERO)

    def test_derived_relative_w_preserves_local_real_scale(self):
        t=s.symbols('t',real=True)
        eps=s.Function('eps',real=True)(t)
        Theta=self.H+I*(t*ONE+P[0])
        scaled=s.exp(eps)*Theta
        W=density_w(plus(scaled),t)
        self.assertEqual(s.simplify(W+s.diff(eps,t)),0)
        lhs=s.diff(scaled,t)+W*scaled+auxiliary(scaled,P[2])
        rhs=s.exp(eps)*(s.diff(Theta,t)+auxiliary(Theta,P[2]))
        self.assertEqual(s.simplify(lhs-rhs),ZERO)

    def test_local_boost_preserves_H_parallelism(self):
        t,u=s.symbols('t u',real=True)
        S=s.diag(s.exp(u*t),s.exp(-u*t))
        Omega=-s.diff(S,t)*S.inv()
        HP=S*self.H*adj(S)
        self.assertEqual(s.simplify(s.diff(HP,t)+Omega*HP+HP*adj(Omega)),ZERO)
        self.assertEqual(s.simplify(density_w(HP,t)),0)

    def test_local_boost_preserves_canonical_sharp_metric(self):
        S=s.diag(2,s.Rational(1,2))
        A=I*ONE+I*P[0]
        B=2*I*P[1]+I*P[2]
        Ap=S*A*adj(S)
        Bp=S*B*adj(S)
        inner=lambda X,Y:s.simplify((sharp(X)*Y+sharp(Y)*X)/2)
        self.assertEqual(s.simplify(inner(Ap,Bp)-inner(A,B)),ZERO)

    def test_exact_orthogonal_auxiliary_response_rank_three(self):
        Kset=[P[0],P[1],P[2],I*P[0],I*P[1],I*P[2]]
        X=I*ONE
        cols=[]
        for K in Kset:
            Q=auxiliary(X,K)
            cols.append(s.Matrix([s.trace(Q)/(2*I)]+
                                   [s.trace(Q*R)/(2*I) for R in P]))
        M=s.Matrix.hstack(*cols)
        self.assertEqual(M.rank(),3)
        for j in (3,4,5):
            self.assertEqual(M[:,j],s.zeros(4,1))

    def test_full_spacetime_auxiliary_image_rank_twelve(self):
        Kset=[P[0],P[1],P[2],I*P[0],I*P[1],I*P[2]]
        col=[]
        for mu in range(4):
            for K in Kset:
                Q=auxiliary(I*ONE,K)
                V=s.Matrix([s.trace(Q)/(2*I)]+
                           [s.trace(Q*R)/(2*I) for R in P])
                A=s.zeros(4,4)
                A[mu,:]=V.T
                col.append(A.reshape(16,1))
        self.assertEqual(s.Matrix.hstack(*col).rank(),12)

    def test_regular_canonical_sharp_metric_with_nonzero_K(self):
        t,x,y,z,k=s.symbols('t x y z k',real=True)
        coord=(t,x,y,z)
        Theta=ONE+I*(t*ONE+x*P[0]+y*P[1]+z*P[2])
        Ks=(ZERO,k*P[2],ZERO,ZERO)
        E=[s.simplify(s.diff(Theta,coord[m])+auxiliary(Theta,Ks[m]))
           for m in range(4)]
        for em in E:
            self.assertEqual(s.simplify(em+adj(em)),ZERO)
        frame=s.Matrix(4,4,lambda m,n:s.simplify(
            s.trace(E[m])/(2*I) if n==0
            else s.trace(E[m]*P[n-1])/(2*I)))
        self.assertEqual(s.factor(frame.det()),1)
        metric=s.simplify(frame*ETA*frame.T)
        for m in range(4):
            for n in range(4):
                bilin=s.simplify((sharp(E[m])*E[n]+sharp(E[n])*E[m])/2)
                self.assertEqual(s.simplify(bilin-metric[m,n]*ONE),ZERO)

    def test_complex_linear_map_vanishing_on_H_must_be_zero(self):
        # Hermitian matrices constitute a complex basis of Mat2(C).
        C=s.Matrix.hstack(*[A.reshape(4,1) for A in [ONE,*P]])
        self.assertNotEqual(C.det(),0)

    def test_auxiliary_is_not_complex_linear(self):
        self.assertEqual(auxiliary(self.H,self.K),ZERO)
        self.assertNotEqual(auxiliary(I*self.H,self.K),ZERO)
        self.assertNotEqual(auxiliary(I*self.H,self.K),
                            I*auxiliary(self.H,self.K))

    def test_central_phase_is_not_auxiliary_equivariant(self):
        self.assertEqual(auxiliary(self.H,self.K),ZERO)
        self.assertNotEqual(auxiliary(I*self.H,self.K),ZERO)

    def test_common_phase_cannot_preserve_real_sharp_metric(self):
        A=I*ONE
        z=I
        metric=lambda M:s.simplify(sharp(M)*M)
        self.assertEqual(s.simplify(metric(z*A)-z*z*metric(A)),ZERO)
        self.assertNotEqual(metric(z*A),metric(A))

    def test_joint_reality_does_not_prove_action_selection(self):
        # The K term may be nonzero while Hermitian-sector constraint stays 0.
        K=P[2]
        t=s.symbols('t',real=True)
        T=ONE+I*(t*ONE+P[0])
        self.assertEqual(plus(s.diff(T,t)+auxiliary(T,K)),ZERO)
        self.assertNotEqual(auxiliary(T,K),ZERO)

if __name__=='__main__':
    unittest.main()
