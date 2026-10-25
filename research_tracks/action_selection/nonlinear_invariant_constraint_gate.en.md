# Nonlinear invariant constraints: a nongauge negative direction at the timelike vacuum

**Status:** exact local algebraic probe, conditional on the congruence representation and the pre-existing H pairing (2026-10-26). This is NOT a full nonlinear Dirac reduction or proof of a propagating ghost.

At X0=i r I (r nonzero real), use X=(a+ib)I+sum_j (u_j+i v_j)i sigma_j as the real coordinate parametrization. The quadratic pairing H(delta X)=2(a²+b²-|u|²-|v|²) has inertia (2,6). In the infinitesimal congruence action delta_T X=T X+X T^dagger, boost tangent vectors span the three u_j directions and SU(2) rotations stabilize X0; the three v_j directions are negative and transverse to the gauge orbit at X0.

For an explicit probe X(v)=i r I-v sigma3, one has z0=i r, z3=i v, and therefore exactly
```
H(X(v))=2(r²-v²),
det X(v)=-r²-v².
```
Both invariant functions have vanishing first derivative in v at zero but nonzero second derivative. The direction is not an infinitesimal congruence boost at X0, and cannot be discarded merely by counting all six Lie generators as gauge directions. A constraint on an invariant may have singular linearization there, however; one must explicitly inspect its regularity and the nonlinear constrained phase space.

If a smooth invariant constraint surface through X0 is chosen, every infinitesimal boost orbit vector at X0 is tangent to that surface (as long as the full orbit stays in it). Since the kinetic quadratic form is strictly negative on nonzero boost tangents, the **unquotiented induced metric** cannot be positive definite. After gauge quotient this argument alone no longer forbids positivity: the remaining negative v_j could in principle be removed by additional independently justified regular constraints. But such constraints have not been derived, and isolated invariant equalities imposed ad hoc do not count as the UBT Dirac equations.

Next theorem gate: specify a concrete single action and its primary/secondary constraint functions, compute the full constraint Jacobian and Poisson-bracket rank around X0 (including singular constraints), and evaluate the kinetic form on the actual gauge-reduced tangent/normal cone. Include the noncompact YM sector if chosen. Do not claim full falsification based only on the present kinematic probe.

Verifier: tools/verify_theta_nonlinear_invariant_gate.py; regression: tests/test_theta_nonlinear_invariant_gate.py.
