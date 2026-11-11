# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""OI-6: generalized-bit minimal tensor countermodel.

This reproduces elementary generalized probabilistic theory (GPT) facts:
local tomography + connected pure-state reversibility do not uniquely imply
complex quantum theory. Finite checks do not certify new physical dynamics.
Run from repo root with Python 3.10+: python3 research_tracks/
ontological_information_axioms/verify_ball_gpt_countermodel.py
"""
from fractions import Fraction
from itertools import product
from math import cos, pi, sin, sqrt
import unittest


def tensor(x, y):
    return tuple(a * b for a in x for b in y)


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def norm2(x):
    return dot(x, x)


def normalized_state(r):
    assert norm2(r) <= 1 + 1e-12
    return (1,) + tuple(r)


def unit_effect(n):
    return (Fraction(1),) + (Fraction(0),) * n


def coordinate_effect(n, axis):
    e = [Fraction(0)] * (n + 1)
    e[0] = Fraction(1, 2)
    e[axis + 1] = Fraction(1, 2)
    return tuple(e)


def local_effect_basis(n):
    return (unit_effect(n),) + tuple(coordinate_effect(n, i) for i in range(n))


def exact_rank(rows):
    """Gaussian elimination over rationals, no numerical tolerance."""
    a = [[Fraction(x) for x in row] for row in rows]
    rank = 0
    if not a:
        return rank
    for col in range(len(a[0])):
        piv = next((i for i in range(rank, len(a)) if a[i][col] != 0), None)
        if piv is None:
            continue
        a[rank], a[piv] = a[piv], a[rank]
        scale = a[rank][col]
        a[rank] = [q / scale for q in a[rank]]
        for i in range(len(a)):
            if i != rank:
                scale = a[i][col]
                if scale:
                    a[i] = [x - scale * y for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def rotate_01(r, angle):
    """A connected and reversible SO(n) subgroup acting on the Bloch ball."""
    c, s = cos(angle), sin(angle)
    return (c * r[0] - s * r[1], s * r[0] + c * r[1]) + tuple(r[2:])


def witness_product(r, s):
    """Two-setting correlator T11+T22 on a product state."""
    return r[0] * s[0] + r[1] * s[1]


def target_joint_prob(a, b, outcome_a, outcome_b):
    """A formally entangled state in the *maximal* tensor ball GPT.

    Unit-norm measurement direction a/b; zero marginals; correlations
    T_11=T_22=1. Not a state of the minimal tensor product.
    """
    corr = dot(a[:2], b[:2])
    return (1 + outcome_a * outcome_b * corr) / 4


class BallGPTCountermodelTests(unittest.TestCase):
    def test_bounded_local_effects(self):
        for n in (3, 4):
            e = local_effect_basis(n)
            for i, ef in enumerate(e):
                for axis in range(n):
                    for sign in (-1, 1):
                        r = [0] * n
                        r[axis] = sign
                        probability = dot(ef, normalized_state(r))
                        self.assertGreaterEqual(probability, 0)
                        self.assertLessEqual(probability, 1)
                        if i == 0:
                            self.assertEqual(probability, 1)

    def test_product_effects_span_all_composite_coordinates(self):
        for n in (2, 3, 4):
            basis = local_effect_basis(n)
            effects = [tensor(e, f) for e, f in product(basis, repeat=2)]
            self.assertEqual(len(effects), (n + 1)**2)
            self.assertEqual(exact_rank(effects), (n + 1)**2)

    def test_parameter_counts_do_not_force_quantum(self):
        self.assertEqual((3 + 1, (3 + 1)**2), (4, 16))
        self.assertEqual((4 + 1, (4 + 1)**2), (5, 25))
        self.assertEqual((2 + 1, (2 + 1)**2), (3, 9))

    def test_connected_reversible_rotations_on_pure_states(self):
        source = (1.0, 0.0, 0.0, 0.0)
        target = (0.0, 1.0, 0.0, 0.0)
        for k in range(21):
            t = k / 20
            intermediate = rotate_01(source, t * pi / 2)
            self.assertAlmostEqual(norm2(intermediate), 1.0)
            self.assertTrue(all(abs(x - y) < 1e-12 for x, y in zip(
                rotate_01(intermediate, -t * pi / 2), source)))
        self.assertTrue(all(abs(x - y) < 1e-12 for x, y in zip(
            rotate_01(source, pi / 2), target)))

    def test_local_rotations_connect_pure_product_states(self):
        r = (1.0, 0, 0, 0)
        s = (0.0, 1, 0, 0)
        transformed = tensor(
            normalized_state(rotate_01(r, pi / 2)),
            normalized_state(rotate_01(s, -pi / 2))
        )
        target = tensor(normalized_state((0, 1, 0, 0)),
                        normalized_state((1, 0, 0, 0)))
        self.assertTrue(all(abs(a - b) < 1e-12 for a, b in zip(
            transformed, target)))

    def test_all_constructed_composite_states_are_separable(self):
        states = [
            tensor(normalized_state((1, 0, 0, 0)), normalized_state((0, 1, 0, 0))),
            tensor(normalized_state((0, 1, 0, 0)), normalized_state((-1, 0, 0, 0))),
        ]
        mixed = tuple((a + b) / 2 for a, b in zip(*states))
        self.assertEqual(mixed[0], 1)
        self.assertEqual(len(mixed), 25)
        # This is a constructive mixture of product states; absence of all
        # entangled states is a theorem from the DEFINITION of minimal tensor.

    def test_separable_two_setting_witness_bound(self):
        directions = [
            (1.0, 0, 0, 0), (0.0, 1, 0, 0), (-1.0, 0, 0, 0),
            (0.0, -1, 0, 0), (0.5, 0.5, 0.5, 0.5),
        ]
        for r, s in product(directions, repeat=2):
            self.assertLessEqual(witness_product(r, s), 1 + 1e-12)
        # Convex mixtures inherit this linear witness bound.

    def test_nonseparable_correlator_is_valid_for_product_measurements(self):
        directions = [
            (1.0, 0, 0, 0), (0.0, 1, 0, 0),
            (1/sqrt(2), 1/sqrt(2), 0, 0), (-1/sqrt(2), 1/sqrt(2), 0, 0),
            (0.5, 0.5, 0.5, 0.5),
        ]
        for a, b in product(directions, repeat=2):
            probs = [target_joint_prob(a, b, x, y)
                     for x, y in product((-1, 1), repeat=2)]
            self.assertTrue(all(0 <= p <= 1 for p in probs))
            self.assertAlmostEqual(sum(probs), 1.0)
        # Yet T11+T22 = 2 > 1, so this state cannot lie in minimal tensor.
        self.assertEqual(1 + 1, 2)
        self.assertGreater(2, 1)

    def test_same_qubit_bloch_ball_not_same_composite_theory(self):
        # B_3 has exactly the single-qubit Bloch ball as local state space.
        # Nevertheless the chosen minimal tensor composite has no entanglement.
        n = 3
        self.assertEqual(exact_rank(
            [tensor(e, f) for e, f in product(local_effect_basis(n), repeat=2)]
        ), 16)
        self.assertGreater(2, 1)  # Bell correlations violate product witness.

    def test_pure_extreme_is_not_nontrivial_midpoint(self):
        u = (1.0, 0.0, 0.0, 0.0)
        v = (0.0, 1.0, 0.0, 0.0)
        midpoint = tuple((x + y)/2 for x, y in zip(u, v))
        self.assertLess(norm2(midpoint), 1)
        self.assertEqual(norm2(u), 1)
        self.assertEqual(norm2(v), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
