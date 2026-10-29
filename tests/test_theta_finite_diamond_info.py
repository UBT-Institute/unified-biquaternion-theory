# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact finite causal-diamond / biquaternion invariant information control.

Conditional toy model only: the causal poset and measurement map are inputs,
not derived from Theta, and no microscopic physical Hamiltonian is selected.
"""
import itertools
import unittest
from fractions import Fraction
import sympy as s

SIGNS=s.diag(1,-1,-1,-1,1,-1,-1,-1)

def h(q):
    return s.expand(2*(q.T*SIGNS*q)[0])

def probs(binary_p):
    return {0:1-binary_p,1:binary_p}

def prod_state(labels, marg):
    return {bits:s.prod(marg[key][b] for key,b in zip(labels,bits))
            for bits in itertools.product((0,1),repeat=len(labels))}

def marginal(state, locations, keep):
    out={}
    for bits,prob in state.items():
        key=tuple(bits[locations.index(e)] for e in keep)
        out[key]=out.get(key,0)+prob
    return out

def KL(P,Q):
    return s.expand(sum(p*s.log(s.cancel(p/Q[k])) for k,p in P.items() if p!=0))

class TestThetaFiniteDiamond(unittest.TestCase):
    def test_congruence_invariance_of_reference_outcomes(self):
        R=s.symbols('R',real=True,positive=True)
        A=R*s.eye(2)
        S=s.diag(2,s.Rational(1,2))
        adj=lambda X:s.Matrix([[X[1,1],-X[0,1]],[-X[1,0],X[0,0]]])
        HH=lambda X:s.simplify(s.trace(adj(X)*X.conjugate().T))
        self.assertEqual(HH(A),2*R**2)
        self.assertEqual(HH(S*A*S.conjugate().T),HH(A))
        self.assertEqual(HH(s.I*A),HH(A))
        self.assertEqual(
            s.simplify(HH(A)-h(s.Matrix([R,0,0,0,0,0,0,0]))),0)

    def test_scalar_reference_state_derived_from_theta(self):
        beta=s.log(2)/2
        for n,p in [(1,s.Rational(2,3)),(2,s.Rational(16,17)),
                    (3,s.Rational(512,513))]:
            q=s.Matrix([n,0,0,0,0,0,0,0])
            N=h(q)
            self.assertEqual(N,2*n*n)
            self.assertEqual(s.simplify(
                1/(1+s.exp(-beta*N))-p),0)

    def test_exact_overlap_consistency_and_no_double_counting(self):
        p={"a":s.Rational(2,3),"o":s.Rational(16,17),
           "b":s.Rational(512,513)}
        r={"a":s.Rational(1,3),"o":s.Rational(1,2),
           "b":s.Rational(2,3)}
        P={k:probs(v) for k,v in p.items()}
        R={k:probs(v) for k,v in r.items()}
        gl=prod_state(('a','o','b'),P)
        gr=prod_state(('a','o','b'),R)
        for keep in [('a','o'),('o','b'),('o',)]:
            self.assertEqual(
                marginal(gl,('a','o','b'),keep),prod_state(keep,P))
            self.assertEqual(
                marginal(gr,('a','o','b'),keep),prod_state(keep,R))
        lg=marginal(gl,('a','o','b'),('a','o'))
        lr=marginal(gr,('a','o','b'),('a','o'))
        rg=marginal(gl,('a','o','b'),('o','b'))
        rr=marginal(gr,('a','o','b'),('o','b'))
        og=marginal(gl,('a','o','b'),('o',))
        orr=marginal(gr,('a','o','b'),('o',))
        diff=s.simplify(s.expand_log(
            KL(lr,lg)+KL(rr,rg)-KL(orr,og)-KL(gr,gl),
            force=True))
        self.assertEqual(diff,0)
        self.assertGreater(float(KL(orr,og)),0)

    def test_undetected_endpoint_correlation_even_with_full_diamond_marginals(self):
        # All events have nonzero timelike trial field Theta=I, N=2.
        # With beta=log(2)/2 every Bernoulli event has p=2/3.
        po=s.Rational(2,3)
        def global_state(coupling):
            m=probs(po)
            return {(a,o,b):m[o]*(m[a]*m[b]+coupling*(-1)**(a+b))
                    for a,o,b in itertools.product((0,1),repeat=3)}
        independent=global_state(0)
        corr=global_state(s.Rational(1,18))
        self.assertEqual(sum(corr.values()),1)
        self.assertTrue(all(v>0 for v in corr.values()))
        for keep in [('a','o'),('o','b')]:
            self.assertEqual(
                marginal(corr,('a','o','b'),keep),
                marginal(independent,('a','o','b'),keep))
        self.assertNotEqual(corr,independent)
        joint_kl=KL(corr,independent)
        expected=(s.Rational(1,6)*s.log(s.Rational(3,2))
                  +s.Rational(1,3)*s.log(s.Rational(3,4))
                  +s.Rational(1,2)*s.log(s.Rational(9,8)))
        self.assertEqual(s.simplify(joint_kl-expected),0)
        self.assertGreater(float(joint_kl),0)

    def test_information_gradient_and_rank_one_fisher_hessian(self):
        beta,N,r=s.symbols('beta N r',positive=True)
        p=1/(1+s.exp(-beta*N))
        # D_Bern(r||p(N))=constant(r)+log(1+exp(beta*N))-r*beta*N.
        D=s.log(1+s.exp(beta*N))-r*beta*N
        self.assertEqual(
            s.simplify(s.diff(D,N)-beta*(p-r)),0)
        self.assertEqual(
            s.simplify(s.diff(D,N,2)-beta**2*p*(1-p)),0)
        q=s.Matrix([1,0,0,0,0,0,0,0])
        qq=s.symbols('q0:8')
        grad=s.Matrix([s.diff(h(s.Matrix(qq)),v) for v in qq])
        grad0=grad.subs(dict(zip(qq,list(q))))
        self.assertEqual(grad0,s.Matrix([4,0,0,0,0,0,0,0]))
        fisher=grad0*grad0.T # positive scalar beta²*p*(1-p)
        self.assertEqual(fisher.rank(),1)
        self.assertEqual(len(fisher.nullspace()),7)

    def test_information_equilibrium_does_not_select_positive_reduced_hamiltonian(self):
        n,pi=s.symbols('n pi',real=True)
        n0=s.Integer(2)
        ham=lambda lam:s.Rational(1,2)*pi**2+lam*(n-n0)**2
        for lam in (s.Integer(1),s.Integer(3)):
            Hamilton=ham(lam)
            self.assertEqual(s.diff(Hamilton,n).subs({n:n0,pi:0}),0)
            self.assertEqual(s.diff(Hamilton,pi).subs({n:n0,pi:0}),0)
            self.assertEqual(s.diff(Hamilton,n,2),2*lam)
        self.assertNotEqual(
            s.diff(ham(1),n,2),s.diff(ham(3),n,2))
        # n and pi are a hypothetical positive scalar reduced phase space.
        # Its canonical bracket is NOT derived from UBT.

    def test_stationary_relative_entropy_monotonicity_leaves_markov_rate_free(self):
        p=s.Rational(2,3)
        stationary=s.Matrix([[1-p,p]])
        def kernel(gamma):
            return s.Matrix([
                [1-gamma*p,gamma*p],
                [gamma*(1-p),1-gamma*(1-p)]])
        fast=kernel(s.Rational(1,2))
        slow=kernel(s.Rational(1,4))
        for rate,T in ((s.Rational(1,2),fast),
                       (s.Rational(1,4),slow)):
            self.assertEqual(stationary*T,stationary)
            self.assertEqual(T*s.ones(2,1),s.ones(2,1))
            self.assertEqual(T.det(),1-rate)
            d0=s.log(1/(1-p))
            q=(s.Matrix([[1,0]])*T)[0,1]
            d1=q*s.log(q/p)+(1-q)*s.log((1-q)/(1-p))
            self.assertLess(float(d1),float(d0))
        self.assertNotEqual(fast,slow)

if __name__=='__main__':
    unittest.main()
