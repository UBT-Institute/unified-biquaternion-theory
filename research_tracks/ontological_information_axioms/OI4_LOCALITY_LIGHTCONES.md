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

# OI-4D: Exact information cones from finite local updates

**Status:** elementary [STD] conditional mathematical results and finite reproducible tests. **Not** a derivation of relativistic light speed, emergent Lorentzian geometry, UBT dynamics or information-theoretic gravity. Date: 2026-11-11.

## 1. Minimal model: events, updates, operational influence

Choose a finite directed spatial-dependency graph `G=(V,E)`; `u->v` means a local update at v is permitted to read the previous-step state of u. Assign a finite local state alphabet `S_v`. **Explicitly assume an integer update index** `t=0,1,...` and local update maps
```text
s_v(t+1) = F_{v,t}(s_v(t), (s_u(t))_{u in Pa(v)}, eta_{v,t}).
```
The noise variables `eta`, if any, have a joint distribution independent of a setting/intervention at initial site `u`. We compare two evolutions with identical initial states away from u and the same realization of all noise. This is an intervention ("do"), not conditional correlation due to a shared cause.

Define the backwards influence set `B_0(v)={v}` and
```text
B_{k+1}(v) = union_{w in {v} union Pa(v)} B_k(w).
```
Equivalently, `B_k(v)` is the set of vertices with a directed path of at most k spatial edges to v; the explicit self input permits waiting between arrivals.

## 2. Exact finite propagation theorem

**OI-4-T4 [STD, conditional].** If two initial configurations agree at every site in `B_k(v)`, and the same noise realization is used for both, then the outcomes at `v` after k local update steps are identical:
```text
s_v(k) = s'_v(k).
```
In particular, an intervention on u at t=0 cannot change the probability distribution at v at step k whenever `u notin B_k(v)` (given intervention-independent shared noise). More generally, all observables supported on a target set T at time k depend only on the union of its backwards influence sets.

*Proof.* Base k=0: the result is equality of the initial state at v. Inductive step: the update at v for k+1 reads only values at w in {v} union Pa(v) at k and the same noise. Agreement of initial data on B_{k+1}(v) implies agreement on every B_k(w), so by induction all inputs and outputs at v agree. Equality under a common coupling implies equality of marginal distributions. QED.

**OI-4-T5 [STD, sharpness in an existential model].** When each local alphabet contains {0,1}, choose
```text
s_v(t+1) = OR_{w in {v} union Pa(v)} s_w(t).
```
From an isolated unit bit at u, one has `s_v(k)=1 iff u in B_k(v)`. This follows by the same path recursion and proves that the finite influence bound can be *saturated*, although arbitrary dynamics may be strictly slower or cancel influence.

**Important:** We have *assumed* local dependencies and a universal tick index. The theorem converts these assumptions into a causal cone; it does not derive locality, direction of physical time, universal tick duration or 3+1 spacetime from abstract information.

## 3. Why this is not Einstein's light cone

- **Graph cones are not necessarily Lorentzian.** On a 2D square lattice with nearest four neighbors, the two-tick forward cone has cross-section `|x|+|y|<=2` (13 vertices). With all eight nearest neighbors it is `max(|x|,|y|)<=2` (25 vertices). Both satisfy exactly the same kind of local information/no-signalling theorem. One has diamond-shaped and the other square-shaped planar fronts. The precise cone is selected by the **graph topology and update rule**, not by information consistency alone.
- **No absolute speed is fixed.** If an edge has spatial length at most `a`, and a step lasts `Delta t`, the triangle inequality bounds Euclidean displacement by `a*k` after k steps, hence `v_max <= a/Delta t`. This becomes a numerical speed only *after independently specifying the metric embedding and clock calibration*. In some directions the bound is not saturated.
- **No boost symmetry has been derived.** A fixed-time spatial grid typically singles out a frame. A continuum limit and further symmetry/scale conditions would be necessary to approach a Lorentz-invariant signal cone. One cannot identify `a/Delta t` with the observed invariant vacuum light speed `c` by definition and then report an independent derivation of `c`.
- **Cycles in the spatial graph are not time-travel paradoxes.** The time-unrolled influence graph contains edges only `(u,t)->(v,t+1)` and is automatically acyclic. That DAG structure is inherited from the *assumed step index*, rather than derived from logical consistency (see OI-4B's Lugano counterexample).
- **If the graph has all-to-all edges**, a local-in-the-given-graph update can broadcast information everywhere in one tick; finite **spatial** propagation needs a separately motivated graph embedding, controlled degree/interaction range, or analogous locality assumption.

## 4. Standard related results, not UBT discoveries

- Quantum lattice systems: finite-range / sufficiently decaying interactions lead to **Lieb-Robinson bounds** on information/correlation spreading. Unlike the exact finite-step support statement above, continuous-time Lieb-Robinson bounds generally allow exponentially small tails beyond an effective cone. Wilming & Werner (2022), [Phys. Rev. B 105, 125101](https://doi.org/10.1103/PhysRevB.105.125101); Wang & Hazzard (2020), [PRX Quantum 1, 010303](https://doi.org/10.1103/PRXQuantum.1.010303).
- Discrete quantum cellular automata may reproduce relativistic field equations in suitable continuum limits while retaining possible high-energy anisotropy or Lorentz-violation effects. Mlodinow & Brun (2025), [Phys. Rev. D 112, 074513](https://doi.org/10.1103/5w6s-jr1d).
- Causal-set reconstruction uses causal order **plus counting/volume and manifoldlikeness assumptions**; it does not reconstruct all smooth geometry from arbitrary finite DAGs. See [On the Growing Universe of Causal Set Theory (2024)](https://doi.org/10.1007/s10701-024-00767-5).

## 5. Reproducible checks

Run from the repository root:
```sh
python3 research_tracks/ontological_information_axioms/verify_finite_lightcones.py
```

Six standard-library tests verify a directed chain's minimum arrival time; spatial cycles with acyclic *time-unrolling*; sharp propagation by a Boolean OR update; 2D 13-versus-25 cross-section countermodels; an exact intervention/noise coupling test exhaustive over 3 binary nodes and two updates; and all-to-all one-tick broadcast. **6/6 passed in local Python 3 execution on 2026-11-11**. These tests validate the finite-model mathematics only.

## 6. UBT research implications and next proof obligations

Current UBT canonical geometric objects such as `E_mu=D_mu Theta/sqrt(N0)`, the central anticommutator metric, and the biquaternion/Clifford lift are **not selected** by the theorem. We must not insert them into assumptions and claim reconstruction.

| Gate | Status | Required outcome |
|---|---|---|
| OI-4-L1 | [STD] conditional CLOSED | Finite propagation from *assumed* local updates and discrete ticks |
| OI-4-L2 | [STD] countermodels CLOSED | Neither unique cone geometry nor numerical speed follows from generic finite locality |
| OI-4-L3 | **OPEN** | Information principle that independently selects a locality relation or interaction decay |
| OI-4-L4 | **OPEN** | Selection of continuum dimension/signature and emergence of approximate/exact local Lorentz invariance |
| OI-4-L5 | **OPEN** | Operational observables and a stable UBT action connecting reconstructed causal geometry to Theta dynamics and GR/QFT |

**Next falsifiable experiment:** replace the square-grid geometry with competing graph families and update kernels; quantify directional front speed vs lattice scale and whether anisotropy vanishes under a *justified* continuum/renormalization limit. Preserve counterexamples: if coarse-graining does not restore isotropy, the proposed geometry selector is inadequate.
