# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact canonical sharp vs exploratory dagger metric comparison.

Scope: Mat(2,C), one local trial chart and unrestricted complex first jets;
the Killing-flatness lemma assumes a pure gradient with real projection of
full rank. This is not a UBT field equation or a global no-go.
"""
import unittest
import sympy as s

I=s.eye(2)
S1=s.Matrix([[0,1],[1,0]])
S2=s.Matrix([[0,-s.I],[s.I,0]])
S3=s.diag(1,-1)
SIGMA=(I,S1,S2,S3)
ETA=s.diag(1,-1,-1,-1)

def sharp(A):
    return s.trace(A)*I-A

def central(A,B):
    return s.simplify((sharp(A)*B+sharp(B)*A)/2)

def c(A,B):
    return s.simplify(s.trace(sharp(A)*B)/2)

def b(A,B):
    return s.simplify(s.re(s.trace(sharp(A)*B.conjugate().T))/2)


class TestThetaCentralMetricBridge(unittest.TestCase):
    def test_exact_sharp_central_identity_for_arbitrary_complex_matrices(self):
        a,b0,c0,d,e,f,g,h=s.symbols('a b c d e f g h',complex=True)
        A=s.Matrix([[a,b0],[c0,d]])
        T=s.Matrix([[e,f],[g,h]])
        self.assertEqual(s.simplify(central(A,T)-c(A,T)*I),s.zeros(2))
        self.assertEqual(s.simplify(c(A,T)-c(T,A)),0)

    def test_phase_charge_of_central_versus_dagger_invariance(self):
        al=s.symbols('al',real=True)
        A=I
        R=s.exp(s.I*al)*A
        self.assertEqual(s.simplify(c(R,R)-s.exp(2*s.I*al)*c(A,A)),0)
        self.assertEqual(s.simplify(b(R,R)-b(A,A)),0)

    def test_no_global_constant_bridge(self):
        self.assertEqual(c(I,I),1)
        self.assertEqual(c(s.I*I,s.I*I),-1)
        self.assertEqual(b(I,I),1)
        self.assertEqual(b(s.I*I,s.I*I),1)

    def test_curved_witness_local_metric_mismatch(self):
        k=s.symbols('k',real=True)
        U=(I,(1+s.I*k)*S1,S2,S3)
        C=s.Matrix(4,4,lambda i,j:c(U[i],U[j]))
        B=s.Matrix(4,4,lambda i,j:b(U[i],U[j]))
        self.assertEqual(C,s.diag(1,-(1+s.I*k)**2,-1,-1))
        self.assertEqual(B,s.diag(1,-1-k**2,-1,-1))
        self.assertEqual(s.simplify((C-B)[1,1]-2*k**2+2*s.I*k),0)
        self.assertEqual(s.simplify(C.subs(k,1)),s.diag(1,-2*s.I,-1,-1))
        self.assertEqual(B.subs(k,1),s.diag(1,-2,-1,-1))

    def test_no_common_phase_can_make_witness_metric_real(self):
        # k=1 gives C_tt=1, C_xx=-2i. Every common unit phase
        # realifying C_tt must itself be real, hence cannot realify C_xx.
        pr,pi=s.symbols('pr pi',real=True)
        self.assertEqual(
            s.solve([pi,-2*pr,pr**2+pi**2-1],(pr,pi)),[])

    def test_complex_orthogonal_jets_can_produce_real_canonical_metric(self):
        theta=s.symbols('theta',real=True)
        co,si=s.cos(theta),s.sin(theta)
        # A complex Lorentz boost with imaginary rapidity applied to iHerm.
        E=(s.I*(co*I+s.I*si*S1),
           s.I*(s.I*si*I+co*S1),s.I*S2,s.I*S3)
        G=s.Matrix(4,4,lambda i,j:c(E[i],E[j]))
        self.assertEqual(s.simplify(G+ETA),s.zeros(4))
        self.assertNotEqual(
            s.simplify(E[0].conjugate().T+E[0]),s.zeros(2))
        # These constant complex jets integrate to an affine Theta field.

    def test_on_strict_ihermitian_slice_the_pairings_match_up_to_sign(self):
        r=s.symbols('r',real=True)
        A=s.I*(I+r*S1)
        Q=s.I*S2
        self.assertEqual(s.simplify(c(A,Q)+b(A,Q)),0)
        self.assertEqual(s.simplify(c(A,A)+b(A,A)),0)

    def test_exact_real_imaginary_decomposition(self):
        aa=s.symbols('a0:4',real=True)
        yy=s.symbols('y0:4',real=True)
        A=sum((aa[i]*SIGMA[i] for i in range(4)),s.zeros(2))
        Y=sum((yy[i]*SIGMA[i] for i in range(4)),s.zeros(2))
        Z=A+s.I*Y
        self.assertEqual(s.simplify(
            c(Z,Z)-b(Z,Z)+2*c(Y,Y)-2*s.I*c(A,Y)),0)

    def test_degenerate_real_projection_can_hide_nonzero_imaginary_jet(self):
        n=I+S1  # null in Minkowski signature
        A=(n,S2,S3,s.zeros(2))
        Y=(n,s.zeros(2),s.zeros(2),s.zeros(2))
        U=[A[i]+s.I*Y[i] for i in range(4)]
        self.assertEqual(s.Matrix(4,4,lambda i,j:s.simplify(
            c(U[i],U[j])-b(U[i],U[j]))),s.zeros(4))
        R=s.Matrix.hstack(*[
            s.Matrix([c(A[i],SIGMA[j]) for j in range(4)])
            for i in range(4)])
        self.assertEqual(R.rank(),3)

    def test_rank_four_real_part_forces_null_imaginary_jet_to_zero(self):
        # In Lorentz (1,3) a totally isotropic real subspace has dim<=1.
        # A Lorentz basis change puts the nonzero generator along I+S1.
        lm=s.symbols('l0:4',real=True)
        n=I+S1
        constraints=[
            s.expand(c(SIGMA[i],lm[j]*n)+c(lm[i]*n,SIGMA[j]))
            for i in range(4) for j in range(i,4)]
        self.assertEqual(s.linsolve(
            constraints,lm),s.FiniteSet((0,0,0,0)))

    def test_killing_equations_imply_affine_imaginary_field(self):
        xx=s.symbols('X0:4',real=True)
        ya=[s.Function('Y'+str(i))(*xx) for i in range(4)]
        lower=[(-1 if i else 1)*ya[i] for i in range(4)]
        K=lambda i,j:s.diff(lower[i],xx[j])+s.diff(lower[j],xx[i])
        # Identity: 2 Y_{j,ik} = partial_k K_ij
        #                    + partial_i K_jk - partial_j K_ki.
        for i,j,k in [(0,0,1),(0,2,3),(1,2,3),
                      (2,3,0),(3,1,1)]:
            expr=(s.diff(K(i,j),xx[k])
                  +s.diff(K(j,k),xx[i])
                  -s.diff(K(k,i),xx[j]))
            self.assertEqual(s.simplify(
                expr-2*s.diff(lower[j],xx[i],xx[k])),0)

    def test_complex_killing_embedding_has_real_flat_sharp_metric(self):
        t,x,y,z,k=s.symbols('t x y z k',real=True)
        # X=(t,x,y,z) is a coordinate map. Imaginary part
        # Y=k*(x,t,0,0) is an infinitesimal Lorentz boost.
        Q=t*I+x*S1+y*S2+z*S3+s.I*k*(x*I+t*S1)
        coords=(t,x,y,z)
        jets=[s.diff(Q,a) for a in coords]
        G=s.Matrix(4,4,lambda i,j:c(jets[i],jets[j]))
        self.assertEqual(s.simplify(
            G-s.diag(1+k*k,-1-k*k,-1,-1)),s.zeros(4))
        self.assertNotEqual(s.simplify(
            jets[0].conjugate().T-jets[0]),s.zeros(2))
        for entry in G:
            self.assertFalse(entry.has(t,x,y,z))


if __name__=='__main__':
    unittest.main()
