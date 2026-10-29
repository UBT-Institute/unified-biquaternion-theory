<!-- BILINGUAL-UNIT: entangled-even-car-geometry-ccr-gate -->
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

# Entangled even-CAR ground state: timelike correlation and collective bosonic CCR

**2026-10-27. Exact reference construction in two CAR modes per cell and N even cells.** This addresses the polarized-versus-timelike tension noted in merged PR #800 and in `COLLECTIVE_CAR_EMERGENT_GRAVITY_CCR.en.md`. The microscopic couplings, foliation, and identification of the correlator with geometry are **not selected by UBT**.

## 1. A rigorous single-cell parity obstruction, and its limits

In one cell with two fermionic CAR modes, use the occupation basis |00>,|10>,|01>,|11> and define its positive one-body Hermitian matrix C_ij=<c_j†c_i>. Any normalized *pure state of definite fermion parity* lies either in the even span{|00>,|11>} or in the odd span{|10>,|01>}.

- Even pure |phi_e>=alpha|00>+delta|11> gives C=|delta|² I₂, so det C may be strictly positive but the spin/Schwinger polarization Tr(sigma_i C) vanishes for all i.
- Odd pure |phi_o>=beta|10>+gamma|01> gives a rank-one projector C, hence det C=0 (while its spin polarization may be nonzero).

Thus a single **pure parity-definite two-mode cell** cannot simultaneously have det C>0 and nonzero spin polarization. This is not a no-go for mixed local states, several cells, global pure entanglement or a different carrier.

The fully aligned reference in the previous collective-CCR note is a product of local odd pure |up>=|10> states, so its *raw one-body correlator* is null (det C=0), incompatible with naively identifying it as the timelike MM carrier. The escape below is physical entanglement **between cells**, not an unmotivated identity offset C+alpha I.

## 2. Entangled pair with nondegenerate local correlation

Restrict every cell to exactly one fermion and identify |up>=|10>, |down>=|01>. For 0<p<1 take the two-cell pure state
  |chi_p> = sqrt(p)|up up>+sqrt(1-p)|down down>.
This state has exactly two CAR fermions and even global parity. The reduced density of EACH cell, in the one-fermion sector, is diag(p,1-p). Therefore
  C=diag(p,1-p)=(1/2)(I+r sigma_z),   r=2p-1,
  det C=p(1-p)=(1-r²)/4>0.
For p != 1/2 it simultaneously has nonzero spin polarization <S_z>=r. In particular p=3/4 gives r=1/2 and det C=3/16.

The identity
  r²+4 det C=1
is an exact Bloch/determinant relation in this **one-fermion-per-cell, trace C=1** reference model, not a universal new gravitational law.

## 3. A simple EVEN-CAR Hamiltonian actually chooses this reference ground state

For a pair of cells let S_x,S_z be the even Schwinger operators of each CAR cell, restricted to its one-fermion Hilbert space. Define the explicit reference bond Hamiltonian
  h_pair = -J S_x^(1)S_x^(2) - h(S_z^(1)+S_z^(2)),   J,h>0.
Everything is polynomial in **even fermionic CAR bilinears**; no fundamental Grassmann variables or microscopic bosonic oscillator were introduced. The ordered basis {|up up>,|up down>,|down up>,|down down>} yields eigenvalues
  { -R, -J, +J, +R },     R=sqrt(4h²+J²)>J.
Its UNIQUE ground state is precisely |chi_p> with
  r=2p-1=2h/R,    p=(1+r)/2,    det C=J²/(4R²).
The spectral gap is R-J>0. Choosing h=1, J=2sqrt(3) gives R=4, p=3/4, det C=3/16 and energies {−4,−2sqrt(3),+2sqrt(3),4}.

For N=2M cells take H_pair^(N)=sum over M disjoint pair Hamiltonians. Its unique product-pair ground state is |Omega_p^(N)> = |chi_p>^(tensor M), with a gap R-J independent of M. The couplings J,h and pair partition are **independent selections**, not derived from the locked UBT action; translation symmetry by one cell and Lorentz invariance are not automatic.

## 4. Exact emergent CCR and uncertainty in the ground state

Let collective even observables (from the companion gate) be
  Q_N=Σ_(r=1)^N S_x^(r) /sqrt(2N),
  P_N=Σ_(r=1)^N S_y^(r) /sqrt(2N),
  Z_N=Σ_(r=1)^N S_z^(r)/N,
so **at every finite N**:
  [Q_N,P_N]=i Z_N.
On |Omega_p^(N)>:
  <Z_N>=r,   Var(Z_N)=2(1-r²)/N.
For r>0 rescale `Qtilde_N=Q_N/sqrt(r)` and `Ptilde_N=P_N/sqrt(r)`. Then
  <[Qtilde_N,Ptilde_N]>=i,
  < ( [Qtilde_N,Ptilde_N]/i-I )† ( [Qtilde_N,Ptilde_N]/i-I ) >
   = 2(1-r²)/(N r²).
This is **state-dependent mean-square convergence**, not operator-norm convergence on the full finite-N Hilbert space, and does not contradict Tr[A,B]=0.

The cross-cell two-spin entanglement yields
  Var(Q_N)=1/2+sqrt(p(1-p)),
  Var(P_N)=1/2-sqrt(p(1-p)),
  Cov_sym(Q_N,P_N)=0,
  Var(Q_N) Var(P_N)=r²/4.
Thus the rescaled collective fluctuations are exact Robertson-saturating **squeezed minimum-uncertainty** variables in this product-pair reference state, even though their finite-N commutator remains noncentral. A standard quantum central limit under independent identical pair blocks is a plausible route to a genuine bosonic fluctuation representation; the present tests establish precise finite-N moments and mean-square commutator bounds, not a full Weyl-CCR limit theorem.

## 5. Lorentz and gravitational identity remain open

The positive C matrix maps to a timelike Hermitian Lorentz 4-vector **algebraically** via Pauli coordinates, but a Lorentz boost S in SL₂(C) can transform C to sqrt(det C) I₂; such a nonunitary S is NOT the naive unitary automorphism of fixed CAR annihilators. Accordingly the polarization axis r sigma_z is **frame/polarization dependent**: it is not selected Lorentz-covariantly from a timelike vector alone. One must retain the physical observer/foliation, additional bivector/spin data, or derive a gauge-covariant orientation field.

This reference sector has (a) a positive local C, (b) nonzero normalized bosonic CCR expectation and controlled fluctuations, and (c) a gapped purely even-CAR microscopic reference Hamiltonian. It still does NOT generate four invertible tetrad one-forms, the MM split-jet stabilizer quotient, the ADM constraints, a dynamical universal Newton coupling, or a single-Theta action. The variational parameters h,J and the choice of pair interactions remain new input and cannot be silently presented as derived UBT physics.

## Verification

`tests/test_information_entangled_car_geometry_ccr.py` contains eight independently locally executed SymPy tests: pure-cell parity gate, timelike two-cell correlations, exact CCR and mean-square error for N=2,4, squeezed minimum uncertainty, boost/axis obstruction, SU(2) commutant, gapped even-CAR ground state, and independent pair Hamiltonian spectrum. All eight passed locally.

Verification environment: SymPy 1.14.0. LEAN-PENDING: this reference construction is not formalized in Lean and Lean/Lake is unavailable locally. Finite-cutoff checks do not prove the full Weyl-CCR limit or the gravitational action.
