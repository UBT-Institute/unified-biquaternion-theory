"""Exact finite checks for the scoped MacDowell–Mansouri circle obstruction."""

from itertools import combinations

import pytest
import sympy as sp

from tools.verify_fifth_channel_macdowell_mansouri import canonical_gammas


def boost_constraint_rank(basis, boosts):
    dimension = basis[0].rows
    columns = [
        sp.Matrix.vstack(*[
            (boost * generator - generator * boost).reshape(dimension**2, 1)
            for boost in boosts
        ])
        for generator in basis
    ]
    return sp.Matrix.hstack(*columns).rank()


@pytest.mark.parametrize("epsilon", [1, -1])
def test_five_vector_lorentz_centralizer(epsilon):
    signature = (-1, 1, 1, 1, epsilon)
    generators = {}
    for a, b in combinations(range(5), 2):
        generator = sp.zeros(5)
        generator[a, b] = 1
        generator[b, a] = -signature[a] * signature[b]
        generators[a, b] = generator
    boosts = [generators[0, i] for i in (1, 2, 3)]
    assert boost_constraint_rank(list(generators.values()), boosts) == 10


@pytest.mark.parametrize("epsilon", [1, -1])
def test_clifford_lorentz_centralizer(epsilon):
    gammas, grading = canonical_gammas()
    gamma_psi = grading if epsilon == 1 else sp.I * grading
    lorentz = {
        (a, b): gammas[a] * gammas[b] / 2
        for a, b in combinations(range(4), 2)
    }
    translations = [gamma * gamma_psi / 2 for gamma in gammas]
    boosts = [lorentz[0, i] for i in (1, 2, 3)]
    assert boost_constraint_rank([*lorentz.values(), *translations], boosts) == 10
    assert all(boost * gamma_psi == gamma_psi * boost for boost in boosts)


def test_curvature_pullback_on_a_noncommuting_spacetime_connection():
    x, y, psi, new_psi = sp.symbols("x y psi psi_prime", real=True)
    radius, new_radius = sp.symbols("R R_prime", positive=True)
    gammas, grading = canonical_gammas()

    def curvature(angle):
        a_x = y * sp.cos(angle) * gammas[0] * gammas[1]
        a_y = x * sp.sin(angle) * gammas[1] * grading
        return a_y.diff(x) - a_x.diff(y) + a_x * a_y - a_y * a_x

    original = curvature(psi / radius)
    rescaled = original.subs(psi, radius * new_psi / new_radius)
    assert rescaled == curvature(new_psi / new_radius)
    assert original != sp.zeros(4)


def test_normalized_circle_gradient_depends_on_beta_over_radius_squared():
    psi = sp.symbols("psi", real=True)
    radius, beta, scale = sp.symbols("R beta lambda", positive=True)
    n = sp.symbols("n", integer=True, positive=True)
    mode = sp.exp(sp.I * n * psi / radius)
    gradient = mode.diff(psi)
    energy = sp.integrate(beta * gradient.conjugate() * gradient, (psi, 0, 2 * sp.pi * radius))
    energy = sp.simplify(energy / (2 * sp.pi * radius))
    assert energy == beta * n**2 / radius**2
    assert energy.subs({radius: scale * radius, beta: scale**2 * beta}) == energy
