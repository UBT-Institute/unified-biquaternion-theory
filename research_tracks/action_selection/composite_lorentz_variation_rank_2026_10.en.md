<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: composite-connection-variation-rank -->
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

# Composite Lorentz connection: exact metric-variation cokernel and Clifford joint response

**2026-10-31 · C_working · restricted pointwise theorem.** This audit builds on the previously established canonical composite-jet geometry, the July exact-gradient no-go, the October split-jet surjectivity and real-dilation chain variation, and the full Clifford 24-to-8 contraction merged in PR #816. It is NOT a new physical action, proof of an Einstein equation or count of propagating modes. The fundamental field component count remains provisional.

## Restricted physical-Lorentz-only response [ASSUMED]

On a regular Lorentz-real patch, hold the original internal vector X fixed when varying ONLY an independent antisymmetric Lorentz connection. The chosen tetrad formula is a restricted connection-variation comparator, not a general replacement for the UBT two-sided derivative:

\[
s=\sqrt{\mathcal N_0}>0,\quad X^2\ne0,\quad
e_\mu{}^a=s^{-1}(\partial_\mu X^a+
\omega_\mu{}^a{}_bX^b),\quad
\omega_{\mu ab}=-\omega_{\mu ba}.
\]

Its linearized tetrad response is orthogonal to X for each spacetime index:

\[
\delta_\omega e_\mu{}^a=s^{-1}
\eta^{ac}\delta\omega_{\mu cb}X^b,\qquad
X_a\delta_\omega e_\mu{}^a=0.
\]

The stabilizer of a non-null internal Lorentz vector has dimension 3, independently for each spacetime index. Consequently the exact 24-by-16 real Jacobian has image X-orthogonal and rank 12:

\[
J_X:\mathbb R^{24}\to\mathbb R^{16},\quad
\operatorname{rank}J_X=12,\quad
\ker J_X\simeq\mathbb R^{12},\quad
\operatorname{im}J_X=\{\delta e:X_a\delta e_\mu{}^a=0\}.
\]

## The missing metric-normal covector [PROVED, restricted]

Push this response through the **canonical** metric differential, not through a dagger Gram substitute:

\[
M_X:=D_eg\circ J_X:\mathbb R^{24}\to
\operatorname{Sym}^2T^*M,\quad
g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab}.
\]

Let the regular tetrad have inverse e^mu_a and define the spacetime vector V corresponding to X. The normal double contraction vanishes identically for every allowed Lorentz-only variation:

\[
V^\mu=e^\mu{}_aX^a,\qquad
V^\mu V^\nu\delta_\omega g_{\mu\nu}
=2V^\mu X_a\delta_\omega e_\mu{}^a=0,
\quad \operatorname{rank}M_X=9.
\]

This is the ENTIRE cokernel, not just one candidate: a symmetric test tensor annihilating the metric image must obey S^{mu nu}e_{nu a}=lambda^mu X_a. Invertibility of e gives S^{mu nu}=lambda^mu V^nu. Symmetry of S then forces lambda proportional to V, proving the cokernel has dimension one. Thus 24 connection directions vary only 9 of the 10 symmetric metric components. The proof is independent of the coordinate frame and does not assume X is aligned with time.

## Actual chain rule for a supplied geometric action [PROVED, conditional]

Let S0[e,omega] be ANY independently differentiable geometric comparator with its full fixed-tetrad connection derivative C, including curvature integration by parts. Pulling e back via the restricted composite relation gives exactly:

\[
\delta S_0=\int\!\left(
\mathcal E^\mu{}_a\,\delta e_\mu{}^a+
\mathcal C^{\mu ab}\delta\omega_{\mu ab}\right),
\qquad
\delta_\omega S_0[e(X,\omega),\omega]
=\int\!(\mathcal C+J_X^*\mathcal E)\cdot\delta\omega.
\]

Exact differentiation of a linear local action with independent tetrad Euler sources and fixed-tetrad connection sources verifies the full composite chain rule for all 24 Lorentz directions. This finite source test does not vary an actual curved action. A common central one-form cancels between the two sides; a relative center does not.

A nonzero normal tetrad Euler covector can lie in ker J_X^*:

\[
\mathcal E^\mu{}_a=V^\mu X_a
\ne0\quad\Longrightarrow\quad J_X^*\mathcal E=0.
\]

Therefore an equation obtained ONLY by varying the physical Lorentz connection does not independently supply the missing normal/lapse tetrad equation. **This is NOT a no-go for the full Theta system**: field-value, field-derivative and permitted relative-jet variations may contribute. The Cartan equation and the tetrad equation also mix through the displayed chain rule; they must not be silently equated with their independently varied counterparts.

## Relative real dilation repairs rank, not dynamics [PROVED, conditional]

As in the older split-jet/dilation comparator, if a **genuinely permitted relative** scalar connection one-form w is independently available, its jet variation supplies the missing normal X direction:

\[
\delta_w e_\mu{}^a=s^{-1}\delta w_\mu X^a,\quad
X_a\delta_we_\mu{}^a=s^{-1}X^2\delta w_\mu,\quad
\operatorname{rank}D_eg\circ(J_X\oplus J_w)=10.
\]

The metric response is then surjective, but this is an algebraic statement about a chosen variation space. A *common central* term cancelling between A and B cannot do this. Neither scalar w nor its free variation has been dynamically selected by UBT, and its relation to physical connection/torsion must still be justified.

## Joint Clifford projection: a further gauge-fixed diagnostic [PROVED, scoped]

In the same frozen orthonormal Lorentz-frame comparator, the existing PR #816 minimal Clifford contraction has rank 8 over the 24 real spin-connection coefficients:

\[
L_{\rm Clifford}:
\mathbb R^{24}\to\operatorname{Mat}_4(\mathbb C),
\quad \delta\omega\mapsto
\gamma^\mu\delta\Omega_\mu,\quad
\operatorname{rank}_{\mathbb R}L_{\rm Clifford}=8.
\]

An exact combined matrix calculation yields the following rank and nullity at the stated timelike X/e reference point:

\[
\operatorname{rank}_{\mathbb R}
\begin{pmatrix}M_X\\L_{\rm Clifford}\end{pmatrix}
=16,\quad
\dim_{\mathbb R}\ker=8
\qquad(X^a=(2,0,0,0),\,e_\mu{}^a=\delta_\mu{}^a).
\]

**Crucial limitation:** this combines a composite metric differential with the *fixed-gamma lower-order connection contraction*. The FULL variation of the Dirac operator also contains delta Gamma_mu(E), module connection compatibility, gauge rotations and possible Theta-dependence. The eight-dimensional joint kernel is therefore NOT a set of eight physical undetectable torsion modes or a gauge-invariant field-degree count. Curvature, holonomy, nonlinear variation and matter response can detect it. The joint rank only prevents a false inference from these two truncated readouts.

## Next action-selection gate [OPEN]

**Do not repeat known work:** the independent Palatini-Holst Cartan map, split-jet right inverse, real-dilation minisuperspace chain rule, vacuum b-degeneracy and full homogeneous Hamiltonian are already available in the repo. The next decisive check is to write a SINGLE candidate Theta action with an explicit real measure, physical/redundant connection identification and permitted variation bundle. Compute its full chain-rule pullback and project its Euler equations onto the normal covector above; prove that this equation survives after reducing auxiliaries and constraints. Then calculate the reduced principal symbol and bounded physical Hamiltonian, without assuming a new carrier dimension or replacing the canonical sharp metric. The current note does not select such an action.

**Verifier:** `tests/test_clifford_composite_variation_rank.py` (11/11 local exact SymPy tests). **Grounding:** `canonical/geometry/connection.tex:13-83`; `research_tracks/action_selection/physics_closure_action_family_2026_10.en.md:39-80`; `research_tracks/action_selection/physics_closure_dilation_2026_10.en.md:16-54`; `research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md:17-145`; `research_tracks/canonical_relation_generalized_dirac/FULL_CLIFFORD_TORSION_SQUARE.en.md:15-132`. No fundamental action selection or independent semantic translation approval is claimed.
