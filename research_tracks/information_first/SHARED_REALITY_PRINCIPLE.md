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

# Observer-independent shared reality: precise compatibility and dynamical obstruction

**2026-10-26. Candidate principle, not an established law, UBT fundamental action or Hamiltonian.**

## POIK (operational shared-reality principle)
For every observer O_i identify a local algebra A_i of operationally accessible observables, a positive normalized state rho_i thereon, and physical comparison maps on overlapping accessible events. Require compatible expectation values for jointly comparable measurement records, with appropriate frame/time and instrument maps. When observer domains are actual tensor-factor regions of a single physical state rho_ABC, compatibility means rho_AB and rho_BC have the same marginal rho_B. This is necessary for a shared state but **not sufficient** to guarantee that both marginals come from a common global state.

A globally consistent joint extension rho_ABC>=0, Tr rho_ABC=1, Tr_C rho_ABC=rho_AB, Tr_A rho_ABC=rho_BC is the stronger, falsifiable condition. This state extension problem is a quantum marginal problem; in QFT/gravity tensor factorization can fail, so replace matrices with consistent algebraic state restrictions and boundary/edge identifications.

## Exact obstruction: identical overlap marginals can be nonextendable

Use a three-qubit system A,B,C. Suppose observer AB assigns a Bell singlet pure state to AB, and observer BC independently assigns a Bell singlet pure state to BC. Both overlap marginals are I_B/2, so their shared B statistics coincide. But no common rho_ABC can have both: purity of AB forces rho_ABC=|singlet><singlet|_AB tensor rho_C, hence rho_BC=(I_B/2) tensor rho_C, never an entangled Bell singlet. Thus pairwise comparison consistency without extension is too weak. This is monogamy of entanglement, not spiritual observer-dependent creation of reality.

## Exact obstruction: existence of shared reality does not select the Hamiltonian

For any initial rho_ABC and ANY self-adjoint global H, rho_ABC(t)=e^{-itH}rho_ABC(0)e^{itH} defines mutually consistent observer marginals rho_AB(t), rho_BC(t). In particular H=0 and H=omega Z_B are distinct, and both satisfy all compatibility/extension constraints over time, while giving different measured dynamics. Therefore POIK alone, even demanded at every time, does not derive or uniquely select H, nor the single-Theta action. This is a rigorous no-selection benchmark. Do not infer GR or a graviton from shared state consistency.

## Stronger candidate: dynamical gluing and causal covariance
To select dynamics, require *additional independently motivated content*: causal nets of algebras A(O), consistent restrictions/inclusions, microcausality, suitable state conditions (Hadamard/KMS where applicable), composite Lorentzian g[Theta], physically calibrated local time evolution, and covariance of corresponding derivations. No fixed Hamiltonian is selected by these axioms in general: many distinct local QFTs can satisfy them. Therefore any uniqueness theorem must say exactly which extra UBT geometric/biquaternionic datum removes the residual model freedom.

Promising discriminant: require the quantum relative entropy under restriction obey data processing, then require Theta geometric response to modular energy, and compute the full symplectic/Dirac structure without assuming Einstein dynamics or prescribing SO(2) connection. Check possibility of nontrivial family before uniqueness claims.

Status: principle candidate and explicit counterexamples. The observer is any physical information-processing system, not necessarily human or conscious. This program deliberately avoids claiming subjective consciousness causes measurement outcomes.

Regression: tests/test_shared_reality_quantum_marginals.py.
