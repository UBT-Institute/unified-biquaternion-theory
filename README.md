> **Current status update (10 October 2026):** UBT now has a mature conditional GR-recovery chain and a substantially sharpened research programme for colour, theta/complex-time, CMB covariance, and torus-modulus dynamics. The single fundamental action is still **not finalized**; full QCD, a first-principles primordial covariance, and a bounded interacting torus-modulus potential remain open. See `STATUS_OF_UBT.md`, `CLAIMS.yaml`, and `research_tracks/priority_program_2026_10/README.md`.

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


# Unified Biquaternion Theory (UBT)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21347352.svg)](https://doi.org/10.5281/zenodo.21347352)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

**Author**: Ing. David Jaroš  
**Status**: Canonical core + separated research and speculative layers

---

The canonical UBT core is a mathematical physics research program based on
biquaternionic fields, a projection-free covariant-tetrad metric, and
GR/gauge/alpha recovery tracks.

Speculative interpretations concerning consciousness, psychons, survival
after death, ThetaComm, or metaphysical ontology are not part of the
canonical physical claims. They are maintained separately under
speculative_extensions/ and should be read as exploratory hypotheses, not
established physics.

---

## Current Research Status — 10 October 2026

The repository distinguishes exact theorems, conditional reductions, no-go
results, and open research targets. The current high-level status is:

- **Fundamental action:** one action is required, but the registered
  \(S_\Theta\) family is still DEFINED_FAMILY_NOT_FINALIZED. No sector action
  may be promoted to a second fundamental action.
- **GR:** the covariant-tetrad geometry, rank-ten map, connection
  reconstruction, split-jet nonpropagation, and the local Einstein--\(\Lambda\)
  infrared branch are strongly developed. The effective GR recovery remains
  conditional on the still-open microscopic Hessian/measure/coupling
  derivation.
- **Colour \(SU(3)\):** the algebraic stabilizer, Gell--Mann operator
  decomposition, moving rank-three carrier, and exact \(4\times3\)
  Stiefel/hidden-local-\(SU(3)\) rewrite are established. **Full QCD is not
  derived.** The preferred remaining target is a finite-radius quantum phase
  with autonomous gauge dynamics, \(Z_B>0\), vanishing HLS locking, suppressed
  determinant anisotropy, and gapped charged frame modes.
- **Theta / complex time:** physical
  \(\tau_{\rm UBT}=t+i\psi\) is distinct from the dimensionless Jacobi modular
  parameter. The free compact-circle heat trace is ordinary Jacobi theta
  mathematics; generic finite weighted sums are not modular/mock-modular by
  default.
- **CMB:** the H0/H1/H2/H3 full-covariance comparison machinery is prepared,
  but an action-derived primordial covariance \(P_{\rm UBT}\) is still
  missing. Compact \(S^1_\psi\) alone does not impose a spatial
  \(k_{\min}=1/R_\psi\).
- **Torus modulus:** the isolated massless one-loop determinant does not
  produce a finite stable modulus minimum. A genuine
  massive/interacting/backreacted \(V_{\rm eff}\) remains open.
- **Fine structure / \(\alpha\):** structural and numerical observations remain
  explicitly separated from a first-principles derivation.

Authoritative status sources:
- STATUS_OF_UBT.md
- CLAIMS.yaml
- WHAT_IS_PROVED.md
- research_tracks/priority_program_2026_10/README.md

---

## What Is UBT?

UBT is a biquaternionic field framework over complex time **τ = t + iψ** that aims to recover:

- emergent Lorentzian metric geometry and the GR chain,
- gauge-sector structure consistent with Standard Model symmetries,
- α-related derivation tracks with explicit proof-status discipline.

UBT **aims to recover GR as its classical geometric sector and may extend it**; it does not claim to replace or contradict GR.

---

## Multi-Channel Stability

The winding-mode effective potential $V_{\rm eff}(n) = n^2 - Bn\ln n$
has a stationary point at $n^* = e^{B/2 - 1}$.
For $B \approx 46.28$ (numerical observation [OBS]):
$n^* \approx 137$.

This is a **channel family** observation, not a derivation:
the potential selects a family of stable winding numbers
depending on the value of $B$. The identification $n^*=137$
with the fine-structure constant inverse $\alpha^{-1}$ is
[OBS] — a motivated conjecture, not a proved result.

In this sense, the effective $\alpha$ is channel-dependent.

**Alpha is NOT DERIVED from first principles.**
See `research_tracks/T3_ALPHA/` for the open Gap G137-B.

---

## Repository Layers (Authority Discipline)

### `canonical/`
Authoritative mathematical and physical core only:
- biquaternion algebra
- Θ-field definitions
- complex-time formulation
- covariant-tetrad metric emergence and GR chain
- gauge/QED/QCD/SM recovery tracks where mathematically formulated
- alpha derivation only with explicit proof status and open gaps

No claims of afterlife, soul, immortality, ThetaComm, or metaphysical ontology belong here.

### `research_tracks/`
Active scientific work not yet fully closed:
- alpha derivation attempts
- CMB/Planck diagnostics
- theta transforms and prime-stability studies
- lepton-spectrum work
- numerical experiments and reproducibility reports
- explicit conjectures and open gaps

### `speculative_extensions/`
Non-canonical exploratory hypotheses only:
- consciousness / psychons
- afterlife / survival-of-consciousness narratives
- ThetaComm and related proposals
- soul/immortality language
- Matrix/simulation and other metaphysical interpretations

### `ARCHIVE/`
Historical snapshots, deprecated or conflicting versions, superseded routes.

---

## Claim-Status Rule

No speculative or metaphysical claim may appear in `canonical/` or in the
abstract/introduction/conclusion of physics papers unless it is explicitly
marked as speculative and separated from the mathematical derivation.

For formal claim levels and repository scope policy, see
[`docs/UBT_SCOPE_AND_CLAIM_LEVELS.md`](docs/UBT_SCOPE_AND_CLAIM_LEVELS.md).

---

## Scaffolded Open-Gap Interfaces (No premature closure claims)

The repository now includes explicit scaffold interfaces for unresolved sectors:

- Quantum-sector scaffold: `src/ubt/quantum/quantum_scaffold.py`
- Soliton regularization scaffold: `src/ubt/solitons/regularization.py`
- Chirality/parity algebra scaffold: `src/ubt/algebra/chirality.py`
- Observable bridge scaffold: `src/ubt/observables/physics_observable_bridge.py`

These interfaces are designed to keep numerical experimentation reproducible
while explicitly preserving open derivation gaps. They must not be interpreted
as completed proofs of quantum closure, renormalization closure, weak-sector
closure, or precision-observable derivation.

See:
- [`docs/QUANTUM_ROADMAP.md`](docs/QUANTUM_ROADMAP.md) — phase-by-phase quantum development plan with explicit gap labels
- [`docs/quantum_sector_status.md`](docs/quantum_sector_status.md)
- [`docs/observable_bridge.md`](docs/observable_bridge.md)
- [`research_tracks/renormalization/finite_energy_soliton_regularization.md`](research_tracks/renormalization/finite_energy_soliton_regularization.md)
- [`research_tracks/weak_sector/chirality_and_parity_status.md`](research_tracks/weak_sector/chirality_and_parity_status.md)

---

## Quick Navigation

- Canonical derivation chain: [`DERIVATION_INDEX.md`](DERIVATION_INDEX.md)
- Claim-status matrix: [`CLAIMS_MATRIX.md`](CLAIMS_MATRIX.md)
- Scope and claim levels: [`docs/UBT_SCOPE_AND_CLAIM_LEVELS.md`](docs/UBT_SCOPE_AND_CLAIM_LEVELS.md)
- Quantum development roadmap: [`docs/QUANTUM_ROADMAP.md`](docs/QUANTUM_ROADMAP.md)
- Canonical theory tree: [`canonical/`](canonical/)
- Research tracks: [`research_tracks/`](research_tracks/)
- Speculative extensions: [`speculative_extensions/`](speculative_extensions/)
- History of the theory: [`docs/HISTORY_OF_UBT.md`](docs/HISTORY_OF_UBT.md)
- Historical archive: [`ARCHIVE/`](ARCHIVE/)

---

## How to cite

Jaroš, D. (2026). *Unified Biquaternion Theory: Emergent Lorentzian Geometry
and GR Recovery* (v10.1.3) [Software]. Zenodo.
https://doi.org/10.5281/zenodo.21347352

---

## License

Theory documents (LaTeX, Markdown): **CC BY-NC-ND 4.0**  
Code and scripts: **MIT License**  
Author: Ing. David Jaroš — see [`LICENSE.md`](LICENSE.md)
