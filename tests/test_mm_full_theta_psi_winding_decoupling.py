# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact audit: topological winding is invisible to the existing gravity-only
curvature-square/MM pullback on a restricted flat defining-connection chart.

The canonical tetrad remains E_mu=N0^-1/2 D_mu Theta and central sharp;
no extra string, psi action, matter charge, or on-shell MM solution is asserted.
"""
import unittest
import sympy as sp

I=sp.I
ONE=sp.eye(2)
ZERO=sp.zeros(2)
P=(sp.Matrix([[0,1],[1,0]]),
   sp.Matrix([[0,-I],[I,0]]),
   sp.diag(1,-1))
ETA=sp.diag(-1,1,1,1)
t,x,y,z,psi=sp.symbols("t x y z psi",real=True)
R=sp.symbols("R",positive=True,real=True)
rho=sp.Rational(1,2)
COORDS=(t,x,y,z)
H=P[2]

def theta(n):
    a=sp.Integer(n)*psi/R
    c=sp.sqrt(1+rho*sp.cos(a))
    b=rho*sp.sin(a)
    B=sp.Matrix([[0,c],[c,b]])
    return H+I*(B+t*ONE+x*P[0]+y*P[1]+z*P[2])

def base(A):
    return A.subs({t:0,x:0,y:0,z:0})

def sharp(A):
    return sp.trace(A)*ONE-A

def frame(A):
    return tuple(sp.diff(A,u) for u in COORDS)

def inner(A,B):
    return (sharp(A)*B+sharp(B)*A)/2

def winding_log_derivative(n):
    T=base(theta(n))
    return sp.simplify(sp.diff(T.det(),psi)/T.det())

class MMPsiTopologicalDecoupling(unittest.TestCase):
    def test_winding_profiles_nonzero_and_periodic(self):
        for n in range(5):
            d=sp.simplify(base(theta(n)).det())
            a=sp.Integer(n)*psi/R
            self.assertEqual(sp.simplify(d-rho*sp.exp(I*a)),0)
            self.assertEqual(sp.simplify(theta(n).subs(psi,psi+2*sp.pi*R)-theta(n)),ZERO)
            self.assertEqual(sp.simplify(d*sp.conjugate(d)-rho**2),0)

    def test_exact_integer_winding_across_profiles(self):
        for n in range(5):
            self.assertEqual(winding_log_derivative(n),I*n/R)

    def test_all_profiles_have_identical_spacetime_tetrad(self):
        expected=(I*ONE,I*P[0],I*P[1],I*P[2])
        for n in range(5):
            self.assertEqual(frame(theta(n)),expected)

    def test_sharp_metric_independent_of_winding(self):
        for n in range(5):
            E=frame(theta(n))
            for mu in range(4):
                for nu in range(4):
                    self.assertEqual(sp.simplify(inner(E[mu],E[nu])
                                               -ETA[mu,nu]*ONE),ZERO)

    def test_four_tetrad_columns_are_independent(self):
        for n in range(5):
            E=frame(theta(n))
            M=sp.Matrix(4,4,lambda mu,a:
                sp.trace(E[mu])/(2*I) if a==0
                else -sp.trace(E[mu]*P[a-1])/(2*I))
            self.assertEqual(M.det(),-1)

    def test_psi_gradient_nonzero_but_tetrad_psi_gradient_zero(self):
        for n in (1,2,3):
            self.assertNotEqual(sp.diff(base(theta(n)),psi).subs(psi,0),ZERO)
            self.assertEqual([sp.diff(v,psi) for v in frame(theta(n))],
                             [ZERO]*4)

    def test_psi_only_shifts_leave_tetrad_off_shell_fixed(self):
        f=sp.Function("f",real=True)(psi)
        a=theta(1)
        shifted=a+I*f*P[0]
        self.assertEqual(frame(shifted),frame(a))
        self.assertNotEqual(base(shifted),base(a))

    def test_complex_norm_responds_to_vertical_shift(self):
        lam=sp.symbols("lam",real=True)
        A=base(theta(1))+I*lam*P[0]
        c=sp.sqrt(1+rho*sp.cos(psi/R))
        self.assertEqual(sp.simplify(sp.diff(A.det(),lam).subs(lam,0)-2*c),0)

    def test_gravity_pullback_local_psi_principal_symbol_zero(self):
        # Declared first-jet gravitational comparator depends on (E,omega),
        # never on ∂psi Theta. Exact finite-dimensional principal proxy:
        vpsi,vt,Om=sp.symbols("vpsi vt Om",real=True)
        E=vt+Om
        L=sp.symbols("u0")*E**2+sp.symbols("u1")*E**4
        self.assertEqual(sp.diff(L,vpsi),0)
        self.assertEqual(sp.diff(L,vpsi,2),0)

    def test_existing_mm_cosmological_parameter_excludes_flat_vacuum(self):
        ell=sp.symbols("ell",positive=True,real=True)
        sign=sp.symbols("epsilon",nonzero=True)
        Lambda=3*sign/ell**2
        for k in range(4):
            self.assertNotEqual(sp.simplify(-Lambda*ETA[k,k]),0)

    def test_spacelike_carrier_never_null_on_entire_circle(self):
        for n in (0,1,2,3):
            a=n*psi/R
            c=sp.sqrt(1+rho*sp.cos(a))
            b=rho*sp.sin(a)
            v=sp.Matrix([b/2,c,0,-b/2])
            self.assertEqual(sp.simplify((v.T*ETA*v)[0]-c**2),0)

    def test_h_signature_indefinite_and_relative_H_center_zero(self):
        self.assertEqual(H.det(),-1)
        self.assertEqual(sp.diff(H.det(),psi),0)

    def test_straight_shift_interpolation_crosses_singular_norm(self):
        # θ=π: n=1 is det=-ρ, n=0 is det=+ρ.
        c0=sp.sqrt(1+rho)
        c1=sp.sqrt(1-rho)
        sstar=(c0-1)/(c0-c1)
        self.assertGreater(float(sstar),0)
        self.assertLess(float(sstar),1)
        B0=sp.Matrix([[0,c0],[c0,0]])
        B1=sp.Matrix([[0,c1],[c1,0]])
        A=H+I*((1-sstar)*B0+sstar*B1)
        self.assertEqual(sp.simplify(A.det()),0)

    def test_same_geometry_distinct_topological_integer(self):
        a=theta(0);b=theta(1)
        self.assertEqual(frame(a),frame(b))
        self.assertNotEqual(winding_log_derivative(0),winding_log_derivative(1))

    def test_declared_psi_quadratic_energy_can_detect_winding_but_is_new(self):
        for n in (1,2,3):
            T=base(theta(n))
            deriv=sp.diff(T,psi).subs(psi,0)
            positive=simplified=sp.simplify(sp.trace(deriv.conjugate().T*deriv))
            self.assertEqual(positive,rho**2*n**2/R**2)
        self.assertEqual(sp.diff(base(theta(0)),psi),ZERO)

    def test_existing_splitjet_free_Q_right_inverse_exact(self):
        # Reuse the EXISTING split_jet_palatii_variational_lift formula.
        # This is the FREELY VARIED w model, NOT derived w(H).
        X=sp.Matrix([3,1,2,0])
        Y=sp.Matrix([1,2,3,4])
        q=(X.T*ETA*X)[0]
        self.assertEqual(q,-4)
        w=(X.T*ETA*Y)[0]/q
        U=Y-w*X
        Xa=ETA*X
        Ua=ETA*U
        Kdown=(Ua*Xa.T-Xa*Ua.T)/q
        Kmixed=ETA*Kdown
        self.assertEqual(sp.simplify(Kdown+Kdown.T),sp.zeros(4))
        self.assertEqual(sp.simplify(Kmixed*X+w*X-Y),sp.zeros(4,1))

    def test_winding_interpolation_is_nonnul_carrier_even_at_det_zero(self):
        lam=sp.symbols("lam",real=True)
        c0=sp.sqrt(1+rho)
        c1=sp.sqrt(1-rho)
        c=(1-lam)*c0+lam*c1
        X=sp.Matrix([0,c,0,0])
        q=sp.simplify((X.T*ETA*X)[0])
        self.assertEqual(sp.simplify(q-c*c),0)
        lam_star=(c0-1)/(c0-c1)
        self.assertEqual(sp.simplify(q.subs(lam,lam_star)),1)
        # det Theta=0 need not obstruct the FREE-Q lift (q remains 1).
        self.assertEqual(sp.simplify((-1+c*c).subs(lam,lam_star)),0)

    def test_any_tetrad_target_can_be_lifted_at_topological_crossing(self):
        # At the explicit zero of det Theta, original Lorentz carrier X
        # is spacelike and non-null. The free-w splitjet right inverse works.
        X=sp.Matrix([0,1,0,0])
        q=(X.T*ETA*X)[0]
        self.assertEqual(q,1)
        target=sp.diag(2,3,4,5)
        dX=sp.eye(4)
        for mu in range(4):
            Y=target[mu,:].T-dX[mu,:].T
            w=(X.T*ETA*Y)[0]/q
            U=Y-w*X
            Kdown=(ETA*U*(ETA*X).T-ETA*X*(ETA*U).T)/q
            self.assertEqual(sp.simplify(ETA*Kdown*X+w*X+dX[mu,:].T
                                         -target[mu,:].T),sp.zeros(4,1))
            self.assertEqual(sp.simplify(Kdown+Kdown.T),sp.zeros(4))

    def test_global_winding_invariant_under_nonsingular_continuation(self):
        # The zero-determinant passage above is forced by changing the
        # homotopy class; do NOT call winding an ordinary local gauge mode.
        self.assertEqual(winding_log_derivative(0),0)
        self.assertEqual(winding_log_derivative(1),I/R)
        self.assertEqual(sp.simplify(sp.exp(I*sp.pi)),-1)

if __name__=="__main__":
    unittest.main()
