<!-- BILINGUAL-UNIT: mm-complex-theta-spectator-rank -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional principal-symbol result, not full UBT Dirac analysis.
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

# Route A decision: four imaginary Theta components are spectators in the current MM gravity action

**2026-10-26. New restricted-action kinetic rank witness.** Existing source: `single_theta_macdowell_mansouri_candidate.en.md` defines X as the Lorentz-real projection of the full complex Theta, and S_MM depends on Theta through E[X,omega,K_J,w] only. The earlier `colour_projector_shift_rank.en.md` already found six projector tangents; the new point here is the **simultaneous variational rank of the actual gravity action and the colour projector**.

In any local real-linear chart write Theta=X+iY with four real coordinates X^a and four Y^a (the i is a coefficient-space complex structure, not a second fundamental field). If X=r e0, Y=0, r>0, and the gravity-only candidate is S_MM[E(X,K_J,w,omega),omega], then it is **independent of all Y and their derivatives**, exactly (not only to quadratic order). Thus
delta S_MM/delta Y^a=0 and d²L_MM/d(dot Y^a)d(dot Y^b)=0, and all mixed velocity Hessian entries involving dot Y vanish, whatever gravitational kinetic/connection reduction is used. The full first-order presymplectic form pulled back from the gravity candidate annihilates the four Y variations. It follows that this action ALONE cannot give dynamics, masses or Hilbert-space excitations for the missing imaginary Theta directions.

However P_+(Theta)=Theta Theta† G/(Theta†GTheta) **does** depend on three of the Y directions at first order. At reference Theta=r e0,
  delta_{Y_j} P = (i/r)(e_j e0†G - e0 e_j†G), j=1,2,3,
which are three independent nonzero real tangent matrices. The imaginary time-direction delta Y_0=i e0 is pure phase and gives delta P=0. Hence the real linear map Y∈R4 -> delta P has rank 3 and kernel dimension 1, whereas the gravity action has rank zero in these four Y directions.

No conventional Legendre transform of S_MM alone can generate a nonzero canonical momentum for any Y. One cannot read this as 'four healthy first-class gauge modes' without proving the full constraint algebra and boundary prescription. In the restricted action, arbitrary Y variations are off-shell action symmetries, but they shift the colour projector, so P is NOT a gauge-invariant observable of the restricted gravitational quotient. The enlarged colour physics needs a genuinely new coupled invariant in the SAME eventual action or a different gauge interpretation.

**Decision gate:** The presently specified MM action is not yet a full-complex-Theta action with physical colour dynamics. Before attempting 'full Hessian' one must specify a definite nontrivial Y-dependent term and check its invariance, kinetic principal symbol, full Dirac constraints, and metric lock; there is currently no uniquely selected such term from Route A. This is a concrete structural endpoint of the existing candidate, not an impossibility theorem for any conceivable geometric completion. The observer-negentropy option B can be studied later without claiming it cures this rank defect.

Verification: `tests/test_mm_complex_spectator_rank.py`.
