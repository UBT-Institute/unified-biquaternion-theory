<!-- BILINGUAL-UNIT: theta-role-2026.provenance -->
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

# Theta parameter-role theorem — October 2026

**Status:** exact mathematics closed; UBT identification audit narrowed  
**Verifier:** \`verification/theta_parameter_role_check.py\`  
**Czech edition:** \`theta_parameter_role_result_2026-10.cs.md\`

<!-- BILINGUAL-UNIT: theta-role-2026.theorem -->
## 1. Exact S1 heat-kernel theorem

Let the canonical compact internal coordinate have circumference
\[
L=2\pi R_\psi,\qquad \psi\sim\psi+L.
\]
For the free Laplacian
\[
H_\psi=-\partial_\psi^2
\]
and heat parameter \(s>0\),
\[
K_s(\psi,\psi')
=
\frac1L\sum_{n\in\mathbb Z}
e^{-(2\pi n/L)^2s}
e^{2\pi i n(\psi-\psi')/L}.
\]

With the Jacobi convention
\[
\vartheta_3(z|\tau)
=\sum_{n\in\mathbb Z}e^{\pi i n^2\tau+2\pi i n z},
\]
coefficient matching gives exactly
\[
\boxed{
K_s(\psi,\psi')
=
\frac1L\vartheta_3\!\left(
z_\theta\,\middle|\,\tau_\theta
\right),
\quad
z_\theta=\frac{\psi-\psi'}L,
\quad
\tau_\theta=\frac{4\pi i s}{L^2}
=\frac{i s}{\pi R_\psi^2}.
}
\]

Thus in the controlled heat-kernel construction:

- the compact coordinate difference belongs to the **elliptic argument** \(z_\theta\);
- the positive non-compact heat parameter determines the **Jacobi modulus**
  \(\tau_\theta\);
- \(\operatorname{Im}\tau_\theta>0\) follows from \(s>0\).

<!-- BILINGUAL-UNIT: theta-role-2026.consequence -->
## 2. Consequence for UBT complex time

Canonical UBT independently defines
\[
\tau_{\rm UBT}=t+i\psi.
\]

The heat-kernel theorem above does not identify this coordinate with the Jacobi
modulus. Therefore the present canonical axioms imply only
\[
\boxed{
\tau_{\rm UBT}\not\equiv\tau_\theta
\quad\text{as a derived identity.}
}
\]

This is a statement about derivational status, not a theorem that no future map can
relate them.

A reduced bridge kernel
\[
\sum_n a_n e^{-\pi\psi n^2}e^{\pi i t n^2}
\]
is mathematically a theta series with bridge parameter
\[
\tau_{\rm bridge}=t+i\psi
\]
when \(\psi>0\). But identifying the damping coordinate in that reduced model with
the canonical compact UBT coordinate is an **ansatz/bridge**, not a consequence of the
canonical action.

<!-- BILINGUAL-UNIT: theta-role-2026.torus -->
## 3. No automatic time torus

Compactness of \(S^1_\psi\) alone does not make real Minkowski time \(t\) a second
compact lattice generator. Therefore
\[
\tau_{\rm UBT}=t+i\psi
\]
does not by itself define the modular shape of a physical
\(\mathbb C/(\mathbb Z+\tau\mathbb Z)\) torus.

A separate compact real-time scale \(R_t\) may define a mathematical lattice model
with
\[
\tau_{\rm mod}=iR_\psi/R_t,
\]
but \(R_t\) and its physical compactness must be independently derived. Without that
derivation this remains a modular model, not canonical UBT spacetime topology.

<!-- BILINGUAL-UNIT: theta-role-2026.status -->
## 4. Updated ledger

| Claim | Status |
|---|---|
| free heat kernel on \(S^1_\psi\) is a Jacobi theta kernel | PROVED |
| \(z_\theta=(\psi-\psi')/L\) | PROVED |
| \(\tau_\theta=4\pi i s/L^2\) | PROVED |
| \(\tau_{\rm UBT}=t+i\psi\) | canonical definition |
| \(\tau_{\rm UBT}=\tau_\theta\) | NOT DERIVED |
| real time + compact \(\psi\) automatically form a modular torus | NOT DERIVED |
| reduced bridge \(\tau_{\rm bridge}=t+i\psi\) | mathematically valid bridge ansatz |
| UBT kernel belongs to a Weil/Hermitian/mock theta class | OPEN |

<!-- BILINGUAL-UNIT: theta-role-2026.classification -->
## 5. Free-sector theta classification

For the fixed-background compact-psi fluctuation operator with spectrum
\[
\lambda_n=\frac{n^2}{R_\psi^2},
\]
the heat trace is exactly
\[
\operatorname{Tr}e^{-sH_\psi}
=
\sum_{n\in\mathbb Z}e^{-s n^2/R_\psi^2}
=
\vartheta_3\!\left(0\,\middle|\,\frac{i s}{\pi R_\psi^2}\right).
\]

Therefore the controlled free/fixed-background compact sector is classified as a
**classical Jacobi / rank-one lattice theta function**. It is not a mock theta
function, and no mock-modular completion or resurgence hypothesis is needed for this
free sector.

This agrees with the existing fixed-background Hessian result: after controlled
Euclidean continuation its principal part is Laplace type, so the standard heat-kernel
construction is the correct mathematical object.

Howard's Weil-representation framework is therefore useful as a representation-theory
benchmark for this ordinary lattice theta sector. Costin--Dunne--Saraeb becomes relevant
only if a later interacting/composite kernel is proved to have mock/modular asymptotics
or a nontrivial natural-boundary/resurgent problem.

<!-- BILINGUAL-UNIT: theta-role-2026.next -->
## 6. Remaining P1 target

P1 is **closed for the free compact heat-kernel sector**.

The remaining nontrivial task concerns the full interacting/composite Hessian or a
canonical correlation function: derive it from the final action, determine its lower-order
operator data, and only then ask whether the resulting kernel stays in the classical
Jacobi/Weil class or moves to a more general modular object.

Thus the direct parameter-role ambiguity is closed; the interacting theta classification
remains open.
