<!-- BILINGUAL-UNIT: theta-oct2026.provenance -->
<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Research audit; no new canonical identification is made.
UBT-AI-PROVENANCE-END
-->

# Theta / complex-time modular and resurgent audit — October 2026

**Status:** RESEARCH AUDIT — open classification problem  
**Czech edition:** theta_modular_resurgent_audit_2026-10.cs.md

<!-- BILINGUAL-UNIT: theta-oct2026.guardrail -->
## 1. Binding guardrail

The following variables are distinct unless a theorem identifies them:
\[
\tau_{\rm UBT}=t+i\psi,\qquad
\tau_\theta,\qquad
z_\theta,\qquad
s_{\rm heat}.
\]

The existing complex-time branch-selection track already records this separation.
This note does not redefine canonical UBT time.

<!-- BILINGUAL-UNIT: theta-oct2026.problem -->
## 2. Exact problem

Given a UBT solution or kernel described informally as "theta-like", determine whether
there exists a derived map
\[
\Phi:(t,\psi,\Theta,\ldots)\mapsto(z_\theta,\tau_\theta)
\]
such that the kernel is actually a Jacobi/lattice theta function or a controlled
generalization.

The audit must establish all hypotheses needed for any claimed transformation law:
domain, quadratic/Hermitian form, lattice, convergence region, representation, and
growth conditions.

<!-- BILINGUAL-UNIT: theta-oct2026.tests -->
## 3. Tests

1. **Jacobi test:** verify the heat equation and exact elliptic/modular transformation
   laws for the proposed \(z_\theta,\tau_\theta\).
2. **Weil/Hermitian test:** identify a lattice or Hermitian space and a Weil
   representation producing the UBT kernel, or record the obstruction.
3. **Boundary test:** determine the behavior as
   \(\operatorname{Im}\tau_\theta\to0^+\).
4. **Resurgence test:** only if the kernel is mock/modular or has a proven divergent
   cusp expansion, determine Borel singularities and Stokes data. Mock-theta results
   are not imported into ordinary Jacobi theta by analogy.
5. **Compactness test:** a non-compact heat parameter is not identified with compact
   periodic \(\psi\) without an explicit quotient/semigroup theorem.

<!-- BILINGUAL-UNIT: theta-oct2026.color -->
## 4. Possible colour bridge

The canonical colour carrier
\[
V=\mathbb C\text{-span}\{I,J,K\}
\]
has a derived Hermitian form \(h\) and volume form \(\Omega\) with
\(\operatorname{Stab}(h,\Omega)=SU(3)\).

A legitimate research question is whether some UBT theta object is a Hermitian theta
lift built from \((V,h)\). This is currently **OPEN**. Dimension matching alone is
not evidence.

<!-- BILINGUAL-UNIT: theta-oct2026.references -->
## 5. External benchmarks

- Benjamin Howard, Theta functions after Weil, arXiv:2609.13429.
- Ovidiu Costin, Gerald V. Dunne, Ali Saraeb,
  Resurgent rigidity of mock theta functions: uniqueness and natural boundary crossing,
  arXiv:2609.40276.

These papers define comparison standards. They do not establish that UBT belongs to
their mathematical classes.

<!-- BILINGUAL-UNIT: theta-oct2026.exit -->
## 6. Exit criterion

Close this audit only with either:

- an explicit, checked theta/Weil/mock classification with all variables mapped; or
- a no-go statement explaining exactly which required property fails.
