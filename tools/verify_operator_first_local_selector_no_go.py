#!/usr/bin/env python3
"""Exact SymPy checks for a local Lorentz stabilizer connection-selector obstruction.

The numerical background is an exact rational representative of a general
analytic residual-gauge argument. Passing does not prove a UBT field equation.
"""

# UBT-AI-PROVENANCE-BEGIN
# schema: ubt-ai-provenance/v1
# tier: B_machine_verified
# ai_assistance: disclosed
# human_review: machine-verified
# editorial_responsibility: Ing. David Jaroš
# policy: ../AI_PROVENANCE.md
# notice: The script checks only the finite-dimensional identities encoded here.
# UBT-AI-PROVENANCE-END

import sympy as sp


def zero_matrix(matrix):
    return all(sp.cancel(value) == 0 for value in matrix)


def main():
    t, x, y, z = sp.symbols('t x y z', real=True)
    eta = sp.diag(-1, 1, 1, 1)
    v = sp.Matrix([2 + t, x, y, z])
    q = (v.T * eta * v)[0]
    assert q.subs({t: 0, x: 0, y: 0, z: 0}) == -4

    p = sp.eye(4) - v * (v.T * eta) / q
    j = sp.zeros(4)
    j[1, 2], j[2, 1] = 1, -1
    h_generator = p * j * p

    assert zero_matrix(p * p - p), 'orthogonal projector identity'
    assert zero_matrix(p * v), 'projector must kill V'
    assert zero_matrix(h_generator * v), 'residual generator must kill V'
    assert zero_matrix(h_generator.T * eta + eta * h_generator), 'Lorentz skewness'

    origin = {t: 0, x: 0, y: 0, z: 0}
    assert h_generator.subs(origin) == j

    # Let h(x) = exp(x * H(x)); exact H(x) V(x) = 0 implies
    # h(x) V(x) = V(x) and the entire ordinary V jet is unchanged.
    # At the origin h(0)=I, d_x h(0)=J. Therefore a gauge-covariant
    # connection must transform 0 -> -J dx at that point, although V,
    # dV and e(p)=I are the same. No pointwise F(V,dV,e) can do both.
    derivative_h_at_origin = h_generator.subs(origin)
    assert derivative_h_at_origin == j
    assert derivative_h_at_origin != sp.zeros(4)

    # Independent algebraic check: the Lorentz Lie algebra has dimension 6;
    # for timelike V=(2,0,0,0), A |-> A V has rank 3 and nullity 3.
    basis = []
    for a in range(4):
        for b in range(a + 1, 4):
            n = sp.zeros(4)
            n[a, b], n[b, a] = 1, -1
            basis.append(eta.inv() * n)
    v0 = v.subs(origin)
    selection = sp.Matrix.hstack(*(a * v0 for a in basis))
    assert selection.shape == (4, 6)
    assert selection.rank() == 3
    assert 4 * (len(basis) - selection.rank()) == 12

    print('PASS: exact Lorentz projector and residual generator identities')
    print('PASS: pointwise residual gauge jet mismatch at the origin')
    print('PASS: rank=3, stabilizer nullity=3 per direction, 12 total')
    print('SymPy:', sp.__version__)
    print('LEAN-PENDING: analytic no-selector theorem not formally compiled')


if __name__ == '__main__':
    main()
