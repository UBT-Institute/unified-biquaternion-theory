<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: information-bloch-orbit.scope -->
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

# Information-first full Theta: the gravity-vertical Bloch ball and the local state-only obstruction

**2026-11-05 · C_working · conditional exact finite-matrix result; physical dynamics OPEN.** English is the translation source. The result concerns the existing positive-H graded gravity-only comparator and a CHOSEN observer readout, not all UBT completions.

<!-- BILINGUAL-UNIT: information-bloch-orbit.premise -->
## Premises: one full Theta and the gravity-only comparator

The merged graded derived-H Gaussian lift and representative quotient permit different full-Theta carriers with identical physical tetrads. The merged three-clock observer paper supplies a candidate positive local readout. Draft PR #832 exhibited one vertical rapidity direction; this study analyzes all spatial boost directions. This is not a new fundamental action or a physical state derivation.

<!-- BILINGUAL-UNIT: information-bloch-orbit.lift -->
## All boosts recover the same exact physical coframe [PROVED conditional]

Use the existing positive-H Gaussian right inverse on a common contractible Minkowski patch. The timelike hyperplane normal varies freely; the algebraic Lorentz tensor K exactly compensates. The Hermitian and anti-Hermitian pieces are coordinates of ONE original complex biquaternion. The defining spin is zero, and the independent physical connection omega stays fixed. The coframe equation holds on the entire patch, not just at the origin. All finite parameters give smooth invertible full-Theta fields, since their determinant away from the origin has nonzero imaginary part.

\[
\eta=\operatorname{diag}(-1,1,1,1),\quad
e_\mu{}^a=\delta_\mu{}^a,\quad
\mathbf b=(a,b,c)\in\mathbb R^3,\quad
C=\sqrt{1+|\mathbf b|^2},\quad
u_{\mathbf b}=Ct+ax+by+cz,
\]
\[
n^a=(-C,a,b,c),\quad n^an_a=-1,\quad
L=h_0=\sqrt{\mathcal N_0}=1,\quad
H=hI_2,\quad h=e^{u_{\mathbf b}},\quad
X=i(n^0I_2-n^j\sigma_j),\quad
\Theta_{\mathbf b}=H+X,
\]
\[
w_\mu=-\partial_\mu u_{\mathbf b},\quad
R_\mu{}^a=\delta_\mu{}^a+(\partial_\mu u_{\mathbf b})n^a,\quad
q=-1,\quad
K_{\mu ab}=\frac{R_{\mu a}n_b-n_aR_{\mu b}}q,
\]
\[
n_aR_\mu{}^a=0,\quad K_\mu{}^a{}_bn^b=R_\mu{}^a,\quad
\partial_\mu H+w_\mu H=0,\quad
\boxed{e_\mu{}^a[\Theta_{\mathbf b},K,\varpi=0]
=\delta_\mu{}^a\quad(\forall\mathbf b)}.
\]

<!-- BILINGUAL-UNIT: information-bloch-orbit.density -->
## One fixed observer has an explicit three-direction density [PROVED]

The geometric observer clock is N_obs=I in the common orthonormal coframe; it does not follow the auxiliary Gaussian normal. The exact full complex matrix and its Pauli product at the same spacetime origin yield the displayed density and a nonzero determinant. Changing the representative therefore changes measured probabilities even though the geometric data are fixed.

\[
N_{\rm obs}=I_2,\quad
\Theta_{\mathbf b}(0)=(1-iC)I_2-i\mathbf b\cdot\boldsymbol\sigma,\quad
\det\Theta_{\mathbf b}(0)=-2iC\ne0,
\]
\[
Q=\Theta_{\mathbf b}(0)\Theta_{\mathbf b}(0)^\dagger
=2C^2I_2+2C\,\mathbf b\cdot\boldsymbol\sigma,\quad
\boxed{\rho_{\mathbf b}=\frac Q{\operatorname{tr}Q}
=\tfrac12(I_2+\mathbf v\cdot\boldsymbol\sigma),\qquad
\mathbf v=\frac{\mathbf b}{\sqrt{1+|\mathbf b|^2}}}.
\]

<!-- BILINGUAL-UNIT: information-bloch-orbit.surjectivity -->
## Every full-rank qubit density appears on one gravity fiber [PROVED]

The boost parameters cover R3, and the explicit inverse maps the entire open Bloch ball to them. The differential has two transverse strictly positive eigenvalues and one longitudinal strictly positive eigenvalue. Thus the readout has rank three ALONG gravity-vertical directions on one fixed physical geometry; this is not an exceptional one-parameter trajectory. The pure-state boundary requires unbounded boosts, so it is excluded from the stated exact domain.

\[
\mathbf b\in\mathbb R^3\ \longleftrightarrow\
\mathbf v\in B^3,\quad
B^3=\{\mathbf v:|\mathbf v|<1\},\quad
\boxed{\mathbf b=\frac{\mathbf v}{\sqrt{1-|\mathbf v|^2}}},
\]
\[
\frac{\partial v_i}{\partial b_j}
=\frac{\delta_{ij}}C-\frac{b_ib_j}{C^3},\quad
\lambda_\parallel=C^{-3},\quad
\lambda_\perp=C^{-1},\quad
\operatorname{rank}_{\mathbb R}D_{\mathbf b}\mathbf v=3.
\]

<!-- BILINGUAL-UNIT: information-bloch-orbit.fisher -->
## Three independent Fisher directions can be purely gravity-vertical [PROVED]

For the previously merged tetrahedral informationally complete POVM, the classical Fisher matrix on the Bloch ball is strictly positive and equals I3/3 at the center. Its pullback to the boost parameters has rank three because the Jacobian is invertible. The geometric tetrad has not changed. Statistical identifiability therefore does not imply that a direction is a physical dynamical mode, carries positive canonical energy or helps select a microscopic Hamiltonian.

\[
E_\ell=\tfrac14(I_2+\mathbf u_\ell\cdot\boldsymbol\sigma),\quad
\mathbf u_\ell\in\frac1{\sqrt3}
\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\},
\]
\[
p_\ell=\tfrac14(1+\mathbf u_\ell\cdot\mathbf v),\qquad
F_{ij}^{(\mathbf v)}(\mathbf0)
=\sum_\ell\frac{\partial_i p_\ell\partial_jp_\ell}{p_\ell}
=\frac13\delta_{ij},\qquad
\boxed{F_{ij}^{(\mathbf b)}(\mathbf0)=\frac13\delta_{ij}}.
\]

<!-- BILINGUAL-UNIT: information-bloch-orbit.entropy -->
## Fixed-reference relative entropy varies inside the same geometry [PROVED]

Relative entropy to the maximally mixed reference has a unique minimum at the unboosted representative and is nonconstant throughout the accessible states. The reference is a chosen protocol datum. Extremizing this entropy can pick a representation but does not derive why it is physical or establish an admissible UBT action.

\[
D(\rho_{\mathbf v}\Vert I_2/2)
=\frac{1+r}{2}\log(1+r)
+\frac{1-r}{2}\log(1-r),\quad r=|\mathbf v|<1,
\]
\[
D(\rho_{\mathbf0}\Vert I_2/2)=0,\quad
D(\rho_{\mathbf v}\Vert I_2/2)>0\ (r>0),\quad
\lim_{r\uparrow1}D(\rho_{\mathbf v}\Vert I_2/2)=\log2.
\]

<!-- BILINGUAL-UNIT: information-bloch-orbit.no-go -->
## State-only local invariance implies a trivial observable [PROVED, restricted]

Let O=f(rho_N[Theta]) be a pointwise observable using ONLY this fixed-clock local density, with no derivatives, other charges, reference fields or boundary data. If O descends to the existing gravity-only quotient it must be constant whenever (e,omega) are fixed. Our one fixed-gravity fiber covers the entire open Bloch ball, so f must be constant on ALL strictly positive qubit densities. This rules out any NONCONSTANT state-only invariant on that restricted comparator, not information in gravity, geometric curvature observables or an information-sensitive single full-Theta action with a different physical quotient.

\[
\mathcal F_{\rm grav}:(\Theta,K,\varpi,\omega)\mapsto(e,\omega),\quad
\mathcal O=f(\rho_{N_{\rm obs}}[\Theta]),\quad
\mathcal O=\overline{\mathcal O}\circ\mathcal F_{\rm grav}
\Longrightarrow f(\rho_{\mathbf v})=\mathrm{constant}
\quad\forall\,\mathbf v\in B^3.
\]

<!-- BILINGUAL-UNIT: information-bloch-orbit.next -->
## Decisive information-first dynamics gate [OPEN]

Either derive observer algebras and instruments from genuine physical gauge-invariant geometry, curvature and causal edge charges; or derive an information-sensitive term from the SAME one-Theta microscopic action that changes the actual physical constraint structure, followed by its Dirac closure, causal and ghost tests. The second path cannot be replaced by minimizing an arbitrary reference entropy. The parity finding in draft PR #833 must also be checked on the actual physical quotient; its ideal tomography is not enough.

<!-- BILINGUAL-UNIT: information-bloch-orbit.verification -->
## Verification and precise exclusions

Nine SymPy tests executed locally cover full-Theta Pauli algebra, determinant, inverse Bloch map, original coframe and K reconstruction, nontrivial measurement states, map rank, tetrahedral Fisher and relative entropy. Analytical surjectivity follows from the explicit inverse, not numerics. No full microscopic UBT action, gauge interpretation beyond this comparator, physical detector, Lean formalization or independently certified semantic translation is claimed. Premises: research_tracks/action_selection/derived_h_graded_gaussian_lift_2026_11.en.md, derived_h_graded_representative_quotient_2026_11.en.md, research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md, canonical/ACTION.en.md; draft PR #832 was the earlier one-direction case.
