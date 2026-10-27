<!-- BILINGUAL-UNIT: theta-period-two-hamiltonian-recurrence -->
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

# Jacobi T² periodicity and an exact conditional Hamiltonian recurrence

**2026-10-26.** This is the explicit check requested for Jacobi period two. Canonical source: `canonical/bridges/theta_parameter_separation.md`. Do NOT identify dimensionful UBT complex time tau_UBT=t+i psi with the dimensionless Jacobi parameter tau_J.

## An actual derived equality within a specified compact-circle spectral model

Let A=-partial_psi² on a circle psi ≡ psi+2 pi R, with eigenfunctions e^(in psi/R), n integer, eigenvalues lambda_n=n²/R². This choice is a **test spectral operator**, not a demonstrated reduction of the fundamental UBT Hamiltonian. Its heat trace is
 Z(s)=sum_{n∈Z} exp(-s n²/R²)=theta_3(0 | i s/(pi R²)), Re(s)>0.
For real-time unitary dynamics U(t)=exp(-i t A) (hbar=1), use an Abel regulator epsilon>0:
 Z_epsilon(t)=sum_n exp(-(epsilon+i t)n²/R²)
             =theta_3(0 | (-t+i epsilon)/(pi R²)).
By the Jacobi identity theta_3(tau_J+2)=theta_3(tau_J), the regulated trace satisfies
 Z_epsilon(t+T)=Z_epsilon(t), T=2 pi R².
Stronger, **the entire operator** U(t+T)=U(t) on this spectral Hilbert space, because exp(-i 2pi n²)=1 for every integer n. The Abel regulator is essential for convergence of the trace; on the real-time axis the unregulated trace sum is not trace-class, though the unitary operator recurrence is exact.

For physical units H=alpha A with energy coefficient alpha>0, U(t)=exp(-i Ht/hbar), so
 **T=2 pi hbar R²/alpha**.
This includes an undetermined alpha; the integer-square spectrum determines commensurability and recurrence, not the absolute mass/energy scale.

If the spectrum is perturbed E_n=alpha n²/R²+delta_n, exact recurrence at this T survives only when (delta_n-delta_0)T/hbar∈2 pi Z for all n. A global offset delta_0 contributes only a common unobservable phase. Generic perturbations break the recurrence.

## Why this does not give an oscillator mass

The prior half-line radial oscillator has gaps 2 hbar m for Dirichlet/Neumann, and recurrence up to global phase T=pi/m. Setting its T equal to 2 pi hbar R²/alpha yields m=alpha/(2 hbar R²), **conditional on a separately derived equality of clocks/generators**. There is currently NO UBT derivation identifying the radial and compact-circle generators or forcing their periods equal. Matching them by definition would be circular.

## Discriminating next step for Hamiltonian selection

Specify a physical, gauge-invariant Theta sector in which the circle Laplacian actually occurs in the **Dirac-reduced** Hamiltonian; prove its kinetic normalization alpha and R from the same action. Verify periodicity of phase-sensitive, gauge-invariant time correlators and distinguish from mere heat-trace modular rewriting. Correlation negentropy alone can be periodic or time-independent for many inequivalent H. Falsification: non-quadratic gaps generically spoil the universal return.

**Status:** exact conditional spectral-model bridge; periodicity-two checked, but neither unique H_UBT nor parameter-free particle masses follow. `tests/test_theta_period_two_hamiltonian_gate.py`.
