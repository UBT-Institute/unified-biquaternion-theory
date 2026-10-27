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

# Orthogonal-only biquaternion fermion construction: exact scope and Hamiltonian selector

**2026-10-26 — exact finite-dimensional Clifford/CAR algebra, NOT a full UBT quantum field theory.** Builds on [BIQUATERNION_INTRINSIC_CAR_SPIN_STATISTICS_GATE.md](BIQUATERNION_INTRINSIC_CAR_SPIN_STATISTICS_GATE.md) and the preexisting SU(3) exterior-Fock track. Investigates the proposal that orthogonal biquaternion components could replace *fundamental* general Grassmann number coefficients. Does **not** assert fermionic spin-statistics from orthogonality alone.

Let B=H⊗_R C≅Mat₂(C), with quaternion units e_i e_j+e_j e_i=-2δ_ij and † satisfying e_i†=-e_i, scalar i†=-i. For vectors u,v∈R³ define e(u)=u_i e_i. Then

  {e(u),e(v)} = -2(u·v)1.

Thus orthogonal u⊥v anticommute, while e(u)²=-||u||². If u,v are **unit orthogonal vectors**, a=(e(u)+i e(v))/2, a†=(-e(u)+i e(v))/2 obey a²=(a†)²=0 and {a,a†}=1. N=a†a is a projection, and Γ=1-2N=i e(u)e(v) is Hermitian, Γ²=1. This is a complete exact CAR algebra for **one fermionic mode**, using only Clifford-orthogonal directions and the already present central imaginary unit. General Grassmann-valued coefficients are not necessary to *represent this operator algebra*.

## Selection/polarization is the missing geometric input

The ordered oriented orthonormal pair (u,v) determines the polarization a. Under a proper rotation **within its plane** by θ,

 u'=cosθ u+sinθ v,  v'=-sinθ u+cosθ v,

we have a'=e^(-iθ)a, N'=N and Γ'=Γ. Thus the occupation operator is independent of the in-plane basis angle. But tilting the plane changes N: Γ encodes its unit normal n=u×v.

On the irreducible complex SU(2) spin representation, an operator H fixed under *all* SU(2) conjugations is proportional to I₂ (Schur's lemma; explicitly [H,σ_i]=0 for i=1,2,3). Therefore a **fixed nontrivial occupation Hamiltonian** H=ωN is not invariant under the whole SU(2); it transforms *covariantly* if its plane/normal is also transformed. UBT must therefore derive a physical or gauge-covariant preferred complex structure/polarization, rather than arbitrarily select e1,e2. This may be linked to an already justified oriented geometric/complex-time structure, but is not selected by bare orthogonality.

## From local CAR to many mutually orthogonal modes

B has complex dimension four and is isomorphic to CAR₁≈Mat₂(C). A **pair** of independent fermion modes requires CAR₂≈Mat₄(C) (complex dimension 16) and cannot be faithfully represented as a unital algebra within the same Mat₂(C). No counting of Theta's four complex *matrix entries* changes that operator-algebra fact.

For many modes use graded tensor products, e.g. Jordan–Wigner:

 c_j=Γ^(⊗(j-1))⊗a⊗I^(⊗(n-j)),

which has exact {c_j,c_k†}=δ_jk and {c_j,c_k}=0. A Hilbert-space orthonormal mode basis alone does NOT force these exchange relations; choosing the CAR representation/graded tensor product is a distinct quantum step. General Grassmann integration is optional calculational technology for coherent-state path integrals, not a microscopic ingredient in this finite-mode operator formulation.

The positive benchmark H=∑_j ω_j c_j†c_j exists for chosen frequencies ω_j>0, but bare orthogonality does not determine ω_j. This is not yet the Lorentz-covariant Dirac field Hamiltonian.

## Geometry and action impact

At fixed chosen Γ, the Hermitian even operator subalgebra of one local CAR mode is span_R{I₂,Γ}, only **two real dimensions**. This by itself cannot furnish four independent real internal tetrad legs. Extra independent modes/derivatives, covariant projections, operator expectation prescriptions or derived bilinear geometry are needed. Unlike classical supercommutative odd Grassmann fields, operator-odd combinations can square to I (Majorana operator a+a†), so no blanket no-go for even geometry from operator CAR follows.

**Decision:** the user's orthogonal-only hypothesis is mathematically viable for the intrinsic *local fermionic operator algebra*, and it genuinely avoids fundamental arbitrary Grassmann coefficients. It is **insufficient** to complete a unified UBT action without explaining (1) how the preferred polarization/grade arises covariantly, (2) how physical spatial/KK modes get the graded tensor product, (3) how a nondegenerate even composite tetrad and Lorentz covariance emerge, and (4) how a unique Hamiltonian/energy scale is selected. Neither existing canonical one-action status nor GR/QM unification is claimed as complete.

Verified symbolic regressions: `tests/test_information_orthogonal_clifford_selector.py` (six locally passing checks).
