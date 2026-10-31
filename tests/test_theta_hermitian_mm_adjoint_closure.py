# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Conditional split-jet/MM adjoint injectivity with w from the SAME Theta.

Local Lorentz-real / positive Hermitian chart, physical spin Ω and algebraic
split-jet K distinct. This is not microscopic UBT action selection.
"""
import itertools
import unittest
import sympy as sp

eta=sp.diag(-1,1,1,1)
I2=sp.eye(2)

def generator(a,b):
    mat=sp.zeros(4)
    mat[a,b]=eta[a,a]
    mat[b,a]=-eta[b,b]
    return mat

def normal_source_matrices(X,e):
    """For E^mu_a=f^mu X_a: transverse X adjoint and Weyl trace test."""
    f=sp.Matrix(sp.symbols('f0:4'))
    low=eta*X
    dual=eta*e.T*f
    wedge=sp.Matrix([dual[a]*low[b]-dual[b]*low[a]
                      for a,b in itertools.combinations(range(4),2)])
    W=wedge.jacobian(f)
    scale=(e*low).T
    return W,scale

class HermitianMMAdjointClosure(unittest.TestCase):
    def test_lorentz_pair_preserves_eta(self):
        for a,b in itertools.combinations(range(4),2):
            G=generator(a,b)
            self.assertEqual(G.T*eta+eta*G,sp.zeros(4))

    def test_splitjet_lorentz_map_rank_twelve(self):
        for X in (sp.Matrix([3,1,0,0]),sp.Matrix([1,3,0,0])):
            columns=[]
            for mu in range(4):
                for a,b in itertools.combinations(range(4),2):
                    de=sp.zeros(4,4)
                    de[mu,:]=(generator(a,b)*X).T
                    columns.append(de.reshape(16,1))
            J=sp.Matrix.hstack(*columns)
            self.assertEqual(J.rank(),12)
            self.assertEqual(len(J.T.nullspace()),4)

    def test_K_annihilator_is_normal(self):
        X=sp.Matrix([3,1,0,0])
        Xlow=eta*X
        for mu in range(4):
            for a,b in itertools.combinations(range(4),2):
                self.assertEqual((Xlow.T*generator(a,b)*X)[0],0)

    def test_X_equation_transverse_rank_three(self):
        X=sp.Matrix([3,1,0,0])
        e=sp.eye(4)
        W,scl=normal_source_matrices(X,e)
        self.assertEqual(W.rank(),3)
        self.assertEqual(len(W.nullspace()),1)
        self.assertEqual((W*e.inv().T*X),sp.zeros(6,1))

    def test_X_and_scale_remove_normal_source_in_general_frame(self):
        e=sp.Matrix([[1,1,0,0],[0,2,1,0],[0,0,1,1],[0,0,0,1]])
        for X in (sp.Matrix([3,1,0,0]),sp.Matrix([1,3,0,0])):
            W,scl=normal_source_matrices(X,e)
            self.assertEqual(W.rank(),3)
            self.assertEqual(W.col_join(scl).rank(),4)
            self.assertEqual((scl*e.inv().T*X)[0],(X.T*eta*X)[0])

    def test_null_carrier_is_a_real_boundary_of_the_theorem(self):
        X=sp.Matrix([1,1,0,0]);e=sp.eye(4)
        W,scl=normal_source_matrices(X,e)
        self.assertEqual(W.col_join(scl).rank(),3)

    def test_w_is_fixed_by_existing_H_trace(self):
        t,u,v=sp.symbols('t u v',real=True)
        H=sp.diag(sp.exp(u*t),sp.exp(v*t))
        w=-sp.diff(H.det(),t)/(2*H.det())
        self.assertEqual(sp.simplify(w+(u+v)/2),0)
        omega=sp.diag(-(u-v)/4,(u-v)/4)
        C=sp.diff(H,t)+omega*H+H*omega.T+w*H
        self.assertEqual(sp.simplify(C),sp.zeros(2))

    def test_residual_H_constraint_stays_homogeneous_under_scale(self):
        t,u,v=sp.symbols('t u v',real=True)
        eps=sp.Function('eps')(t)
        H=sp.diag(sp.exp(u*t),sp.exp(v*t))
        Omega=sp.diag(-(u-v)/4,(u-v)/4)
        w=-(u+v)/2
        HH=sp.exp(eps)*H
        ww=w-sp.diff(eps,t)
        C=sp.diff(HH,t)+Omega*HH+HH*Omega.T+ww*HH
        self.assertEqual(sp.simplify(C),sp.zeros(2))

    def test_joint_scaling_X_H_produces_exact_Weyl_tetrad_variation(self):
        t=sp.symbols('t',real=True)
        eps=sp.Function('eps')(t)
        X=sp.Matrix([sp.Function('X%d'%i)(t) for i in range(4)])
        A=generator(0,1)*sp.symbols('a')+generator(2,3)*sp.symbols('b')
        H=sp.eye(2)
        ww=sp.Integer(0)
        e=sp.diff(X,t)+A*X+ww*X
        Xt=sp.exp(eps)*X
        Ht=sp.exp(eps)*H
        wt=-sp.diff(Ht.det(),t)/(2*Ht.det())
        ep=sp.diff(Xt,t)+A*Xt+wt*Xt
        self.assertEqual(sp.simplify(ep-sp.exp(eps)*e),sp.zeros(4,1))

    def test_previous_transport_source_now_detected_by_H(self):
        t,x,y,z=sp.symbols('t x y z',real=True)
        c=(t,x,y,z)
        X=sp.Matrix(c)
        q=(X.T*eta*X)[0]
        rho=-q
        h=rho**(-sp.Rational(5,2))
        F=sp.Matrix(4,4,lambda mu,a:h*X[mu]*(eta*X)[a])
        for a in range(4):
            self.assertEqual(sp.simplify(sum(sp.diff(F[mu,a],c[mu]) for mu in range(4))),0)
        div=sp.simplify(sum(sp.diff(h*X[mu]*q,c[mu]) for mu in range(4)))
        self.assertEqual(sp.simplify(div-h*q),0)
        self.assertNotEqual(div.subs({t:2,x:0,y:0,z:0}),0)

    def test_weyl_tangent_not_gauge_of_MM_gravity(self):
        X=sp.Matrix([3,1,0,0]);e=sp.eye(4)
        V=e.inv().T*X
        f=V
        E=f*(eta*X).T
        self.assertEqual(sp.trace(E.T*e),(X.T*eta*X)[0])
        self.assertNotEqual(sp.trace(E.T*e),0)

    def test_same_spin_connection_H_reality_blocks_boost_splitjet(self):
        sigma=(sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.diag(1,-1))
        uu=sp.symbols('u0:3',real=True)
        vv=sp.symbols('v0:3',real=True)
        K=sum(((uu[j]+sp.I*vv[j])*sigma[j] for j in range(3)),sp.zeros(2))
        CH=sp.simplify(K+K.conjugate().T)
        EX=sp.simplify(K*(sp.I*I2)+(sp.I*I2)*K.conjugate().T)
        self.assertEqual(sp.simplify(EX-sp.I*CH),sp.zeros(2))
        for j in range(3):
            self.assertEqual(sp.diff(CH,vv[j]),sp.zeros(2))
            self.assertNotEqual(sp.diff(CH,uu[j]),sp.zeros(2))
        self.assertEqual(sp.simplify(EX.subs(dict.fromkeys(uu,0))),sp.zeros(2))

    def test_boost_versus_rotation_failure_is_explicit(self):
        sig=sp.Matrix([[0,1],[1,0]])
        for K,visible in ((sig,True),(sp.I*sig,False)):
            dH=K+K.conjugate().T
            dX=K*(sp.I*I2)+(sp.I*I2)*K.conjugate().T
            self.assertEqual(dX,sp.I*dH)
            self.assertEqual(dX!=sp.zeros(2),visible)
            self.assertEqual(dH!=sp.zeros(2),visible)

    def test_H_only_splitjet_projector_is_not_complex_linear(self):
        Pminus=lambda T:(T-T.conjugate().T)/2
        Theta=I2+sp.I*I2
        self.assertNotEqual(Pminus(sp.I*Theta),sp.I*Pminus(Theta))

    def test_pointwise_Kplus_Weyl_is_not_full_tetrad_right_inverse(self):
        X=sp.Matrix([3,1,0,0]);col=[]
        for mu in range(4):
            for a,b in itertools.combinations(range(4),2):
                de=sp.zeros(4,4)
                de[mu,:]=(generator(a,b)*X).T
                col.append(de.reshape(16,1))
        col.append(sp.eye(4).reshape(16,1))
        self.assertEqual(sp.Matrix.hstack(*col).rank(),13)

if __name__=='__main__': unittest.main()
