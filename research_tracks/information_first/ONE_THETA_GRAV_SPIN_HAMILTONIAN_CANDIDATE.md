> **FERMIONIC ORDERING UPDATE (2026-10-26):** The determinant identity below assumes commuting Theta entries. For Grassmann-odd Theta the actual invariant Dirac mass uses the antisymmetric Weyl pairing B=u^T epsilon v, and m Psi† beta Psi=-m(B+B†), not the naively ordered determinant. See [graded Hamiltonian/action gate](GRASSMANN_SPINOR_HAMILTONIAN_ACTION_GATE.md). The one-Theta tetrad-versus-fermionic-parity obstruction also remains open.

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

# Concrete candidate Hamiltonian: one-biquaternion Dirac sector plus MM/ADM gravity

**2026-10-26. A COMPUTED conditional benchmark, not a uniquely derived UBT action.** This note deliberately stops imposing delta det(Theta)=0: Lorentz scalar invariance does NOT mean field constancy. A determinant term only conflicts with shifts if the shifts are stipulated as exact gauge symmetries of the full action; pure MM gravity has them but unified dynamics may modify them and hence requires new constraints.

## Explicit spinor Hamiltonian from a single Theta

Write Theta=[u v], u,v∈C², ε=iσ₂=[[0,1],[-1,0]], R=ε conjugate(v). The map Theta→Psi=(u,R) is invertible **real-linearly** and Spin⁺(1,3)-equivariant under the conditional left action Theta→STheta. Set hbar=c=1, Pauli matrices σᵢ and pᵢ=-i∂ᵢ, and use the previously verified Dirac factorization alphaᵢ=diag(-σᵢ,+σᵢ), beta=[[0,I],[I,0]]. On a fixed Minkowski slice define the candidate energy functional
 H_spin[Theta] = ∫d³x [u†(-σ·p)u + R†(σ·p)R + 2m Re det Theta].
The kinetic bilinear may be symmetrized by integration by parts with prescribed decay/boundaries. Its Hamiltonian operator squares to (-Δ+m²)I₄ and has E=±sqrt(k²+m²). The mass relation is exact: R†u=det Theta, thus Psi†beta Psi=2Re detTheta. The coefficient m and the kinetic normalization are **NOT** selected by the biquaternion algebra.

If one *assumes* Grassmann-odd Psi and the standard first-order Dirac symplectic term, the flat action is
 S_spin=∫dt d³x [ (i/2)(Psi†dot Psi-dot Psi†Psi)-Psi†(-i alphaᵢ∂ᵢ+m beta)Psi ].
Then momentum constraints are pi_Psi-(i/2)Psi†≈0 and pi_Psi†+(i/2)Psi≈0 in an ordered graded convention; their Dirac brackets lead to standard fermion CAR after quantization. **This is an assumption about statistics, not an algebraic theorem:** an ordinary commuting Theta cannot be made Grassmann-odd by invertible real-linear map. The displayed action is therefore a benchmark for what the single-field theory must generate.

## Minimal combined constraint target

For the torsionless spin-structure Einstein–Dirac benchmark,
 H_target=∫d³x [N(C_ADM+C_D)+N^i(C_i,ADM+C_i,D)+lambda_ab G^{ab}_Lorentz+fermionic primary multipliers]+H_boundary.
The ADM gravity constraint is
 C_ADM= (2κ/sqrt(h))(pi_ij pi^ij-(pi²)/2) -(sqrt(h)/(2κ))(³R-2Λ).
The curved-spinor C_D and C_i,D must be computed using a specific orthonormal frame, spin connection, Grassmann convention and connection/torsion treatment; substituting the flat H_spin density as C_D without lapse/connection factors is wrong. An independent spin connection can yield torsion/contact interactions absent from the torsionless benchmark; choice must be derived. The known MM action gives the pure gravity equations in the selected branch, not yet this matter-coupled action.

## Exact compatibility gates

(1) The locked geometric tetrad E∝DTheta lives in a Lorentz-real congruence representation, whereas Theta under pure-left spin transformation lives in a Weyl representation. The known intertwiner obstruction remains; the bilinear X=Theta Theta† supplies a vector but does not satisfy the old locked tetrad formula without further proof.
(2) A determinant mass respects proper Lorentz left transformations but generally breaks common Theta phase U(1) to Z₂; no arbitrary delta det=0 should be imposed.
(3) The MM split-jet shift is gauge for gravity alone, not automatically for the mass term. Adding spinor dynamics can change gauge constraints and physical DOFs. Do not carry over the previous four shift first-class constraints without recomputing the constraint algebra.
(4) Fermionic statistics and a nonnegative renormalized physical Fock Hamiltonian do not follow from the classical c-number H_spin, whose one-particle spectrum has ± branches.
(5) Compact psi-time dynamics, gauge triplet and information correlations are not in this candidate. Their sum must not be declared the complete UBT action.

**Status:** flat spinor operator and mass explicitly constructed using one Theta; gravity ADM constraint available conditionally; a single off-shell covariant action compatible with locked UBT geometry/statistics is NOT derived.

## Grassmann ordering correction (essential)

The equality R†u=det Theta in this note and its SymPy regression is an identity for **commuting complex entries**. For independent Grassmann-odd entries, moving v through u changes signs: with the displayed component order, R†u=v₁u₀-v₀u₁ = -(u₀v₁-u₁v₀)=-det Theta. The Hermitian-conjugate companion also needs explicit graded ordering. Thus the mass written as +2m Re detTheta is **not yet established** as the correctly ordered fermionic mass under a graded promotion. One must choose a Grassmann algebra, adjoint/order convention and recompute the invariant bilinear before presenting a fermionic UBT action. This is an additional concrete obstruction; do not use the commuting symbolic identity to prove a fermionic action.
