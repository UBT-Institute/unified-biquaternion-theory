<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# G1 first negative control: a full-rank tetrad jet need not encode gravity

In the restricted attempt to extract e^a from a four-real-component
Hermitian chart H(phi)=phi^a sigma_a, the naive prescription

\[
e^a=d\phi^a
\]

has a 16×16 **identity** Jacobian from formal jet components
(d_mu phi^a) to e^a_mu. Yet whenever the Jacobian is invertible,
phi gives local coordinates and

\[
g=\eta_{ab}\,d\phi^a\,d\phi^b
\]

is locally the pullback of Minkowski space. Consequently Riem[g]=0.

An explicit nontrivial example, tested with exact symbolic
Christoffels and all Riemann components, is

\[
\phi^0=t,\quad\phi^1=x+t^2,\quad
\phi^2=y,\quad\phi^3=z;
\quad
g=-dt^2+(dx+2t\,dt)^2+dy^2+dz^2.
\]

This has nonconstant metric components and nonzero Christoffels,
yet every Riemann component vanishes. See
\`tests/test_theta_gradient_solder.py\`.

**Scientific meaning:** neither a 16-rank jet certificate nor
a coordinate-dependent metric is sufficient evidence of nontrivial
emergent gravitational curvature. This recovers the known
gradient/torsionless limitation relevant to #805/#807. It does
not preclude a nonintegrable **covariant** Theta derivative,
a genuinely derived conformal Cartan connection, or curvature
from a justified jet closure.

**Next positive target:** write an explicit local, Lorentz-real
candidate E(Theta, D_A Theta, A), with (1) exact local gauge
transformation law, (2) tetrad rank and nondegenerate signature,
(3) an exact curved example **without** freely importing an
independent tetrad, (4) full chain-rule first variation of a
declared nontrivial comparison action. Evaluate the #807 no-go
hypotheses before claiming an evasion. If no candidate survives,
record a scoped no-go rather than changing the carrier by fiat.
