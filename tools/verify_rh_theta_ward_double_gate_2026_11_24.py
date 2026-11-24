#!/usr/bin/env python3
"""Exact model-level Ward/locality/TT-access gates for RH-inspired UBT.

4D Euclidean principal-symbol comparator, not a selected UBT action.
No inference from this script to the full quantum gravity constraint algebra.
"""
import sympy as s

D = 4
I = s.eye(D)


def kernel(H, p, a, b, c, d, e):
    p2 = p.dot(p)
    hp = H * p
    return (a * p2 * H + b * (p * hp.T + hp * p.T)
            + c * p * p.T * s.trace(H)
            + d * I * (p.T * H * p)[0]
            + e * I * p2 * s.trace(H))


def spin2_projection(H, p):
    p2 = p.dot(p)
    assert p2 != 0
    t = I - p * p.T / p2
    return s.simplify(t * H * t - t * s.trace(t * H) / (D - 1))


def test_selfadjointness_and_ward_select_fp():
    a, b, c, d, e = s.symbols('a b c d e')
    mom = I[:, 0]
    h1, h2 = I, mom * mom.T
    defect = s.expand(s.trace(h1 * kernel(h2, mom, a, b, c, d, e))
                      - s.trace(kernel(h1, mom, a, b, c, d, e) * h2))
    assert s.expand(defect + 3 * (c - d)) == 0
    # Symmetry of a real quadratic Hessian imposes c=d.
    eqs = []
    for xi in (I[:, 0], I[:, 1]):
        gauge = mom * xi.T + xi * mom.T
        eqs.extend(kernel(gauge, mom, a, b, c, c, e))
    assert s.linsolve(eqs, (b, c, e)) == s.FiniteSet((-a, a, -a))
    p = s.Matrix(s.symbols('p0:4', real=True))
    xi = s.Matrix(s.symbols('xi0:4', real=True))
    pure_gauge = p * xi.T + xi * p.T
    fp = s.simplify(kernel(pure_gauge, p, 1, -1, 1, 1, -1))
    assert fp == s.zeros(D)
    transverse_traceless = s.diag(1, -1, 0, 0)
    k_z = s.Matrix([0, 0, 0, 1])
    assert kernel(transverse_traceless, k_z, 1, -1, 1, 1, -1) == transverse_traceless
    print('PASS: local selfadjoint 2-derivative Ward kernel unique up to scale')


def test_no_local_analytic_mass_term():
    m, n = s.symbols('m n')
    mom = I[:, 0]
    eqs = []
    for xi in (I[:, 0], I[:, 1]):
        gauge = mom * xi.T + xi * mom.T
        eqs.extend(m * gauge + n * I * s.trace(gauge))
    assert s.linsolve(eqs, (m, n)) == s.FiniteSet((0, 0))
    print('PASS: local momentum-independent symmetric rank-two mass terms forbidden')


def test_transverse_ward_alone_not_mass_protection():
    p = s.Matrix([1, 2, 3, 4])
    xi = s.Matrix(s.symbols('xi0:4'))
    assert spin2_projection(p*xi.T + xi*p.T, p) == s.zeros(D)
    q = s.Matrix(4, 4, lambda i, j: s.Symbol(f'h{min(i,j)}{max(i,j)}'))
    assert s.simplify(spin2_projection(spin2_projection(q, p), p)
                      - spin2_projection(q, p)) == s.zeros(D)
    # P2 has k-dependent 1/k^2,1/k^4 pieces and has NO analytic k=0 value.
    H = I[:, 0] * I[:, 0].T
    assert spin2_projection(H, I[:, 0]) == s.zeros(D)
    assert spin2_projection(H, I[:, 1]) != s.zeros(D)
    # P2 is an off-shell transverse traceless rank-5 projector in 4D,
    # not the two physical on-shell helicities of a massless graviton.
    basis = []
    for i in range(D):
        for j in range(i, D):
            b = s.zeros(D)
            b[i, j] = 1
            b[j, i] = 1
            basis.append(b)
    projective_matrix = s.Matrix.hstack(*[s.Matrix(list(spin2_projection(b, I[:, 0])))
                                       for b in basis])
    assert projective_matrix.rank() == 5
    print('PASS: nonlocal m^2 P2 satisfies Ward but gives massive TT inverse kernel')


def test_quadratic_theta_composite_has_no_linear_diff_lift():
    a = s.Matrix(s.symbols('a0:3', real=True))
    Q = a*a.T - s.eye(3) * a.dot(a) / 3
    at_zero = {a[i]: 0 for i in range(3)}
    for z in Q:
        for aj in a:
            assert s.simplify(s.diff(z, aj).subs(at_zero)) == 0
    # The required inhomogeneous gauge fluctuation is nonzero for generic p,xi.
    p = s.Matrix([1, 0, 0, 0]); xi = s.Matrix([0, 1, 0, 0])
    assert p*xi.T + xi*p.T != s.zeros(D)
    # Even a true diffeo-covariant pullback from four affine scalars has only
    # pure-gradient metric perturbations (and no independent TT image).
    assert spin2_projection(p*xi.T + xi*p.T, p) == s.zeros(D)
    print('PASS: isotropic quadratic composite has no smooth linear metric gauge lift')


if __name__ == '__main__':
    test_selfadjointness_and_ward_select_fp()
    test_no_local_analytic_mass_term()
    test_transverse_ward_alone_not_mass_protection()
    test_quadratic_theta_composite_has_no_linear_diff_lift()
    print('SCOPE: exact local/nonlocal toy Ward selection; UBT dynamics OPEN')
