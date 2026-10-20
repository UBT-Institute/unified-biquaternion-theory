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

## Remaining theorem-critical work

1. Finalize the single Theta action's pairing, measure, potential, composite metric and connection variations.
2. Compute the full Dirac constraints and remove any ghost directions without breaking Lorentz covariance.
3. Derive the selected vacuum, scalar channel and effective Einstein coefficient from that same action.
4. Only then promote the conditional dodecahedral CMB calculation to a parameter-controlled physical prediction.

**Claim boundary:** this note proves a conditional Hamiltonian and reduction identity. It does not prove fundamental UBT dynamics, GR recovery without effective-action assumptions, alpha, or a Planck fit.
