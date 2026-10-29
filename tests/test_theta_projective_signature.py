# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact restricted (2,6) signature gate for composite scale+phase projection.

The field's positive H-norm branch is used. The zero-connection
gradient metric is a comparator, not a canonical SU(2,2) UBT metric.
"""
import unittest
import sympy as s

B=s.diag(1,-1,-1,-1,1,-1,-1,-1)
J=s.zeros(8)
J[:4,4:]=-s.eye(4)
J[4:,:4]=s.eye(4)
I=s.eye(8)
q=s.Matrix(s.symbols("q0:8",real=True))

def dot(a,b):
    return s.simplify((a.T*B*b)[0])

def projector(Q):
    n=dot(Q,Q)
    JQ=J*Q
    return s.simplify(I-(Q*Q.T*B+JQ*JQ.T*B)/n)

class TestThetaProjectiveSignature(unittest.TestCase):
    def test_complex_structure_orthogonality_and_signature(self):
        self.assertEqual(J.T*B*J,B)
        self.assertEqual(J.T*B+B*J,s.zeros(8))
        self.assertEqual(dot(q,J*q),0)
        self.assertEqual(s.expand(dot(J*q,J*q)-dot(q,q)),0)

    def test_projection_orthogonality_idempotence_generic(self):
        Q=s.Matrix([2,1,0,0,0,1,0,0])
        P=projector(Q)
        self.assertEqual(Q.T*B*P,s.zeros(1,8))
        self.assertEqual((J*Q).T*B*P,s.zeros(1,8))
        self.assertEqual(P*P,P)
        self.assertEqual(P.rank(),6)
        self.assertEqual(s.simplify(P.T*B-B*P),s.zeros(8))

    def test_positive_scalar_point_negative_semidefinite(self):
        Q=s.Matrix([1,0,0,0,0,0,0,0])
        P=projector(Q)
        self.assertEqual(P,s.diag(0,1,1,1,0,1,1,1))
        self.assertEqual(P.T*B*P,
                         s.diag(0,-1,-1,-1,0,-1,-1,-1))

    def test_projection_annihilates_time_jet_in_affine_chart(self):
        Q=s.Matrix([1,0,0,0,0,0,0,0])
        P=projector(Q)
        E=s.Matrix.hstack(*[I[:,i] for i in (0,1,2,3)])
        self.assertEqual(E.T*P.T*B*P*E,s.diag(0,-1,-1,-1))

    def test_projected_four_dimensional_metric_can_be_negative_definite(self):
        Q=s.Matrix([1,0,0,0,0,0,0,0])
        P=projector(Q)
        E=s.Matrix.hstack(*[I[:,i] for i in (1,2,3,5)])
        self.assertEqual(E.T*P.T*B*P*E,-s.eye(4))

    def test_negative_norm_branch_allows_lorentz_tangent_metric(self):
        Q=I[:,1]  # sigma1; q and Jq both have negative norm
        self.assertEqual(dot(Q,Q),-1)
        P=projector(Q)
        E=s.Matrix.hstack(*[I[:,i] for i in (0,2,3,6)])
        self.assertEqual(P*E,E)
        self.assertEqual(E.T*P.T*B*P*E,
                         s.diag(1,-1,-1,-1))

    def test_phase_only_compensator_preserves_lorentz_metric(self):
        a=s.symbols("a",real=True)
        Q=s.Matrix([1,0,0,0,0,0,0,0])
        D=s.Matrix.hstack(*[I[:,i] for i in (0,1,2,3)])
        shifted=D.copy()
        shifted[:,0]+=a*J*Q
        j=s.Matrix([dot(J*Q,shifted[:,i])/dot(Q,Q)
                    for i in range(4)])
        self.assertEqual(j,s.Matrix([a,0,0,0]))
        corrected=s.Matrix.hstack(*[
            shifted[:,i]-j[i]*(J*Q) for i in range(4)])
        self.assertEqual(corrected.T*B*corrected,
                         s.diag(1,-1,-1,-1))

    def test_combined_scale_and_phase_covariance_of_projection(self):
        lam,alpha=s.symbols("lam alpha",real=True)
        Q=s.Matrix([2,1,0,0,0,1,0,0])
        D=s.Matrix([1,2,3,4,0,-1,-2,1])
        R=s.cos(alpha)*I+s.sin(alpha)*J
        Qp=s.exp(lam)*R*Q
        Dp=s.exp(lam)*R*(D+Q+J*Q)
        radial=lambda X,dX:-dot(X,dX)/dot(X,X)
        phase=lambda X,dX:dot(J*X,dX)/dot(X,X)
        self.assertEqual(s.simplify(radial(Qp,Dp)-(radial(Q,D)-1)),0)
        self.assertEqual(s.simplify(phase(Qp,Dp)-(phase(Q,D)+1)),0)
        projected=lambda X,dX:dX+radial(X,dX)*X-phase(X,dX)*J*X
        self.assertEqual(s.simplify(
            projected(Qp,Dp)-s.exp(lam)*R*projected(Q,D)),
            s.zeros(8,1))

if __name__=="__main__":
    unittest.main()
