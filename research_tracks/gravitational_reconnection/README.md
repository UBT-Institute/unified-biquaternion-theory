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

# Gravitational reconnection and Theta geometry

**Status:** OPEN — non-canonical research proposal (2026-11-20)  
**Confidence:** Open; external GR comparator is peer-reviewed; no UBT-specific reconnection result established  
**Canonical impact:** none  
**Research question:** Can the tetrad induced by the UBT field `Theta` support a geometrically meaningful analogue of gravitational field-sheet transport/reconnection, without confusing tetrad-frame artefacts with observables?

## Primary references

1. L. Comisso and F. A. Asenjo, *Reconnection of Gravitational Fields*, **Phys. Rev. D 114, 084095** (2026), DOI: https://doi.org/10.1103/lmqy-pf9k ; preprint https://arxiv.org/abs/2609.25241 .
2. F. A. Asenjo, M. A. Winkler and L. Comisso, *Frozen-In Gravitational Fields*, **Phys. Rev. Lett. 136, 161401** (2026), preprint https://arxiv.org/abs/2609.25240 .
3. Popular-science prompt: https://www.nationalgeographic.cz/veda/gravitace-se-muze-pretrhnout-jako-pole-na-slunci/ .

## What the published GR comparator establishes

In a tetrad formulation of GR, an ideal Ohm-type condition permits conserved gravitational flux and transport of gravitational field sheets. The cited reconnection paper studies failure of ideal frozen-in evolution, defines reconnection rates, and analyzes energy-momentum transfer and gravitational helicity. These are results of the cited **GR** formalism, not independent evidence for UBT or proof that gravity literally turns off or spacetime tears.

**Read the exact paper before adopting its notation/conventions.** The following equations are exploratory UBT diagnostics; they are not quotations from the source and are not asserted to reproduce the full comparator formalism.

## Candidate UBT diagnostic

UBT's canonical covariant tetrad is (subject to the canonical normalization/conventions)

```tex
E_\mu[\Theta] = D_\mu\Theta / \sqrt{\mathcal N_0},
\qquad
g_{\mu\nu}[\Theta] = \mathrm{central}\!\left(\tfrac12
\{E_\mu,E_\nu\}\right).
```

After selecting a legitimate real tetrad/coframe `e^a_mu[Theta]` from this construction and specifying the local Lorentz gauge, define the **anholonomy** two-form

```tex
F^a_{\mu\nu}[\Theta] := 2\partial_{[\mu}e^a_{\nu]}[\Theta],
\qquad
R^a_\nu[\Theta,u] := u^\mu F^a_{\mu\nu}[\Theta].
```

These are proposed **diagnostics**, not dynamical equations. Crucially, `de^a` is **not** local-Lorentz covariant on its own and should **not** be identified with torsion. A covariant comparison must explicitly keep the spin connection and compute

```tex
T^a = de^a + \omega^a{}_b \wedge e^b .
```

Test whether field-sheet structures and reconnection criteria can be expressed in terms of a Lorentz-gauge-independent quantity (or a specified physically justified frame), and whether a smooth transport vector `u` exists. Nonzero `R` in a chosen frame is **not sufficient** to establish reconnection; changes of transport vector/frame may remove it.

## Research plan and falsifiable gates

1. **Comparator audit:** reproduce the exact definitions, gauge dependence, integrability assumptions, ideal condition, reconnection criterion, energy-momentum and helicity balances of both cited papers. No equation-level correspondence is presumed in advance.
2. **Embedding/gauge:** map the canonical `Theta -> E -> g` chain into a valid real coframe and spin connection. Record regularity, invertibility and signatures; treat degenerate tetrads separately.
3. **Invariant transport:** derive field-sheet integrability and frozen-in conditions, including Lie derivatives/Lie dragging and possible transport-vector redefinitions, and identify an invariant obstruction if one exists.
4. **Connection/torsion:** compare torsion-free Levi-Civita, composite connection, and any residual `SO(2)` choice. Do not equate anholonomy with dynamical torsion.
5. **Dynamics:** only after action and constraints are specified, study whether torsion, phase/compact-mode excitations or other `Theta` sectors supply a non-ideal contribution; compute energy and helicity balances, gauge-invariant perturbations, and physical degrees of freedom.
6. **Examples:** start with exact flat Minkowski and a known GR background, then attempt a controlled non-trivial configuration. Include explicit numerical/symbolic counterchecks.

**Falsifiers / stop rules:**

- If the proposed reconnecting quantity changes under a pure local Lorentz frame rotation with unchanged geometry, reject its interpretation as a physical UBT prediction.
- If apparent violation disappears under a permitted choice of smooth transport vector, do not report reconnection.
- If the construction cannot consistently produce a nondegenerate real Lorentzian tetrad on the test domain, restrict the claim to a degenerate/kinematic model and do not claim GR reconnection.
- If a putative new effect requires an unmotivated term in the action or introduces ghosts/ill-posed degrees of freedom, keep it OPEN or reject it.
- Reproducing the cited GR result is only a consistency test, not evidence for new UBT physics.

## Relation to other UBT work

Relevant internal questions: canonical covariant tetrad/GR recovery; composite-connection invariant basis through second derivative order; kinetic Hessian and constraint counting; whether the residual `SO(2)` connection is auxiliary, gauge, or physical; nondegenerate vs degenerate tetrad branches; Theta phases and compact modes.

**Current conclusion:** a mathematically well-motivated comparator and potential research direction, **not** a demonstration of reconnection in UBT. Promotion to canonical requires a covariant formulation, dynamically consistent closure, and an independent reproducer.
