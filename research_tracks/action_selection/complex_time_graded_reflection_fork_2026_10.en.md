<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: complex-time-graded-reflection-fork -->
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


# Complex-time graded connection: local fiber versus reflected holomorphy

**2026-10-31 · C_working.** This continues merged PR #823 without claiming completed microscopic dynamics. The previous global Lorentz/holomorphy obstruction, quaternion-sharp phase weight and split-jet gravitational comparator are reused. New: exact reflection-holomorphic construction, finite-jet locality obstruction and compact-fiber half-winding example.

## Canonical interpretation and reflected involution [ASSUMED]

Canonical psi is a compact internal scalar-fiber coordinate. Previous work proves that strict all-inertial-frame holomorphy in t+i psi cannot be imposed on general Lorentz-covariant microscopic dynamics when psi is an independent Lorentz scalar. We therefore examine a reduced holomorphic strip with reflection symmetry only, not the complete physical Lorentz theory:

\[
\tau=t+i\psi,\qquad
F^\star(\tau):=F(\bar\tau)^\dagger,\quad
(FG)^\star=G^\star F^\star,\quad
(\partial_\tau F)^\star=\partial_\tau(F^\star).
\]

Unlike ordinary pointwise Hermitian conjugation, the Schwarz-reflected adjoint maps holomorphic matrix functions to holomorphic ones, reverses products, and commutes with the complex-time derivative. It permits two reflected eigensectors of the SAME original Theta and a graded auxiliary term:

\[
H=\tfrac12(\Theta+\Theta^\star),\quad
X=\tfrac12(\Theta-\Theta^\star),\quad
H^\star=H,\quad X^\star=-X,\quad
\mathcal K_\mu=K_\mu X+XK_\mu^\star.
\]

Locally choose a nonvanishing determinant of H and a branch of the logarithm/square root. The earlier relative center and defining Lorentz connection then have the holomorphic reflected candidate:

\[
\widehat H=H/\sqrt{\det H},\quad
w_\mu=-\tfrac12\partial_\mu\log\det H,\quad
\mathfrak D_\mu\Theta=\partial_\mu\Theta+
\varpi_\mu\Theta+\Theta\varpi_\mu^\star+
w_\mu\Theta+\mathcal K_\mu.
\]

For holomorphic SL2(C) transformations, the covariant algebraic identity holds with reflected star. This does NOT override the older all-frame complex-time theorem:

\[
\Theta'=S\Theta S^\star,\quad
K'_\mu=SK_\mu S^{-1},\quad
\varpi'_\mu=S\varpi_\mu S^{-1}-
(\partial_\mu S)S^{-1},\quad\det S=1
\Longrightarrow
\mathfrak D'_\mu\Theta'=S(\mathfrak D_\mu\Theta)S^\star.
\]

## Reflected holomorphy has a locality price [PROVED]

At nonreal complex time ordinary dagger creates conjugate-tau dependence, while the reflected star evaluates the original field at the mirror coordinate. This is a genuinely different operation, coinciding with dagger only on the real-time axis:

\[
F(\tau)^\dagger=\overline{F(\tau)}^{\,T}
\quad\text{is generically antiholomorphic},\qquad
F^\star(\tau)=\overline{F(\bar\tau)}^{\,T}
\quad\text{is holomorphic}.
\]

For every finite jet order N and any nonreal tau0, choose the following holomorphic polynomial. Zero and this polynomial have identical N-jets but different reflected-star values at tau0:

\[
\tau_0=t_0+i\psi_0,\ \psi_0\ne0,\quad
f_N(\tau)=(\tau-\tau_0)^{N+1},\quad
\partial_\tau^k f_N(\tau_0)=0\ (0\le k\le N),\quad
f_N^\star(\tau_0)=(2i\psi_0)^{N+1}\ne0.
\]

Consequently the star map on arbitrary holomorphic configurations is NOT representable by any finite-order local differential operator on the complex-time cylinder. This is not a prohibition of nonlocal theories or specially restricted solution spaces. There is a separate standard fact: imposing ordinary pointwise anti-Hermiticity on an open complex-time region makes a holomorphic matrix function constant in tau, but says nothing about other spacetime coordinates:

\[
E(\tau)\in i\operatorname{Herm}_2
\ \forall\tau\text{ in a connected complex open set},\quad
\partial_{\bar\tau}E=0
\quad\Longrightarrow\quad\partial_\tau E=0.
\]

## The local smooth scalar-fiber route [ASSUMED]

In the already provisionally selected scalar-fiber branch, do not require strict holomorphy of general microscopic Theta in t+i psi. Treat the original field as smooth in spacetime and psi; its ordinary dagger projectors and real-linear graded auxiliary connection are local at each fiber point:

\[
\Theta(x^\mu,\psi)\in C^\infty,\quad
\psi\in S^1,\quad
P_\pm(\Theta(x,\psi))=
\tfrac12\left(\Theta(x,\psi)\pm\Theta(x,\psi)^\dagger\right).
\]

This branch avoids the reflected-star nonlocality problem but does not yield psi kinetic energy, field equations, a positive Hamiltonian, or action selection by itself. The real Lorentz slice and physical-versus-defining spin remain constraints to be varied correctly.

## Compact fiber and the half-winding obstruction [PROVED]

In the optional reflected-holomorphic cylinder, this entire example is positive Hermitian on the physical real axis and periodic around the imaginary fiber:

\[
H_n(\tau)=\operatorname{diag}(e^{n\tau/R},1),\quad
R>0,\ n\in\mathbb Z,\quad
H_n(\tau+2\pi iR)=H_n(\tau),\quad H_n^\star=H_n.
\]

The relative logarithmic ONE-FORM is globally single-valued even when its potential is not. The period and its exponential are:

\[
w_\tau=-\frac n{2R},\quad
\oint_{S^1_\psi}w_\tau\,d\tau=-\pi i n,\quad
\exp\!\left(\oint w\right)=(-1)^n.
\]

The normalized Hermitian matrix exhibits sign monodromy for odd n:

\[
\widehat H_n=
\operatorname{diag}\left(e^{n\tau/(2R)},e^{-n\tau/(2R)}\right),
\quad
\widehat H_n(\tau+2\pi iR)=(-1)^n\widehat H_n(\tau).
\]

This is a conditional topological sign of a reduced analytic sector, NOT a prediction of physical generations or spin. Choosing a globally single-valued square root of det H would be an additional topological restriction.

## Dynamics decision [OPEN]

Keep the canonical smooth scalar-fiber branch as the next LOCAL candidate for the existing real-linear graded connection. Do not silently promote strict t+i psi holomorphy to a fundamental physical axiom. A reflected-star strict analytic extension is possible mathematically but nonlocal on the fiber for unrestricted holomorphic fields. Next actual physics gate: specify the psi-principal part of the already chosen single-Theta/MM candidate, its admissible real-linear matter sector, and full Cartan/K/Theta constraint algebra. Existing action nonselection remains unresolved.

**Verifier:** `tests/test_complex_time_graded_reflection_fork.py` (17 exact SymPy tests), run with 33 previous graded-jet and MM-adjoint tests in Physics Laws CI. **Previously established sources:** `canonical/THEORY/complex_time_canonical_choice.tex:31-129`, `research_tracks/theta_complex_time_classification/holomorphy_lorentz_no_go.md:14-64`, `research_tracks/action_selection/full_theta_reallinear_graded_jet_2026_10.en.md:15-140`, `research_tracks/action_selection/phase_central_metric_compatibility.en.md:15-103`, `canonical/CANONICAL_DEFINITIONS.md:130-201`. No Lean proof, independently approved semantic translation, final action or new measured physical prediction is claimed.
