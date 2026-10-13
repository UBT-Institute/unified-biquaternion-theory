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

# Metric quotient versus full connection: differential-closure decision

Date: 2026-10-12. RESEARCH, AI-assisted; no canonical claim promotion. This note does not select an action.

## Premises
Let V be a non-null Lorentz-real field with a nondegenerate coframe e_mu^a=s^{-1} D_mu V^a and g=eta_ab e^a tensor e^b. omega is a metric-compatible spin connection. Consider omega'=omega+C with C_mu in so(1,3) and C_mu V=0. Holding V fixed preserves e and g.

## Result 1: the metric observable subalgebra is closed under canonical metric differential constructions

Any natural tensor built from g, its Levi-Civita connection nabla^g, Riemann tensor, metric Hodge star, exterior derivative and Hodge codifferential depends only on g and orientation where required. Thus it is unaffected by omega->omega+C for fixed V and e. In particular the Hodge–Dirac operator d+delta_g and its Hodge Laplacian are invariant on ordinary differential forms.

This is a consistent *kinematic restriction* of observable algebra; it is not established as the physical observable algebra of canonical UBT. A candidate Theta master equation using the original omega may not descend to this restricted algebra.

## Result 2: torsion-free uniqueness kills stabilizer deformations

The torsion two-form for omega is T^a=de^a+omega^a{}_b wedge e^b. Under omega->omega+C, at fixed e,

 T'^a - T^a = C^a{}_b wedge e^b.

For invertible e, if both spin connections are metric-compatible and have the same torsion (in particular both torsion-free), then C^a{}_b wedge e^b=0. Writing C_ab=C_abc e^c, Lorentz antisymmetry gives C_abc=-C_bac and equality of torsion gives C^a{}_[bc]=0, i.e. C_abc=C_acb. These two index symmetries imply C_abc=0 (cyclic argument). Therefore C=0.

This is standard uniqueness of a metric-compatible spin connection for fixed e and prescribed torsion. It does NOT show that physical UBT must be torsion-free. The known torsion-free concurrent-vector obstruction for e=DV remains operative in the minimal paired Lorentz branch.

## Result 3: no action-free identification of the two branches

Full connection observables such as F(omega), T(e,omega), holonomy and the second covariant jet of V generally change under stabilizer shifts even when g is unchanged; see sibling audits. Therefore quotienting out C is not a symmetry of *all* covariant observables. It is legitimate only if the physical observable set and field equations factor through the metric quotient or a separate constraint removes dependence.

The metric-quotient route is compatible with differential closure but leaves the connection-selection / Theta-dynamics question unanswered. The full-connection route retains non-metric information and requires independently justified dynamics/constraints; its 12 pointwise stabilizer components are NOT automatically particle modes.

## Research decision / gates

A. **Metric-first conditional programme:** define a projection to g and its unique Levi-Civita differential geometry, then explicitly test whether all accepted UBT field equations descend to this projection. If not, cannot identify C as gauge.

B. **Connection-physical programme:** retain omega curvature and torsion as physical candidates; search for a symmetry, integrability condition or principle selecting their dynamics without tuning an Einstein/Palatini action.

C. **Decision gate:** for an actual source-linked canonical master equation E[Theta,omega], compute E[Theta,omega+C]-E[Theta,omega] with C V=0, including metric, connection and torsion dependencies. If zero identically, metric quotient may be compatible for that equation; if not, retain or constrain C. The project currently has no uniquely selected fundamental master action/equation; do not manufacture one.

Next: perform a fully explicit toy master-equation comparison on a common Minkowski representer; distinguish this proxy from canonical UBT, and verify the transformations analytically. Then inspect exact source equations for the same symmetry.

Status: two exact kinematic lemmas; no unique operator, Einstein dynamics, ghost-free graviton or complete UBT derived.
