<!-- BILINGUAL-UNIT: c5-aux.scope -->
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

# Auxiliary jet test of the self-contracted kinetic action

Date: 2026-10-08. Status: **DERIVED_WITH_ASSUMPTIONS [L1]**; physical completion: **OPEN_GAP**. This is a local obstruction for one explicitly defined action in the independent-complex-tau research alternative. It does not change the canonical UBT action registry or disprove its conditional effective GR branch. The [overview](README.en.md) separates the complex coordinate hypothesis from this real variational test.

<!-- BILINGUAL-UNIT: c5-aux.assumptions -->
## Domain, independent variables and representation

Work on an oriented real five-dimensional patch, with smooth fields, compactly supported variations and fixed orientation. Choose a fixed nowhere-zero one-form u and a prescribed Lorentz reference connection omega. The independent variables are the Lorentz-real components X of the original field Theta, a Lorentz-antisymmetric auxiliary one-form K, and a relative-central real one-form w. No additional fundamental matter field is introduced. Absorb the fixed global jet normalization into the fields and take nonzero constant tension T.

\[
A=0,\ldots,4,\quad a=0,\ldots,3,\quad
\eta_{ab}=\operatorname{diag}(-1,1,1,1),\quad
X^2=\eta_{ab}X^aX^b\ne0,\quad K_{Aab}=-K_{Aba}.
\]
\[
E_A^a=\partial_A X^a+\omega_A{}^a{}_bX^b
       +K_A{}^a{}_bX^b+w_AX^a,\qquad
e_A{}^I=(E_A^a,u_A),\qquad \det e\ne0.
\]

The composite coframe E is not varied independently. In the biquaternionic representation, ddagger is Hermitian conjugation, Omega represents the reference Lorentz connection, and the calligraphic K represents its Lorentz jet correction. Multiplication sides are explicit:

\[
D_A\Theta=\partial_A\Theta+A_A\Theta-\Theta B_A,
\quad A_A=\Omega_A+\mathcal K_A+\tfrac12w_AI,
\quad B_A=-\Omega_A^\ddagger-\mathcal K_A^\ddagger-\tfrac12w_AI.
\]

The relative-central term is a jet dilation, not a metric-compatible physical spin connection. This calculation does not identify the jet connection with the physical Levi–Civita connection. Simultaneous Lorentz frame transformations of X, E and the connections preserve the construction; a gauge-invariant potential must also be Lorentz invariant. The calculation below permits any smooth algebraic potential in a fixed frame. No gauge quotient or physical degree-of-freedom count is assumed.

<!-- BILINGUAL-UNIT: c5-aux.action -->
## Defined action and exact kinetic contraction

Use the same Lorentz pairing in the metric and the kinetic term, with a smooth potential depending only on field values:

\[
g_{AB}=\eta_{ab}E_A^aE_B^b+u_Au_B,
\qquad
S_{\rm aux}=\mathcal T\int d^5Z\sqrt{|g|}
\left[\tfrac12g^{AB}\eta_{ab}E_A^aE_B^b-V(X)\right].
\]

There are no curvature terms, derivatives of K or w, or further terms in this candidate. Full coframe invertibility implies the following identities without requiring E to be exact:

\[
g^{AB}u_Au_B=1,\qquad
g^{AB}\eta_{ab}E_A^aE_B^b=4,\qquad
S_{\rm aux}=\mathcal T\int d^5Z\sqrt{|g|}F(X),
\quad F=2-V.
\]

Unlike the exact-gradient case, this density need not be a pullback of a fixed top-degree form. Its auxiliary variation must therefore be computed. Holding the composite metric fixed would define a different variational problem.

<!-- BILINGUAL-UNIT: c5-aux.inverse -->
## Existing jet right inverse applied to the candidate [L1]

At fixed X and omega, take any smooth target variation Y with compact support. The existing split-jet construction [U1, U2] applies independently in each coordinate direction:

\[
\delta E_A^a=\delta K_A{}^a{}_bX^b+\delta w_AX^a,
\qquad
\delta w_A=\frac{X\cdot Y_A}{X^2},\qquad
Y_{\perp A}=Y_A-\delta w_AX,
\]
\[
\delta K_{Aab}=\frac{Y_{\perp Aa}X_b-X_aY_{\perp Ab}}{X^2}.
\]

Antisymmetry is explicit. Contracting with X gives the orthogonal target component, and the central term gives the parallel component. Thus the auxiliary variation realizes every variation of E. Smoothness and compact support are preserved on the non-null patch. This right inverse is an existing result; its application to the action above is the present test.

<!-- BILINGUAL-UNIT: c5-aux.stationarity -->
## Stationarity forces a critical zero coefficient [L1]

Let the inverse coframe be denoted by e with lower internal and upper coordinate indices. With u fixed, the complete variation is

\[
\delta\sqrt{|g|}=\sqrt{|g|}\,e_a{}^A\delta E_A^a,
\qquad
\delta S_{\rm aux}=\mathcal T\int d^5Z\sqrt{|g|}
\left[F e_a{}^A\delta E_A^a-V_{,a}\delta X^a\right].
\]

First set the field variation to zero. Surjectivity makes every coframe variation available, so stationarity requires F to vanish. Equivalently, choose an arbitrary smooth scalar epsilon with compact support and scale all the E columns:

\[
\delta E_A^a=\epsilon E_A^a,\qquad
\delta\sqrt{|g|}=4\epsilon\sqrt{|g|},\qquad
\delta S_{\rm aux}=4\mathcal T\int d^5Z\epsilon\sqrt{|g|}F
\quad\Longrightarrow\quad F=0.
\]

At a stationary configuration F vanishes throughout the patch. All induced coframe variations from varying X consequently have zero coefficient, including its derivative terms. The remaining field equation is the critical-point condition:

\[
\boxed{V(X)=2,\qquad V_{,a}(X)=0.}
\]

These conditions are also sufficient for local stationarity within this domain. If the potential has no non-null critical point at the required value, no nondegenerate stationary configuration exists here. If it has one, a constant field at that point can realize any full coframe with the fixed u through the auxiliary right inverse. This action then does not select its geometry. This is a statement about a vanishing scalar coefficient, not a vanishing or degenerate metric volume.

<!-- BILINGUAL-UNIT: c5-aux.quadratic -->
## Quadratic bulk action [L1]

Expand about any stationary background, allowing all independent variables to fluctuate. Write the field perturbation as xi and define the quadratic action as the coefficient of the squared expansion parameter. The constant and linear Taylor coefficients of F vanish, so every perturbation of the volume starts contributing only at higher order:

\[
X=X_0+\varepsilon\xi+O(\varepsilon^2),\qquad
F(X_0)=0,\quad F_{,a}(X_0)=0,
\]
\[
\boxed{S^{(2)}=-\frac{\mathcal T}{2}\int d^5Z\sqrt{|g_0|}
V_{,ab}(X_0)\xi^a\xi^b.}
\]

There are no derivatives of the perturbations in this quadratic bulk action. It provides no conventional wave or graviton kinetic operator on these backgrounds. This is not a complete Hamiltonian constraint analysis, a stability result, or a statement about every complex component of Theta. A null Hessian in some directions does not establish a healthy propagating mode.

<!-- BILINGUAL-UNIT: c5-aux.boundary -->
## Relation to the canonical action and next calculation

The obstruction uses independent algebraic K and w, fixed u, the equal metric/kinetic pairing and the absence of additional terms. A prescribed derivative-dependent composite jet does not allow these independent variations; its full chain rule and Hessian must be calculated separately. Substituting the Levi–Civita connection as a functional of E also changes the variational problem. Neither substitution has been analyzed by this theorem.

The existing split-jet Palatini candidate [U2] includes curvature. Its auxiliary variation transmits the Palatini coframe equation, which contains more than the scalar volume coefficient. The present result therefore does not contradict that conditional GR construction. The existing fixed/value-dependent connection audit [U3] already identifies related Hessian obstructions; no priority is claimed for those earlier results. The single-action registry [U4] remains authoritative.

The next useful test is an explicitly specified derivative-dependent composite jet with its full quadratic action and constraint quotient, or a derivation of the curvature term from the registered action family. The extra coordinate and auxiliary representability alone do not supply that missing dynamics. This note predicts neither the fine-structure constant nor energy quantization and does not establish string equivalence.

<!-- BILINGUAL-UNIT: c5-aux.verification -->
## Verification and limitations

`verify_auxiliary_action.py` records 22 exact checks in `auxiliary_action_results.json`: a generic SymPy right inverse, a coframe kinetic contraction, volume scaling and a quadratic coefficient, plus independently implemented rational right inverses, determinants and polynomial interpolation using Python Fraction. The rational channel is finite witness evidence; the generic analytic argument is given above. Tool versions, assumptions and exclusions are recorded in the JSON and `status.json`.

**LEAN-PENDING:** Lean and Lake executables were unavailable in the execution runtime. The local variational theorem has not been formalized in Lean. The checks do not verify a microscopic UBT action, all complex modes, a physical gauge quotient, stability or observations. English was the translation source; matching structure does not replace the human semantic-equivalence review required before merge.

<!-- BILINGUAL-UNIT: c5-aux.sources -->
## Sources within the repository

- [U1] [Existing split-jet right inverse](../../canonical/gr_closure/gap_10t_split_jet_right_inverse.tex).
- [U2] [Split-jet Palatini variational lift](../action_selection/split_jet_palatii_variational_lift.en.md).
- [U3] [Fixed/value-dependent connection action audit](../action_selection/biquaternionic_induced_gravity_boundary.en.md).
- [U4] [Single-action registry](../../canonical/ACTION.en.md).
