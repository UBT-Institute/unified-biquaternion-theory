<!-- BILINGUAL-UNIT: hamiltonian-correlator-reconstruction -->
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

# Hamiltonian reconstruction gate from shared-negentropy dynamics

**2026-10-26. Exact finite-dimensional inverse-dynamics theorem and falsification test; not the microscopic UBT Hamiltonian.** Complements `SHARED_NEGENTROPY_CORRELATION.en.md` and existing `MODULAR_HAMILTONIAN_RECONSTRUCTION_GATE.md`.

## What entropy fails to measure
A pure Bell pair |Phi+>=(|00>+|11>)/sqrt(2) has J(A)=J(B)=0, I(A:B)=2 ln 2. Evolve with H0=0 or H1=omega (sigma_z tensor I), omega!=0. Both give the SAME local entropies and mutual information for all t, because H1 is local-unitary: |Phi(t)>=(exp(-i omega t)|00>+exp(+i omega t)|11>)/sqrt(2). Nevertheless the phase-sensitive correlator <sigma_x tensor sigma_x>=cos(2 omega t) (while H0 yields 1). Thus even complete time histories of J_A,J_B,I_AB need not recover H; shared-reality consistency is satisfied by both.

## Actual inverse-commutator reconstruction
For a fixed finite-dimensional Hilbert space with *independently defined time variable*, full state rho(t) and unitary von Neumann dynamics:
   dot rho=-i[H,rho].
Diagonalize rho at t0: rho=diag(p_1,...,p_d). For p_i != p_j,
   H_ij=i dot rho_ij/(p_j-p_i).
For p_i=p_j, consistency requires dot rho_ij=0 in the eigenbasis; even for nondegenerate rho, diagonal H_ii remain unobservable to first order. Thus from one state trajectory at an instant the generator is defined only modulo Hermitian operators commuting with rho. In a degenerate sector the ambiguity includes an entire matrix block. Multiple independent known state preparations may reduce the common commutant to scalar multiples of identity, enabling reconstruction up to an irrelevant energy origin, **conditional on complete time-resolved tomography** and a common unitary generator.

For UBT, a gravitational Hamiltonian is constrained (often a sum of first-class constraints and boundary generators), so the finite-dimensional formula is only a precision benchmark, not a license to identify observer modular generators with global H_UBT.

## Route B criterion with an operational output
1. From an actual candidate Theta action, derive reduced positive Hilbert space and shared local observable algebras; include gauge/gravitational edge modes.
2. Obtain enough time-dependent **phase-sensitive** cross-observer correlators (not just entropy) to constrain commutator dynamics.
3. Check whether a generator exists, whether independent observer descriptions agree on overlaps, and whether its reduced Dirac/Noether charges reproduce MM gravity.
4. Without dynamics/tomography, correlation-negentropy remains a consistency/selection score, not a Hamiltonian derivation.

**Immediate answer:** a purely static or entropy-history functional cannot uniquely select H. The nearest rigorous Hamiltonian route is correlator *dynamics* plus a physical state/Poisson structure, not maximizing J by itself.

Regression: `tests/test_information_hamiltonian_correlator_reconstruction.py`.
