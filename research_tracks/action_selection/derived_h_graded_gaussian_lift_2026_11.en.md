<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: derived-h-gaussian.scope -->
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

# Derived-H graded jet: a local Gaussian lift and the on-shell presymplectic current

**2026-11-02 · C_working · PROVED under declared comparator assumptions.** English is the translation source. The new contribution is a smooth local right inverse with the central one-form already fixed by H, followed by its complete local variational boundary term. The old freely varied central one-form is not reused as an independent variable.

<!-- BILINGUAL-UNIT: derived-h-gaussian.reuse -->
## Existing results and the precise new gate

The covariant tetrad and its central-sharp metric stay locked. The original full complex biquaternion, its Hermitian/anti-Hermitian decomposition, the Lorentz-equivariant real-linear graded connection and the formal-adjoint transmission theorem already exist in [U1–U3]. The older free split-jet presymplectic and spatial Dirac results [U4–U5] do not automatically apply after deriving the central form from H. The full-Theta winding audit [U6] explicitly retains that distinction. We close local representability in the positive-H graded comparator and compute its actual presymplectic boundary correction. No action is selected.

<!-- BILINGUAL-UNIT: derived-h-gaussian.variables -->
## Domain, representations and independent variables

Work with smooth fields on a sufficiently small contractible Lorentzian patch before Gaussian normal geodesics develop focal points. Use the existing congruence representation and real-linear graded connection of [U1]. The entire tetrad, rather than a projected output, is Lorentz-real. The Hermitian and anti-Hermitian parts are coordinates of the same original field. The defining spin varpi and the physical curvature spin omega have distinct roles. K is the freely varied algebraic Lorentz tensor of that existing comparator; it is not a second propagating gauge connection.

\[
\Theta=H+X,\quad H^\dagger=H>0,\quad X^\dagger=-X,\quad
s=\sqrt{\mathcal N_0}>0,\quad \eta=\operatorname{diag}(-1,1,1,1).
\]
\[
\mathfrak D_\mu\Theta=\partial_\mu\Theta+
\varpi_\mu\Theta+\Theta\varpi_\mu^\dagger+w_\mu(H)\Theta+
K_\mu X+XK_\mu^\dagger,\qquad
w_\mu(H)=-\tfrac12\partial_\mu\log\det H.
\]
\[
\widehat H=H/\sqrt{\det H},\quad
D^\varpi_\mu\widehat H=0,\quad
e_\mu{}^a=s^{-1}\left[\partial_\mu X^a+
(\varpi_\mu{}^a{}_b+K_\mu{}^a{}_b)X^b+w_\mu X^a\right].
\]
\[
E_\mu=s^{-1}\mathfrak D_\mu\Theta,\qquad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=g_{\mu\nu}I_2,\qquad g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab}.
\]

<!-- BILINGUAL-UNIT: derived-h-gaussian.lift -->
## Smooth local right inverse [PROVED]

Let e be any smooth nondegenerate Lorentz coframe. A local Gaussian normal coordinate u exists about a non-null hypersurface after shrinking the patch. A spacelike initial hypersurface always supplies the timelike-normal choice. The dual normal n defined below has fixed norm. Choose arbitrary positive representation constants L and h0; they are neither action couplings nor predictions. The coordinate u is used to construct a representative, and is not an extra independently varied physical field.

\[
g^{\mu\nu}\partial_\mu u\,\partial_\nu u=\varepsilon,\quad
\varepsilon\in\{-1,1\},\qquad
n^a=e^{a\mu}\partial_\mu u,\quad
n^an_a=\varepsilon,\quad n_ae_\mu{}^a=\partial_\mu u.
\]
\[
X^a=sL n^a,\qquad
H=hI_2,\qquad h=h_0e^{-\varepsilon u/L}>0,\qquad
\varpi_\mu=0,\qquad w_\mu(H)=\frac{\varepsilon}{L}\partial_\mu u.
\]
\[
q=X^aX_a=\varepsilon s^2L^2\ne0,\qquad
R_\mu{}^a=s e_\mu{}^a-\partial_\mu X^a-w_\mu X^a.
\]
\[
X_aR_\mu{}^a=s^2L\,\partial_\mu u-w_\mu q=0,\qquad
K_{\mu ab}=\frac{R_{\mu a}X_b-X_aR_{\mu b}}q,\qquad
K_\mu{}^a{}_bX^b=R_\mu{}^a.
\]
\[
\boxed{\mathfrak D_\mu(H+X)=sE_\mu,\qquad e[\Theta,K,\varpi]=e.}
\]

<!-- BILINGUAL-UNIT: derived-h-gaussian.interpretation -->
## Regularity, full-Theta invertibility and covariance [PROVED]

The denominator is nonzero, and all constructed fields are smooth on the chosen patch. Normalized H is the identity and is parallel with the chosen defining connection. The construction permits arbitrary physical omega, including the Levi-Civita connection of the supplied coframe. Setting the defining varpi to zero does not set physical curvature to zero or identify the jet correction with physical torsion. Applying any smooth Lorentz congruence gives the general frame version under [U1].

\[
v^\dagger(H+X)v=h\,v^\dagger v+v^\dagger Xv,\quad
\operatorname{Re}\bigl(v^\dagger(H+X)v\bigr)=h\,v^\dagger v>0
\quad(v\ne0).
\]
\[
\det(H+X)\ne0\qquad(\forall\,\varepsilon\in\{-1,1\}).
\]
\[
X=i(x^0I_2-x^j\sigma_j),\quad q=-(x^0)^2+\sum_j(x^j)^2,\qquad
\det(hI_2+X)=h^2+q+2ihx^0.
\]

<!-- BILINGUAL-UNIT: derived-h-gaussian.limits -->
## What the right inverse does not supply

For a timelike X the real part of this determinant can vanish while its imaginary part is nonzero. The accretivity argument avoids a mistaken determinant-sign argument and covers both signs. This positive-H lift lies in the zero-winding subsector identified in [U6]; it does not lift the indefinite-H winding interpolation. The choice of u depends on the supplied metric through a local geodesic/PDE construction. It is not an algebraic universal formula for a dynamically selected connection functional of arbitrary Theta, and it gives no global, null-patch or horizon extension.

<!-- BILINGUAL-UNIT: derived-h-gaussian.variation -->
## Complete variation in an admissible local chart [PROVED]

On the positive-H patch use a smooth Lorentz frame to set normalized H to the identity. The residual defining spin preserves it. Because K is freely varied, its sum with that defining spin is an arbitrary Lorentz-algebra-valued one-form A in this chart. The point transformation Y=X/h is invertible. The independent variations used below are Y, positive h, A and physical omega. They are admissible directions of the original constrained graded comparator. No Gaussian coordinate is varied as a new field. The cancellation of the derivative of h is exact.

\[
H=hI_2,\qquad A=\varpi+K,\qquad Y=X/h,\qquad
e_\mu{}^a=\frac h s(D^A_\mu Y)^a,\quad D^A_\mu Y=\partial_\mu Y+A_\mu Y.
\]
\[
\delta e_\mu{}^a=\frac h s
\left[(D^A_\mu\delta Y)^a+\delta A_\mu{}^a{}_bY^b\right]
+\frac{\delta h}h e_\mu{}^a.
\]
\[
s\,\delta e_\mu{}^a=
(D^{A+w}_\mu\delta X)^a+\delta A_\mu{}^a{}_bX^b
-X^a\partial_\mu\zeta,\qquad
\zeta=\delta\log h,\quad \delta w_\mu=-\partial_\mu\zeta.
\]

<!-- BILINGUAL-UNIT: derived-h-gaussian.stationary -->
## Exact stationary transmission [PROVED, conditional]

Supply the already chosen differentiable, local-Lorentz-invariant gravity-only geometric functional with independent e and omega and its complete boundary potential. It has no direct Y, h, A or additional matter dependence. Compactly supported variations remove its boundary integral. The A equation makes the tetrad Euler covector normal to Y. Integration by parts gives the displayed Y equation, while varying h supplies the missing trace equation. Invertibility of e and non-null Y force the normal coefficient to vanish. The remaining physical-omega equation is the original fixed-tetrad Cartan equation.

\[
\delta\mathcal L_0
=\mathcal P^\mu{}_a\delta e_\mu{}^a+
\mathcal C^\mu{}_{ab}\delta\omega_\mu{}^{ab}
+\partial_\mu\vartheta_0^\mu,\qquad
\mathcal L_{\rm pull}=\mathcal L_0(e[Y,h,A],\omega).
\]
\[
\delta_A S_{\rm pull}=0\quad\Longrightarrow\quad
\mathcal P^\mu{}_a=f^\mu Y_a.
\]
\[
\mathcal E_{Y,a}
=-\frac1s\left[\partial_\mu(h f^\mu)Y_a+s f^\mu e_{\mu a}\right]=0,
\qquad
\mathcal E_h=\frac1h\mathcal P^\mu{}_a e_\mu{}^a=0.
\]
\[
V^\mu=e^\mu{}_aY^a,\quad
c=-s^{-1}\partial_\mu(hf^\mu),\quad
f^\mu=cV^\mu,\quad
0=\mathcal P^\mu{}_a e_\mu{}^a=cY^2
\quad\Longrightarrow\quad f^\mu=0,\quad\mathcal P=0,\quad\mathcal C=0.
\]

<!-- BILINGUAL-UNIT: derived-h-gaussian.stationaryscope -->
## Local implication and its exact boundary

Conversely, vanishing base Euler covectors make the complete composed first variation zero in every admissible original direction, including normalized-H and defining-spin variations. Together with the new local right inverse this gives local stationary lifts of every supplied geometric solution in this restricted comparator. In particular an Einstein–Lambda solution of the adopted Palatini/MM gravity branch has such a graded positive-H lift. This does not determine that branch, its coefficient or a microscopic action. It is not the older pointwise rank argument: at fixed h and Y the A image still has rank below the full tetrad rank.

<!-- BILINGUAL-UNIT: derived-h-gaussian.current -->
## Presymplectic boundary term on the stationary surface [PROVED, conditional]

The same integration by parts, retaining the entire base potential including any Euler/topological contribution, yields the additional carrier boundary term below. Evaluate its antisymmetrized variation only on a stationary solution and two tangent variations obeying the linearized tetrad equation. The extra current then vanishes. This proves equality of these pullback currents under the stated support and boundary conventions. It does not establish a global symplectic bijection, finite boundary charges, a complete Dirac quotient, or removal of all vertical complex/psi modes.

\[
\vartheta_{\rm pull}^\mu
=F^*\vartheta_0^\mu+\frac h s\mathcal P^\mu{}_a\delta Y^a
=F^*\vartheta_0^\mu+\frac1s\mathcal P^\mu{}_a
(\delta X^a-X^a\delta\log h).
\]
\[
\omega_{\rm pull}^\mu-F^*\omega_0^\mu
=\frac1s\left[
\delta_1(h\mathcal P^\mu{}_a)\delta_2Y^a-
\delta_2(h\mathcal P^\mu{}_a)\delta_1Y^a\right]=0
\quad(\mathcal P=\delta_1\mathcal P=\delta_2\mathcal P=0).
\]

<!-- BILINGUAL-UNIT: derived-h-gaussian.verification -->
## Verification and remaining physics gates

The exact SymPy checker has 12 passing tests covering both normal signs, nonconstant boosted curved coframes, the actual sharp matrix metric, determinant signs, the full unrescaled chain rule, the point transformation, the boundary correction and the final normal-source trace. The independent NumPy implementation samples 128 coframes for each sign and differentiates the normal numerically in all coordinate directions with step 0.00001. Its absolute acceptance tolerance is 0.00000002; the largest observed coframe-recovery error is below 0.00000000004. Neither code proves Gaussian-coordinate existence or the continuum variational theorem; the analytic arguments above carry those implications.

<!-- BILINGUAL-UNIT: derived-h-gaussian.gates -->
## Status

**LEAN-PENDING:** Lean and Lake are unavailable in this runtime; no checked formalization is supplied. The companion record binds actual tools, source hashes and exclusions. Independent bilingual semantic review remains pending; this work must remain a draft until repository gates pass. The calculation uses the smooth scalar-fiber branch of [U7], without imposing strict holomorphy in every Lorentz frame. It does not identify left U(1), Lorentz congruence and psi translation, derive an observer channel or a psi-principal term, select a potential or a physical measure, or establish ghost freedom. Fundamental action status remains DEFINED_FAMILY_NOT_FINALIZED and physical GR recovery remains CONDITIONAL.

<!-- BILINGUAL-UNIT: derived-h-gaussian.sources -->
## Sources and executable artifacts

The references below are the reused premises and the new verification artifacts. No historical priority, independent external review or author attestation is claimed.

- [U1] [Graded full-Theta representation](full_theta_reallinear_graded_jet_2026_10.en.md).
- [U2] [Derived-H formal-adjoint theorem](dynamics_reuse_hermitian_mm_adjoint_2026_10.en.md).
- [U3] [Hermitian determinant and sharp geometry](full_theta_hermitian_compensator_2026_10.en.md).
- [U4] [Free split-jet presymplectic variation](mm_composite_presymplectic_variation.en.md).
- [U5] [Free split-jet spatial Dirac reduction](splitjet_spatial_dirac_2026_10.en.md).
- [U6] [Full-Theta winding and restricted on-shell lift](mm_full_theta_psi_winding_decoupling_2026_11.en.md).
- [U7] [Complex-time locality and holomorphy boundary](complex_time_graded_reflection_fork_2026_10.en.md).
- [V1] [Exact tests](../../tests/test_derived_h_graded_gaussian_lift.py).
- [V2] [Independent numerical check](../../tools/verify_derived_h_graded_gaussian_lift_numeric.py).
- [V3] [Verification record](../../reports/derived_h_graded_gaussian_lift_2026_11_02.json).
