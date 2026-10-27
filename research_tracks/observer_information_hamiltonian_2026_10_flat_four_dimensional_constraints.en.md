<!-- BILINGUAL-UNIT: flat-4d-constraints -->
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

# Four-dimensional gradient-volume constraint calculation

<!-- BILINGUAL-UNIT: result -->
## result

In the restricted flat-gradient branch $e_\mu{}^a=\partial_\mu Y^a$, with fixed orientation $\det e>0$ and $\mathcal L_{\rm vol}=\alpha\det(e_\mu{}^a)$, denote $v^a=\partial_0Y^a$ and $M_i{}^a=\partial_iY^a$. The determinant is linear in its first row: $\det e=\sum_{a=0}^3v^a C_{0a}(M)$.

<!-- BILINGUAL-UNIT: constraints -->
## constraints

Canonical momenta are $p_a=\alpha C_{0a}(M)$; hence the four primary relations $\phi_a=p_a-\alpha C_{0a}(M)\approx0$. The velocity Hessian $W_{ab}=\partial^2\mathcal L_{\rm vol}/(\partial v^a\partial v^b)$ vanishes identically and the canonical Hamiltonian density $\mathcal H_{\rm can}=\sum_ap_av^a-\mathcal L_{\rm vol}=0$. This does **not** remove possible boundary charges and it does **not** calculate the constrained physical Hamiltonian of full UBT.

<!-- BILINGUAL-UNIT: verification -->
## verification

SymPy 4x4 symbolic determinant, differentiation and Legendre identity returned the zero Hessian and zero canonical density (local computation on 2026-10-27). The result also follows directly from determinant multilinearity. No Lean run. **CAS-checked restricted model; LEAN-PENDING**.

<!-- BILINGUAL-UNIT: scope -->
## scope

The result applies only to an exact-gradient tetrad in a fixed-orientation, nondegenerate patch with fixed volume coefficient $\alpha$. It does **not** apply automatically to curved/torsionful two-sided composite connections or to Hilbert--Palatini curvature terms, which must undergo separate constrained Hamiltonian analysis. The existing split-jet right-inverse theorem gives representability, not dynamical selection; adding its auxiliary variables does not automatically solve the Hamiltonian problem.

<!-- BILINGUAL-UNIT: next -->
## next

Next test: choose an admissible torsionful composite background from the existing canonical route; derive the connection's dependence on time derivatives, the complete first-order or higher-derivative action and its presymplectic/Dirac constraints. Check characteristic speeds relative to the emergent metric and avoid any new fundamental field. **BILINGUAL-SEMANTICS-PENDING**; do not merge before required verification.
