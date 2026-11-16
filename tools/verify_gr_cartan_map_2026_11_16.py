"""Exact 24x24 Cartan map audit for an oriented orthonormal coframe.

Conventions: e^a=dx^a; T^a=sum_{m<n} t^a_{mn} dx^m wedge dx^n;
C(T)_{cd}=sum_{ab} eps_{abcd} T^a wedge dx^b.
Rows are (c<d, i<j<k), columns are (a,m<n).
The determinant depends on ordering/conventions; rank does not.
"""
from itertools import combinations
from sympy import Matrix, zeros, LeviCivita

PAIRS = list(combinations(range(4), 2))
TRIPLES = list(combinations(range(4), 3))
COLS = [(a, m, n) for a in range(4) for m, n in PAIRS]
ROWS = [(c, d, i, j, k) for c, d in PAIRS for i, j, k in TRIPLES]

def cartan_map():
    mat = zeros(24, 24)
    for col, (a, m, n) in enumerate(COLS):
        for row, (c, d, i, j, k) in enumerate(ROWS):
            target = (i, j, k)
            for b in range(4):
                if set((m, n, b)) != set(target):
                    continue
                permutation = [target.index(x) for x in (m, n, b)]
                mat[row, col] += (
                    LeviCivita(a, b, c, d) * LeviCivita(*permutation)
                )
    return Matrix(mat)

if __name__ == "__main__":
    M = cartan_map()
    assert M.shape == (24, 24)
    assert M.rank() == 24
    assert M.det() == 16
    assert M.inv() * M == Matrix.eye(24)
    print("PASS: rank=24, det=16, inverse verified over rationals")
