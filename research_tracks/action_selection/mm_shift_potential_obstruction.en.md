<!-- BILINGUAL-UNIT: mm-shift-potential-obstruction -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional local shift-symmetry obstruction, not full-Theta Hamiltonian.
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

# Selection gate: Lorentz-invariant Theta potentials generically break the MM split-jet shift symmetry

**2026-10-26.** Cross-reference the established `theta_potential_invariants.en.md`, `splitjet_auxiliary_kernel.en.md` and `mm_finite_splitjet_lift.en.md`. The former classifies V=V0+m²H(X)+lambda1 H(X)^2+lambda2 |det X|² under Lorentz congruence and phase; none of those invariances implies the different local split-jet redundancy.

On the non-null Lorentz-real carrier chart E=(D_omega X+Q)/sqrt(N0), the exact finite split-jet shift is X->X'=X+epsilon, Q->Q'=Q-D_omega epsilon, omega fixed, yielding E'=E. For a standalone nondifferential action integral V(X) vol(E), with vol(E) nondegenerate, its off-shell variation is
 δ_e S_V = integral vol(E) (partial V/partial X^a) epsilon^a.
For arbitrary smooth compactly supported epsilon in the non-null chart, exact shift invariance requires ∂_a V=0 everywhere, hence V is constant on each connected component. The connected Lorentz-real timelike future/past and spacelike charts each have this property. It is not necessary that V vanish; V0 multiplies vol(E) and is a cosmological contribution.

Restrict the classified invariants to the Hermitian Lorentz-real slice X=x^mu sigma_mu. Then det X=eta(x,x) and H(X)=2 eta(x,x) (up to the conventions used in theta_potential_invariants). Hence V|real = V0+2 m² s + (4 lambda1+lambda2) s², s=eta(x,x). Its gradient is 2 x_a [2m²+2(4lambda1+lambda2)s] (depending on index raising), and vanishes for all non-null x only if m²=0 and 4lambda1+lambda2=0. In particular one tuned nonconstant full-complex quartic can *vanish identically on the restricted real slice*: do NOT infer lambda1=lambda2=0 from this restricted calculation. That tuned combination can still affect the remaining complex Theta sector, where the shift has not been derived.

Any separate regular derivative term for the carrier, such as eta_ab g^{mu nu}(D_mu X^a)(D_nu X^b), likewise changes under local epsilon because D X shifts by D epsilon while E stays fixed. Its variation can break the shift and make the carrier dynamical; evaluating its signature after gauge reduction is mandatory. Conversely terms constructed solely from E and omega retain this redundancy (up to boundary prescriptions).

**Consequences:** (1) MM gravity-only shift quotient is compatible with a carrier-independent cosmological density; (2) the generic Theta potential classified under Lorentz invariance cannot simply be appended without destroying the quotient; (3) the tuning 4lambda1+lambda2=0 on the real slice is necessary for shift invariance there but not a microscopic dynamical derivation and not sufficient to protect complex Theta; (4) an actual full-Theta action must either realize a larger compensating local symmetry for the complex sector, or honestly treat the lifted carrier as physical and re-run its full Dirac/positivity analysis. This is a candidate-selection gate, not a complete no-go for all UBT actions.
