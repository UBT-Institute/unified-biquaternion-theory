# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact restricted composite Lorentz-connection variation rank.

Fixed non-null Lorentz-real Theta value, regular coframe and the original
metric tangent. The connection is an independent *comparator input*, NOT a
Theta-derived UBT action. The Clifford contraction is frozen-frame only.
"""
import itertools
import unittest
import sympy as s

I=s.I
e2,z2=s.eye(2),s.zeros(2)
pauli=(s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1))
def blk(a,b,c,d): return s.BlockMatrix([[a,b],[c,d]]).as_explicit()
gammas=(blk(z2,e2,-e2,z2),)+tuple(blk(z2,p,p,z2) for p in pauli)
eta=s.diag(-1,1,1,1)
pairs=tuple(itertools.combinations(range(4),2))
dirs=tuple((mu,a,b) for mu in range(4) for a,b in pairs)
sympairs=tuple(itertools.combinations_with_replacement(range(4),2))

def omega_response(mu,a,b,X):
    de=s.zeros(4,4)
    de[mu,a]+=eta[a,a]*X[b]
    de[mu,b]-=eta[b,b]*X[a]
    return de

def metric_response(de,e):
    dg=de*eta*e.T+e*eta*de.T
    return s.Matrix([dg[a,b] for a,b in sympairs])

def matrices(X,e):
    decols=[omega_response(*d,X) for d in dirs]
    J=s.Matrix.hstack(*[s.Matrix(q).reshape(16,1) for q in decols])
    G=s.Matrix.hstack(*[metric_response(q,e) for q in decols])
    return J,G

def minimal_dirac_contraction_matrix():
    return s.Matrix.hstack(*[(gammas[mu]*gammas[a]*gammas[b]/2).reshape(16,1)
                            for mu,a,b in dirs])

class CompositeLorentzVariationRank(unittest.TestCase):
    def test_antisymmetry_forbids_internal_normal_response(self):
        for X in (s.Matrix([2,0,0,0]),s.Matrix([2,1,0,0])):
            for d in dirs:
                self.assertEqual(omega_response(*d,X)*eta*X,s.zeros(4,1))

    def test_connection_to_tetrad_rank_is_twelve(self):
        for X in (s.Matrix([2,0,0,0]),s.Matrix([2,1,0,0])):
            J,_=matrices(X,s.eye(4))
            self.assertEqual(J.rank(),12)
            self.assertEqual(len(J.nullspace()),12)

    def test_connection_to_metric_rank_is_nine(self):
        frames=(s.eye(4),s.Matrix([[1,1,0,0],[0,2,1,0],
                                  [0,0,1,1],[0,0,0,1]]))
        for e in frames:
            for X in (s.Matrix([2,0,0,0]),s.Matrix([2,1,0,0])):
                _,G=matrices(X,e)
                self.assertEqual(G.rank(),9)
                self.assertEqual(len(G.T.nullspace()),1)

    def test_universal_normal_metric_cokernel(self):
        e=s.Matrix([[1,1,0,0],[0,2,1,0],[0,0,1,1],[0,0,0,1]])
        X=s.Matrix([2,1,0,0])
        _,G=matrices(X,e)
        V=e.inv().T*X
        S=s.Matrix([V[a]*V[b]*(1 if a==b else 2) for a,b in sympairs])
        self.assertEqual(S.T*G,s.zeros(1,24))
        self.assertNotEqual(S,s.zeros(10,1))

    def test_relative_real_dilation_restores_full_metric_rank(self):
        e=s.eye(4); X=s.Matrix([2,0,0,0])
        _,G=matrices(X,e)
        dil=[]
        for mu in range(4):
            de=s.zeros(4,4)
            for a in range(4): de[mu,a]=X[a]
            dil.append(metric_response(de,e))
        self.assertEqual(G.row_join(s.Matrix.hstack(*dil)).rank(),10)

    def test_prior_minimal_clifford_visibility_rank_eight(self):
        V=minimal_dirac_contraction_matrix()
        self.assertEqual(V.rank(),8)
        self.assertEqual(len(V.nullspace()),16)

    def test_combined_response_has_eight_dimensional_kernel(self):
        X=s.Matrix([2,0,0,0]);_,G=matrices(X,s.eye(4))
        V=minimal_dirac_contraction_matrix()
        J=G.col_join(V)
        self.assertEqual(J.rank(),16)
        self.assertEqual(len(J.nullspace()),8)
        self.assertEqual(G.rank()+V.rank()-J.rank(),1)
        self.assertTrue(all(J*w==s.zeros(26,1) for w in J.nullspace()))

    def test_joint_kernel_does_not_force_spin_connection_zero(self):
        X=s.Matrix([2,0,0,0]);_,G=matrices(X,s.eye(4))
        n=G.col_join(minimal_dirac_contraction_matrix()).nullspace()
        self.assertEqual(len(n),8)
        w=n[0]
        omega=[s.zeros(4) for _ in range(4)]
        for j,(mu,a,b) in enumerate(dirs):
            omega[mu]+=w[j]*gammas[a]*gammas[b]/2
        self.assertTrue(any(x!=s.zeros(4) for x in omega))

    def test_normal_metric_source_missed_by_pure_lorentz_variation(self):
        # One nonzero Euler covector, annihilating all 24 projected
        # Lorentz variations. This is a local test, not a field solution.
        X=s.Matrix([2,0,0,0]);e=s.eye(4);_,G=matrices(X,e)
        V=e.inv().T*X
        source=s.Matrix([V[a]*V[b]*(1 if a==b else 2)
                         for a,b in sympairs])
        self.assertNotEqual(source,s.zeros(10,1))
        self.assertEqual(source.T*G,s.zeros(1,24))

    def test_full_composite_chain_rule_all_lorentz_coefficients(self):
        X=s.Matrix([2,1,0,0]); e0=s.eye(4)
        source=s.Matrix(4,4,lambda i,j:s.Rational(2*i+3*j+1,7))
        t=s.symbols("t")
        for k,d in enumerate(dirs):
            de=omega_response(*d,X)
            bare=s.Rational(k-11,3)
            L=sum(source[i,j]*(e0[i,j]+t*de[i,j])
                  for i in range(4) for j in range(4))+bare*t
            target=bare+sum(source[i,j]*de[i,j]
                            for i in range(4) for j in range(4))
            self.assertEqual(s.diff(L,t),target)

    def test_common_central_two_sided_jet_cancels(self):
        t=s.symbols("t")
        Q=s.Matrix([[1+I,2],[3,4-I]])
        self.assertEqual(t*s.eye(2)*Q-Q*t*s.eye(2),s.zeros(2))
        self.assertEqual(2*t*s.eye(2)*Q-Q*t*s.eye(2),t*Q)

if __name__=="__main__": unittest.main()
