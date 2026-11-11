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

# OI-4D — Local information cones and finite-stencil anisotropy

**Status:** mathematical results [STD], physical emergence [OPEN]. No new canonical UBT physics is claimed.

## Operational assumptions

Let a finite graph specify which preceding-node states can affect a local state update. Each node also reads its own preceding state. We assume a shared discrete update index and noise independent of an initial intervention. These assumptions are not consequences of information distinguishability alone.

$$
s_v(t+1)=F_{v,t}(s_v(t),(s_u(t))_{u \in Pa(v)},\eta_{v,t}).
$$

Define the backwards influence set by a graph recursion:

$$
B_0(v)=\{v\}, \quad B_{k+1}(v)=\bigcup_{w\in\{v\}\cup Pa(v)}B_k(w).
$$

## Exact finite propagation — OI-4-T4

**Conditional theorem [STD].** If two initial configurations agree on the backwards influence set of a target, identical local rules and a common noise realization give the same target value after the corresponding updates.

**Proof.** By induction on update steps. At the initial step the target values coincide. At each subsequent step the target reads only its own preceding value and values at its permitted predecessors. The recursive backwards set contains every relevant earlier input. Inductive equality of the inputs and shared noise imply equality of the output. A coupling argument gives equality of interventional marginal distributions.

## Saturation — OI-4-T5

**Construction [STD].** For Boolean sites choose the OR of the local input bits, including the previous local bit. A single active source bit reaches exactly those target sites connected by a path of at most the specified number of update steps. Thus the bound is sharp for this rule. Other rules may cancel transmission or propagate more slowly.

## Finite-direction isotropy obstruction — OI-4-T6

Suppose the allowed one-step spatial displacements form a fixed finite stencil in a Euclidean plane, with translation-invariant, synchronous steps. The convex hull of reachable net displacements after repeated steps and its directional support satisfy

$$
\operatorname{conv}(D^{\oplus k})=k\operatorname{conv}(D), \quad h_k(n)=k\max_{d\in D}n\cdot d.
$$

**Conditional theorem [STD].** A nontrivial fixed finite stencil has a polygonal maximal-reachability front. This cannot be exactly invariant under every continuous spatial rotation. A nontrivial rotation-invariant compact convex body is a disk, which cannot have only finitely many extreme vertices. The convex hull identity follows from repeated Minkowski addition. This proves the stated obstruction for maximal support, not for every possible effective field propagation law.

## Countermodels, checks and limitations

A cardinal-neighbor square lattice has **13** reachable sites after **2** steps; an eight-neighbor lattice has **25** after **2** steps. The first stencil has axial support **1** and diagonal support **1/sqrt(2)**; the second has **1** and **sqrt(2)**. Hence a common local-information principle does not uniquely determine a Euclidean or Lorentzian signal cone.

Run the standard-library script at research_tracks/ontological_information_axioms/verify_finite_lightcones.py . **8/8** tests passed locally on **2026-11-11**. The script checks graph support, saturation, time-unrolled feedback, shared-noise intervention cases and anisotropic directional front bounds.

A spatial velocity bound requires independent clock and distance calibration. No invariant vacuum light speed, Lorentz symmetry, spacetime dimension, quantum probability law, UBT action or Einstein equation has been derived. Those questions remain [OPEN].

## Related work

Wilming and Werner, *Physical Review B* **105**, 125101 (2022): https://doi.org/10.1103/PhysRevB.105.125101 .

Mlodinow and Brun, *Physical Review D* **112**, 074513 (2025): https://doi.org/10.1103/5w6s-jr1d .
