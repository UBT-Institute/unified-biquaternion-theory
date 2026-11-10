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

# OI-4: Can an operational information principle determine causality?

**Status (2026-11-10):** restricted finite-graph theorem [STD / elementary mathematics]; physical derivation **OPEN**. This note does not identify information with spacetime, claim a new physical result, or modify UBT canonical claims.

## I. Operational data — BEFORE assigning spacetime

Take a finite labelled set of laboratories/sites `L={1,...,n}`. At each site `i`, an experimenter can choose a setting `x_i` from a finite set `X_i`, and observes an outcome `y_i` in `Y_i`. For a full setting vector `x`, the abstract experimental model supplies normalized conditional distributions

```text
P(y_1,...,y_n | x_1,...,x_n).
```

Settings are taken as independently selectable in this toy model. **This is already a nontrivial intervention/experimental-agency assumption; it is NOT given by a bare information alphabet, and such conditional tables are NOT automatically physically implementable quantum process matrices.**

Define a directional operational dependence relation `R_P`:

```text
i R_P j, i != j
iff there exist settings x_-i and u,v in X_i such that
P(y_j | x_i=u,x_-i) != P(y_j | x_i=v,x_-i)
for at least one outcome y_j.
```

Here `P(y_j|x)` is obtained by marginalizing over all other outcomes. This definition does **not** presume a metric, speed of light, or prior event ordering. It does presume that intervention knobs/sites and joint conditional data are meaningful.

Operational influence `R_P` may be mediated, hidden by destructive interference, absent despite a real directed connection, or dependent on which interventions are allowed. In particular `R_P` need not be transitively closed or acyclic.

## II. Finite graph theorem (not physics)

Let `R` be an arbitrary directed relation without self edges on `L`. Write `R^+` for its transitive closure: `i R^+ j` if a directed path of positive length from `i` to `j` exists.

**Theorem OI-4-T1 [STD].** `R^+` is a **strict partial order** (transitive and irreflexive) **if and only if** the directed graph of `R` has no directed cycles.

**Proof.** By definition of path concatenation, `R^+` is transitive. If `R` has a directed cycle through `i`, then `i R^+ i`, so the closure is not irreflexive. Conversely, `i R^+ i` would exhibit a positive-length directed cycle. Hence irreflexivity of `R^+` is equivalent to acyclicity. QED.

For `R=R_P` this gives a **conditional operational order**. The theorem does not show that (a) nature enforces acyclicity, (b) the operational order coincides with ontic chronology, (c) sites with no measured influence are spacelike, (d) transitive paths are physically observable end-to-end, or (e) a continuum Lorentz metric exists.

## III. Three countermodels (why stronger axioms are necessary)

**C1 — full distinguishability with no intersite order.** Two bit labs with settings `x_A,x_B` and outcomes `y_A=x_A, y_B=x_B`. Every local setting is distinguishable; `R_P` has no directed edge. This can describe separately operated labs or chronologically ordered labs whose available communication link is unused. Same operational data, different possible underlying orders. Hence local information alone does not uniquely fix causal embedding.

**C2 — two-way conditional dependence.** Abstract deterministic table `y_A=x_B, y_B=x_A` has `A R_P B` and `B R_P A`. Thus the operational graph has a cycle. This is a *mathematical conditional table only*: it is not asserted to be implementable by ordinary, definite-order, independently chosen physical laboratories or to be a valid quantum process matrix. It disproves a deduction of acyclicity from mere normalization of conditional probability distributions.

**C3 — cancellation / causal unfaithfulness.** Consider structural equations `b=a` and `c=a XOR b XOR x_C`, where `a=x_A`. A structural model could have directed edges `A->B`, `B->C`, `A->C` yet the actually observed `c=x_C` has no marginal dependence on `x_A`. A directed physical path therefore need not imply detectable end-to-end signalling; inferring actual causal structure from `R_P` additionally needs suitable interventions, exclusion of fine-tuned cancellations, or an explicit faithfulness-type assumption.

## IV. Status of the conceptual information -> causal arrow

The graph theorem demonstrates only:

```text
operational interventions + conditional probabilities
       -> measured influence relation R_P
       + [INDEPENDENT acyclicity axiom]
       -> transitive closure R_P^+ is a strict partial order.
```

A partial order is much weaker than a spacetime geometry. Inferring metric cones would still require strong continuum, dimensional, locality and regularity hypotheses. In the other direction, **absence of signalling does not imply absence of a possible causal relation**.

For genuine indefinite-causal-order quantum models see Oreshkov, Costa & Brukner, *Quantum correlations with no causal order*, Nature Communications **3**, 1092 (2012), https://doi.org/10.1038/ncomms2076 . Their valid quantum process formalism is **not** represented by C2's arbitrary classical table, and the finite theorem here is independent of their result.

## V. Next falsifiable / formal work

- **OI-4-G1:** identify a physically meaningful, experimentally operational family of local interventions that is not implicitly defined using pre-existing global time or spacetime.
- **OI-4-G2:** characterize extra constraints on `P(y|x)` that enforce a DAG **without** simply naming acyclicity or assuming an ordered circuit.
- **OI-4-G3:** test when measured influence can distinguish causal adjacency, mediators and hidden connections; compare coarse-graining, cancellation, hidden variables and interventions.
- **OI-4-G4:** examine alternative generalized-quantum-process / indefinite-order branch; do not rule it out just to obtain Lorentz geometry.
- **OI-4-G5:** only after operational-order selection, determine necessary and sufficient additional assumptions for a continuum Lorentzian 3+1 limit, keeping the dimension selection gap OI-5 explicit.

## Reproduction

```sh
python3 research_tracks/ontological_information_axioms/verify_operational_order.py
```

The script enumerates all 64 loop-free directed graphs on three labelled sites (25 acyclic graphs and 19 distinct strict partial orders from their closures) and tests the explicit finite conditional-table examples. These finite counts verify the **combinatorics**, not any emergent-physics claim.
