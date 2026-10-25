<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Inverse Legendre reconstruction: what scalar energy can and cannot select

**C-tier, 2026-10-23.** Exact finite-dimensional kinetic theorem under stated assumptions, not fundamental UBT action.

Current sources: [canonical action registry](../../canonical/ACTION.en.md), [existing conditional Hamiltonian](canonical_family_hamiltonian_bridge.en.md), [scalar-energy bridge](scalar_energy_gravity_bridge.en.md), and [DavJ/research #3](https://github.com/DavJ/research/pull/3).

## Proposition 1: regular inverse transform preserves kinetic inertia

For real q in R^n, nondegenerate symmetric K, and C>0, suppose
```math
H(q,p)=\frac{1}{2C}p^T K^{-1}p+U(q).
```
Hamilton's velocity relation yields `dot q=K^{-1}p/C`, `p=CK dot q`, and
```math
L=p\cdot\dot q-H=\frac C2\dot q^TK\dot q-U(q).
```
Thus the Hessian of L with respect to velocities is `CK`. Sylvester's law of inertia guarantees that the number of negative kinetic directions is invariant under any invertible real linear field redefinition. A potential U cannot change this highest-time-derivative quadratic form. With the **existing UBT congruence kinetic comparator** `K=2 diag(1,-1,-1,-1,1,-1,-1,-1)`, the unconstrained Lagrangian has signature (2,6), or (6,2) if the overall sign is reversed. Neither is positive on all eight directions.

This is a theorem of the *regular fixed-background quadratic comparator*. It is not a ghost theorem for the physical constrained composite Theta theory. The presence of gauge or second-class constraints makes the kinetic reduction singular or restricts the admissible momentum subspace.

## Proposition 2: energy density does not uniquely select an action

A function called 'scalar energy' without a specified symplectic form, canonical variables, time notion, constraint surface, and boundary terms does not uniquely define the Hamiltonian or its inverse Lagrangian. Even if the canonical phase space is specified, two Lagrangians differing by `dF(q,t)/dt` have shifted momenta and equivalent Euler equations; their bare functional expressions are not unique. In gravity the Hamiltonian includes lapse/shift constraints and boundary charges; treating the ADM gravitational kinetic sign as an unconstrained particle ghost is invalid.

## Proposition 3: why the existing composite metric changes the problem

Canonical UBT sets `E_mu=N0^(-1/2)D_mu Theta` and constructs `g_mu nu` from central products of E. In a candidate action using `g[E]`, velocity dependence enters both explicit DTheta factors and the metric, volume element and connections. Hence the fixed-background Hessian above is not the Hessian of the full composite functional. To infer a physical scalar energy, vary the *same selected action* with full chain rules, perform Dirac-Bergmann reduction, then derive the stress tensor/energy and cosmological equation of state. The action-selection ambiguity remains OPEN after merged #700, and merged #635 recovers Einstein–Lambda **conditionally** with a low-energy postulate.

## Decision gates

1. Identify canonical variables and all symmetry generators/redundancies of the actual single-Theta realization.
2. For each proposed action invariant, calculate full velocity Hessian, lapse/shift dependence and constraints **before** a homogeneous FLRW truncation.
3. Reduce the phase space and test the physical quadratic kinetic form. A negative direction in K is not harmless unless an explicit physical constraint removes it.
4. Only then ask whether a derived scalar stress tensor has `rho+3p/c²<0` without unstable physical modes.
5. No term `lambda (div A)^2` from the old Maxwell scalar is imported; the research audit's pure-gauge and Hamiltonian counterexamples remain regression gates.

**Immediate constructive output:** inverse Legendre transformation is mathematically valid and does not solve action *selection*. It establishes a falsifiable constraint: any claimed cure of the (2,6) signature must exhibit the actual reduced physical subspace and its energy sign. No new adjustable coefficient is proposed.

Reproduce via `python -m unittest discover -s research_tracks/action_selection/tests -p 'test_inverse_legendre_signature.py' -v`.
