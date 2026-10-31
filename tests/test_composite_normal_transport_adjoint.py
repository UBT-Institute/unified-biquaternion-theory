# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact formal-adjoint kernel of the restricted composite Lorentz tetrad map.

NOT a finalized UBT action; the nonzero p is a deliberately supplied
off-shell tetrad Euler-source density used to test the variation map.
"""
import itertools
import unittest
import sympy as s

eta=s.diag(-1,1,1,1)
coords=s.symbols('t x y z', real=True)
t,x,y,z=coords
X=s.Matrix(coords)
E=s.eye(4)
V=E.inv().T*X
lam=t**-5
Xdown=eta*X
p=V*Xdown.T*lam
pairs=tuple(itertools.combinations(range(4),2))

def lorentz_jet(mu,a,b,X):
    de=s.zeros(4,4)
    de[mu,a]+=eta[a,a]*X[b]
    de[mu,b]-=eta[b,b]*X[a]
    return de

def divergence(p):
    return s.Matrix([s.simplify(sum(s.diff(p[mu,a],coords[mu])
                                  for mu in range(4))) for a in range(4)])

class NormalTransport(unittest.TestCase):
    def test_regular_timelike_chart_at_sample(self):
        self.assertEqual((X.T*eta*X)[0].subs(
            {t:2,x:s.Rational(1,4),y:0,z:0}),-s.Rational(63,16))
        self.assertEqual(E.det(),1)

    def test_lorentz_contraction_all_24(self):
        for mu in range(4):
            for a,b in pairs:
                d=lorentz_jet(mu,a,b,X)
                self.assertEqual(s.simplify(sum(p[i,j]*d[i,j]
                    for i in range(4) for j in range(4))),0)

    def test_carrier_divergence_zero_all_four(self):
        self.assertEqual(divergence(p),s.zeros(4,1))

    def test_nonzero_normal_source(self):
        self.assertNotEqual(p.subs({t:2,x:0,y:0,z:0}),s.zeros(4))
        self.assertEqual(s.simplify(p[0,0]),-t**-3)

    def test_transport_first_order_equation(self):
        self.assertEqual(s.simplify(sum(
            s.diff(lam*V[mu],coords[mu]) for mu in range(4))+lam),0)
        g=t**-5*(1+(x/t)**2)
        self.assertEqual(s.simplify(sum(
            s.diff(g*V[mu],coords[mu]) for mu in range(4))+g),0)

    def test_constant_lambda_fails(self):
        self.assertEqual(divergence(V*Xdown.T),5*Xdown)

    def test_vary_carrier_as_gradient_full_chain_rule(self):
        h=s.Matrix([t**2+x,x*y+y**2,t*z,x*z+t*y])
        contribution=sum(p[mu,a]*s.diff(h[a],coords[mu])
                         for mu in range(4) for a in range(4))
        boundary=sum(s.diff(sum(p[mu,a]*h[a] for a in range(4)),coords[mu])
                     for mu in range(4))
        self.assertEqual(s.simplify(contribution-boundary),0)

    def test_actual_canonical_sharp_metric_equals_eta(self):
        pauli=[s.eye(2),s.Matrix([[0,1],[1,0]]),
               s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
        def lift(row):
            return s.I*(row[0]*pauli[0]-sum(
                (row[j]*pauli[j] for j in range(1,4)),s.zeros(2)))
        sharp=lambda A:s.trace(A)*s.eye(2)-A
        jets=[lift(list(E.row(mu))) for mu in range(4)]
        metric=s.Matrix(4,4,lambda mu,nu:s.simplify(
            s.trace(sharp(jets[mu])*jets[nu])/2))
        self.assertEqual(metric,eta)

    def test_affine_nonorthonormal_frame(self):
        M=s.Matrix([[1,s.Rational(1,2),0,0],
                    [0,1,0,0],[0,0,2,0],[0,0,0,1]])
        XT=M*X
        ET=M.T
        VT=s.simplify(ET.inv().T*XT)
        self.assertEqual(VT,X)
        pT=VT*(eta*XT).T*lam
        self.assertEqual(divergence(pT),s.zeros(4,1))
        for mu in range(4):
            for a,b in pairs:
                d=lorentz_jet(mu,a,b,XT)
                self.assertEqual(s.simplify(sum(pT[i,j]*d[i,j]
                    for i in range(4) for j in range(4))),0)

    def test_dilation_detects_normal(self):
        x2=(X.T*eta*X)[0]
        for mu in range(4):
            self.assertEqual(s.simplify(
                sum(p[mu,a]*X[a] for a in range(4))-lam*V[mu]*x2),0)
        self.assertNotEqual((lam*V[0]*x2).subs(
            {t:2,x:0,y:0,z:0}),0)

if __name__=='__main__':
    unittest.main()
