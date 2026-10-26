<!-- BILINGUAL-UNIT: proposition9_volume_overlap_audit -->
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


# Action-selection cross-check: Proposition 9 already subsumes vector volume collapse

**2026-10-25 — source reconciliation, not a new theorem. C-tier working note.**

## Established result already on master

`research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md`, Proposition 9, proves for its precisely stated timelike Lorentz-real, independent auxiliary SL(2,C) connection and composite-metric minimal kinetic/potential family:
```
B(D_mu X,D_nu X)=-2 N0 g_mu nu;
g^{mu nu} B(D_mu X,D_nu X)=-8 N0;
S_min = int d4x sqrt(-g) [4 c N0 - U(rho)].
```
It also proves the nondegenerate tetrad no-go for the specified nonconstant quartic U and the auxiliary boost-connection variations, with a checked verifier `tools/verify_theta_composite_volume_no_go.py`. The canonical registry `canonical/ACTION.en.md` explicitly records this conditional result, without promoting the minimal family into a finalized S_UBT.

## Avoid duplicate theorem or normalization confusion

`composite_metric_kinetic_volume_identity.en.md` in this PR treats another expressly chosen vector pairing with contraction `g^{mu nu} eta_ab D_mu V^a D_nu V^b = 4 N0`. This agrees structurally with Proposition 9 but is not identical to its Lorentz-invariant matrix polarization B, whose contraction is `-8 N0`. Do not infer a contradiction: pairing and prefactors are different. Proposition 9 is the **stronger existing source** for that specific timelike action; the draft note adds no independent action-level no-go.

## Exact distinction from transverse-contortion stabilizer

On the canonical Gaussian reconstruction, shifts C with C^a_(mu b) V^b=0 leave the vector carrier D V, tetrad and central composite metric invariant. Thus any action depending only on their metric/volume does not distinguish such shifts. This is compatible with Proposition 9, which independently shows that the minimal timelike branch with a nonconstant polynomial potential and freely varied auxiliary boosts cannot admit a nondegenerate stationary tetrad.

Neither result establishes permission to add an *arbitrary* curvature term under the locked axioms. An acceptable new dynamical sector must be selected from the one-Theta programme, not appended to evade a no-go after the fact.

## Actual next research target

Instead of rerunning the volume identity, find an already justified, **non-volume**, Theta-only invariant with fully specified sharp/ddagger pairing and composite connection. Exhibit a nonzero gauge-reduced kinetic principal symbol (or explain why none can be derived), determine the action-level compatibility with the 12-dimensional stabilizer, and verify how Hamiltonian constraints close. If no such selection follows from the locked definitions, record underdetermination rather than claiming closure.

**Source precedence:** canonical/ACTION.en.md and its Proposition-9 source on master supersede narrower duplicate exploratory notes; no canonical file or axiom changed.
