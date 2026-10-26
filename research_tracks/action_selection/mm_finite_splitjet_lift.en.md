<!-- BILINGUAL-UNIT: mm-finite-lift-quotient -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional local finite-gauge result; not complete microscopic UBT reduction.
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

# Finite gauge equivalence of split-jet carrier choices: exact local quotient

**26 Oct 2026 — incremental theorem after existing `splitjet_auxiliary_kernel.en.md` (rank 16, auxiliary nullity 12) and `split_jet_palatii_variational_lift.en.md` (surjective right inverse).** These prior rank results are NOT new.

Use N0>0 and a prescribed physical omega, and define E=(D_omega X+Q)/sqrt(N0), Q=K_J X+wX. On a chart where X² !=0, the (K_J,w)->Q map is onto. At fixed E and omega, any smooth non-null carrier replacement X' can be compensated by
   Q'=Q+D_omega(X-X').
Then D_omega X'+Q'=D_omega X+Q **exactly at finite amplitude**, and hence the full composite MM/Palatini action depending on (E,omega) is unchanged. On another chart X'²!=0, an explicit algebraic split-jet lift of Q' exists:
  w'_mu = (X'·Q'_mu)/(X'²),
  Y'_mu = Q'_mu-w'_mu X',
  K'_{J,mu,ab}=(Y'_{mu,a}X'_b-X'_aY'_{mu,b})/(X'²).
With eta index lowering, K' X'=Y' and Q'=K'X'+w'X'. One can also add any Lorentz-algebra element annihilating X'; it parametrizes the already proved 3-per-mu auxiliary kernel. This is a *field reparametrization*, not an extra transformation of omega or an independent fundamental symmetry selector.

The finite transformations between carrier choices compose: X -> X' -> X'' gives Q''=Q+D(X-X'') and is independent of the intermediate choice. Thus, locally, the entire fibre of the map (X,K_J,w)->E is covered by the X-choice and its auxiliary stabilizer, for suitable boundary conditions and smooth non-null charts. This proves a **local configuration-space quotient** for the restricted MM gravitational action, stronger than the earlier infinitesimal shift. No assertion is made that it extends smoothly over X²=0, preserves other Theta matter or complex-time action terms, or suffices to prove the global presymplectic symplectomorphism.

On shell (Palatini tetrad equation F=0 and linearized F=0), the covariant presymplectic current obtained in `mm_composite_presymplectic_variation.en.md` is the pullback of the Palatini current, up to Euler/topological boundary ambiguities. Strict vertical transformations with δE=δomega=0 are null. The inverse image of an admissible Palatini variation of (E,omega) exists locally by the same right-inverse, so the pullback form has the expected **local reduced symplectic structure** wherever the Palatini presymplectic quotient is regular. Potential extra nulls inherited from Palatini gauge, noncompact boundary charges, X²=0 singular loci, full Theta/psi dynamics and actual Dirac closure are not addressed.

**P0 implication:** no new perturbative Theta ghost can be inferred solely from redundant X labels in this *gravity-only* MM lift; the full physical problem is to couple all other Theta/psi sectors without breaking the shift quotient or introducing propagating negative norms.

Verification: `tests/test_mm_finite_splitjet_lift.py`. 
