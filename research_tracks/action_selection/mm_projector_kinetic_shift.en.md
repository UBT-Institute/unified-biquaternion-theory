<!-- BILINGUAL-UNIT: mm-projector-kinetic-shift-test -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional quadratic compatibility test, not a full Dirac proof.
UBT-AI-PROVENANCE-END -->
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

# Route A: explicit quadratic conflict between projector kinetics and gravity-only shift gauge

**2026-10-26.** Reuses the previously verified projector differential rank (6 real; 3 Lorentz-real) and split-jet gravitational shift. This is a new **combined-action perturbative compatibility check**, not a new proof of the component rank.

Consider the specific, deliberately chosen candidate
S_total = S_MM[E(X,Q),omega] + S_P[P(X),g(E)],
where S_P = (c/2) integral sqrt(-g) g^{mu nu} [-tr(partial_mu P partial_nu P)] with c != 0, P=n n† G, n=Theta/sqrt(Theta†GTheta), G=diag(1,-1,-1,-1). The formula on the full complex timelike carrier is conditional on an identification of its Lorentz-real projection X with the split-jet variable; evaluate the following witness on their shared real chart.

At X=r e0 (r>0), write small real transverse fluctuations u_j. The projector satisfies -tr(delta P delta P)=2 sum_j u_j²/r². Thus the quadratic velocity matrix for three transverse real directions, on a fixed local Lorentz background, is nonzero of rank three (for nonzero c with a specified time-sign convention). The same carrier shifts delta X_j=epsilon_j and delta Q=-D_omega epsilon leave E fixed but change P. Consequently delta_e S_MM=0 while delta_e S_P generally != 0: even a compactly supported time-dependent epsilon starting from u=0 induces nonzero quadratic kinetic action. Therefore the **old** shift constraints cannot remain first class as generators of arbitrary carrier shifts in this summed theory. This is an off-shell symmetry-breaking witness, not by itself proof of a propagating ghost.

On the full complex tangent the projector has six real directions and its positive internal quadratic form has rank six, but only the three *real* shifts above have been proved in the restricted gravitational lift. Do not declare six first-class constraints absent or present in the full complex theory. In particular a field-dependent positive internal norm on a frozen background is insufficient to establish positive physical energy after metric-locking; see `T2_GAUGE/su3_positive_kinetic_metric_lock_audit.md`. Nor does this sigma-model generate eight dynamical SU(3) gluons.

A compensating transformation of the projector or a separately transforming gauge connection could restore an enlarged symmetry, but that would be an additional demonstrated construction, not a consequence of the existing geometric MM action. Alternatively, enforce the old split-jet quotient and restrict new matter terms to functionals of (E,omega) and invariant descendants; those cannot encode this orientation P(X) as a separate local physical field. The two architectures must not be conflated.

**Decision:** the explicit additive projector kinetic candidate FAILS the original carrier-shift compatibility test. Remaining route A question is whether any existing single-Theta *coupled* kinetic structure replaces those shifts by new healthy constraints without independent postulates; this requires a full velocity-Hessian and Dirac computation on the exact proposed action.

Regression: `tests/test_mm_projector_kinetic_shift.py`, locally 2 tests passed with SymPy/pytest.
