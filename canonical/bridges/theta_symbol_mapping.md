<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->


> **2026-10-09 correction:** The old table used the same symbol `tau` for two different roles.  Use `tau_UBT=t+i psi` for canonical complex time and `tau_J` for a Jacobi modular parameter.  Do not map `phi -> psi` as a canonical identity.  The established spectral mapping is `tau_J(s)=i s/(pi R_psi^2)` for the compact-fibre heat trace.

# Theta-to-UBT Symbol Mapping

Status: Bridge support document

Purpose: This file prevents notation drift between the reduced theta complex-time construction and canonical UBT notation.

## Mapping Table

| Sprint Symbol | UBT Role | Status | Notes |
|---|---|---|---|
| $a_n$ | Reduced discrete mode amplitude / projected field component | Bridge | Not identified with the full canonical field $\Theta(q,\tau)$. |
| $s$ | External evolution index | Bridge | Use as an external label only. Do not confuse with real kernel time $t$ or with canonical spacetime coordinates. |
| $t$ | Real part of complex time $\tau$ | Canonical anchor | Compatible with canonical UBT real time. |
| $\phi$ | Positive damping parameter of the reduced toy kernel | Bridge | Not canonically identical to compact UBT $\psi$; a map must be derived. |
| $\tau_{\rm UBT}$ | Canonical complex time | Canonical anchor | $t+i\psi$ with compact internal $\psi$. |
| $\tau_J$ | Jacobi modular parameter | Mathematical theta variable | Lives in the upper half-plane. In the established KK heat trace, $\tau_J=i s/(\pi R_\psi^2)$. |
| $S_s(t,\phi)$ | Reduced theta amplitude / projected propagator-like observable | Bridge | Compatible with a reduced operator viewpoint, but not the full canonical field. |
| $\Theta_s(t,\phi)$ | Energy-like observable | Bridge | Strong notation conflict with canonical $\Theta(q,\tau)$. Prefer $\mathcal{E}_s(t,\psi)$ in UBT-facing text. |

## Conflicts with Existing UBT Notation

### 1. Conflict: $\Theta$

Canonical: In UBT, capital $\Theta$ is the fundamental biquaternion field.

Bridge: The sprint notation uses $\Theta_s(t,\phi)$ for an energy observable.

Resolution: In bridge material aimed at the UBT repo, keep the sprint formula when needed for traceability, but rename the reduced observable to

$$
\mathcal{E}_s(t,\psi) := |S_s(t,\psi)|^2
$$

and the averaged observable to

$$
\overline{\mathcal{E}}_s(t).
$$

This is the minimal renaming needed to prevent collision with the canonical field.

### 2. Conflict: $\phi$ versus $\psi$

Canonical: The scalar imaginary component of complex time is $\psi$.

Bridge: The sprint notation uses $\phi$ as the imaginary damping variable.

Resolution: Preserve $\phi$ only when quoting the reduced theta construction in its original notation. In UBT-facing equations, map

$$
\phi \mapsto \psi
$$

and state the mapping explicitly.

### 3. Potential Confusion: $s$ versus $t$

Bridge: The reduced model has two distinct temporal labels.

- $s$ is an external evolution label for the family of reduced mode sequences.
- $t$ is the real part of the internal complex-time kernel.

Resolution: Keep both symbols, but always describe them explicitly in bridge documents.

## Recommended UBT-Facing Form

For bridge documents inside the UBT repo, the preferred notation is

$$
S_s(t,\psi) = \sum_{n=0}^{N-1} a_n^{(s)} e^{-\pi \psi n^2} e^{\pi i t n^2},
$$

$$
\mathcal{E}_s(t,\psi) = |S_s(t,\psi)|^2,
$$

$$
\overline{\mathcal{E}}_s(t) = \frac{1}{P}\sum_{j=1}^{P} \mathcal{E}_s(t,\psi_j).
$$

Status: Bridge. This is a notation-adapted reduced formalism compatible with the isotropic complex-time limit of canonical UBT, not a replacement for the canonical field notation.
