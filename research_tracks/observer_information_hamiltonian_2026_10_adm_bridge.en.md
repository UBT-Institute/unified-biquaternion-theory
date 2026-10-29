<!-- BILINGUAL-UNIT: adm-bridge -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Conditional ADM Hamiltonian bridge

<!-- BILINGUAL-UNIT: scope -->
## Scope

This is a conditional ADM bridge for the existing Einstein--Hilbert infrared branch, not an independent fundamental field and not a completed composite Hamiltonian.

<!-- BILINGUAL-UNIT: underdetermination -->
## Curvature coefficient

The existing `gap_10d_induced_gravity_endgame.tex` establishes that kinematic axioms allow arbitrary curvature coefficient. They do not determine Newton's constant. The family of actions is:

\[
S_\alpha[\Theta]=S_0[\Theta]+\alpha\int d^4x\sqrt{-g[\Theta]}R[g[\Theta]].
\]

<!-- BILINGUAL-UNIT: adm -->
## Conditional ADM Hamiltonian (units c=1)

Choose an ADM foliation and an Einstein--Hilbert effective action with its boundary terms. The standard Legendre transform gives the following canonical momentum and constraints. These are conditional results from GR, not a fundamental derivation from the composite field Theta.

\[
\pi^{ij}=\frac{\sqrt h}{16\pi G}(K^{ij}-h^{ij}K),\qquad
H_{\rm ADM}=\int d^3x(N\mathcal H_\perp+N^i\mathcal H_i)+H_{\partial\Sigma}.
\]
\[
\mathcal H_\perp=\frac{16\pi G}{\sqrt h}(\pi^{ij}\pi_{ij}-\tfrac12\pi^2)
-\frac{\sqrt h}{16\pi G}({}^{(3)}R-2\Lambda),\quad
\mathcal H_i=-2D_j\pi^j{}_i.
\]

<!-- BILINGUAL-UNIT: caveat -->
## Outstanding proof obligation

Substitute the induced metric, and vary Theta and its two-sided connection consistently, including torsion and split-jet constraints. Determine the true primary constraints and their Dirac--Bergmann algebra. A direct substitution into ADM Poisson brackets is insufficient. LEAN-PENDING; FULL-CAS-PENDING; BILINGUAL-SEMANTICS-PENDING.
