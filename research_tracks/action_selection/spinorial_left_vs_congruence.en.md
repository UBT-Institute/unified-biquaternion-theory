<!-- BILINGUAL-UNIT: spinorial_left_vs_congruence -->
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


# Spin(3) left-action versus congruence: corrected interpretation of Dirac obstacle

**2026-10-24, C-tier conditional representation audit.** Corrects any overbroad reading of draft #720. Locked UBT axioms are unchanged.

For U in SU(2)=Spin(3) and X in Mat(2,C), there are distinct mathematically valid group actions:

* Left spinorial action L_U(X)=UX. Since U(2π)=-I₂, L_{-I₂}(X)=-X. Identifying the two columns of X as two fundamental SU(2) spinors, the complex representation decomposes as 1/2 ⊕ 1/2 under spatial rotations.
* Congruence/adjoint action C_U(X)=UXU†. Its 2π central element acts trivially: C_{-I₂}(X)=X, and the representation decomposes as 0 ⊕ 1.

**Hence a four-complex-component biquaternion matrix is perfectly capable of carrying half-integer spin when acted on from the left.** Draft #720's obstruction applies **only if the field itself is required to transform by the congruence/adjoint law**. It is not a no-go against spinors in UBT's underlying quaternion algebra.

A single left SU(2) action is not yet a complete relativistic Dirac representation of Spin(1,3), does not supply right-handed chirality, mass coupling, a time evolution Hamiltonian or a positive physical energy. The matrices and their transformation must be tested against the already locked UBT central tetrad identity and two-sided covariant derivative. For example, spinorial columns of X are not automatically the Lorentz-vector tetrad E_mu in W_L; blindly imposing E_mu→UE_mu can fail to preserve W_L or the central metric. Geometry may instead transform in an induced vector/adjoint representation. A consistent model must explicitly intertwine field, derivative, tetrad and metric representations.

**Main gate for Hamiltonian-first programme:** derive (rather than choose) the physical Spin(1,3) action on Theta and its compatible invariant presymplectic structure, determine whether the candidate Dirac alpha/beta symbols are equivariant, then find the constrained Hamiltonian. Neither left nor congruence alone selects a unique H.

Exact regression: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_left_spin_rep.py' -v\`.
