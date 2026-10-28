<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# AGENT TASK — Conformal Cartan bridge from UBT geometry, causality and shared reality

**Date:** 2026-10-28
**Track:** `research_tracks/conformal_causal_shared_reality/`
**Branch:** `research/conformal-causal-shared-reality-20261028`
**Tier:** C_working / exploratory
**Do not edit:** PR #807, PR #808, `canonical/`, `CLAIMS*`,
`provenance/`, existing author attestations.
**STOP after Gate G1.** Do not select an action, claim GR recovery,
or merge this draft without an independent adversarial check.

## Starting evidence — reuse, do not rerun a one-week selector search

Read `RESEARCH.en.md` and `G1_NEGATIVE_CONTROL.en.md` first;
replay exact checks:

```bash
python -m unittest discover -s tests -p 'test_theta_conformal_gate.py' -v
python -m unittest discover -s tests -p 'test_theta_gradient_solder.py' -v
```

If repository pytest uses its own test harness, also execute
`python -m pytest -q tests/test_theta_conformal_gate.py tests/test_theta_gradient_solder.py`.

Current results: locally seven checks passed (6 chart checks + one
gradient-curvature test). This is NOT an external CI or Lean certificate.

Accepted mathematical starting points:
- [STD] C⊗H≅Mat₂(C) as ONE candidate chart; component count is provisional.
- [STD] Hermitian determinant yields Minkowski quadratic form.
- [STD] SU(2,2) acts on the future tube G/K, K=S(U2×U2), dim 8.
- [T1] Pullback of positive tube metric cannot be Lorentzian.
- [T2] No fully SU(2,2)-equivariant pointwise map G/K→G/P, with
  P the null-line parabolic. Check group-theoretic assumptions explicitly.
- [STD] A naive full-rank e=d(phi) has zero Riemann curvature.
- [OPEN] Any UBT-specific bridge from Theta to a nonflat,
  physical Lorentz tetrad with derived dynamics.

## G0: reproduce the finite kinematic algebra (mostly complete)

Verify independently, preferably analytically and in exact CAS:
1. Hermitian and anti-Hermitian conventions; how the repository's
   i·Herm condition relates to W=X+iY.
2. Compact stabilizer K vs parabolic P, including connected covers,
   centers and the maximal-compact argument.
3. The 8-positive-direction tube metric and why its pullback is not
   the 4D Lorentz metric.
4. Disk phase vs tube linear phase: do not identify either with UBT
   U(1) or Wick rotation without a proven transformation.
5. Show that finite c / causal order determines a conformal class
   **given a Lorentzian geometry**, not an automatic SU(2,2) gauge field.

Reject count-of-components coincidences as proofs of equivalence.
Do NOT change fundamental Theta's component count by assumption.

## G1: derive or refute a Theta-to-solder-form bridge

Compare at least two **explicit** candidates, maintaining the same
declared field representation throughout:

A. `e_mu^a = P^a(Re D_mu Theta)`, with physical Lorentz slice and
   an explicitly represented **independent conformal Cartan**
   connection A_mu. Show exact under-gauge transformation, whether
   P^a is well defined under the FULL group, whether an independent
   P-reduction is implicit, rank, and exact curved solution. If
   reduced to e=d(phi), reuse the flatness no-go.

B. A genuine parabolic/tractor compensator or *derived*
   P-reduction from Theta and its first jet. Specify the carrier,
   every constraint and gauge redundancy, G-equivariance under local
   transformations, the number of independent fields, and whether
   using a null ray secretly adds an independent field. Do NOT
   import an unconstrained tetrad hidden in A^{P}.

If A and B both fail, exhibit restricted counterexamples or a theorem
with explicit assumptions. Do not write a third ad hoc potential.

For a surviving candidate supply:
- `e` and `g=e^T eta e` with stated Lorentz reality.
- 16-rank variation map on a regular patch, including *constraints*.
- Nonzero, explicitly computed Riemann tensor, NOT mere nonconstant g.
- Full first variation, including e(Theta,A) chain rule and independent
  A and Theta variations for one declared comparison functional.
- A table identifying its dependence on PR #807 no-go assumptions.
- Distinguish exact symbolic algebra, numeric samples, formal proof,
  and unproved analytic physics claims.
- EN and CZ paired notes preserving `C_working` status.

## After G1 — parking lot ONLY, not immediate implementation

G2: Specify shared-reality algebras/states on causal diamonds
and test one finite-region entanglement variation. An overlap consistency
rule does not by itself imply a global quantum state, a classical Poisson
bracket, or the Einstein equations. Review Zeeman, modular flow and
Jacobson's fixed-volume, conformal-matter hypotheses.

G3: Only after a successful geometric and information bridge,
write a sharply bounded (max polynomial degree) invariant-action family.
`Weyl^2` alone has known fourth-order/ghost concerns. No claims of
unique action without a class and proof.

G4: Full spatial Dirac constraints, physical Hessian, helicity
spectrum, ghost/tachyon/hyperbolicity check, GR endpoint; preregister
first discriminating observation only if these pass.

## Report format (mandatory)

For each result state: exact assumptions, expression, proof or
counterexample, verifier command, proof boundary, effect on
[T1]/[T2], and one of [STD], [AX], [CANDIDATE], [PROVED],
[COUNTEREXAMPLE], [OPEN]. Record original author of research
programme as supplied in the repo; AI assistance transparently;
do not overwrite historical provenance.

**STOP CONDITION:** G1 is proved or cleanly obstructed for both
declared candidates. Produce a short recommendation that preserves
rather than silently revises #807/#808.

## G1 interim result (2026-10-28) — read before extending

See G1_INDUCED_GEOMETRY.en.md / .cs.md and
tests/test_theta_induced_geometry.py. An explicit trial
Theta = t I + x sigma_1 + y sigma_2 + z sigma_3
        + i kappa t x sigma_1
has a Lorentz-signature, genuinely curved induced metric
g=B(dTheta,dTheta), with R_{txtx}(0)=kappa²,
and a derived local i·Herm tetrad. It is only SL(2,C)
congruence/global-phase covariant in the declared representation;
full SU(2,2) covariance, the exact canonical UBT metric
identity, a viable action and a graviton spectrum are **OPEN**.

Critical obstruction: about an affine flat background
the metric has no gauge-invariant **linear** graviton:
tangent Theta perturbations are diffeomorphisms,
normal perturbations enter at quadratic order.
Also, a coframe E(phi)dphi with only four invertible
real coordinate scalars is locally a pullback of
one fixed target geometry (no independent metric DOF).
Causal diamonds and overlap alone cannot select
a positive Weyl factor because g and f²g share
all causal cones. Require a quantitative state/entropy
scale before using [SR] as a dynamical selector.

G1 remains PARTIAL. **Do not proceed to G2–G4** or merge
on the strength of a curved example. First independently
audit the 7 exact tests, exhibit a genuinely covariant
jet/Cartan realization with nontrivial *linear* spin-2,
and respect the stop-for-review criterion.

## G1 continuation result — real dilation and projected EH equations (2026-10-28)

Read the paired notes G1_RT_EXTRA_SOLUTION.en.md/.cs.md and
G1_CONNECTION_RANK.en.md/.cs.md before proposing another action.
Supporting tests:
- tests/test_theta_rt_extra_solution.py: exact restricted Regge–Teitelboim non-Einstein stationary solution
- tests/test_theta_connection_metric_rank.py: 9→10 metric Jacobian rank when real dilation joins Lorentz boosts (fixed timelike Theta)
- tests/test_theta_exact_dilation.py: u=dσ is locally removable by a real Theta rescaling and cannot itself supply a full tetrad

**Decision:** Pure-Lorentz rank deficiency can be repaired pointwise, but
free boost+dilation variables make the composite tetrad effectively
independently variable (not derived from Theta). Exact dilation has
du=0; a nonexact u carries new curvature and requires its own
constraints and dynamical justification. Neither fixes the
missing two healthy propagating graviton modes.

**Next admissible single task:** classify one explicit, noncircular
local connection closure u[Theta], Omega[Theta] or a constrained
connection first-order system, and compute its linear principal
symbol after gauge reduction on one regular curved solution.
If it fails, write a scoped counterexample and stop. Do not
guess a new fundamental potential, import a freely varying
Cartan solder form, or claim that causal cones alone set
the conformal scale or Newton coupling.
