#!/usr/bin/env python3
"""Exact L0 gate: positive observer readout does not select Lorentz tetrad.

Scope: fixed inertial N=I, connection-free flat first jet; no claim about
on-shell UBT, the composite connection, or physical graviton dynamics.
"""
import sympy as sp


def matrix_gate():
    t, x, y, z = coords = sp.symbols("t x y z", real=True)
    unit = sp.eye(2)
    pauli = (
        unit,
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.diag(1, -1),
    )
    field = unit + sp.I * sum(
        (c * s for c, s in zip(coords, pauli)), sp.zeros(2)
    )
    sharp = lambda m: sp.trace(m) * unit - m
    frame = [sp.diff(field, c) for c in coords]
    eta = sp.diag(-1, 1, 1, 1)
    for mu in range(4):
        for nu in range(4):
            central = sp.expand(
                (sharp(frame[mu]) * frame[nu] +
                 sharp(frame[nu]) * frame[mu]) / 2
            )
            assert central == eta[mu, nu] * unit, (mu, nu)

    q = sp.simplify(field * field.conjugate().T)
    r2 = t*t + x*x + y*y + z*z
    v = x*pauli[1] + y*pauli[2] + z*pauli[3]
    assert sp.simplify(q - (1+r2)*unit - 2*t*v) == sp.zeros(2)
    rho = sp.simplify(q / sp.trace(q))
    assert sp.simplify(rho - unit/2 - t*v/(1+r2)) == sp.zeros(2)

    origin = {c: 0 for c in coords}
    assert rho.subs(origin) == unit/2
    for c in coords:
        assert sp.simplify(sp.diff(rho, c).subs(origin)) == sp.zeros(2)
    # Any fixed POVM probability tr(rho M) therefore has zero derivative:
    # the pullback of any regular quantum/classical information metric is zero.
    # The positive unnormalised intensity instead has Euclidean Hessian.
    intensity = sp.expand(sp.trace(q))
    assert sp.hessian(intensity, coords).subs(origin) == 4*sp.eye(4)
    assert 4*sp.eye(4) != 4*eta


def petz_nonuniqueness_gate():
    # Morozova-Chentsov normalization, X=sigma_x, rho=diag(3/4,1/4).
    # Both are known monotone quantum metrics; we test their distinct values.
    p, q = sp.Rational(3, 4), sp.Rational(1, 4)
    arith_mean = (p + q) / 2
    log_mean = (p-q) / (sp.log(p)-sp.log(q))
    sld = sp.simplify(2 / arith_mean)
    bkm = sp.simplify(2 / log_mean)
    assert sld == 4
    assert sp.simplify(bkm - 4*sp.log(3)) == 0
    assert sld != bkm


def lorentz_positive_cone_gate():
    a, b, c, d = sp.symbols("a b c d", real=True)
    unit = sp.eye(2)
    x1 = sp.Matrix([[0, 1], [1, 0]])
    x2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    x3 = sp.diag(1, -1)
    h = a*unit + b*x1 + c*x2 + d*x3
    assert sp.expand(h.det()) == a*a-b*b-c*c-d*d


if __name__ == "__main__":
    matrix_gate()
    petz_nonuniqueness_gate()
    lorentz_positive_cone_gate()
    print("PASS: exact Lorentz tetrad plus first-order observer-density blindness")
    print("PASS: unnormalized intensity has Euclidean Hessian, not Lorentz")
    print("PASS: SLD=4 differs from BKM=4*log(3) on the same qubit tangent")
    print("PASS: positive Hermitian matrix determinant has a Lorentz cone")
    print("Scope: off-shell finite-matrix L0 only; Lean and CI pending")
