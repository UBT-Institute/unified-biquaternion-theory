<!-- BILINGUAL-UNIT: nonlinear-cartan.scope -->
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

# Local nonlinear Cartan lift retaining the complex Theta data

**2026-10-29; C_working; PARTIAL.** English is the translation source. This is a conditional construction for the currently written congruence model, not a choice of the fundamental component count. It supplies a local extension of the Lorentz action, but fails the independently declared standard field-phase compatibility test. The canonical covariant tetrad and central sharp metric are unchanged.

<!-- BILINGUAL-UNIT: nonlinear-cartan.carrier -->
## The declared carrier and the constant-linear obstruction

Write the generic matrix field as two Hermitian matrices in the Pauli basis. Under the already declared congruence action both coordinate vectors transform by the same real Lorentz matrix. This is a coordinate decomposition; neither part is deleted and no spacetime metric is defined by a projection.

\[
\Theta=P(X)+iP(Y),\quad P(X)=X^0 I+X^j\sigma_j,\quad
\eta=\operatorname{diag}(-1,1,1,1),\quad
\Theta\mapsto S\Theta S^\dagger,\quad
(X,Y)\mapsto(\Lambda X,\Lambda Y).
\]
\[
[J_{ab},K_c]=\eta_{bc}K_a-\eta_{ac}K_b.
\]

A constant linear de Sitter extension on this exact doubled-vector carrier would require the displayed covariance in every matrix block. The exact coefficient matrix for one block has shape **384 by 64** and rank **64**, so every vector-operator block vanishes. The required nonzero Lorentz commutator of broken generators is then impossible. This excludes that constant-linear extension, not nonlinear actions, other carriers, or the UBT programme.

<!-- BILINGUAL-UNIT: nonlinear-cartan.lift -->
## A nonlinear lift with no loss of the imaginary coordinates

Supply a positive scale in the field-coordinate units and restrict to the following smooth open chart. Relating it to the gravity length of the existing comparator requires an additional normalization bridge. The compensator alone depends only on the first vector, while the derived tangent vector retains the second.

\[
\ell>0,\quad \phi(X)=\sqrt{\ell^2-X\cdot X}>0,\quad h=X\cdot Y,
\quad n=(X,\phi),\quad v=(Y,-h/\phi),\quad
\widehat\eta=\operatorname{diag}(-1,1,1,1,1).
\]
\[
n\cdot n=\ell^2,\qquad n\cdot v=0,\qquad
X=n^{0:3},\quad Y=v^{0:3}.
\]

The joint lift has an identity coordinate minor and rank **8**. Its image is exactly the stated fixed-norm tangent chart with positive last compensator coordinate; the inverse is the displayed projection. Both lifted objects are functions of the original field data, not independent new fields. Using only the compensator in an action would leave the tangent data's dynamics unspecified. The length and action are not predicted.

The construction establishes a real smooth coordinate lift and retention of data. It does not establish complex-linearity, holomorphy or preservation of the biquaternion product.

<!-- BILINGUAL-UNIT: nonlinear-cartan.action -->
## Local group action and exact Lie brackets

Let the group act linearly on the two lifted vectors and transport that action back through the chart. Whenever the transformation and intermediate points remain inside the chart, the norm and tangency constraints prove exact reconstruction and the local composition law. This is a local action, not a global chart.

\[
g^T\widehat\eta g=\widehat\eta,\quad \det g=1,\qquad
(n',v')=(gn,gv),\qquad (X',Y')=(n'^{0:3},v'^{0:3}).
\]
\[
F_a=-\phi\,\partial_{X^a}+\frac{h}{\phi}\partial_{Y^a},\qquad
F_{ab}=-(J_{ab}X)^c\partial_{X^c}-(J_{ab}Y)^c\partial_{Y^c},
\]
\[
[F_a,F_b]=-F_{ab},\qquad
[F_{ab},F_c]=\eta_{bc}F_a-\eta_{ac}F_b.
\]

The displayed vector fields use the negative-fundamental-field convention. Their exact brackets realize the required algebra through nonlinear coefficients, evading the constant-linear obstruction. This does not derive a selected local gauge symmetry, a composite connection, or equality with the canonical spacetime tetrad.

<!-- BILINGUAL-UNIT: nonlinear-cartan.phase -->
## The standard independent phase gate fails

Test the ordinary common phase of the field values, not translation of the imaginary-time coordinate. It commutes with the Lorentz action, but not with these broken generators. The obstruction already occurs at an invertible nonzero matrix field.

\[
\Theta\mapsto e^{i\alpha}\Theta,\qquad
P=-Y^a\partial_{X^a}+X^a\partial_{Y^a},\qquad
X=(r,0,0,0),\quad Y=0,\quad r>0,\quad\Theta=rI,
\]
\[
[P,F_a]=\frac{\ell^2}{\sqrt{\ell^2+r^2}}\partial_{Y^a}\ne0
.
\]

Therefore this chart does not close the full embedding gate if the standard phase must remain an independent commuting symmetry. It does not prove that every nonlinear completion fails. Discarding the imaginary coordinates would conceal the actual problem and is not a repair.

<!-- BILINGUAL-UNIT: nonlinear-cartan.verification -->
## Verification and precise remaining obligations

`tools/verify_nonlinear_cartan_chart.py` checks the exact covariance rank, all displayed generator brackets, coordinate retention and the phase counterexample. An independent NumPy/SciPy implementation tests finite group covariance, composition and inverse recovery in **24** seeded samples. Invalid group inputs and exits from the chart are rejected. The numerical acceptance tolerance is

\[
\varepsilon_{\rm numeric}=10^{-11}.
\]

`formal/lean/UBT/GR/NonlinearCartanChart.lean` contains finite norm, tangency, quotient-cancellation and data-injectivity cores. Their compiled status is recorded in `reports/theta_nonlinear_cartan_chart_2026_10_29.json`; no local Lean runtime is installed. The full covariance-rank, differential local-action and physical statements remain LEAN-PENDING as formalizations. The canonical sharp readout, a selected connection/action, compatible phase symmetry, global continuation and the physical Dirac/stability analysis remain OPEN. The [Cartan comparator](README.en.md) and [canonical sharp audit](../conformal_causal_shared_reality/G1_CANONICAL_SHARP_BRIDGE.en.md) retain their earlier proof boundaries.
