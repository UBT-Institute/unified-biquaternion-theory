<!-- BILINGUAL-UNIT: rotational-hamiltonian-commutant -->
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

# Rotational covariance gate for the information-first UBT Hamiltonian

**2026-10-26. Exact representation-theoretic restriction at a reference timelike carrier; not the complete UBT Hamiltonian.** The four complex coefficient components in the timelike reference chart split under the *chosen ordinary spatial rotation subgroup* SO(3) as C ⊕ C^3 (singlet plus spatial vector). This is not a proof that the full physical Hilbert space equals four complex components, nor an identification of SO(3) with the moving colour SU(3).

Take J_i = diag(0,L_i) with (L_i)_{jk}=-i epsilon_{ijk} acting on the complex 3-vector; [J_i,J_j]=i epsilon_{ijk}J_k. A Hermitian zero-momentum 4x4 Hamiltonian H commuting with all J_i must have the form
  **H(0)=diag(E_s,E_v I_3), E_s,E_v real.**
Proof: the trivial and complex spin-1 irreducible representations are inequivalent, so their cross blocks vanish; by Schur's lemma the spin-1 endomorphism is scalar. Hermiticity makes both coefficients real. This implies the triplet degeneracy at the reference isotropic point but does NOT fix the singlet-triplet gap. Adding full SU(3) covariance on this same linear carrier leaves precisely the same 1⊕3 block structure; gauge SU(3) transformations should not be confused with physical spatial rotations or with propagating gluons.

At finite spatial momentum k, covariance demands U(R)H(k)U(R)†=H(Rk), **not** [H(k),J_i]=0 for fixed nonzero k. Thus spin/momentum couplings and helicity splitting can be allowed; no blanket triplet degeneracy at nonzero k follows. If only real rotations are assumed, the complex vector representation may carry parity-odd epsilon_{ijk}k_k terms; parity/time reversal or other symmetry assumptions must be declared rather than silently imposed.

**Connection to observable correlations.** Let rho be a state invariant under rotations. Then [rho,J_i]=0, and its equal-time phase-insensitive correlation data do not fix E_s,E_v. In fact for rho=I4/4, every Hamiltonian commutes with rho, yielding stationary negentropy and correlation observations. A time-dependent observable with a nonzero singlet-vector matrix element can acquire a phase at angular frequency |E_v−E_s|, providing an operational route to constrain the gap if the transition is observable and dynamics unitary. Absolute overall energy remains unobservable from commutators.

**UTB/UBT gate:** before extrapolating to full Theta/Clifford modes, derive the *actual* rotation action on the physical reduced state space, prove compatible observer algebras and gauge constraints, then enumerate rotational scalars constructed from Theta, its derivatives, and correlations. Rotational symmetry reduces unknown couplings; it does not uniquely determine H and does not resolve split-jet colour conflict.

Check: `tests/test_rotational_hamiltonian_commutant.py`.
