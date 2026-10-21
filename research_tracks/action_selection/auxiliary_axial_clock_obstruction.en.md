<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: auxiliary-axial-clock.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Auxiliary independent-torsion comparator only; full UBT composite dynamics open.
UBT-AI-PROVENANCE-END -->
# Auxiliary axial torsion: exact failure to restore the missing normal constraint

**Status: CONDITIONAL EXACT RESULT.** The previous axial Clifford mixing result in merged PR #691 admits a sharper test against the unit-clock projection lemma of merged PR #684.

## Hypotheses

Work in the invertible positive-Hermitian timelike orbit and adopt the exact unit-clock identity:

\[
g^{\mu\nu}\partial_\mu r\,\partial_\nu r=-q^2,
\qquad q=\sqrt{\mathcal N_0},\quad r=\sqrt{\det X}.
\]

Independently vary a metric-compatible trace torsion vector t and axial pseudovector A with purely algebraic interactions. Restrict their sources to functions of this one clock times its gradient. The comparison density is

\[
\mathcal L_{\rm aux}/\sqrt{-g}=
\frac12 c_t\,t_\mu t^\mu+\beta\,t_\mu A^\mu+
\frac12 c_A\,A_\mu A^\mu+
f(r)\,\partial_\mu r\,t^\mu+
h(r)\,\partial_\mu r\,A^\mu.
\]

Coefficient beta and source h require parity-compatible pseudoscalar transformation laws if parity is preserved. They are comparison inputs, not derived UBT couplings. The algebraic torsion Hessian is

\[
K=\begin{pmatrix}c_t&\beta\\\beta&c_A\end{pmatrix},
\qquad \Delta=c_tc_A-\beta^2.
\]

## Exact elimination and witness

For nonsingular K, stationarity uniquely gives

\[
\boxed{
t_\mu=\frac{-c_A f+\beta h}{\Delta}\partial_\mu r,\qquad
A_\mu=\frac{\beta f-c_t h}{\Delta}\partial_\mu r.
}
\]

Substitution completes the square:

\[
\mathcal L_{\rm aux,on}=
-\frac{\sqrt{-g}}{2\Delta}
(c_A f^2-2\beta f h+c_t h^2)\,
g^{\mu\nu}\partial_\mu r\partial_\nu r.
\]

The constrained clock norm therefore makes this term an ordinary effective potential:

\[
\boxed{
\mathcal L_{\rm aux,on}=\sqrt{-g}W(r),\quad
W(r)=\frac{q^2}{2\Delta}(c_A f^2-2\beta f h+c_t h^2).
}
\]

An explicit nonzero axial field demonstrates the limitation:

\[
c_t=2,\ c_A=3,\ \beta=1,\ f=2,\ h=0
\quad\Longrightarrow\quad
t_\mu=-\frac65\partial_\mu r,\quad
A_\mu=\frac25\partial_\mu r,\quad W=\frac65q^2.
\]

Even though A does not vanish, no independent normal-metric variation has been introduced by eliminating these auxiliary fields. For vanishing currents the nonsingular torsion solution is zero.

## Singular case

If K is singular, stationary solutions require compatibility with the matrix kernel:

\[
\Delta=0\quad\Longrightarrow\quad
(\beta,-c_t)K=0,\qquad
\boxed{\beta f-c_t h=0}
\]

Failure gives no stationary torsion; compatibility leaves an undetermined auxiliary combination. A singular algebraic matrix alone is not evidence of a healthy Hamiltonian constraint or stable propagation.

## Why the clock residual survives

After elimination, the **independent-field metric-scalar comparator** is still a functional of g and r with an additional local W(r). The projected radial-Theta variation in merged PR #684 therefore allows a residual normal equation whose scalar-current evolution on FLRW is

\[
n_\mu=\partial_\mu r/q,\qquad
\nabla_\mu(\lambda n^\mu)=\frac q2\mathcal J(r),\qquad
\boxed{
\lambda(t)=\frac{a(t_i)^3\lambda_i-\frac q2
\int_{t_i}^t a(s)^3\mathcal J(s)\,ds}{a(t)^3}.
}
\]

The initial value lambda_i is arbitrary. Thus nonsingular auxiliary trace–axial mixing sourced solely by the clock gradient cannot **by itself** restore the missing independent Einstein normal equation. A varying Nieh–Yan coefficient of only this clock can similarly induce an axial gradient current without escaping this restricted conclusion.

**Essential limitation:** This is not the full UBT theorem. In UBT the tetrad e=DTheta/sqrt(N0) changes with the spin connection; the true composite connection Euler equation contains extra tetrad-variation terms, as recorded in draft PR #687. Eliminating torsion before imposing that dependence need not commute with the complete variation. Propagating spin curvature, independent nonmetric constraints, singular systems with secondary constraints and other Theta sectors remain open.

## Next discrimination

Derive or exclude a curvature four-form from the **existing single action**, perform full composite spin and Theta variation first, then inspect the local lapse equation and reduced-mode kinetic Hessian. Do not claim a CMB spectrum from this algebraic test.

**Reproducibility:** `tools/verify_auxiliary_axial_torsion_clock.py`, `tests/test_auxiliary_axial_torsion_clock.py`. Background: merged PR #684, merged PR #691, draft PR #687. Independent precedent: https://doi.org/10.1103/PhysRevD.104.064036.
