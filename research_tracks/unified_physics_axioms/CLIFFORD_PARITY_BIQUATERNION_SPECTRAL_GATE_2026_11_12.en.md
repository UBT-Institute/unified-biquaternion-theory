# Clifford parity, biquaternion adjugate and exact doubled spectral branches (2026-11-12)

**Status: exact finite-dimensional algebra; physical UBT spectrum and boson/fermion assignment OPEN.**

## Existing basis and precise parity

The canonical UBT Clifford lift uses four gamma matrices and an involutive grading Gamma_* (see `research_tracks/action_selection/clifford_palatini_trace_selector.en.md`). The grading on **Clifford algebra elements** is the conjugation automorphism alpha(X)=Gamma_* X Gamma_*; do not identify alpha with left multiplication Gamma_* on spinors. Over C, Cl(1,3) is Mat_4(C), its even algebra is Mat_2(C) direct-sum Mat_2(C), and the odd vector space comprises off-diagonal 2x2 blocks. The even/odd dimensions are 8+8 over C. Clifford parity is distinct from physical fermion number and from bosonic/fermionic field statistics.

## General odd operator theorem

Let V=V_+ direct-sum V_- with equal dimension n, grading J=diag(I_n,-I_n), and D=[[0,A],[B,0]]. Then JD=-DJ and
```
D^2 = diag(A B, B A)
det(lambda I_(2n)-D)=det(lambda^2 I_n - B A).
```
The spectrum is paired lambda <-> -lambda with algebraic multiplicity, including at non-diagonalizable exceptional points. For lambda != 0, if AB u=lambda^2 u, then (u,lambda^(-1)B u) is a D eigenvector of eigenvalue lambda. Zero eigenvalues may have Jordan chains. An even operator instead preserves each grade and has no general +/- pairing.

## Exact biquaternion-adjugate construction

Represent Q=z0 I_2+z1 sigma1+z2 sigma2+z3 sigma3, zi complex. Define Qsharp=adj(Q)=z0 I_2-z1 sigma1-z2 sigma2-z3 sigma3, Delta=det Q=z0^2-z1^2-z2^2-z3^2. (Sharp is the algebraic adjugate, **not** Hermitian conjugation.) Define
```
D_Q=[[0,Q],[Qsharp,0]], J=diag(I_2,-I_2).
```
Then D_Q^2=Delta I_4 and
```
det(lambda I_4-D_Q)=(lambda^2-Delta)^2.
```
For Delta!=0, the eigenvalues +sqrt(Delta), -sqrt(Delta) each have **geometric and algebraic multiplicity 2**, with explicit eigenvectors
```
Psi_lambda(u)=(u, Qsharp u/lambda), u in C^2.
```
For Delta=0, D_Q^2=0, so D_Q is nilpotent and may be non-diagonalizable: do not count two independent eigenspaces of each sign at the exceptional locus. This doubled spectrum is an exact algebraic degeneracy from the 2x2 adjugate identity, not a new particle mass or measured speed.

With Q=p0 I+sum p_i sigma_i for real momentum, Delta=p0^2-|p|^2; the determinant-zero set is the familiar null momentum cone in c=1 units. This is the known Weyl/Dirac algebraic factorization, **not** an independent derivation of Lorentz invariance, quantum statistics or physical signal speed from the UBT action.

## Boson/fermion and ghost boundaries

The matrix D_Q can act on a Dirac spinor and flip chirality; that does not turn its odd Clifford matrix entries into fermionic fields. A bosonic Clifford-valued connection can also have odd algebra grade. A fermionic action requires Grassmann-odd fields and appropriate quantization, not merely eigenvalue -1 of alpha. In particular, eigenvalue -sqrt(Delta) is **not** a negative-energy kinetic ghost.

To claim a physical UBT spectral selection, derive the operator from a single microscopic action and show it is on shell on a rank-four background, determine its domain and inner product, calculate the complete constrained kinetic Hamiltonian and verify whether the 2-fold degeneracy survives coupling, mass terms and Lorentz-breaking backgrounds. The unselected physical action and boson/fermion identification remain OPEN.
