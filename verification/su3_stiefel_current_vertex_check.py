#!/usr/bin/env python3
"""Symbolic expansion of the Stiefel frame current to O(beta^2)."""
import sympy as sp

# Treat beta and dbeta as independent complex column symbols at one spacetime point.
b=sp.Matrix(sp.symbols("b0:3", complex=True))
db=sp.Matrix(sp.symbols("d0:3", complex=True))

# Formal conjugate row variables.
bc=sp.Matrix(1,3,sp.symbols("bc0:3", complex=True))
dbc=sp.Matrix(1,3,sp.symbols("dc0:3", complex=True))

# Z = [ beta^dagger ; I + 1/2 beta beta^dagger ].
top=bc
bottom=sp.eye(3)+sp.Rational(1,2)*b*bc
Z=top.col_join(bottom)

dtop=dbc
dbottom=sp.Rational(1,2)*(db*bc+b*dbc)
dZ=dtop.col_join(dbottom)

G=sp.diag(1,-1,-1,-1)

# Z^dagger is represented to this formal order by [beta, I+1/2 beta beta^dagger].
Zdag=b.row_join(sp.eye(3)+sp.Rational(1,2)*b*bc)

C=sp.expand(Zdag*G*dZ)

# Keep only terms of total beta/dbeta order 2 by hand: beta d beta^dagger
# minus one half each from derivative of the lower block.
C2=sp.Rational(1,2)*(b*dbc-db*bc)

# Difference contains only cubic+ terms from the truncated multiplication.
diff=sp.expand(C-C2)
for z in diff:
    # Every nonzero monomial in the remainder must have degree >=3 in field symbols.
    poly=sp.Poly(z, *(list(b)+list(db)+list(bc)+list(dbc)))
    if poly.is_zero:
        continue
    assert min(sum(mon) for mon,coeff in poly.terms()) >= 3

# Traceless projection.
C20=sp.simplify(C2-sp.trace(C2)*sp.eye(3)/3)
assert sp.simplify(sp.trace(C20))==0

print("PASS: Stiefel vertical current starts as 1/2(beta d beta^dagger - d beta beta^dagger)_0, giving the adjoint B-beta-dbeta vertex")
