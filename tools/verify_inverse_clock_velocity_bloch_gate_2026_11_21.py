#!/usr/bin/env python3
"""Exact conditional geometry bridge: observer-clock velocity -> Bloch radius.

This is an algebraic/geometric comparator on the canonical Lorentz-real tetrad,
NOT the operational density rho_N[Theta] nor a microscopic UBT action.
"""
import sympy as sp

I = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.diag(1, -1)


def X(v):
    return v[0]*I + v[1]*SX + v[2]*SY + v[3]*SZ


def test_clock_velocity_spectrum():
    u = [sp.Rational(5, 4), sp.Rational(3, 4), 0, 0]
    v = [sp.Rational(5, 3), 0, sp.Rational(4, 3), 0]
    N, V = X(u), X(v)
    assert N.det() == V.det() == 1
    A = sp.simplify(N.inv() * V)  # similar to Hermitian whitening
    gamma = sp.simplify(sp.trace(A)/2)
    assert gamma == sp.Rational(25, 12)
    assert A.det() == 1
    q = A / sp.trace(A)
    beta = sp.sqrt(1 - 1/gamma**2)
    assert sp.simplify(q.det() - (1-beta**2)/4) == 0
    assert sp.simplify(beta - sp.sqrt(481)/25) == 0

    # Simultaneous Lorentz congruence preserves spectrum/relative speed.
    S = sp.diag(2, sp.Rational(1, 2))
    Ap = (S*N*S.T).inv() * (S*V*S.T)
    assert sp.simplify(sp.trace(Ap) - sp.trace(A)) == 0
    assert sp.simplify(Ap.det() - A.det()) == 0


def test_null_pure_and_comoving_mixed():
    u = [1, 0, 0, 0]
    N = X(u)
    assert N == I
    assert sp.simplify((X(u)/sp.trace(X(u))) - I/2) == sp.zeros(2)
    vnull = [1, 1, 0, 0]
    q = X(vnull)/sp.trace(X(vnull))
    assert q.det() == 0
    assert sp.simplify(q*q - q) == sp.zeros(2)
    # This geometric velocity density is not generally the chosen rho_N[Theta].
    # At origin Theta=I, the latter equals I/2 irrespective of the tangent v.
    vtimelike = [sp.Rational(5,4), sp.Rational(3,4), 0, 0]
    assert X(vtimelike)/sp.trace(X(vtimelike)) != I/2


def test_qfi_klein_conformal_factor():
    x, y, z = sp.symbols('x y z', real=True)
    r = sp.Matrix([x, y, z])
    r2 = x*x + y*y + z*z
    # SLD-QFI normalization = 4*Bures.
    g_qfi = sp.eye(3) + r*r.T/(1-r2)
    g_bk = sp.eye(3)/(1-r2) + r*r.T/(1-r2)**2
    assert sp.simplify(g_bk - g_qfi/(1-r2)) == sp.zeros(3)

    # Independent SLD checks at the diagonal qubit rho=(I+z SZ)/2.
    # The radial probability FI is 1/(1-z^2); tangential SLD-QFI is 1.
    diag = {x: 0, y: 0}
    assert sp.simplify(g_qfi[0,0].subs(diag)) == 1
    assert sp.simplify(g_qfi[2,2].subs(diag) - 1/(1-z*z)) == 0
    assert sp.simplify(g_bk[2,2].subs(diag) - 1/(1-z*z)**2) == 0


if __name__ == '__main__':
    test_clock_velocity_spectrum()
    test_null_pure_and_comoving_mixed()
    test_qfi_klein_conformal_factor()
    print('PASS: clock-covariant geometric Bloch spectrum encodes relative speed')
    print('PASS: geometric null = pure; comoving = maximally mixed')
    print('PASS: Beltrami-Klein = gamma^2 * SLD-QFI (4 Bures)')
    print('Scope: kinematic/off-shell comparator; no UBT action, Hamiltonian or detector derived')
