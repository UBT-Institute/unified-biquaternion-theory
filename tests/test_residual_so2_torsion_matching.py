"""Exact Cartan contractions on the two-carrier residual connection."""

from itertools import combinations, permutations, product

import sympy as sp


SIGNATURE = (-1, 1, 1, 1)
ORIENTED_INDICES = tuple((indices, sp.LeviCivita(*indices)) for indices in permutations(range(4)))


def trace_and_axial(tensor):
    trace = sp.Matrix([
        sum(SIGNATURE[i] * tensor[i, i, j] for i in range(4))
        for j in range(4)
    ])
    axial = sp.zeros(4, 1)
    for (i, j, k, m), epsilon in ORIENTED_INDICES:
        axial[i] -= epsilon * tensor[j, k, m] / 6
    return trace, axial


def wedge_square(tensor):
    return sum(
        epsilon * SIGNATURE[i] * tensor[i, j, k] * tensor[i, m, n] / 4
        for (j, k, m, n), epsilon in ORIENTED_INDICES
        for i in range(4)
    )


def test_reference_torsion_and_five_residual_contractions():
    u22, u23, u33, n22, n23, n33, x2, x3, a, b, p2, p3 = sp.symbols(
        "u22 u23 u33 n22 n23 n33 x2 x3 a b p2 p3"
    )
    u_block = sp.Matrix([[u22, u23], [u23, u33]])
    n_block = sp.Matrix([[n22, n23], [n23, n33]])
    x = (x2, x3)
    alpha = (a, b, p2, p3)
    generator = sp.diag(sp.zeros(2), sp.Matrix([[0, 1], [-1, 0]]))

    # contortion[direction][output, input] has one index raised.
    contortion = [sp.zeros(4) for _ in range(4)]
    for i in (2, 3):
        contortion[i][1, 0] = contortion[i][0, 1] = -x[i - 2]
        contortion[1][i, 0] = contortion[1][0, i] = -x[i - 2]
        contortion[0][i, 1] = x[i - 2]
        contortion[0][1, i] = -x[i - 2]
        for j in (2, 3):
            contortion[j][i, 0] = contortion[j][0, i] = -u_block[i - 2, j - 2]
            contortion[j][i, 1] = -n_block[i - 2, j - 2]
            contortion[j][1, i] = n_block[i - 2, j - 2]

    def torsion(connection):
        return sp.ImmutableDenseNDimArray([
            SIGNATURE[i] * (connection[j][i, k] - connection[k][i, j])
            for i, j, k in product(range(4), repeat=3)
        ], (4, 4, 4))

    reference = torsion(contortion)
    shifted = torsion([piece + alpha[i] * generator for i, piece in enumerate(contortion)])
    for i, j, k in product(range(4), repeat=3):
        assert shifted[i, j, k] - reference[i, j, k] == (
            alpha[j] * generator[i, k] - alpha[k] * generator[i, j]
        )
        if i in (0, 1):
            assert reference[i, j, k] == 0
    for i, j in product((2, 3), repeat=2):
        assert reference[i, 0, j] == u_block[i - 2, j - 2]
        assert reference[i, 1, j] == n_block[i - 2, j - 2]
    assert [reference[i, 0, 1] for i in (2, 3)] == [2 * x2, 2 * x3]

    def invariants(tensor):
        norm = 0
        swap = 0
        for i, j, k in product(range(4), repeat=3):
            raised_sign = SIGNATURE[i] * SIGNATURE[j] * SIGNATURE[k]
            norm += raised_sign * tensor[i, j, k] ** 2
            swap += raised_sign * tensor[i, j, k] * tensor[k, j, i]

        trace, axial = trace_and_axial(tensor)
        return (
            norm, swap, trace.dot(sp.diag(*SIGNATURE) * trace), trace.dot(axial), wedge_square(tensor)
        )

    parallel_norm = -a**2 + b**2
    screen_norm = p2**2 + p3**2
    trace_u, trace_n = sp.trace(u_block), sp.trace(n_block)
    linear_longitudinal = trace_n * a - trace_u * b
    linear_screen = p2 * x2 + p3 * x3
    expected = (
        4 * parallel_norm + 2 * screen_norm,
        -2 * parallel_norm + screen_norm,
        screen_norm,
        sp.Rational(2, 3) * (linear_longitudinal + linear_screen),
        2 * (linear_longitudinal + 2 * linear_screen),
    )
    differences = tuple(sp.expand(v - v0) for v, v0 in zip(invariants(shifted), invariants(reference)))
    assert differences == tuple(sp.expand(value) for value in expected)


def test_odd_wedge_invariant_in_the_irreducible_basis():
    coefficients = iter(sp.symbols("t:24"))
    torsion = sp.MutableDenseNDimArray.zeros(4, 4, 4)
    for i in range(4):
        for j, k in combinations(range(4), 2):
            torsion[i, j, k] = next(coefficients)
            torsion[i, k, j] = -torsion[i, j, k]
    trace, axial = trace_and_axial(torsion)
    eta = sp.diag(*SIGNATURE)
    tensor_part = sp.ImmutableDenseNDimArray([
        torsion[i, j, k]
        - (eta[i, j] * trace[k] - eta[i, k] * trace[j]) / 3
        - sum(sp.LeviCivita(i, j, k, m) * axial[m] for m in range(4))
        for i, j, k in product(range(4), repeat=3)
    ], (4, 4, 4))
    assert sp.expand(wedge_square(torsion) - 2 * trace.dot(axial) - wedge_square(tensor_part)) == 0


def test_residual_stationary_solution_and_effective_density():
    long, screen, lam, mu, du, dn, x2, x3, a, b, p2, p3 = sp.symbols(
        "long screen lam mu du dn x2 x3 a b p2 p3"
    )
    components = (a, b, p2, p3)
    density = (
        long * (b**2 - a**2) + screen * (p2**2 + p3**2)
        + lam * (dn * a - du * b) + mu * (p2 * x2 + p3 * x3)
    )
    stationary = {
        a: lam * dn / (2 * long),
        b: lam * du / (2 * long),
        p2: -mu * x2 / (2 * screen),
        p3: -mu * x3 / (2 * screen),
    }
    assert sp.hessian(density, components) == 2 * sp.diag(-long, long, screen, screen)
    assert all(density.diff(q).subs(stationary) == 0 for q in components)
    assert sp.expand(density.subs(stationary)) == sp.expand(
        -lam**2 * (du**2 - dn**2) / (4 * long) - mu**2 * (x2**2 + x3**2) / (4 * screen)
    )
