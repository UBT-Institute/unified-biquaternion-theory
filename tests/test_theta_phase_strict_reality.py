# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""G1 restricted strict-tetrad rank/no-go for phase-only and full projectors.

Exact claims refer to direct unprojected Hermitian jets on the declared
eight-real-component Mat(2,C) carrier, NOT all possible UBT tetrads.
"""
import unittest
import sympy as s

B=s.diag(1,-1,-1,-1,1,-1,-1,-1)
J=s.zeros(8)
J[:4,4:]=-s.eye(4)
J[4:,:4]=s.eye(4)
E=s.eye(8)[:,:4]

def pair(u,v):
    return s.simplify((u.T*B*v)[0])

def phase_projector(q):
    return s.eye(8)-(J*q)*(J*q).T*B/pair(q,q)

def full_projector(q):
    return s.eye(8)-(q*q.T*B+(J*q)*(J*q).T*B)/pair(q,q)

class TestPhaseOnlyStrictReality(unittest.TestCase):
    def test_phase_projection_orthogonality(self):
        q=s.Matrix([2,0,0,0,0,1,0,0])
        P=phase_projector(q)
        self.assertEqual(s.simplify(P*P-P),s.zeros(8))
        self.assertEqual(s.simplify((J*q).T*B*P),s.zeros(1,8))

    def test_real_slice_phase_only_rank_three_complex_field(self):
        q=s.Matrix([2,0,0,0,0,1,0,0])
        constraint=(J*q).T*B*E
        self.assertEqual(constraint.rank(),1)
        self.assertEqual(len(constraint.nullspace()),3)

    def test_real_slice_full_rank_two_complex_field(self):
        q=s.Matrix([2,0,0,0,0,1,0,0])
        constraints=s.Matrix.vstack(q.T*B*E,(J*q).T*B*E)
        self.assertEqual(constraints.rank(),2)
        self.assertEqual(len(constraints.nullspace()),2)

    def test_negative_norm_escaping_gram_still_not_direct_tetrad(self):
        q=s.Matrix([0,1,0,0,0,0,0,0])
        self.assertEqual(pair(q,q),-1)
        constraints=s.Matrix.vstack(q.T*B*E,(J*q).T*B*E)
        self.assertEqual(constraints.rank(),1)
        self.assertEqual(len(constraints.nullspace()),3)
        P=full_projector(q)
        jet=s.Matrix.hstack(*[s.eye(8)[:,i] for i in (0,2,3,6)])
        self.assertEqual(jet.T*P.T*B*P*jet,s.diag(1,-1,-1,-1))
        self.assertNotEqual((s.eye(8)-E*E.T)*P*jet,s.zeros(8,4))

    def test_pure_hermitian_phase_jet_can_rank_four(self):
        q=s.Matrix([1,0,0,0,0,0,0,0])
        self.assertEqual(phase_projector(q)*E,E)
        self.assertEqual(E.T*B*E,s.diag(1,-1,-1,-1))

    def test_curved_trial_phase_projection_is_lorentz_at_point(self):
        t,x,y,z,k=s.symbols("t x y z k",real=True)
        coords=(t,x,y,z)
        sig=(s.eye(2),s.Matrix([[0,1],[1,0]]),
             s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1))
        Q=(t+2)*sig[0]+x*sig[1]+y*sig[2]+z*sig[3]+s.I*k*t*x*sig[1]
        def adj(m):
            return s.Matrix([[m[1,1],-m[0,1]],[-m[1,0],m[0,0]]])
        def bilin(m,n):
            return s.simplify(s.re(s.trace(adj(m)*n.conjugate().T))/2)
        N=s.factor(bilin(Q,Q))
        js=[s.factor(bilin(s.I*Q,s.diff(Q,w))/N) for w in coords]
        self.assertEqual(s.simplify(js[0]+k*x**2/N),0)
        self.assertEqual(js[1:],[0,0,0])
        dQ=[s.diff(Q,w)-s.I*js[i]*Q for i,w in enumerate(coords)]
        g=s.Matrix(4,4,lambda i,j:bilin(dQ[i],dQ[j]))
        at={t:1,x:0,y:0,z:0}
        self.assertEqual(s.simplify(g.subs(at)),s.diag(1,-1-k*k,-1,-1))
        g0=s.diag(1,-1,-1,-1)-k*k*s.Matrix([x,t,0,0])*s.Matrix([[x,t,0,0]])
        self.assertEqual(s.simplify(g-(g0-s.diag(k*k*x**4/N,0,0,0))),s.zeros(4))
        mixed=s.diff(g[0,1],t,x)
        Rtxtx=s.simplify((2*mixed-s.diff(g[1,1],t,2)-s.diff(g[0,0],x,2))/2)
        self.assertEqual(s.simplify(Rtxtx.subs({t:0,x:0,y:0,z:0})),k*k)

    def test_curved_example_traceless_antihermitian_cannot_be_removed(self):
        k,gamma,u,r=s.symbols("k gamma u r",real=True)
        a,b,c,d=s.symbols("a b c d",complex=True)
        L=s.Matrix([[a,b],[c,d]])
        sigma=s.Matrix([[0,1],[1,0]])
        D=(1+s.I*k)*sigma+r*(L+L.conjugate().T)+r*u*s.eye(2)+s.I*r*gamma*s.eye(2)
        anti=s.simplify((D-D.conjugate().T)/2)
        traceless=s.simplify(anti-s.trace(anti)*s.eye(2)/2)
        self.assertEqual(traceless,s.I*k*sigma)

    def test_full_projection_for_any_nonzero_hermitian_q_has_rank_three(self):
        for idx in range(4):
            q=E[:,idx]
            c=s.Matrix.vstack(q.T*B*E,(J*q).T*B*E)
            self.assertEqual(c.rank(),1)
            self.assertEqual(len(c.nullspace()),3)

if __name__=="__main__":
    unittest.main()
