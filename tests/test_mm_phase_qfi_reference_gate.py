# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Research counterexample: phase-sensitive Fisher information detects winding
but remains regular when det Theta crosses zero. The external reference
amplitude is not a derived UBT quantum state or a physical psi action.
"""
import unittest
import sympy as sp

A,u,v,du,dv=sp.symbols("a u v du dv",real=True)
R,rho=sp.symbols("R rho",positive=True,real=True)
N=A**2+u**2+v**2

class FullThetaPhaseQFI(unittest.TestCase):
    def test_projective_qfi_exact_for_reference_and_determinant(self):
        w=sp.Matrix([A,u+sp.I*v])
        dw=sp.Matrix([0,du+sp.I*dv])
        dot=lambda l,r:(l.conjugate().T*r)[0]
        qfi=4*(dot(dw,dw)/dot(w,w)-dot(w,dw)*dot(dw,w)/dot(w,w)**2)
        expected=4*A**2*(du**2+dv**2)/N**2
        self.assertEqual(sp.simplify(qfi-expected),0)

    def test_global_phase_only_has_zero_projective_qfi(self):
        theta,k=sp.symbols('theta k',real=True)
        w=sp.Matrix([sp.exp(sp.I*k*theta)])
        dw=w.diff(theta)
        dot=lambda l,r:(l.conjugate().T*r)[0]
        self.assertEqual(sp.simplify(4*(dot(dw,dw)-dot(w,dw)*dot(dw,w))),0)

    def test_winding_phase_qfi_with_reference(self):
        n=sp.symbols('n',integer=True)
        expression=4*A**2*(rho**2*n**2/R**2)/(A**2+rho**2)**2
        self.assertEqual(sp.simplify(expression.subs(A,rho)-n**2/R**2),0)
        self.assertEqual(expression.subs(n,0),0)

    def test_crossing_has_finite_qfi_and_nonzero_reference_norm(self):
        rr=sp.Rational(1,2)
        s_star=(sp.sqrt(1+rr)-1)/(sp.sqrt(1+rr)-sp.sqrt(1-rr))
        derivative=-sp.I*s_star*rr/R
        qfi_at_zero=4*A**2*(derivative*sp.conjugate(derivative))/A**4
        self.assertEqual(sp.simplify(qfi_at_zero-4*s_star**2*rr**2/(A**2*R**2)),0)
        self.assertTrue(0<float(s_star)<1)

    def test_measurement_probabilities_and_zero_crossing(self):
        chi=sp.symbols('chi',real=True)
        realpart=u*sp.cos(chi)+v*sp.sin(chi)
        plus=sp.Rational(1,2)+A*realpart/N
        minus=sp.Rational(1,2)-A*realpart/N
        self.assertEqual(sp.simplify(plus+minus),1)
        self.assertEqual(sp.simplify(plus.subs({u:0,v:0})-sp.Rational(1,2)),0)
        self.assertEqual(sp.simplify(minus.subs({u:0,v:0})-sp.Rational(1,2)),0)

    def test_interferometer_resolves_phase_winding(self):
        h,k=sp.symbols('h k',real=True)
        p=(1+sp.cos(k*h))/2
        fi=sp.simplify(sp.diff(p,h)**2/(p*(1-p)))
        self.assertEqual(sp.trigsimp(fi-k**2),0)

    def test_interferometer_saturates_qfi_at_zero_with_chosen_phase(self):
        chi=sp.symbols('chi',real=True)
        realpart=u*sp.cos(chi)+v*sp.sin(chi)
        p=sp.Rational(1,2)+A*realpart/N
        dp=sp.diff(p,u)*du+sp.diff(p,v)*dv
        fi=(dp**2/p+dp**2/(1-p)).subs({u:0,v:0,chi:-sp.pi/2})
        self.assertEqual(sp.simplify(fi-4*dv**2/A**2),0)
        self.assertEqual(sp.simplify(fi.subs({du:0,dv:-rho/R})-4*rho**2/(A**2*R**2)),0)

    def test_uniform_bound_finite_even_at_det_zero(self):
        derivative_norm=du**2+dv**2
        bound=4*derivative_norm/A**2
        actual=4*A**2*derivative_norm/N**2
        self.assertEqual(sp.factor(bound-actual),
          sp.factor(4*derivative_norm*(N**2-A**4)/(A**2*N**2)))

if __name__=="__main__": unittest.main()
