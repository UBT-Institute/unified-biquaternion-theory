<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# UBT research priorities — 2026-10-09

## Purpose

This note converts the October literature scan and the current repository state into four
testable research programmes. It separates proved mathematics from physical identification
and from speculative interpretation.

## Progress snapshot — 2026-10-09

| Priority | Current result | Remaining decisive gate |
|---|---|---|
| P1 theta / complex time | **Free compact sector CLOSED:** exact S1 heat kernel is a classical rank-one Jacobi theta kernel with z_theta=(psi-psi')/L and tau_theta=4 pi i s/L^2. Direct tau_UBT=t+i psi = tau_theta identification is **NOT DERIVED**. | Derive and classify the full interacting/composite Hessian or canonical correlator. |
| P2 SU(3) dynamics | **Kinematic bridge substantially closed:** exact 3+5 spin/quadrupole construction, minimal bimodule and pure-MC no-gos, plus a Theta-defined rank-three projector bundle with nonzero traceless composite curvature. | Prove that the canonical Hessian/action selects this connection, reduce U(3) to the physical SU(3) determinant sector, and derive unrestricted YM dynamics and g_s. |
| P3 CMB | **Protocol + comparator implemented:** H0/H1/H2/H3 full-covariance likelihood/KL tooling and regression tests are in repo. | Generate/fetch physically justified topology covariances, freeze parameters, and run independent evaluation. |
| P4 torus shape | **DEFERRED / no-go for current canonical topology:** one compact S1_psi has a radius but no rank-two torus shape modulus. | Reactivate only after a second compact cycle or genuine rank-two lattice modulus is action-derived. |

The active programme therefore concentrates on P1 interacting-kernel classification,
P2 Hessian selection of the composite colour connection, and P3 independent CMB
evaluation. P4 must not be expanded by analogy alone.

---

## Locked execution order

1. Theta / complex-time role audit and SU(3) dynamics bridge in parallel.
2. CMB full-covariance falsification protocol once the null hierarchy is frozen.
3. Theta torus-potential programme only after an effective potential is derived from the
   canonical action. No free-standing torus-potential ansatz is to be promoted to UBT.

## P1 — Theta / complex-time modular and resurgent audit

### Existing binding facts

- Canonical UBT uses \(\tau_{\rm UBT}=t+i\psi\).
- Existing complex-time notes distinguish \(\tau_{\rm UBT}\), the Jacobi theta modulus
  \(\tau_\theta\), the theta argument \(z_\theta\), and heat/proper-time variables.
- Compact periodic \(\psi\) is not automatically the same object as a non-compact heat
  parameter or upper-half-plane modulus.

### Research gates

**T1 — role map or no-go.** Derive an explicit map
\[
(t,\psi,\text{UBT data})\longmapsto (z_\theta,\tau_\theta)
\]
from a canonical UBT equation, or prove that no such identification follows from the
current axioms.

**T2 — theta class.** Classify the actual UBT theta kernel, if present, as one of:
classical Jacobi/lattice theta, Weil/Siegel/Hermitian theta lift, mock/modular completion,
or none of these. Similar notation is not sufficient.

**T3 — boundary analysis.** If \(\operatorname{Im}\tau_\theta\to0^+\) is physically
reachable, determine whether the canonical object has a controlled boundary value,
distributional limit, modular continuation, or resurgent continuation. Do not import
mock-theta resurgence into ordinary Jacobi theta without a derivation.

**T4 — falsification condition.** State at least one property that would fail if the UBT
kernel is not in the proposed modular class: a transformation law, growth bound, PDE,
Fourier coefficient relation, or boundary behavior.

External benchmarks:
- B. Howard, Theta functions after Weil, arXiv:2609.13429.
- O. Costin, G. V. Dunne, A. Saraeb, Resurgent rigidity of mock theta functions:
  uniqueness and natural boundary crossing, arXiv:2609.40276.

These are benchmarks, not evidence that UBT already satisfies their hypotheses.

**Exit criterion:** a proof-level role map/classification or an explicit no-go report.

## P2 — Close the SU(3) dynamics gap as far as the present algebra allows

A new research note and exact verifier establish the quaternion-adjoint
spin/quadrupole decomposition
\[
\mathfrak{su}(3)=\mathbf3_{\rm spin}\oplus\mathbf5_{\rm quadrupole}
\]
on \(V=\mathbb C\text{-span}\{I,J,K\}\), with
\[
S_1=\lambda_7,\qquad S_2=-\lambda_5,\qquad S_3=\lambda_2,
\]
and the remaining five Gell-Mann directions obtained from symmetric traceless
quadratic combinations of the \(S_i\).

The same note records two no-go results:

1. the minimal two-sided derivative \(X\mapsto AX-XB\), with
   \(A,B\in\mathbb C\otimes\mathbb H\simeq M_2(\mathbb C)\), cannot contain a full
   \(\mathfrak{su}(3)\) gauge algebra;
2. a connection written only as \(U^{-1}dU\) or \(U^\dagger dU\) is locally pure gauge
   and has zero curvature by the Maurer--Cartan identity.

Still open:

**S1 — action origin.** Derive a local
\[
\mathcal G_\mu\in\mathfrak{su}(3)\subset\operatorname{End}_{\mathbb C}(V)
\]
from the same canonical \(S[\Theta]\), rather than inserting \(G_\mu^a\) by hand.

**S2 — normalization.** Derive the normalization/coupling \(g_s\) or state precisely
which coefficient remains independent.

**S3 — curvature.** Show that the derived connection admits nonzero
\[
\mathcal F_{\mu\nu}=[\nabla_\mu,\nabla_\nu]_{\rm colour}
\]
on admissible UBT configurations.

**S4 — induced Yang--Mills bridge.** If the full Euclideanized composite Hessian is
Laplace type with this connection, compute the heat-kernel coefficient containing
\(\operatorname{tr}\mathcal F_{\mu\nu}\mathcal F^{\mu\nu}\). This step is
conditional until S1 is closed.

**Exit criterion:** either an action-level derivation of \(\mathcal G_\mu\), or a
precise no-go theorem showing why the current canonical action cannot generate it.

## P3 — CMB full-covariance falsification protocol

Freeze the following null hierarchy before further optimization:
\[
\begin{aligned}
H_0&=\Lambda{\rm CDM}\text{ with trivial topology},\\
H_1&=\text{ordinary compact topology},\\
H_2&=\text{compact topology + generic oscillatory primordial spectrum},\\
H_3&=\text{UBT theta/prime-gated model}.
\end{aligned}
\]

Primary observables:
\[
C_{\ell m,\ell' m'}^{TT},\quad
C_{\ell m,\ell' m'}^{TE},\quad
C_{\ell m,\ell' m'}^{EE}.
\]
Primordial \(BB\) is secondary unless a UBT derivation predicts a specifically stronger
B-mode effect.

Required safeguards:
- pre-register the statistic and parameter ranges;
- use independent tuning and evaluation realizations/data partitions;
- include off-diagonal covariance;
- compare \(H_3\) against \(H_2\), not only against \(H_0\);
- report look-elsewhere corrections and failed variants.

External benchmark:
R. Himeno, A. J. Nishizawa, K. Ichiki,
Limited Impact of CMB B-mode Polarization on Constraints on Cosmic Topology,
arXiv:2610.05960.

**Exit criterion:** a reproducible protocol plus a blind/split-data result; no claim of
prediction until the UBT filter parameters are independently fixed.

## P4 — Theta torus-potential / geometry selection

This programme is gated, not yet an active physical claim.

Do not identify the modular shape parameter of a lattice/torus with
\(\tau_{\rm UBT}=t+i\psi\) merely because both are conventionally denoted \(\tau\).

The track may become active only after deriving an effective functional
\[
V_{\rm eff}(\tau_{\rm mod})
\]
from \(S[\Theta]\) or a controlled effective action.

Then:
1. reduce \(\tau_{\rm mod}\) to a modular fundamental domain where appropriate;
2. solve \(\partial_{\tau_{\rm mod}}V_{\rm eff}=0\);
3. prove local/global stability using the Hessian;
4. compare square, hexagonal/rhombic, rectangular and boundary degenerations;
5. propagate any selected geometry to a measurable prediction.

**Exit criterion:** derived \(V_{\rm eff}\) plus a certified minimum, or remain deferred.

## Claim discipline

- Literature overlap is a benchmark, not validation.
- No new fundamental algebra is introduced by these priorities.
- GAP-SU3-DYN remains open until the colour connection is action-derived.
- \(\tau_{\rm UBT}\), \(\tau_\theta\), \(z_\theta\), heat time and torus modulus
  remain distinct until a theorem identifies them.
- CMB exploratory significance is not a prediction unless the analysis is frozen before
  evaluation.
