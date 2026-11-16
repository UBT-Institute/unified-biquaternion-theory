"""Exact central bivector pair identity in the canonical Lorentz slice.

Checks all 4^4 index combinations using SymPy complex quaternion arithmetic.
This tests the algebraic identity, not a dynamical UBT action or on-shell solution.
"""
from itertools import product
import sympy as s

I = s.I
basis = [s.eye(4)[:, j] for j in range(4)]
E = [I*basis[0], basis[1], basis[2], basis[3]]
eta = s.diag(-1, 1, 1, 1)

def mul(a,b):
    return s.Matrix([
        a[0]*b[0]-sum(a[j]*b[j] for j in range(1,4)),
        a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2],
        a[0]*b[2]+a[2]*b[0]+a[3]*b[1]-a[1]*b[3],
        a[0]*b[3]+a[3]*b[0]+a[1]*b[2]-a[2]*b[1]
    ])

def sharp(a):
    return s.Matrix([a[0], -a[1], -a[2], -a[3]])

sigma = {(a,b):(mul(sharp(E[a]),E[b])-mul(sharp(E[b]),E[a]))/2
         for a,b in product(range(4),repeat=2)}
for a,b,c,d in product(range(4),repeat=4):
    z = (mul(sharp(sigma[a,b]),sigma[c,d])
         + mul(sharp(sigma[c,d]),sigma[a,b]))/2
    want = eta[a,c]*eta[b,d]-eta[a,d]*eta[b,c]-I*s.LeviCivita(a,b,c,d)
    assert z == s.Matrix([want, 0, 0, 0]), (a,b,c,d,z,want)

# Orthogonal tangent basis; Hodge pseudoscalar vanishes against
# any algebraic-curvature R satisfying R_[abcd]=0 (first Bianchi identity).
# Construct nontrivial R from constant-curvature and symmetric Ricci sectors.
Ric = s.Matrix([[2,1,0,0],[1,3,0,0],[0,0,4,2],[0,0,2,5]])
def R(a,b,c,d):
    return (eta[a,c]*Ric[b,d]-eta[a,d]*Ric[b,c]
           -eta[b,c]*Ric[a,d]+eta[b,d]*Ric[a,c])
eps_contraction = sum(s.LeviCivita(a,b,c,d)*R(a,b,c,d)
                      for a,b,c,d in product(range(4),repeat=4))
assert s.simplify(eps_contraction) == 0
print("PASS: 256 canonical sharp-bivector identities and torsion-free epsilon contraction")
