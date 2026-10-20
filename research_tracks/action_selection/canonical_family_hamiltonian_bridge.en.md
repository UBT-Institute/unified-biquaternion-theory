<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional mathematical derivation, not finalized fundamental UBT action.
UBT-AI-PROVENANCE-END -->

# Canonical-family Hamiltonian and exact test-sector reduction

**Status: mathematical derivation under explicit assumptions; fundamental closure OPEN.** This is a Legendre transform of the family recorded in canonical/ACTION.en.md, not an additional competing fundamental action.

## Proposition 1 — fixed-background Hamiltonian

Represent the biquaternion field by eight real components q^A. Assume a fixed ADM metric of signature (-+++), lapse N>0, shift N^i, spatial metric h_ij, a fixed linear two-sided connection with D_t q = dot q + Omega_0 q, and a real symmetric nondegenerate kinetic matrix K_AB. With c nonzero and U(q) an unspecified real potential, define the **conditional realization of the existing family**

\[
S=\int dt\,d^3x\,N\sqrt h\left[
\frac{c}{2N^2}K_{AB}v^Av^B
-\frac c2h^{ij}K_{AB}(D_iq)^A(D_jq)^B-U(q)\right],
\quad v^A=(D_tq)^A-N^i(D_iq)^A.
\]

This ADM sign convention is explicitly chosen, not derived from a unique microscopic UBT action. Then

\[
\pi_A=\frac{c\sqrt h}{N}K_{AB}v^B,\qquad
v^A=\frac{N}{c\sqrt h}(K^{-1})^{AB}\pi_B.
\]

The Legendre transform gives the **exact fixed-background Hamiltonian density**

\[
\boxed{\mathcal H=
N\left[\frac{\pi_A(K^{-1})^{AB}\pi_B}{2c\sqrt h}
+\sqrt h\left(\frac c2h^{ij}K_{AB}(D_iq)^A(D_jq)^B+U(q)\right)\right]
+N^i\pi_A(D_iq)^A-\pi_A(\Omega_0q)^A.}
\]

**Proof:** Substitute dot q = v + N^i D_i q - Omega_0 q into pi dot q - L and eliminate v using the momentum relation. This is algebraic and exact under the assumptions. If the metric or connections are independent dynamical fields or composites of q, the full canonical momenta and constraints differ; this is NOT the gravitational ADM constraint.

## Proposition 2 — reduction map to the existing dodecahedral Hamiltonian

Assume q=bar q+Q phi, with K(Q,Q)=1, D_mu Q=0, D_mu bar q=0, vanishing linear potential term, decoupled transverse channels, and U(bar q+Q phi)=U(bar q)+m_eff^2 phi^2/2+O(phi^3). Choose c=1 as a **sector normalization**, not a fundamental parameter prediction. On a *prescribed* FLRW quotient background N=1, shift=0, h_ij=a(t)^2 h0_ij, the quadratic action is

\[
S_\phi^{(2)}=\frac12\int dt\,d\mathrm{vol}_{h0}\,a^3
[\dot\phi^2-a^{-2}|\nabla_{h0}\phi|^2-m_{\rm eff}^2\phi^2].
\]

Expand phi=sum_{n,j} u_nj(t) Y_nj(x), with orthonormal eigenfunctions -Delta_h0 Y_nj=lambda_n Y_nj. Then

\[
p_{nj}=a^3\dot u_{nj},\quad
\boxed{H_\phi^{(2)}=\frac12\sum_{nj}
\left[a^{-3}p_{nj}^2+a^3(\lambda_n/a^2+m_{\rm eff}^2)u_{nj}^2\right].}
\]

For h0=R_c^2 gamma on S^3/(binary icosahedral group), lambda_n=n(n+2)/R_c^2 on the allowed invariant modes. This **recovers exactly** the test Hamiltonian already proved in research_tracks/dodecahedral_action_cmb/DERIVATION.md. It is a conditional reduction from the existing family, not a new unrelated postulate.

**Unproved dynamical inputs:** existence and selection of bar q, a physical gauge-invariant Q, absence of mixing with other seven real components, positive kinetic signature on physical modes, the compact quotient topology, and backreaction. The chosen K is not thereby proven to be Lorentz-invariant.

## Proposition 3 — fixed-background ghost obstruction

If cK has a negative eigenvalue and there is no constraint on its conjugate momentum, the kinetic Hamiltonian pi^T K^{-1} pi/(2c sqrt h) is unbounded below: scale pi along a negative eigendirection. Thus an indefinite nondegenerate pairing cannot define an unconstrained stable eight-component test-field Hamiltonian. This is **not** a no-go for a constrained full UBT model; one must compute its first-class constraints and physical quotient.

## Proposition 4 — unique invariant kinetic form and signature (exact algebra)

The invariant-potential classification in
theta_potential_invariants.en.md establishes that the real quadratic
invariants of the declared U(1) x SL(2,C) congruence representation are
spanned by

\[
H(X)=\operatorname{Tr}(X^\sharp X^\dagger).
\]

Polarizing H therefore gives the only nonzero invariant constant symmetric
bilinear kinetic form, up to an overall scalar, **if the derivative field
transforms in that same representation**. Explicitly, write a completely
general complex matrix as

\[
X=(u_0+iv_0)I+\sum_{j=1}^3(u_j+iv_j)\sigma_j,
\quad u_\alpha,v_\alpha\in\mathbb R.
\]

The 2-by-2 adjugate and Pauli identities yield

\[
\boxed{H(X)=2(u_0^2+v_0^2-\mathbf u^2-\mathbf v^2).}
\]

Its real quadratic-form matrix, in the order
\((u_0,u_1,u_2,u_3,v_0,v_1,v_2,v_3)\), is

\[
K=2\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1),
\quad\operatorname{inertia}(K)=(2,6).
\]

**Result:** the minimal *unconstrained, fixed-background* quadratic kinetic
family with this exact connected symmetry has a negative Hamiltonian
direction for either choice of nonzero kinetic sign \(c\).
A positive Hilbert--Schmidt replacement is NOT invariant under the declared
full noncompact spin congruence action. This excludes a straightforward
positive-energy eight-component realization, not a theory with additional
genuine first-class constraints or a different declared representation.

## Proposition 5 — symmetry-normal modes at the established nonzero minimum

Use **the same** invariant quartic potential already classified and minimized
in biquaternionic_potential_vacuum.en.md:

\[
U(X)=V_0+\mu H(X)+\lambda_1 H(X)^2+\lambda_2|\det X|^2,
\quad
\lambda_1\ge0,\ \lambda_2>0,\ 
\mu=-(4\lambda_1+\lambda_2)r^2,\ r>0.
\]

It has a pointwise global minimizer \(X_0=irI\).
The phase direction \(\delta X=-rI\) and the three boost directions
\(\delta X=ir\sigma_j\) span its four-dimensional orbit under the declared
connected symmetry. The three rotation generators stabilize \(X_0\).
The **K-orthogonal normal** is spanned by
\(\delta X=i\,\delta v_0 I+\sum_j\delta u_j\sigma_j\).

On this normal, direct differentiation of the original quartic gives

\[
\begin{aligned}
K_{\perp}&=2\,\operatorname{diag}(1,-1,-1,-1),\\
M_{\perp}&=\operatorname{Hess}U|_{\perp}
=8r^2\,\operatorname{diag}(4\lambda_1+\lambda_2,
                            \lambda_2,\lambda_2,\lambda_2),\\
K_{\perp}^{-1}M_{\perp}
&=4r^2\,\operatorname{diag}(4\lambda_1+\lambda_2,
                         -\lambda_2,-\lambda_2,-\lambda_2).
\end{aligned}
\]

The orbit directions lie in \(\ker\operatorname{Hess}U\);
the normal is orthogonal to the orbit in the invariant pairing, and has
signature **(1,3)**. This is stronger than the eight-component
signature calculation: *simply quotienting the four phase/boost tangent
directions cannot make the remaining normal kinetic metric positive*,
provided the normal remains a propagating subspace of the frozen-background
realization.

On a local frozen Minkowski background with vanishing connection,
homogeneous normal perturbations have the quadratic Lagrangian

\[
L^{(2)}_\perp
=c\left[(\dot{\delta v}_0)^2-
       \sum_j(\dot{\delta u}_j)^2\right]
-4r^2\left[(4\lambda_1+\lambda_2)(\delta v_0)^2
 +\lambda_2\sum_j(\delta u_j)^2\right].
\]

The associated equations are

\[
c\,\ddot{\delta v}_0+4r^2(4\lambda_1+\lambda_2)\delta v_0=0,
\qquad
c\,\ddot{\delta u}_j-4r^2\lambda_2\delta u_j=0.
\]

For \(c>0\) the three normal-vector modes grow exponentially;
for \(c<0\) the scalar normal mode grows exponentially. Hence this
**specific unconstrained fixed-background vacuum linearization** cannot
have only stable propagating normal modes with the invariant pairing,
regardless of kinetic sign.

**Crucial scope:** the constant vacuum with zero connection has
\(D_\mu X_0=0\) and therefore a *degenerate composite tetrad*.
It is **not** an admissible nondegenerate vacuum of completed UBT gravity.
Moreover, the orbit is a symmetry orbit; identifying it as a removable
*local gauge orbit* requires the full gauge transformations, dynamical
connections and Dirac constraint algebra. This theorem does **not** prove
that the complete composite, potentially constrained UBT has a ghost.
It gives a sharp obstruction any claimed completion must evade and
a counterexample to inferring stability from the pointwise positive
potential Hessian alone.

**Exact computational certificate:**
tools/verify_theta_kinetic_signature.py checks the Pauli-matrix
expansion, 8-real Hessian, 4+4 orbit/normal decomposition, full potential
gradient/Hessian and generalized normal eigenvalues symbolically.
tests/test_theta_kinetic_signature.py is a regression check. The
checker was executed independently with SymPy 1.14 and its focused
pytest passed (1 test). Full repository CI and the Dirac algebra have
**not** been checked by that local execution.

## Proposition 6 — the bare kinetic/potential family contains no propagating Yang--Mills connection (tree-level)

Treat a connection \(C_\mu^a\) as an independent field entering only the
covariant derivative \(D_\mu X=\partial_\mu X+C_\mu^aT_aX\),
in the linear representation defined above, with **no** curvature
\(F_{\mu\nu}F^{\mu\nu}\) or other connection-derivative term in the
family action. On a prescribed metric the infinitesimal connection variation
is exact:

\[
\delta_{C} S
=c\int d^4x\,\sqrt{-g}\,g^{\mu\nu}
B(T_aX,D_\nu X)\,\delta C_\mu^a,
\]

where \(B(U,V)\) is the polarization of the invariant quadratic form
\(H\). Therefore

\[
\frac{\delta S}{\delta C_\mu^a}
=c\sqrt{-g}\,g^{\mu\nu}B(T_aX,D_\nu X)=0,
\qquad
P^\mu_{C_a}=\frac{\partial\mathcal L}
{\partial(\partial_t C_\mu^a)}=0.
\]

These are **algebraic connection equations** and vanishing primary
connection momenta. No Yang--Mills hyperbolic wave equation for
\(C_\mu^a\) follows from this bare classical action. The same absence
of \(\partial C\) persists for a metric built *algebraically*
from \(D_\mu X\), provided no curvature/differentiated metric terms
are added. Such a composite metric does change the algebraic current
by the chain rule; the displayed fixed-metric current is **not**
its full equation of motion.

This is a restricted **tree-level structural no-go** for this
minimal family, not for quantum induced gauge kinetics, an explicitly
curvature-dependent single action, or a connection that is a derivative
composite of another dynamical field. Deriving a finite, positive
Yang--Mills coefficient by a constrained one-loop effective action
would constitute an additional physical result and cannot be presumed.

In particular, allowing independent \(C_0^a\) variations can impose
constraints on \(X\) that were absent in the prescribed-connection
Legendre transform of Proposition 1. The full Dirac analysis must
include these algebraic constraints and their Poisson closure *before*
interpreting any fixed-connection negative normal modes as
physical instabilities of UBT.

The independent full-eight-real-component symbolic verification and
long-wavelength dispersion relation for Proposition 5 are recorded in
[theta_kinetic_spectrum.en.md](theta_kinetic_spectrum.en.md).
**Proposition 2 remains a conditional scalar truncation**, not a
demonstration that the remaining modes of the full UBT action are stable.

## Proposition 7 — eliminating auxiliary phase/boost connections does not cure the normal instability

This is a **stronger, still conditional** statement than merely quotienting
the symmetry orbit. Consider the same fixed-background minimal family,
but now allow an **independent auxiliary** local
\(U(1)\times SL(2,\mathbb C)\) connection inside \(D_\mu X\), with
**no connection-curvature kinetic term**. Linearize at \(X_0=irI\)
with vanishing background connection. The phase generator sends
\(X_0\mapsto-rI\), the three boost generators send
\(X_0\mapsto ir\sigma_j\), and the three rotation generators annihilate
\(X_0\). The last three connection components do not enter the
quadratic fluctuation action.

For each spacetime index \(\mu\), the tangent covariant derivatives are

\[
D_\mu u_0=\partial_\mu u_0-rA_\mu^\phi,\qquad
D_\mu v_j=\partial_\mu v_j+rA_\mu^{b_j}.
\]

The normal derivatives are \(\partial_\mu v_0\) and
\(\partial_\mu u_j\) at quadratic order. The time-derivative part of
the quadratic kinetic Lagrangian is therefore exactly

\[
\mathcal L_{\mathrm{kin,time}}^{(2)}
=c\left[(\dot u_0-rA_0^\phi)^2
-\sum_j(\dot v_j+rA_0^{b_j})^2
+\dot v_0^2-\sum_j\dot u_j^2\right].
\]

The algebraic connection equations have the **unique** solution

\[
A_\mu^\phi=\frac{\partial_\mu u_0}{r},\qquad
A_\mu^{b_j}=-\frac{\partial_\mu v_j}{r}.
\]

Substitution cancels all tangent covariant derivatives, leaving

\[
\boxed{
\mathcal L_{\mathrm{red}}^{(2)}
=c\left[(\partial_t v_0)^2-\sum_j(\partial_t u_j)^2
-(\nabla v_0)^2+\sum_j|\nabla u_j|^2\right]
-4r^2\left[(4\lambda_1+\lambda_2)v_0^2+
\lambda_2\sum_j u_j^2\right].
}
\]

Thus the **actually eliminated** auxiliary phase/boost gauge sector
still leaves a \((1,3)\) normal kinetic signature and the opposite-sign
generalized squared masses of Proposition 5. For either nonzero
real \(c\), a long-wavelength normal mode grows exponentially.
This rules out repairing this **particular quadratic auxiliary-gauge
realization** by merely treating the phase/boost tangent directions
as gauge.

The conclusion assumes a prescribed flat metric, a pointwise-minimum
background, zero background connection, independent nonpropagating
connections entering only through \(D_\mu X\), and no other constraints.
The background has a **degenerate composite tetrad**, and the full
single-Theta composite metric, torsion, relative connections, higher
derivatives and their Dirac algebra are not included. Therefore this
is **not** a no-go for all possible UBT completions.

Exact symbolic verifier:
tools/verify_theta_auxiliary_connection_reduction.py;
regression tests: tests/test_theta_auxiliary_connection_reduction.py.

## Remaining theorem-critical work

1. Finalize the single Theta action's pairing, measure, potential, composite metric and connection variations.
2. Compute the full Dirac constraints and remove any ghost directions without breaking Lorentz covariance.
3. Derive the selected vacuum, scalar channel and effective Einstein coefficient from that same action.
4. Only then promote the conditional dodecahedral CMB calculation to a parameter-controlled physical prediction.

**Claim boundary:** this note proves a conditional Hamiltonian and reduction identity. It does not prove fundamental UBT dynamics, GR recovery without effective-action assumptions, alpha, or a Planck fit.
