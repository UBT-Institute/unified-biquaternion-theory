"""Grade automorphism vs physical field-only flip and fermion parity.

Small symbolic sign identities; no claim of microscopic UBT symmetry selection.
"""
import sympy as sp


def grade_sign(grade):
    return (-1) ** grade


def test_clifford_grade_is_algebra_automorphism():
    for i in range(5):
        for j in range(5):
            assert grade_sign(i + j) == grade_sign(i) * grade_sign(j)


def test_bivector_from_derivative_and_vector_is_grade_even():
    # D has geometric grade 1 and V has geometric grade 1.
    # Their exterior product has grade 2, hence unchanged by full alpha.
    assert grade_sign(1) * grade_sign(1) == grade_sign(2) == 1


def test_field_only_flip_changes_mixed_term():
    b, d, v = sp.symbols("b d v")
    term = b*d*v
    assert sp.expand(term.subs(v, -v) + term) == 0
    assert sp.expand(term.subs({d: -d, v: -v}) - term) == 0


def test_fermion_parity_preserves_bilinear_vector_coupling():
    e, psi_bar, gamma, gauge, psi = sp.symbols(
        "e psi_bar gamma gauge psi", commutative=True
    )
    term = -e*psi_bar*gamma*gauge*psi
    assert sp.expand(term.subs({psi: -psi, psi_bar: -psi_bar}) - term) == 0
    assert sp.expand(term.subs(gauge, -gauge) + term) == 0
