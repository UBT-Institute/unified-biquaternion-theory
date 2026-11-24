<!-- BILINGUAL-UNIT: holomorphic-compact-time-unitarity-2026-11-24 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional elementary functional analysis, not an on-shell UBT theorem, no derived action.
UBT-AI-PROVENANCE-END
-->
# Compatibility gate: holomorphic complex time, compact psi and unitary real-time dynamics

**24 November 2026. C_working, exact conditional theorem (L0); fundamental UBT dynamics OPEN.**

This is a new *consistency filter*, not a change to the locked Axiom B. The canonical time coordinate is \(\tau=t+i\psi\), but the axioms do **not** themselves impose all of the additional conditions below. In particular a periodic/compact \(\psi\), strong holomorphy of the physically evolving carrier, and a fixed self-adjoint real-time generator must not be silently inferred from Jacobi notation. The existing `canonical/bridges/theta_complex_time_bridge.md` explicitly separates its Jacobi modulus from physical \(\tau\).

## The simultaneous-assumption theorem

Let \(\mathscr H\) be a complex Hilbert space, let \(H\) be a fixed self-adjoint (possibly unbounded) operator, and let \(\Psi(t,\psi)\in\mathscr H\) be a sufficiently regular Hilbert-space-valued function on an imaginary-periodic complex-time cylinder. Assume: (A) **holomorphy** in \(\tau=t+i\psi\), so the Cauchy–Riemann relation holds in the common domain; (B) **unitary Schrödinger evolution** with the same generator in physical \(t\); (C) periodic imaginary time of period \(L>0\):
\[
\partial_\psi\Psi=i\partial_t\Psi,\qquad
i\partial_t\Psi=H\Psi,\quad H=H^\dagger,\qquad
\Psi(t,\psi+L)=\Psi(t,\psi).\tag{1}
\]
Thus
\[
\boxed{\partial_\psi\Psi=H\Psi,\qquad
\Psi(t,\psi+L)=e^{LH}\Psi(t,\psi).}\tag{2}
\]
Here \(e^{LH}\Psi\) is asserted only for vectors in its spectral domain; the assumed regular solution supplies the required domain. Periodicity and the spectral theorem give
\[
\boxed{(e^{LH}-I)\Psi=0
\ \Longrightarrow\ \Psi\in\ker H
\ \Longrightarrow\ \partial_t\Psi=0.}\tag{3}
\]
Indeed \(\lVert(e^{LH}-I)\Psi\rVert^2=\int_{\mathbb R}|e^{L\lambda}-1|^2\,d\mu_\Psi(\lambda)\). The integrand vanishes only at \(\lambda=0\) for real \(\lambda\). This theorem needs **self-adjointness, holomorphy and imaginary periodicity all at once**. It is not a universal prohibition of UBT dynamics.

## Equivalent exact finite-mode calculation

For \(L=2\pi R\), assume a finite periodic Fourier expansion, with \(R>0\),
\[
\Psi(t,\psi)=\sum_{n=-N}^N a_n(t)e^{in\psi/R}.
\]
The Cauchy–Riemann condition in (1) acts coefficientwise:
\[
\frac{in}{R}a_n=i\dot a_n
\quad\Longrightarrow\quad
\boxed{a_n(t)=a_n(0)e^{nt/R}.}\tag{4}
\]
For any nonzero \(n\), the amplitude grows/decays exponentially in *physical* real time. If additionally \(i\dot a_n=H a_n\) with \(H\) self-adjoint, a nonzero such mode would require an imaginary eigenvalue \(in/R\), a contradiction. The \(n=0\) mode has zero time frequency. A normally convergent infinite-mode extension obeys the same coefficientwise relation when differentiation and mode projection are legitimate.

A different analytic Jacobi factor
\[
f_n(t,\psi)=e^{i\omega_n t-\omega_n\psi}
=e^{i\omega_n\tau},\qquad \omega_n>0
\]
has a **real-time oscillating phase**, but it is *not periodic* in \(\psi\): \(f_n(t,\psi+L)=e^{-L\omega_n}f_n(t,\psi)\). In the conventional equation \(i\partial_t f_n=Hf_n\), this sign gives eigenvalue \(-\omega_n\), so the choice \(\omega_n=\pi n^2\) also gives an unbounded-below spectrum if interpreted directly as physical energy. Neither branch can be relabelled a healthy compact-psi physical Hamiltonian without changing assumptions or specifying a physical projection.

## Exact counterexample once holomorphy is dropped

The perfectly admissible **nonholomorphic** periodic unitary profile
\[
\Psi(t,\psi)=e^{-iEt}e^{in\psi/R}v,\qquad E\in\mathbb R,\ n\in\mathbb Z
\]
solves \(i\partial_t\Psi=E\Psi\) and is periodic for every \(n\), but
\[
\partial_\psi\Psi=\frac{in}{R}\Psi\ne
i\partial_t\Psi=E\Psi
\]
except the trivial joint case \(n=0,E=0\). Thus the no-go is caused by imposing **strong complex analyticity and periodic internal time on the same unitary quantum state**; neither compact internal coordinates nor unitarity alone is inconsistent.

## Physical decision and escape routes

The fundamental UBT \(\Theta\) is a *classical field object* until its physical Hilbert space and unitary quantum evolution have been derived; \(\Psi=\Theta\) is an **additional conditional identification**, not a canonical assertion. Hence the theorem cannot currently reject UBT as such. It rejects a particular often-implicit shortcut.

Viable alternatives must be explicit: (i) keep the Jacobi modulus/damping \(\phi\) distinct from the physical periodic \(\psi\), as the existing bridge already requires; (ii) use \(\psi\) as a noncompact imaginary-time coordinate with appropriate spectral domains, sacrificing winding interpretations; (iii) allow nonholomorphic dependence on \(t,\psi\), so compact Fourier winding and unitary real-time flow can coexist; or (iv) derive a nontrivial observable/constraint projection from the classical \(\Theta\) field to a distinct physical Hilbert state with unitary dynamics. None automatically selects the correct generator, torsion law, two graviton helicities or the fundamental action.

**Strict next dynamics gate:** specify which of \(\Theta\), Jacobi coefficients and operational quantum states obeys (1). Then derive the *actual* time-evolution equation, connection-dependent constraint map and reduced physical Hamiltonian. The theorem supplies a falsification test, not the missing microscopic \(S_{\rm UBT}[\Theta]\).

**Regression:** `tools/verify_complex_time_unitarity_gate_2026_11_24.py`, `research_tracks/fundamental_dynamics/tests/test_complex_time_unitarity_gate_2026_11_24.py`. Exact finite-mode symbolic checks for the Cauchy–Riemann relation, Fourier growth, self-adjoint spectral obstruction, Jacobi monodromy and explicit nonholomorphic counterexample. The infinite-dimensional statement follows from the spectral theorem under the declared domain conditions, not from finite tests. **LEAN-PENDING, semantic review pending.**
