<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: full-theta-sharp-norm-psi-winding -->
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


# Full complex-Theta sharp-norm winding without replacing the tetrad

**2026-10-31 · C_working.** This exact local topological counterexample does not establish strings or physical field dynamics. Earlier PR #824 restricted its vanishing-winding statement to w(H) on a Hermitian branch. That does NOT exclude the central complex norm of the original full Theta winding on an indefinite-H patch.

## Central quaternion sharp norm [ASSUMED]

The original complex biquaternion admits its faithful 2-by-2 matrix representation. Its determinant is EXACTLY the central quaternion-sharp norm, not a competing metric or a Hermitian Gram replacement:

\[
\Theta=H+X\in\mathbb C\otimes\mathbb H
\simeq\operatorname{Mat}_2(\mathbb C),\quad
H^\dagger=H,\quad X^\dagger=-X,\quad
\Theta^\sharp\Theta=\det\Theta\,I_2.
\]

## Explicit regular full-Theta winding [PROVED]

Set a fixed nonsingular but indefinite Hermitian H, and choose a smooth periodic anti-Hermitian X. The extra B symbol below is a matrix of ALREADY EXISTING original-field components, not an independent new field or connection:

\[
\theta=\psi/R_\psi,\quad 0<\rho<1,\quad
H=\sigma_3=\operatorname{diag}(1,-1),\quad
c=\sqrt{1+\rho\cos\theta},\quad b=\rho\sin\theta,
\]

Take the single full field on the real physical spacetime and compact internal psi circle:

\[
B_\psi=\begin{pmatrix}0&c\\c&b\end{pmatrix},\qquad
\Theta(t,x,y,z,\psi)=H+i(B_\psi+tI_2+x\sigma_1+y\sigma_2+z\sigma_3).
\]

At the spacetime origin, its full central sharp norm is nonzero and winds once. Replacing theta by n theta gives any integer n. The nonzero determinant persists on a sufficiently small 4D spacetime neighborhood by continuity and compactness of the psi circle:

\[
\det H=-1,\quad
\det\Theta(0,0,0,0,\psi)
=-1+c^2+ib=\rho e^{i\theta}\ne0,\quad
\nu_\Theta=\frac1{2\pi i}\oint d\log\det\Theta=1.
\]

## The original tetrad and sharp metric survive [PROVED]

In this local FLAT defining-connection witness, the four spacetime derivatives of the SAME Theta remain exactly the familiar anti-Hermitian basis, with no psi projector or fiber average:

\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\quad
\mathcal N_0=1,\quad D_\mu=\partial_\mu,\quad
(E_t,E_x,E_y,E_z)=(iI_2,i\sigma_1,i\sigma_2,i\sigma_3).
\]

The actual canonical central quaternion-sharp anticommutator yields a regular Minkowski tetrad and metric at EVERY psi:

\[
e_\mu{}^a=\operatorname{diag}(1,-1,-1,-1),\quad\det e=-1,\quad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=
\operatorname{diag}(-1,1,1,1)_{\mu\nu}I_2.
\]

This is a kinematic witness only: no microscopic Euler equation is shown, and the metric is flat in this example. The full Theta is nonconstant along psi even though its 4D tetrad is constant.

## Distinct logarithmic connections and square-root sign [PROVED]

The former Hermitian-determinant reality compensator is zero. The FULL central sharp norm supplies another, mathematically defined scalar 1-form wherever Theta is invertible:

\[
w_H=-\tfrac12d\log|\det H|=0,\quad
\mathcal A_\Theta:=\tfrac12d\log\det\Theta=
\tfrac12\operatorname{tr}(\Theta^{-1}d\Theta),\quad
(\mathcal A_\Theta)_\psi|_0=i/(2R_\psi).
\]

Its integral has a nontrivial square-root sign. This is the holonomy of a FORMAL determinant-square-root line; it is NOT automatically physical spin, spin statistics or a charged spinor field:

\[
\oint\mathcal A_\Theta=i\pi,\quad
\exp(\oint\mathcal A_\Theta)=-1,\quad
\sqrt{\det\Theta}|_0=\sqrt\rho\,e^{i\psi/(2R_\psi)}.
\]

Do NOT replace w(H) with A_Theta in the defining tetrad derivative: reality would generally fail. The two geometric/composite objects have different purposes and neither is a new independent fundamental field.

## Why strictly positive H forbids the full winding [PROVED]

If H is positive definite EVERYWHERE around the circle, the full complex Theta is strictly accretive. The exact homotopy shrinks the anti-Hermitian X without meeting a zero determinant:

\[
H(\psi)>0,\quad \Theta_u=H+uX,\quad 0\le u\le1,\quad
\Re(v^\dagger\Theta_uv)=v^\dagger Hv>0\quad(v\ne0)
\Longrightarrow\det\Theta_u\ne0
\Longrightarrow\nu_\Theta=0.
\]

Therefore the full determinant winding is zero in that POSITIVE subsector; likewise for everywhere negative definite H. This is a restriction on H's inertia, not a no-go of original complex-biquaternion UBT. Our H has inertia (1,1). Its traceless stabilizer is su(1,1), not su(2):

\[
\Omega\in\{\sigma_1,\sigma_2,i\sigma_3\}
\subset\mathfrak{su}(1,1),\quad
\Omega H+H\Omega^\dagger=0,\quad
[\sigma_1,\sigma_2]=2i\sigma_3.
\]

## Conditional matter shift, not string T-duality [OPEN]

The winding is invariant under unimodular Lorentz congruence, and a periodic real rescaling changes A_Theta only by an exact form:

\[
\Theta'=S\Theta S^\dagger,\ \det S=1
\Longrightarrow\det\Theta'=\det\Theta,\qquad
\Theta'=e^\varepsilon\Theta,\ \varepsilon\in\mathbb R
\Longrightarrow\mathcal A_\Theta'=\mathcal A_\Theta+d\varepsilon.
\]

ONLY IF a separate physical field is supplied with a justified charge q under the new composite A_Theta will its periodic Fourier spectrum be half-shifted at odd q. This equation is a DECLARED diagnostic probe, not a derived UBT mode equation:

\[
\mathcal D_\psi^{(q)}=\partial_\psi+q\mathcal A_{\Theta,\psi},\quad
\mathcal D_\psi^{(q)}e^{im\psi/R_\psi}=
i(m+q/2)e^{im\psi/R_\psi}/R_\psi,
\quad m,q\in\mathbb Z.
\]

The existing chronofactor Fourier label is KK momentum, not an independently dynamical winding of a fundamental string. Prior repository work already established a CONDITIONAL Gaussian momentum-winding lattice but no full UBT T-duality; the old restricted local dual-field maps failed. This novel determinant winding therefore creates a concrete separate topological integer but does NOT derive a string worldsheet, string tension, physical fermion, new mass or particle generations.

## Exact reproducibility and next action gate [OPEN]

**21 exact SymPy tests** in `tests/test_full_theta_det_winding_tetrad_2026.py`, added to Physics Laws CI. Tests distinguish the full sharp norm, H positivity, winding, unchanged Lorentz tetrad/metric, Lorentz congruence, su(1,1), half-root sign, conditional probe and lack of selected psi dynamics. **Next falsifiable task:** determine whether the existing SINGLE-Theta action and full constraints admit indefinite-H configurations and whether a nontrivial psi kinetic term and charged matter coupling can be derived without damaging the canonical tetrad. Reuse: `canonical/CANONICAL_DEFINITIONS.md:130-201`, `canonical/fields/chronofactor_operator.tex:95-180`, `canonical/THEORY/t_duality_ubt.tex:31-90`, `reports/t_dual_winding_verdict.md:25-70`, `research_tracks/action_selection/complex_time_graded_reflection_fork_2026_10.en.md:15-134`. No Lean proof, real-world detection or final physical theory is claimed.
