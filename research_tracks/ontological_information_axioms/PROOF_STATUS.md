<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# Proof status — ontological/information axioms

**Overall:** OPEN. This track currently makes **no new proved UBT first-principles physical claims**. The distinction between textbook identities, conditional external theorems, and conjectural UBT bridges is mandatory.

| ID | Statement | Status | Dependence / gap |
|---|---|---|---|
| OI-0 | Nonempty state set plus a possible distinction does not uniquely fix physical kinematics | Elementary underdetermination / countermodels | Classical bit vs qubit (see README); no choice of composition, causality, dimension |
| OI-1 | Distinguishing causal order determines conformal class in appropriate Lorentzian spacetimes | [STD], conditional | HKMM/Malament; Lorentzian manifold already assumed |
| OI-2 | Conformal structure + compatible volume element fixes metric scale | [STD], conditional | Smooth continuum and measure assumptions |
| OI-3 | `Herm(2,C)` determinant has signature (+---) | [STD/L0 algebra], representation chosen | Pauli matrices; does not single out `C⊗H` physically |
| OI-4 | Distinguishability implies intrinsic causal ordering | [OPEN] | No unconditional derivation; operational influence is neither automatically acyclic nor a complete account of ontic order |
| OI-4-T1 | For any finite directed R, its transitive closure R+ is a strict partial order iff R is acyclic | [STD] elementary theorem | [OI4_OPERATIONAL_CAUSALITY.md](OI4_OPERATIONAL_CAUSALITY.md); finite n=3 check in [verifier](verify_operational_order.py) |
| OI-4-N1 | Normalized finite intervention tables need not yield a strict operational order; operational data do not uniquely determine underlying causal embedding | [STD] elementary countermodels (within toy assumptions) | Bidirectional table and unused links; **not** a new fundamental physics theorem |
| OI-5 | Operational principles uniquely select 3+1 Lorentz geometry | [OPEN] | Countermodels of alternate dimensions/signatures |
| OI-6 | Operational principles select `C⊗H` over alternate Clifford/matrix systems | [OPEN] | Need minimal faithful-selector theorem, not a matching identity |
| OI-7 | Thermodynamic information principles generate UBT field action and constants | [OPEN] | Erasure vs measurement, state dynamics, UV/IR and stability |
| OI-8 | One observer-consistency principle yields the quantum measurement rules | [OPEN] | Specify observer records and composition; exclude hidden imported Born rule |
| OI-9 | Full GR, quantum field theory, and SM spectra follow from the minimal programme | [OPEN] | Local constraints, matter representations, anomaly cancellation, empirical agreement |

## Non-circularity requirements

- Never infer light cones from a relation already defined by signal travel in a given Lorentz metric, then claim to have derived Lorentz signature from scratch.
- Never insert dimension `4` via `Herm(2,C)` and subsequently call the number of dimensions a prediction.
- Never identify algebraic compatibility with physical necessity.
- Never use entropy/information without an operational measure and ensemble.
- Never upgrade [STD] or a toy calculation to a proven UBT claim.
- Keep competing axiom routes independently reproducible and publish the failed routes as no-go results.

## First work package

1. Write operational event/test axioms with explicit independence table.
2. Construct finite counterexamples to uniqueness, including classical probability and qubit models.
3. Distinguish primitive causality from inferred signalling and from postulated locality.
4. Study dimension-selection claims versus `Herm(n,C)`, Clifford-even, odd and full modules.
5. Connect the least-assumptive surviving route to `Theta` geometry and Hamiltonian action audits; do not assume an action before this step.
6. Record a falsifier or concrete proof obligation for every surviving bridge.

**Promotion:** Only after mathematical closure, independent checks, and compatibility with canonical GR + quantum/SM constraints under the repository's normal criteria.
