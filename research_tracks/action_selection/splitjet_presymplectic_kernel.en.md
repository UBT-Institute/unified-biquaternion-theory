<!-- BILINGUAL-UNIT: splitjet_presymplectic_kernel -->
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


# Presymplectic null shifts in the adopted split-jet gravity sector

**C-tier structural deduction, not a complete UBT Dirac classification.** Builds on the pointwise kernel calculation in draft PR #713 and the adopted Palatini–HT gravity action. No new action or coupling.

For each spacetime index mu, with nonnull X^a and E_mu^a=q^-1(D_mu X^a+K_J,mu^a_b X^b+w_mu X^a), the auxiliary map (K_J,w)->E has 7 components, rank 4 and three kernel directions. Let Z_mu^a_b be Lorentz antisymmetric and obey Z_mu^a_b X^b=0. Then the finite shift K_J,mu -> K_J,mu + Z_mu leaves E, omega, R(omega), the volume form and S_G unchanged at fixed other variables. This statement is off shell, pointwise and exact.

For a Lagrangian with no derivatives of these *kernel coordinates* z^I (I=1,...,12), and depending on the other fields through E and the adopted action, L is independent of z^I and dot z^I in a local adapted chart. Thus p_{z^I}=0 are twelve primary constraints and the canonical presymplectic two-form has twelve coordinate-shift null vectors before any further reduction. Since H_c is independent of z^I, preservation of p_z gives no secondary condition: dot p_z={p_z,H_T}=0. Their mutual brackets vanish. **Conditional:** when these adapted coordinates are valid, the remaining constraints are also invariant under the shift, and boundary data do not break it, the p_z are first-class generators of shifts in *this sector*. Their count should not be added on top of the final physical GR count because these are auxiliary coordinates absent from a reduced tetrad chart.

Important subtlety: the stabilizer frame depends on X. To form legitimate local coordinates split K into a transverse image plus stabilizer using a smooth X-dependent basis; the resulting canonical transformation may mix momenta of X. Therefore the naive bare momenta of original K components need not individually equal p_z. The precise primary shift constraints are linear combinations in adapted canonical coordinates. This is not a proof of twelve independent full-UBT gauge generators in a theory with additional K-dependent source or kinetic terms.

The already adopted gravity sector's first-order Palatini kinetic presymplectic potential has the form Theta_pre ~ (1/(4 kappa)) epsilon_abcd E^a wedge E^b wedge delta omega^{cd} (up to boundary conventions), plus auxiliary HT terms. Because E is invariant along Z, the contraction of this potential with delta_Z vanishes. Hence the *covariant* presymplectic current has null contraction along shift directions modulo boundary subtleties and field-dependent generators. This is the more invariant diagnostic than naive Hessian ranks.

## What this does not prove
No calculation here determines the entire constraint matrix involving omega, X, the image components of K_J/w, Lambda, C3, or any extra complex-time degrees of freedom. The gravitational endpoint still has two ADM graviton modes conditionally. It does not follow that the complete UBT has only two physical degrees of freedom, or that the (2,6) fixed-background kinetic signature is harmless.

**Next decisive calculation:** construct a concrete first-order canonical chart of the *adopted full gravity postulate*, explicitly retaining X-dependent adapted-kernel transformation, and compute mixed brackets with the tetrad/connection primary constraints. Only then claim a complete constraint count.
