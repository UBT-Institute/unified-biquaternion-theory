"""Exact Clifford parity / biquaternion adjugate spectral gate.

Finite-dimensional algebra only; no physical UBT action or boson/fermion
statistics derived.
"""
import sympy as sp


def matrices():
    z0, z1, z2, z3, lam = sp.symbols("z0 z1 z2 z3 lam")
    q = sp.Matrix([[z0 + z3, z1 - sp.I*z2],
                   [z1 + sp.I*z2, z0 - z3]])
    sharp = sp.Matrix([[z0 - z3, -z1 + sp.I*z2],
                       [-z1 - sp.I*z2, z0 + z3]])
    d = sp.zeros(4)
    d[:2, 2:] = q
    d[2:, :2] = sharp
    delta = z0**2 - z1**2 - z2**2 - z3**2
    return q, sharp, d, delta, lam


def test_biquaternion_adjugate_and_doubled_spectrum():
    q, sharp, d, delta, lam = matrices()
    assert sp.simplify(q*sharp - delta*sp.eye(2)) == sp.zeros(2)
    assert sp.simplify(sharp*q - delta*sp.eye(2)) == sp.zeros(2)
    assert sp.simplify(d*d - delta*sp.eye(4)) == sp.zeros(4)
    assert sp.simplify(d.charpoly(lam).as_expr() - (lam**2-delta)**2) == 0


def test_clifford_grading_anticommutes():
    _, _, d, _, _ = matrices()
    j = sp.diag(1, 1, -1, -1)
    assert j*d + d*j == sp.zeros(4)


def test_explicit_eigenvectors():
    _, sharp, d, delta, lam = matrices()
    for u in (sp.Matrix([1, 0]), sp.Matrix([0, 1])):
        psi = u.col_join(sharp*u/lam)
        residual = (d - lam*sp.eye(4))*psi
        assert sp.simplify(residual[2:4, 0]) == sp.zeros(2, 1)
        assert sp.simplify(residual[:2, 0] -
                           (delta-lam**2)*u/lam) == sp.zeros(2, 1)


def test_nilpotent_nonzero_null_cone():
    _, _, d, delta, _ = matrices()
    witness = {sp.Symbol("z0"): 1, sp.Symbol("z1"): 1,
               sp.Symbol("z2"): 0, sp.Symbol("z3"): 0}
    dw = d.subs(witness)
    assert delta.subs(witness) == 0
    assert dw != sp.zeros(4)
    assert dw*dw == sp.zeros(4)
    assert dw.rank() == 2
