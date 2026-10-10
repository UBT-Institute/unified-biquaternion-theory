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

# UBT Development Roadmap

**Current programme date:** 10 October 2026

This file records the current priority order. Earlier week-by-week roadmaps are
preserved in git history rather than duplicated here.

## 1. Cross-cutting priority — finalize one fundamental action

The single-\(\Theta\) action family is defined but not finalized.

Required closure:
- configuration space and status of \(\psi\);
- microscopic integration measure and Jacobian;
- real pairing and sign conventions;
- independent versus composite metrics/connections;
- derivative order, potential and boundary terms;
- complete Euler--Lagrange system;
- constrained/gauge-fixed Hessian and physical mode count;
- explicit reduction maps to GR, gauge, matter and cosmology sectors.

No sector-specific effective functional may silently replace this object as a
second fundamental action.

## 2. P1 — theta / complex time

**Status:** closed for the currently defined free/reduced theta objects.

Established:
\[
\tau_{\rm UBT}=t+i\psi
\]
is a physical dimensionful coordinate and is not canonically the Jacobi
modular parameter. The compact-circle heat trace has ordinary Jacobi-theta
structure with
\[
\tau_J=\frac{i s}{\pi R_\psi^2}.
\]

Open:
- full interacting modular covariance;
- any action-derived map from physical complex time to a genuine modulus.

## 3. P2 — colour SU(3)

**Status:** primary active physics target; algebra/geometry strong, full QCD
open.

Closed/narrowed:
- exact algebraic \(SU(3)\) stabilizer and Gell-Mann structure;
- direct raw-carrier and simple finite-jet gluon interpretations are no-go;
- exact constrained \(4\times3\) Stiefel/HLS rewrite on the timelike branch;
- derived adjoint frame current;
- weak fixed-frame induction gives \(Z_B>0\) but a massive vector phase;
- Stiefel continuation through \(\rho=0\) is singular;
- pure composite frame topology has no independent instanton bundle sectors.

Preferred finite-radius target:
\[
\rho_0>0,\qquad
Z_B>0,\qquad
c_V\to0,\qquad
\lambda_2\to0,\qquad
M_\beta^2>0.
\]

Next decisive calculations:
1. finite noncompact Stiefel/HLS phase flow;
2. complete locking-operator flow;
3. mixed sharp/GR source
   \[
   \left.\beta_{\lambda_2}\right|_{\lambda_2=0};
   \]
4. Yang--Mills 1PI/BRST/Slavnov--Taylor matching;
5. autonomous gauge topology after frame-matter decoupling.

## 4. P3 — CMB full covariance

**Status:** statistical infrastructure ready; H3 theory template open.

Do not treat post-hoc prime/theta filtering as a UBT prediction.

Required physics chain:
\[
S^{(2)}_{\rm scalar}
\to
\delta\Theta\to\mathcal R
\to
\text{state prescription}
\to
P_{\rm UBT}
\to
C_{\ell m,\ell'm'}^{XY}.
\]

Only then compare H3 against H2 out of sample.

## 5. P4 — torus modulus

**Status:** isolated massless one-loop selection closed as no-go.

For fixed area,
\[
\det{}'\Delta_\tau\propto\Im\tau\,|\eta(\tau)|^4.
\]

The square point is not a stable minimum of the standard positive bosonic
one-loop action, and no finite global modulus minimum is selected by that
isolated massless determinant.

Next step: derive a genuine compact modulus and bounded
massive/interacting/backreacted \(V_{\rm eff}\) from the finalized action.

## 6. Quantitative-prediction gate

No numerical result is promoted to a first-principles UBT prediction unless:
- all theory inputs are fixed before comparison with data;
- the observable follows from the same finalized action;
- uncertainty and nuisance parameters are declared;
- competing generic null models are tested;
- the result is reproducible out of sample.

## 7. Current success criteria

Near-term success means:
- one finalized microscopic action/measure;
- a controlled physical Hessian with no hidden ghost branch;
- a decisive result on the finite-radius HLS colour phase;
- an action-derived \(P_{\rm UBT}\);
- at least one preregistered quantitative prediction not obtained by fitting.

## Status synchronization rule

Status changes must be mirrored in:
- CLAIMS.yaml;
- STATUS_OF_UBT.md;
- WHAT_IS_PROVED.md;
- CLAIMS_MATRIX.en.md and CLAIMS_MATRIX.cs.md;
- research_tracks/priority_program_2026_10/README.md.

Historical roadmaps remain recoverable through git history.
