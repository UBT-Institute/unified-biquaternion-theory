# Hamiltonian-first foundations: configuration algebra does not select a generator

**Status: precise underdetermination theorem and candidate phase-space specification; C-tier. 2026-10-24.** NOT a completed UBT Hamiltonian. Does not derive dynamics by Legendre-transforming an adopted action. Respects the locked single fundamental field Theta.

## Starting from the locked objects only

The UBT axioms define Theta(x,t+i psi) in the 8-real-dimensional biquaternion algebra and its allowed transformations and composite geometry. On a real-time slice, choose local real coordinates q^A, A=1,...,8. The choice of *canonical* cotangent extension (q^A,p_A) with 1-form θ=∫p_A δq^A and Ω=∫δp_A∧δq^A is mathematically consistent, but is **not fixed by the field algebra**. Spatial boundary conditions, psi dynamics, gauge reduction and possible constrained/noncanonical Poisson brackets require independent derivation.

For a linear global representation q'=M q (for any invertible real M in the declared symmetry representation), the cotangent lift p'=M^{-T}p preserves θ exactly: p'^T dq'=p^T dq. Consequently the canonical Poisson brackets, if selected, are compatible with the symmetry. Compatibility is not selection.

## The exact non-uniqueness obstruction

Even on the **same** chosen canonical phase space, symmetry and fixed kinetic normalization do not select one H. Let I(q) denote the known invariant quadratic polynomial from theta_potential_invariants.en.md. Let J(q)=I(q)^2, also invariant. If T(q,p) is *any* nontrivial invariant Hamiltonian term, both H_0=T and H_λ=T+λ J(q) are invariant for arbitrary real λ. Their momentum evolution differs:
\[
\dot p_A[H_\lambda]-\dot p_A[H_0]=-\lambda\frac{\partial J}{\partial q^A}.
\]
Whenever ∇J≠0 and λ≠0 these are physically different flows, although both preserve the same symmetry and phase-space two-form. Importantly, neither H_0 nor H_λ is claimed to be the real UBT Hamiltonian. This is a proof that **a further dynamical selector is required**; tuning a quartic potential to a preferred vacuum does not eliminate this ambiguity.

The same logic holds in field theory with H_λ=H_0+λ∫d^3x w(x)J(q(x)) whenever the measure/density w is already symmetry-invariant and fixed independently; no independent metric assumption is hidden here. If full diffeomorphism invariance is additionally required, appropriate density weights and closure of constraints must be established; this finite-dimensional argument alone does not prove the existence of two viable full gravitational Hamiltonians.

## What must be derived next, in order

1. **Canonical data / brackets:** Is the unique UBT time evolution a real-time flow or a relation involving psi? Derive a physically defensible symplectic/presymplectic form on Theta's gauge-reduced initial-data space. Do not assume [Theta,Pi] quantization or canonical Poisson brackets are axioms.
2. **Independent Hamiltonian selector:** Define a pre-action principle (e.g. conserved energy as a geometric Noether charge, closure of gravitational constraint algebra, or a spectral positivity/representation condition) and demonstrate it follows from locked UBT data rather than being imposed. A symmetry classification will give candidates, not a unique operator.
3. **Constraint closure:** compute all candidate primary/secondary constraints and their Poisson brackets in a nondegenerate composite tetrad background. Eliminate gauge directions; check positivity only on physical phase space.
4. **Inverse Legendre map:** reconstruct a single action only after the selected H and symplectic form are known. Verify that its gravity, matter and psi limits follow, not just agree by reversing an already postulated action.

## Distinguish existing results

- canonical_family_hamiltonian_bridge.en.md is a Hamiltonian *derived from a family of Lagrangians*, so it cannot independently select the action.
- adm_gr_hessian_constraint_audit.en.md is the adopted GR endpoint, not a microscopic Theta-only Hamiltonian.
- splitjet_auxiliary_kernel.en.md documents auxiliary null shifts in the adopted gravity sector, not the fundamental Poisson algebra.
- Existing quartic invariants and kinetic signature (2,6) are valuable candidate constraints but do not uniquely determine positive physical dynamics.

**Decision gate:** any future claim 'Hamiltonian derived' must exhibit the symplectic form, generator, assumptions that select it, closure/health checks and explicit reduction maps. Do not add H_λ to canonical UBT.

Reproducibility: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_hamiltonian_nonuniqueness.py' -v\`.
