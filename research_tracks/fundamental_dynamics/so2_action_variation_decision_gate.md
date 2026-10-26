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

# Residual SO(2) variational decision gate (trial comparison only)

**26 October 2026 — conditional sector classification, not a UBT fundamental action.**

Merged PR #787 proves two carriers leave a local one-form alpha in the stabilizer of their Lorentz connection. This note asks which forms of a **selected** reduced action could determine alpha. On an oriented transverse SO(2) bundle, denote its induced Abelian connection A and curvature F=dA locally (in general the reference connection and normal-plane geometry also contribute; A is the **total induced** connection, not simply alpha in an arbitrary non-adapted frame). Under a local frame rotation A -> A+d chi, F is unchanged.

A deliberately comparative fixed-background action family is
S[A]=integral sqrt(-g) [-a/4 F_mu_nu F^mu_nu + b/2 (A_mu-B_mu)(A^mu-B^mu) + A_mu j^mu],
where a,b are *trial coefficients*, B is a prescribed one-form and j a prescribed current. Its Euler equation, with stated boundary data and sign convention, is
a nabla_mu F^mu_nu + b(A_nu-B_nu) + j_nu = 0.
No claim is made that the microscopic Theta dynamics yields any of these terms, a physical U(1) field, or its signs.

- a=0, b!=0: algebraic auxiliary solution A=B-j/b, subject to compatibility with all previously imposed carrier transport constraints. **No curvature kinetic term for A** in this comparison.
- a!=0, b=0: Maxwell-like differential equation. Frame gauge invariance of the source term requires covariant current conservation (or boundary restrictions); field equations do not demand F=0. Local vacuum Maxwell has two polarizations in 3+1 dimensions **in this standalone independent gauge-field trial**, not necessarily in composite UBT.
- a!=0, b!=0: differential Proca-like sector. It has three local modes under ordinary fixed-background nondegenerate assumptions when B and j are external and generic consistent; again this is not a UBT mode count. With a mass term, B must transform with A for frame-gauge invariance, or be a genuine compensating composite. Otherwise such a trial term explicitly breaks the normal-frame gauge redundancy.
- a=b=0: A is absent without j; with linear source A·j alone it acts as a multiplier imposing j=0, not as a reconstructed unique connection.

When varying **composite** B[Theta], A[Theta] or g[Theta], these field equations cannot be adopted without the complete chain-rule variational terms. The constants, positivity, gauge redundancy, boundary terms and underlying action are all open. Hence this classification is a **decision tree for candidate actions**, not a solution to their selection.

**Research priority:** derive the A-dependence of the original single-Theta reduced action using omega=omega0+alpha J. If the reduced density is independent of alpha modulo boundary terms, the stabilizer is not determined by local bulk Euler equations. If alpha appears without derivatives, compute its full algebraic Hessian and constraint rank. If d alpha appears, perform gauge/Dirac analysis and test ghost sign.

Test: tests/test_so2_action_decision.py (symbolic variation in 1+1 dimensions checks the Euler sign structure and auxiliary elimination).
