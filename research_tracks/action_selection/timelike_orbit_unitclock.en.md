<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: timelike-orbit-unitclock.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact timelike-orbit kinematics; no complete UBT field equations established.
UBT-AI-PROVENANCE-END -->
# Timelike-orbit unit-clock theorem: nonradial Theta does not restore an independent lapse

**Status: EXACT KINEMATICS UNDER STATED REPRESENTATION / FULL UBT DYNAMICS OPEN.** This strengthens the RADIAL-GAUGE unit-gradient theorem of merged PR #684 and identifies which attempted escape fails. No additional fundamental action or new matter is introduced.

## Full positive-Hermitian Lorentz orbit

Take the standard future-timelike Hermitian Pauli slice of a biquaternion matrix (the extra factor i follows the existing Lorentz-real Theta convention). Assume a traceless single spin connection with the compatible two-sided action:

\[
\Theta=iX,\qquad X=\rho I+s_i\sigma_i=X^\dagger>0,\quad
r=\sqrt{\det X}=\sqrt{\rho^2-\lVert s\rVert^2}>0,\quad q=\sqrt{\mathcal N_0}.
\]

\[
DX=dX+\Omega X+X\Omega^\dagger,\quad
\Omega=\tfrac12(\boldsymbol\beta+i\boldsymbol\omega)\cdot\boldsymbol\sigma.
\]

Direct Pauli multiplication gives the scalar and three-vector components

\[
D\rho=d\rho+\boldsymbol\beta\cdot\mathbf s,\qquad
D\mathbf s=d\mathbf s+\rho\boldsymbol\beta-\boldsymbol\omega\times\mathbf s.
\]

The boost contributions cancel and the rotation contribution is orthogonal to the spatial vector. Consequently:

\[
\boxed{-\rho\,D\rho+\mathbf s\cdot D\mathbf s
=-\rho\,d\rho+\mathbf s\cdot d\mathbf s=-r\,dr.}
\]

Define the **composite** tetrad and central Lorentz metric in the given patch by

\[
E_\mu{}^a=(DX_\mu)^a/q,\quad g_{\mu\nu}=\eta_{ab}E_\mu{}^aE_\nu{}^b,
\quad\eta=\mathrm{diag}(-1,1,1,1).
\]

Whenever the coframe is invertible, contraction with its inverse yields the exact, gauge-independent unit-clock constraint

\[
\boxed{g^{\mu\nu}\partial_\mu r\,\partial_\nu r=-q^2=-\mathcal N_0.}
\]

This is **not** merely an artifact of imposing radial gauge. The invariant clock is the square root of the determinant of X, while rho itself is not gauge invariant. The identity holds pointwise for any smooth positive-Hermitian timelike X and compatible traceless spin lift. One may also exhibit a local explicit Lorentz rotation to radial gauge:

\[
S=\sqrt r\,X^{-1/2}\in SL(2,\mathbb C),\qquad
SXS^\dagger=rI.
\]

Since X is positive definite, its smooth positive inverse square root exists locally and det S is one. Thus the original radial proof cannot be evaded merely by keeping s_i nonzero while preserving exactly the same field representation and local Lorentz covariance.

## Consequence for the metric-only Einstein–Hilbert comparator

The exact projection lemma from merged PR #684 implies that when an **externally supplied metric-only** functional S[g[DTheta]] is pulled back to this timelike orbit, all boost/spatial tetrad variations can leave one normal Einstein component unconstrained; its equation takes the conserved clock-current form

\[
\mathcal E^{\mu\nu}=\lambda n^\mu n^\nu,\quad
\nabla_\mu(\lambda n^\mu)=0,\quad
n_\mu=\partial_\mu r/q,\quad n^\mu n_\mu=-1.
\]

Here the formula assumes no explicit scalar source in the metric functional and the same invertible coframe/independent boost chart. This is the familiar mimetic/dust mechanism, not novel UBT matter. Because the clock identity persists throughout the positive-Hermitian Lorentz orbit, adding offradial components s_i to Theta does **not** by itself restore an independently variable normal/lapse equation.

**Boundary of the claim:** this theorem neither determines the full UBT action nor rules out additional physical sectors, complex/non-Hermitian configurations, a genuinely independent connection field equation, a different invariant metric prescription, or a derived mechanism that imposes the missing normal equation. It does not independently prove the existence of a nonzero-dust solution for every possible microscopic action. It only shows that *this particular attempt to escape the known clock obstruction* fails at the geometric level.

## Verification and next discriminating research step

Exact matrix/Pauli algebra, Minkowski contraction, an invertible nonradial numerical-symbolic coframe and an explicit SL(2,C) radialization witness are independently checked by `tools/verify_timelike_orbit_clock.py` and its focused CI test. These are kinematic tests, not a proof of on-shell GR, ghost freedom, CMB predictions or physical topology selection.

**Next gate:** either show a unique covariant dynamical term of the *already declared one-Theta action family* enforces the normal Einstein projection without an auxiliary imposed constraint, or explicitly classify which assumption (timelike positive-Hermitian slice, metric-only dependence, traceless SL(2,C) connection, composite tetrad) must be changed. Without such a derivation, closed de Sitter from merged PR #688 remains an imported-EH comparator.

**Related work:** `research_tracks/action_selection/theta_unit_clock_mimetic_constraint.en.md` (merged PR #684); `research_tracks/action_selection/closed_clock_hamiltonian.en.md` (merged PR #688). Known mimetic gravity: https://doi.org/10.1007/JHEP11(2013)135.
