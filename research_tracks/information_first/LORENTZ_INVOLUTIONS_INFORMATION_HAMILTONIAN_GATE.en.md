<!-- BILINGUAL-UNIT: lorentz-involutions-information-hamiltonian-gate -->
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

# Lorentz, biquaternion involutions, CPT and information: Hamiltonian selection gate

**2026-10-26. Exact restricted-representation results, not a full UBT Hamiltonian.** Continues `JOINT_SYMMETRY_COMMUTANT_SELECTION.en.md`. Uses canonical/algebra/involutions_Z2xZ2xZ2.tex and canonical/symmetry/step1_CPT_definitions.tex; their transformations on field arguments and complex time must not be conflated with purely internal matrices.

## I. Restricted zero-momentum reference carrier

Write V=C 1 ⊕ C³ with H0=E_s P_s+E_t P_t (real energies) from the SO(3)/SU(3) commutant. The quaternion conjugation P2 on this coefficient carrier acts diagonally diag(1,-I3), while axis flip P3=diag(1,+1,-1,-1) (on 1,I,J,K components). Both commute with H0. Complex conjugation P1 is anti-linear on complex coefficient space: P1 H0 P1^{-1}=H0 for real E_s,E_t. Thus these involutions place **no additional constraint** on E_t-E_s at this reference point. Their transformations of derivatives and spacetime coordinates may impose further restrictions on the full differential operator, but they have not been shown to fix the gap.

Caution: antiunitary time reversal obeys T e^{-iHt} T^{-1}=e^{+i(THT^{-1})t}, together with t->-t, rather than a naive ordinary complex-linear commutator. C, P, and T representation-dependent mappings between particle/antiparticle, momentum and time-reversed sectors cannot be replaced by demanding each acts trivially on H0.

## II. Lorentz covariance is not ordinary commutation with boosts

For Λ in proper Lorentz group, a relativistic field operator D(p) is covariant by D(Λp)=S(Λ)D(p)S(Λ)^{-1} in the appropriate representation (and with domain/bundle qualifications). A fixed finite-dimensional positive-definite Hilbert space carrying the usual nontrivial four-vector boosts cannot implement Lorentz boosts unitarily: the boost B(χ) is η-orthogonal, B^TηB=η, but B^TB≠I for χ≠0. Consequently adding Lorentz boosts as *Hermitian unitary symmetry generators of the same four-dimensional positive-definite carrier* is invalid. In QFT Lorentz acts unitarily on an infinite-dimensional physical state space while finite-dimensional field components transform nonunitarily. The existing positive timelike metric K⁺_Theta is field-dependent/covariant and does not by itself turn the fixed four-vector representation into a unitary representation of boosts.

Without a specified local differential operator, physical Hilbert space and constraint reduction, Lorentz covariance alone does not determine E_s or E_t. A separate relativistic dispersion relation may follow only after specifying the Lorentz representation and field equations; it is not licensed by treating H0 as a literal relativistic single-particle energy.

## III. Do information constraints fix the remaining gap?

Let rho_p=diag(p,(1-p)/3,(1-p)/3,(1-p)/3), 0<p<1. This density operator is SU(3), SO(3), U(1) and reference-involution invariant and commutes with **every** H0=E_s P_s+E_t P_t. Its entropy, negentropy, stationarity and invariant same-time correlation data are compatible with arbitrary gap Δ=E_t-E_s. Imposing compatibility among observer reductions of rho_p likewise does not choose Δ. Thus purely *static* shared-reality/information constraints do not close selection, even after the available symmetries.

A conditional genuinely discriminating information constraint is **time-dependent phase-sensitive cross-sector correlation** where allowed by gauge superselection: for O=|s><v|+h.c., a prepared coherent |ψ>=(|s>+|v>)/sqrt2 gives <O(t)>=cos(Δt) (ħ=1). This determines |Δ| from physical time-resolved data, but assumes physical coherent states and observables, an independently calibrated clock and appropriate gauge invariance. If SU(3) is a true local gauge symmetry and s/v belong to inequivalent charge sectors, O is not gauge invariant and the proposed measurement is forbidden; then use gauge-invariant composites/relational observables. This is an observable constraint/parameter measurement, NOT derivation of a unique microscopic Hamiltonian from negentropy.

A stronger conditional modular constraint rho∝exp(-βH) gives H=-(log rho)/β+const, but β, reference algebra, KMS condition, clock and positivity must be independently fixed. It must not be advertised as emergent action derivation. Correlation entropies plus all these symmetries still do not determine the gravitational action, the eight-real Theta dynamics, local SU(3) connection or reduced Dirac Hamiltonian.

**Decision:** the named symmetries do not uniquely select H_UBT. Route B can supply additional *operational* dynamical correlation conditions, not an assumed entropy extremum. The next physically meaningful task is a constrained, Lorentz-covariant gauge-invariant observable algebra and its correlation evolution; only then an inverse generator and compatibility with MM/Einstein sector.
