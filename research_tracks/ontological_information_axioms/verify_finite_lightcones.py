# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""OI-4D: exact finite propagation in time-indexed local information networks.

Elementary finite mathematics; neither Lorentz invariance nor UBT dynamics is
claimed. Run: python3 verify_finite_lightcones.py
"""
from itertools import product
import unittest


def ancestors(predecessors, vertex, steps):
    """Input sites at time 0 that may affect vertex after steps ticks."""
    active = {vertex}
    for _ in range(steps):
        active = active | {u for v in active for u in predecessors[v]}
    return active


def or_step(predecessors, values):
    """Information-spreading rule that saturates the graph light cone."""
    return {v: int(any(values[u] for u in ({v} | set(predecessors[v]))))
            for v in predecessors}


def xor_noise_step(predecessors, values, noise):
    """Generic local dynamics with a time-dependent externally supplied noise."""
    return {v: (values[v] ^ noise[v] ^
                (sum(values[u] for u in predecessors[v]) & 1))
            for v in predecessors}


def square_grid(radius, mode="von-neumann"):
    sites = set(product(range(-radius, radius + 1), repeat=2))
    displacements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if mode == "moore":
        displacements += [(a, b) for a in (-1, 1) for b in (-1, 1)]
    return {v: {tuple(v[i] + dv[i] for i in (0, 1))
                for dv in displacements
                if tuple(v[i] + dv[i] for i in (0, 1)) in sites}
            for v in sites}


class FinitePropagationTests(unittest.TestCase):
    def test_directed_chain_exact_bound(self):
        graph = {0: set(), 1: {0}, 2: {1}, 3: {2}, 4: {3}}
        self.assertNotIn(0, ancestors(graph, 4, 3))
        self.assertIn(0, ancestors(graph, 4, 4))
        states = {v: int(v == 0) for v in graph}
        for tick in range(5):
            self.assertEqual(states[4], int(tick >= 4))
            states = or_step(graph, states)

    def test_cyclic_spatial_graph_not_causal_time_loop(self):
        # Spatial cycles are permitted: dependencies point from t to t+1.
        graph = {0: {1}, 1: {2}, 2: {0}}
        states = {0: 1, 1: 0, 2: 0}
        states = or_step(graph, states)
        self.assertEqual(states, {0: 1, 1: 0, 2: 1})
        states = or_step(graph, states)
        self.assertEqual(states, {0: 1, 1: 1, 2: 1})

    def test_all_reachable_vertices_saturate_or_cone(self):
        graph = square_grid(3, "von-neumann")
        values = {v: int(v == (0, 0)) for v in graph}
        for k in range(4):
            self.assertEqual({v for v in graph if values[v]},
                             {v for v in graph if (0, 0) in ancestors(graph, v, k)})
            values = or_step(graph, values)

    def test_anisotropic_2d_cones(self):
        graph4 = square_grid(4, "von-neumann")
        graph8 = square_grid(4, "moore")
        targets4 = {v for v in graph4 if (0, 0) in ancestors(graph4, v, 2)}
        targets8 = {v for v in graph8 if (0, 0) in ancestors(graph8, v, 2)}
        self.assertEqual(targets4, {v for v in graph4 if abs(v[0]) + abs(v[1]) <= 2})
        self.assertEqual(targets8, {v for v in graph8 if max(abs(v[0]), abs(v[1])) <= 2})
        self.assertEqual((len(targets4), len(targets8)), (13, 25))
        self.assertNotIn((2, 2), targets4)
        self.assertIn((2, 2), targets8)

    def test_common_noise_coupling_respects_exact_support(self):
        graph = {0: set(), 1: {0}, 2: {1}}
        vertices = tuple(graph)
        # All binary initial states, all independent intervention sites and
        # every 2-step binary noise history on all three vertices.
        for bits in product((0, 1), repeat=3):
            initial = dict(zip(vertices, bits))
            for intervention_site in vertices:
                changed = initial.copy()
                changed[intervention_site] ^= 1
                for noise_bits in product((0, 1), repeat=6):
                    noises = [
                        dict(zip(vertices, noise_bits[0:3])),
                        dict(zip(vertices, noise_bits[3:6]))
                    ]
                    state, altered = initial, changed
                    for tick in range(3):
                        for target in vertices:
                            if intervention_site not in ancestors(graph, target, tick):
                                self.assertEqual(state[target], altered[target])
                        if tick < 2:
                            state = xor_noise_step(graph, state, noises[tick])
                            altered = xor_noise_step(graph, altered, noises[tick])

    def test_complete_graph_can_broadcast_in_one_tick(self):
        vertices = tuple(range(6))
        graph = {v: {u for u in vertices if u != v} for v in vertices}
        states = {v: int(v == 0) for v in vertices}
        result = or_step(graph, states)
        self.assertEqual(result, {v: 1 for v in vertices})
        self.assertEqual(ancestors(graph, 5, 1), set(vertices))


if __name__ == "__main__":
    unittest.main(verbosity=2)
