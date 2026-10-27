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

# Joint symmetry commutant: SO(3), SU(3), U(1), and the momentum gate

**2026-10-26. Exact finite-representation classification, not a derivation of the full UBT Hamiltonian.** Extends `ROTATIONAL_HAMILTONIAN_COMMUTANT.md` and `SU3_ROTATIONAL_HAMILTONIAN_GATE.md`.

At the timelike reference point take V=C_s ⊕ C³_t. The natural coefficient-space spatial SO(3) is a subgroup of the SU(3) frame group acting on the same triplet; DO NOT treat them as independent tensor factors. For a Hermitian, momentum-zero endomorphism H, the common commutant is **R P_s ⊕ R P_t**:
  H(0)=E_s P_s+E_t P_t, P_s=diag(1,0,0,0), P_t=diag(0,1,1,1).
Its real dimension is two, reduced to one measurable gap after quotient by H->H+c I4.

An internal U(1) with generator Q=q_s P_s+q_t P_t, whether q_s=q_t (overall phase) or unequal, commutes with both projectors and does not further select E_s or E_t. On this carrier U(1) and SU(3) therefore leave the commutant unchanged. Enlarging the symmetry family cannot automatically eliminate the remaining energy gap.

At fixed nonzero momentum, distinguish TWO different assumptions:
(A) ordinary spacetime rotational covariance: U(R)H(k)U(R)^†=H(Rk), permitting terms like singlet-vector mixing proportional to k and vector helicity splitting proportional to i epsilon_ijk k_k;
(B) independent global internal SU(3) invariance at each fixed k: [H(k),T_a]=0. This forces H(k)=A(k)P_s+B(k)P_t, suppressing those mixing and polarization terms. Rotational covariance then implies A(k)=A(|k|), B(k)=B(|k|). Treating the same SO(3) subgroup as independent internal and external actions without specifying the momentum transformation is inconsistent.

The set of **possible** additional spacetime/involution constraints (Lorentz covariance, complex conjugation, charge conjugation, parity, time reversal, local gauge constraints, diffeomorphism invariance) must each be represented on the *physical reduced state space*, not imposed as extra commuting matrices by name. Local gauge SU(3) implies Gauss constraints rather than a naive global colour Hamiltonian block, and the existing moving SU(3) colour frame is not yet a propagating gauge field.

**Selection result:** SO(3)+the same-carrier SU(3)+diagonal U(1) still leave at least one undetermined energy gap at k=0 and two real dispersion functions A(|k|), B(|k|) for k≠0 under assumption (B). Thus this symmetry stack does **not** uniquely select H_UBT. Observed time-dependent cross-sector correlations may constrain the gap where allowed by gauge superselection, but entropy alone does not. A Lorentz-covariant local action, its constraints, and positivity must supply further restrictions.

Executable exact commutant test: `tests/test_information_joint_symmetry_commutant.py`.
