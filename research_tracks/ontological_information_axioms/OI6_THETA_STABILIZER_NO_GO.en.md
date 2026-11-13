<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# OI-6 — Residual stabilizer and the Theta-only gauge connection obstruction

**Status:** conditional known gauge geometry [STD]; dynamical UBT closure [OPEN]. All claims use the full complex matrix carrier on an explicitly restricted open sector, not the real-only approximation.

## A. Assumptions

Let the full complex biquaternion field transform as a single complex matrix by local SL2(C) Hermitian congruence. Work on the open subset where its Hermitian part H is positive definite, with K Hermitian. No commutation between H and K is assumed.

$$
\Theta=H+iK,\quad H=H^\dagger>0,\quad K=K^\dagger,\quad
\Theta'=g\Theta g^\dagger,\quad g(x)\in SL(2,\mathbb C).
$$

## B. OI-6-T20 — The generic stabilizer is U1

The following traceless matrix generates a nontrivial infinitesimal stabilizer whenever K is not proportional to H. The trace of KH-inverse is real; direct multiplication gives QH+HQ-dagger=0 and QK+KQ-dagger=0.

$$
Q=i\left(KH^{-1}-\frac12\operatorname{Tr}(KH^{-1})I_2\right),\qquad
\operatorname{Tr}Q=0,\qquad
Q\Theta+\Theta Q^\dagger=0.
$$

Conjugating by a positive square-root of H reduces the stabilizer to the subgroup of SU2 commuting with a Hermitian matrix. Its generic nondegenerate spectrum leaves U1; a scalar matrix enhances the stabilizer to SU2. Thus the orbit map has the displayed generic and exceptional ranks.

$$
\dim_{\mathbb R}SL(2,\mathbb C)=6,\quad
\dim_{\mathbb R}\mathrm{Stab}_{\rm generic}=1,\quad
\mathrm{rank}_{\rm generic}=5,\quad
\dim_{\mathbb R}\mathrm{Stab}_{\rm enhanced}=3,\quad
\mathrm{rank}_{\rm enhanced}=3.
$$

**OI-6-T20 [STD].** The residual U1 is abstractly isomorphic to SO2. It is **not yet proven** to be the same gauge direction as the residual SO2 mode in UBT Hamiltonian research.

## C. OI-6-T21 — No fully covariant full connection as a functional of Theta alone

Suppose an SL2(C) connection is a deterministic functional A[Theta] of the entire Theta configuration, possibly including arbitrary derivatives, with no additional covariant fields or gauge choice. It must obey the standard local inhomogeneous gauge law.

$$
A_\mu[\Theta']=hA_\mu[\Theta]h^{-1}-(\partial_\mu h)h^{-1}.
$$

Pick a smooth nonzero stabilizer generator Q(x), and choose h(x)=exp(f(x)Q(x)) with f(x0)=0 but derivative f(x0) nonzero. The transformation fixes Theta **pointwise everywhere** and therefore all its ordinary jets. At x0, h is identity while its derivative is nonzero. Gauge covariance contradicts the fact that the functional input is unchanged.

$$
\Theta'=h\Theta h^\dagger=\Theta,\quad h(x_0)=I_2,\quad
A_\mu[\Theta](x_0)=A_\mu[\Theta](x_0)
-(\partial_\mu f)(x_0)Q(x_0).
$$

**OI-6-T21 [STD; conditional no-go].** On this open sector, a full local SL2(C) connection cannot be reconstructed in an equivariant way solely from Theta. This remains true even if the functional uses arbitrarily high derivatives, because the stabilizer fixes the complete field. It is an ordinary nonfree-gauge-orbit obstruction, **not** a global no-go for UBT composite connections built from a specified tetrad, torsion or extra covariant data.

## D. OI-6-T22 — Two misleading flat shortcuts

For an invertible complex Theta, the local logarithmic determinant differential is SL2(C)-invariant but exact, hence has no ordinary Abelian curvature away from zeros or singular patches.

$$
q=\frac12\,d\log\det\Theta,\qquad dq=0\quad(\det\Theta\ne0).
$$

For a different group-valued field S transforming by left multiplication, the pure-gauge potential is likewise flat and annihilates that group field. It is **not** automatically a permissible Theta connection under congruence, where a second derivative term from the right factor appears.

$$
A=-(dS)S^{-1},\qquad F=dA+A\wedge A=0,\qquad(d+A)S=0.
$$

**OI-6-T22 [STD].** Neither shortcut alone produces generic curved gravitational dynamics. This does **not** exclude nonlinear composites involving an independently specified frame, Cartan torsion or the complete Theta-dependent action.

## E. An additional covariant object can remove the stabilizer

Two independent matrices with different preferred Pauli axes can have only a discrete common stabilizer. The combined infinitesimal map then has full rank. This is a countermodel to interpreting the obstruction as requiring a necessarily propagating new field.

$$
\Theta_1=I_2+i\sigma_z,\quad\Theta_2=I_2+i\sigma_x,\quad
\operatorname{rank}D(\Theta_1)=5,\quad
\operatorname{rank}D(\Theta_1,\Theta_2)=6.
$$

A covariant tetrad could supply further data, but the fundamental relation E_mu=D_mu Theta makes reconstructing that same D from E an implicit, potentially circular problem. Rank counting does not solve it.

## F. Consistency with the existing canonical UBT proofs

The canonical gap_10i_paired_connection_audit.tex reduces the Lorentz-compatible pair to a single spin connection. The torsionful local representer gap_10i_torsionful_local_representer.tex **already constructs** a right inverse for specified tetrad and composite contortion K[e,Theta]; gap_10omega_connection_elimination.tex reconstructs Omega(e,T). The full composite Theta variation and dynamical choice of torsion are explicitly OPEN in gap_10tdyn_10d_canonical_action_audit.tex. Our no-go addresses a different, stronger demand: a full equivariant connection from Theta **alone** with no independent covariant frame data.

**G-OI6-16 [OPEN]:** test whether this U1 is the residual SO2 of the canonical Hessian/constraint analysis. **G-OI6-17 [OPEN]:** formulate the self-consistent variation with composite e, K and Omega rather than an independent Palatini variation. **G-OI6-18 [OPEN]:** compute the physical kinetic Hessian and constraints of the residual connection and establish auxiliary, pure-gauge, or propagating status.

## G. Tests and references

The standard-library verifier verify_theta_stabilizer_obstruction.py has 11 locally passing tests (2026-11-13) for real orbit ranks, a generic noncommuting complex Theta stabilizer, the local gauge-law contradiction, flat determinant and Maurer–Cartan shortcuts, and the two-matrix rank example. The full uploaded source was not separately executed byte-for-byte; its finite calculations are mirrored by the local tests. Proofs are provided above, not replaced by those tests.

- Residual U1 in adjoint SU2 gauge systems: https://doi.org/10.1103/PhysRevD.25.3319 .
- Pure-gauge and Maurer–Cartan flat connections: https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM2014.2/ICM2014.2.pdf .
- Internal UBT canonical comparison: canonical/gr_closure/gap_10i_paired_connection_audit.tex; canonical/gr_closure/gap_10i_torsionful_local_representer.tex.