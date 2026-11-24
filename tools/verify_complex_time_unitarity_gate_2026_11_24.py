#!/usr/bin/env python3
"""Conditional Cauchy-Riemann/compact-psi/unitary-time exact no-go tests.

Not a theorem about the on-shell UBT field: a quantum-state interpretation,
strong holomorphy and compact psi are all extra assumptions.
"""
import sympy as s


def analytic_periodic_fourier_forces_real_exponential_time():
    t, psi, R = s.symbols("t psi R", real=True, positive=True)
    for n in range(-3, 4):
        a = s.exp(s.Rational(n) * t / R)
        f = a * s.exp(s.I * n * psi / R)
        assert s.simplify(s.diff(f, psi) - s.I * s.diff(f, t)) == 0
        assert s.simplify(s.diff(a, t) - s.Rational(n) * a / R) == 0
        norm_sq = a**2
        assert s.simplify(s.diff(norm_sq, t) - 2*s.Rational(n)*norm_sq/R) == 0
        if n != 0:
            assert s.simplify(s.diff(norm_sq, t)) != 0
        assert s.simplify(f.subs(psi, psi + 2*s.pi*R) / f) == 1
    print("PASS: holomorphic imaginary-periodic modes have real-time exp(nt/R)")


def selfadjoint_generator_periodicity_obstruction():
    # Exact finite-dimensional sample for the spectral theorem argument.
    # L=log(2) >0, H self-adjoint with spectrum (0,2,-3).
    H = s.diag(0, 2, -3)
    L = s.log(2)
    expLH = s.diag(*[s.exp(L * H[j, j]) for j in range(3)])
    assert expLH == s.diag(1, 4, s.Rational(1, 8))
    periodicity_operator = expLH - s.eye(3)
    assert periodicity_operator.rank() == 2
    assert periodicity_operator.nullspace() == [s.Matrix([1, 0, 0])]
    for v in periodicity_operator.nullspace():
        assert H*v == s.zeros(3, 1)
    print("PASS: periodic exp(LH) implies zero-energy support in a selfadjoint comparator")


def holomorphic_jacobi_factor_not_compact_psi():
    t, psi, omega, L = s.symbols("t psi omega L", real=True, positive=True)
    f = s.exp(s.I * omega * t - omega * psi)
    assert s.simplify(s.diff(f, psi) - s.I*s.diff(f, t)) == 0
    assert s.simplify(f.subs(psi, psi + L)/f - s.exp(-omega*L)) == 0
    assert s.simplify(s.I*s.diff(f, t) + omega*f) == 0
    # If omega=pi*n**2, physical Schr. generator is negative unbounded.
    n = s.symbols("n", integer=True)
    assert s.simplify((-s.pi*n*n).subs(n, 10) + 100*s.pi) == 0
    print("PASS: Jacobi analytic damping breaks psi periodicity and has negative Schr sign")


def nonholomorphic_escape_witness():
    t, psi, R, E = s.symbols("t psi R E", real=True, positive=True)
    n = 2
    f = s.exp(-s.I*E*t + s.I*n*psi/R)
    assert s.simplify(s.I*s.diff(f,t) - E*f) == 0
    assert s.simplify(f.subs(psi,psi+2*s.pi*R)/f) == 1
    residual = s.simplify((s.diff(f,psi) - s.I*s.diff(f,t)) / f)
    assert residual == s.I*n/R-E
    assert residual != 0
    print("PASS: unitary periodic states exist without joint holomorphy")


if __name__ == "__main__":
    analytic_periodic_fourier_forces_real_exponential_time()
    selfadjoint_generator_periodicity_obstruction()
    holomorphic_jacobi_factor_not_compact_psi()
    nonholomorphic_escape_witness()
    print("SCOPE: conditional state-space no-go, NOT canonical single-Theta dynamics")
