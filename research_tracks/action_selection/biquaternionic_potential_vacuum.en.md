<!-- BILINGUAL-UNIT: biquat-potential.scope -->
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

# A nonzero minimum of the existing biquaternionic potential

This is a constructive theorem for the already classified pointwise potential
of the original field `Theta`. The matrix representation uses all eight real
components of the same biquaternion. The result neither adds a potential term
nor selects its coefficients. It does not establish a vacuum of the full
spacetime action.

\[
X=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{Mat}(2,\mathbb C),\quad
H=2\operatorname{Re}(a\bar d)-|b|^2-|c|^2
=\operatorname{Re}\operatorname{tr}(\operatorname{adj}X\,X^\dagger),
\]
\[
V(X)=V_0+\mu H+\lambda_1H^2+\lambda_2|\det X|^2.
\]

Here `mu` denotes the coefficient written `m^2` in
`theta_potential_stability.en.md`; that notation does not require it to be
positive. The following sign region is an explicit assumption:
\[
\lambda_1\ge0,\qquad\lambda_2>0,\qquad\mu<0,\qquad
r=\sqrt{\frac{-\mu}{4\lambda_1+\lambda_2}}>0.
\]

<!-- BILINGUAL-UNIT: biquat-potential.minimum -->
## Global minimum and equality conditions

For every matrix in the stated domain,
\[
\boxed{V(X)\ge V_{\min}:=V_0-(4\lambda_1+\lambda_2)r^4.}
\]
Equality is attained at the nonzero Lorentz-real representative
\[
X_0=irI_2,\qquad H(X_0)=2r^2,\qquad |\det X_0|=r^2.
\]

**Proof.** First, the real-part estimate, the inequality between the arithmetic
and geometric means of the squared off-diagonal moduli, and the reverse
triangle inequality give
\[
H\le2|a||d|-2|b||c|
\le2\bigl||a||d|-|b||c|\bigr|\le2|ad-bc|.
\]
Writing \(\rho=|\det X|\), direct completion of squares gives the exact identity
\[
\boxed{
V(X)-V_{\min}
=\lambda_1(H-2r^2)^2+\lambda_2(\rho-r^2)^2
 +\lambda_2r^2(2\rho-H).
}
\]
All terms are nonnegative. Since \(\lambda_2r^2>0\), their sum vanishes
exactly when
\[
H=2r^2,\qquad \rho=r^2.
\]
Substitution of \(X_0\) proves attainment. These are exact invariant equality
conditions; this theorem alone does not classify global symmetry orbits.

The known unbounded ray \(X_t=t\operatorname{diag}(1,0)\) has
\[
H(X_t)=|\det X_t|^2=0,\qquad V(X_t)=V_0,\qquad
V(X_t)-V_{\min}=(4\lambda_1+\lambda_2)r^4>0.
\]
It proves noncoercivity but does not exclude this nonzero global minimum.
No instability of that minimum follows from the ray alone.

<!-- BILINGUAL-UNIT: biquat-potential.hessian -->
## Actual second variation in all field directions

Use the real coordinates
\[
x=(\operatorname{Re}a,\operatorname{Im}a,\operatorname{Re}d,\operatorname{Im}d,
\operatorname{Re}b,\operatorname{Im}b,\operatorname{Re}c,\operatorname{Im}c).
\]
At \(x_0=(0,r,0,r,0,0,0,0)\), the first derivative vanishes and, for every
\(v\in\mathbb R^8\), the actual second derivative is
\[
\begin{aligned}
\left.\frac{d^2}{dt^2}V(x_0+tv)\right|_{t=0}
=2r^2\bigl[&(4\lambda_1+\lambda_2)(v_1+v_3)^2\\
&+\lambda_2((v_0-v_2)^2+(v_4+v_6)^2+(v_5-v_7)^2)\bigr].
\end{aligned}
\]
The proof expands the original matrix polynomial along an arbitrary affine
variation and differentiates the resulting quartic twice. It does not
postulate a Hessian with the desired sign.

Thus the Hessian is positive semidefinite and is strictly positive in every
direction outside the kernel
\[
v_1+v_3=0,\quad v_0-v_2=0,\quad v_4+v_6=0,\quad v_5-v_7=0.
\]
In the displayed Euclidean coordinate norm its eigenvalues are
\[
4\lambda_2r^2\quad(3),\qquad
4(4\lambda_1+\lambda_2)r^2\quad(1),\qquad 0\quad(4).
\]
Parentheses give multiplicities; coincident positive eigenvalues combine
when \(\lambda_1=0\). These are eigenvalues of a pointwise potential Hessian,
not normalized physical masses.

The kernel is the span of the infinitesimal phase direction \(-rI_2\) and
the three boost directions \(ir\sigma_j\) at \(X_0\), where \(\sigma_j\) are
the Pauli matrices. Equivalently, it is the image of
\[
w\longmapsto r(-w_0,w_3,-w_0,-w_3,w_2,w_1,-w_2,w_1).
\]
The independent symbolic checker verifies that this map has rank \(4\),
is annihilated by the full Hessian, and exhausts its kernel. Declared symmetry
tangent directions are not automatically removable physical gauge modes.

<!-- BILINGUAL-UNIT: biquat-potential.tetrad -->
## Compatibility with the covariant tetrad

The architecture remains
\[
\Theta\in\mathbb C\otimes\mathbb H,\qquad
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\qquad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf1.
\]
Minimizing the pointwise potential is not sufficient to provide an admissible
spacetime background. In the branch where \(\Theta\) is Lorentz-real and the
defining connection preserves the Lorentz pairing, let
\[
q=(q^0,q^1,q^2,q^3),\qquad
\eta=\operatorname{diag}(-1,1,1,1),\qquad H=-2q^T\eta q.
\]
If a smooth field stays at the fixed invariant value \(H=2r^2\), pairing
compatibility implies
\[
0=\partial_\mu H=-4q^T\eta D_\mu q.
\]
Because \(q\ne0\), all four generated tetrad columns lie in the
three-dimensional orthogonal complement of \(q\). Therefore this constant
invariant ansatz gives
\[
\operatorname{rank}E\le3,\qquad\det E=0.
\]
This elementary rank argument is restricted to the stated pairing-preserving
branch. It does not cover a general two-sided relative connection. It prevents
identifying the pointwise minimizer with a nondegenerate spacetime vacuum
without checking the full defining connection and field equations.

<!-- BILINGUAL-UNIT: biquat-potential.verification -->
## Verification and remaining scope

`formal/lean/UBT/Action/PotentialVacuum.lean` formalizes the universal norm
inequality, global minimum, invariant equality conditions, negative-coefficient
parameterization, strict gap above the null ray, quartic variation identity,
actual second derivative, positivity and the four kernel equations.
The actual compiler, kernel-checker and axiom-audit result is recorded in
`reports/lean_volume_hessian_2026_09_09.json`. Its filename retains the initial
record date; its contents identify the checked commit and verification date.

`tools/verify_biquaternionic_potential_vacuum.py` independently checks the matrix
invariants, the gap identity, all gradient and Hessian entries, eigenvalues,
rank and kernel. The test is `tests/test_biquaternionic_potential_vacuum.py`.
The CAS calculation verifies exact polynomial identities; the universal norm
inequality is a separate analytic Lean proof.

The eigenvalue multiplicities, identification of the symmetry generators and
the conditional tetrad rank argument are not formalized in this Lean module.
The full composite action, its kinetic normalization, admissible spacetime
background, physical fluctuation measure, Einstein coefficient and Newton
constant remain to be derived. This theorem has no asserted implication for
RH. No canonical claim tier or author attestation is changed.
