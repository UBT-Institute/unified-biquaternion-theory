<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: composite-normal-transport-adjoint -->
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

# Composite carrier Euler variation: nonzero normal adjoint transport mode

**2026-10-31 · C_working · exact restricted adjoint-kernel witness.** This continues the rank-9 normal-cokernel result merged in PR #817. It does NOT finalize the fundamental UBT action, disprove Palatini or GR, or add degrees of freedom. The existing full Clifford algebra and canonical **sharp** metric are retained; the component count of fundamental Theta is not fixed by this Lorentz-real subcase.

## Admissible composite variation [ASSUMED]

In a smooth regular non-null Lorentz-real patch, use a single internal real vector and an independently variable metric-compatible Lorentz connection as a restricted comparator. The real scale s is fixed:

\[
s=\sqrt{\mathcal N_0}>0,\quad X^2\ne0,\qquad
e_\mu{}^a=s^{-1}D_\mu^\omega X^a,\quad
D_\mu^\omega X^a=\partial_\mu X^a+\omega_\mu{}^a{}_bX^b.
\]

Let S0 be ANY independently differentiable geometric source functional, with its fixed-tetrad omega variation C_omega (including integrations by parts already performed). Denote the tetrad Euler density P:

\[
S_{\mathrm{pull}}[X,\omega]=S_0[e(X,\omega),\omega],\qquad
\delta S_0=\int d^4x\,
\bigl(P^\mu{}_a\,\delta e_\mu{}^a+C_\omega(\delta\omega)\bigr).
\]

The exact composite chain rule for compactly supported variations gives:

\[
\delta e_\mu{}^a=s^{-1}\bigl(
D_\mu^\omega\delta X^a+\delta\omega_\mu{}^a{}_bX^b\bigr),
\quad
\mathcal E_{X,a}=-s^{-1}D_\mu^\omega P^\mu{}_a.
\]

The omega equation MUST also contain the induced tetrad response, rather than silently reusing the independent Cartan equation:

\[
\mathcal E_{\omega}(\delta\omega)
=C_\omega(\delta\omega)
+s^{-1}P^\mu{}_a\delta\omega_\mu{}^a{}_bX^b.
\]

Here D_mu on P denotes the dual internal Lorentz connection and ordinary divergence of the spacetime vector **density**. This identity holds off shell; if omega itself is a derived functional of X, additional chain-rule contributions must be included.

## Conditional normal transport theorem [PROVED, restricted]

**Assume C_omega=0 on the tested branch.** Then all 24 antisymmetric connection variations enforce only that P is pointwise parallel to X in its internal index. The X Euler equation, together with regular invertibility of e, further implies:

\[
C_\omega=0\quad\Longrightarrow\quad
P^\mu{}_a=f^\mu X_a,\qquad
V^\mu e_\mu{}^a=X^a,\qquad
P^\mu{}_a=\lambda V^\mu X_a.
\]

To prove the last step, expand D_mu(f^mu X_a) and use D_mu X_a=s e_{mu a}; the part orthogonal to X forces f^mu=lambda V^mu. The remaining normal part is a scalar transport equation:

\[
D_\mu^\omega(\lambda V^\mu X_a)=
\bigl[\partial_\mu(\lambda V^\mu)+s\lambda\bigr]X_a=0,
\quad
V^\mu\partial_\mu\lambda+
(\partial_\mu V^\mu+s)\lambda=0.
\]

A transport equation does **not** generally imply lambda=0. It supplies initial data along the V flow. An independent requirement of zero lambda on a transverse initial hypersurface would force its vanishing locally by transport uniqueness, but such a boundary condition has not been derived from UBT.

## Nonzero exact smooth formal-adjoint witness [PROVED, restricted]

Choose the open timelike patch with t>0 and t squared greater than the spatial radius squared. At the reference configuration:

\[
s=1,\quad\omega=0,\quad
X^a=x^a=(t,x,y,z),\quad
e_\mu{}^a=\delta_\mu{}^a,\quad V^\mu=x^\mu,\quad
\lambda=t^{-5}.
\]

The tetrad Euler covector is nonzero, but its Lorentz contraction and carrier divergence vanish identically:

\[
P^\mu{}_a=t^{-5}x^\mu\eta_{ab}x^b\not\equiv0,\quad
\partial_\mu P^\mu{}_a
=\bigl(x^\mu\partial_\mu\lambda+5\lambda\bigr)X_a=0,
\quad P^\mu{}_a\delta\omega_\mu{}^a{}_bX^b=0.
\]

This is a nonzero kernel element of the **formal adjoint** of the differential map from admissible compactly supported (delta X, delta omega) to delta e. It also comes from a **symmetric metric** Euler source, not merely an antisymmetric tetrad source:

\[
\mathcal G^{\mu\nu}=\tfrac12\lambda V^\mu V^\nu,\qquad
P^\mu{}_a=2\mathcal G^{\mu\nu}e_{\nu a},\qquad
\mathcal G^{\mu\nu}\not\equiv0.
\]

For example, an externally sourced linear probe S_probe with fixed P0 has this source as its ambient tetrad variation, yet the pulled-back (X,omega) equations are stationary on the reference configuration. This is a **deliberately non-fundamental, external-source diagnostic**, not a Lorentz/diffeomorphism-invariant UBT model or a matter action:

\[
S_{\mathrm{probe}}[e]=\int d^4x\,
P_0^\mu{}_a(x)\bigl(e_\mu{}^a-\delta_\mu{}^a\bigr),
\quad P_0^\mu{}_a=t^{-5}x^\mu\eta_{ab}x^b.
\]

A rational constant non-orthonormal frame and a second scale-invariant lambda profile pass the same adjoint-kernel conditions. The witness is local and smooth on its stated patch, though it need not admit continuation through t=0. No physical stress-energy is inferred.

## Relative dilation and the exact open gate [PROVED, conditional]

The already known *relative*, independently variable real dilation w detects the normal source algebraically whenever X is non-null:

\[
\delta_w e_\mu{}^a=s^{-1}\delta w_\mu X^a,\quad
P^\mu{}_a\delta_w e_\mu{}^a
=s^{-1}\lambda V^\mu X^2\,\delta w_\mu.
\]

This is NOT an unconditional repair: a **common** central two-sided term cancels, w must be derived as an admissible independent/composite variation from one single-Theta action, and dynamical connection/matter contributions may change the Euler equations. The known split-jet Palatini variational equivalence includes a freely varied w and therefore does not contradict this restricted formal-adjoint counterexample.

## Research decision [OPEN]

The next useful input is the **actual** microscopic S_UBT[Theta]: write its variation bundle and connection closure explicitly, compute C_omega and all induced terms, and test whether the transported normal amplitude lambda is fixed, gauge, boundary data or an extra physical mode after Dirac constraint reduction. A nonzero kernel of an unconstrained diagnostic source map does NOT decide that. Keep the canonical complex Theta carrier, sharp metric, full Clifford grades and action status unchanged.

**Reproduce:** `python -m unittest discover -s tests -p 'test_composite_normal_transport_adjoint.py' -v` — 11/11 exact local SymPy cases passed. Prior sources: `canonical/geometry/connection.tex:13-83`, `research_tracks/action_selection/composite_lorentz_variation_rank_2026_10.en.md:18-132` (PR #817), `research_tracks/action_selection/split_jet_palatii_variational_lift.en.md:18-199`, `research_tracks/action_selection/physics_closure_dilation_2026_10.en.md:18-54`, `research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md:18-85`. Lean and independent translation semantics remain unverified.
