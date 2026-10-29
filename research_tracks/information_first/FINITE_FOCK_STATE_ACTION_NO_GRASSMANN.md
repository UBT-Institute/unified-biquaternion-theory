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

# Finite-mode CAR Hamiltonian to ordinary quantum-state action (without Grassmann variables)

**26 October 2026. Exact finite-dimensional variational construction; a conditional quantum STATE action, not the fundamental UBT field action.** Uses `FINITE_CAR_EVEN_LORENTZ_DIRAC_BENCHMARK.md`.

Given n orthogonal biquaternion CAR factors and a Hermitian Fock-space Hamiltonian H_F on Hilbert space F≅C^(2^n), represent the quantum state by a normalized complex vector Φ(t)∈F, Φ†Φ=1. The *ordinary complex-number* first-order action is
 S_fin[Φ,λ]=∫dt [ (i/2)(Φ†dot Φ−dot Φ†Φ)−Φ†H_F Φ+λ(Φ†Φ−1)].
Here λ(t)∈R. Vary Φ and Φ† independently in the usual complex variational bookkeeping (then impose conjugation), giving
 i dot Φ=(H_F−λ I)Φ, Φ†Φ=1.
A time-dependent global phase of Φ shifts λ and changes the Berry term by a boundary phase. Choosing λ=0 gauge yields ordinary Schrödinger evolution. Since H_F†=H_F, d/dt(Φ†Φ)=0. This action is finite and no Grassmann coefficients or Berezin measures are required for its definition. In particular the four-mode Hamiltonian of the companion note acts on Φ∈C^16 and has nonnegative excitation spectrum after choice of filled negative-energy reference vacuum.

**Physical parity note:** H_F conserves fermion-number parity. Coherent superpositions across even and odd parity sectors must respect the usual fermion-parity superselection requirement when modeling physical observables; the full vector action is a convenient mathematical representation and need not identify every normalized vector as a physically preparable state.\n\n**Scope:** this is quantum mechanics on a 16-dimensional Fock space, built by *choosing* four graded CAR modes and H_F. It does not derive the probabilities/Born rule, physical spatial locality, the four independent CAR factors as one local Theta field, spacetime geometry, or a common covariant off-shell UBT action. It also requires specifying a time parameter; time-reparametrization/gravity constraints of UBT are not yet included. It cannot be substituted for S_UBT[Theta]. The purpose is to show the finite-mode Hamiltonian-to-action step is mathematically complete without general Grassmann numbers, isolating where real gravitational soldering remains missing.

Regression: `tests/test_information_finite_fock_variation.py`.
