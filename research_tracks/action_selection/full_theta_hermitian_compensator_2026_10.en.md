<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: full-theta-hermitian-compensator -->
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

# Full single-Theta Hermitian compensator: regular curved sharp geometry and residual connection gate

**2026-10-31 · C_working · conditional kinematics, not chosen dynamics.** This audit continues merged PR #820's *norm-only real-carrier degeneracy* but does not postulate a new fundamental field or enlarge the canonical four-complex-component biquaternion. It REUSES the previous Hermitian/anti-Hermitian decomposition and common-connection obstruction from `physics_closure_carrier_2026_10.en.md` and the established exact relative-dilation and Clifford lifts. The new restricted contribution is a forced determinant-based relative center, a nondegenerate **curved** sharp-metric witness, and exact identification of the remaining reality, phase, and dynamics gates.

## Existing biquaternion components, not a second field [ASSUMED]

Use the faithful 2-by-2 complex matrix representation of ONE biquaternion Theta; ddagger is Hermitian conjugation. The two real four-dimensional sectors are already contained in the original eight real field components:

\[
\Theta=H+X\in\operatorname{Mat}_2(\mathbb C),\quad
H=\tfrac12(\Theta+\Theta^\ddagger)\in\operatorname{Herm}_2,\quad
X=\tfrac12(\Theta-\Theta^\ddagger)\in i\operatorname{Herm}_2.
\]

Supply a candidate two-sided *relative real* central jet, with a traceless Lorentz spin connection and no independent scalar. The full canonical metric is read from E with quaternion sharp, never by taking Re, a Hermitian Gram tensor or a projection:

\[
\Omega_\mu\in\mathfrak{sl}(2,\mathbb C),\quad
D_\mu\Theta=\partial_\mu\Theta+\Omega_\mu\Theta+
\Theta\Omega_\mu^\ddagger+w_\mu\Theta,\quad
E_\mu=s^{-1}D_\mu\Theta,\quad s=\sqrt{\mathcal N_0}>0.
\]

## Classical Lorentz reality forces the central trace [PROVED, conditional]

Demand that the **entire** defining tetrad lie on the canonical i-Hermitian classical Lorentz slice. Since ddagger commutes with this particular real central and two-sided Lorentz transport, its Hermitian part must vanish:

\[
C_\mu:=\partial_\mu H+\Omega_\mu H+
H\Omega_\mu^\ddagger+w_\mu H=0,
\qquad E_\mu\in i\operatorname{Herm}_2.
\]

On the invertible-H patch, contract with H inverse and take the trace. The tracelessness of Omega cancels its two trace terms, so the relative scalar connection is uniquely fixed by the existing field's Hermitian determinant:

\[
0=\operatorname{tr}(H^{-1}C_\mu)
=\partial_\mu\ln|\det H|+2w_\mu
\quad\Longrightarrow\quad
\boxed{w_\mu=-\tfrac12\partial_\mu\ln|\det H|.}
\]

**Trace is necessary, not sufficient.** On the positive-definite H patch the remaining traceless Hermitian matrix condition is precisely covariant constancy of normalized H:

\[
\widehat H=\frac{H}{\sqrt{\det H}},\qquad
C_\mu=0\iff
\partial_\mu\widehat H+\Omega_\mu\widehat H+
\widehat H\Omega_\mu^\ddagger=0
\qquad(\det H>0).
\]

That is a real restriction on allowed spin connections: a positive definite normalized H reduces connection holonomy locally to an SU(2) stabilizer. Nonzero SU(2) curvature remains possible, but this is not a proof of generic torsion-free Einstein metrics. The physical versus defining spin connection and any torsion must follow from a chosen action; identifying the same connection with torsion-free Levi-Civita reintroduces the known parallel-vector obstruction.

## Existing Theta directions generate the missing Weyl tangent [PROVED, scoped]

Under any local positive real rescaling of the ORIGINAL entire Theta, det H scales quadratically and the relative connection transforms with a minus derivative. Therefore the exact composite jet and its full sharp metric scale as follows:

\[
\Theta'=e^\varepsilon\Theta,\quad
H'=e^\varepsilon H,\quad
w'_\mu=w_\mu-\partial_\mu\varepsilon,\quad
D_\mu\Theta'=e^\varepsilon D_\mu\Theta,\quad
\delta E_\mu=\varepsilon E_\mu,\quad
\delta g_{\mu\nu}=2\varepsilon g_{\mu\nu}.
\]

This is a legitimate field variation tangent to the specified reality constraint: if C_mu=0 initially, its transformed value stays zero. The Weyl variation is NOT a gauge redundancy unless a future selected action makes it one; no extra physical field is introduced.

The determinant is unchanged under the declared unimodular Lorentz congruence; thus the candidate compensator is frame-covariant within that subgroup:

\[
\Theta\longmapsto S\Theta S^\ddagger,\qquad
S\in SL(2,\mathbb C),\qquad
\det(SHS^\ddagger)=\det H,\quad w'_\mu=w_\mu.
\]

## Exact nondegenerate curved witness [PROVED, scoped]

Take a regular future-timelike patch of the full biquaternion, with H the nonzero identity, X anti-Hermitian and SU(2)-valued noncommuting Lorentz spin coefficients. The derived w vanishes on this BACKGROUND, but its variation is nontrivial:

\[
H=I_2,\quad X=i(tI_2+x\sigma_1+y\sigma_2+z\sigma_3),\quad
\Omega_t=0,\quad\Omega_x=ia\sigma_1,\quad
\Omega_y=ib\sigma_2,\quad\Omega_z=0,\quad w=0.
\]

Because Omega is anti-Hermitian here, the Hermitian H is covariantly constant and the ENTIRE E lies in i-Herm without projecting away any component. In the canonical Lorentz basis (i I, -i sigma_k), the coframe is explicitly:

\[
e_\mu{}^a=
\begin{pmatrix}
1&0&0&0\\
0&-1&-2az&2ay\\
0&2bz&-1&-2bx\\
0&0&0&-1
\end{pmatrix},
\qquad
\det e=-1-4abz^2.
\]

The physical central-sharp metric has nonzero Riemann curvature, independently of the nonzero spin curvature. At the displayed origin and under the stated Riemann sign convention:

\[
F_{xy}=[\Omega_x,\Omega_y]=-2iab\sigma_3,\qquad
R^x{}_{yxy}(g)\big|_{x=y=z=0}=-12ab,\qquad
(a,b)=(1,2)\Rightarrow R^x{}_{yxy}=-24.
\]

The verifier checks each central-sharp bilinear and the ACTUAL full 4-by-4 block Clifford anticommutator, not merely a real-vector metric substitute:

\[
E_\mu^\sharp=\operatorname{tr}(E_\mu)I_2-E_\mu,\quad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}I_2,\quad
\Gamma_\mu=\begin{pmatrix}0&E_\mu\\E_\mu^\sharp&0\end{pmatrix},
\quad\{\Gamma_\mu,\Gamma_\nu\}=2g_{\mu\nu}I_4.
\]

The background is kinematically curved and has a regular tetrad near the origin; it is **not** shown to solve the full UBT Euler equations, nor to have torsion-free physical Levi-Civita spin transport. The SU(2) connection is a selected comparator and its relation to the microscopic physical connection remains OPEN.

## Normal-source pairing and remaining selection gates [OPEN]

For the non-null anti-Hermitian component X, the Weyl tangent is not invisible to the prior normal Euler source from PR #819. In the local curved witness one can choose an internal timelike X, hence the pairing is nonzero:

\[
\mathcal E^\mu{}_a=hV^\mu X_a,\quad
V^\mu=e^\mu{}_aX^a,\quad
\mathcal E^\mu{}_a\delta_\varepsilon e_\mu{}^a
=\varepsilon hX^aX_a\ne0
\quad(X^2\ne0,\ h\ne0).
\]

**Other exact restrictions:** the Hermitian determinant is not generally invariant under an independent central complex phase: such a phase mixes H with X. The tempting phase-invariant modulus of det Theta does NOT automatically preserve the required i-Hermitian classical jet; an exact counterexample is tested. Similarly, phi(H) is not holomorphic in arbitrary complex Theta, so compatibility with complex-time analyticity must be derived rather than assumed.

\[
\Theta\mapsto e^{i\chi}\Theta
\quad\Longrightarrow\quad
H\mapsto\tfrac12(e^{i\chi}\Theta+e^{-i\chi}\Theta^\ddagger);
\qquad
\det H\ \text{is not generally phase invariant}.
\]

**Action-level OPEN:** this is not yet a derivation of the physical relative center from one UBT action. The additional traceless normalized-H compatibility condition, the admissible full complex-time variation bundle, independent central phase symmetries, physical/jet connection distinction, torsion constraints, Cartan response, principal spectrum and energy positivity must be fixed and derived. The prior bare action no-go and conditional Palatini/GR branch still apply in their tested scopes.

**Verification:** `tests/test_full_theta_hermitian_relative_compensator.py`: **20/20 exact local SymPy tests passed** including full 2-by-2 Theta decomposition, required w trace, residual H constraint, local Lorentz transformations, curved coframe and Riemann, real sharp identities and full Clifford 4-by-4 lift, local scaling, normal-source pairing, phase and holomorphy caveats. Prior-work sources: `canonical/CANONICAL_DEFINITIONS.md:130-201`, `canonical/geometry/biquaternion_dirac_lift.tex:31-140`, `research_tracks/action_selection/physics_closure_carrier_2026_10.en.md:19-59`, `research_tracks/action_selection/exact_relative_weyl_norm_gate_2026_10.en.md:15-124`, `research_tracks/action_selection/flat_jet_torsion_action_2026_10.en.md:23-50`. No Lean proof or independent bilingual semantic approval is claimed.
