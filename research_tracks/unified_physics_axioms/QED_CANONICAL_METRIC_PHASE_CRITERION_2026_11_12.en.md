# Canonical central metric phase test: necessary and sufficient condition

**Status:** exact identity for the canonical central anticommutator metric; identification of the actual sharp action on the central complex unit is still required.

## Canonical source

`canonical/geometry/biquaternion_metric.tex` defines, on the classical Lorentz slice W_L,

g_{mu nu} I = (E_mu^sharp E_nu + E_nu^sharp E_mu)/2,

with no trace, real-part or Hermitian-projection substitution. `canonical/geometry/connection.tex` gives E_mu=N0^(-1/2) D_mu Theta.

For a central phase u=exp(i q alpha) and a phase-covariant derivative E'_mu=u E_mu, assuming sharp is an involutive anti-automorphism and maps central elements to central elements,

g'_{mu nu} I = u^sharp u g_{mu nu} I.

Thus a nondegenerate metric is invariant **if and only if** u^sharp u=1. This is a necessary-and-sufficient local algebraic criterion, not merely a sufficient one.

If sharp(i)=-i, then u^sharp=u^{-1}, and the phase is metric preserving.

If sharp(i)=+i, then u^sharp=u, and g'=u^2 g; a continuous nontrivial U(1) phase is NOT a symmetry of the canonical metric. The surviving phase values obey u^2=1 (discrete signs), on a nondegenerate patch.

The canonical Lorentz-slice restriction is a separate condition. Even if u^sharp u=1, one must show that u E_mu remains in the permitted W_L or is identified as the same physical tetrad by an explicitly declared quotient. Metric invariance alone does not imply preservation of the chosen real tetrad representative.

## Gauge connection and spinor tests

A relative central one-form c_mu=a_mu-b_mu can yield D_mu Theta=(Dhat_mu+i c_mu)Theta and c'_mu=c_mu-q partial_mu alpha, which ensures E'=u E. But the reduced canonical connection B=-Omega^ddagger may constrain c_mu, and the actual action of ddagger on iI must be checked. The common central one-form cancels exactly.

A valid electromagnetic interpretation additionally requires a positive Maxwell kinetic term, U(1) gauge invariance of the entire action and measure, a charged Grassmann module, and quantum Ward identities. No physical photon, fine structure constant, or one-loop QED matching has yet been derived.

## Decisive remaining source check

Locate the defining axiom of the actual canonical sharp (rather than guessing it from the notation). Evaluate (iI)^sharp and check the phase action on W_L and the physical connection reduction. Until this is done, both branches remain conditional. Do not replace the canonical anticommutator metric by a trace or Hermitian norm to manufacture phase invariance.
