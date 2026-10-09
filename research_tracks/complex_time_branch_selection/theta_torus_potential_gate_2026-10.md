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

# Theta torus-potential gate — canonical-topology no-go

**Date:** 2026-10-09  
**Status:** P4 DEFERRED / closed as a no-go for the current single-circle topology

## Question

Can the present canonical UBT action dynamically select a two-dimensional torus shape
by minimizing an effective potential
\[
V_{\rm eff}(\tau_{\rm mod})?
\]

## Canonical topology actually available

The active complex-time formulation has
\[
\tau_{\rm UBT}=t+i\psi,
\qquad
\psi\sim\psi+2\pi R_\psi,
\]
where \(t\) is ordinary non-compact physical time and \(S^1_\psi\) is a compact internal
phase fibre.

Therefore the canonical compact complex-time sector contains one compact cycle:
\[
\boxed{S^1_\psi.}
\]

A single circle has a radius/scale modulus \(R_\psi\), but it does not have the complex
shape modulus of a rank-two lattice
\[
\mathbb C/(\mathbb Z+\tau_{\rm mod}\mathbb Z).
\]

## No-go statement

Compactness of \(\psi\) does not compactify real Minkowski time. Hence the pair
\((t,\psi)\) does not by itself supply two compact lattice periods.

Consequently, within the current canonical topology:
\[
\boxed{
\text{there is no action-derived physical torus shape }
\tau_{\rm mod}\text{ for a theta lattice potential to select.}
}
\]

This rules out promoting square/hexagonal/rhombic theta-lattice minimization results to
a canonical UBT prediction at present.

## What remains legitimate

The canonical single-circle sector can have an effective radius potential
\[
V_{\rm eff}(R_\psi)
\]
or spectral/heat-kernel dependence through
\[
\vartheta_3\!\left(0\,\middle|\,\frac{i s}{\pi R_\psi^2}\right).
\]

That is a **scale-selection** problem, not a two-dimensional torus-shape problem.

A genuine modular-shape programme may be reactivated only if UBT independently derives
one of the following:

1. a second compact cycle with a physical period;
2. a rank-two charge/winding lattice whose complex structure is dynamical;
3. another canonical object whose moduli space is genuinely the upper half-plane modulo
   a modular group.

An arbitrary bookkeeping scale \(R_t\) is insufficient.

## Relation to old repository material

Older modular notes that introduce
\[
\tau_{\rm mod}=iR_\psi/R_t
\]
are mathematically valid after assuming two lattice scales. They are not a derivation
that real physical time is compact, and therefore do not establish a canonical UBT
torus-shape modulus.

## P4 verdict

| Target | Status |
|---|---|
| single-circle \(R_\psi\) effective-potential programme | legitimate / separate |
| physical rank-two torus shape in current canonical complex time | NOT DERIVED |
| theta-lattice geometry-selection programme | DEFERRED |
| importing external lattice minima as UBT geometry | PROHIBITED without derived functional |

P4 is therefore not an active theory-building task. The higher-priority problem is to
derive the actual theta/operator kernel and the \(R_\psi\) dependence from the canonical
action.
