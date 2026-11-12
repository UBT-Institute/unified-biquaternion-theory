<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Research work programme, not a canonical result or proof.
UBT-AI-PROVENANCE-END
-->

# Current UBT Research Programme — Theta Geometry, Electromagnetism, Scalars, Then Information

**Date:** 2026-11-12  
**Status:** WORKING PLAN / OPEN hypotheses, not new axioms, proofs, or a replacement fundamental action.  
**Location:** Research track only. Preserve locked canonical definitions until an independently verified complete derivation justifies a change.

## Motivation and guiding hypothesis

Seek the simplest physically viable decomposition of ONE complex-biquaternion field
\[
\Theta=\theta_0+\theta_1\mathbf e_1+\theta_2\mathbf e_2+\theta_3\mathbf e_3,\quad
\theta_A\in\mathbb C,
\]
with gravity, electromagnetism, and scalar excitations emerging in *different ways* from the same carrier. Do not require all sectors to be the same form of curvature; do not insert independent gauge fields or scalar particles before testing the direct Theta candidates.

The order of work is
\[
\Theta
\quad\leadsto\quad
(\text{candidate EM projection},\ \text{induced/composite geometric metric},\ \text{scalar modes})
\quad\leadsto\quad
\text{one common dynamic law}
\quad\leadsto\quad
\text{information principle as a physically testable selector}.
\]

**The project's priority is a falsifiable derivation, not an aesthetically appealing assignment of labels.** Counting 3 complex coefficients = 6 real variables is only a starting point, not a Maxwell theorem.

## Work package 0 — preserve what is already canonical

- Canonical field: \(\Theta\in\mathbb C\otimes\mathbb H\simeq M_2(\mathbb C)\), 8 real value components.
- Locked 4D classical geometry:
  \[
  E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\quad
  \tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf1,\quad E_\mu\in W_L.
  \]
- \(\sharp\) is quaternion conjugation and leaves the central commuting complex unit unchanged; never replace this metric by a Hermitian/real/trace projector without declaring an alternative noncanonical branch.
- Paired derivative:
  \[
  D_\mu X=\partial_\mu X+A_\mu X-XB_\mu,
  \quad [D_\mu,D_\nu]X=F^A_{\mu\nu}X-XF^B_{\mu\nu}.
  \]
  A and B in the locked branch must be composite/reconstructed; do not silently count them as new independent propagating particles.
- Coordinate count: \(\tau=z^0=t+i\psi\) is *inside* \(q=z^\mu\mathbf e_\mu\) in the full complex-coordinate bookkeeping; no automatic 8+2=10 real coordinates. Distinguish a 4D physical base with \(\psi\) fiber from a genuinely 8-real-dimensional base. Distinguish all coordinate dimensions from the 8-real *fiber values* of Theta.
- Fundamental action status: DEFINED FAMILY, NOT FINALIZED, per canonical/ACTION.en.md. Never import separate Einstein-Hilbert, Maxwell or Higgs actions as proof of a single Theta origin.

## WP1 — electromagnetic sector: try direct components first

**Hypothesis EM-A:** After selecting a background \(\bar\Theta\), there is a Lorentz-equivariant local projection from \(\delta\Theta\) (possibly including first jet) into a *self-dual bivector* identified with the Riemann–Silberstein vector
\[
\mathcal F=\mathbf E+i\mathbf B.
\]
Simplest trial in one local frame: \(\operatorname{Vec}(\delta\Theta)=\mathcal F\). The six real component count is necessary but insufficient.

**Gates:** (a) show the self-dual Lorentz (1,0) transformation, not a simple Lorentz vector transformation; (b) field strengths with nonzero constant E/B exist without relying on a pure-gradient scalar potential; (c) Maxwell equations (including divergences and sources) follow from the single selected Theta Euler–Lagrange equations rather than being imposed; (d) two healthy helicity-1 degrees of freedom, appropriate gauge invariance/charge conservation; (e) coupling to the geometric metric produces its null characteristic cone.

**Failure response:** if the direct value projection is not equivariant, attempt a *minimal first-jet* projection or a composite connection from relative Theta components. No automatic abandonment of the overarching single-Theta hypothesis.

## WP2 — gravity: rotating gradients in the larger biquaternion carrier

**Hypothesis G-A:** Theta's local gradients sweep out a 4D tangent distribution in a larger *real* coefficient carrier. Their changing orientation can induce a spacetime connection and nonzero curvature, analogous to Gauss's equations for a curved immersion. The already documented 2D quaternionic sphere immersion is an exact mathematical witness, **not** a demonstration of 4D GR.

**Critical canonical compatibility:** In the fixed 4D Lorentz-real slice W_L and vanishing connection, four gradient vectors with a locally invertible Jacobian give a flat pullback metric. Therefore, either (i) derive a valid larger-target pairing compatible with locked physical sharp/metric or (ii) retain W_L but calculate the implicit *composite* connection and its full Theta dependence. Do not silently assume arbitrary 8D positive/Hermitian metrics.

**Gates:** solve the \(\Theta\mapsto E\mapsto g\mapsto\Gamma[\Theta]\) implicit system with constraints; compute \(\delta A[\vartheta],\delta B[\vartheta]\) before linearizing curvature; construct an on-shell *nonzero* gauge-invariant 4D Riemann tensor; derive two positive-energy graviton helicities and correct Newton/Einstein infrared dynamics from ONE finalized action. Pure frame rotation U^{-1}dU is flat unless projection/normal geometry creates genuine curvature.

**Light:** Once a Maxwell-like sector is dynamically coupled to \(g[\Theta]\), verify that its high-frequency principal symbol is \(g^{\mu\nu}k_\mu k_\nu=0\), with rays following null geodesics. Do not mistake "shortest spatial path" for a null geodesic. Nonminimal/torsion couplings can change propagation, so this must be calculated, not just assumed.

## WP3 — scalar/Higgs question without premature identification

**Hypothesis S-A:** scalar Theta coefficient, invariant amplitude, modulus, or internal/fiber fluctuations might yield scalar excitations. A complex scalar is NOT already the Standard Model Higgs doublet. Determine exact \(SU(2)_L\times U(1)_Y\) representation, gauge couplings, vacuum, stable potential, scalar mass spectrum and W/Z masses (where applicable) from a common action.

**Falsifier:** if the scalar is merely gauge/longitudinal/normalization redundancy, it is not a physical Higgs.

## WP4 — find wave dynamics only after the correct geometry and variables

Study first-order biquaternion/Clifford operators and their covariant second-order squares:
\[
[D_\mu,D_\nu]\Theta = \mathscr F_{\mu\nu}\Theta
\]
and \(\Box_D\Theta\), distinguishing Laplacian on a scalar section from the Laplacian on its gradient. Curvature can enter through operator commutators, including when the electromagnetic field strength is spatially constant.

**Do not use** \(D_\mu\Box_D\Theta=0\) as a new equation merely because it is intuitively attractive; if \(\Box_D\Theta=0\), that gradient is a derivative of the same equation. Determine a nontrivial kinetic Hessian, principal symbol, constraint algebra, and physical propagating spectrum. Guard against the documented fixed-background indefinite kinetic pairing and the metric-locked kinetic scalar collapsing to a volume term.

## WP5 — information principle LAST, but architected from the start

Information is a candidate **selection/constraint principle**, not automatically an additional fundamental force.

Candidate observable quantities: normalized correlation/observer data, relative Theta phases, coarse-grained entropy, Fisher-information functionals, and energy cost of irreversible information erasure (Landauer). These are distinct physical concepts; do not equate them or multiply one by an arbitrary coefficient and call dynamics derived.

**Tests:** require a well-defined probability distribution/measurement map from Theta, units and observer dependence, covariance, relation to energy-momentum conservation, and at least one new falsifiable condition on propagating modes or correlations. Preserve earlier no-go results from Fisher/Fokker–Planck and the torus-information action bridge; reintroduce them only with a different explicit premise proven sufficient.

Do not assume observer-specific entropies imply distinct spacetime metrics. Establish first whether information modifies the action, defines admissible states, or describes observer observables of fixed dynamics; these are mathematically different roles.

## Priority experiments and success criteria

1. **Transformation gate:** compute the Lorentz action on the whole complex Theta fluctuation and test whether the simplest \(\operatorname{Vec}(\delta\Theta)\) is a self-dual Maxwell bivector under that *same* physical action. An explicit counterexample must be reported if not.
2. **Curvature gate:** construct and verify a nondegenerate 4D Theta configuration with nonzero induced/composite curvature compatible with locked sharp/W_L, or prove the exact obstruction under stated hypotheses.
3. **Kinetic gate:** linearize the **single** actual composite action; check the characteristic polynomial, constraints, energy signs and physical helicities.
4. **Scalar gate:** find a genuine physical scalar and electroweak transformation, without calling the scalar coefficient "Higgs" merely by analogy.
5. **Information gate:** only after a consistent baseline, derive/test a parameter-economical information principle with predictive content.

## Status and links

- **Established mathematical ingredients:** exact biquaternionic rewriting of Maxwell equations; quaternion-gradient curved 2D immersion; 4D canonical tetrad-metric rank; known curvature commutator and operator factorization identities.
- **Not established:** electromagnetic or Higgs sector identified dynamically with Theta, curved on-shell 4D Theta gravity derived from a complete action, or information-derived unification.
- Follow prior work: 
  - research_tracks/unified_physics_axioms/MAXWELL_RS_BIQUATERNION_FIRST_ORDER_BRIDGE_2026_11_12.en.md
  - research_tracks/unified_physics_axioms/MAXWELL_BRIDGE_PURE_GRADIENT_AUDIT_2026_11_12.en.md
  - research_tracks/unified_physics_axioms/ROTATING_THETA_GRADIENT_INDUCED_CONNECTION_GATE_2026_11_12.en.md
  - research_tracks/unified_physics_axioms/THETA_COVARIANT_LAPLACIAN_GRADIENT_CURVATURE_GATE_2026_11_12.en.md
  - research_tracks/information_first/BOTTOM_UP_THETA_QUADRATIC_ACTION_SELECTION.en.md
  - research_tracks/information_first/TORUS_THETA_CANONICAL_ACTION_BRIDGE_GATE.en.md
  - canonical/ACTION.en.md
  - canonical/AXIOMS.md

**Decision:** This research programme is the present preferred *working direction*; the canonical theory is not declared completed or redefined.
