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

# Missing spinor sector: conditional Einstein–Dirac Hamiltonian and UBT representation gate

**2026-10-26. Reference calculation only: not a single-Theta fundamental action or a completed first-class Dirac analysis of composite MM gravity.** Cross-check against `research_tracks/action_selection/dirac_factorization_hamiltonian.en.md`, `spinor_tetrad_intertwiner_gate.en.md`, and `research_tracks/information_first/MM_ADM_HAMILTONIAN_BRIDGE.md`.

## 1. Fixed-background Dirac factorization is already present

For a chosen identification vec(Theta)↦Psi∈C⁴ and chosen Clifford representation on flat background,
 h_D(p)=c alpha^i p_i+beta m c², {alpha^i,alpha^j}=2δij, {alpha^i,beta}=0, beta²=I.
Hence h_D²=(c²p²+m²c⁴)I and the one-particle spectrum has ± branches. This is **not** a positive bounded-below single-particle Hamiltonian without specifying the physical fermion Fock construction, filled vacuum/renormalization and constraints. Linear spinor factorization neither makes Psi Grassmann-odd nor proves its emergence from commuting Theta components.

## 2. Conditional standard Einstein–Dirac reference action

Assume a spin structure, independent anticommuting Dirac carrier Psi and a compatible tetrad e and spin connection omega(e) on a globally hyperbolic spacetime. The benchmark classical action is
 S_ref=S_EH[e]+∫d⁴x e [ (i/2)(bar Psi gamma^mu nabla_mu Psi-(nabla_mu bar Psi)gamma^mu Psi)-m bar Psi Psi ],
with suitable boundary terms, hbar=c=1. This is a **separate reference action**: inserting it in UBT would violate the one-Theta derivation rule until Psi=F(Theta) and the induced spin structure/statistics/symplectic form are demonstrated.

In ADM on a prescribed time gauge tetrad, the spinor Hamiltonian enters schematically via
 H_ref=∫d³x [N(C_grav+C_D)+N^i(C_i,grav+C_i,D)+lambda_ab G_Lorentz^{ab}]+H_boundary,
where the fermionic C_D and C_i,D are defined by the Legendre transform of the above covariant Dirac density and depend on triad/spin connection conventions; do **not** conflate the flat expression Psi†(-i alpha^i partial_i+beta m)Psi with a generally covariant lapse constraint. Spinor momenta are constrained by the first-order kinetic form. With a standard symmetrized flat Dirac Lagrangian, pi_Psi=(i/2)Psi† and pi_Psi†=-(i/2)Psi, hence second-class graded canonical constraints; their reduced graded brackets yield the CAR after quantization. In gravity the Gauss, diffeo and Hamiltonian constraints and any torsion-induced four-fermion terms must be handled consistently. A torsion-free Levi–Civita spin connection inserted by hand and an independently varied Einstein–Cartan connection are distinct benchmark models.

## 3. Direct UBT obstruction, not merely a missing equation

The fixed Lorentz-real tetrad E∝DTheta transforms by Lorentz congruence (S E S†), whereas a pure left spinor Theta→STheta has derivative DTheta→S DTheta. These cannot simultaneously coincide for a generic invertible tetrad, as already proved in the intertwiner gate. Flattening Theta∈Mat(2,C) to C⁴ changes the representation on coefficients, not this transformation law. Thus even if the reference h_D factorizes the mass shell, it is **not** yet the Hamiltonian of the actual single Theta field.

A physically meaningful bridge must:
(1) construct an equivariant nonlinear soldering F(Theta,E,omega) with its correct transformation law and no second independent fundamental field;
(2) derive, rather than assume, the fermionic graded presymplectic structure/statistics and nondegenerate positive physical inner product;
(3) show compatibility with the split-jet shifts that keep E fixed, or modify/derive the exact constraint generators;
(4) perform the first-order connection/torsion and fermionic graded Dirac constraint reduction, then compare with the ADM gravity constraints;
(5) show the quantum Hamiltonian bounded below in its physical sector and retain gauge-invariant colour observables if claimed.

## 4. Exact small verification

The flat 4x4 Dirac anticommutator checks and the graded-momentum algebraic normalization are in `tests/test_information_spinor_missing_bridge.py`. The tests cannot establish a covariant one-field map or fermionic emergence.
