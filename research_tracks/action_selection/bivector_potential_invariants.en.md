<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: bivector-potential-invariant.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact algebraic degree-four result; no new fundamental UBT action or physical CMB prediction.
UBT-AI-PROVENANCE-END
-->
# Vector, tensor and bivector potentials: exact algebraic audit and derivative frontier

**Status: PROVED CONDITIONAL ALGEBRA / FUNDAMENTAL DYNAMICS OPEN.** The prior full polynomial-potential classification in `theta_potential_invariants.en.md` is authoritative: with the declared spin-congruence and U(1) phase symmetry, the single-Theta derivative-free scalar potential at degree at most four is exhausted by H and |det X|². The purpose here is to test alternative *representations* of those invariants and to identify which proposals truly require geometric derivatives or new field content.

## Two Lorentz vectors within one complex biquaternion

Use the existing Pauli representation of a generic non-Hermitian Theta field:

\[
X=z^\mu\sigma_\mu,\quad z^\mu=u^\mu+iv^\mu,\quad
\eta=\operatorname{diag}(+1,-1,-1,-1),
\quad u,v\in\mathbb R^{1,3}.
\]

Because SL(2,C) acts on each Hermitian part as the same real Lorentz transform, while the original U(1) phase rotates both parts, the group action is

\[
X\mapsto e^{i\alpha}SXS^\dagger,\quad
u\mapsto\cos\alpha\,u-\sin\alpha\,v,\quad
v\mapsto\sin\alpha\,u+\cos\alpha\,v.
\]

Two natural **phase-neutral** tensors are

\[
B_{\mu\nu}=u_\mu v_\nu-u_\nu v_\mu,\quad
S_{\mu\nu}=u_\mu u_\nu+v_\mu v_\nu.
\]

Here B is a *field-value bivector* and S a symmetric tensor. They are not the Cartan torsion or the independent spin-connection curvature. Their scalar building blocks satisfy

\[
H(X)=\operatorname{Tr}(X^\sharp X^\dagger)=2(u^2+v^2),\quad
|\det X|^2=(u^2-v^2)^2+4(u\cdot v)^2.
\]

## New exact identity: bivector 'potential' is not a new invariant

Direct contraction gives the factorization

\[
\boxed{
B_{\mu\nu}B^{\mu\nu}
=2[u^2v^2-(u\cdot v)^2]
=\frac18 H(X)^2-\frac12|\det X|^2.}
\]

The symmetric tensor supplies no new degree-four scalar either:

\[
\boxed{
S^\mu{}_\mu=\tfrac12H(X),\qquad
S_{\mu\nu}S^{\mu\nu}=\tfrac18 H(X)^2+\tfrac12|\det X|^2.
}
\]

The simple bivector has identically zero pseudoscalar square and a single vector has no nonzero self-wedge:

\[
\epsilon^{\mu\nu\rho\sigma}B_{\mu\nu}B_{\rho\sigma}=0,
\qquad u_{[\mu}u_{\nu]}=0.
\]

The existing quartic scalar family is

\[
V_4(X)=V_0+m^2H+\lambda_1H^2+\lambda_2|\det X|^2,\quad
\Delta V=\lambda_B B_{\mu\nu}B^{\mu\nu}.
\]

Consequently adding a proposed bivector potential changes ONLY the known couplings:

\[
\boxed{
\lambda_1\mapsto\lambda_1+\lambda_B/8,\qquad
\lambda_2\mapsto\lambda_2-\lambda_B/2.
}
\]

This is not a new field-theoretic sector, nor does it remove the known indefinite kinetic signature or the original fixed-background quartic instability simply by being renamed 'bivector potential'. A derivative-free Lorentz scalar made from S and B at this polynomial order is already in the classified space; a free vector/tensor term would require an additional contraction, an explicit background (breaking symmetry), a new carrier or derivatives.

## What happens on the established timelike single-Theta branch

On the Lorentz-real classical subspace, X has only one real Hermitian four-vector up to an overall phase, so u and v are parallel: B vanishes. At the standard radial minimum one finds the exact second-order behavior

\[
X_0=irI,\quad r>0,\quad
B_{\mu\nu}(X_0)=0,\quad
\left.\frac{\partial (B^2)}{\partial z^a}\right|_{X_0}=0,\quad
B^2=-2r^2\sum_{i=1}^{3}(\delta u^i)^2+O(\delta z^3).
\]

The first variation of B² therefore vanishes on that branch, including the composite-metric volume factor. It **cannot** source the missing normal/lapse Euler equation at that background by itself. The transverse quadratic Hessian is nonzero, and it is precisely a reparameterization of the original classified quartic coefficients — its physical stability must still be judged by the full constrained kinetic Hessian.

## Geometric/derivative operators that ARE genuinely distinct

For the invariant radial clock r of the positive Hermitian Lorentz orbit, the kinematic unit-gradient theorem of merged PR #688 and draft PR #689 implies

\[
n_\mu=\frac{\partial_\mu r}{\sqrt{\mathcal N_0}},\quad
n_\mu n^\mu=-1,\quad
2\nabla^{\rm LC}_{[\mu}n_{\nu]}=0,\quad
n^\nu\nabla^{\rm LC}_\nu n_\mu=0.
\]

Thus a 'Maxwell' term made solely from the exact clock one-form n has **zero** field strength (for torsion-free Levi-Civita differentiation); the vorticity and the unit-clock acceleration vanish. However its symmetric derivative (extrinsic curvature, expansion and shear) can be nonzero. Known Einstein-aether/khronometric derivative operators use these terms, but may propagate extra scalar modes and require new stability and observational checks.

Potentially non-redundant *geometric* action densities, to be derived or excluded within the **single canonical UBT action**, include

\[
\mathcal O_{\mathrm{trace}}=t_\mu t^\mu,\quad
\mathcal O_{\mathrm{curv}}=\epsilon_{abcd}e^a\wedge e^b\wedge\mathcal R^{cd},\quad
\mathcal O_{\mathrm{YM}}=\operatorname{Tr}(F_{\mu\nu}F^{\mu\nu}).
\]

The first uses the existing 24-component torsion (trace/vector part), the second is a bivector two-form contracted with spin curvature (Einstein–Cartan/Palatini structure), and the third gives independent spin-connection kinetic derivatives. None is an algebraic polynomial potential solely of field values X. A noncompact Lorentz/SL(2,C) Yang–Mills trace has indefinite internal form in naive formulations; no healthy gauge modes should be assumed. Likewise introducing an independent Kalb–Ramond 2-form is an additional field, not free new content of the single X.

On a homogeneous FLRW slice, the extrinsic curvature squared terms collapse to

\[
K_{ij}K^{ij}=3H_{\mathrm{FLRW}}^2,\qquad
K^2=9H_{\mathrm{FLRW}}^2.
\]

which is only one parameter combination on this symmetric background. The full anisotropic/perturbative Hessian, spin-current variation and local Hamiltonian constraint must be computed before claiming physical improvement.

## Decision for UBT

**Algebraic bivector/vector/tensor potential alone: NO new degree-four invariant, and no rescue of the normal constraint in the timelike branch.** **Curvature/torsion/bivector derivative interactions: worth testing**, but they must arise from one coherent, gauge-invariant, real-valued action, not be added as separate fundamental patches. Priority gate: compute the variation of the lowest-order torsion and Palatini curvature invariants with the **composite** tetrad e=DTheta/sqrt(N0), then classify the resulting primary/secondary Dirac constraints, causal speeds and sign of physical modes. CMB prediction remains OPEN.

**Repo grounding:** `canonical/ACTION.en.md`; `research_tracks/action_selection/theta_potential_invariants.en.md`; `research_tracks/action_selection/flrw_canonical_contortion.en.md`; `research_tracks/action_selection/timelike_orbit_unitclock.en.md` (draft PR #689). **Independent precedent:** Einstein-aether/khronometric derivative classification, https://doi.org/10.1103/PhysRevD.70.024003 . **Checker:** `tools/verify_bivector_potential_invariants.py` and focused pytest.
