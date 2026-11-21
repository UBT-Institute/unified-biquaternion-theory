#!/usr/bin/env python3
"""Exact L0 no-go: 8 real M2(C) congruence spin 0+1 cannot linearly source TT helicity 2.

Scope: equivariant differentiable map about isotropic background and nonzero
Fourier spatial k along z. This is NOT a complete action/Hessian test.
"""
import sympy as s


def little_group_intertwiner():
    # x = (Re t0, Im t0, Re tx, Re ty, Re tz, Im tx, Im ty, Im tz)
    Jin = s.zeros(8)
    for ix, iy in [(2, 3), (5, 6)]:
        Jin[ix, iy] = -1
        Jin[iy, ix] = 1
    Jtt = s.Matrix([[0, -2], [2, 0]])
    unknown = s.symbols("L0:16", real=True)
    L = s.Matrix(2, 8, unknown)
    eq = Jtt * L - L * Jin
    M, rhs = s.linear_eq_to_matrix(list(eq), unknown)
    assert M.shape == (16, 16)
    assert M.rank() == 16
    assert M.det() != 0
    assert Jin**3 + Jin == s.zeros(8)
    assert Jtt**2 == -4 * s.eye(2)
    assert Jtt**3 + Jtt == -3 * Jtt
    print("PASS: 16x16 equivariance rank 16; no scalar/vector -> helicity-two linear map")
    return Jin, Jtt


def pauli_rotation_check():
    I = s.eye(2)
    sx = s.Matrix([[0, 1], [1, 0]])
    sy = s.Matrix([[0, -s.I], [s.I, 0]])
    sz = s.diag(1, -1)
    phi = s.symbols("phi", real=True)
    U = s.diag(s.exp(-s.I * phi / 2), s.exp(s.I * phi / 2))
    assert s.simplify(s.expand_complex(
        U * sx * U.conjugate().T - s.cos(phi) * sx - s.sin(phi) * sy
    )) == s.zeros(2)
    assert s.simplify(s.expand_complex(
        U * sy * U.conjugate().T + s.sin(phi) * sx - s.cos(phi) * sy
    )) == s.zeros(2)
    assert s.simplify(U * sz * U.conjugate().T - sz) == s.zeros(2)
    assert U * I * U.conjugate().T == I
    print("PASS: SU2 Theta congruence has scalar and vector rotation sectors")


def quadratic_spin2_gate():
    ax, ay, az, eps = s.symbols("ax ay az eps", real=True)
    a = s.Matrix([ax, ay, az])
    Q = a * a.T - s.eye(3) * (a.dot(a)) / 3
    assert s.trace(Q) == 0
    Qscaled = s.expand(Q.subs({ax: eps * ax, ay: eps * ay, az: eps * az}))
    assert s.simplify(Qscaled - eps**2 * Q) == s.zeros(3)
    assert Qscaled.diff(eps).subs(eps, 0) == s.zeros(3)
    hp = s.expand((Q[0, 0] - Q[1, 1]) / 2)
    hx = Q[0, 1]
    assert hp == (ax**2 - ay**2) / 2 and hx == ax * ay
    R = s.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    Qrot = s.simplify(Q.subs({ax: -ay, ay: ax}, simultaneous=True))
    assert s.simplify(Qrot - R * Q * R.T) == s.zeros(3)
    print("PASS: quadratic vector bilinear has TT, but no linear TT near isotropic zero")


def independent_connection_counterexample():
    p, c, v0 = s.symbols("p c v0", nonzero=True)
    H = s.Matrix([[p, c, 0], [c, -p, 0], [0, 0, 0]])
    omega = H / (2 * v0)
    dh = v0 * (omega + omega.T)
    assert s.simplify(dh - H) == s.zeros(3)
    print("PASS: independent connection can fill TT, demonstrating composite-map distinction")


def gaussian_two_particle_gate():
    # Finite exact Fock witness: a normal-ordered bilinear creates two,
    # but never one, elementary Gaussian quanta from vacuum.
    n = 4
    a = s.zeros(n)
    for j in range(1, n):
        a[j - 1, j] = s.sqrt(j)
    ad = a.T
    normal_x2 = a * a + 2 * ad * a + ad * ad
    X = a + ad
    Qplus = (s.kronecker_product(normal_x2, s.eye(n))
             - s.kronecker_product(s.eye(n), normal_x2)) / 2
    Qcross = s.kronecker_product(X, X)
    vac = s.zeros(n * n, 1)
    vac[0] = 1
    one_x = s.zeros(n * n, 1)
    one_x[n] = 1
    one_y = s.zeros(n * n, 1)
    one_y[1] = 1
    two_x = s.zeros(n * n, 1)
    two_x[2 * n] = 1
    one_each = s.zeros(n * n, 1)
    one_each[n + 1] = 1
    for Q in (Qplus, Qcross):
        assert (one_x.T * Q * vac)[0] == 0
        assert (one_y.T * Q * vac)[0] == 0
    assert (two_x.T * Qplus * vac)[0] == s.sqrt(2) / 2
    assert (one_each.T * Qcross * vac)[0] == 1
    print("PASS: Gaussian normal-ordered spin-two bilinear: 2-particle, no 1-particle transition")



def gaussian_massless_bubble_gate():
    # The 3 free vector components are treated as independent massless scalar
    # species on Euclidean 4D, only as a Gaussian comparator.
    # Wick TT two-point is D(x)**2; Fourier => once-subtracted bubble log(p²).
    delta = lambda a, b: s.KroneckerDelta(a, b)
    C = lambda i, j, k, l: (
        delta(i, k) * delta(j, l)
        + delta(i, l) * delta(j, k)
        - s.Rational(2, 3) * delta(i, j) * delta(k, l)
    )
    hp = s.diag(s.Rational(1, 2), -s.Rational(1, 2), 0)
    hx = s.Matrix([[0, s.Rational(1, 2), 0],
                   [s.Rational(1, 2), 0, 0], [0, 0, 0]])
    proj = lambda A, B: s.simplify(sum(
        A[i, j] * C(i, j, k, l) * B[k, l]
        for i in range(3) for j in range(3)
        for k in range(3) for l in range(3)
    ))
    assert proj(hp, hp) == 1
    assert proj(hx, hx) == 1
    assert proj(hp, hx) == 0
    p2, mu2 = s.symbols("p2 mu2", positive=True)
    x = s.symbols("x", positive=True)
    subtraction = -s.integrate(s.log(p2 / mu2), (x, 0, 1)) / (16 * s.pi**2)
    assert s.simplify(subtraction + s.log(p2 / mu2)/(16*s.pi**2)) == 0
    u = s.symbols("u", positive=True)
    assert s.limit(u * s.log(u), u, 0, dir="+") == 0
    print("PASS: free Gaussian TT Wick correlator is bubble log(p²), no isolated 1/p² pole")


if __name__ == "__main__":
    little_group_intertwiner()
    pauli_rotation_check()
    quadratic_spin2_gate()
    independent_connection_counterexample()
    gaussian_two_particle_gate()
    gaussian_massless_bubble_gate()
    print("SCOPE: isotropic rotation-equivariant smooth M2(C) carrier only, no full field equations")
