<!-- BILINGUAL-UNIT: composite_metric_1d_bracket_selector -->
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


# Composite metric structure function: conditional 1D Hamiltonian selector

**Exact canonical toy theorem (2026-10-25). Not UBT's physical Hamiltonian or a closed generally covariant constraint system.** Follow-on to draft #738. Note recent draft #739: canonical connection uses D=∂+AΘ−ΘB, while research #735 uses a plus-right-B redefinition; no independent connection is invoked here.

Let q be one real coordinate field on a 1D spatial patch with q'(x)≠0, p its canonical density, and bracket {q(x),p(y)}=δ(x-y). Construct a *trial* induced metric h_xx=(q')², h^xx=(q')^(−2). This is the 1D analog of the locked first-jet construction, but does not implement the full four-dimensional Lorentz-sharp metric, torsion or connection, nor the field-dependence on time derivatives.

Take H[N]=∫N(x)[a p²/2+U(q')+V(q)] dx with constant a≠0 and differentiable U,V; D[ξ]=∫ξ p q' dx. Functional differentiation gives δH/δp=Nap, δH/δq=−(N U'(q'))'+NV'(q). Therefore the antisymmetrized bracket is exactly
\[
\{H[N],H[M]\}=\int dx\,a p U'(q')(N M'-M N')
=D\!\left[\frac{a U'(q')}{q'}(N M'-M N')\right].
\]
Requiring the *formal H,H structure function* to be precisely h^xx=1/(q')² for all q'≠0 forces
\[
aU'(s)/s=1/s²,\quad\Rightarrow\quad U(s)=a^{-1}\log|s|+C
\]
on each connected sign branch. This is a nontrivial conditional selector for the gradient density; potential V(q) is unrestricted by {H,H} alone.

**Fails two independent full-theory gates:**
1. Since q is a spatial scalar and p a density, p² and log|q'| do not transform as weight-one scalar densities under arbitrary spatial diffeomorphisms. Accordingly {D,H} does not have the required GR covariance for this ansatz. Choosing dx is a coordinate-fixed toy model. The log term is also unbounded below as q'→0 and the patch becomes degenerate.
2. A spatial coordinate embedding variable y=q in 1D has h_xx=(q')² and no intrinsic 1D gravity; the physical refoliation algebra, gravitational propagating modes, and curvature cannot be inferred from this reduction. In UBT the composite tetrad E=N0^-1/2 DΘ has 4D Lorentz slice and composite torsion, so its h^ij includes higher dimensional constraints and time-derivative dependence.

**Outcome:** the {H,H} condition can constrain a gradient potential once a specific composite h is substituted, but only full (D,D), (D,H), and (H,H) closure with valid density weights, physical Dirac brackets and stability can establish a credible Hamiltonian candidate. No action finalized and no canonical files changed.
