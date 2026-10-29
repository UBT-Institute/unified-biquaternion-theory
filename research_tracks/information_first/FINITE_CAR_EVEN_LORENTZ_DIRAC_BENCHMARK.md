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

# Two-mode even Lorentz bilinears and a four-mode finite Dirac Hamiltonian

**26 October 2026 — exact FINITE-MODE operator-algebra benchmark. NOT a canonical UBT tetrad, full Lorentz-covariant CAR field, or a derived unified action.** This follows the orthogonal-only Clifford/CAR program in `ORTHOGONAL_CLIFFORD_HAMILTONIAN_SELECTOR_GATE.md` and `BIQUATERNION_INTRINSIC_CAR_SPIN_STATISTICS_GATE.md`. No independent fundamental Grassmann coefficient variables appear.

## A. Two quaternionic CAR factors yield a real four-dimensional even sector

Take B=H⊗C≅M₂(C), a=(e₁+i e₂)/2, Γ=1−2a†a. In two ordered factors of B let
  c₁=a⊗I₂,   c₂=Γ⊗a.
These satisfy {c_i,c_j†}=δ_ij and {c_i,c_j}=0. Let σ₀=I₂, σ₁,σ₂,σ₃ be the standard Hermitian Pauli matrices. Define four **even Hermitian** operators
  B_μ=∑_{i,j=1}² c_i† (σ_μ)_{ij}c_j,  μ=0,1,2,3.
They are linearly independent as operators on Fock space C⁴. Their restriction to the one-occupation subspace F₁=span{c₁†|0>,c₂†|0>} is exactly the Hermitian 2×2 basis σ_μ. The compressed matrix
  X(x)=∑_μ x^μ B_μ|_{F₁}=x⁰I₂+∑_i xⁱσ_i
satisfies
  det X(x)=(x⁰)²−(x¹)²−(x²)²−(x³)².
Thus the **algebraic internal space of even two-mode bilinears** carries the Lorentzian determinant form. The Pauli/trace identity yields η=diag(1,−1,−1,−1). The spatial bilinears satisfy [B_i,B_j]=2i ε_ijk B_k. This is a kinematical Spin(3) action, not yet gravity.

For S∈SL₂(C), X↦SXS† preserves determinant, giving the usual proper Lorentz *vector representation*. However this generally is **not implemented by a simple CAR-preserving linear transformation** c↦Sc, because {Sc,(Sc)†}=SS†≠I for nonunitary boosts. For example S=diag(e^(t/2),e^(−t/2)) yields diag(e^t,e^(−t)). A Lorentz-covariant physical construction must account for time slicing, metric/inner product or a suitable induced representation; one cannot simply identify Lorentz boosts with finite-site unitary CAR automorphisms. This is a genuine remaining compatibility gate.

The four internal B_μ alone do **not** constitute four spacetime 1-forms E^a_μ(x), nor establish det E≠0 or the locked E∝DTheta. A spacetime soldering map and nondegenerate Jacobian must be derived separately.

## B. Four-mode CAR Hamiltonian: complete finite Dirac/Fock example

Use four ordered B factors, with JW annihilators c_j=Γ^{⊗(j−1)}⊗a⊗I^{⊗(4−j)}. On the 16-dimensional Fock space define the quadratic number-conserving operator
  H_F(p,m)=∑_{i,j=1}⁴ c_i† [h_D(p,m)]_{ij} c_j,
  h_D(p,m)=α·p+β m,
  α_i=diag(−σ_i,+σ_i), β=[[0,I₂],[I₂,0]].
By the Clifford relations, h_D²=(|p|²+m²)I₄; the one-particle eigenvalues are (−E,−E,+E,+E), E=sqrt(|p|²+m²). Four CAR annihilators are operators in the tensor power of biquaternion algebras; their coefficients are ordinary complex numbers, not formal Grassmann generators.

At p=(0,0,3),m=4, E=5 the exact many-body eigenvalues of H_F and multiplicities are:
  −10:1, −5:4, 0:6, +5:4, +10:1.
With vacuum-reference subtraction H_exc=H_F+2E I₁₆, the exact energy levels are
  0:1, 5:4, 10:6, 15:4, 20:1.
Consequently H_exc≥0 at this regulated point. For generic real p,m the same spectral combinatorics give levels k E (k=0..4) after subtraction. The two negative Dirac branches must be filled in the chosen reference vacuum; this is a standard finite-mode Fock construction, NOT spontaneous derivation of vacuum, locality or relativistic field theory from UBT.

A finite-mode, ordinary operator evolution is then i∂_t|Ψ_F>=H_exc|Ψ_F>. A phase-space fermionic coherent-state path integral may use Grassmann parameters computationally, but these are not required to write the physical operator Hamiltonian or state evolution.

## C. What this resolves and what remains

Proved: exact CAR from orthogonal B directions; even bilinear 4-vector and Lorentzian determinant on F₁; explicit four-mode Dirac/Fock Hamiltonian with nonnegative vacuum-relative spectrum; five passing symbolic regressions.

Not proved: uniquely derived choice of quaternionic polarization; physical local Lorentz boosts acting consistently with CAR and the Hilbert norm; spatial field anti-commutators/microcausality; a rank-four spacetime tetrad from the **same** operator carrier; coupling and closure of gravitational constraints; one covariant off-shell fundamental action and UBT mass/energy normalization.

The Einstein–Dirac action remains a **reference effective action**, not the final UBT action. Keep `canonical/ACTION.en.md` status `DEFINED_FAMILY_NOT_FINALIZED`.

Executable: `tests/test_information_finite_car_lorentz_dirac.py` (5 focused locally passing cases).
