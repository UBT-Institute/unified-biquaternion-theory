# QED from a two-sided biquaternion connection: central cancellation and charged-module gate

**Status: exact algebraic central-sector result; physical QED emergence OPEN.**

Canonical starting point: `canonical/geometry/connection.tex` defines D_mu Theta = partial_mu Theta + A_mu Theta - Theta B_mu, and explicitly notes cancellation of a common central term in the no-new-field representative.

Write A_mu=Ahat_mu+i a_mu I, B_mu=Bhat_mu+i b_mu I, with real a,b. Since I is central,

D_mu Theta=partial_mu Theta+Ahat_mu Theta-Theta Bhat_mu+i(a_mu-b_mu)Theta.

Thus a common center a=b is exactly invisible to Theta. Only c_mu=a_mu-b_mu enters the carrier derivative. For the central parts of curvature,

F_A^center=i (da) I, F_B^center=i (db) I,

and the two-sided commutator gives i(dc)Theta. This is algebraically a U(1)-like relative curvature, not yet Maxwell dynamics.

## Local phase transformation and compatibility gate

Let Theta'=exp(i q alpha) Theta and c'_mu=c_mu-q partial_mu alpha, while the hatted connections are held fixed. Then D'_mu Theta'=exp(i q alpha)D_mu Theta, provided the displayed central term is i c_mu Theta. If instead c_mu is normalized as q A_em, A_em transforms as A_em -> A_em-partial alpha.

**Important:** the canonical sharp metric and Lorentz-real tetrad are not automatically invariant under this phase rotation. Therefore one cannot claim this transformation is a physical gauge symmetry of full UBT without explicitly verifying the transformation of E, its sharp conjugation, the normalization N0 and the complete action. The real-Lorentz split-jet chart may not be preserved by multiplying Theta by a complex phase.

## Charged spinor module alternative

If the common central term cancels on Theta, it may still act on a separately specified charged module psi with D_mu psi=(partial_mu+Omega_mu+i q A_em,mu)psi. This gives the usual U(1) covariant derivative but **does not derive** the charge representation or electromagnetic connection from Theta alone. Its physical meaning depends on how the matter module couples to the left/right algebra.

## Ward identity gate

For a genuinely gauge-invariant, anomaly-free quantum action and symmetry-preserving regularization, the 1PI electron vertex with the electric charge stripped satisfies

k_mu Gamma^mu(p+k,p)=S^{-1}(p+k)-S^{-1}(p).

The equality is a quantum consequence of gauge symmetry; it cannot be inferred solely from the algebraic central decomposition. An independent Maxwell kinetic term, positive photon norm, Gauss constraint, and explicit fermion representation are necessary. At one loop, a single charge-one Dirac fermion should give beta(e)=e^3/(12 pi^2)+O(e^5) above threshold, in the standard QED limit.

## Decisive next calculations

1. Check phase transformation of the actual canonical central-sharp metric and normalized E= N0^(-1/2) D Theta. Identify whether phase is a redundancy or changes geometry.
2. Determine whether a-b is independent after imposing B=-Omega^ddagger and the permitted physical connection constraints; do not reintroduce a forbidden doubled connection.
3. Supply or derive a gauge-invariant kinetic term for the surviving relative U(1) curvature and its normalization.
4. Construct a consistent charged spinor representation and compute its Ward identity and one-loop vacuum polarization.
5. Preserve the existing split-jet quotient and verify absence of new negative-norm states.

**Conclusion:** A relative central one-form is a precise algebraic candidate for U(1); a common central one-form is invisible to Theta. Neither observation alone establishes emergent QED or predicts alpha.
