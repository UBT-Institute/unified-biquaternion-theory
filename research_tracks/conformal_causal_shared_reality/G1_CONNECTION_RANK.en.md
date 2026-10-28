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

# G1: real dilation restores metric variation rank but not dynamics

**2026-10-28 · PR #809 · C_working.** This compares the restricted
Lorentz-real jet with PR #807, without changing its no-go theorem.

## Rank lemma [PROVED, pointwise]

At a timelike Hermitian value X=rI (r>0), use the two-sided derivative
D X = dX + Omega X + X Omega† and vary Omega while keeping X and dX
fixed. A trial connection variation is

\[
 \delta\Omega_\mu=\tfrac12\beta^i_\mu\sigma_i
       +\tfrac i2\vartheta^i_\mu\sigma_i
       +\tfrac12u_\mu I.
\]

The real u term is NOT in the original Lorentz algebra sl(2,C);
it is an explicitly proposed enlargement. Matrix multiplication gives

\[
 \delta(D_\mu X)=r(\beta_\mu^i\sigma_i+u_\mu I).
\]

Thus boosts supply 3 real jet components per spacetime direction,
rotations annihilate this X, and real dilation supplies the fourth.
At a regular point e^a_mu=delta^a_mu and eta=diag(1,-1,-1,-1),
the exact linear symmetric-metric variation

\[
 \delta g_{\mu\nu}=\eta_{ab}
   (e^a_\mu\delta e^b_\nu+e^a_\nu\delta e^b_\mu)
\]
has
\[
 \boxed{\mathrm{rank}(\partial g/\partial\beta)=9,\qquad
        \mathrm{rank}(\partial g/\partial(\beta,u))=10.}
\]

The pure-boost map cannot vary g_00 in this local frame. The complete
coframe jet map is 16→16 full-rank only *at fixed X* and with freely
variable boost + dilation connection components. The rank-10 result is
**not** a Dirac mode count, a Hamiltonian or an SU(2,2) representation.
Executable check: tests/test_theta_connection_metric_rank.py.

## Exact dilation lemma [PROVED, restricted]

Write Omega=Omega_L+(u/2)I with real 1-form u and Lorentz Omega_L.
The two-sided derivative is

\[
 D^\Omega\Theta=D^{\Omega_L}\Theta+u\Theta.
\]

On a local patch where u=dσ, the exact identity is

\[
 \boxed{D^{\Omega_L+(dσ/2)I}\Theta
          =e^{-σ}D^{\Omega_L}(e^σ\Theta).}
\]

The central curvature is (du/2)I=0. Exact dilation is therefore
locally equivalent to a real field rescaling. If real Weyl rescaling
is a symmetry of the FULL action, it is gauge redundancy; if not,
the scalar profile can matter and cannot be discarded on symmetry
grounds. This is **not** a claim that the metric itself is invariant.

For the purely radial case Theta=r(x)I, Omega_L=0, u=d log r,
the jet becomes 2 dr I and its coframe has rank at most one.
The flat exact-dilation case therefore does not generate gravity
by itself. If du≠0, the dilation has a new curvature channel whose
equations, constraints and physical modes remain unknown.
Exact checks: tests/test_theta_exact_dilation.py.

## Why the apparent shortcut would be circular [CONDITIONAL]

For a *borrowed* Einstein–Hilbert functional S_EH[g(Theta,Omega)],
freely varying enough auxiliary boost and real-dilation components
can span ten off-shell metric directions and hence transmit the
Einstein metric Euler equations by the chain rule. But that means
we have supplied the freely variable coframe through the independent
connection rather than **derived** it from Theta, causal geometry or
shared reality. This is legitimate as an effective first-order
comparator, not a microscopic UBT proof.

Conversely the previously studied gradient metric g=B(dTheta,dTheta)
under a borrowed EH action has only the Regge–Teitelboim projected
equations G^{mu nu} b^A_{mu nu}=0 and explicit non-Einstein stationary
solutions; see G1_RT_EXTRA_SOLUTION.en.md.

## Remaining noncircular G1 gate [OPEN]

Derive a gauge-covariant closure for the connection, or a constrained
first-order connection principle, that is compatible with Theta's
carrier and Lorentz reality and simultaneously supplies:
(1) a nonflat regular background, (2) sufficient *allowed* metric
variations without freely importing a tetrad, (3) a reduced healthy
two-helicity linear graviton sector, and (4) explicit quantitative
causal/shared-reality constraints. An exact u=dσ choice is insufficient;
an unconstrained arbitrary u only shifts the problem to the connection.

G1 remains PARTIAL. No full SU(2,2)-equivariant solder form, UBT action,
Dirac analysis or physical spectrum is established. STOP for independent
scientific review before moving to G2–G4.
