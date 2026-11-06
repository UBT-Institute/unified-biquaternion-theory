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

    def test_reference_strength_is_unselected(self):
        x=sp.symbols('x', positive=True)
        weight=4*x**2/(1+x**2)**2
        self.assertEqual(sp.simplify((1-weight) - (x**2-1)**2/(1+x**2)**2), 0)
        self.assertEqual(sp.limit(weight,x,0),0)
        self.assertEqual(sp.limit(weight,x,sp.oo),0)
        self.assertEqual(sp.simplify(weight.subs(x,1)),1)

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


    def test_full_theta_radial_family_keeps_original_tetrad(self):
        psi,s,R=sp.symbols('psi s R',real=True)
        R=sp.symbols('R',positive=True)
        n=sp.Integer(2)
        rr=(1-s)*sp.Rational(1,2)
        c=sp.sqrt(1+rr*sp.cos(n*psi/R))
        b=rr*sp.sin(n*psi/R)
        one=sp.eye(2)
        pauli=(sp.Matrix([[0,1],[1,0]]),
               sp.Matrix([[0,-sp.I],[sp.I,0]]),
               sp.diag(1,-1))
        t,x,y,z=sp.symbols('t x y z',real=True)
        theta=pauli[2]+sp.I*(sp.Matrix([[0,c],[c,b]])+
                            t*one+x*pauli[0]+y*pauli[1]+z*pauli[2])
        origin=theta.subs({t:0,x:0,y:0,z:0})
        self.assertEqual(sp.simplify(origin.det()-
            rr*(sp.cos(n*psi/R)+sp.I*sp.sin(n*psi/R))),0)
        self.assertEqual([theta.diff(var) for var in (t,x,y,z)],
            [sp.I*one,sp.I*pauli[0],sp.I*pauli[1],sp.I*pauli[2]])
        self.assertEqual(sp.simplify(c.subs(s,1)),1)

    def test_fixed_winding_qfi_infimum_zero_even_before_det_zero(self):
        rr,a,R,n=sp.symbols('r a R n',positive=True)
        J=2*sp.pi*n**2/R*4*a**2*rr**2/(a**2+rr**2)**2
        self.assertEqual(sp.limit(J,rr,0,dir='+'),0)
        self.assertEqual(sp.simplify(J.subs(rr,a)-2*sp.pi*n**2/R),0)

    def test_uniform_radial_descent_second_variation_is_negative(self):
        s=sp.symbols('s',real=True)
        f=4*(1-s)**2/(1+(1-s)**2)**2
        self.assertEqual(sp.simplify(f.subs(s,0)-1),0)
        self.assertEqual(sp.simplify(f.subs(s,1)),0)
        self.assertEqual(sp.simplify(sp.diff(f,s).subs(s,0)),0)
        self.assertEqual(sp.simplify(sp.diff(f,s,2).subs(s,0)+2),0)
        self.assertLess(sp.diff(f,s).subs(s,sp.Rational(1,2)),0)

    def test_radial_hessian_negative_at_balanced_reference(self):
        a,w,R,n=sp.symbols('a w R n',positive=True)
        J=2*sp.pi*n**2/R*4*a**2*w**2/(a**2+w**2)**2
        self.assertEqual(sp.simplify(sp.diff(J,w).subs(w,a)),0)
        self.assertEqual(sp.simplify(sp.diff(J,w,2).subs(w,a)
            +4*sp.pi*n**2/(R*a**2)),0)

    def test_fubini_study_euler_lagrange_circle_equator(self):
        a,w,R=sp.symbols('a w R',positive=True)
        theta=sp.symbols('theta',real=True)
        n=sp.Integer(2)
        z=w*sp.exp(sp.I*n*theta/R)
        zpsi=sp.diff(z,theta)
        residual=sp.diff(zpsi,theta)-2*sp.conjugate(z)*zpsi**2/(a**2+w**2)
        expected=n**2/R**2*z*(w**2-a**2)/(w**2+a**2)
        self.assertEqual(sp.simplify(residual-expected),0)
        self.assertEqual(sp.simplify(residual.subs(w,a)),0)

if __name__=="__main__": unittest.main()
