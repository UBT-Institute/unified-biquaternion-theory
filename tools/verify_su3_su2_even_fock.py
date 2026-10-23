"""Exact conditional SU(3)xSU(2)xU(1) even-exterior-Fock audit.

The colour C^3 is the existing proved UBT representation.  The weak C^2,
the even-parity projection, physical Weyl spinors, and a gauge action
are ASSUMED FOR THIS REPRESENTATION TEST and are not derived from Theta.
"""
from itertools import combinations
import sympy as sp


def verify_even_fock_generation():
    I = sp.I
    color = [
        sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
        sp.diag(1, -1, 0),
        sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
        sp.diag(1, 1, -2) / sp.sqrt(3)
    ]
    color = [m / 2 for m in color]
    weak = [sp.Matrix([[0, 1], [1, 0]]) / 2,
            sp.Matrix([[0, -I], [I, 0]]) / 2,
            sp.diag(1, -1) / 2]

    def second_quantize(A, states):
        pos = {S: i for i, S in enumerate(states)}
        B = sp.zeros(len(states))
        for S, col in pos.items():
            for j in S:
                reduced = tuple(x for x in S if x != j)
                remove_sign = (-1) ** S.index(j)
                for i in range(A.rows):
                    if i in reduced or A[i, j] == 0:
                        continue
                    changed = tuple(sorted(reduced + (i,)))
                    add_sign = (-1) ** sum(x < i for x in reduced)
                    B[pos[changed], col] += remove_sign * add_sign * A[i, j]
        return B

    states = [tuple(S) for k in (0, 2, 4) for S in combinations(range(5), k)]
    lift = lambda A: second_quantize(A, states)
    blocks_c = [m.row_join(sp.zeros(3, 2)).col_join(sp.zeros(2, 5))
                for m in color]
    blocks_w = [sp.zeros(3, 5).col_join(sp.zeros(2, 3).row_join(m))
                for m in weak]
    C = [lift(m) for m in blocks_c]
    W = [lift(m) for m in blocks_w]
    Nc = sp.diag(*[sum(x < 3 for x in S) for S in states])
    Nw = sp.diag(*[sum(x >= 3 for x in S) for S in states])
    Y = -Nc / 3 + Nw / 2
    sectors = {}
    for S in states:
        key = (sum(i < 3 for i in S), sum(i >= 3 for i in S))
        sectors[key] = sectors.get(key, 0) + 1
    expected = {(0, 0): (1, 0), (0, 2): (1, 1),
                (1, 1): (6, sp.Rational(1, 6)),
                (2, 0): (3, sp.Rational(-2, 3)),
                (2, 2): (3, sp.Rational(1, 3)),
                (3, 1): (2, sp.Rational(-1, 2))}
    results = {}
    results["16 even exterior states"] = len(states) == 16
    results["six standard-model multiplet sectors"] = {
        k: (n, -sp.Rational(k[0], 3) + sp.Rational(k[1], 2))
        for k, n in sectors.items()} == expected
    results["Hermitian traceless generators"] = all(
        m == m.conjugate().T and m.trace() == 0 for m in C + W)
    results["strong and weak generators commute"] = all(
        a * b == b * a for a in C for b in W)
    results["colour algebra closure"] = all(
        C[i] * C[j] - C[j] * C[i] ==
        lift(blocks_c[i] * blocks_c[j] - blocks_c[j] * blocks_c[i])
        for i in range(8) for j in range(i + 1, 8))
    results["weak algebra closure"] = all(
        W[i] * W[j] - W[j] * W[i] ==
        lift(blocks_w[i] * blocks_w[j] - blocks_w[j] * blocks_w[i])
        for i in range(3) for j in range(i + 1, 3))
    results["hypercharge commutes with both algebras"] = all(
        m * Y == Y * m for m in C + W)
    results["colour Casimir 4/3"] = sum(
        (m * m for m in C), sp.zeros(16)) == sp.diag(*[
        sp.Rational(4, 3) if sum(i < 3 for i in S) in (1, 2)
        else 0 for S in states])
    results["weak Casimir 3/4"] = sum(
        (m * m for m in W), sp.zeros(16)) == sp.diag(*[
        sp.Rational(3, 4) if sum(i >= 3 for i in S) == 1
        else 0 for S in states])
    results["gravitational U1 anomaly"] = sp.trace(Y) == 0
    results["U1 cubic anomaly"] = sp.trace(Y ** 3) == 0
    results["SU3 squared U1 anomaly"] = all(
        sp.simplify(sp.trace(Y * (a * b + b * a))) == 0
        for a in C for b in C)
    results["SU2 squared U1 anomaly"] = all(
        sp.simplify(sp.trace(Y * (a * b + b * a))) == 0
        for a in W for b in W)
    results["SU3 U1 squared anomaly"] = all(
        sp.simplify(sp.trace(Y ** 2 * m)) == 0 for m in C)
    results["SU2 U1 squared anomaly"] = all(
        sp.simplify(sp.trace(Y ** 2 * m)) == 0 for m in W)
    results["SU3 cubic tensor 288 entries"] = all(
        sp.simplify(sp.trace(C[a] * (C[b] * C[c] + C[c] * C[b]))) == 0
        for a in range(8) for b in range(8) for c in range(b, 8))
    results["SU2 cubic tensor"] = all(
        sp.simplify(sp.trace(W[a] * (W[b] * W[c] + W[c] * W[b]))) == 0
        for a in range(3) for b in range(3) for c in range(b, 3))
    results["Witten global SU2 anomaly absent: four doublets"] = (
        (sectors[(1, 1)] + sectors[(3, 1)]) // 2 == 4)

    # Direct Schur-commutant rank of the prior single-colour 8-state Fock.
    old_states = [tuple(S) for k in range(4)
                  for S in combinations(range(3), k)]
    old_C = [second_quantize(m, old_states) for m in color]
    comm_eqs = sp.zeros(0, 64)
    for m in old_C:
        comm_eqs = comm_eqs.col_join(
            sp.kronecker_product(sp.eye(8), m) -
            sp.kronecker_product(m.T, sp.eye(8)))
    results["exact colour-Fock commutant has complex dimension six"] = (
        comm_eqs.rank() == 58)
    results["one colour-Fock lacks triplet doublet"] = (
        [sum(len(S) == k for S in old_states) for k in range(4)]
        == [1, 3, 3, 1])
    results["two colour Focks match the 16-state SU3 content"] = (
        2 * 2 == 4 and 2 * 1 == sectors[(1, 1)] // 3 and
        2 * 1 == (sectors[(2, 0)] + sectors[(2, 2)]) // 3)

    a, b, c = sp.symbols("a b c", real=True)
    Q = a * Nc + b * Nw + c * sp.eye(16)
    qlinear = sp.trace(Q)
    qcubic = sp.trace(Q ** 3)
    results["general linear occupation trace factorization"] = (
        sp.expand(qlinear - 8 * (3 * a + 2 * b + 2 * c)) == 0)
    results["general cubic occupation trace factorization"] = (
        sp.expand(qcubic - 4 * (3 * a + 2 * b + 2 * c) *
                  (9*a*a + 6*a*b + 6*a*c + 5*b*b + 4*b*c + 2*c*c)) == 0)
    results["neutral vacuum fixes charge-offset branch"] = (
        sp.solve(3 * a + 2 * b, b) == [-3 * a / 2] and
        sp.simplify(qcubic.subs({b: -3*a/2, c: 0})) == 0)
    results["normalized SM hypercharge recovered"] = (
        Q.subs({a: -sp.Rational(1,3), b: sp.Rational(1,2), c: 0}) == Y)
    return results


if __name__ == "__main__":
    tests = verify_even_fock_generation()
    for name, value in tests.items():
        print(("PASS" if value else "FAIL") + " " + name)
    print(f"{sum(tests.values())}/{len(tests)} exact checks")
    if not all(tests.values()):
        raise SystemExit(1)
