# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""OI-4: Finite consistency versus definite causal order.

Standard-library tests for (a) unrestricted Boolean functions on *fixed wiring*
networks and (b) general environment-process maps. These are reproductions of
finite mathematical facts and published process-function results, NOT a new
physical principle or a UBT spacetime derivation.
"""

from collections import Counter
from itertools import combinations, product
import unittest


def directed_graphs(n):
    possible = [(i, j) for i in range(n) for j in range(n) if i != j]
    for mask in product((0, 1), repeat=len(possible)):
        yield frozenset(e for e, flag in zip(possible, mask) if flag)


def cyclic(n, edges):
    reach = set(edges)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (i, k) in reach and (k, j) in reach:
                    reach.add((i, j))
    return any((i, i) in reach for i in range(n))


def profiles_on_fixed_wiring(n, edges):
    """All Boolean local maps f_i from values of the selected parent nodes.

    Unused edges (ignored by a chosen f_i) are permitted. This full freedom is
    essential: it includes constants, identities, and a single bit inversion.
    """
    parents = [tuple(i for i in range(n) if (i, j) in edges) for j in range(n)]
    local_functions = [product((0, 1), repeat=1 << len(p)) for p in parents]
    for functions in product(*local_functions):
        yield parents, functions


def fixed_points_on_wiring(n, parents, functions):
    solutions = []
    for state in product((0, 1), repeat=n):
        if all(
            state[j] == functions[j][sum(state[i] << k for k, i in enumerate(parents[j]))]
            for j in range(n)
        ):
            solutions.append(state)
    return solutions


def lugano_process(outputs):
    """Published 3-party Lugano process, w(out_A,out_B,out_C) -> inputs.

    w_A=(NOT out_B) AND out_C;
    w_B=(NOT out_C) AND out_A;
    w_C=(NOT out_A) AND out_B.
    """
    a, b, c = outputs
    return ((1 - b) & c, (1 - c) & a, (1 - a) & b)


def functions_on_binary_input():
    """All four deterministic local maps {0,1}->{0,1}."""
    return list(product((0, 1), repeat=2))


def fixed_points_for_environment(w, maps):
    """Solutions for incoming = w(outgoing), outgoing_i = f_i(incoming_i)."""
    fixed = []
    for incoming in product((0, 1), repeat=len(maps)):
        outgoing = tuple(f[incoming[i]] for i, f in enumerate(maps))
        if incoming == w(outgoing):
            fixed.append((incoming, outgoing))
    return fixed


def events_pairwise_exclusive(w, n):
    """For every two distinct global outputs, at least one site has
    equal incoming symbols but distinct outgoing symbols.

    For a complete deterministic process w and arbitrary independent local
    maps, this is equivalent to universal uniqueness of the fixed point;
    see Dourdent et al. (2026), not an original UBT theorem.
    """
    outgoing = list(product((0, 1), repeat=n))
    for a, b in combinations(outgoing, 2):
        ia, ib = w(a), w(b)
        if not any(ia[k] == ib[k] and a[k] != b[k] for k in range(n)):
            return False
    return True


def process_dependency_edges(w, n):
    """Aggregate dependencies of each environment input on outgoing bits."""
    edges = set()
    for outgoing in product((0, 1), repeat=n):
        for j in range(n):
            changed = list(outgoing)
            changed[j] ^= 1
            before, after = w(outgoing), w(tuple(changed))
            for i in range(n):
                if i != j and before[i] != after[i]:
                    edges.add((j, i))
    return edges


class ConsistencyVersusOrderTests(unittest.TestCase):
    def test_all_three_node_wiring_graphs_and_local_maps(self):
        graph_types = Counter()
        fixed_point_hist = Counter()
        total_profiles = 0
        for graph in directed_graphs(3):
            is_cyclic = cyclic(3, graph)
            graph_types['cyclic' if is_cyclic else 'dag'] += 1
            bad_profiles = 0
            for parents, functions in profiles_on_fixed_wiring(3, graph):
                solutions = fixed_points_on_wiring(3, parents, functions)
                fixed_point_hist[len(solutions)] += 1
                total_profiles += 1
                if len(solutions) != 1:
                    bad_profiles += 1
            # Universal one-solution property <-> DAG in *fixed wiring* model.
            self.assertEqual(bad_profiles == 0, not is_cyclic)
        self.assertEqual(total_profiles, 17576)
        self.assertEqual(graph_types, Counter(dag=25, cyclic=39))
        self.assertEqual(
            fixed_point_hist, Counter({1: 11832, 0: 2902, 2: 2784, 3: 56, 4: 2})
        )

    def test_simple_feedback_ring_is_not_universally_consistent(self):
        # Two-way identity gives two solutions; invert one direction gives none.
        ring = {(0, 1), (1, 0)}
        identity = ((0, 1), (0, 1))
        inverted = ((0, 1), (1, 0))
        parents = [(1,), (0,)]
        self.assertEqual(len(fixed_points_on_wiring(2, parents, identity)), 2)
        self.assertEqual(len(fixed_points_on_wiring(2, parents, inverted)), 0)
        self.assertTrue(cyclic(2, ring))

    def test_lugano_is_consistent_under_all_64_local_maps(self):
        local = functions_on_binary_input()
        for maps in product(local, repeat=3):
            self.assertEqual(len(fixed_points_for_environment(lugano_process, maps)), 1)

    def test_lugano_aggregate_dependency_has_a_cycle(self):
        edges = process_dependency_edges(lugano_process, 3)
        self.assertEqual(len(edges), 6)
        self.assertTrue(cyclic(3, edges))
        # Cyclic potential dependencies are not a fixed Boolean wiring ring.
        self.assertTrue(events_pairwise_exclusive(lugano_process, 3))

    def test_simple_ring_fails_pairwise_exclusive_events(self):
        self.assertFalse(events_pairwise_exclusive(lambda out: (out[1], out[0]), 2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
