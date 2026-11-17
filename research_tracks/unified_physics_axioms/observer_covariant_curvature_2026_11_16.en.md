<!-- BILINGUAL-UNIT: observer-covariant-curvature-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact GR comparator; novel observer-information proposal remains conjectural.
UBT-AI-PROVENANCE-END
-->
# Observer-covariant tidal curvature in arbitrary GR spacetime — Relativity squared baseline

<!-- UNIT: status -->
## Scope and claim status
[EXACT GR COMPARATOR / INFORMATION HYPOTHESIS OPEN] Use a single Lorentzian metric and a common Riemann tensor. Observer-dependent measured tidal components are already present in GR. A separate observer-conditioned information *estimate* of geometry might be studied, but is not implied by these formulas. This is NOT the scalar curvature-square R^2. It does not alter the locked canonical UBT Theta, covariant tetrad or metric.

<!-- UNIT: general -->
## Arbitrary observer and boost
```text
signature=(-,+,+,+),  u.u=-1, n.n=1, u.n=0
h_ab(u)=g_ab+u_a u_b
E_ab(u)=R_aμbν u^μ u^ν
v=gamma (u+beta*n), gamma=(1-beta^2)^(-1/2)
E_ab(v)=gamma^2 [E_ab(u)+beta*R_aμbν(u^μ n^ν+n^μ u^ν)
                          +beta^2*R_aμbν n^μ n^ν]
E^obs_ij(v)=e'_i{}^a e'_j{}^b E_ab(v)
Schwarzschild k=GM/(c^2 r^3):
E_static/k=diag(-2,1,1)
tangential boost (along e2): E_tangent/k=diag(-gamma^2*(2+beta^2),1,gamma^2*(1+2*beta^2))
radial boost (along e1): E_radial/k=diag(-2,1,1)
Kretschmann R_abcd R^abcd=48*k^2, both observers
```
All formulas hold pointwise for arbitrary Lorentzian curvature with the chosen sign convention. The second observer's actual measured components require a transported/local orthonormal tetrad e'_i orthogonal to v. The rank-two electric Riemann tidal projection E_ab(v) is orthogonal to v, but not necessarily trace-free: g^ab E_ab(v)=R_munu v^mu v^nu, subject to the adopted Riemann/Ricci sign convention. In vacuum it is trace-free. No Einstein field equation is needed for the general boost formula, only tensor algebra.

<!-- UNIT: vacuum -->
## Vacuum Weyl and full curvature
In vacuum R_ab=0, so the electric tidal tensor is the electric part of Weyl. The magnetic Weyl part depends on the same observer velocity and generally mixes with the electric part under boosts. Observer-dependent electric magnitudes are not scalars of the full curvature. E.g. a tangential Schwarzschild boost yields E'_ij E'^{ij}-E_ij E^{ij}=18*k^2*beta^2/(1-beta^2)^2, but the Kretschmann scalar remains 48*k^2. Under a radial boost along a principal Weyl direction, the three electric eigenvalues stay unchanged; changing speed does not necessarily change every tidal measurement. The Schwarzschild static observer is accelerated; the boosted frame is an instantaneous local comparison, not automatically a geodesic train.

<!-- UNIT: operational -->
## Operational distinction: train versus light
A freely falling massive body follows a timelike geodesic and a test light ray a null geodesic of the same physical metric in ordinary GR. A massive train need not freely fall; its acceleration is a separate non-geodesic effect. A photon has no rest frame and should not be treated as an observer with timelike four-velocity. Geodesic deviation describes relative free-fall acceleration via R(u,xi)u with conventional signs. Spatial slicing, coordinate transformations, relative Lorentz boosts, and unequal information are distinct effects.

<!-- UNIT: information -->
## Strict interface to a stronger Relativity² hypothesis
Let a universal physical geometry g[Theta] exist in the classical limit, and let I_O specify physically available relational data for observer O. A tentative estimate g_hat[Theta|I_O] must be (i) a covariantly defined tensor/conditional object with an explicit probability or state space, (ii) consistent when observers compare shared experiments, and (iii) reducible to the same universal g when relevant classical information is complete. A naive component-wise conditional expectation of metric coefficients is generally not diffeomorphism-invariant without relational identification of points; do not use it as a definition. There is no derived informational dynamics here. A new physical principle requires an invariant measurable residual, not the standard boosted tidal tensor.

<!-- UNIT: tests -->
## Decisive UBT tests
T1. Given an actual on-shell canonical Theta geometry, reproduce arbitrary-frame local Riemann components and the Schwarzschild radial/tangential benchmarks.
T2. Compute both Ricci and Weyl parts for matter backgrounds, e.g. FLRW; disentangle acceleration of a chosen observer congruence from curvature.
T3. Only after T1–T2, formulate a covariant observer-information map, demonstrate shared-measurement consistency and compare invariant predictions.
T4. Require the classical equivalence-principle limit and avoid additional independent fundamental observer-metrics.

<!-- UNIT: checks -->
## Verification status
The listed Schwarzschild benchmark follows from exact tetrad tensor contractions and has a standalone SymPy verifier at tools/verify_gr_observer_generalization_2026_11_16.py. It is an established GR algebra result; deriving a Schwarzschild solution from Theta is still open. Independent bilingual semantic review, Lean, full repository CI and UBT coupled field equations have NOT been completed for this note.
