# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact restricted check: amplitude Fisher information does not force
invertibility of original full-complex Theta, even at the winding crossing.

No physical observer probability, selected psi action or protected defect
is inferred from this mathematical witness.
"""
import unittest
import sympy as sp

R=sp.symbols('R', real=True, positive=True)
psi,s=sp.symbols('psi s', real=True)
rho=sp.Rational(1,2)
c0=sp.sqrt(1+rho)
c1=sp.sqrt(1+rho*sp.cos(psi/R))
c=(1-s)*c0+s*c1
b=s*rho*sp.sin(psi/R)
H=sp.diag(1,-1)
B=sp.Matrix([[0,c],[c,b]])
Theta=H+sp.I*B
d=sp.expand(Theta.det())
q=sp.expand_complex(d*sp.conjugate(d)).expand()

class FisherWindingGate(unittest.TestCase):
    def test_det_formula(self):
        self.assertEqual(sp.simplify(d-(-1+c**2+sp.I*b)),0)

    def test_endpoint_equal_amplitude_probability(self):
        for endpoint in (0,1):
            self.assertEqual(sp.simplify(q.subs(s,endpoint)-rho**2),0)

    def test_finite_frobenius_gradient(self):
        # B and B-prime are Hermitian for 0<rho<1; this is a
        # smoothness diagnostic, NOT a Lorentz-invariant physical action.
        gradient_norm=sp.simplify(sp.trace(B.diff(psi)*B.diff(psi)))
        expected=2*sp.diff(c,psi)**2+sp.diff(b,psi)**2
        self.assertEqual(sp.simplify(gradient_norm-expected),0)

    def test_crossing_zero_is_not_tetrad_zero(self):
        c1_pi=sp.sqrt(1-rho)
        sstar=(c0-1)/(c0-c1_pi)
        self.assertEqual(sp.simplify(d.subs({s:sstar,psi:sp.pi*R})),0)
        self.assertEqual(sp.simplify(c.subs({s:sstar,psi:sp.pi*R})),1)
        self.assertEqual(sp.simplify(b.subs({s:sstar,psi:sp.pi*R})),0)

    def test_fisher_density_has_finite_extension_at_det_zero(self):
        sstar=(c0-1)/(c0-sp.sqrt(1-rho))
        dd_pi=sp.simplify(sp.diff(d,psi).subs({s:sstar,psi:sp.pi*R}))
        self.assertEqual(sp.simplify(dd_pi+sp.I*sstar*rho/R),0)
        self.assertNotEqual(dd_pi,0)
        # q=|d|^2=|dd_pi|^2*(psi-pi R)^2+O(delta^3);
        # (q')^2/q tends to 4*|dd_pi|^2, finite.

    def test_lorentz_congruence_preserves_det_amplitude(self):
        a=sp.symbols('a',real=True,positive=True)
        S=sp.diag(a,1/a)
        self.assertEqual(sp.simplify((S*Theta*S.conjugate().T).det()-d),0)

    def test_fisher_pointwise_cauchy_schwarz_bound(self):
        # (q')^2/q <= 4|d'|^2, for q=|d|^2>0.
        u,v,du,dv=sp.symbols('u v du dv',real=True)
        expr=sp.expand(4*(u*u+v*v)*(du*du+dv*dv)
                       -(2*(u*du+v*dv))**2)
        self.assertEqual(sp.simplify(expr-4*(u*dv-v*du)**2),0)

    def test_same_original_four_spacetime_jet(self):
        t,x,y,z=sp.symbols('t x y z',real=True)
        I=sp.eye(2)
        p1=sp.Matrix([[0,1],[1,0]])
        p2=sp.Matrix([[0,-sp.I],[sp.I,0]])
        p3=sp.diag(1,-1)
        full=Theta+sp.I*(t*I+x*p1+y*p2+z*p3)
        self.assertEqual(tuple(full.diff(u) for u in (t,x,y,z)),
                         (sp.I*I,sp.I*p1,sp.I*p2,sp.I*p3))

if __name__=='__main__': unittest.main()
