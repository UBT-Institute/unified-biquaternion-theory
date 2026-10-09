#!/usr/bin/env python3
"""Exact algebraic check of the complex-time holomorphy/Lorentz boost no-go."""
import sympy as sp

g,v=sp.symbols("gamma v", nonzero=True)
# After eliminating d_psi using the unboosted CR equation, boosts +v and -v:
M=sp.Matrix([[g-1,g*v],[g-1,-g*v]])
det=sp.factor(M.det())
assert det == -2*g*v*(g-1)

# For a nontrivial boost gamma != 1 and v != 0, the only (d_t,d_x) solution is 0.
dt,dx=sp.symbols("dt dx")
sol=sp.solve([sp.Eq((g-1)*dt+g*v*dx,0),
              sp.Eq((g-1)*dt-g*v*dx,0)],(dt,dx),dict=True)
assert sol == [{dt:0,dx:0}]

print("PASS: frame-independent CR holomorphy with scalar psi forces trivial derivatives under opposite boosts")
