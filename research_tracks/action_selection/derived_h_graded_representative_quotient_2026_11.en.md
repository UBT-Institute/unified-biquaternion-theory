<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: derived-h-quotient.scope -->
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

# Derived-H representatives: finite differential coordinates and the local covariant quotient

**2026-11-02 · C_working · PROVED under declared comparator assumptions.** English is the translation source. We classify every regular representative in the compressed positive-H graded chart, its complete local vertical symmetry and the additional defining-spin split redundancy. With explicit regularity and boundary assumptions this gives a local covariant reduced-solution-space equivalence to the supplied geometric comparator. It is not a microscopic action selection or a canonical Dirac analysis.

<!-- BILINGUAL-UNIT: derived-h-quotient.reuse -->
## Premises and scope

Use smooth fields and solution germs on a small coordinate slab about an internal spacelike Cauchy slice. Fix the Lorentz coframe orientation, the non-null sign and, in the timelike case, a normal time orientation. Require uniform nonzero margins on the compact spatial region used for variations. All fields and the selected little-group frame stay in one smooth local chart. The central-sharp tetrad and the real-linear graded comparator are those of [U1–U2]; the fundamental field remains the same full complex biquaternion. The previous Gaussian lift, stationary-transmission theorem and on-shell current identity [U2] are reused, not claimed anew. The free-central-form results [U3–U4] allow more carrier shifts and cannot simply be copied here.

\[
H=hI_2,\quad h>0,\quad Y=X/h,\quad
A_\mu=\varpi_\mu+K_\mu,\quad A_\mu\in\mathfrak{so}(1,3),\quad
e_\mu{}^a=\frac h s(\partial_\mu Y^a+A_\mu{}^a{}_bY^b),\quad s>0.
\]
\[
\det e\ne0,\quad r=Y^aY_a\ne0,\quad
g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab},\qquad
\eta=\operatorname{diag}(-1,1,1,1).
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.split -->
## The defining-spin split must be quotiented explicitly

In the chosen normalized-H frame the residual defining spin is an arbitrary su(2) one-form, represented by spatial Lorentz rotations. Its curvature need not vanish. The gravity comparator depends on it and K only through A. Thus the following off-shell split transformations preserve the entire coframe and action. This is an action-invisible change of the split, not a claim that a curved defining connection can be set to zero by Lorentz gauge. We first quotient this affine redundancy; the complete classification below concerns the compressed variables. Restoring the original split adds one arbitrary su(2) one-form, with the displayed transformations. If another action term depends separately on defining-spin curvature, this premise and this quotient cease to apply.

\[
\varpi_\mu\mapsto\varpi_\mu+W_\mu,\qquad
K_\mu\mapsto K_\mu-W_\mu,\qquad W_\mu\in\mathfrak{su}(2),\qquad
\delta A_\mu=0.
\]
\[
4\dim\mathfrak{su}(2)=12.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.necessity -->
## Necessary radial identity [PROVED]

Metric compatibility of A and the full defining coframe relation give the first identity below. Invertibility of the coframe then gives its norm and inversion. Thus dr is automatically non-null and has the same norm sign as r. The positive sign of h removes a square-root ambiguity; the normal orientation is retained in dr. These are identities of actual smooth fields, not equations imposed on unrelated independent jets.

\[
\partial_\mu r=2Y_a(D^A_\mu Y)^a=\frac{2s}{h}Y_ae_\mu{}^a,\qquad
k:=g^{\mu\nu}\partial_\mu r\,\partial_\nu r=\frac{4s^2r}{h^2}\ne0.
\]
\[
\boxed{h=2s\sqrt{\frac r k}>0,\qquad
Y^a=\frac h{2s}e^{a\mu}\partial_\mu r.}
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.sufficiency -->
## Complete finite differential parametrization [PROVED]

Conversely, prescribe any regular coframe e and any smooth r for which r and k are nonzero with the same sign and the chosen orientation. Construct h and Y by the boxed formula. Their norm is exactly r. Differentiating that identity makes T orthogonal to Y, so the explicit Lorentz-algebra map below solves the entire coframe relation. Every possible A differs from that particular solution by exactly one stabilizer-valued one-form Z. This proves both existence and completeness, without introducing a new physical scalar or connection: r is the old composite norm, and Z consists of components of the old A.

\[
Y^2=\frac{h^2}{4s^2}k=r,\qquad
T_\mu{}^a=\frac s h e_\mu{}^a-\partial_\mu Y^a,\qquad
Y_aT_\mu{}^a=\frac s h Y_ae_\mu{}^a-\tfrac12\partial_\mu r=0.
\]
\[
J_Y(T)_{ab}:=\frac{T_aY_b-Y_aT_b}{r},\qquad
J_Y(T)Y=T\quad(Y\cdot T=0).
\]
\[
\boxed{A_\mu=J_Y(T_\mu)+Z_\mu,\qquad
Z_\mu\in\mathfrak{so}(1,3),\quad Z_\mu Y=0.}
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.coordinates -->
## Fixed stabilizer coordinates and the exact inverse

Choose a smooth local Lorentz frame L(Y) carrying a fixed unit vector of the selected sign and orientation to the normalized Y. The stabilizer is so(3) in the timelike case and so(1,2) in the spacelike case. Expand z in a fixed basis of that algebra. The displayed inverse is algebraic in the original A and Y because T equals A Y on the defining relation. The map to the new coordinates has finite differential order, and its explicit inverse uses at most first coframe derivatives and second r derivatives. Compositions are the identity on holonomic smooth sections and their prolonged tangent variations; no inverse differential operator or boundary-value solver is used.

\[
\mathcal L(Y)n_\varepsilon=\frac{Y}{\sqrt{|r|}},\qquad
Z_\mu=\mathcal L(Y)z_\mu\mathcal L(Y)^{-1},\qquad z_\mu n_\varepsilon=0.
\]
\[
Z_\mu=A_\mu-J_Y(A_\mu Y),\qquad
z_\mu=\mathcal L(Y)^{-1}Z_\mu\mathcal L(Y).
\]
\[
(h,Y,A)\longleftrightarrow(e,r,z),\qquad
\operatorname{ord}\bigl((h,Y,A)\mapsto(e,r,z)\bigr)\le1,\quad
\operatorname{ord}\bigl((e,r,z)\mapsto(h,Y,A)\bigr)\le2.
\]
\[
16+1+4\cdot3=29=1+4+4\cdot6.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.temporal -->
## A non-Gaussian local representative [PROVED]

The classification gives a simpler existence corollary than the previous Gaussian construction. Around any Lorentzian point choose a local temporal coordinate with the indicated inverse-metric sign; a constant timelike covector at the point supplies such a coordinate after shrinking the patch. The displayed r then has the required sign and non-null derivative. Reconstruction produces a local representative by finite derivatives of e in that existing coordinate chart. No Gaussian geodesic/PDE construction is needed. The positive constants only label representatives. This coordinate is a freely chosen local chart, not a physically selected preferred clock or an extra field.

\[
g^{tt}<0,\qquad r=-r_0e^{2t/L},\quad r_0>0,\quad L>0,\qquad
k=\frac{4r^2}{L^2}g^{tt}<0,\qquad
h^2=\frac{s^2L^2}{r\,g^{tt}}>0.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.finite -->
## Complete finite vertical symmetries [PROVED]

At fixed entire e and physical omega replace r and z by any other admissible labels in the same local chart and apply the inverse construction. This keeps the composed action exactly invariant off shell. Every two compressed representatives of that same coframe differ in this way. These replacements form a local gauge groupoid: composition depends on the final labels, not on the intermediate representative. On a small convex label neighborhood all replacements are generated by the infinitesimal shifts below. They commute for field-independent label parameters and are irreducible in this chart. Restoring the defining-spin split adds the independent split transformations above. The count is of arbitrary functions in a redundant description, not a count of physical degrees of freedom or Hamiltonian constraints.

\[
\delta e=\delta\omega=0,\qquad
\delta r=\sigma,\qquad \delta z_\mu=\zeta_\mu,\qquad
[\delta_{(\sigma,\zeta)},\delta_{(\widetilde\sigma,\widetilde\zeta)}]=0.
\]
\[
1+4\cdot3=13,\qquad 13+12=25.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.infinitesimal -->
## All vertical variations in the original compressed variables

Differentiating the inverse at fixed e gives the complete formula below. The image vector M is orthogonal to Y by differentiation of the radial identity. Conversely, the coframe variation and the norm identity force every vertical variation to have this form. Zero source variation gives zero sigma and zero stabilizer-label variation, establishing irreducibility. In covariant stabilizer notation Z is not an independent fixed tensor when Y changes: its differentiated constraint must be retained. Commutation is asserted in fixed label coordinates, not for an incorrectly frozen field-dependent stabilizer basis. An arbitrary transverse carrier shift allowed by the older free-central-form model violates this radial identity here.

\[
b_\sigma:=\frac{\delta h}{h}
=\frac12\left(\frac{\sigma}{r}
-\frac{2g^{\mu\nu}\partial_\mu r\,\partial_\nu\sigma}{k}\right),\qquad
\delta Y^a=b_\sigma Y^a+\frac h{2s}e^{a\mu}\partial_\mu\sigma.
\]
\[
M_\mu=-D^A_\mu\delta Y-b_\sigma D^A_\mu Y,\qquad
Y\cdot M_\mu=0,\qquad
\delta A_\mu=J_Y(M_\mu)+\Xi_\mu,\quad\Xi_\mu Y=0.
\]
\[
\delta Z_\mu\,Y+Z_\mu\,\delta Y=0,\qquad
\delta e_\mu=\frac h s
\left(b_\sigma D^A_\mu Y+D^A_\mu\delta Y+\delta A_\mu Y\right)=0.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.derivatives -->
## Parameter derivatives, support and initial data

The original h and Y variations involve first derivatives of sigma, and the A variation generally contains second derivatives of sigma. Stabilizer-label and split parameters are algebraic. Thus these symmetries are local finite-derivative transformations, not point transformations on a fixed-time canonical phase space. Their prolongations preserve commutation of the label shifts. A Hamiltonian analysis must separately include parameter-derivative chains, momentum redefinitions and boundary terms; no primary/secondary constraint count is inferred.

<!-- BILINGUAL-UNIT: derived-h-quotient.boundary -->
## Spatial support and a concrete Cauchy-surface obstruction

Use compactly supported spacetime test variations only to derive the off-shell Euler equations. For the covariant quotient use solution germs about an internal Cauchy slice Sigma and a common class of spacelike-compact Jacobi fields, or a sufficiently small time slab with variations vanishing in a fixed spatial boundary collar. Physical Cauchy data on Sigma are free. Neither physical solution tangents nor vertical parameters are required to vanish near Sigma or be compactly supported in time. Integrate the presymplectic current over Sigma, retaining the chosen spatial boundary/corner convention.

Fix only the spatial representative boundary sector and a small label neighborhood whose interpolation stays admissible. Finite differentiation does not enlarge support. Hence both vertical label transformations in this spatial-support class and base Jacobi fields lifted with labels fixed remain admissible; no nonlocal continuation in time is inserted. In particular, the representative labels may vary on Sigma.

If a different problem allows representative labels to differ on an initial surface but restricts gauge transformations to the identity near that surface, forgetting those labels need not be injective. The flat-coframe family below has different initial h for different rates. Such transformations cannot connect it under that different restriction. This is an excluded boundary prescription, not a restriction imposed on physical perturbations in the present theorem. The rate change can also be localized in the spatial interior after shrinking the time slab.

\[
a>0,\quad e_\mu{}^b=\delta_\mu{}^b,\quad
r_a=-e^{at},\quad h_a=\frac{2s}{a}e^{-at/2},\quad
Y_a=e^{at/2}n_-,\quad n_-=(1,0,0,0),
\]
\[
A_{a,0}=0,\qquad A_{a,i}=\frac a2 B_{0i},\qquad
B_{0i}n_-=e_i,\qquad h_a(0)=\frac{2s}{a}.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.gauge -->
## Lifting geometric Lorentz and diffeomorphism gauge

The normalized-H frame leaves only rotations as manifest congruence transformations. A base boost or diffeomorphism must therefore not be identified with a naive transformation that freezes all original source components in that frame. An explicit local lift is obtained by transforming the base variables, keeping the representative labels fixed, and applying the finite differential inverse. It intertwines the base map and preserves the pullback action whenever the base action is invariant. Infinitesimal base transformations in the same spatial-support class have lifts in that class. This chosen lift can include a compensating representative change; it is not asserted to be the original bare congruence or a canonical transformation. Locally its compositions follow the base transformations wherever the chart remains admissible.

\[
F\bigl(R(e,r,z),\omega\bigr)=(e,\omega),\qquad
\widetilde g\bigl(R(e,r,z),\omega\bigr)
:=\bigl(R(g\cdot e,r,z),\,g\cdot\omega\bigr),\qquad
F\circ\widetilde g=g\circ F.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.quotient -->
## Local covariant reduced-space theorem [PROVED, conditional]

Assume the differentiable local-Lorentz-invariant gravity-only base action and the stationary-transmission hypotheses of [U2], including all its independent physical connection variations. On solution germs about Sigma choose the common spacelike-compact Jacobi class or fixed spatial collar described above. Assume the base covariant presymplectic quotient is regular and smooth for this class and boundary convention. Do not fix physical Cauchy data or suppress vertical parameters at Sigma. There is no extra direct dependence on Y, h, A or the defining-spin split. The earlier stationary theorem identifies source solutions with the inverse image of base solutions. The new finite coordinates provide complete connected local inverse-image orbits and lift every admissible base Jacobi field by fixing labels. The forms below are integrals of the actual variational currents over Sigma.

\[
\mathrm{Sol}_{\rm pull}=F^{-1}(\mathrm{Sol}_0),\qquad
\left.\Omega_{\rm pull}\right|_{\mathrm{Sol}_{\rm pull}}=F^*\left(\left.\Omega_0\right|_{\mathrm{Sol}_0}\right).
\qquad \Omega=\int_\Sigma\omega.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.kernel -->
## Kernel equality and the reduced bijection

The on-shell current identity [U2] gives the displayed pullback form after restricting to solutions and linearized solutions. Surjectivity of the tangent map now proves equality of kernels: if a source vector pairs to zero with every source tangent, lift each base tangent to show that its image pairs to zero with every base tangent; the converse follows directly from pullback. The vertical directions are exactly the representative and split orbits classified above. Quotienting them first gives the base solution neighborhood; then quotienting the lifted regular base null foliation gives a local bijection preserving the reduced covariant symplectic form. This is a conditional local covariant equivalence proved from completeness, tangent lifting and the actual variational current together. It does not follow from finite-jet inversion alone.

\[
\ker\Omega_{\rm pull}=(dF)^{-1}(\ker\Omega_0),\qquad
\ker dF\subseteq\ker\Omega_{\rm pull},
\]
\[
\mathrm{Sol}_{\rm pull}/\ker\Omega_{\rm pull}\ \simeq_{\rm local}\ \mathrm{Sol}_0/\ker\Omega_0.
\]

<!-- BILINGUAL-UNIT: derived-h-quotient.verification -->
## Verification and open obligations

Thirteen exact SymPy tests cover generic coframe and radial jets of both signs, both inverse directions, the algebraic stabilizer projection, all fixed little-group labels, the complete vertical variation, moving-stabilizer and old-free-shift countercontrols, second parameter derivatives, the finite kernel core, the boundary family, the non-Gaussian temporal lift and the curved defining-spin split. The independent NumPy checker uses 96 original source fields per sign, reconstructs them and performs finite radial-label replacements. With finite-difference step 0.00001 and tolerance 0.0000002, the largest coframe error is below 0.00000000007. These finite checks do not prove the continuum quotient assumptions.

<!-- BILINGUAL-UNIT: derived-h-quotient.status -->
## Status boundaries

**LEAN-PENDING:** Lean and Lake are unavailable, and no checked continuum formalization is supplied. The source-bound report records actual checks and limitations. Independent semantic approval remains required before merge. The result holds only for the supplied gravity-only positive-H graded comparator with the declared split redundancy, sign/orientation chart and spatial-support/Cauchy-germ prescription. It proves no global equivalence, null-locus continuation, full fixed-time Dirac constraint count, microscopic measure, selected action, healthy extra Theta/psi sector, strict-holomorphic compatibility or left-U(1) interpretation. The full action remains DEFINED_FAMILY_NOT_FINALIZED and physical GR recovery remains CONDITIONAL.

<!-- BILINGUAL-UNIT: derived-h-quotient.sources -->
## Reused sources and verification artifacts

Only the scoped mathematical implications above are claimed. No author attestation, historical priority or independent external scientific review is supplied.

- [U1] [Existing graded comparator](full_theta_reallinear_graded_jet_2026_10.en.md).
- [U2] [Derived-H stationary transmission and actual current](derived_h_graded_gaussian_lift_2026_11.en.md).
- [U3] [Older free-central-form finite quotient](mm_finite_splitjet_lift.en.md).
- [U4] [Older free-central-form Dirac reduction](splitjet_spatial_dirac_2026_10.en.md).
- [V1] [Exact finite-jet checks](../../tests/test_derived_h_representative_quotient.py).
- [V2] [Independent source-field controls](../../tools/verify_derived_h_representative_quotient_numeric.py).
- [V3] [Verification record](../../reports/derived_h_representative_quotient_2026_11_02.json).
