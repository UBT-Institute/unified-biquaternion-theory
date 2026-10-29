<!-- BILINGUAL-UNIT: flat-jet-action.scope -->
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

# Quadratic jet torsion with flat Lorentz transport and closed dilation

**2026-10-29; C_working; CONDITIONAL.** English is the translation source. This is an action-level test of a specified derivative candidate, beyond the previously excluded weighted-volume family. It derives the full composite equations within a restricted flat-jet configuration space. It does not select a microscopic UBT action. The restriction produces conformal scalar dynamics rather than the tensor sector of GR. The result is not a no-go for arbitrary two-sided jets, nonflat Lorentz jets, or unrestricted teleparallel gravity.

<!-- BILINGUAL-UNIT: flat-jet-action.branch -->
## Declared branch and connection conventions

Work locally with smooth fields on a simply connected patch, fixed positive global normalization, non-null Lorentz-real gravity carrier and a nondegenerate oriented tetrad. Variations have compact support and preserve the chart and the declared branch. The remaining complex-Theta and imaginary-time sectors are outside this comparison; their components are not deleted or counted as gauge. The original carrier retains all its Lorentz-vector components; the scalar below is a derived reduced coordinate.

Use the already studied real relative-dilation extension of the two-sided derivative. Its Lorentz-vector restriction and the additional comparison assumptions are

\[
s=\sqrt{\mathcal N_0}>0,\quad
A_J=\Omega_J+\tfrac12w\mathbf1,\quad
B_J=-\Omega_J^\ddagger-\tfrac12w\mathbf1,\quad
D_J\Theta=d\Theta+A_J\Theta-\Theta B_J,
\]
\[
E^a=s^{-1}(dX^a+\varpi^a{}_bX^b+wX^a),\quad
\Omega_J=\rho_*(\varpi),\quad X^2\ne0,\quad
R(\varpi)=0,\quad dw=0,\quad \eta=\operatorname{diag}(-1,1,1,1).
\]

Here the Lorentz-vector action is the declared representation on the classical gravity carrier, not a derivation of the fundamental component count. The flat Lorentz connection is a jet connection. It is not identified with the physical Levi–Civita connection reconstructed from the metric. The one-form is a real dilation, not an ordinary field phase or translation of imaginary time. Flatness and closedness are assumptions defining this comparison, not equations derived from UBT.

Local Lorentz covariance permits a gauge in which the flat jet connection vanishes. Closedness gives a local potential. Define

\[
\varpi=0,\quad w=df,\quad \chi=e^{-f}>0,\quad
Y^a=e^fX^a/s,\quad X^a=s\chi Y^a,
\]
\[
\boxed{E^a=\chi\,dY^a,\qquad
g_{\mu\nu}=\chi^2\eta_{ab}\partial_\mu Y^a\partial_\nu Y^b.}
\]

This metric is exactly the canonical central-sharp metric of that tetrad. No trace, projection or local metric normalization is introduced. Nondegeneracy makes the functions in the displayed coordinate map valid local coordinates. Thus every metric on this branch is conformally flat; its Weyl tensor vanishes at every order. This is stronger than testing one symmetric background.

<!-- BILINGUAL-UNIT: flat-jet-action.family -->
## Complete parity-even quadratic torsion family on the branch

Define jet torsion using the flat Lorentz jet connection and fix the following index conventions. It is not assumed to be physical spin torsion.

\[
T_J^a=dE^a+\varpi^a{}_b\wedge E^b=-w\wedge E^a,\quad
T^\rho{}_{\mu\nu}=\delta^\rho_\mu w_\nu-\delta^\rho_\nu w_\mu,\quad
t_\mu=T^\nu{}_{\mu\nu}=-3w_\mu,
\]
\[
I_1=T_{\rho\mu\nu}T^{\rho\mu\nu}=6w^2,\quad
I_2=T_{\rho\mu\nu}T^{\nu\mu\rho}=3w^2,\quad
I_3=t_\mu t^\mu=9w^2.
\]

Supply constant real coefficients and a positive normalization. No potential, matter term or further curvature term is included. All constant-coefficient parity-even quadratic contractions reduce to

\[
S_{\rm test}=\frac1{2\kappa}\int\sqrt{-g}\,(c_1I_1+c_2I_2+c_3I_3)\,d^4x,\quad
\kappa>0,\quad C=6c_1+3c_2+9c_3,\quad A=\frac C{2\kappa},
\]
\[
\boxed{S_{\rm test}=A\int d^4Y\,\eta^{ab}\partial_a\chi\partial_b\chi.}
\]

This is a genuinely derivative-dependent, non-volume functional, but it has only the conformal channel. The positive Einstein–Hilbert convention corresponds, up to a boundary term, to the following special combination:

\[
\mathbb T=\tfrac14I_1+\tfrac12I_2-I_3,\quad
R[g]=-\mathbb T-2\nabla^{\rm LC}_\mu t^\mu,\quad
(c_1,c_2,c_3)=(-\tfrac14,-\tfrac12,1),\quad C=6,\quad A=3/\kappa.
\]

The signs are tied to the stated torsion trace and curvature convention. The usual torsion/curvature boundary identity is standard; see [Krššák and collaborators](https://arxiv.org/pdf/1810.12932). Its unrestricted GR equivalence requires the appropriate unrestricted tetrad variations. It does not restore tensor directions absent from the present composite configuration space.

<!-- BILINGUAL-UNIT: flat-jet-action.variation -->
## Complete composite variation before coordinate fixing

The field-value transformation between the original carrier/dilation variables and the new variables is invertible on the positive chart. If the Euler densities before coordinate fixing are denoted by their field subscripts, the exact functional chain rule gives

\[
\mathcal E_{X a}=\frac{e^f}{s}\mathcal E_{Y a},\qquad
\mathcal E_f=Y^a\mathcal E_{Y a}-\chi\mathcal E_\chi.
\]

Therefore all original composite equations are equivalent to all transformed equations. This includes the tetrad, inverse metric, volume and induced jet-connection response. It does not substitute independent metric or independent torsion equations from a different variational problem.

Before imposing any coordinate gauge, diffeomorphism invariance supplies

\[
\mathcal E_{Y a}\partial_\mu Y^a+\mathcal E_\chi\partial_\mu\chi=0.
\]

The coordinate-map Jacobian is invertible, so the coordinate equations are consequences of the scalar equation. Only now choose the coordinate gauge. The scalar equation and the coordinate equations evaluated in that gauge are

\[
Y^a=x^a,\qquad
\mathcal E_\chi=-2A\Box_\eta\chi,\qquad
\mathcal E_{Y a}=2A(\partial_a\chi)\Box_\eta\chi.
\]

For nonzero kinetic coefficient the full branch equations are exactly the massless scalar wave equation. When the coefficient vanishes, the restricted density is identically zero and supplies no kinetic equation. These are variations within the flat-Lorentz/closed-dilation branch. Varying an unrestricted connection or one-form first and imposing the branch afterwards is a different problem and is not solved here.

<!-- BILINGUAL-UNIT: flat-jet-action.hamiltonian -->
## Reduced Hamiltonian and physical content

The four coordinate-map fields are removed by the regular diffeomorphism gauge; the conformal scalar remains. The displayed Noether identity accounts for the coordinate equations, so no independent Einstein lapse constraint can be borrowed to remove this scalar. In the coordinate gauge its canonical momentum and Hamiltonian density are

\[
p=-2A\dot\chi,\qquad
\mathcal H=-\frac{p^2}{4A}-A\lvert\nabla\chi\rvert^2,\qquad
\ddot\chi=\Delta\chi\quad(A\ne0).
\]

| Coefficient | Local propagating content | Reduced energy |
|---|---|---|
| Positive | One conformal scalar; no tensor modes | Negative kinetic direction |
| Negative | One conformal scalar; no tensor modes | Positive scalar quadratic energy |
| Zero | No kinetic equation in this restricted action | Identically zero density |

For positive coefficient, fix a positive scalar configuration and scale a nonzero smooth compactly supported momentum. Its energy tends to negative infinity quadratically. Initial data can stay on the regular chart for a sufficiently short evolution interval. This is an unbounded reduced Hamiltonian for this restricted model, not a statement about the asymptotic ADM energy of GR.

For the positive Einstein–Hilbert normalization the kinetic coefficient is positive, so this branch has that negative scalar direction. Changing the sign makes the scalar energy positive but still supplies no tensor sector. The characteristic cone is nevertheless the metric light cone for either nonzero sign. Causal propagation alone does not establish energy positivity.

This is not a ghost claim about unrestricted GR: its full metric constraints remove the conformal direction differently. Here the composite metric tangent contains only conformal changes and diffeomorphisms, and the transverse traceless projection is zero. The scalar geometry and vacuum equation have the familiar Einstein–Fokker/Nordström form; see [Deruelle](https://arxiv.org/pdf/1104.4608). No new scalar-gravity theory, derived matter coupling or observational UBT prediction is claimed.

<!-- BILINGUAL-UNIT: flat-jet-action.witness -->
## Curved on-shell witness that is not an Einstein vacuum

In local coordinate units choose the following smooth positive solution and its original single-carrier representative:

\[
\chi=1+\epsilon Y^0>0,\quad\epsilon\ne0,\quad
X^a=s\chi Y^a,\quad w=-d\ln\chi,\quad\varpi=0,\quad
\eta_{ab}Y^aY^b<0.
\]
\[
\Box_\eta\chi=0,\quad R[g]=0,\quad
R_{00}=\frac{3\epsilon^2}{\chi^2},\quad
R_{ij}=\frac{\epsilon^2}{\chi^2}\delta_{ij}.
\]

The carrier is non-null and the original tetrad is nondegenerate. All composite branch equations hold, yet the Ricci tensor is nonzero. The zero Ricci scalar would force a zero cosmological constant in any Einstein vacuum, contradicting that Ricci tensor. At the normalized point the finite contradiction is particularly explicit:

\[
\epsilon=1,\quad Y^0=1,\quad Y^i=0,\quad\chi=2,\quad
g_{00}=-4,\quad g_{11}=4,\quad R_{00}=\tfrac34,\quad R_{11}=\tfrac14.
\]

This is a solution of the declared torsion-action branch, not a proposed physical cosmology or a counterexample to Einstein's equations as derived from the unrestricted Einstein action.

<!-- BILINGUAL-UNIT: flat-jet-action.verification -->
## Verification and the surviving origin problem

`tools/verify_flat_jet_torsion_action.py` checks **41** exact identities, including the quadratic contractions, all **256** Weyl components, coordinate-momentum variations before gauge fixing, all coordinate Noether equations, the scalar Legendre transform and the curved witness. `tests/test_flat_jet_torsion_action.py` contains **42** cases.

A separate NumPy implementation reconstructs the original carrier, tetrad, torsion and metric from field jets in **24** seeded samples. Nonconstant boosts and rotations give a nonzero Lorentz connection with noncommuting components and exactly vanishing curvature. Variations change the carrier, dilation, coordinate map and connection jets together. Original and reduced density variations are compared with step **0.00001** and absolute tolerance **0.0000001**. The density tolerance is **0.0000000001**, while the coframe and flat-curvature tolerances are **0.00000000001**. The numerical first-variation test is pointwise in consistent jets; the functional argument is the analytic chain rule and Noether derivation above.

`formal/lean/UBT/GR/FlatJetTorsion.lean` encodes **7** finite algebraic cores: coframe cancellation, the Einstein-sign coefficient, the boundary cancellation, dimension-independent chain stationarity, Legendre energy, negative kinetic energy and the finite non-Einstein contradiction. `reports/flat_jet_torsion_action_2026_10_29.json` records source hashes, versions and compiled status. There is no local Lean runtime. The local geometric classification, continuum variational/Noether argument and full physical reduction remain LEAN-PENDING beyond those finite statements.

The [zero-connection theorem](exact_flat_connection_no_curvature.en.md) and [pure Lorentz integrability identity](cartans_theta_integrability.en.md) are prior results with their earlier scope. Real closed dilation enlarges their simplest flat case to conformally curved metrics, but not to generic GR. The [gravity-only parent reduction](splitjet_spatial_dirac_2026_10.en.md) has its own supplied functional and freely variable jet images; this test uses a different comparison functional and constrained jet space. This closes the tested constant-coefficient quadratic-torsion route on this exact branch. Nonflat Lorentz jets, nonclosed relative forms, other two-sided representations and genuinely derived quantum mechanisms remain separate problems. No new kinetic term is inserted into the canonical action. Its status remains `DEFINED_FAMILY_NOT_FINALIZED`.
