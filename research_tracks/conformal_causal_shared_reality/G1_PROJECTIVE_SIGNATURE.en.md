<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: g1-projective-signature -->
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

# G1: composite phase/scale projection — a sharp positive-norm signature obstruction

**2026-10-28 · PR #809 · C_working · OPEN.** This is an exact finite-linear-algebra theorem about the restricted Mat(2,C) carrier. It does not fix Theta's fundamental dimension, construct a Lorentz connection or prove a physical gravity solution.

## Setup and covariant composite projector [PROVED, restricted]

Work in the realification of the same complex matrix carrier and the polarization B of its known SL(2,C) invariant H. Multiplication by i is a real complex structure J:

\[
V=\mathbb R^{2,6},\quad B\text{ of signature }(2,6),\quad
J\Theta=i\Theta,\quad B(JX,JY)=B(X,Y),\quad B(X,JX)=0.
\]

Let nabla^L be a **given** Lorentz-compatible two-sided connection and define a scalar norm, real scale 1-form and phase 1-form where N is nonzero:

\[
N=B(\Theta,\Theta)\ne0,\quad
j_\mu=\frac{B(J\Theta,\nabla^L_\mu\Theta)}{N},\quad
u_\mu=-\frac{B(\Theta,\nabla^L_\mu\Theta)}{N}.
\]

Their unique orthogonal subtraction in the two directions spanned by Theta and JTheta is the following projection:

\[
\mathscr D_\mu\Theta=\nabla^L_\mu\Theta
+u_\mu\Theta-j_\mu J\Theta
=P_\Theta\nabla^L_\mu\Theta,\quad
P_\Theta=1-\frac{\Theta\otimes B(\Theta,\cdot)
+J\Theta\otimes B(J\Theta,\cdot)}{N}.
\]

Direct algebra yields orthogonality and exact rank. These are off-shell pointwise statements, and rank six is a **target-space** projection rank, not a physical Dirac degree-of-freedom count:

\[
B(\Theta,\mathscr D_\mu\Theta)
=B(J\Theta,\mathscr D_\mu\Theta)=0,\quad
P_\Theta^2=P_\Theta,\quad \operatorname{rank}P_\Theta=6.
\]

Under local scale and local complex-phase transformations, assuming nabla^L has the appropriate Lorentz gauge transformation and commutes with J, one obtains:

\[
\Theta'=e^\lambda e^{\alpha J}\Theta,\quad
u'=u-d\lambda,\quad j'=j+d\alpha,\quad
\mathscr D'\Theta'=e^\lambda e^{\alpha J}\mathscr D\Theta.
\]

Consequently the normalized composite metric is invariant under these two transformations. No independent phase or scale 1-form is introduced:

\[
\widehat g_{\mu\nu}:=
\frac{B(\mathscr D_\mu\Theta,\mathscr D_\nu\Theta)}{|N|},
\qquad \widehat g'=\widehat g
\quad\text{under local scale and phase}.
\]

**Boundary:** these transformations do NOT demonstrate complete SU(2,2) Cartan covariance, since a full Lorentz/conformal connection and its dynamics have not been derived. The explicit examples use a chart with nabla^L=d.

## Positive-norm signature obstruction [PROVED, exact]

When N>0, the orthogonal vectors Theta and JTheta both have positive B-norm N. Since the full real B has inertia (2,6), they exhaust all available positive target directions. Sylvester's inertia theorem fixes the inertia of their B-orthogonal complement:

\[
N>0\ \Longrightarrow\
\operatorname{inertia}\bigl(B|_{\{\Theta,J\Theta\}^\perp}\bigr)
=(0,6),\qquad
\widehat g(v,v)\le0\quad\text{for all tangent }v.
\]

Every projected field derivative lies in that strictly negative six-plane, so the normalized composite metric is negative semidefinite in spacetime. It can be rank deficient or negative definite, but never Lorentzian of signature (1,3) on this branch. An exact affine tangent witness is:

\[
\Theta=I,\quad \nabla^L_\mu\Theta=(I,\sigma_1,\sigma_2,\sigma_3),
\quad \widehat g=\operatorname{diag}(0,-1,-1,-1).
\]

The obstruction holds for any jets and any Lorentz-compatible nabla^L, not just the displayed affine jet, **provided** the metric is built by this very projection of the declared fixed-inertia B and N>0. It does not exclude other metric readouts, additional carrier directions, a nonorthogonal first-order closure, null branches or independent constrained connections.

## Negative-norm escape branch [PROVED, pointwise existence only]

When N<0, the removed complex line is negative, and the complement is indefinite:

\[
N<0\ \Longrightarrow\
\operatorname{inertia}\bigl(B|_{\{\Theta,J\Theta\}^\perp}\bigr)
=(2,4).
\]

In particular, the following **pointwise jet** is B-orthogonal to Theta and JTheta and has Lorentzian normalized Gram matrix:

\[
\Theta=\sigma_1,\quad
\nabla^L_\mu\Theta=(I,\sigma_2,\sigma_3,i\sigma_2),\quad
N=-1,\quad \widehat g=\operatorname{diag}(1,-1,-1,-1).
\]

Such a jet can be realized by an affine smooth matrix field near the point, where N stays negative. This proves only local algebraic compatibility with Lorentz signature; it does NOT show the field is a UBT solution, Lorentz-real tetrad in the locked i·Herm readout, healthy graviton, or a background picked by information principles.

## Phase-only route versus simultaneous scale gauge [OPEN]

If one gauges the phase alone and retains the radial amplitude as physical, the composite phase derivative is:

\[
D_\mu^{\mathrm{phase}}\Theta
=\nabla_\mu^L\Theta-j_\mu J\Theta,\qquad
g^{\mathrm{phase}}_{\mu\nu}
=B(D_\mu^{\mathrm{phase}}\Theta,D_\nu^{\mathrm{phase}}\Theta).
\]

On the Hermitian affine background at Theta=I, the phase-only derivative reproduces the original Lorentzian flat Gram matrix and cancels arbitrary local phase drift. It does not transform covariantly under **local real scale** because a radial d-lambda term remains. The positive-norm no-go therefore rules out the **specific simultaneous scale-and-phase orthogonal quotient**, not the phase-only option.

**Scientific decision [OPEN]:** Do not conclude that shared reality or the information principle automatically demand both radial and phase redundancy. One must independently establish the physical gauge group. Test a phase-only composite connection on a nonflat regular Theta background, its strict reality, and first-order dynamical closure; or independently justify the negative-norm branch. G1 remains PARTIAL; no merge, no changes to #807/#808 or canonical UBT.

**Verification:** `python -m unittest discover -s tests -p 'test_theta_projective_signature.py' -v` (8 exact local SymPy tests). Previous scalar-observable bridge: `tests/test_theta_invariant_causal_bridge.py` (7 local tests). GitHub CI remains a separate gate.
