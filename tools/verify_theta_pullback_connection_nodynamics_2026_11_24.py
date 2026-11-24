#!/usr/bin/env python3
"""Exact restricted pullback axial-connection/torsion no-dynamics checks.

A nonzero local Lorentz connection curvature/torsion need not provide bulk
dynamics if all geometric data pull back from a fixed 4D target via Y(x).
This is not the full eight-real UBT theory or a selected torsion law.
"""
import sympy as s


def axial_stabilizer_and_torsion():
    Y = s.Matrix(s.symbols('Y0:4', real=True))
    lam = s.symbols('lam', real=True)
    signs = (1, -1, -1, -1)
    eta = s.diag(*signs)
    norm = sum(signs[a]*Y[a]**2 for a in range(4))
    # C^a_b = A_d^a_b(Y) dY^d, epsilon_0123=+1
    A = [
        s.Matrix(4, 4, lambda a, b:
                 signs[a]*lam*sum(s.LeviCivita(a, b, c, d)*Y[c]
                                  for c in range(4))/norm)
        for d in range(4)
    ]
    for D in A:
        assert s.simplify(norm*D*Y) == s.zeros(4, 1)
        assert s.simplify((eta*D).T + eta*D) == s.zeros(4)
    torsion = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                torsion[a, b, c] = s.cancel(A[b][a,c]-A[c][a,b])
                expected = (
                    2*signs[a]*lam
                    *sum(s.LeviCivita(a,b,c,d)*Y[d] for d in range(4))
                    / norm
                )
                assert s.simplify(torsion[a,b,c]-expected)==0
    invariant = s.factor(sum(
        signs[a]*signs[b]*signs[c]*torsion[a,b,c]**2
        for a in range(4) for b in range(4) for c in range(4)
    ))
    assert s.simplify(invariant+24*lam**2/norm)==0
    print('PASS exact stabilizer connection and nonzero axial T_abc T^abc')
    return Y, lam, norm, A


def curved_connection_with_flat_locked_metric():
    Y, lam, norm, A = axial_stabilizer_and_torsion()
    r = s.symbols('r', positive=True)
    at_rest = {Y[0]: r, Y[1]: 0, Y[2]: 0, Y[3]: 0}
    # F_12^1{}_2: partial_1 A_2 - partial_2 A_1 + [A_1,A_2].
    derivative = s.diff(A[2][1,2],Y[1])-s.diff(A[1][1,2],Y[2])
    assert derivative == 0
    comm = A[1]*A[2]-A[2]*A[1]
    assert s.simplify(comm[1,2].subs(at_rest)+lam**2/r**2)==0
    print('PASS F_12^1{}_2=-lam^2/r^2, while E=dY and g=Y*eta')


def pullback_torsion_action_zero_bulk_euler():
    t,x,y,z,a,b,lam = s.symbols('t x y z a b lam', real=True)
    coord = (t,x,y,z)
    Y = s.Matrix([t+a*x*x, x+b*t*t, y, z])
    J = Y.jacobian(coord)
    jac_det = s.factor(J.det())
    norm = Y[0]**2-Y[1]**2-Y[2]**2-Y[3]**2
    f = -24*lam**2/norm
    cof = J.adjugate().T
    u = s.symbols('u0:4', real=True)
    symbolic_f = -24*lam**2/(u[0]**2-u[1]**2-u[2]**2-u[3]**2)
    for i in range(4):
        assert s.simplify(sum(
            s.diff(cof[i,mu],coord[mu]) for mu in range(4))) == 0
        f_i = s.diff(symbolic_f,u[i]).subs(dict(zip(u,Y)))
        euler = s.factor(f_i*jac_det-sum(
            s.diff(f*cof[i,mu],coord[mu]) for mu in range(4)))
        assert euler == 0, (i,euler)
    velocities=s.symbols('v0:4',real=True)
    spatial=s.symbols('s0:12',real=True)
    general_J=s.Matrix(4,4,lambda a,mu:
                       velocities[a] if mu==0 else spatial[3*a+mu-1])
    assert s.hessian(s.Symbol('f')*general_J.det(),velocities)==s.zeros(4)
    print('PASS nonaffine Y, nonconstant torsion action: all Euler equations and Hessian vanish')


if __name__ == '__main__':
    axial_stabilizer_and_torsion()
    curved_connection_with_flat_locked_metric()
    pullback_torsion_action_zero_bulk_euler()
    print('SCOPE: target-pullback-only geometry; full eight-real Theta dynamics OPEN')
