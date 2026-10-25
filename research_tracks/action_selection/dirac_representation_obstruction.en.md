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

# Dirac-factorization gate: vector-congruence Theta is not a Dirac spinor

**C-tier exact representation-theoretic obstruction, 2026-10-24.** Follows draft #719's dimension-only factorization. The result applies to the *locked* action of spatial Spin(3)=SU(2) on Theta by congruence X↦UXU†, and to the usual Dirac action under the same spin group. It is not a no-go for emergent spinors or a distinct carrier representation.

## The 2π test

Let U(θ)=exp(-iθσ3/2). The congruence representation on the four-complex-dimensional vector space Mat(2,C), R_C(U):X↦UXU†, is complex linear in X. At θ=2π, U=-I2, so
\[
R_C(-I_2)X=(-I_2)X(-I_2)=X
\]
for every X. Thus R_C(-I2)=+I4. In contrast the standard four-component Dirac spinor rotation representation R_D(U)=diag(U,U) gives R_D(-I2)=-I4. If an invertible complex-linear intertwiner T obeyed T R_C(U)=R_D(U)T for all U∈SU2, the central element would force T=-T and hence T=0. **No invertible intertwiner exists.** In fact no nonzero linear intertwiner exists between these two representations of SU2.

This also follows from their decomposition on rotations: Mat(2,C)=span(I2) ⊕ span(σ_i) ≅ spin 0 ⊕ spin 1, whereas the Dirac carrier ≅ two copies of spin 1/2. Different central character and different irreducible content cannot be fixed by reordering entries.

## Meaning for Hamiltonian-first UBT

The 4×4 Clifford matrices in #719 satisfy the Dirac square-root identity as linear algebra on C⁴, but simply defining Ψ=vec(Theta) does NOT create a Lorentz-covariant physical Dirac Hamiltonian for canonical congruence Theta. Likewise a putative invariant linear derivative symbol on the congruence representation needs an independent covariance and symplectic compatibility proof. Avoid introducing a spinor index or independent field to evade this theorem without deriving it from the original structure.

Paths not excluded: (a) Dirac spinors as *emergent* excitations with nonlinear/topological transformation or spinorial sections; (b) a separate **derived** carrier representation of an existing Theta-based composite operator; (c) alternative first-order systems transforming as tensors (not to be mislabelled Dirac). These all require a fully specified dynamical generator, physical symplectic form and covariance test.

**Next sharp test:** classify first-order translation-invariant linear differential operators equivariant under the rotations induced by U X U† on the vector carrier, and check whether any allowed symbol squares to scalar relativistic dispersion without adding a non-derived Clifford carrier. Even a positive answer to this narrower rotation test would require Lorentz boosts and the physical constraint/symplectic analysis.

Reproduction: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_dirac_representation_obstruction.py' -v\` (exact SymPy).
