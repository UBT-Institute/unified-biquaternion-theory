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

# Information cycles, modular flow and the Hamiltonian reconstruction gate

**26 October 2026. Exact finite-dimensional theorem and conditional thermodynamic identity. Not a UBT Hamiltonian.**

## Spectral aliasing from discrete time
For a given sampling period T>0 and unitary U(T)=exp(-i H T/hbar), knowledge of U(T) cannot determine the spectrum of H uniquely. If H is diagonal in the basis of U, each eigenenergy E_j may be shifted independently by 2 pi hbar n_j/T, n_j integer, with the same sampled unitary. A common shift n_j=n is a physically unobservable global phase (exact U equality for integer n); unequal shifts cause distinct continuous-time relative phases despite equal stroboscopic dynamics. Counts of primitive cycles or Mobius inversion of iterates contain still less information than the full U(T), and cannot uniquely reconstruct H.

If U(T) has degenerate eigenvalues, additional logarithm branches and eigenbasis ambiguities arise. The same problem exists before attempting the UBT continuum and constraint structure.

## Conditional modular reconstruction
For a finite-dimensional full-rank Gibbs state rho=exp(-beta H)/Z, K=-log rho=beta H+log Z I. Hence H=(K-log Z I)/beta. This is an identity, NOT an independent derivation of H unless the state, Gibbs/KMS property relative to physical time, inverse temperature beta, normalization and reference algebra are supplied independently. The additive identity shift is physically conventional in nongravitational mechanics but may matter for composite gravity or cosmological sources; the vacuum reference and renormalization must be justified.

A pure global state gives singular -log rho off its support and does not supply a full-rank Gibbs generator. For observer-restricted local algebras K depends on wedge/region/state; these modular generators generally differ from one global physical Hamiltonian.

## Proposed UBT action/Hamiltonian selection test
1. Specify an observer-compatible Theta-to-quantum-state map rho_A[Theta] and algebra of observables, physical positivity and covariance.
2. Determine whether geometric causality implies a known modular flow in some wedge, and calibrate beta from an independently identified geometric boost or surface gravity, not fitted data.
3. Verify compatibility between overlapping observer algebras; test whether candidate generators induce one consistent derivation of shared observables. Check for state-dependent obstructions.
4. Recover a well-defined Lorentzian symplectic term and action, perform full Theta/composite-geometry chain-rule variation, and classify first-/second-class constraints. In particular test whether surviving SO(2) connection can be selected or is dynamical.
5. Prove boundedness of the physical reduced Hamiltonian and recover a nondegenerate graviton sector. Until then canonical/ACTION.en.md remains DEFINED_FAMILY_NOT_FINALIZED.

Mobius coefficients have an exact role in removing repeated periodic orbits of a defined dynamics, not selecting the dynamics or its energy scale.

Regression: tests/test_modular_hamiltonian_aliasing.py.
