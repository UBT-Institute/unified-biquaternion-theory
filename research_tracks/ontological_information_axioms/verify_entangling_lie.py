# © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""OI-6: finite Pauli Lie closure and reversible entanglement comparator.

Reproduces standard two-qubit quantum-control facts. These facts are not a
first-principles derivation of complex amplitudes, entanglement or UBT dynamics.
Uses only the Python standard library; run as python3 this_file.py.
"""
import cmath
import math
import unittest
from itertools import product


I = ((1, 0), (0, 1))
X = ((0, 1), (1, 0))
Y = ((0, -1j), (1j, 0))
Z = ((1, 0), (0, -1))
PAULI = {'I': I, 'X': X, 'Y': Y, 'Z': Z}


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def dagger(a):
    return tuple(tuple(complex(a[j][i]).conjugate() for j in range(len(a)))
                 for i in range(len(a[0])))


def kron(a, b):
    return tuple(tuple(a[i // len(b)][j // len(b[0])] *
                       b[i % len(b)][j % len(b[0])]
                       for j in range(len(a[0]) * len(b[0])))
                 for i in range(len(a) * len(b)))


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def anticommute_pauli_words(a, b):
    return sum(x != y and x != 'I' and y != 'I'
               for x, y in zip(a, b)) % 2 == 1


# Multiplication of Pauli axes, ignoring their +/-i complex phase.
AXIS_MULTIPLICATION = {
    ('X', 'Y'): 'Z', ('Y', 'Z'): 'X', ('Z', 'X'): 'Y',
    ('Y', 'X'): 'Z', ('Z', 'Y'): 'X', ('X', 'Z'): 'Y',
}


def commutator_direction(a, b):
    """Hermitian Pauli basis label proportional to i[a,b], or None."""
    if not anticommute_pauli_words(a, b):
        return None
    return ''.join(x if y == 'I' else y if x == 'I' else
                   'I' if x == y else AXIS_MULTIPLICATION[(x, y)]
                   for x, y in zip(a, b))


def lie_closure(initial):
    """Lie closure of i*Pauli-word generators up to nonzero real scales."""
    generators = set(initial)
    while True:
        new = set(generators)
        for a, b in product(generators, repeat=2):
            c = commutator_direction(a, b)
            if c is not None:
                new.add(c)
        if new == generators:
            return frozenset(generators)
        generators = new


def evolve_xx_on_00(t):
    """exp(-it X tensor X)|00> in computational basis."""
    return (math.cos(t) + 0j, 0j, 0j, -1j * math.sin(t))


def reduced_rho_a(psi):
    return tuple(tuple(sum(psi[2*a+b] * psi[2*c+b].conjugate()
                           for b in range(2)) for c in range(2)) for a in range(2))


def purity(rho):
    return tr(matmul(rho, rho)).real


class ConnectedEntanglementTests(unittest.TestCase):
    def test_pauli_string_commutator_directions_against_exact_matrices(self):
        words = [a+b for a, b in product('IXYZ', repeat=2) if a+b != 'II']
        for p, q in product(words, repeat=2):
            a = kron(PAULI[p[0]], PAULI[p[1]])
            b = kron(PAULI[q[0]], PAULI[q[1]])
            ab, ba = matmul(a, b), matmul(b, a)
            c = commutator_direction(p, q)
            if c is None:
                self.assertTrue(all(abs(ab[i][j]-ba[i][j]) < 1e-12
                                    for i, j in product(range(4), repeat=2)))
            else:
                target = kron(PAULI[c[0]], PAULI[c[1]])
                # Commutator is +/-2i times a Pauli word.
                coefficient = tr(matmul(dagger(target), ab)) / 4
                self.assertAlmostEqual(abs(coefficient), 1)
                self.assertTrue(all(abs((ab[i][j]-ba[i][j])-
                                         2*coefficient*target[i][j]) < 1e-12
                                    for i, j in product(range(4), repeat=2)))

    def test_local_generators_close_in_su2_plus_su2(self):
        local = {'XI', 'YI', 'ZI', 'IX', 'IY', 'IZ'}
        self.assertEqual(lie_closure(local), frozenset(local))

    def test_one_xx_interaction_with_local_controls_generates_su4(self):
        local = {'XI', 'YI', 'ZI', 'IX', 'IY', 'IZ'}
        closure = lie_closure(local | {'XX'})
        self.assertEqual(len(closure), 15)
        self.assertEqual(closure, frozenset(a+b for a, b in product('IXYZ', repeat=2)
                                            if a+b != 'II'))

    def test_any_single_nonlocal_pauli_product_with_local_controls(self):
        local = {'XI', 'YI', 'ZI', 'IX', 'IY', 'IZ'}
        for a, b in product('XYZ', repeat=2):
            self.assertEqual(len(lie_closure(local | {a+b})), 15)

    def test_entangling_path_is_normalized_and_reversible(self):
        for t in [0, math.pi/16, math.pi/8, math.pi/4, math.pi/2]:
            psi = evolve_xx_on_00(t)
            self.assertAlmostEqual(sum(abs(z)**2 for z in psi), 1)
            xx = kron(X, X)
            u = tuple(tuple((math.cos(t) if i == j else 0) -
                            1j*math.sin(t)*xx[i][j] for j in range(4)) for i in range(4))
            unitary = matmul(dagger(u), u)
            self.assertTrue(all(abs(unitary[i][j] - int(i==j)) < 1e-12
                                for i,j in product(range(4), repeat=2)))
            inverse = tuple(tuple((math.cos(t) if i == j else 0) +
                                  1j*math.sin(t)*xx[i][j] for j in range(4)) for i in range(4))
            self.assertEqual(dagger(u), inverse)

    def test_entanglement_has_nonunit_reduced_purity(self):
        for t in [0, math.pi/16, math.pi/8, math.pi/4, math.pi/2]:
            rho = reduced_rho_a(evolve_xx_on_00(t))
            self.assertAlmostEqual(purity(rho),
                                   1 - 0.5*math.sin(2*t)**2)
            self.assertAlmostEqual(rho[0][1].real, 0)
            if 0 < t < math.pi/2:
                self.assertLess(purity(rho), 1)

    def test_maximally_entangled_midpoint(self):
        rho = reduced_rho_a(evolve_xx_on_00(math.pi/4))
        self.assertAlmostEqual(rho[0][0].real, 0.5)
        self.assertAlmostEqual(rho[1][1].real, 0.5)
        self.assertAlmostEqual(purity(rho), 0.5)

    def test_local_reversible_evolution_does_not_entangle_product_state(self):
        for a, b in product([0, math.pi/8, math.pi/4], repeat=2):
            # A normalized product of two real-rotation single-qubit states.
            u = (math.cos(a), math.sin(a))
            v = (math.cos(b), math.sin(b))
            psi = (u[0]*v[0], u[0]*v[1], u[1]*v[0], u[1]*v[1])
            self.assertAlmostEqual(purity(reduced_rho_a(psi)), 1)

    def test_pauli_basis_is_orthogonal(self):
        words = [a+b for a, b in product('IXYZ', repeat=2) if a+b!='II']
        for p, q in product(words, repeat=2):
            ap = kron(PAULI[p[0]], PAULI[p[1]])
            aq = kron(PAULI[q[0]], PAULI[q[1]])
            self.assertAlmostEqual(tr(matmul(ap, aq)).real,
                                   4 if p == q else 0)
            self.assertAlmostEqual(tr(matmul(ap, aq)).imag, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
