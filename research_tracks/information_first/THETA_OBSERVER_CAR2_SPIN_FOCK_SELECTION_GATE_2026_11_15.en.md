<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional finite-mode algebra/topology, not physical electron, photon, full QED, GR, or unified Theta action.
UBT-AI-PROVENANCE-END
-->

# Observer spin lines, intrinsic CAR, two-mode spin Fock lift, and action nonuniqueness

**2026-11-15; exact scoped algebra, NOT a derived UBT quantum action.**

Source gates:
- canonical/ACTION.en.md: the single microscopic action is DEFINED_FAMILY_NOT_FINALIZED.
- canonical/geometry/biquaternion_tetrad.tex: the locked physical E_mu=N0^(-1/2) D_mu Theta belongs to W_L=i Herm2.
- research_tracks/information_first/THETA_SPIN_LIFT_PROJECTIVE_OBSERVER_Z2_GATE_2026_11_15.en.md: no nonzero single-valued equivariant Weyl spinor can be made from only Lorentz-tensorial canonical Theta data, because central Spin -I acts trivially on the data but nontrivially on a spinor.
- research_tracks/information_first/BIQUATERNION_INTRINSIC_CAR_SPIN_STATISTICS_GATE.md: single-mode CAR1=M2(C), many-mode Jordan-Wigner, but no physical spin-statistics theory.
- research_tracks/information_first/GEOMETRIC_HAMILTONIAN_NONUNIQUENESS.md: quantum geometry does not select a unique Hamiltonian.

## Gate A: one clock yields local CAR polarization, but NOT spin-half operator

For a positive observer clock N, define
\[
T_N=N^{-1/2}\Theta N^{-1/2},\quad \rho_N=T_NT_N^\dagger/\mathrm{tr}(T_NT_N^\dagger).
\]
At a nondegenerate spectral point,
\[
\rho=\tfrac12(I+r\,\mathbf n\cdot\sigma),\quad0<r<1,\quad
P_\pm=\tfrac12(I\pm\mathbf n\cdot\sigma).
\]
A normalized eigenbasis |+>,|-> defines the exact CAR1 operator
\[
a_\rho=|-\rangle\langle+|,\quad a_\rho^2=0,\quad
\{a_\rho,a_\rho^\dagger\}=I,\quad a_\rho^\dagger a_\rho=P_+.
\]
It depends on the RELATIVE phase of the eigenvectors, absent from the local rho. Under the induced observer SU2 rotation U, a_rho transforms by adjoint conjugation U a_rho U†; central U=-I therefore fixes a_rho. It is an even *adjoint* object, not a fundamental Weyl spinor. At r=0 the eigenvalues coincide, and no preferred P_plus or annihilator can be selected by this spectral rule.

### Topological discriminator

For a Bloch-sphere eigenbasis
\[
|+\rangle=(\cos(\theta/2),e^{i\varphi}\sin(\theta/2))^T,
\quad |-\rangle=(-e^{-i\varphi}\sin(\theta/2),\cos(\theta/2))^T,
\]
the Berry curvatures are
\[
f_+=+\tfrac12\sin\theta\,d\theta\wedge d\varphi,\quad
f_-=-\tfrac12\sin\theta\,d\theta\wedge d\varphi.
\]
Hence c1(L_plus)=+1, c1(L_minus)=-1. The CAR annihilator is a local section of
\[
\mathrm{Hom}(L_+,L_-)=L_-\otimes L_+^*,\qquad
\boxed{c_1(\mathrm{Hom}(L_+,L_-))=-2}.
\]
Equivalently its relative Berry curvature is f_- - f_+ = -sin(theta) dtheta wedge dphi. The operator line and the spinor eigenline have DISTINCT Chern numbers, so cannot be identified globally. This is projective-observer kinematics, not physical electromagnetic charge, and the pointwise rho comparator is not claimed to satisfy the canonical gravity equations.

## Gate B: two ordered biquaternion CAR modes carry true spin-1/2 and parity

A SINGLE CAR1 mode has a one-dimensional odd sector; with a rotation-invariant vacuum and parity-preserving SU2 it cannot provide the two-dimensional spin-1/2 doublet. Use the ordered two-mode extension B tensor B = M4(C) and the standard Jordan-Wigner operators:
\[
a=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
c_1=a\otimes I,\quad c_2=\sigma_3\otimes a.
\]
They satisfy \(\{c_a,c_b\}=0\) and \(\{c_a,c_b^\dagger\}=\delta_{ab}I_4\).

Define
\[
n_a=c_a^\dagger c_a,\quad N_f=n_1+n_2,\quad
J_k=\tfrac12\sum_{a,b}c_a^\dagger(\sigma_k)_{ab}c_b.
\]
Exact checks give
\[
[J_i,J_j]=i\epsilon_{ijk}J_k,\quad [N_f,J_k]=0,
\quad J_3=\operatorname{diag}(0,-1/2,1/2,0).
\]
On the ordered basis |00>,|01>,|10>,|11>, zero- and two-particle sectors are rotational singlets, and the one-particle states carry a genuine spin-1/2 doublet. Most importantly,
\[
\boxed{e^{2\pi iJ_3}=(-1)^{N_f}=\operatorname{diag}(1,-1,-1,1)}.
\]
Thus the Spin central element becomes fermion parity, and conjugation by this operator sends each c_a to -c_a. An independent global number U1 acts as
\[
U_q(\alpha)=e^{i\alpha N_f},\quad
U_q c_a U_q^\dagger=e^{-i\alpha}c_a,\quad [U_q,J_k]=0.
\]
Spin and charge are separable in this exact quantum model. This does NOT establish electric charge, local U1 gauge redundancy, an electron, or two photon helicities. It is a finite-mode SU2 rotational representation, NOT the full positive-energy Lorentzian CAR field.

**Single-Theta caution:** B tensor B is NOT one local B; the TWO mode selection and many-mode quantum Hilbert space must be derived from one canonical Theta dynamics rather than treated as additional fundamental fields by fiat.

## Gate C: symmetries alone cannot select the Hamiltonian

For omega>0 and lambda>0 two distinct positive, spin- and charge-invariant Hamiltonians are
\[
H_0=\omega N_f,\qquad H_\lambda=\omega N_f+\lambda n_1n_2.
\]
Both commute with all J_k and N_f, share the same CAR and fermion parity, but their spectra differ:
\[
\mathrm{spec}(H_0)=\{0,\omega,\omega,2\omega\},
\quad \mathrm{spec}(H_\lambda)=\{0,\omega,\omega,2\omega+\lambda\}.
\]
Therefore CAR + spin + internal number phase + observer projective geometry DO NOT mathematically determine a unique physical time evolution. The fundamental Theta action must supply an extra energy/locality/causal selection.

## Next complete physics gates

1. Derive the two-mode and continuum CAR operator net from the ONE canonical Theta with a selected Spin structure, a physical vacuum and observer-covariant mode polarization.
2. Derive local relativistic causal evolution, the physical fermion current and charge as its Noether generator, with a bounded Hamiltonian and correct spin-statistics assumptions.
3. Prove compatibility with the locked E=DTheta tetrad and its full variational composite connection; show GR dynamics (rather than assume the metric/Einstein action).
4. Obtain an actual first-class *internal* U1 Gauss generator, dynamical spin-1 pole and its two healthy polarizations from the same action; then derive QED and classical Maxwell.
5. Recover an anomaly-free chiral Standard Model field spectrum and couplings. The full single action is still missing.

**Verification:** 9 exact local SymPy/pytest regression tests passed for these finite-mode statements. File: tests/test_theta_observer_car2_spin_fock_gate.py. No physical UBT action, photon, GR, or SM claimed.
