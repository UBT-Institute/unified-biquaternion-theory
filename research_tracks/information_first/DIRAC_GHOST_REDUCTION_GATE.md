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

# Dirac ghost-removal criterion: a worked constrained benchmark, not UBT closure

**2026-10-26.** The ADM kinetic pairing has negative directions on the unrestricted phase space. A healthy Hamiltonian requires actual action-generated constraints, not just calling these directions gauge.

Take a finite two-coordinate benchmark L=(dot x²-m²x²)/2 - (dot y²-m²y²)/2 + lambda*y. Equivalently canonical H=(p_x²+m²x²)/2 -(p_y²+m²y²)/2 -lambda*y, with primary p_lambda=0. Dirac consistency gives y=0, p_y=0, lambda=0. The four constraints (p_lambda,y,p_y,lambda) have a nondegenerate Poisson matrix (determinant 1), thus are SECOND CLASS, not gauge transformations. The reduced Hamiltonian is H_red=(p_x²+m²x²)/2 >=0 when m²>=0. This is an explicit existence proof that constraints *can* remove a negative-energy degree of freedom. It does not show that UBT generates such constraints.

Without the multiplier y=0 the unconstrained negative oscillator contributes -(p_y²+m²y²)/2 and is unbounded below. In genuine UBT, a constraint must follow from a specified single-Theta action, preserve Lorentz/covariant observer consistency, propagate under time evolution, and have a calculated Poisson/Dirac rank; deleting six negative directions by fiat is not an acceptable derivation. Even count 2 positive + 6 negative in pointwise internal pairing does not by itself establish physical propagating DOF of the composite theory.

**Next falsifiable gate**: compute the complete velocity Hessian and primary constraints of one explicit composite Theta ansatz with omega[Theta], g[Theta]; propagate secondary constraints; form the full constraint matrix; calculate reduced quadratic Hamiltonian around a nondegenerate exact solution and check real frequency/energy norms. Unless all pass, S_UBT remains DEFINED_FAMILY_NOT_FINALIZED.

Test: tests/test_information_dirac_ghost_reduction.py.
