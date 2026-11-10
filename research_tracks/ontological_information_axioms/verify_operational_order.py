# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""Finite operational-influence toy models for UBT research track OI-4.

Runs with Python's standard library only. Verifies elementary graph-theoretic
results; it does NOT prove emergence of physical causality from information.
"""
from __future__ import annotations

from itertools import product
import unittest


def transitive_closure(n: int, edges: set[tuple[int, int]]) -> set[tuple[int, int]]:
    """Compute positive-length reachability, retaining (i,i) when cycles exist."""
    if not all(0 <= i < n and 0 <= j < n for i, j in edges):
        raise ValueError("Edge endpoints must belong to the n sites")
    reach = set(edges)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (i, k) in reach and (k, j) in reach:
                    reach.add((i, j))
    return reach


def is_acyclic(n: int, edges: set[tuple[int, int]]) -> bool:
    reach = transitive_closure(n, edges)
    return all((i, i) not in reach for i in range(n))


def is_strict_partial_order(n: int, relation: set[tuple[int, int]]) -> bool:
    if any((i, i) in relation for i in range(n)):
        return False
    return all(
        (i, j) in relation
        for i in range(n)
        for k in range(n)
        for j in range(n)
        if (i, k) in relation and (k, j) in relation
    )


def all_loopless_graphs(n: int):
    """Yield all 2^(n*(n-1)) directed graphs without self edges."""
    slots = [(i, j) for i in range(n) for j in range(n) if i != j]
    for choices in product((False, True), repeat=len(slots)):
        yield {edge for edge, flag in zip(slots, choices) if flag}


def measured_influences(n: int, outcomes) -> set[tuple[int, int]]:
    """Operational R: changing setting i can change observed output j.

    outcomes(x) returns n deterministic local outputs for binary settings x.
    This table-level test assumes independently settable x; not every such table
    corresponds to a physically valid quantum or causal-order process.
    """
    found: set[tuple[int, int]] = set()
    for i in range(n):
        other_sites = [k for k in range(n) if k != i]
        for other_settings in product((0, 1), repeat=n - 1):
            x0 = [0] * n
            for k, value in zip(other_sites, other_settings):
                x0[k] = value
            x1 = x0.copy()
            x1[i] = 1
            out0 = tuple(outcomes(tuple(x0)))
            out1 = tuple(outcomes(tuple(x1)))
            if len(out0) != n or len(out1) != n:
                raise ValueError("Expected one output per site")
            for j in range(n):
                if i != j and out0[j] != out1[j]:
                    found.add((i, j))
    return found


class OperationalOrderTests(unittest.TestCase):
    def test_all_three_site_graphs(self):
        graphs = list(all_loopless_graphs(3))
        self.assertEqual(len(graphs), 64)
        dag_count = 0
        closures = set()
        for graph in graphs:
            close = transitive_closure(3, graph)
            # This is theorem OI-4-T1, verified exhaustively for n = 3.
            self.assertEqual(is_acyclic(3, graph), is_strict_partial_order(3, close))
            if is_acyclic(3, graph):
                dag_count += 1
                closures.add(frozenset(close))
        self.assertEqual(dag_count, 25)
        self.assertEqual(len(closures), 19)

    def test_distinguishable_local_bits_have_no_intersite_order(self):
        relation = measured_influences(3, lambda x: x)
        self.assertEqual(relation, set())

    def test_directed_chain_with_transitive_operational_dependence(self):
        relation = measured_influences(
            3, lambda x: (x[0], x[0] ^ x[1], x[0] ^ x[1] ^ x[2])
        )
        self.assertEqual(relation, {(0, 1), (0, 2), (1, 2)})
        self.assertTrue(is_strict_partial_order(3, transitive_closure(3, relation)))

    def test_two_way_table_is_not_acyclic(self):
        relation = measured_influences(2, lambda x: (x[1], x[0]))
        self.assertEqual(relation, {(0, 1), (1, 0)})
        self.assertFalse(is_acyclic(2, relation))
        self.assertIn((0, 0), transitive_closure(2, relation))
        self.assertIn((1, 1), transitive_closure(2, relation))

    def test_structural_cancellation_hides_end_to_end_influence(self):
        # Structural equations: a=x0, b=a, c=a XOR b XOR x2 = x2.
        # Structural graph has A->B, A->C, B->C, yet no measured A->C.
        def response(x):
            a = x[0]
            b = a
            c = a ^ b ^ x[2]
            return a, b, c

        self.assertEqual(measured_influences(3, response), {(0, 1)})


if __name__ == "__main__":
    unittest.main(verbosity=2)
