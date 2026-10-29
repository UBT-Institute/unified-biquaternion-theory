<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: g1-complex-gradient-flat-connection -->
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

# G1: full complex-gradient flatness and the necessary/non-sufficient connection-curvature gate

**2026-10-29 · C_working · new research PR.** Strengthens G1_CANONICAL_SHARP_BRIDGE, now in master. Uses the locked **sharp** anticommutator and no derivative projection, independent tetrad, Einstein–Hilbert term or assumption that Theta itself is Hermitian. Mathematical statements refer to one standard Mat(2,C) carrier; a larger biquaternion-matrix carrier is NOT automatically covered.

## Setup: the original complex bilinear metric [PROVED, conditional]

Identify the complex biquaternion with the Pauli-matrix representation. The symmetric sharp pairing has a constant nondegenerate complex Lorentz matrix:

\[
\Theta=z^a\sigma_a,\quad z^a\in\mathbb C,\qquad
\eta_{ab}=\operatorname{diag}(1,-1,-1,-1),\qquad
C(A,B)=\tfrac12\operatorname{tr}(A^\sharp B).
\]

For **zero defining connection** and the canonical global real normalization, the central metric is:

\[
g_{\mu\nu}^{\rm can}
=\mathcal N_0^{-1}C(\partial_\mu\Theta,\partial_\nu\Theta)
=\mathcal N_0^{-1}\eta_{ab}\partial_\mu z^a\partial_\nu z^b,
\qquad \mathcal N_0>0.
\]

## Stronger local flatness theorem [PROVED, exact]

The complex Jacobian of Theta is square. A regular metric forces it to be invertible **over the complex numbers**, independently of the rank of any real or imaginary part:

\[
J^a{}_\mu=\partial_\mu z^a,\qquad
g=\mathcal N_0^{-1}J^T\eta J,\qquad
\det g=-\mathcal N_0^{-4}(\det J)^2.
\]

For an invertible complex Jacobian, define the unique torsion-free metric-compatible connection by the ordinary pullback formula:

\[
\Gamma^\rho{}_{\mu\nu}
=(J^{-1})^\rho{}_a\,\partial_\mu J^a{}_\nu,
\quad \Gamma^\rho{}_{\mu\nu}=\Gamma^\rho{}_{\nu\mu},\quad
\nabla_\lambda g_{\mu\nu}=0,\qquad
R^\rho{}_{\sigma\mu\nu}[g]=0.
\]

The connection is pure matrix Jacobian gauge, so all curvature components vanish by the Maurer–Cartan identity and commuting partial derivatives. If the metric is real, its Levi-Civita symbols are real by uniqueness, and therefore its real Riemann tensor also vanishes. No assumption of full real projection rank is needed. The theorem is local and requires enough smoothness and nondegeneracy. It is a no-go ONLY for zero defining connection in this fixed four-complex-dimensional carrier.

## A rank-deficient real projection does not evade it [PROVED, explicit]

A complex affine field whose real part contains just two independent coordinate differentials has the exactly real Lorentzian sharp metric:

\[
\Theta_0=i z\,I+x\sigma_1+y\sigma_2+i t\,\sigma_3,\qquad
\operatorname{rank}_{\mathbb R}(d\,\operatorname{Re}\Theta_0)=2,\qquad
g^{\rm can}=\operatorname{diag}(1,-1,-1,-1).
\]

Use a nonlinear coordinate replacement, while the real projection still has rank two. The resulting metric is coordinate-dependent and has nonzero Christoffels, yet its full Riemann tensor vanishes:

\[
T=t+x^2,\quad X=x+yz,\qquad
\Theta_1=i z\,I+X\sigma_1+y\sigma_2+i T\,\sigma_3,
\qquad
g^{\rm can}=dT^2-dX^2-dy^2-dz^2.
\]

## Two-sided flat connection boundary [PROVED, conditional]

Use the **declared** two-sided derivative, but restrict this subtest to a determinant-preserving complex left/right isometry group; this group is an algebraic comparator and is NOT declared the unique physical UBT gauge group:

\[
D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu,\quad
A_\mu,B_\mu\in\mathfrak{sl}_2(\mathbb C),\quad
\Theta'=L\Theta R^{-1},\quad L,R\in SL_2(\mathbb C).
\]

For local left/right changes of matrix frame the potentials transform as:

\[
A'=LAL^{-1}-dL\,L^{-1},\qquad
B'=RBR^{-1}-dR\,R^{-1},\qquad
(D\Theta)'=L(D\Theta)R^{-1}.
\]

Because the sharp pairing is determinant-polarized, it is invariant under this group. If both connections are flat in a contractible patch, both can be locally gauged to zero while preserving the canonical metric. The previous flatness theorem then applies. Hence in this **precise gauge-compatible class**, a curved real nondegenerate canonical metric requires nonzero curvature in at least one of the two potential fields:

\[
C(LUR^{-1},LVR^{-1})=C(U,V),\quad
F_A=dA+A\wedge A,\quad F_B=dB+B\wedge B,
\quad (F_A=F_B=0)\Longrightarrow R[g^{\rm can}]=0
\]

This is a necessary criterion, NOT a unique connection construction or a dynamical field equation. It does not fix the action, local reality slice or physical Einstein limit.

## Composite pure-gauge attempt collapses the tetrad [COUNTEREXAMPLE]

For an invertible Theta on a local patch, the naive left logarithmic-derivative connection projected to the traceless algebra is:

\[
\Theta\in GL_2(\mathbb C),\quad
K_\mu=\partial_\mu\Theta\,\Theta^{-1},\quad
A_\mu=-(K_\mu-\tfrac12\operatorname{tr}K_\mu I_2),\quad B_\mu=0,
\]

The same algebra immediately makes every covariant Theta jet proportional to Theta. Its Gram/central sharp metric has rank at most one, so this natural pure-gauge choice cannot yield a regular spacetime. Under local left SL(2,C) transformations it has the correct connection law, but independently varying right transformations are not automatically accommodated by B=0:

\[
D_\mu\Theta=\tfrac12\operatorname{tr}(K_\mu)\Theta
=\tfrac12\partial_\mu\log\det\Theta\,\Theta,\qquad
\operatorname{rank}(g^{\rm can})\le 1.
\]

## Nonzero connection curvature alone is not sufficient [COUNTEREXAMPLE]

The ordinary pure Lorentz paired derivative with a matrix anti-Hermitian spin connection admits a separate counterexample. Choose a nonzero field and a connection **proportional to the traceless part of that field**:

\[
\Theta=t I+x\sigma_1+y\sigma_2+z\sigma_3,\quad
Z=x\sigma_1+y\sigma_2+z\sigma_3,\quad
\Omega_x=i t Z,\quad\Omega_t=\Omega_y=\Omega_z=0.
\]

The connection commutes with Theta, and its anti-Hermitian partner cancels it in the Theta jet. Consequently the canonical metric is exactly flat, even though the connection curvature is nonzero:

\[
D_\mu^\Omega\Theta
=\partial_\mu\Theta+\Omega_\mu\Theta+\Theta\Omega_\mu^\dagger
=\partial_\mu\Theta,\quad
g^{\rm can}=\eta,\quad
F^\Omega_{tx}=i Z\not\equiv0.
\]

This explicitly distinguishes **gauge curvature** from **Riemann curvature of the observable metric**. In a genuine UBT gravity solution, the relation between those curvatures requires derived tetrad compatibility, torsion/contortion constraints and actual field equations; nonzero F alone does not establish the desired spacetime dynamics. The example even has nonzero F while the curvature operator acts trivially on this particular Theta field.

## Shared Reality extension: metric-invisible holonomy [PROVED as a gauge control]

For the preceding flat-metric but curved-connection witness,
restrict to a rectangular loop in the t-x plane with y=z=0.
All connection matrices commute along this loop, so its
path-ordered holonomy and trace are exactly:

\[
\Omega_x=i\lambda t\,x\sigma_1\quad(y=z=0),\qquad
\Phi=\lambda\,\delta t\,\left(x_0\ell+\tfrac12\ell^2\right),
\quad W_\square=\exp(-i\Phi\sigma_1),\quad
\operatorname{tr}W_\square=2\cos\Phi.
\]

\[
(\lambda,\delta t,\ell,x_0)=(1,1/3,1/2,1)
\Longrightarrow \Phi=5/24,\qquad
g_{\mu\nu}=\eta_{\mu\nu},\quad
\operatorname{tr}W_\square=2\cos(5/24)\ne2.
\]

This trace is invariant under conjugation by local SU(2) spin
frame changes (with a shared loop base point). It distinguishes
the lambda family although every member has exactly the same
real canonical metric. The example does NOT establish that
a particular matter field or observer in UBT can measure this
holonomy: that requires a derived coupling and measurement
protocol. It does establish that local metric agreement
alone is too weak to select a gauge connection. A physically
grounded Shared Reality condition may have to compare accessible
holonomies in overlapping causal regions, alongside metric
observations; this remains an explicit operational research gate.

## Next falsifiable G1 task [OPEN]

The next single candidate must genuinely derive the *curved* left/right closure and its physical admissibility from Theta and the as-yet-unfinalized single action; show a nonzero effective curvature on the relevant field, real nondegenerate central sharp metric, connection/tetrad compatibility, torsion and independent variations, plus a healthy reduced linear principal symbol. Phase/projective Gram metrics remain separate exploratory comparators. **Shared Reality** should test cross-observer agreement of these *canonical real gauge-invariant* observables, not choose the connection by fiat. Preserve G1 PARTIAL and original canonical status.

**Reproduction:** `python -m unittest discover -s tests -p 'test_theta_canonical_flatness_gate.py' -v`. All 11 exact symbolic tests passed locally; GitHub Actions checks are independent. Baseline: `canonical/CANONICAL_DEFINITIONS.md:164-190`; `canonical/fields/theta_field.tex:101-160`; `G1_CANONICAL_SHARP_BRIDGE.en.md`; master action status `DEFINED_FAMILY_NOT_FINALIZED`. Do not reinterpret this as a physical metric prediction or quantum effective action.
