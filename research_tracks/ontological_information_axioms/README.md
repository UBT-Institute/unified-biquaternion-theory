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

# Ontological and Information Axioms: Reverse Engineering UBT

**Status:** OPEN research track — alternative foundational programmes, not a canonical derivation.  
**Opened:** 2026-11-10.  
**Scope:** Work backwards from operational facts to conditions under which spacetime, quantum theory, dynamics, and the UBT algebra could be *selected*, instead of being presupposed.

## Motivating heuristic (not a physical premise)

The three-stage narrative in Genesis 1:1–3 suggests an evocative *ordering of questions*: existence; an initially undifferentiated potential; and the appearance of distinctions ("let there be light"). This is a philosophical analogy only. **No biblical text, creator, ideal observer, or metaphysical assertion is a physics axiom or evidence of UBT.** The temporal/exegetical interpretation of the passage is not needed for any result here. Keep such material out of `canonical/` and physics theorem statements.

Research question: **what minimal non-circular premises imply the mathematical structures underlying empirically validated physics?** Each proposed step must say exactly what has been assumed.

## Three competing entry points (do not silently combine assumptions)

1. **O — existence-first:** assume only a nonempty set of possible states `S`. Ask what, *if anything*, follows without primitive time, space, field or scalar numbers. By itself this is too weak to pick a physical theory.
2. **I — information-first:** assume operationally distinguishable preparations and outcome statistics. Define `s ~ t` iff every permitted experiment gives identical outcome distributions. Study the quotient `S/~` and composition of experimental systems. An information measure requires additional probabilities/structure; it is not created by the word “information”.
3. **C — causal-first:** separately posit a set of events `E` with an acyclic/transitive causal order `≺` (or explicitly justify why a different relation is chosen). Ask which regularity, dimension, measure and continuum hypotheses permit reconstructing Lorentzian spacetime. Causal order **cannot be inferred from distinguishability alone** without a bridge axiom.

A fourth **observer-relative consistency test** may be attached to any entry point: many observers can have different accessible sigma-algebras/outcomes; compare their compatible public records. Do **not** assume their underlying realities must be identical or different. An ideal all-knowing observer is a mathematical limiting construct, not a physical entity or theological claim.

## Conditional reconstruction ladder

```text
possible states / operations [proposed]
          | additional testable axioms required
          v
operational distinctions + composition [proposed]
          | independent locality / signaling or causal axiom required
          v
causal events and order [assumed unless derived]
          | continuum + distinguishing spacetime + regularity
          v
conformal Lorentzian metric class [standard theorem, conditional]
          | independent volume data / normalization
          v
metric scale [standard reconstruction, conditional]
          | select matrix/spinorial representation
          v
Herm(2,C) ↔ R^(1,3); C⊗H ≅ M_2(C) [standard algebra]
          | fundamental action / probability law / spectrum
          v
classical + quantum + gauge dynamics [OPEN]
```

**Standard result, not a UBT discovery.** For an appropriate future-and-past-distinguishing Lorentzian spacetime of dimension >2, chronological order determines its conformal metric class (HKMM/Malament). A compatible volume measure fixes the conformal factor under additional assumptions. This **does not** produce the order from information, select four dimensions, or derive Einstein's equations. In the causal-set programme the related heuristic is "order + number = geometry" in a suitable continuum approximation, *not* for arbitrary posets.

**Standard algebra, not a uniqueness theorem.** For Pauli matrices `σ_i` and real `x^μ`,
`X = x^0 I + Σ_i x^i σ_i ∈ Herm(2,C)` has
`det X = (x^0)^2 − Σ_i(x^i)^2`. The action `X -> A X A†`, `A∈SL(2,C)`, preserves this quadratic form. Also `C⊗H ≅ M_2(C)`. This demonstrates a **compatible representation after choosing Herm(2,C)**, not a derivation of that choice or of spacetime dimension. Compare odd/even/full Clifford representations explicitly before asserting selection.

## First countermodel: why existence + distinctions are insufficient

Both (a) a classical bit with distinguishable values 0/1 and (b) a qubit with at least two distinguishable orthogonal states satisfy the minimal premises "nonempty state set + existence of a distinguishing experiment". Their composition laws, interference structure, and continuous state spaces differ. Neither premise fixes a Lorentzian metric, a signal speed, 3+1 dimensions, or a unique algebra. Consequently all selection claims remain **OPEN** until stronger axioms are stated and non-target models excluded.

## Information thermodynamics

Landauer's bound concerns physical logically irreversible information erasure (under specific thermodynamic conditions); it is **not** a general cost for creating distinctions, and cannot be used to derive Einstein gravity or irreversible time evolution without a model. Specify operations, entropy definition, bath/temperature and reversibility before attempting any connection with gravitational dynamics.

## Targets and strict gates

| Gate | Question | Minimum completion evidence |
|---|---|---|
| G0 | Are axioms independent, non-circular, and operational? | Formal definitions; countermodels for each dropped axiom |
| G1 | Can causal order emerge, rather than being postulated? | Explicit construction and proof; no imported metric/light cones |
| G2 | Why Lorentzian 3+1, and not other signatures/dimensions? | Uniqueness or conditional selection theorem with alternatives |
| G3 | Why `C⊗H` rather than `M_n(C)`, real, odd or full Clifford? | Comparison and an independently motivated selector |
| G4 | Why quantum probability/composition/measurement? | Reconstruction or explicit incompatibility/no-go |
| G5 | Can action and GR/SM sectors be derived ghost-free? | Constraints/Hamiltonian DOF, appropriate GR/SM limits |
| G6 | What distinguishes this route empirically? | Parameter-independent quantitative prediction or falsification |

**Success cannot mean merely recovering GR.** The full target is compatibility with *all established domains* of physical theory (including appropriate quantum/SM and thermodynamic limits), while clearly marking presently uncovered regimes.

### Neighbouring repository work

- `canonical/geometry/biquaternion_dirac_lift.tex`: established algebraic Clifford lift within prior UBT definitions — not a derivation of those definitions.
- `canonical/gr_closure/`: rank-ten metric map and conditional Einstein/Palatini paths; action-selection gaps remain.
- `research_tracks/gray_transport_layer/`, `research_tracks/information_probes/`: observational/coding diagnostics, not foundational axiom proofs.
- `speculative_extensions/`: appropriate home for substantive metaphysical interpretation; this track keeps only an explicitly labeled historical analogy.

**First formal work package OI-4 (2026-11-10):** [Operational causality theorem, explicit countermodels and limits](OI4_OPERATIONAL_CAUSALITY.md) plus [finite verifier](verify_operational_order.py). The conditional statement “acyclic operational influence graph → strict partial order by transitive closure” is elementary [STD]. Operational distinguishability does **not** imply acyclicity or identify physical spacetime order. Run `python3 research_tracks/ontological_information_axioms/verify_operational_order.py` (five tests).
 
**OI-4 second work package (2026-11-10):** [Universal consistency versus definite causal order](OI4_CONSISTENCY_VS_ORDER.md), verified by [standard-library script](verify_consistency_vs_order.py). Its two contrasting results are an elementary fixed-wiring DAG iff universal-uniqueness theorem and the **published counterexample** of the logically consistent, noncausal three-party Lugano process. Pairwise exclusivity of complete deterministic events characterizes universal fixed-point uniqueness (published 2026 result). Neither the unconditional information-to-causality bridge nor 3+1 Lorentz geometry is derived. 
   
See [PROOF_STATUS.md](PROOF_STATUS.md) and [AXIOM_MATRIX.md](AXIOM_MATRIX.md).

## Relevant standard references (background, not UBT validation)

- D. B. Malament, *The class of continuous timelike curves determines the topology of spacetime* (1977); causal reconstruction theorem reviewed in [Surya, Living Reviews in Relativity (2019)](https://doi.org/10.1007/s41114-019-0023-1).
- [Surya, *The causal set approach to quantum gravity* (2019)](https://doi.org/10.1007/s41114-019-0023-1).
- [Einstein Online, *Geometry from order: causal sets*](https://www.einstein-online.info/en/spotlight/causal_sets/).
- [Baez & Huerta, *Division Algebras and Supersymmetry II*](https://math.ucr.edu/home/baez/susy2_1.pdf) — standard Hermitian-matrix / Minkowski form correspondence.
