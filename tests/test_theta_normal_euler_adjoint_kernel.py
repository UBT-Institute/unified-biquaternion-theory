# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact formal-adjoint kernel for a restricted composite Lorentz tetrad.

This is a source-probe of the smooth, regular, Lorentz-real sector.
The external source functional is NOT a selected fundamental UBT action.
"""
import unittest
import sympy as s

eta=s.diag(-1,1,1,1)
coords=s.symbols('t x y z',real=True)
X=s.Matrix(coords)
Xlow=eta*X
rad=coords[0]**2-coords[1]**2-coords[2]**2-coords[3]**2
h=rad**(-s.Rational(5,2))
E=s.Matrix(4,4,lambda mu,a:h*X[mu]*Xlow[a])

class NormalEulerAdjointKernel(unittest.TestCase):
    def test_regular_future_timelike_patch(self):
        self.assertEqual(rad.subs({coords[0]:2,coords[1]:1,coords[2]:0,coords[3]:0}),3)

    def test_homogeneous_degree_minus_five(self):
        self.assertEqual(s.simplify(sum(coords[mu]*s.diff(h,coords[mu])
                                        for mu in range(4))+5*h),0)

    def test_zero_divergence_every_internal_component(self):
        for a in range(4):
            self.assertEqual(s.simplify(sum(s.diff(E[mu,a],coords[mu])
                                         for mu in range(4))),0)

    def test_all_lorentz_connection_directions_annihilate(self):
        for a in range(4):
            for b in range(a+1,4):
                rot=s.zeros(4)
                rot[a,b]=eta[a,a]
                rot[b,a]=-eta[b,b]
                for mu in range(4):
                    self.assertEqual(s.simplify((E.row(mu)*rot*X)[0]),0)

    def test_source_is_not_identically_zero(self):
        p={coords[0]:2,coords[1]:1,coords[2]:0,coords[3]:0}
        self.assertNotEqual(E[0,0].subs(p),0)

    def test_is_symmetric_canonical_metric_euler_source(self):
        H=s.Matrix(4,4,lambda mu,nu:h*X[mu]*X[nu]/2)
        self.assertEqual(E,2*H*eta)
        self.assertEqual(H,H.T)

    def test_linearized_metric_connection_variation(self):
        q=s.symbols('q')
        mu,a,b=1,0,2
        domega=s.zeros(4)
        domega[a,b]=eta[a,a]
        domega[b,a]=-eta[b,b]
        de=s.Matrix(4,4,lambda i,j:
          q*sum(domega[j,k]*X[k] for k in range(4)) if i==mu else 0)
        dg=de*eta+eta*de.T
        H=s.Matrix(4,4,lambda i,j:h*X[i]*X[j]/2)
        self.assertEqual(s.simplify(s.trace(H*dg)),0)

    def test_transport_equation_has_nonzero_local_solution(self):
        t=s.symbols('t',positive=True)
        self.assertEqual(s.simplify(s.diff(t**(-5),t)+5*t**(-6)),0)

    def test_nontrivial_frame_normal_connection_cokernel(self):
        frame=s.Matrix([[1,1,0,0],[0,2,1,0],[0,0,1,1],[0,0,0,1]])
        Q=s.Matrix([2,1,0,0])
        V=frame.inv().T*Q
        Eb=V*(eta*Q).T
        for mu in range(4):
            for a in range(4):
                for b in range(a+1,4):
                    rot=s.zeros(4)
                    rot[a,b]=eta[a,a]
                    rot[b,a]=-eta[b,b]
                    self.assertEqual(s.simplify((Eb.row(mu)*rot*Q)[0]),0)

    def test_integration_by_parts_density_identity(self):
        t=s.symbols('t',positive=True)
        q=s.Function('q')(t)
        F=t**(-5)*t*t
        self.assertEqual(s.diff(F,t)*q+F*s.diff(q,t),s.diff(F*q,t))

    def test_nonzero_metric_euler_of_explicit_external_source_action(self):
        # S_H[e]=int H^{mu nu}(e_mu^a eta_ab e_nu^b-eta_mu nu).
        # H is prescribed, not a fundamental UBT field or allowed action.
        H=s.Matrix(4,4,lambda i,j:h*X[i]*X[j]/2)
        v=s.Matrix(4,4,lambda i,j:s.Symbol('v%d%d'%(i,j)))
        F=s.trace(H*(v*eta*v.T-eta))
        identity={v[i,j]:int(i==j) for i in range(4) for j in range(4)}
        dF=s.Matrix(4,4,lambda i,j:s.diff(F,v[i,j]).subs(identity))
        self.assertEqual(s.simplify(dF-E),s.zeros(4))
        self.assertNotEqual(dF[0,0].subs({coords[0]:2,coords[1]:1,
                                         coords[2]:0,coords[3]:0}),0)

if __name__=='__main__':
    unittest.main()
