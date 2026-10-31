<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: full-theta-graded-reallinear-connection -->
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


# A Lorentz-equivariant real-linear full-Theta graded auxiliary jet

**2026-10-31 · C_working · restricted existence construction.** This closes the *mathematical representation* subgate left open in PR #822 in the REAL-linear category. It does not close single-Theta microscopic action selection, physical matter, complex-time holomorphy or continuous central-phase gauge symmetry. It REUSES earlier full-Theta Hermitian/determinant and Lorentz-slice proofs; phase-weight two is historical, not new.

## Original field decomposition and specified graded jet [ASSUMED]

Use the same ORIGINAL Mat2(C) biquaternion with its existing two real sectors, no new fundamental complex field:

\[
\Theta=H+X,\quad P_\pm(\Theta)=\tfrac12(\Theta\pm\Theta^\ddagger),
\quad H=P_+(\Theta),\quad X=P_-(\Theta),\quad
H^\ddagger=H,\ X^\ddagger=-X.
\]

Choose a physical-versus-defining separation: varpi is the defining SL2(C) Lorentz connection; the independently varied gravitational connection omega remains the fixed-e Cartan variable in the already selected geometric MM/Palatini action. An algebraic auxiliary Lorentz-tensor K enters through the anti-Hermitian projector. Define this **candidate extension** of the original first jet, not a claimed complex-linear canonical connection:

\[
\mathfrak D_\mu\Theta=
\partial_\mu\Theta+
\varpi_\mu\Theta+\Theta\varpi_\mu^\ddagger+
w_\mu(H)\Theta+
K_\mu P_-(\Theta)+P_-(\Theta)K_\mu^\ddagger,
\quad K_\mu,\varpi_\mu\in\mathfrak{sl}(2,\mathbb C).
\]

As required by the earlier determinant audit, demand Hermitian H is positive and its normalized value is parallel with the defining connection. Then the relative real connection is derived from H, rather than independently inserted:

\[
w_\mu(H)=-\tfrac12\partial_\mu\ln\det H,\quad
\widehat H=H/\sqrt{\det H},\quad\det H>0,\quad
\partial_\mu\widehat H+\varpi_\mu\widehat H+
\widehat H\varpi_\mu^\ddagger=0.
\]

## Reality and local Lorentz equivariance [PROVED, scoped]

The K contribution is anti-Hermitian for EVERY K and anti-Hermitian X; it does not alter the Hermitian parallelism constraint. Thus the whole tetrad stays on the locked i-Herm Lorentz slice, not just a projected postprocessed subset:

\[
P_+(\mathfrak D_\mu\Theta)=
\partial_\mu H+\varpi_\mu H+
H\varpi_\mu^\ddagger+w_\mu(H)H=0,\quad
P_-(\mathfrak D_\mu\Theta)=\mathfrak D_\mu X,
\]

Under a local SL2(C) congruence, K transforms HOMOGENEOUSLY as a tensor, not as a second gauge connection. Varpi has the usual inhomogeneous gauge law. Both P-minus and the determinant w commute with Lorentz congruence in the required ways:

\[
\Theta'=S\Theta S^\ddagger,\quad
\varpi'_\mu=S\varpi_\mu S^{-1}-(\partial_\mu S)S^{-1},\quad
K'_\mu=SK_\mu S^{-1},\quad S\in SL(2,\mathbb C).
\]

This yields exact local equivariance even under nonconstant boosts, including the derivative of S:

\[
\det(SHS^\ddagger)=\det H,\qquad
\boxed{\mathfrak D'_\mu\Theta'=S(\mathfrak D_\mu\Theta)S^\ddagger}.
\]

A real local dilation of the existing Theta likewise preserves the Hermitian reality constraint and produces exactly the Weyl tetrad tangent needed for the conditional Euler adjoint theorem in PR #822:

\[
\Theta'=e^\varepsilon\Theta,\quad\varepsilon\in\mathbb R,\quad
w'_\mu=w_\mu-\partial_\mu\varepsilon
\quad\Longrightarrow\quad
\mathfrak D'_\mu\Theta'=e^\varepsilon\mathfrak D_\mu\Theta,\quad
\delta g_{\mu\nu}=2\varepsilon g_{\mu\nu}.
\]

**Auxiliary rank:** at the non-null timelike reference, the three Hermitian traceless boosts move X and the three anti-Hermitian rotations stabilize it. With one independent algebraic K per spacetime index, this reconstructs the exact previously assumed 12-rank split-jet tangent *within this chosen real-linear extension*:

\[
H=I_2,\quad X=iI_2,\quad
\delta_K\mathfrak D_\mu\Theta=i(\delta K_\mu+\delta K_\mu^\ddagger),
\quad
\operatorname{rank}_{\mathbb R}(\delta K_\mu\mapsto\delta_K E_\mu)=3,\quad
\operatorname{rank}_{\mathbb R}(\delta K\mapsto\delta E)=12.
\]

This now supplies a Lorentz-equivariant representation of the separate auxiliary action assumed in PR #822, WITHOUT a new fundamental Theta or independent w. Because the MM gravity candidate depends on K only via E, its Lagrangian introduces no explicit dK term; nevertheless the full Hamiltonian/first-class constraint reduction is NOT established. Its full action remains a chosen conditional gravitational comparator.

## Strict complex-linearity obstruction [PROVED, scoped]

There cannot be a nonzero field-independent COMPLEX-linear auxiliary map L on the whole original Mat2(C) that annihilates EVERY Hermitian H: the Hermitian basis {I,sigma1,sigma2,sigma3} already spans Mat2(C) over C. Hence complex linearity and H-annihilation force L=0:

\[
L:\operatorname{Mat}_2(\mathbb C)\to\operatorname{Mat}_2(\mathbb C)
\ \text{complex-linear},\quad
L(H)=0\ \forall H\in\operatorname{Herm}_2
\quad\Longrightarrow\quad L=0.
\]

The exhibited nontrivial K mechanism avoids this no-go precisely by being real-linear and dagger-dependent. It cannot simply be rewritten as a standard holomorphic complex-linear bimodule connection while keeping its exact H-only vanishing property:

\[
P_-(iH)=iH,\quad P_-(H)=0,\quad
\mathcal K_\mu(iH)=i(K_\mu H+HK_\mu^\ddagger),\quad
i\mathcal K_\mu(H)=0
\quad\text{in general}.
\]

## Central phase and geometry boundary [OPEN]

An independent central phase mixes H and X, and therefore the P-minus graded auxiliary connection is NOT equivariant under the unrestricted phase action on Theta. Separately, the pre-existing phase-versus-sharp theorem already excludes interpreting homogeneous nontrivial continuous central U(1) as gauge of the unchanged real metric:

\[
(zE_\mu)^\sharp=zE_\mu^\sharp,\quad
g_{\mu\nu}[zE]=z^2g_{\mu\nu}[E],\quad
z=e^{i\chi},\quad z^2\ne1
\quad\Longrightarrow\quad g[zE]\ne g[E].
\]

The phase issue must be **DECIDED**, not hand-waved: either the real classical geometry is a symmetry-breaking sector and full scalar central U(1) is not its gauge symmetry, or one must derive an inequivalent phase-neutral geometric field/transformation law. Complex-time holomorphy and spinorial Dirac matter may also require a different carrier representation; the prior antilinear Weyl intertwiner is real-linear and has opposite chiral phase weights. No electric U(1), SU(3) or charge is inferred here.

## Metric and action-level closure status [OPEN]

A regular real tetrad with nonzero auxiliary K has been checked against the ORIGINAL central sharp metric and a full Lorentz boost. The identity is not a new metric prescription:

\[
E_\mu=s^{-1}\mathfrak D_\mu\Theta\in i\operatorname{Herm}_2,\quad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}I_2,\quad
\operatorname{rank}e=4\ \text{in a regular witness}.
\]

**Remaining physical tasks, in strict order:** decide physical central phase on the classical Lorentz branch; justify this real-linear graded jet as a permissible full complex-Theta structure, or prove it cannot satisfy the required complex-time analytic axioms; insert it into the ALREADY SELECTED MM gravity action and verify fixed-e Cartan response and K/Theta constraint algebra, including physical-versus-defining spin distinction; derive nontrivial dynamics for the complex spectator sector; only then discuss a unique microscopic action, physical Hamiltonian positivity and predictions. No new gravity functional is selected in this note.

**Verifier:** `tests/test_full_theta_reallinear_graded_jet.py` — 18 independent exact SymPy regressions: Hermitian decomposition, K-reality, Lorentz congruence (global and local), real local Weyl scaling, H constraint, rank 12, canonical sharp metric with regular frame, complex-linearity no-go, and central phase counterexample. **Reuse, not rediscovery:** `research_tracks/action_selection/dynamics_reuse_hermitian_mm_adjoint_2026_10.en.md`; `research_tracks/action_selection/full_theta_hermitian_compensator_2026_10.en.md`; `research_tracks/action_selection/lorentz_slice_two_sided_connection_classification.en.md`; `research_tracks/action_selection/phase_central_metric_compatibility.en.md`; `research_tracks/action_selection/antilinear_weyl_map.en.md`; `canonical/CANONICAL_DEFINITIONS.md`. No Lean proof, independent bilingual semantic review, phase-gauge resolution or full physical dynamics is claimed.
