# Composite Hodge star audit: constructibility versus dynamics

Date: 2026-10-12. Status: working research; AI-assisted. No canonical promotion.

## Premises

Let B=C tensor H have a chosen Lorentz-real vector slice W_L and an invariant nondegenerate quadratic pairing eta. Let Theta be W_L-valued in this test. Suppose E_mu=(D_mu Theta)/sqrt(N0) belongs to W_L and is an invertible coframe e_mu^a. Then

 g_mu_nu = eta_ab e_mu^a e_nu^b

is algebraically defined by the central anticommutator. Given orientation, g uniquely defines vol_g and Hodge star *_g on differential forms. In components:

 (*_g F)_{mu nu}=(1/2) sqrt(abs(det g)) epsilon_{mu nu rho sigma} g^{rho alpha}g^{sigma beta} F_{alpha beta}

for a 2-form F, with sign conventions tied to orientation/signature.

**Consequence:** a nondegenerate UBT coframe is sufficient to *construct* the Hodge star; there is no independent Hodge-star field. This relies on a coframe, signature and orientation already selected, so it is not a metric-free construction from the bare abstract algebra B.

## Theorem: flatness of the pure-gradient nondegenerate branch

Let the Lorentz connection vanish in a simply connected local patch and e^a=dX^a for four real functions X^a with det(∂_mu X^a) nonzero. Then

 g=eta_ab dX^a tensor dX^b = X^*(eta).

The inverse-function theorem makes X=(X^0,...,X^3) local coordinates. Hence the Levi–Civita Riemann tensor R[g]=0 **exactly**, not only to linear order. The induced Hodge operator satisfies naturality

 *_g X^*alpha = X^*(*_eta alpha)

for an orientation-preserving local diffeomorphism X and the corresponding form alpha (with orientation sign if reversed). Consequently the Hodge–Dirac operator d+delta_g is locally conjugate through X-pullback to the ordinary flat-space Hodge–Dirac operator. It generates no intrinsic curved Einstein geometry on this branch.

Proof: pullback metric and Hodge naturality; Riemann tensor natural under diffeomorphisms and R[eta]=0. The pullback commutes with exterior d; delta_g is constructed via the Hodge star.

Boundary conditions, global topology and noninvertible Jacobians may be nontrivial but do not change the local curvature theorem on nondegenerate patches.

## Composite-connection branch: constructive but not selected

When E^a=(DTheta)^a/sqrt(N0) with nontrivial paired Lorentz connection, curvature of g need not vanish. Existing UBT notes give local torsionful right inverses to arbitrary metrics. However the connection must be specified; a right inverse does not dynamically select one.

If one requires a connection depending on g[E] (e.g. Levi-Civita, or composite contortion), E=D_{Omega[g[E]]}Theta is a differential implicit relation. Before declaring the star *_g and the Dirac–Kähler operator fundamental, one must prove existence/uniqueness and account for variation of E, g, *, delta and Omega. In the torsion-free minimal Lorentz pair, existing concurrent-vector no-go restricts allowed curved solutions.

## Operator-selection obstruction

The constructed D_K=d+delta_g uses the metric formal adjoint, but the bare algebra B does not fix an action functional Tr f(D_K^2/Lambda^2) or a Hilbert-space domain, test function f, cutoff Lambda or measure. In Lorentz signature, delta as a formal adjoint is not a positive Hilbert adjoint.

Thus the following are distinct:
(A) construct g and * once a nondegenerate coframe is supplied — established algebraically;
(B) determine e, Omega, and g uniquely from Theta and fundamental axioms — open;
(C) derive a distinguished action and healthy propagating spin-2 modes — open.

## Priority consequences

1. Keep P0 metric/connection-selection and implicit-system integrability in front of spectral regularization.
2. Do not use pure-gradient Hodge construction as an explanation for curved GR; it is locally diffeomorphic to Minkowski.
3. Check composite connection branches for local existence, physically meaningful constraints and non-circular operator construction.
4. Prefer theorem/no-go outcomes to fitted action coefficients.
5. No change in claim status to 'fundamental Einstein derivation'.

References in repository:
- canonical/gr_closure/gap_10i_torsionful_local_representer.tex
- canonical/gr_closure/gap_10i_paired_connection_audit.tex
- research_tracks/operator_first_2026_10/dirac_kahler_closure_audit.md
