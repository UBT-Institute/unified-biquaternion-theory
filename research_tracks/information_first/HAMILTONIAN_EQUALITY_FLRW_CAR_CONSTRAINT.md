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

# Matching gravitational and fermionic Hamiltonians: constraint, not operator identity

**2026-10-27 — EXACT toy minisuperspace equality conditional on standard Einstein/ADM gravity and a selected finite-CAR Fock matter sector. NOT a derivation of the final single-Theta UBT Hamiltonian or a proof of GR/QM unification.**

## The equality to test

For a closed spatial slice with no boundary charge, general covariance imposes the scalar Hamiltonian constraint (plus the momentum/Gauss constraints)
  C_total(x) = C_GR(x)+C_ferm(x)+C_mix(x) ≈ 0.
Therefore, *on the constraint surface only*,
  C_GR ≈ -(C_ferm+C_mix).
This is the precise meaning in which one contribution must match the other. Requiring H_GR=H_QM as independent positive operators is not a consequence of GR; gravity's kinetic term has an indefinite DeWitt supermetric and lapse/shift act as constraint multipliers. The full Hamiltonian also includes shift/Gauss constraints and boundary generators, so even the integrated equality is subject to boundary and gauge conditions.

For a genuine one-Theta UBT result one would need a common phase space or operator algebra and a map
  C_UBT[Theta] = C_MM[E(Theta),pi_E(Theta)] + C_CAR[Theta] + C_mix[Theta] ≈ 0,
rather than merely the direct sum of separately postulated Einstein and Dirac theories. This equality **alone** selects neither the UBT action nor matter couplings.

## Exactly solvable classical FLRW plus finite-CAR benchmark

Take a fiducial comoving cell of volume one, spatially flat FRW metric
  ds²=-L(t)² dt²+a(t)²(dx²+dy²+dz²),
where L(t)>0 is the lapse, a(t)>0 the scale factor, and κ=8πG in c=ℏ=1 units. Suppress all boundaries and assume a homogeneous, isotropic reference state. The Einstein–Hilbert gravitational minisuperspace Lagrangian is, after standard boundary treatment,
  L_g = -3 a dot(a)²/(κ L) - L Λ a³/κ.
The momentum is
  p_a = -6 a dot(a)/(κ L).
Legendre transformation gives
  H_g=L C_g,
  C_g= -κ p_a²/(12a)+Λ a³/κ.

Use a four-mode (two spin polarizations for each of particles and antiparticles) **zero-comoving-momentum** CAR Hamiltonian from our biquaternion/Jordan–Wigner factors,
  H_f=m N_f,     N_f=Σ_{j=1}^4 c_j†c_j, m>0,
with occupancies n=0,1,2,3,4, multiplicities (1,4,6,4,1). The positive spectrum is m n. The zero-momentum condition is chosen deliberately: for moving modes instantaneous curved-background frequencies are a-dependent and canonical basis changes/spin connections require additional terms. We are not treating an arbitrary excited Dirac field as a homogeneous perfect fluid.

In an N_f=n stationary matter sector, the lapse constraint becomes
  C = -κ p_a²/(12a)+Λ a³/κ+m n =0.      (Eq. 1)
With physical Hubble rate H=dot(a)/(L a) and p_a=-6 a² H/κ this is equivalent to
  H² = Λ/3+ κρ_f/3,    ρ_f=m n/a³.         (Eq. 2)
Hence the equality C_g=-m n recovers the standard flat-space FLRW first Friedmann equation with dustlike a^(-3) density. At Λ=0 and n>0 the expanding classical branch gives a(t)∝t^(2/3) in L=1 gauge. Note: the effective homogeneous/dust truncation and state interpretation remain assumptions; no complete stress-tensor evolution or field-locality proof follows from this toy equality.

The bare Hamiltonian H_total=L C vanishes ON SHELL in this constrained, boundaryless toy sector; matter excitation energies are not zero. A relational/clock Hamiltonian can be nonzero after gauge fixing or deparametrization. Equating positive matter energy directly to positive ADM energy is a sign error.

## A quantum equation for the gravity–fermion toy model

For a **formal, illustrative** Dirac quantization promote p_a→-i ∂_a, choose the simple non-unique ordering (1/a) p_a², and use the CAR occupation eigenbasis. The constraint equation on Ψ(a)=Σ_{n,degeneracy} ψ_{n,r}(a)|n,r⟩ becomes
  [ κ/(12a) d²/da² + Λ a³/κ + m n ] ψ_{n,r}(a) =0.
This is an operator-constraint equation; not a statement H_g=H_f as operators on their separate unconstrained spaces. Factor ordering, inner product, boundary conditions at a=0 and the meaning of relational time are unresolved.

For Λ=0 and n>0:
  ψ''(a) + (12 m n/κ) a ψ(a)=0.
Writing q=(12 m n/κ)^(1/3), a linearly independent pair of solutions is
  Ai(-q a), Bi(-q a).
For n=0, ψ''=0, giving ψ=A+B a. The oscillatory Airy solutions need not be normalizable in a naive Lebesgue measure; no physical Hilbert-space completion is claimed here.

## Why this is useful, and the remaining decisive UBT condition

This gives an explicit common CONSTRAINT that our previously constructed positive finite-CAR fermion Hamiltonian can satisfy alongside ADM gravity. It shows the correct SIGN, normalizations, and an exactly solvable quantum minisuperspace benchmark. These equations are known reductions of Einstein gravity with matter; recovering them is a required consistency test, not an original new prediction.

The missing step is a dynamical identification of the gravitational variable a, its canonical momentum p_a, and the CAR mode algebra as observables **of the same underlying Theta system**, with a shared symplectic/Poisson/quantum structure. The unconstrained a and c_j used above have been assembled as independent toy variables, and therefore do NOT prove this. A successful candidate must additionally satisfy the full (nonhomogeneous) scalar-vector constraint algebra including the true biquaternion composite tetrad/spin connection; only then consider a unique unified action.

Regression: `tests/test_information_hamiltonian_equality_flrw_car.py`; symbolic identities checked locally before recording.

External checks: Living Reviews in Relativity, *Hamiltonian formulation of general relativity and post-Newtonian dynamics of compact binaries* (2024), https://link.springer.com/article/10.1007/s41114-024-00048-7 ; Friedmann-equation canonical example https://www.degruyterbrill.com/de/document/doi/10.1515/zna-2021-0384/html .
