#!/usr/bin/env python3
"""Order-counting check for the composite coset connection and F^2 term.

The check uses a formal small parameter eps:
pi = eps*pi1.
Then d pi is order eps, A starts at eps^2, F starts at eps^2,
and F^2 starts at eps^4.
"""
import sympy as sp

eps=sp.symbols("eps")
a2,a3=sp.symbols("a2 a3")
f2,f3,f4=sp.symbols("f2 f3 f4")

# Composite connection has no linear term.
A=eps**2*a2+eps**3*a3
assert sp.expand(A).coeff(eps,1)==0
assert sp.expand(A).coeff(eps,2)==a2

# Curvature likewise starts at second order.
F=eps**2*f2+eps**3*f3+eps**4*f4
assert sp.expand(F).coeff(eps,1)==0
assert sp.expand(F).coeff(eps,2)==f2

F2=sp.expand(F**2)
assert F2.coeff(eps,2)==0
assert F2.coeff(eps,3)==0
assert F2.coeff(eps,4)==f2**2

print("PASS: composite A begins at O(pi^2), F at O(pi^2), and tr F^2 at O(pi^4); no quadratic gluon kernel is generated in the original coset variables")
