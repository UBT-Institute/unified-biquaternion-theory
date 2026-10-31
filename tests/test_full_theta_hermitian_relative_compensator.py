# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact restricted full-biquaternion Hermitian relative-jet audit.

Theta is ONE Mat2(C) biquaternion, H and X are its existing Hermitian and
anti-Hermitian sectors. The relative central connection is a CANDIDATE
composite law; full UBT action selection and phase covariance are OPEN.
"""
import unittest
import sympy as sp

I=sp.I
P=(sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-I],[I,0]]),sp.diag(1,-1))
J=sp.eye(2)
zero=sp.zeros(2)
t,x,y,z,a,b=sp.symbols('t x y z a b',real=True)
coords=(t,x,y,z)
H=J
X=I*(t*J+x*P[0]+y*P[1]+z*P[2])
Theta=H+X
Omega=(zero,I*a*P[0],I*b*P[1],zero)

def adj(m): return m.conjugate().T
def sharp(m): return sp.trace(m)*J-m
def D(m,k): return sp.diff(m,coords[k])+Omega[k]*m+m*adj(Omega[k])
def relative_w(h):
    det=sp.det(h)
    return [-sp.simplify(sp.diff(det,u)/(2*det)) for u in coords]

w=relative_w(H)
E=tuple(sp.simplify(D(Theta,k)+w[k]*Theta) for k in range(4))
frame=sp.Matrix(4,4,lambda mu,nu:sp.simplify(
    sp.trace(E[mu])/(2*I) if nu==0
    else -sp.trace(E[mu]*P[nu-1])/(2*I)))
eta=sp.diag(-1,1,1,1)
metric=sp.simplify(frame*eta*frame.T)

def curvature_xyxy_at_origin(g):
    """Coordinate R^x_{yxy}, sign R^i_jkl=d_k Gamma^i_lj-d_l Gamma^i_kj+..."""
    G=g[1:4,1:4]
    v=(x,y,z)
    origin={x:0,y:0,z:0}
    def d(i,j,k):return sp.diff(G[i,j],v[k]).subs(origin)
    def dd(i,j,k,l):return sp.diff(G[i,j],v[k],v[l]).subs(origin)
    def ch(i,j,k):return sp.Rational(1,2)*(d(i,k,j)+d(i,j,k)-d(j,k,i))
    def dc(i,j,k,l):
        t1=-sum(d(i,m,l)*(d(m,k,j)+d(m,j,k)-d(j,k,m))
                for m in range(3))
        return sp.Rational(1,2)*(t1+dd(i,k,j,l)+dd(i,j,k,l)-dd(j,k,i,l))
    def R(i,j,k,l):
        return sp.expand(dc(i,l,j,k)-dc(i,k,j,l)
                         +sum(ch(i,k,m)*ch(m,l,j)
                              -ch(i,l,m)*ch(m,k,j) for m in range(3)))
    return sp.factor(R(0,1,0,1))

class FullThetaHermitianCompensator(unittest.TestCase):
    def test_same_original_biquaternion_two_real_sectors(self):
        self.assertEqual((Theta+adj(Theta))/2,H)
        self.assertEqual((Theta-adj(Theta))/2,X)
        self.assertEqual(sp.det(H),1)

    def test_h_parallel_and_e_antihermitian(self):
        self.assertEqual(w,[0]*4)
        for k in range(4):
            self.assertEqual(D(H,k)+w[k]*H,zero)
            self.assertEqual(E[k]+adj(E[k]),zero)

    def test_sharp_distinct_from_dagger(self):
        self.assertEqual(sharp(I*J),I*J)
        self.assertEqual(adj(I*J),-I*J)

    def test_full_canonical_sharp_metric_no_projection(self):
        for mu in range(4):
            for nu in range(4):
                L=sp.simplify((sharp(E[mu])*E[nu]+sharp(E[nu])*E[mu])/2)
                self.assertEqual(sp.simplify(L-metric[mu,nu]*J),zero)

    def test_full_block_clifford_lift_preserves_metric(self):
        def gamma(Q):
            return sp.BlockMatrix([[zero,Q],[sharp(Q),zero]]).as_explicit()
        G=[gamma(Q) for Q in E]
        for mu in range(4):
            for nu in range(4):
                anticommutator=G[mu]*G[nu]+G[nu]*G[mu]
                self.assertEqual(
                    sp.simplify(anticommutator-2*metric[mu,nu]*sp.eye(4)),
                    sp.zeros(4))

    def test_real_regular_curved_frame(self):
        self.assertEqual(sp.factor(frame.det()),-1-4*a*b*z*z)
        self.assertEqual(frame.subs({x:0,y:0,z:0}),sp.diag(1,-1,-1,-1))
        self.assertEqual(metric.subs({x:0,y:0,z:0}),eta)

    def test_nonzero_two_sided_spin_curvature(self):
        F=Omega[1]*Omega[2]-Omega[2]*Omega[1]
        self.assertEqual(sp.simplify(F+2*I*a*b*P[2]),zero)
        self.assertNotEqual(F.subs({a:1,b:2}),zero)

    def test_nonflat_physical_metric_riemann(self):
        self.assertEqual(curvature_xyxy_at_origin(metric),-12*a*b)
        self.assertEqual(curvature_xyxy_at_origin(metric).subs({a:1,b:2}),-24)

    def test_phi_comes_from_old_field_not_new_scalar(self):
        eps=sp.symbols('eps',real=True)
        hp=(1+eps)*H
        phi=-sp.log(sp.det(hp))/2
        self.assertEqual(sp.diff(phi,eps).subs(eps,0),-1)
        self.assertEqual(sp.expand(sp.det(hp)-(1+eps)**2),0)

    def test_local_scale_derivative_cancels(self):
        lam=sp.Function('lam')(t)
        theta=lam*Theta
        hh=lam*H
        wc=-sp.diff(sp.det(hh),t)/(2*sp.det(hh))
        self.assertEqual(sp.simplify(wc+sp.diff(lam,t)/lam),0)
        e0=sp.diff(theta,t)+Omega[0]*theta+theta*adj(Omega[0])+wc*theta
        self.assertEqual(sp.simplify(e0-lam*E[0]),zero)

    def test_local_scale_cancel_all_four_directions(self):
        L=sp.Function('L')(t,x,y,z)
        for k in range(4):
            dL=sp.diff(L,coords[k])
            new=sp.diff(L*Theta,coords[k])+Omega[k]*L*Theta
            new+=L*Theta*adj(Omega[k])-(dL/L)*L*Theta
            self.assertEqual(sp.simplify(new-L*E[k]),zero)

    def test_normal_euler_pairing_nonzero(self):
        pt={t:2,x:0,y:0,z:0,a:1,b:2}
        Xa=sp.Matrix([t,-x,-y,-z])
        V=frame.inv().T*Xa
        q=(Xa.T*eta*Xa)[0]
        self.assertEqual(q.subs(pt),-4)
        self.assertEqual(sp.simplify((V.T*frame*eta*Xa)[0].subs(pt)),q.subs(pt))

    def test_sl2c_constant_boost_keeps_det_h(self):
        L=sp.symbols('L',real=True)
        S=sp.diag(sp.exp(L),sp.exp(-L))
        HH=S*H*adj(S)
        self.assertEqual(sp.simplify(HH.det()),1)
        TT=S*Theta*adj(S)
        self.assertEqual(sp.simplify((TT+adj(TT))/2-HH),zero)

    def test_local_lorentz_boost_preserves_parallel_h(self):
        k=sp.symbols('k',real=True)
        S=sp.diag(sp.exp(k*t),sp.exp(-k*t))
        HH=S*H*adj(S)
        Om=-sp.diff(S,t)*S.inv()
        self.assertEqual(sp.simplify(sp.diff(HH,t)+Om*HH+HH*adj(Om)),zero)

    def test_h_reality_forces_unique_relative_center(self):
        u,v,c=sp.symbols('u v c',real=True)
        hh=sp.diag(sp.exp(u*t),sp.exp(v*t))
        om=sp.diag(c,-c)
        ww=sp.symbols('ww',real=True)
        C=sp.diff(hh,t)+om*hh+hh*adj(om)+ww*hh
        self.assertEqual(sp.simplify(sp.trace(hh.inv()*C)),u+v+2*ww)
        residual=sp.simplify(C.subs(ww,-(u+v)/2))
        self.assertEqual(sp.simplify(sp.trace(hh.inv()*residual)),0)
        self.assertNotEqual(residual,zero)

    def test_normalized_h_parallel_equivalence(self):
        u,v,c=sp.symbols('u v c',real=True)
        hh=sp.diag(sp.exp(u*t),sp.exp(v*t))
        om=sp.diag(c,-c)
        droot=sp.exp((u+v)*t/2)
        hhat=hh/droot
        left=sp.diff(hhat,t)+om*hhat+hhat*adj(om)
        right=(sp.diff(hh,t)+om*hh+hh*adj(om)-(u+v)*hh/2)/droot
        self.assertEqual(sp.simplify(left-right),zero)

    def test_trace_free_h_constraint_is_nontrivial(self):
        u=sp.symbols('u',real=True)
        hh=sp.diag(sp.exp(u*x),sp.exp(-u*x))
        self.assertEqual(hh.det(),1)
        self.assertEqual(relative_w(hh),[0]*4)
        self.assertNotEqual(sp.diff(hh,x),zero)

    def test_phase_mixes_h_and_x(self):
        chi=sp.symbols('chi',real=True)
        TT=sp.exp(I*chi)*(J+2*I*J)
        hp=(TT+adj(TT))/2
        self.assertEqual(sp.simplify(sp.diff(hp.det(),chi).subs(chi,0)),-4)

    def test_phase_invariant_full_det_guess_breaks_reality(self):
        tt=sp.symbols('tt',real=True)
        TT=(1+I*tt)*J
        wf=-tt/(1+tt**2)
        dt=sp.diff(TT,tt)+wf*TT
        herm=sp.simplify((dt+adj(dt))/2)
        self.assertEqual(herm,wf*J)
        self.assertNotEqual(herm.subs(tt,1),zero)

    def test_real_slice_stable_under_scale(self):
        L=sp.Function('L')(t,x,y,z)
        for k in range(4):
            CC=sp.diff(L*H,coords[k])+Omega[k]*(L*H)
            CC+=(L*H)*adj(Omega[k])-sp.diff(L,coords[k])*H
            self.assertEqual(sp.simplify(CC),zero)

if __name__=='__main__':
    unittest.main()
