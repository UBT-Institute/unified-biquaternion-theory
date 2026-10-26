<!-- BILINGUAL-UNIT: minimal_branch_falsification_verdict -->
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


# Minimal independent-metric Theta branch: scoped falsification verdict

**2026-10-26; conditional model verdict.** This note does NOT falsify the original composite-metric UBT or all possible single-action theories.

## Explicit model tested

Independent Lorentzian 4D metric with Einstein gravity, eight real Theta coordinates on the SL(2,C) congruence carrier, invariant kinetic form H(X)=2(|z0|²-sum|zj|²) of inertia (2,6), conventional quadratic covariant derivatives, and invariant classified quartic U=U0+m²H+lambda1 H²+lambda2|det X|². An SL(2,C) gauge sector, if propagated by ordinary real invariant YM form, has its own (3,3) kinetic obstruction. This is a proposed/conditional alternative to the canonical composite-tetrad UBT; the fundamental ADR is not automatically accepted.

## Vacuum

At X0=i r I (r!=0) the stationarity condition is m²+(4lambda1+lambda2)r²=0. The exact Hessian at the stationary point in real coordinates (Re z0..Re z3,Im z0..Im z3) is diag(0,0,0,0,8r²(4lambda1+lambda2),8lambda2 r²,8lambda2 r²,8lambda2 r²). For lambda1>=0,lambda2>0,m²<0, a nonzero stationary point exists with positive semidefinite potential Hessian. A Minkowski solution additionally requires cancellation of its vacuum energy, U0=(4lambda1+lambda2)r^4 if there is no separate cosmological term; not a zero-parameter prediction.

## Constraint and kinetic test

The congruence orbit at X0 has rank three (boosts); three rotations stabilize the background. The transverse Im z_j directions have negative kinetic form and positive potential Hessian, so generalized mass²=-4lambda2 r² for each (normalization conventions as in the verifier). They are not tangent to the infinitesimal boost orbit. The Theta Gauss momentum Jacobian has rank three. Under a stationary Minkowski background with standard minimally coupled GR, the linearized gravitational constraints have no first-order matter source, leaving those modes in the regular perturbative reduction unless an extra independently derived primary constraint exists. The reduced quadratic Hamiltonian contains negative momentum squares, and its infrared linearized equations have exponentially growing modes.

There is also a separate exact fixed-background Gauss-surface family with unbounded negative matter energy, and a conditional ADM initial-data witness with matter energy arbitrarily negative while both gravity scalar/momentum constraints are solvable. Neither the latter nor the flat perturbative result is a nonperturbative ADM-mass theorem.

## Stop decision — precisely scoped

**FAIL** the acceptance criterion 'positive physical quadratic kinetic matrix and tachyon-free spectrum' for the stated minimal GR+Theta branch around the specified vacuum, conditional on regular perturbative reduction and no further derived constraints. Full noncompact YM has an additional standard free-sector negative-energy obstruction. Do not salvage this failed branch by adding unmotivated R², ad hoc torsion terms, arbitrary new constraints or redefining S_UBT. Do not claim all UBT is disproved or that a unique fundamental Hamiltonian has been found.

Outstanding for a completely formal theorem: derive/accept one fully specified common action and all its independent/composite variables; independently verify complete constraint Poisson closure with chosen psi treatment and background; determine whether the conformal/diffeomorphism sector introduces any unexpected additional constraints. No such closure is being claimed by this scoped decision.

## Reproducibility and implementation state

- tools/verify_theta_quartic_vacuum_hessian.py (exact SymPy Hessian);
- tools/verify_theta_gauss_momentum_rank.py;
- tools/verify_theta_gauss_energy_unbounded.py;
- tools/verify_theta_quadratic_ghost_channel.py;
- tools/verify_theta_positive_slice.py;
- research_tracks/action_selection/{quadratic_reduced_ghost_stationary_vacuum,adm_constraint_negative_theta_witness,no_positive_invariant_linear_slice}.en.md.

All statements about GitHub Actions/CI must be verified separately; adding a test is not equivalent to a successful CI run.
