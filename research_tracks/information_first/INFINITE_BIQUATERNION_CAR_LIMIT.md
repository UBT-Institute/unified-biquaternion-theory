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

# Infinite CAR extension from orthogonal biquaternion factors

**2026-10-26. Exact algebraic inductive-limit construction and conditional free dynamics; NOT the full infinite-volume UBT or GR/QM Hamiltonian.** Extends `FINITE_CAR_EVEN_LORENTZ_DIRAC_BENCHMARK.md` and `ORTHOGONAL_CLIFFORD_HAMILTONIAN_SELECTOR_GATE.md`; canonical one-action status remains unchanged.

## CAR from a countable tower of biquaternion factors

The orthogonal quaternionic units in B=H⊗C ≅ M₂(C), with a=(e₁+i e₂)/2, Γ=1−2a†a, realize CAR₁. For N ordered modes, take
 A_N=B₁⊗...⊗B_N≅M_{2^N}(C)
and inject A_N into A_{N+1} by ι_N(O)=O⊗I₂. With the Jordan–Wigner parity strings define
 c_j^(N)=Γ^(⊗(j−1))⊗a⊗I^(⊗(N−j)).
These satisfy {c_j,c_k}=0, {c_j,c_k†}=δ_jk I and ι_N(c_j^(N))=c_j^(N+1) for all N≥j.

Hence the norm-closed inductive algebra
 A_∞=closure(∪_N A_N) ≅ CAR(ℓ²(N)) ≅ UHF(2^∞).
Any separable infinite-dimensional one-particle complex Hilbert space is isomorphic to ℓ²(N); a flat-spacetime Dirac example is h=L²(R³,C⁴), with a countable orthonormal mode basis. The fields at sharp spatial points are distributions; smeared c(f) are well-defined bounded CAR operators.

Thus the **infinite fermionic algebra itself requires no fundamental general Grassmann-number coefficient fields**. The graded tensor/JW prescription, mode polarization, and quantum interpretation are still genuine physical choices, not automatically forced by an arbitrary classical Theta.

## Dynamics, without taking an ill-defined matrix limit

Choose a positive diagonal one-particle Hamiltonian h e_j=ω_j e_j, ω_j>0. On A_N set H_N=∑_{j≤N} ω_j c_j†c_j. Since number operators of new modes commute with observables built from earlier modes, every local O∈A_M evolves by exp(itH_N)Oexp(−itH_N) independently of N≥M. In particular α_t(c_j)=exp(−iω_j t)c_j. This defines a strongly continuous C*-automorphism group on A_∞, even if the generator is unbounded.

The standard vacuum Fock representation is F_-(h)=⊕_{k≥0}Λ^k h. If h is positive self-adjoint, H=dΓ(h) is a nonnegative self-adjoint many-body generator; finite-particle finite-mode vectors form a natural core for a diagonal h. One should **not** demand operator-norm convergence of H_N as N→∞.

For a physical free Dirac h_D, the ± energy branches require spectral particle/antiparticle polarization. The finite subtraction H_F+2E must NOT be extrapolated as a literal infinite sum of vacuum shifts: that sum is divergent. The positive excitation Hamiltonian uses the second-quantized positive particle and antiparticle energies after choosing a reference vacuum/state.

## What remains a real UBT problem

1. Derive from Theta (rather than choose) the physical complex/quaternionic polarization and local CAR mode algebra.
2. Establish Lorentz-covariant Dirac propagation and graded spacelike locality, not a naïve pointwise nonunitary boost of annihilators (which would violate CAR).
3. Derive a nondegenerate, even rank-four tetrad and spin connection from the **same** physical theory, and close combined constraints.
4. Control continuum UV singularities, renormalized stress-energy, states and any interactions; in curved spacetime a preferred vacuum is not automatic.
5. Derive, instead of assembling, the unique fundamental one-Theta Hamiltonian and action.

**Decision:** the CAR-algebra infinite limit is already mathematically available; its physical UBT realization, gravitational soldering and interactions are the bottleneck. No claim that UBT is unified/finished.

Verification: `tests/test_information_infinite_car_inductive.py` (five finite-cutoff exact-identity tests, locally passing).

Background: https://encyclopediaofmath.org/wiki/AF-algebra ; https://arxiv.org/abs/0911.1304 ; https://arxiv.org/abs/1504.00586 .
