<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: phase-central-metric.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional compatibility audit of stated phase transformation and sharp central metric; gauge implementation remains unresolved.
UBT-AI-PROVENANCE-END -->
# Scalar phase symmetry versus the canonical sharp central metric

**Status: EXACT ALGEBRAIC COMPATIBILITY OBSTRUCTION; MODEL-LEVEL INTERPRETATION OPEN.** This research note compares two **already recorded** UBT formulas. No replacement action, compensator, independent gauge field, phase projector or alternative metric is introduced. The conclusion is conditional on the phase group being intended as a symmetry of the same physical tetrad and metric.

## Canonical inputs examined together

The published invariant polynomial-potential classification declares the scalar phase action on the matrix representative. The canonical metric definition instead uses the complex-linear quaternion sharp without complex conjugation:

\[
X\longmapsto e^{i\alpha}SXS^\dagger,\qquad
E_\mu=q^{-1}D_\mu\Theta,\qquad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}I.
\]

Here q is a fixed positive normalization; the phase-covariant transformation of E follows for any **constant** phase when D is the already-declared homogeneous Lorentz spin derivative, and also for any ordinary local phase-covariant connection. We do **not** identify this scalar phase with Standard Model hypercharge or with the imaginary-time coordinate.

## Exact weight-two obstruction

The sharp involution is complex-linear, not sesquilinear. Therefore the central metric has phase weight two:

\[
(zE)^\sharp=z E^\sharp,\qquad
\boxed{g_{\mu\nu}[zE]=z^2g_{\mu\nu}[E]}\qquad
(z\in\mathbb C).
\]

For a phase rotation its infinitesimal and finite transformations are

\[
z=e^{i\alpha}\quad\Longrightarrow\quad
g'_{\mu\nu}=e^{2i\alpha}g_{\mu\nu},\qquad
\delta_\alpha g_{\mu\nu}=2i\alpha\,g_{\mu\nu}+O(\alpha^2).
\]

At a nonzero real Lorentz metric, the subgroup leaving the canonical metric unchanged is exactly

\[
\boxed{g'_{\mu\nu}=g_{\mu\nu}\ne0
\Longleftrightarrow e^{2i\alpha}=1
\Longleftrightarrow e^{i\alpha}\in\{+1,-1\}.}
\]

So the connected U(1) scalar phase **cannot be a gauge redundancy of the unchanged classical central metric**. Even a global constant phase outside the residual subgroup changes that metric; adding a local compensating phase connection would not remove the homogeneous weight-two factor. This is a kinematic compatibility theorem, not a dynamical equation of motion.

## Explicit nondegenerate Lorentz coframe witness

Using the biquaternion-to-Pauli representation consistent with quaternion sharp, choose a perfectly regular Lorentz coframe:

\[
E_0=iI,\quad E_j=-i\sigma_j,\quad
g_{\mu\nu}=\mathrm{diag}(-1,+1,+1,+1),\qquad
e^{i\pi/4}:\ g'_{\mu\nu}=ig_{\mu\nu},\quad
e^{i\pi/2}:\ g'_{\mu\nu}=-g_{\mu\nu}.
\]

A quarter-circle phase turns the real Lorentz metric into a purely imaginary tensor. A half-circle phase changes its sign. The unmodified central definition therefore does **not** give the same real physical metric along the entire continuous scalar phase orbit.

## Potential invariance does not solve the metric problem

The quadratic and quartic potential invariants were classified using Hermitian conjugation in addition to sharp. They are genuinely phase neutral:

\[
H(X)=\operatorname{Tr}(X^\sharp X^\dagger),\quad
H(e^{i\alpha}X)=H(X),\quad
|\det(e^{i\alpha}X)|^2=|\det X|^2.
\]

There is no contradiction in the **algebraic potential-classification theorem by itself**. The incompatibility arises only if its declared full scalar U(1) transformation is also assumed to act as a gauge invariance on the original sharp metric and full action. An invariant potential cannot neutralize the metric's nonzero charge by itself.

## Reality constraint and precise options without an invented correction

The real Lorentz slice has another exact limitation under multiplication by complex phases:

\[
E_\mu=i\,Y_\mu,\quad Y_\mu=Y_\mu^\dagger,\qquad
e^{i\alpha}E_\mu\in i\,\mathrm{Herm}(2)
\Longleftrightarrow e^{i\alpha}\in\{+1,-1\}
\quad(E_\mu\not\equiv0).
\]

Consequently the existing documents require an explicit **interpretation**, not an ad hoc modification: (A) treat the scalar U(1) as a symmetry of the complex potential sector that is not preserved by the selected classical real-geometric slice (global/spontaneous breaking or restricted domain), and do not claim it is a gauge symmetry of g; or (B) insist it is a physical gauge redundancy of the full geometry, in which case the current metric law and field transformations cannot both remain untouched, requiring a separately derived covariant metric prescription or compensating transformation law. Either option is a **choice still absent from the canonical action selection**.

This is not a theorem that all UBT is inconsistent: phase may be globally broken, an effective sector symmetry, or absent in the real metric theory. It is a theorem that the combination of full **gauged** continuous phase on E and the unmodified sharp metric is incompatible with a nonzero gauge-invariant real metric. Do not silently interpret the phase as the Standard Model U(1)_Y.

## Scientific decision and prior results

The minimal timelike kinetic/potential no-go (draft PR #700) already shows that adjusting an arbitrary scalar radial U cannot restore gravitation in that minimal auxiliary sector. The present audit now isolates an **independent upstream symmetry-selection gap**: even before choosing a more complicated action, say which transformation group the classical metric actually respects. This must be settled explicitly to derive, rather than postulate, any final UBT action.

**Tests:** `tools/verify_phase_central_metric_compatibility.py`, `tests/test_phase_central_metric_compatibility.py`; exact matrix sharp, Lorentz real metric, phase-weight two, and neutral potential invariants. **Sources:** `canonical/CANONICAL_DEFINITIONS.md` (sharp and real central metric); `research_tracks/action_selection/theta_potential_invariants.en.md` (declared scalar phase and neutral polynomial basis); `canonical/ACTION.en.md` (fundamental action remains undefined).
