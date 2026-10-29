# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact scope: real central dilation is locally removable when exact.

For a two-sided SL(2,C) Lorentz derivative and a real central one-form
u=d(sigma), D_{Omega+u/2 I} Theta=e^-sigma D_Omega(e^sigma Theta).
Neither a gravity action nor local SU(2,2) covariance is implied.
"""
import unittest
import sympy as s

t,x,y,z=s.symbols("t x y z",real=True)
I=s.I
sigmas=(s.eye(2),s.Matrix([[0,1],[1,0]]),
        s.Matrix([[0,-I],[I,0]]),s.diag(1,-1))
sigma=t*x+y**2
theta=(t+2)*sigmas[0]+(x+t*y)*sigmas[1]+(z+I*t)*sigmas[2]
Lor=(s.Rational(1,3)*sigmas[1]+I*s.Rational(1,7)*sigmas[3])
def D0(F, v):
    return s.diff(F,v)+Lor*F+F*Lor.conjugate().T
def Du(F,v):
    u=s.diff(sigma,v)
    Om=Lor+u*s.eye(2)/2
    return s.diff(F,v)+Om*F+F*Om.conjugate().T

class TestRealDilationExactness(unittest.TestCase):
    def test_weyl_exact_connection_identity(self):
        for v in (t,x,y,z):
            lhs=Du(theta,v)
            rhs=s.exp(-sigma)*D0(s.exp(sigma)*theta,v)
            self.assertEqual(s.simplify(lhs-rhs),s.zeros(2))

    def test_exact_dilation_field_strength_zero(self):
        for a in (t,x,y,z):
            for b in (t,x,y,z):
                u_a=s.diff(sigma,a)
                u_b=s.diff(sigma,b)
                self.assertEqual(s.simplify(s.diff(u_a,b)-s.diff(u_b,a)),0)

    def test_nonintegrable_dilation_is_not_removable(self):
        # u=x dt; (du)_{x,t}=+1. Cannot be written as d sigma locally.
        u={t:x,x:s.Integer(0),y:s.Integer(0),z:s.Integer(0)}
        self.assertEqual(s.diff(u[t],x)-s.diff(u[x],t),1)

    def test_radial_only_cannot_make_rank_four(self):
        r=s.exp(t+x*y)
        Xi=r*s.eye(2)
        # sigma=ln r: exact u = d log r, Omega_Lor=0
        d=[s.simplify(s.diff(Xi,v)+s.diff(s.log(r),v)*Xi)
           for v in (t,x,y,z)]
        self.assertTrue(all(s.simplify(m-2*s.diff(r,v)*s.eye(2))==s.zeros(2)
                        for m,v in zip(d,(t,x,y,z))))
        # All four spacetime directions are proportional to identity.
        self.assertEqual(s.Matrix([[s.simplify(s.trace(m*P)/2)
                                      for m in d] for P in sigmas]).rank(),1)

if __name__=="__main__":
    unittest.main()
