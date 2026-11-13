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

# OI-6 — Residual U1: kinetic Hessian, constraints, and composite variation

**Status:** known conditional Hamiltonian mathematics [STD]; full UBT dynamics [OPEN]. This is an auxiliary Abelian comparator, not the Hessian, particle spectrum or action of the actual composite biquaternion field.

## A. Scope and canonical baseline

PR #898 established a generic U1 stabilizer only in the positive-Hermitian-part open sector of a full complex Theta with SL2(C) congruence. A mathematically isomorphic U1/SO2 stabilizer is **not** automatically the physical residual SO2 mode of the canonical Hamiltonian analyses. To classify dynamics we must specify the action and the primary/secondary constraint algebra. The canonical fixed-background audit already determined that the Theta kinetic action, varied with independent Palatini connection, contains no derivatives of the connection and no generated curvature-squared term at tree level.

## B. OI-6-T23 — Two inequivalent residual-gauge kinetic branches

Take an **assumed** pair of real charged scalars u,v and one Abelian gauge one-form b_mu in flat 3+1 dimensional spacetime. Under a local angle alpha, (u,v) rotates by charge q times alpha, and b_mu shifts by minus the angle derivative. This is a diagnostic field theory: its matter variables are not identified with Theta components and its b_mu is not derived from Omega(e,T).

$$
D_\mu u=\partial_\mu u-qb_\mu v,\quad
D_\mu v=\partial_\mu v+qb_\mu u,\quad
f_{\mu\nu}=\partial_\mu b_\nu-\partial_\nu b_\mu,\quad q=2.
$$

Compare a matter-only branch with the explicitly augmented Maxwell branch. Both respect the selected U1 covariance, so covariance alone cannot choose the coefficient z.

$$
\mathcal L_z=\frac12(D_\mu uD^\mu u+D_\mu vD^\mu v)
-V(u^2+v^2)-\frac z4 f_{\mu\nu}f^{\mu\nu},\qquad z\in\mathbb R.
$$

Order velocities as (u-dot,v-dot,b0-dot,b1-dot,b2-dot,b3-dot). With the (+---) signature, their pointwise kinetic Hessian is diagonal as follows:

$$
W_z=\frac{\partial^2\mathcal L_z}{\partial\dot q^I\partial\dot q^J}
=\operatorname{diag}(1,1,0,z,z,z),\quad
\operatorname{rank}W_0=2,\quad
\operatorname{rank}W_{z\ne0}=5.
$$

**OI-6-T23 [STD, conditional].** In this toy, b has no velocities when z=0; its temporal component never has a velocity even when z is nonzero. The sign z<0 gives negative vector kinetic eigenvalues and signals an instability in this isolated model. The Hessian rank alone is **not** the physical mode count: Dirac-Bergmann constraints must also be analyzed.

## C. OI-6-T24 — Auxiliary branch eliminates a gauge phase on its regular patch

On an open patch with nonzero scalar amplitude, switch to polar variables. The connection appears algebraically with no derivatives if z=0; its Euler-Lagrange equation sets the gauge-covariant phase gradient to zero.

$$
u=\rho\cos\varphi,\quad v=\rho\sin\varphi,\quad
(D_\mu u)^2+(D_\mu v)^2=
(\partial_\mu\rho)^2+\rho^2(\partial_\mu\varphi+qb_\mu)^2.
$$

$$
b_\mu=-q^{-1}\partial_\mu\varphi\quad(\rho>0,z=0),\qquad
\mathcal L_{\mathrm{eff}}=
\frac12\partial_\mu\rho\,\partial^\mu\rho-V(\rho^2).
$$

**OI-6-T24 [STD, conditional].** In this regular pure-matter model, the connection is auxiliary and does not propagate its own Maxwell polarizations. The phase is gauge, leaving one radial scalar degree of freedom. At rho=0 the algebraic equation loses rank, so this elimination is not uniform over field space. This does **not** prove that the UBT residual connection is auxiliary; its action and compositeness are different.

### OI-6-T24a — Exact reduced kinetic Hessian

Eliminating the algebraic temporal connection changes the scalar-velocity Hessian by a Schur complement. At nonzero scalar amplitude, the angular vector is its null direction and the radial vector its only kinetic direction. At the origin this elimination is undefined. The result is **not** a count of modes of the full UBT connection.

$
\mathbf r=(u,v)^T,\quad J\mathbf r=(-v,u)^T,\quad
W_{\rm reduced}=I_2-\frac{(J\mathbf r)(J\mathbf r)^T}{\mathbf r^T\mathbf r}
=\frac{\mathbf r\mathbf r^T}{\mathbf r^T\mathbf r},\qquad
\operatorname{rank}W_{\rm reduced}=1\quad(\rho>0).
$

## D. OI-6-T25 — Maxwell branch has Gauss constraints and two transverse polarizations

For positive z, the b0 momentum vanishes as a primary first-class constraint. Its preservation yields Gauss's law, the second first-class constraint. For a nonzero spatial Fourier momentum, the transverse projector has rank 2. Four gauge-vector configuration variables minus two first-class constraints yield two propagating vector polarizations. With two real charged scalars the total configuration-space count is 4 in this model, whether described on the symmetric side or as one radial scalar plus a massive vector in a regular nonzero-amplitude gauge.

$$
\pi^0\approx0,\qquad
\mathcal G=\partial_i\pi^i+q(u\pi_v-v\pi_u)\approx0,\qquad
P_{ij}(\mathbf k)=\delta_{ij}-\frac{k_ik_j}{|\mathbf k|^2},\quad
\operatorname{rank}P=2\ (\mathbf k\ne0).
$$

**OI-6-T25 [STD, conditional].** A propagating residual U1 vector requires a physical kinetic term and appropriate sign; the stabilizer group structure and matter covariance do not generate that term. The first-class count is standard for an ordinary Abelian gauge theory with compatible matter couplings and regular constraints.

## E. OI-6-T26 — The composite variational chain changes the Hessian

The actual UBT issue is not simply whether a connection term is chosen, but which fields depend on Theta before variation. The exact Euler-operator chain rule for a composite embedding must include the formal adjoints of the Fréchet derivatives of every substituted field. All derivatives, boundary conditions and field dependencies matter.

$$
S_{\rm comp}[\Theta]=S[\Theta,e[\Theta],\omega[\Theta]],\qquad
\mathcal E_\Theta^{\rm comp}
=\mathcal E_\Theta+
(D_\Theta e)^*\,\mathcal E_e+
(D_\Theta\omega)^*\,\mathcal E_\omega .
$$

A finite one-dimensional comparator exposes the difference even before the UBT nonlinearity. Vary independent theta and e versus substitute e=a theta-dot first:

$$
L(\dot\theta,e)=\frac12(\dot\theta-e)^2+\frac\kappa2 e^2,\qquad
e=a\dot\theta,\qquad
W_{\rm independent}=1,\quad
W_{\rm composite}=(1-a)^2+\kappa a^2.
$$

For instance a=1, kappa=0 makes the composite kinetic coefficient vanish even though the independent-field Hessian is nonzero. Exact symbolic rational tests match the full Euler variational chain. If e[Theta] contains derivatives, naive finite-dimensional pullback formulas for the Hessian can miss higher derivatives and extra constraints.

**OI-6-T26 [STD, conditional].** A Hessian obtained with independent e and omega cannot by itself certify the physical modes, signs, or stability of a composite field theory after these variables are substituted. This methodological limitation matches the explicit unresolved scheme distinction in canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex.

## F. Canonical UBT compatibility and the exact next task

The canonical files already derive Omega(e,T) from a prescribed tetrad and torsion, reduce the Lorentz-compatible pair to one spin connection, and construct local torsionful single-Theta representers. The pure split-jet auxiliary sector is already known to be nonpropagating, and pure right-inverse constraints do not select physical tetrads. Repeating that closure as a new theorem is unwarranted. The remaining task is to specify a single actual action, an admissible composite e[Theta] and K[e,Theta], and compute its **full** Hessian and constraint closure.

**G-OI6-19 [OPEN]:** check whether the residual U1 of the single-matrix congruence really coincides with the UBT SO2 direction in the constrained composite system. **G-OI6-20 [OPEN]:** derive the Fréchet linearizations of e[Theta], Omega[e,K] and K[e,Theta] on one non-null nondegenerate canonical background, including time derivatives. **G-OI6-21 [OPEN]:** compute the reduced principal symbol, kinetic signature and first/second-class constraint closure of that actual action, not the toy Maxwell augmentation.

## G. Reproducibility and established methods

The standard-library test script research_tracks/ontological_information_axioms/verify_residual_u1_hessian.py passed 13/13 local tests on 2026-11-13; Git blob SHA bdb7a531224a61a55aa7c8926963728111c8daaa was verified identical to the committed GitHub source. Tests cover exact rational Hessian ranks and sign, auxiliary elimination, local U1 covariance, transverse Fourier projector and constraint count, and the exact variational-chain pullback. This is a mathematical comparator, not validated UBT dynamics.

- J. David Brown (2022), *Singular Lagrangians, Constrained Hamiltonian Systems and Gauge Invariance*: https://arxiv.org/abs/2201.06558 .
- *Constraint characterization and degree of freedom counting in Lagrangian field theory* (2024): https://doi.org/10.1103/PhysRevD.109.025010 .
- Canonical UBT comparison: canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex and canonical/gr_closure/gap_10i_torsionful_local_representer.tex (internal sources, not independent validation).