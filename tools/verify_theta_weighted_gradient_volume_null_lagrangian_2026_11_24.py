#!/usr/bin/env python3
"""Exact restricted null-Lagrangian and algebraic contortion comparators.

Four-real flat pure-gradient UBT branch only: E^a_mu = partial_mu Y^a.
Nothing here identifies a microscopic action of the full single complex Theta.
"""
import sympy as s


def jacobian_identity_and_zero_velocity_hessian():
    v = s.symbols('v0:4', real=True)
    spatial = s.symbols('sp0:12', real=True)
    J = s.Matrix(4, 4, lambda a, mu: v[a] if mu == 0
                 else spatial[3*a + mu - 1])
    cof = J.adjugate().T
    det = J.det()
    assert s.simplify(cof * J.T - det*s.eye(4)) == s.zeros(4)
    assert s.simplify(J.T * cof - det*s.eye(4)) == s.zeros(4)
    f = s.symbols('f')  # f(Y) has no velocity dependence in this branch
    L = f*det
    assert s.hessian(L, v) == s.zeros(4)
    assert all(not s.diff(L, v[a]).has(v[b])
               for a in range(4) for b in range(4))
    print('PASS: generic 4x4 Jacobian/cofactor algebra, zero velocity Hessian')


def nonlinear_four_real_piola_weighted_euler():
    t,x,y,z = s.symbols('t x y z', real=True)
    a,b,c,d = s.symbols('a b c d', real=True)
    coord = (t,x,y,z)
    Y = s.Matrix([t+a*x*y, x+b*t*z, y+c*x*z, z+d*t*y])
    J = Y.jacobian(coord)
    cof = J.adjugate().T
    det = J.det()
    assert all(s.simplify(sum(s.diff(cof[A,mu],coord[mu])
                              for mu in range(4))) == 0 for A in range(4))
    f = s.exp(Y[0])+Y[1]*Y[2]+Y[3]**2
    partial = (s.exp(Y[0]), Y[2], Y[1], 2*Y[3])
    for A in range(4):
        EL = s.simplify(partial[A]*det-sum(
            s.diff(f*cof[A,mu],coord[mu]) for mu in range(4)))
        assert EL == 0, (A, EL)
    print('PASS: nonaffine Y and nonconstant f(Y): all 4 Euler equations zero')


def algebraic_contortion_source_selection():
    q,v,K,m,alpha = s.symbols('q v K m alpha',real=True,nonzero=True)
    J = s.Function('J')(q)
    M = s.Function('M')(q)
    L = J*K+s.Rational(1,2)*M*K**2
    stationary = s.solve(s.diff(L,K),K)[0]
    assert stationary == -J/M
    reduced = s.simplify(L.subs(K,stationary))
    assert reduced == -J**2/(2*M)
    assert s.diff(reduced,v,2) == 0
    # A freely introduced velocity source can change the quadratic energy
    # and its sign; no unique physical torsion selector is established.
    L_v = alpha*v*K+s.Rational(1,2)*m*K**2
    K_star = s.solve(s.diff(L_v,K),K)[0]
    L_red = s.simplify(L_v.subs(K,K_star))
    assert s.simplify(s.diff(L_red,v,2)+alpha**2/m) == 0
    assert s.diff(L_red,v,2).subs({m:1,alpha:1}) == -1
    assert s.diff(L_red,v,2).subs({m:-1,alpha:1}) == 1
    print('PASS: velocity-free torsion source no Hessian; derivative sign unselected')


if __name__=='__main__':
    jacobian_identity_and_zero_velocity_hessian()
    nonlinear_four_real_piola_weighted_euler()
    algebraic_contortion_source_selection()
    print('SCOPE: restricted pure-gradient sector; full UBT dynamics OPEN')
