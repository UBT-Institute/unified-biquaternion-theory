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



def count_binary_three_party_process_functions():
    """Exhaust 16^3 environment maps with no direct self-dependence.

    Reproduces published 744 valid deterministic process functions and 64
    whose three output-to-input component maps are all nonconstant.
    """
    all_out = list(product((0, 1), repeat=3))
    candidates = list(product((0, 1), repeat=4))  # 16 truth tables for 2 bits
    exclusive_count = 0
    no_constant_components = 0
    for truth_tables in product(candidates, repeat=3):
        def environment(outgoing):
            a, b, c = outgoing
            return (
                truth_tables[0][(b << 1) | c],
                truth_tables[1][(a << 1) | c],
                truth_tables[2][(a << 1) | b],
            )

        incoming = [environment(o) for o in all_out]
        if all(
            any(incoming[k][i] == incoming[m][i] and all_out[k][i] != all_out[m][i]
                for i in range(3))
            for k, m in combinations(range(8), 2)
        ):
            exclusive_count += 1
            if all(t not in ((0, 0, 0, 0), (1, 1, 1, 1)) for t in truth_tables):
                no_constant_components += 1
    return exclusive_count, no_constant_components



def single_flip_neighbor_histograms():
    """Hamming-1 perturbation robustness over 12 deterministic truth-table bits.

    This is a combinatorial diagnostic, *not* physical stability or noise.
    """
    all_out = list(product((0, 1), repeat=3))
    pairs = list(combinations(range(8), 2))
    lookup = [
        [(b << 1) | c for a, b, c in all_out],
        [(a << 1) | c for a, b, c in all_out],
        [(a << 1) | b for a, b, c in all_out],
    ]
    valid = set()
    for profile in product(range(16), repeat=3):
        inputs = [
            tuple((profile[i] >> lookup[i][k]) & 1 for i in range(3))
            for k in range(8)
        ]
        if all(
            any(inputs[a][i] == inputs[b][i] and all_out[a][i] != all_out[b][i]
                for i in range(3))
            for a, b in pairs
        ):
            valid.add(profile)
    histogram = Counter()
    no_constant_histogram = Counter()
    with_constant_histogram = Counter()
    for profile in valid:
        neighbors = 0
        for site in range(3):
            for bit in range(4):
                other = list(profile)
                other[site] ^= 1 << bit
                neighbors += tuple(other) in valid
        histogram[neighbors] += 1
        if all(v not in (0, 15) for v in profile):
            no_constant_histogram[neighbors] += 1
        else:
            with_constant_histogram[neighbors] += 1
    return histogram, no_constant_histogram, with_constant_histogram


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

    def test_full_tripartite_process_function_enumeration(self):
        # Established enumeration, not an original UBT claim.
        self.assertEqual(count_binary_three_party_process_functions(), (744, 64))

    def test_hamming_one_perturbation_robustness_observation(self):
        all_hist, no_past_hist, with_past_hist = single_flip_neighbor_histograms()
        self.assertEqual(all_hist, Counter({3: 64, 4: 120, 5: 192, 6: 192, 8: 168, 12: 8}))
        self.assertEqual(no_past_hist, Counter({3: 64}))
        self.assertEqual(with_past_hist, Counter({4: 120, 5: 192, 6: 192, 8: 168, 12: 8}))

    def test_simple_ring_fails_pairwise_exclusive_events(self):
        self.assertFalse(events_pairwise_exclusive(lambda out: (out[1], out[0]), 2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
