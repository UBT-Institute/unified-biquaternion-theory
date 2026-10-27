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

# Dirac gauge-fixing test: constant norm on the split-jet carrier

**2026-10-26; exact local canonical model and Faddeev-Popov rank, not a complete MM/UBT Dirac count.** Based on `action_selection/mm_shift_gauge_dirac.en.md` and `information_first/NORM_PRESERVING_SPLITJET_HAMILTONIAN_GATE.md`.

For timelike X in R^(1,3) with X²=h>0, the full off-shell vertical symmetry of the pure-gravity pullback is δX=epsilon, δQ=-D_omega epsilon, leaving E and omega fixed. The constant-norm condition chi(X)=X²-h0=0 for h0>0 has derivative δ_chi=2 X·epsilon, hence rank ONE. It is locally an admissible **partial gauge fixing** of one real component of the four-function shift symmetry; it is not four gauge conditions. The residual shift has three parameters epsilon perpendicular to X. A coordinate-invariant finite representative is any future timelike X'=sqrt(h0) (cosh(rho),sinh(rho)*u_hat), accompanied by Q'=Q+D(X-X'). All these X' describe the SAME (E,omega) in the pure MM pullback. Thus chi=0 does not create a new radial oscillator or a colour triplet.

Canonical finite-dimensional benchmark: take a gauge-invariant physical pair (e,p_e), a carrier pair (x^a,p_a), and four primary first-class constraints p_a≈0 generating unrestricted carrier shifts (a=0..3). The constraint surface / gauge quotient has 1 physical canonical pair (e,p_e). Add chi=x·x-h0≈0 and choose a compatible radial generator C_rad=(x^a p_a)/(2h0) (on chi=0); {chi,C_rad}=(x²)/h0≈1. This is a second-class gauge-fixing pair and removes one original first-class generator plus one gauge condition, leaving three first-class carrier shifts. Physical phase-space dimension is unchanged. The toy carries no claim that the actual MM canonical momenta are p_a=0: because E depends on derivatives of X, their constraints involve auxiliary momenta and require first-order conversion as already explained in mm_shift_gauge_dirac.en.md. The canonical statement is the local gauge-orbit dimension and gauge-fixing rank, not the full field-theoretic Dirac closure.

**Subtlety:** the naive perpendicular shift epsilon satisfying X·epsilon=0 only defines an infinitesimal tangent distribution; integrating it requires norm-preserving finite transformations and field-dependent parameters. The full residual gauge group is a stabilizer/orbit groupoid description, not a fixed three-dimensional translation subgroup. Strict positive h0 maintains non-null split-jet right inverse; taking h0→0 is singular in this chart.

If a new action contains independent h(X)-dependent matter, the *full* shift ceases to be a gauge symmetry and chi=0 may become a physical holonomic constraint; its classification must be redone for that action. For the existing pure gravity candidate, no previously absent Theta-colour Hamiltonian follows.

**Next actionable bridge:** first identify an E,omega-based gauge-invariant physical observable with a nontrivial canonical bracket; calculate its observer correlation and whether it determines any Hamiltonian coefficients. For a full complex Theta action, separately derive the additional imaginary-component constraints. Do not label the three residual carrier orientations physical.
