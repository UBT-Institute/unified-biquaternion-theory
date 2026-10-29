<!-- BILINGUAL-UNIT: car-correlation-axis-adm-sign -->
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

# Correlation-selected polarization and the gravitation-sign compatibility gate

**2026-10-27. Eight exact finite-matrix tests; conditional physical identification.** Continues the `COLLECTIVE_CAR_EMERGENT_GRAVITY_CCR.en.md`, `ENTANGLED_EVEN_CAR_GEOMETRY_CCR_GATE.en.md`, `EVEN_CAR_PAIR_LOW_ENERGY_OSCILLATOR.en.md` results from PR #801. All CAR degrees of freedom are realized by orthogonal biquaternion factors; no additional fundamental Grassmann variables are invoked.

## 1. A pair's connected quantum correlations can provide a geometric axis

For two one-fermion-per-cell Schwinger-CAR spins define the symmetric two-spin pure state
  |chi_p> = sqrt(p)|up up> + sqrt(1-p)|down down>, 0<p<1.
The local one-body CAR correlation is C=diag(p,1-p), giving
  det C=p(1-p)>0,   r=<sigma_z^A>=<sigma_z^B>=2p-1.
This is an internally timelike Hermitian-vector *candidate*, not the spacetime tetrad.

Compute the real 3x3 two-body correlation tensor
  T_ij=<chi_p|sigma_i^A sigma_j^B|chi_p>.
Exact Pauli algebra gives
  T=diag(s,-s,1),   s=2 sqrt(p(1-p)),
  T T^T =diag(1-r²,1-r²,1).
For r!=0 the largest eigenvalue 1 is SIMPLE, and its eigenspace selects the internal z axis **up to its sign**. The local magnetization vector m=(0,0,r) fixes the sign when r!=0. Under a common SU(2) rotation U on both cells, the induced SO(3) matrix R(U) sends T→R T R^T, so the principal eigendirection transforms covariantly. This establishes a way to *read an axis from the full entangled quantum correlations* rather than from an arbitrary coordinate convention ONCE THE STATE IS GIVEN.

At p=3/4, r=1/2 and the correlator has det C=3/16 with T T^T eigenvalues {3/4,3/4,1}. At p=1/2, C=I/2 remains maximally timelike at fixed trace, but r=0 and T T^T=I: **the principal axis of T T^T is undetermined and the normalized collective CCR construction fails** (the full signed tensor T may still distinguish an axis at this point; the claim is only about this principal-singular-axis rule). The exact tradeoff is
  r²+4 det C=1
for the trace-one local C. This identity is algebraic Bloch geometry, NOT a novel UBT matter/gravity field equation.

## 2. Exact symmetry-selection limitation

Assume a finite-cell microscopic reference Hamiltonian H is invariant under the common full SU(2) action on the CAR spin doublets, and it has a **nondegenerate** ground state |Omega>. Then U^(⊗N)|Omega> equals a phase times |Omega>. Every vector expectation <Omega|Sigma_i|Omega> must therefore be invariant under *all* SO(3) rotations, and hence vanishes.

In particular <[Q_N,P_N]> along any fixed internal axis is zero in such a ground state, so the nonzero normalized bosonic CCR obtained by polarized collective fluctuations cannot appear under these assumptions. A direct two-cell illustration is
  H_iso=J(sigma_x⊗sigma_x+sigma_y⊗sigma_y+sigma_z⊗sigma_z), J>0,
with a UNIQUE spin-singlet ground state of energy -3J, triplet energy +J, local C=I/2, and T=-I (no selected axis).

The previously studied exactly gapped interaction
  H_pair=-J sigma_x⊗sigma_x-h(sigma_z⊗I+I⊗sigma_z)
HAS a unique polarized entangled ground state when h,J>0, precisely because its Zeeman-like h term explicitly chooses a direction and breaks SU(2). That selection is not a derivation from a rotation-invariant bare biquaternionic action.

**Important degenerate-ground exception:** the SU(2)-invariant ferromagnetic two-cell Hamiltonian H_FM=-J(sigma_x⊗sigma_x+sigma_y⊗sigma_y+sigma_z⊗sigma_z), J>0, has a THREE-FOLD-degenerate triplet ground energy -J and singlet energy +3J. Every |chi_p> used above lies exactly in that ground eigenspace. Hence a rotationally invariant Hamiltonian CAN admit an entangled, polarized, timelike reference state without an explicitly symmetry-breaking Zeeman term — but it does NOT uniquely select p or an axis; that requires state/boundary selection or a controlled thermodynamic phase. The nondegenerate-ground no-go is essential and must not be strengthened. **Dynamical price of this exception:** the pair total-spin quadratures Q_pair=(sigma_x⊗I+I⊗sigma_x)/2 and P_pair=(sigma_y⊗I+I⊗sigma_y)/2 commute EXACTLY with H_FM. Consequently their collective fluctuations carry no oscillator frequency from this isotropic pair Hamiltonian, despite the gap 4J from triplet to singlet. The anisotropic reference H_pair yields the nonzero low-energy oscillator frequency Omega=R-J precisely by lifting the triplet degeneracy. Thus SU(2)-invariant ground-state availability is not yet a derived *dynamical* bosonic Hamiltonian. See regression tests.

**Conditional routes:** a gauge-covariant orientation supplied by an independently derived geometric/bivector datum; a spontaneously symmetry-broken phase at infinite N (where a unique finite-volume SU(2)-invariant ground premise no longer applies); or a theory with a physically justified SU(2)-breaking coupling. None has yet been derived within locked UBT. In particular a timelike Lorentz vector alone has an SU(2) little group and cannot choose an additional spatial axis without further data; a standard Lorentz boost is NOT a naive unitary CAR transformation on a fixed finite set of annihilation operators.

## 3. Why the positive collective oscillator is not yet the ADM gravity constraint

The pair low-energy Hamiltonian `H_low=Omega K>=0` is a positive excitation operator. The homogeneous ADM logarithmic scale-factor gravitational kinetic expression, with kappa>0, is
  C_GR,kin=-kappa/12 p_q exp(-3q) p_q.
For a self-adjoint canonical momentum, exp(-3q)>0 and therefore
  <psi|C_GR,kin|psi>=-kappa/12 || exp(-3q/2) p_q psi||² <= 0
whenever defined, with negative values on nontrivial momentum states.

As a finite-matrix illustration put Q=sigma_x/sqrt(2), P=sigma_y/sqrt(2), K=(I-sigma_z)/2 and use a finite positive matrix exp(-3Q). Then H_osc=Omega K is positive with zero-energy reference |up>, whereas
  <up|(-kappa/12 P exp(-3Q) P)|up>
       =-kappa cosh(3/sqrt(2))/24 < 0.
Consequently the **same positive Hamiltonian H_low cannot simply be unitarily relabelled as the negative ADM kinetic constraint** on the full kinematical Hilbert space. It does NOT rule out an emergent *gravitational constraint* built from composite q,p: the constraint is not required to be a positive physical Hamiltonian, and lapse/diffeomorphism gauge freedom or additional interactions may be essential. It does rule out claiming that bosonic CCR plus positive oscillator by themselves finish the UBT Hamiltonian.

## 4. Decisive future checks

- Derive the pair coupling/orientation from existing Lorentz-covariant Theta bilinears and connection; do not add an arbitrary axis or Zeeman coupling by hand.
- Check whether a gauge-invariant correlation/bivector order parameter survives the full split-jet and Lorentz quotient and permits nondegenerate vacuum tetrad legs.
- Derive the sign and form of the **constraint**, including lapse and mixed terms, from a common Theta symplectic structure; do not equate the microscopic positive H with C_GR.
- Recheck locality, state selection and controlled N→infinity limits. Continue retaining the unfinalized action status in `canonical/ACTION.en.md`.

## Verification

`tests/test_information_entangled_polarization_covariance.py`: eight SymPy tests passed locally, including the entangled T tensor, rotation covariance, SU(2)-invariant singlet counterexample, no invariant polarized vector, Bloch determinant/CCR tradeoff, and negative-ADM/positive-oscillator mismatch.

Verification scope: exact finite matrices in the stated reference model. LEAN-PENDING: no formal proof of the many-body limit, physical continuum or UBT dynamics is supplied.
