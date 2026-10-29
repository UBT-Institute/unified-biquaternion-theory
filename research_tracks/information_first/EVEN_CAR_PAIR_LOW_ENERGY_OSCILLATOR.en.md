<!-- BILINGUAL-UNIT: even-car-pair-low-energy-oscillator -->
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

# Dynamic low-energy bosonic oscillator from an even-CAR pair Hamiltonian

**2026-10-27. Exact finite-matrix diagonalization plus controlled low-excitation pair limit.** Builds on `ENTANGLED_EVEN_CAR_GEOMETRY_CCR_GATE.en.md` and `COLLECTIVE_CAR_EMERGENT_GRAVITY_CCR.en.md`. No fundamental Grassmann coefficient algebra or independent microscopic bosonic oscillator is required to REPRESENT the finite model.

## 1. The pair Hamiltonian has a genuine excitation gap

For two one-occupied two-mode CAR cells, use their even Schwinger bilinears sigma_x, sigma_y, sigma_z. With h>0 and J>0 the Hermitian even interaction
  H_pair=−J sigma_x⊗sigma_x−h(sigma_z⊗I+I⊗sigma_z)
has eigenvalues
  −R, −J, +J, +R,    R=sqrt(4h²+J²)>J.
The unique ground state is
  |g>=sqrt(p)|up up>+sqrt(1−p)|down down>,
  p=(1+2h/R)/2.
An exactly orthogonal FIRST excited state is
  |e>=(|up down>+|down up>)/sqrt(2)
with energy −J; the **gap** is
  Omega=R−J>0.
The other excited states have gaps R+J and 2R, relative to |g>.

## 2. Exact low-energy two-level projection

On the invariant eigenspace L=span{|g>,|e>} of H_pair, let W:C²→C⁴ be the isometric embedding W=(|g>,|e>). Define original pair-wide quadratures
  Q_pair=(sigma_x⊗I+I⊗sigma_x)/2,
  P_pair=(sigma_y⊗I+I⊗sigma_y)/2.
The *projected* matrices are exactly
  W† H_pair W = diag(−R,−J),
  W† Q_pair W = q sigma_x,
  W† P_pair W = b sigma_y,
where
  q=sqrt((1+J/R)/2),    b=sqrt((1−J/R)/2),    2qb=r=2h/R.
For h=1,J=2sqrt(3), the reference r=1/2 and
  q=(sqrt(3)+1)/(2sqrt(2)),  b=(sqrt(3)−1)/(2sqrt(2)).

A critical distinction: compression DOES NOT preserve multiplication:
  [W†Q_pair W,W†P_pair W]≠W†[Q_pair,P_pair]W.
For the concrete reference h=1,J=2sqrt(3), the compressed commutator is
  i diag(r,−r),
whereas compressing the FULL commutator yields
  i diag(r,0).
The reason is the projected Q/P can connect to states outside the low-energy subspace. The effective algebra is constructed by projection FIRST, not by falsely pulling back the full commutator.

## 3. Many-pair effective oscillator with exact finite-size corrections

Take M independent pairs. The subspace L^(tensor M) is invariant under the summed microscopic H, and the reference ground is |g>^(tensor M). On that subspace, after subtracting the reference ground energy,
  H_low=Omega K,    K=sum_(k=1)^M (1−tau_z^(k))/2.
Projected collective observables are
  Q_low=(q/sqrt(M))sum_k tau_x^(k),
  P_low=(b/sqrt(M))sum_k tau_y^(k).

Their exact finite-M algebra is
  [Q_low,P_low]=i r (1−2K/M).
For r>0 define normalized Q_c=Q_low/sqrt(r), P_c=P_low/sqrt(r), obtaining
  [Q_c,P_c]=i(1−2K/M).
On K≤k_max the discrepancy from iI is bounded in operator norm by 2 k_max/M, tending to zero with fixed k_max. The collective lowering operator A=(Q_low/q+iP_low/b)/2 obeys
  [H_low,A]=−Omega A.
The low-energy Dicke oscillator excitations are multiples of Omega; their ladder matrix elements converge to the usual sqrt(k) factors at fixed k in the M→∞ limit.

This is a CONTROLLED reference emergent oscillator with a dynamically selected entangled microscopic ground state and gap, not merely an arbitrary chosen first-order bosonic action. Its frequency Omega=R−J and polarization r are both functions of the same even-CAR reference couplings.

## 4. Why this is not yet a gravity Hamiltonian

1. The pair Hamiltonian h,J and pairing graph are CHOSEN; UBT has not derived them from S_UBT[Theta].
2. Its low-energy collective fluctuations form an oscillator, not the indefinite ADM DeWitt kinetic structure or four invertible tetrad one-forms. The freedom to select a cosmological variable q=ln(a) remains unproved.
3. The preferred reference spin axis and foliation, and the nonunitary Lorentz boost of the timelike correlator, are not automatically compatible with the physical gauge quotient of the split-jet MM construction.
4. A finite-mode, energy-gapped reference does not establish continuum Lorentz covariance, UV renormalization or a physical graviton.
5. The effective low-energy projection is an additional reduction; the projected operators need not inherit every full-algebra identity.

**Next falsifiable gate:** compare this exact emergent oscillator's reduced symplectic form, Hamiltonian SIGN and spectrum with the homogeneous ADM constraint and the MM split-jet presymplectic kernel. In particular, obtaining a positive oscillator does not automatically reproduce the *negative* minisuperspace kinetic term `−kappa p_a²/(12a)`; an interaction/constraint derivation must show the required gravitational structure rather than fit it by hand. Keep `canonical/ACTION.en.md` status `DEFINED_FAMILY_NOT_FINALIZED`.

## Verification

`tests/test_information_even_car_pair_oscillator.py` contains five tests, locally passed via pytest, checking exact spectral projection, projected quadratures and signs, failure of multiplicative compression, the low-energy many-pair Hamiltonian, and finite-size low-occupation commutator bounds.

Verification scope: exact finite matrices in the stated reference model. LEAN-PENDING: no formal proof of the many-body limit, physical continuum or UBT dynamics is supplied.
