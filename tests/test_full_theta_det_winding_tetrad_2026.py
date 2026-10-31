# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Full COMPLEX biquaternion determinant winding with the ORIGINAL sharp tetrad.

Mathematically conditional: H is invertible of inertia (1,1), unlike the
previous positive H patch. This is not a selected psi field equation,
spinorial coupling, string winding or physical T-duality.
"""
import unittest
import sympy as s

I=s.I
J=s.eye(2)
Z=s.zeros(2)
SIG=(s.Matrix([[0,1],[1,0]]),
     s.Matrix([[0,-I],[I,0]]),
     s.diag(1,-1))
ETA=s.diag(-1,1,1,1)
t,x,y,z,psi=s.symbols('t x y z psi',real=True)
R=s.symbols('R',real=True,positive=True)
rho=s.Rational(1,2)
theta=psi/R
c=s.sqrt(1+rho*s.cos(theta))
b=rho*s.sin(theta)
H=SIG[2]
K=s.Matrix([[0,c],[c,b]])
Theta=H+I*(K+t*J+x*SIG[0]+y*SIG[1]+z*SIG[2])
coord=(t,x,y,z)

def adj(A):
    # For real psi/R and rho=1/2, 1+rho*cos(psi/R) >= 1/2 > 0.
    # SymPy does not infer this trigonometric bound symbolically, so apply
    # the mathematically justified real-positive-root identity explicitly.
    return s.conjugate(A).T.xreplace({s.conjugate(c):c})
def sharp(A): return s.trace(A)*J-A
def hpart(A): return s.simplify((A+adj(A))/2)
def xpart(A): return s.simplify((A-adj(A))/2)

def sector_at_origin(A):
    return A.subs({t:0,x:0,y:0,z:0})

class FullThetaDeterminantWinding(unittest.TestCase):
    def test_original_field_is_one_complex_biquaternion(self):
        self.assertEqual(Theta.shape,(2,2))
        self.assertEqual(s.simplify(hpart(Theta)-H),Z)
        self.assertEqual(s.simplify(xpart(Theta)-I*(K+t*J+x*SIG[0]+y*SIG[1]+z*SIG[2])),Z)

    def test_h_is_invertible_indefinite_not_positive(self):
        self.assertEqual(H.det(),-1)
        self.assertEqual(H.eigenvals(),{s.Integer(-1):1,s.Integer(1):1})
        self.assertEqual(s.simplify(H+adj(H)),2*H)

    def test_winding_is_canonical_complex_quaternion_sharp_norm(self):
        T=sector_at_origin(Theta)
        self.assertEqual(s.simplify(sharp(T)*T-T.det()*J),Z)
        self.assertEqual(s.simplify(T*sharp(T)-T.det()*J),Z)

    def test_full_field_determinant_is_nonzero_unit_winding(self):
        d=s.simplify(sector_at_origin(Theta).det())
        self.assertEqual(s.simplify(d-rho*s.exp(I*theta)),0)
        self.assertEqual(s.simplify(d*s.conjugate(d)-rho**2),0)

    def test_full_and_H_determinants_have_different_winding(self):
        d=s.simplify(sector_at_origin(Theta).det())
        self.assertEqual(s.simplify(s.diff(d,psi)/d),I/R)
        self.assertEqual(s.diff(H.det(),psi),0)
        self.assertEqual(s.simplify(s.diff(H.det(),psi)/H.det()),0)

    def test_periodicity_of_one_full_theta(self):
        new=Theta.subs(psi,psi+2*s.pi*R)
        self.assertEqual(s.simplify(new-Theta),Z)

    def test_canonical_tetrad_is_psi_independent(self):
        E=[s.simplify(s.diff(Theta,u)) for u in coord]
        expected=[I*J,*[I*Q for Q in SIG]]
        self.assertEqual(E,expected)
        for A in E: self.assertEqual(s.simplify(A+adj(A)),Z)

    def test_full_sharp_metric_is_real_central_minkowski(self):
        E=[s.diff(Theta,u) for u in coord]
        for mu in range(4):
            for nu in range(4):
                g=s.simplify((sharp(E[mu])*E[nu]+sharp(E[nu])*E[mu])/2)
                self.assertEqual(s.simplify(g-ETA[mu,nu]*J),Z)

    def test_tetrad_is_regular_everywhere(self):
        E=[s.diff(Theta,u) for u in coord]
        coframe=s.Matrix(4,4,lambda mu,a:s.simplify(
            s.trace(E[mu])/(2*I) if a==0
            else -s.trace(E[mu]*SIG[a-1])/(2*I)))
        self.assertEqual(coframe,s.diag(1,-1,-1,-1))
        self.assertEqual(coframe.det(),-1)

    def test_derived_H_center_is_zero_but_full_connection_nonzero(self):
        wH=-s.diff(H.det(),psi)/(2*H.det())
        d=s.simplify(sector_at_origin(Theta).det())
        alpha=s.simplify(s.diff(d,psi)/(2*d))
        self.assertEqual(wH,0)
        self.assertEqual(alpha,I/(2*R))

    def test_full_composite_half_holonomy(self):
        alpha=I/(2*R)
        hol=s.simplify(s.exp(alpha*(2*s.pi*R)))
        self.assertEqual(hol,-1)

    def test_half_root_is_antiperiodic(self):
        root=s.sqrt(rho)*s.exp(I*psi/(2*R))
        self.assertEqual(s.simplify(root**2-rho*s.exp(I*theta)),0)
        self.assertEqual(s.simplify(root.subs(psi,psi+2*s.pi*R)+root),0)

    def test_periodic_probe_has_conditional_half_shift(self):
        m=s.symbols('m',integer=True)
        probe=s.exp(I*m*psi/R)
        alpha=I/(2*R)
        self.assertEqual(s.simplify((s.diff(probe,psi)+alpha*probe)/
                                    probe),I*(m+s.Rational(1,2))/R)

    def test_charge_even_has_integer_reindexed_shift(self):
        m=s.symbols('m',integer=True)
        alpha=I/(2*R)
        for q in (0,2,4):
            self.assertEqual(s.simplify((s.diff(s.exp(I*m*psi/R),psi)
                +q*alpha*s.exp(I*m*psi/R))/s.exp(I*m*psi/R)),I*(m+s.Rational(q,2))/R)

    def test_lorentz_SL2_congruence_preserves_full_winding(self):
        S=s.Matrix([[2,0],[0,s.Rational(1,2)]])
        self.assertEqual(S.det(),1)
        T=S*Theta*adj(S)
        self.assertEqual(s.simplify(sector_at_origin(T).det()-
                          sector_at_origin(Theta).det()),0)
        self.assertEqual(s.simplify(hpart(T)-S*H*adj(S)),Z)

    def test_positive_real_rescaling_keeps_winding(self):
        eps=s.Function('eps',real=True)(psi)
        T=s.exp(eps)*sector_at_origin(Theta)
        alpha=s.simplify(s.diff(T.det(),psi)/(2*T.det()))
        self.assertEqual(s.simplify(alpha-I/(2*R)-s.diff(eps,psi)),0)

    def test_single_valued_central_phase_shifts_winding_by_even_int(self):
        k=s.symbols('k',integer=True)
        d=s.simplify(sector_at_origin(Theta).det())
        dp=s.exp(2*I*k*theta)*d
        self.assertEqual(s.simplify(s.diff(dp,psi)/dp-I*(1+2*k)/R),0)

    def test_positive_H_loop_no_winding_example(self):
        Hp=J
        Tp=Hp+I*(s.cos(theta)*SIG[0]+s.sin(theta)*SIG[1])
        self.assertEqual(s.simplify(Tp.det()),2)
        self.assertEqual(s.simplify(s.diff(Tp.det(),psi)),0)

    def test_accretive_positive_H_homotopy_never_singular_example(self):
        lam=s.symbols('lam',real=True)
        Hp=J
        Xp=I*(s.cos(theta)*SIG[0]+s.sin(theta)*SIG[1])
        self.assertEqual(s.simplify((Hp+lam*Xp).det()),1+lam**2)

    def test_indefinite_H_compatible_sl2_stabilizer(self):
        for Om in (SIG[0],SIG[1],I*SIG[2]):
            self.assertEqual(s.simplify(Om*H+H*adj(Om)),Z)
            self.assertEqual(s.trace(Om),0)
        self.assertEqual(s.simplify(SIG[0]*SIG[1]-SIG[1]*SIG[0]),
                         2*I*SIG[2])

    def test_flat_geometry_does_not_select_psi_dynamics(self):
        E=[s.diff(Theta,u) for u in coord]
        self.assertEqual([s.diff(A,psi) for A in E],[Z]*4)
        self.assertNotEqual(s.simplify(s.diff(Theta,psi)),Z)

if __name__=='__main__': unittest.main()
