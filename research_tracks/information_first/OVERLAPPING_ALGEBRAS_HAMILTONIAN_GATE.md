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

# Overlapping observer algebras: an exact uniqueness boundary for modular-time reconstruction

**2026-10-26 — finite-dimensional control theorem, not a UBT action/Hamiltonian.**

Consider H=(C²)_a tensor (C²)_b tensor (C²)_c. Accessible von Neumann algebras A_ab=B(H_a tensor H_b) tensor I_c, and A_bc=I_a tensor B(H_b tensor H_c). Their intersection is I_a tensor B(H_b) tensor I_c. Their union generates B(H_abc).

**Weak information: overlap data cannot reconstruct full dynamics.** For the family
H(alpha,beta)=omega Z_b+alpha Z_a+beta Z_c
the Heisenberg derivation i[H,O_b] on all overlap observables O_b is independent of alpha,beta. Thus matching arbitrary modular or physical flows *only on the overlap* leaves at least two independent coefficients unconstrained. Even knowing common entropy and geometric compatibility there does not close the gap. Note: these particular H preserve A_ab and A_bc; independent local observers who know full derivations on their entire algebras can distinguish the parameters.

**Strong information: conditional uniqueness modulo center.** If two self-adjoint generators H,H' induce the same Heisenberg derivation on every operator in each A_ab and A_bc, then Delta=H-H' commutes with both algebras. Since A_ab and A_bc jointly generate B(H_abc), the commutant is C I, and Delta=cI. Hence sufficiently rich fully calibrated local dynamics fixes H up to an additive identity. This requires knowing the *actual derivation of all local observables*, not merely observer state entropies, modular spectra or geometric state-space structures.

For QFT or gravity the union algebra, centers/edge modes, constraints and operator domains can invalidate the naive full matrix-algebra conclusion. Physical time normalization must be known; modular flow alone is state- and region-dependent. Additive identity shifts can contribute differently once geometry/energy renormalization is dynamical.

**UBT decision gate**: construct Theta-induced observer algebras and their overlap inclusions; prove a common time derivation exists, verify its action on the full generating algebras (not entropy alone), compute its commutant including gauge and boundary centers, and THEN reconstruct the microscopic H modulo gauge/center. Derive its presymplectic form and action independently of the assumed H to avoid circularity. Investigate composite spin connection and first-/second-class constraints. No claim of a closed single-Theta action.

Regression: tests/test_information_overlap_generator_gate.py.
