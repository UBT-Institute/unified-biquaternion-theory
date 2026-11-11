# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""OI-4/OI-6: finite-information propagation limits and minimal Weyl algebra.

Reproduces standard mathematical identities; tests are not a derivation of
spacetime dimension, the physical speed of light or UBT dynamics.
Standard library only. From repository root:
python3 research_tracks/ontological_information_axioms/verify_diffusion_weyl.py
"""
from __future__ import annotations

from collections import defaultdict
from itertools import product
from math import cos, exp, pi, sqrt
import unittest


def add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))


def mul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def scale(a, c):
    return tuple(tuple(c * a[i][j] for j in range(2)) for i in range(2))


def determinant(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def matrix_close(a, b, tol=1e-10):
    return all(abs(a[i][j] - b[i][j]) < tol for i in range(2) for j in range(2))


IDENTITY = ((1 + 0j, 0j), (0j, 1 + 0j))
SIGMA_X = ((0j, 1 + 0j), (1 + 0j, 0j))
SIGMA_Y = ((0j, -1j), (1j, 0j))
SIGMA_Z = ((1 + 0j, 0j), (0j, -1 + 0j))
PAULI = (SIGMA_X, SIGMA_Y, SIGMA_Z)


def pauli_dot(momentum, velocity=1.0):
    result = scale(IDENTITY, 0)
    for coefficient, sigma in zip(momentum, PAULI):
        result = add(result, scale(sigma, velocity * coefficient))
    return result


def random_walk_2d(n):
    """Symmetric nearest-neighbor walk; n time steps on Z^2."""
    dist = {(0, 0): 1.0}
    for _ in range(n):
        nxt = defaultdict(float)
        for (x, y), probability in dist.items():
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nxt[(x + dx, y + dy)] += probability / 4
        dist = dict(nxt)
    return dist


def random_walk_characteristic(kx, ky, lattice_spacing):
    return (cos(kx * lattice_spacing) + cos(ky * lattice_spacing)) / 2


class InformationLimitTests(unittest.TestCase):
    def test_pauli_clifford_anticommutator(self):
        for i, a in enumerate(PAULI):
            for j, b in enumerate(PAULI):
                anti = add(mul(a, b), mul(b, a))
                expected = scale(IDENTITY, 2 if i == j else 0)
                self.assertTrue(matrix_close(anti, expected), (i, j))

    def test_two_component_weyl_cone_and_minkowski_determinant(self):
        for p in product(range(-2, 3), repeat=3):
            squared = sum(x * x for x in p)
            for velocity in (0.5, 1.0, 3.0):
                hamiltonian = pauli_dot(p, velocity)
                self.assertAlmostEqual(determinant(hamiltonian).real, -velocity**2 * squared)
                self.assertAlmostEqual(determinant(hamiltonian).imag, 0)
                for energy in (-3, -1, 0, 2):
                    matrix = add(scale(IDENTITY, energy), scale(hamiltonian, -1))
                    self.assertAlmostEqual(determinant(matrix).real, energy**2 - velocity**2 * squared)
                    self.assertAlmostEqual(determinant(matrix).imag, 0)

    def test_real_symmetric_two_component_carrier_has_at_most_two_axes(self):
        # Real symmetric traceless 2-by-2 matrices have basis X and Z.
        # No nonzero real symmetric candidate can anticommute with both.
        zero = scale(IDENTITY, 0)
        for ax, az in product(range(-2, 3), repeat=2):
            candidate = add(scale(SIGMA_X, ax), scale(SIGMA_Z, az))
            anti_x = add(mul(candidate, SIGMA_X), mul(SIGMA_X, candidate))
            anti_z = add(mul(candidate, SIGMA_Z), mul(SIGMA_Z, candidate))
            both_zero = matrix_close(anti_x, zero) and matrix_close(anti_z, zero)
            self.assertEqual(both_zero, ax == 0 and az == 0)

    def test_fourth_independent_pauli_direction_impossible_in_this_model(self):
        # Three traceless Hermitian 2x2 matrices identify vectors in real R^3.
        # Any putative fourth such matrix is in their real span.
        fourth = scale(
            add(add(SIGMA_X, SIGMA_Y), SIGMA_Z), 1 / sqrt(3)
        )
        overlaps = [mul(a, fourth)[0][0] + mul(a, fourth)[1][1] for a in PAULI]
        self.assertTrue(all(abs(overlap) > 0.1 for overlap in overlaps))
        # This example illustrates the obstruction; the proof is rank <= 3.

    def test_random_walk_normalization_variances_and_support(self):
        for n in range(1, 9):
            distribution = random_walk_2d(n)
            self.assertAlmostEqual(sum(distribution.values()), 1)
            self.assertAlmostEqual(sum(x * x * pr for (x, y), pr in distribution.items()), n / 2)
            self.assertAlmostEqual(sum(y * y * pr for (x, y), pr in distribution.items()), n / 2)
            self.assertTrue(all(abs(x) + abs(y) <= n for x, y in distribution))

    def test_diffusive_fourier_continuum_limit(self):
        # delta_t = a^2/(4D) and n=t/delta_t, with t=1, D=1.
        wave_vector = (0.4, 0.7)
        target = exp(-sum(k * k for k in wave_vector))
        errors = []
        for spacing in (0.5, 0.25, 0.125, 0.0625):
            dt = spacing**2 / 4
            n = round(1 / dt)
            characteristic = random_walk_characteristic(*wave_vector, spacing)
            approx = characteristic**n
            errors.append(abs(approx - target))
        self.assertTrue(all(errors[i + 1] < errors[i] for i in range(len(errors) - 1)))
        self.assertLess(errors[-1], 1e-4)

    def test_heat_kernel_instantaneously_nonzero_tail(self):
        diffusivity, t = 1.0, 1.0
        # Two-dimensional heat kernel is positive at arbitrary finite radius.
        for radius in (0.0, 2.0, 5.0, 10.0):
            gaussian = exp(-(radius**2) / (4 * diffusivity * t)) / (4 * pi * diffusivity * t)
            self.assertGreater(gaussian, 0)
        # Under diffusive scaling, the discrete maximal front speed diverges.
        velocities = [(a / (a * a / (4 * diffusivity))) for a in (0.5, 0.25, 0.125)]
        self.assertEqual(velocities, [8.0, 16.0, 32.0])

    def test_persistent_ballistic_paths_have_finite_support(self):
        # Rate-based flips in a telegrapher process also produce +/- v paths;
        # this enumeration checks the kinematic bound for finite sequences only.
        velocity, dt = 2.5, 0.1
        for n in range(1, 8):
            for velocity_signs in product((-1, 1), repeat=n):
                endpoint = velocity * dt * sum(velocity_signs)
                self.assertLessEqual(abs(endpoint), velocity * n * dt + 1e-12)


if __name__ == "__main__":
    unittest.main(verbosity=2)
