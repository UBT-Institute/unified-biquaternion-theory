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

# OI-4B — Does universal information consistency imply causal order?

**Status:** first-principles emergence of causal geometry **OPEN**. The finite results below are elementary mathematical exercises / reproductions of published process-function work. In particular, **general logical consistency does not imply a fixed global acyclic causal order**. No claim of original discovery, spacetime derivation, physical realizability of a time machine, or closure of GR dynamics.

## 1. Two DIFFERENT models of information composition

**Model W (fixed wiring).** Given a finite directed graph `G=(V,E)`, put one bit `z_v` at each node and allow *every* local deterministic Boolean update rule

```text
z_v = f_v( (z_u)_{u in Pa(v)} ).
```

The parent sets `Pa(v)` are fixed by the graph, but each local rule can ignore any of its permitted incoming edges, copy a selected input, invert it, or be constant. This is a very strong *independent local mechanism freedom* assumption. A global state is a simultaneous fixed point of all equations. "Universal deterministic consistency" (UDC-W) means that **every** profile of local rules has exactly one simultaneous solution.

**Model P (process functions).** The experimenter controls independent local operations `f_i : I_i -> O_i`; a global environment `w : product_i O_i -> product_i I_i` converts outputs to incoming symbols. Physical models in this formalism ask that for *every* local operation profile, the feedback condition

```text
i = w(f_1(i_1), ..., f_n(i_n))
```

has exactly one solution (deterministic case). Unlike Model W, the environment is a **single global map** whose influence can depend on *other sites' output values*. Thus cyclic *potential-dependency* diagrams need not represent a permanently activated feedback circuit.

Model P is the literature's classical deterministic process-function setting; it is not a generic implementation of UBT.

## 2. Restricted theorem: fixed-wiring universality selects DAGs

**OI-4-T2 [STD, elementary conditional].** For any finite directed graph with no self-edges and Boolean site variables, UDC-W holds **iff** `G` is a directed acyclic graph (DAG).

*Proof, DAG -> UDC-W.* Choose a topological ordering of the finite DAG. All parents of a node precede it. The sources have functions of zero inputs, i.e. constants; their bits are fixed. Evaluating downstream local rules recursively produces one global state. Any solution must agree at each successive step, so the solution is unique.

*Proof, UDC-W -> DAG.* Suppose `G` contains a directed simple cycle `v_1 -> v_2 -> ... -> v_k -> v_1`. Choose `f_{v_j}` to copy the predecessor on the cycle for `j>1`; choose `f_{v_1}` to flip the predecessor. Ignore all other incoming edges and choose constant functions outside the cycle. A fixed point would imply `z_{v_1}=NOT z_{v_1}`, contradiction. Thus UDC-W fails. QED.

**Scope limitation:** we needed *arbitrary independently selectable functions over a fixed dependence graph*, as well as simultaneous Boolean equations and a unique-global-solution requirement. These requirements are extra physical premises; no one has derived them here from bare existence or distinguishability. Temporal feedback in an ordinary delayed dynamical circuit can be treated by expanding nodes into separate time-indexed events; the theorem must not be invoked to forbid physical feedback.

## 3. General model P supplies a decisive counterexample

Take the known **tripartite Lugano process** (notation `o=(a,b,c)` for outgoing bits):

```text
w_A(o) = (NOT b) AND c
w_B(o) = (NOT c) AND a
w_C(o) = (NOT a) AND b.
```

Every pair of parties can potentially influence one another as the third party's value varies. Its aggregated potential-dependency graph therefore has **all six edges** among three sites and is cyclic. Nevertheless, direct enumeration finds that each of the **4^3 = 64** profiles of one-bit local deterministic maps has **exactly one** consistent global fixed point. This is a standard studied example of a logically consistent process without a fixed causal order. The result is not incompatible with OI-4-T2 because **Lugano is not the freely selectable fixed-wiring Model W**.

This is the crucial *no-go for the naive axiom*: `universal logical consistency -> acyclic dependency structure` is false once we admit more general process functions. We must not replace "information" by "DAG" as a hidden new axiom and claim to have derived relativity.

References:
- Baumeler, Feix & Wolf (2014), *Maximal incompatibility of locally classical behavior and global causal order in multiparty scenarios*, [Phys. Rev. A 90, 042106](https://doi.org/10.1103/PhysRevA.90.042106).
- Baumeler & Wolf (2016), *The space of logically consistent classical processes without causal order*, [New J. Phys. 18, 013036](https://doi.org/10.1088/1367-2630/18/1/013036).
- Dourdent et al. (2026), *What makes a causal loop consistent?*, [arXiv:2609.39735](https://arxiv.org/abs/2609.39735) — preprint, not an established UBT result. Introduces a complete event-based consistency characterization for deterministic classical single-round processes.

## 4. Stronger event-level constraint: pairwise exclusivity

For a deterministic finite process `w`, take its complete event list

```text
H(w) = { (o, w(o)) : o in product_i O_i }.
```

Two distinct events `(o,w(o))` and `(o',w(o'))` are **exclusive** if **some** party `i` receives the *same* input in both events but would have to produce *different* outputs:

```text
exists i : w_i(o) = w_i(o') AND o_i != o'_i.
```

In that case no single deterministic local function `f_i` can realize both events.

**OI-4-T3 [STD, rederivation of published 2026 criterion in finite deterministic setting].** Universal unique-fixed-point consistency for `w` under all independently selected deterministic local operations is equivalent to *pairwise exclusivity of its complete event list*.

*Proof of necessity.* If a pair is not exclusive, whenever two events have equal local inputs they must prescribe equal local outputs. Thus we can define each `f_i` consistently on those at-most-two specified inputs so that **both** events become fixed points, contrary to uniqueness.

*Proof of sufficiency.* Pairwise exclusivity forbids two distinct fixed points for any local maps, so there is at most one. Choose all local functions uniformly at random over finite function sets. For each fixed output tuple `o`, the chance that `f_i(w_i(o))=o_i` for all sites is `1 / product_i |O_i|`. There are exactly `product_i |O_i|` such tuples, so the **expected** number of fixed points is exactly 1. Since every local-function profile has either 0 or 1 fixed point, expectation 1 forces **exactly one for every profile**. QED.

This finite counting proof is included for clarity. **Credit belongs to the existing process-functions literature**, especially the 2026 event formulation. For general stochastic/quantum maps, further normalization, positivity and operational assumptions are needed.

**Lugano passes the event-pair criterion** despite having cycles in its aggregated potential-dependency diagram. Therefore consistency and event exclusivity are *strictly weaker* than a selection of a single global causal DAG in the general process setting.

## 5. Reproducible computational check

Run from repository root:

```sh
python3 research_tracks/ontological_information_axioms/verify_consistency_vs_order.py
```

Local run on 2026-11-10: **5 tests passed** (Python standard library). Enumerations:
- 64 loop-free directed graphs on three labelled vertices: 25 DAGs / 39 cyclic;
- all **17,576** fixed-wiring local Boolean rule profiles across those graphs; the DAGs have universal unique solutions, every cyclic graph admits a failure;
- profile-wide distribution of fixed-point counts: 0: 2,902; 1: 11,832; 2: 2,784; 3: 56; 4: 2;
- Lugano: 64/64 local function profiles have a unique fixed point; the aggregate potential-dependency graph has 6 directed edges and cycles;
- pairwise exclusivity passes for Lugano and fails for a simple 2-node identity feedback ring.

Finite enumeration validates the scripts' scope and these combinatorial claims, **not physical realizability, novel predictions, quantum dynamics, or emergence of 3+1 spacetime**.

## 6. Implications for UBT and precise next gates

**G-OI4-2A (closed only within Model W):** Theorem T2 explains why universal freedom over *fixed wiring* rules rules out feedback cycles. It does not justify fixed wiring as a law of nature.

**G-OI4-2B (general no-go, standard literature):** Consistency/exclusivity does **not** imply a globally definite causal order for general classical process functions. The strongest version of "information consistency alone derives causality" is untenable in this class.

**G-OI4-2C (OPEN):** Find an independently motivated additional selector (e.g. specific physical composition rules, locality, stability under a precisely defined perturbation class, causal inequalities, or an emergent effective-time regime) that prefers an experimentally consistent Lorentzian causal structure **without baking in its conclusion**. Compare against Lugano and general quantum-process counterexamples.

**G-OI4-2D (OPEN):** Construct an observer-relative event algebra carrying information constraints; identify why its permitted global gluing should yield 3+1 conformal geometry rather than a generic causal partial order or generalized noncausal process. Preserve the difference between an observer's information and the ontology of the full process.

**G-OI4-2E (OPEN):** Only after the causal/geometry gap is closed, seek a genuinely noncircular `C⊗H` selector, a `Theta` field, a local stable action and the appropriate GR+SM+quantum limits. Do not claim Landauer cost or Fisher information already solves these gaps.

**Research status:** no promotion to `canonical/`; no new claim in `WHAT_IS_PROVED.md`.
