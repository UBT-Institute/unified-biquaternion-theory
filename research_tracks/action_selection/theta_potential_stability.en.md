<!-- BILINGUAL-UNIT: theta-potential-stability.provenance -->
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

# Stability boundary of the classified Theta potential

<!-- BILINGUAL-UNIT: theta-potential-stability.scope -->
## Scope

For the exact invariant family already classified in
`theta_potential_invariants.en.md`, write

\[
V(X)=V_0+m^2H(X)+\lambda_1H(X)^2+\lambda_2D(X),
\qquad D(X):=|\det X|^2,
\]

with

\[
H(X)=2\operatorname{Re}(a\bar d)-|b|^2-|c|^2,
\qquad
X=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]

This note determines exactly when this polynomial is bounded below on
`Mat(2,C)` and proves its noncoercivity. Noncoercivity alone does not exclude
a nonzero minimum or establish the structure of the minimizing symmetry orbits.

<!-- BILINGUAL-UNIT: theta-potential-stability.inequality -->
## Universal inequality

For every complex `2 x 2` matrix,

\[
\boxed{H(X)\le 2|\det X|=2\sqrt{D(X)}.}
\]

Indeed,

\[
\begin{aligned}
H
&=2\operatorname{Re}(a\bar d)-|b|^2-|c|^2\\
&\le 2|a||d|-2|b||c|\\
&\le 2\bigl||a||d|-|b||c|\bigr|\\
&\le 2|ad-bc|.
\end{aligned}
\]

The first inequality uses both `Re(z) <= |z|` and
`|b|^2+|c|^2 >= 2|b||c|`; the last is the reverse triangle inequality.

<!-- BILINGUAL-UNIT: theta-potential-stability.boundedness -->
## Exact boundedness theorem [L1]

The potential `V` is bounded below on all of `Mat(2,C)` if and only if one of
the following mutually compatible cases holds:

1. `lambda1 > 0` and `lambda2 >= 0`, with arbitrary real `m^2`;
2. `lambda1 = 0`, `lambda2 > 0`, and `m^2 <= 0`;
3. `lambda1 = lambda2 = m^2 = 0`.

### Sufficiency

If `lambda1 > 0` and `lambda2 >= 0`, completing the square gives

\[
\lambda_1H^2+m^2H
\ge -\frac{(m^2)^2}{4\lambda_1},
\]

so `V` is bounded below.

If `lambda1 = 0`, `lambda2 > 0`, and `m^2=-mu <= 0`, then for `H <= 0`

\[
-\mu H+\lambda_2D\ge0.
\]

For `H>0`, the universal inequality gives `H <= 2 sqrt(D)`. With
`y=sqrt(D)` this implies

\[
-\mu H+\lambda_2D
\ge \lambda_2y^2-2\mu y
\ge -\frac{\mu^2}{\lambda_2}.
\]

The third case is the constant potential.

### Necessity

Exact one-parameter witnesses exclude every remaining sign choice:

- `X=t [[0,1],[0,0]]` has `H=-t^2`, `D=0`; hence `lambda1<0` is unbounded,
  and with `lambda1=0` it also excludes `m^2>0`;
- `X=t diag(1,i)` has `H=0`, `D=t^4`; hence `lambda2<0` is unbounded;
- if `lambda1=lambda2=0` and `m^2<0`, `X=t I_2` has `H=2t^2` and is
  unbounded below; the first witness handles `m^2>0`.

These cases exhaust the complement of the stated region.

<!-- BILINGUAL-UNIT: theta-potential-stability.flat -->
## Exact noncompact flat direction [L0]

For every real `t`,

\[
X_t=t\begin{pmatrix}1&0\\0&0\end{pmatrix}
\]

obeys

\[
H(X_t)=0,
\qquad
D(X_t)=0,
\qquad
V(X_t)=V_0.
\]

Therefore **no member of the complete connected-symmetry invariant quartic
potential family is coercive on the generic field space**. This statement
is coefficient-independent. The ray alone does not exclude isolated minima
elsewhere, nor determine isolation after quotienting by symmetries.

In fact, `biquaternionic_potential_vacuum.en.md` proves a nonzero global
minimum for `lambda1>=0`, `lambda2>0` and `m^2<0`. In that region the ray
lies strictly above the minimum, whose Hessian is positive transverse to its
displayed kernel. The previous inference from this ray to the impossibility
of any vacuum selection was too strong and is withdrawn.

This does not prove stability of the complete UBT action or identify physical
gauge directions. Those questions require its derivative, constraint and
configuration-space structure.

<!-- BILINGUAL-UNIT: theta-potential-stability.verification -->
## Verification

`tools/verify_theta_potential_stability.py` evaluates all exact witness rays
with Gaussian-rational arithmetic and checks the coefficient-case logic used
above. `tests/test_theta_potential_stability.py` keeps the witnesses and the
flat direction under CI.

The universal inequality is formalized as `H_le_twice_norm_det` in
`formal/lean/UBT/Action/PotentialVacuum.lean`; compiler and axiom-audit evidence
is recorded in `reports/lean_volume_hessian_2026_09_09.json`. The complete
necessary-and-sufficient boundedness classification in this note remains
`LEAN-PENDING`. Its proof is the explicit argument above, with independent
exact witness checks.

<!-- BILINGUAL-UNIT: theta-potential-stability.consequence -->
## Consequence for the single-action programme

The potential calculation now distinguishes:

- the invariant basis is exact;
- boundedness gives exact sign regions;
- the entire family retains a noncompact coefficient-independent flat
  direction;
- a nonzero global minimum exists in the stated negative-quadratic region.

Coefficient selection, the physical quotient and the full action Hessian
remain open. A valid microscopic background must satisfy the full equations
and have a nondegenerate covariant tetrad. The companion minimum theorem
explicitly checks why a constant-invariant potential ansatz is insufficient
in the Lorentz-pairing-preserving branch. There is no requirement to remove
every constant-potential ray merely because it exists above the minimum.
