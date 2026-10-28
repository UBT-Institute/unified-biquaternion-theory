# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Restricted Theta invariant/casual-geometry bridge.

Commuting classical gauge-invariant cylinder observables, not a quantum
Haag-Kastler net or selected UBT metric. Exact SymPy algebra only.
"""
import unittest
import sympy as s

u=s.symbols("u0:4",real=True)
v=s.symbols("v0:4",real=True)
coords=u+v
z=[u[i]+s.I*v[i] for i in range(4)]
pauli=(s.eye(2),s.Matrix([[0,1],[1,0]]),
       s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1))
Q=sum((z[i]*pauli[i] for i in range(4)),s.zeros(2))
H=2*(u[0]**2+v[0]**2-sum(u[i]**2+v[i]**2 for i in range(1,4)))
K_re=u[0]**2-v[0]**2-sum(u[i]**2-v[i]**2 for i in range(1,4))
K_im=2*(u[0]*v[0]-sum(u[i]*v[i] for i in range(1,4)))
K=s.expand(K_re**2+K_im**2)
J=s.Matrix([[s.diff(f,c) for c in coords] for f in (H,K)])
def adj(M):
    return s.Matrix([[M[1,1],-M[0,1]],[-M[1,0],M[0,0]]])
def h(M):
    return s.simplify(s.trace(adj(M)*M.conjugate().T))
def k(M):
    return s.simplify(s.expand(M.det()*s.conjugate(M.det())))
def B(A,C):
    return s.simplify(s.re(s.trace(adj(A)*C.conjugate().T))/2)

t,x,y,zsp,alpha=s.symbols("t x y zsp alpha",real=True)
spacetime=(t,x,y,zsp)
X=sum((w*P for w,P in zip(spacetime,pauli)),s.zeros(2))
def metric(Y):
    jets=[s.diff(Y,w) for w in spacetime]
    return s.Matrix(4,4,lambda i,j:B(jets[i],jets[j]))

class TestThetaInvariantCausalBridge(unittest.TestCase):
    def test_two_invariants_match_matrix(self):
        self.assertEqual(s.simplify(H-h(Q)),0)
        self.assertEqual(s.simplify(K-k(Q)),0)
        self.assertEqual(s.simplify(K-(s.re(Q.det())**2+s.im(Q.det())**2)),0)

    def test_constant_lorentz_boost_and_phase_invariance(self):
        S=s.diag(2,s.Rational(1,2))
        for M in (Q,S*Q*S.conjugate().T,s.I*Q):
            self.assertEqual(s.simplify(h(M)-H),0)
            self.assertEqual(s.simplify(k(M)-K),0)

    def test_generic_fisher_rank_two_and_six_null_directions(self):
        point={c:0 for c in coords}
        point[u[0]]=2
        point[u[1]]=1
        point[v[1]]=1
        P=J.subs(point)
        self.assertEqual(H.subs(point),4)
        self.assertEqual(K.subs(point),20)
        self.assertEqual(P.rank(),2)
        F=P.T*s.diag(2,3)*P  # positive measurement weights
        self.assertEqual(F.rank(),2)
        self.assertEqual(len(F.nullspace()),6)

    def test_scalar_reference_branch_has_rank_one(self):
        point={c:(1 if c==u[0] else 0) for c in coords}
        self.assertEqual(J.subs(point).rank(),1)

    def test_identical_local_scalars_but_different_causal_cones(self):
        phase=s.exp(s.I*alpha*t)*X
        self.assertEqual(s.simplify(h(phase)-h(X)),0)
        self.assertEqual(s.simplify(k(phase)-k(X)),0)
        self.assertEqual(metric(X),s.diag(1,-1,-1,-1))
        point={t:1,x:0,y:0,zsp:0}
        self.assertEqual(s.simplify(
            metric(phase).subs(point)-s.diag(1+alpha**2,-1,-1,-1)),
            s.zeros(4))

    def test_curved_theta_null_cone_formula(self):
        kap=s.symbols("kap",real=True)
        gtt=1-kap**2*x**2
        gtx=-kap**2*t*x
        gxx=-1-kap**2*t**2
        A=1+kap**2*(t**2-x**2)
        self.assertEqual(s.simplify(gtx**2-gtt*gxx-A),0)
        for sign in (+1,-1):
            speed=(-kap**2*t*x+sign*s.sqrt(A))/(1+kap**2*t**2)
            self.assertEqual(s.simplify(gxx*speed**2+2*gtx*speed+gtt),0)
        self.assertEqual(s.simplify(
            (s.sqrt(A)/(1+kap**2*t**2)).subs({
                kap:s.Rational(1,2),t:1,x:0})-2/s.sqrt(5)),0)

    def test_sampled_timelike_chain_from_same_nonflat_metric(self):
        kap=s.Rational(1,2)
        Y=(t+2)*pauli[0]+x*pauli[1]+y*pauli[2]+zsp*pauli[3]+s.I*kap*t*x*pauli[1]
        g=metric(Y)
        q=s.Matrix([x,t,0,0])
        self.assertEqual(s.simplify(g-s.diag(1,-1,-1,-1)+kap**2*q*q.T),s.zeros(4))
        for tau in (-s.Rational(1,2),s.Integer(0),s.Rational(1,2)):
            at={t:tau,x:0,y:0,zsp:0}
            self.assertEqual(g[0,0].subs(at),1)
            self.assertGreater(h(Y).subs(at),0)
            self.assertGreater(k(Y).subs(at),0)

if __name__=="__main__":
    unittest.main()
