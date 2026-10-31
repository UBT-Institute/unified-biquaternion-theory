# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Exact relative Weyl compensation and norm-only dilation no-go.

This tests a restricted Lorentz-real composite coframe, NOT a selected
fundamental UBT action, independent physical scalar or carrier dimension.
"""
import itertools
import unittest
import sympy as s

eta=s.diag(-1,1,1,1)

def lorentz_generator(a,b):
    out=s.zeros(4)
    out[a,b]=eta[a,a]
    out[b,a]=-eta[b,b]
    return out

class ExactRelativeWeylGate(unittest.TestCase):
    def test_lorentz_lie_algebra(self):
        for a,b in itertools.combinations(range(4),2):
            w=lorentz_generator(a,b)
            self.assertEqual(w.T*eta+eta*w,s.zeros(4))

    def test_differential_epsilon_cancels_in_compensated_variation(self):
        t=s.symbols('t')
        eps=s.Function('eps')(t)
        phi=s.Function('phi')(t)
        X=s.Matrix([s.Function('X%d'%i)(t) for i in range(4)])
        Om=lorentz_generator(0,1)*s.symbols('u')+lorentz_generator(1,2)*s.symbols('v')
        e=s.diff(X,t)+Om*X+s.diff(phi,t)*X
        dX=eps*X
        dphi=-eps
        de=s.diff(dX,t)+Om*dX+s.diff(phi,t)*dX+s.diff(dphi,t)*X
        self.assertEqual(s.simplify(de-eps*e),s.zeros(4,1))

    def test_compensation_each_coordinate_one_form(self):
        X=s.Matrix(s.symbols('X0:4'))
        for mu in range(4):
            q=s.symbols('q%d'%mu)
            dep=s.symbols('de%d'%mu)
            dX=s.Matrix(s.symbols('J%d_0:4'%mu))
            omega=lorentz_generator(mu%4,(mu+1)%4)*s.symbols('om%d'%mu)
            e=dX+omega*X+q*X
            var=e*s.symbols('eps')+dep*X-dep*X
            self.assertEqual(var,s.symbols('eps')*e)

    def test_stueckelberg_exact_change(self):
        t=s.symbols('t')
        p=s.Function('phi')(t)
        X=s.Matrix([s.Function('X%d'%i)(t) for i in range(4)])
        Om=lorentz_generator(0,3)*s.symbols('q')
        Y=s.exp(p)*X
        e=s.diff(X,t)+Om*X+s.diff(p,t)*X
        self.assertEqual(s.simplify(e-s.exp(-p)*(s.diff(Y,t)+Om*Y)),s.zeros(4,1))

    def test_scalar_norm_only_unique_compensator(self):
        q=s.symbols('q',nonzero=True)
        f=s.Function('f')
        sol=s.dsolve(s.Eq(s.diff(f(q),q),-1/(2*q)),f(q)).rhs
        self.assertEqual(s.simplify(sol+s.log(q)/2).free_symbols,{s.Symbol('C1')})

    def test_norm_only_solution_timelike_domain(self):
        q=s.symbols('q',negative=True)
        f=-s.log(-q)/2
        self.assertEqual(s.simplify(1+2*q*s.diff(f,q)),0)

    def test_radial_compensation_has_no_tetrad_normal(self):
        X=s.Matrix(s.symbols('X0:4'))
        q=(X.T*eta*X)[0]
        for mu in range(4):
            J=s.Matrix(s.symbols('J%d_0:4'%mu))
            Om=lorentz_generator(mu%4,(mu+1)%4)*s.symbols('w%d'%mu)
            w=-(X.T*eta*J)[0]/q
            E=J+Om*X+w*X
            self.assertEqual(s.cancel((X.T*eta*E)[0]),0)

    def test_explicit_norm_based_tetrad_is_degenerate(self):
        t,x,y,z=s.symbols('t x y z',real=True)
        X=s.Matrix([t,x,y,z]); coords=(t,x,y,z)
        q=(X.T*eta*X)[0]
        om=[lorentz_generator(0,1)*x,lorentz_generator(1,2)*t,
            lorentz_generator(2,3)*z,lorentz_generator(0,3)*y]
        E=s.Matrix.hstack(*[s.diff(X,c)+om[j]*X-X*s.diff(q,c)/(2*q)
                            for j,c in enumerate(coords)]).T
        self.assertEqual(s.simplify(E*eta*X),s.zeros(4,1))
        self.assertEqual(s.cancel(E.det()),0)

    def test_normal_euler_density_is_seen_by_weyl_compensation(self):
        X=s.Matrix([2,1,0,0]); e=s.eye(4)
        V=e.inv().T*X
        E=V*(eta*X).T
        self.assertNotEqual(s.simplify(s.trace(E.T*e)),0)
        self.assertEqual(s.simplify(s.trace(E.T*e)),(X.T*eta*X)[0])

    def test_omega_metric_rank_nine_and_weyl_gives_ten(self):
        X=s.Matrix([2,1,0,0]); e=s.eye(4)
        sympairs=list(itertools.combinations_with_replacement(range(4),2))
        columns=[]
        for mu in range(4):
            for a,b in itertools.combinations(range(4),2):
                D=s.zeros(4)
                D[mu,:]=(lorentz_generator(a,b)*X).T
                dg=D*eta*e.T+e*eta*D.T
                columns.append(s.Matrix([dg[i,j] for i,j in sympairs]))
        G=s.Matrix.hstack(*columns)
        dgW=2*e*eta*e.T
        col=s.Matrix([dgW[i,j] for i,j in sympairs])
        self.assertEqual(G.rank(),9)
        self.assertEqual(G.row_join(col).rank(),10)

    def test_common_central_cancels_but_relative_is_seen(self):
        X=s.Matrix([[1+s.I,2],[3,4-s.I]])
        c=s.symbols('c')
        self.assertEqual(c*s.eye(2)*X-X*c*s.eye(2),s.zeros(2))
        self.assertEqual((c*s.eye(2))*X-X*(-c*s.eye(2)),2*c*X)

if __name__=='__main__':
    unittest.main()
