<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: g1-complex-theta-real-coframe -->
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

# G1: a real curved tetrad reconstructed from complex phase-covariant Theta

**2026-10-28 · PR #809 · C_working · RESTRICTED CONSTRUCTION.** The mathematical distinction is essential: a real metric and a real tetrad can be composite observables of a genuinely complex field. The direct-jet reality obstruction in G1_PHASE_STRICT_REALITY applies only when one additionally identifies each projected derivative with a Hermitian coframe leg; it does not forbid this metric-factorization route.

## A complex field and a real metric [PROVED, restricted]

Use an explicit regular local Mat(2,C) trial chart, not a fundamental dimensionality postulate:

\[
\Theta=(t+2)I+x\sigma_1+y\sigma_2+z\sigma_3+i\kappa tx\,\sigma_1,
\qquad \kappa\in\mathbb R.
\]

The known real Lorentz-congruence invariant form on this chart gives:

\[
B(P,Q)=\tfrac14\bigl(H(P+Q)-H(P)-H(Q)\bigr),\quad
H(Q)=\operatorname{Tr}(Q^\sharp Q^\dagger),\quad
N=B(\Theta,\Theta)=(t+2)^2-x^2-y^2-z^2-\kappa^2t^2x^2.
\]

On a patch N>0 (or merely N nonzero for the phase current), define a composite connection and metric:

\[
j_\mu=\frac{B(i\Theta,\partial_\mu\Theta)}{N},\quad
\nabla^{\rm ph}_\mu\Theta=\partial_\mu\Theta-i j_\mu\Theta,\quad
g_{\mu\nu}=B(\nabla^{\rm ph}_\mu\Theta,\nabla^{\rm ph}_\nu\Theta).
\]

Since B is invariant under multiplication by a complex unit phase, the exact local phase transformation is:

\[
\Theta'=e^{i\alpha(x)}\Theta,\qquad j'=j+d\alpha,\qquad
(\nabla^{\rm ph}\Theta)'=e^{i\alpha(x)}\nabla^{\rm ph}\Theta,
\qquad g'=g.
\]

This local phase covariance is a **feature of this metric comparator**, not a claim that the original full UBT action already gauges U(1), nor proof of SU(2,2) Cartan covariance. The Lorentz connection was frozen to zero for this example; no independent phase gauge field was inserted.

The exact current and real Gram metric are:

\[
j=-\frac{\kappa x^2}{N}\,dt,\qquad
ds^2=dt^2-dx^2-dy^2-dz^2
-\kappa^2(x\,dt+t\,dx)^2-\frac{\kappa^2x^4}{N}\,dt^2.
\]

## An explicit real coframe without a free tetrad [PROVED, local kinematics]

Write its nontrivial timelike two-dimensional block using coefficients:

\[
a:=g_{tt}=1-\kappa^2x^2-\frac{\kappa^2x^4}{N},\quad
b:=g_{tx}=-\kappa^2tx,\quad
c:=g_{xx}=-1-\kappa^2t^2,\quad
\Delta:=b^2-ac.
\]

On the regular time-oriented patch, define the following real one-forms **entirely algebraically from g[Theta]**:

\[
a>0,\quad\Delta>0,\quad
e^0=\sqrt a\,dt+\frac b{\sqrt a}\,dx,\quad
e^1=\sqrt{\frac{\Delta}{a}}\,dx,\quad
e^2=dy,\quad e^3=dz.
\]

Direct multiplication shows that this is a real nondegenerate tetrad and gives an i-Hermitian matrix-valued realization:

\[
g=\eta_{ab}e^a\otimes e^b,\quad
\eta=\operatorname{diag}(1,-1,-1,-1),\quad
\det(e^a{}_\mu)=\sqrt{\Delta}\ne0,\quad
E_\mu=i\sum_{a=0}^3 e^a{}_\mu\sigma_a\in i\operatorname{Herm}_2.
\]

At a regular point the metric is manifestly Lorentzian; at the origin a nonzero curvature component is exact:

\[
g\big|_{(t,x,y,z)=(1,0,0,0)}
=\operatorname{diag}(1,-1-\kappa^2,-1,-1),\quad
R_{txtx}(0)=\kappa^2.
\]

In particular, the complex projected jet is not Hermitian at the displayed regular point, while the **derived** E is i-Hermitian:

\[
\nabla^{\rm ph}_x\Theta\big|_{(1,0,0,0)}
=(1+i\kappa)\sigma_1\notin\operatorname{Herm}_2
\quad(\kappa\ne0),\qquad E_x\in i\operatorname{Herm}_2.
\]

No contradiction: physical reality constrains the composite readout, not all intermediate complex algebraic objects. The earlier direct-jet rank theorem must not be imposed on this distinct construction.

## Gauge meaning and limitations [OPEN]

The factorization has a local frame ambiguity:

\[
e^a{}_\mu\longmapsto\Lambda^a{}_b\,e^b{}_\mu,
\qquad\Lambda^T\eta\Lambda=\eta,
\qquad \Lambda(x)\in SO^+(1,3)
\]

This is the usual Lorentz gauge freedom of the *derived* real frame, not an independent physical tetrad field. A coordinate time direction and local time orientation are used to present the factorization, but the metric is constructed without that choice; a global smooth tetrad, spin bundle, or observer-invariant timelike orientation is not established.

The induced metric is the restricted B(DTheta,DTheta) **trial readout**; it has NOT been proved equivalent to the locked canonical UBT central anticommutator metric. The field is kinematical, not an on-shell solution of a selected action. No microscopic Hamiltonian, Dirac constraint closure, positive graviton spectrum, matter coupling, or unique Newton constant follows.

**Next gate [OPEN]:** Prove a noncircular relation to the canonical central-antocommutator geometry, then vary a genuine Theta-derived action and calculate the reduced spin-two principal symbol. The direct-jet restriction is kept as a scoped negative control, not as a required axiom for all realizations. PR #809 remains draft, G1 PARTIAL, PR #807/#808 untouched; no merge.

**Verification:** Exact symbolic tests in `tests/test_theta_phase_real_derived_coframe.py` (7 test cases). This is separate from CI acceptance.
