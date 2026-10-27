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

# Intrinsic fermionic CAR in the biquaternion algebra: a constructive bridge

**2026-10-26. Exact finite-mode operator-algebra construction; NOT a completed spin-statistics theorem, fermionic field theory, or the fundamental UBT action.** Responds to the observation that biquaternion elements exhibit commuting AND anticommuting sectors. Explicitly distinguishes operator CAR from classical Grassmann-odd fields. Cross-references: `canonical/bridges/fermionic_statistics_bridge.tex`, `research_tracks/THEORY_COMPARISONS/su3_qubit_mapping/fermionic_fock_su3_decomposition.md`, `research_tracks/T2_GAUGE/su3_su2_even_fock.en.md`, `research_tracks/information_first/GRASSMANN_SPINOR_HAMILTONIAN_ACTION_GATE.md`.

## 1. Exact algebra

Let B=H⊗_R C≅M₂(C), with quaternion generators e_i e_j=-δ_ij+ε_ijk e_k, e_i†=-e_i, and a commuting scalar imaginary unit i†=-i. For arbitrary p=p0+u and q=q0+v, vector products are over C and
 [p,q]=2u×v,
 {p,q}=2(p0 q0-u·v +p0 v+q0 u).
So generic elements are neither commuting nor anticommuting in toto. Orthogonal quaternion units satisfy {e_i,e_j}=0 when i≠j; this is a Clifford relation, not yet fermionic CAR.

Define
 a=(e1+i e2)/2,    a†=(-e1+i e2)/2.
Direct multiplication gives **{a,a}=0, {a†,a†}=0, {a,a†}=1**, and N=a†a is an idempotent projection. The fermion parity Γ=1-2N has Γ²=1, ΓaΓ=-a. This furnishes an exact **single-mode CAR *-algebra**: CAR₁≅M₂(C)≅B. No external Grassmann coefficients are needed to REPRESENT a quantum annihilation/creation operator. In a Pauli representation e_i=-iσ_i, a=-i|0⟩⟨1| and Γ=σ₃. This does not imply a generic B-valued commuting field is already quantized as a fermion; the choice of a, parity Γ and a Hilbert-space representation are part of the quantum interpretation.

## 2. Many-mode extension: graded tensor/Jordan–Wigner

For n ordered copies of B, set
 c_j=Γ^(⊗(j-1))⊗a⊗1^(⊗(n-j)), j=1,...,n.
Then {c_j,c_k}=0 and {c_j,c_k†}=δ_jk 1 on (C²)^(⊗n), by the Γ anticommutation with a. The simple tensor a⊗1,1⊗a WITHOUT the Γ string would commute and violate cross-mode fermionic locality. Thus the graded tensor product / JW ordering is an **essential selection**, not automatic from one local quaternion.

For four independent Dirac annihilation modes at one regulated spatial site, CAR₄ acts on a 16-complex-dimensional Fock space (full operator algebra M₁₆(C)), not on a single M₂(C). In a continuum, appropriate local field CAR and microcausality must be imposed or derived with a chosen quantum net, rather than identifying the four complex c-number components of Theta with four CAR annihilation generators.

This connects precisely to the existing SU3 exterior-Fock/JW track; it does not independently discover a new SU3 triplet mechanism.

## 2a. Explicit positive fermionic mode Hamiltonian

For two ordered modes in B⊗B, take c₁=a⊗1 and c₂=Γ⊗a. Their number operators N_j=c_j†c_j satisfy N_j²=N_j, and with arbitrary chosen positive frequencies ω_j define the **normal-ordered operator Hamiltonian**
  H_f=ω₁N₁+ω₂N₂.
Its eigenvalues are exactly {0,ω₁,ω₂,ω₁+ω₂}, and [c_j,H_f]=ω_j c_j, giving i∂_t c_j=[c_j,H_f] in the Heisenberg picture. This is a bona fide finite-dimensional fermionic Hamiltonian assembled from biquaternionic factors, with no separate fundamental Grassmann-valued coefficient fields. Coherent-state functional integrals for it may use Grassmann integration as a REPRESENTATION of the same quantum operator algebra, without making Grassmann variables a new elementary carrier.

However the frequencies are inputs, not selected by B alone, and H_f is NOT yet the Lorentz-covariant UBT Dirac field Hamiltonian nor its coupling to the locked composite GR tetrad. The full field theory additionally requires infinitely many spatial/momentum modes and covariant locality.

## 3. Grading and gravity: correction of an overgeneralization

The earlier single-Theta argument that **pure Grassmann-odd classical supercommuting Theta** has no invertible even c-number tetrad from E=DTheta remains valid under those assumptions. It must NOT be extended to an operator CAR-valued odd Theta: an odd self-adjoint Majorana operator Q=a+a† obeys Q²=1, so an even product of odd CAR operators may have an invertible identity component/nonzero expectation. Fermion bilinears can therefore source bosonic, even geometric observables in principle. But this does NOT build an invertible, rank-4, Lorentz-covariant tetrad from the locked E∝DTheta. A derived even soldering/expectation prescription, its symmetries, rank and dynamics are missing.

There is also a **polarization problem**: parity Γ=σ₃ selects an axis. Full SU(2) conjugation rotates it; a fixed Γ does not commute with arbitrary SU(2) rotations. A covariantly varying Γ(Theta) might be possible but requires a physical gauge-covariant axis and connection. The Pauli/Clifford anticommutators are covariant as an algebra even when a chosen local annihilation operator is not invariant.

## 4. Odd winding is not exchange statistics by itself

The older canonical note `canonical/bridges/fermionic_statistics_bridge.tex` argues that the half-period shift ψ→ψ+πR creates (-1)^n and equates that with exchange statistics. The first algebraic phase is exact. But identifying an INTERNAL half-circle shift with a TWO-PARTICLE exchange path is an additional topological/dynamical assertion; the KK phase alone does not establish it.

**Counterexample:** take two symmetric, identical bosonic n=1 KK wave packets with joint factor exp[i(ψ₁+ψ₂)/R]. Exchanging labels 1↔2 leaves the wavefunction unchanged (+1), whereas shifting only ψ₁ by πR multiplies it by -1. Consequently odd KK winding alone cannot force Berezin integration/CAR. The earlier asserted exchange-path identification must be independently derived in the physical configuration space before the stronger claim can stand. This audits, but does not silently rewrite, the canonical bridge.

## 5. Consequences for the Hamiltonian-to-action programme

**Positive:** intrinsic B algebra supplies exact local CAR₁ and an even observable sector. This makes a graded/operator-algebra route more promising than treating all entries of Theta exclusively as commuting c-numbers or as independent classical Grassmann generators.

**Unclosed:** derive (a) physical grading and local oscillator polarization from existing Theta/tetrad symmetries, (b) many-mode CAR and locality, (c) Lorentz-covariant Dirac kinetic Hamiltonian/action with its Fock representation, (d) an even rank-four composite tetrad and the gravitational constraints from the SAME underlying dynamics. One cannot yet mark the UBT Hamiltonian or action finalized.

Six focused algebraic/test counterexamples verified locally: `tests/test_information_biquaternion_car.py`.
