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

# Infinite free Dirac field from biquaternionic CAR factors: spectral, causal and action gates

**27 October 2026 — conditional free quantum field construction on fixed Minkowski background.** The infinite CAR algebra is mathematically available from the nested biquaternion factors in `INFINITE_BIQUATERNION_CAR_LIMIT.md`. Here we check the physical particle/antiparticle polarization and the continuum locality gate. This is a reference *free Dirac QFT* realization, NOT a uniquely derived one-Theta Hamiltonian, matter/gravity coupling, or finalized UBT action.

## Exact one-particle Dirac spectral data

Set ℏ=c=1, m>0. On h=L²(R³,C⁴), take
  h_D(p)=α·p+βm,
  α_i=diag(−σ_i,+σ_i),   β=[[0,I₂],[I₂,0]],
  E_p=sqrt(|p|²+m²),
  P_±(p)=(I₄±h_D(p)/E_p)/2.
The Clifford identities imply h_D²=E_p²I₄, P_±²=P_±, P_+P_-=0, P_++P_-=I₄, rank(P_±)=2. The original signed one-particle operator is **not** a positive physical Fock Hamiltonian.

Choose particle and antiparticle one-particle spaces K_+=P_+h and K_-^c=conjugate(P_-h). Their direct sum K=K_+⊕K_-^c carries the positive physical generator
  h_phys= h_D|K_+ ⊕ overline(−h_D|K_-),   h_phys>=m,
and the antisymmetric Fock space F_-(K). The normal-ordered vacuum-relative free Hamiltonian
  H_phys=dΓ(h_phys)
  =sum_{s=1}² ∫ d³p/(2π)³ E_p [b_s†(p)b_s(p)+d_s†(p)d_s(p)]
is positive self-adjoint with finite-energy vectors in its natural domain. In infinite volume, pointwise creation/annihilation symbols are operator-valued DISTRIBUTIONS; their smeared versions realize CAR. There is NO legitimate infinite literal subtraction of two negative-energy levels at every p: use the chosen positive-energy particle/antiparticle Fock representation.

For a specific regulated p=(0,0,3), m=4 (E=5), let h_D=3α_z+4β, and let U,V be explicit 4×2 orthonormal matrices satisfying h_DU=5U and h_DV=−5V. With four independent CAR modes b₁,b₂,d₁,d₂ from orthogonal quaternion/Jordan–Wigner factors, define
  Ψ_α=Σ_s(U_{αs}b_s+V_{αs}d_s†).
Then {Ψ_α,Ψ_β†}=δ_αβ I, {Ψ_α,Ψ_β}=0. The positive H_phys=5Σ_s(b_s†b_s+d_s†d_s) obeys
  [Ψ_α,H_phys]=Σ_β(h_D)_{αβ} Ψ_β;
its energies are {0,5,10,15,20} with multiplicities {1,4,6,4,1}. This **directly verifies** free Dirac Heisenberg evolution with positive many-body energy within four biquaternion CAR factors; no fundamental Grassmann coefficients are invoked.

## Causal anticommutator in the continuum

Write `barΨ=Ψ†γ⁰` and the scalar Pauli–Jordan distribution, with the sign convention specified explicitly:
  Δ(z)=∫d³p/[(2π)³2E_p] [e^(−ip·z)−e^(+ip·z)],   p⁰=E_p.
The free particle/antiparticle mode expansion and spin sums give
  {Ψ_α(x),barΨ_β(y)}=[(iγ^μ∂_{z^μ}+m)Δ(z)]_{αβ},  z=x−y.
This is a c-number distribution. The Klein–Gordon causal propagator Δ has support in the closed light cone (finite propagation speed of the normally hyperbolic KG operator); differentiation cannot enlarge its support. Thus this ANTICOMMUTATOR vanishes at spacelike separation as a distribution. This is a STANDARD free-Dirac QFT result, not a new UBT prediction.

At equal time Δ(0,r)=0 and ∂_tΔ(0,r)=−iδ³(r); multiplying the preceding spinor kernel by γ⁰ on the right yields
  {Ψ_α(t,x),Ψ_β†(t,y)}=δ_αβ δ³(x−y).
The antiparticle sector is essential for the completeness P_++P_-=I₄ and causal cancellation.

The algebraic identity can be read directly in momentum space:
  P_+(p)γ⁰=(E_pγ⁰−γ^i p_i+m)/(2E_p),
  P_−(p)γ⁰=(E_pγ⁰+γ^i p_i−m)/(2E_p),
the second coefficient being the antiparticle Fourier term after reversing the dummy momentum variable.

**Important regulator caveat:** any finite momentum-mode cutoff is generally nonlocal even at equal time. For example Σ_{k=−1}¹e^(ikr)=1+2cos(r) is nonzero at r=π. The exact distributional delta and relativistic spacelike support require the untruncated continuum (or a suitable infinite-mode local limit); a finite-cutoff CAR check alone cannot prove microcausality.

## Lorentz covariance is not a local CAR matrix automorphism

The Dirac pointwise spinor matrix S(Λ) is nonunitary for boosts; applying it directly as b→Sb to finite-site CAR annihilators would violate {Sb,(Sb)†}=SS†. In the full continuum free theory, proper Lorentz transformations act on the SPACE OF SOLUTIONS, with the conserved Dirac inner product integrated over a Cauchy hypersurface. The transformation of hypersurface, spin indices and momenta together gives an appropriate unitary implementation on the physical one-particle space (and its Fock lift). This resolves the naïve fixed-site boost objection for the **reference free Dirac theory**, not the unresolved UBT composite-tetrad intertwiner or local grading selection.

## State action and status

On differentiable, normalized Fock-state paths Φ(t) in the domain of H_phys, the ordinary complex-number quantum-state action
  S_Fock[Φ,λ]=∫dt [(i/2)(<Φ,dotΦ>−<dotΦ,Φ>)−<Φ,H_physΦ>+λ(<Φ,Φ>−1)]
gives i dotΦ=(H_phys−λI)Φ. It uses no fundamental Grassmann coefficient fields; it is NOT an off-shell covariant microscopic field action and cannot be substituted for S_UBT[Theta]. It presupposes a fixed background Minkowski time and the standard Fock-state Hilbert structure.

**Remaining UBT-specific gates:** justify infinite CAR mode copies and positive polarization FROM one dynamical Theta; show local operator-valued Theta with the conditional antilinear spinor map; construct a nondegenerate even composite tetrad and Lorentz-compatible spin connection from the same physical system; derive matter/geometry constraints and a unique single covariant action. Do not change `canonical/ACTION.en.md`.

**Verification:** six locally executed SymPy/pytest tests in `tests/test_information_free_dirac_car_field.py`: Clifford/projector algebra; explicit positive/negative spectral bases; four-mode CAR+Heisenberg+positive spectrum; Pauli–Jordan equal-time normalization; finite-cutoff nonlocality counterexample; spectral spin sums matching the causal kernel.

Background references: https://qft.org/foundations/free-fermion-fields/canonical-quantization-free-dirac-field/ and https://qft.org/courses/qft-i/35-dirac-field-quantization-and-propagators/ .
