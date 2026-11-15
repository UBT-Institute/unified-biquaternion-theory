# Local phase versus canonical sharp metric: conditional theorem and obstruction

**Status: exact algebraic fork; the actual canonical sharp involution and reality slice must be checked before declaring U(1) a symmetry.**

Let E_mu=N0^(-1/2) D_mu Theta, N0 constant and phase-invariant. Suppose a relative central connection transforms so that E'_mu=u E_mu with u(x)=exp(i q alpha(x)). Let a candidate metric be the symmetric central projection

g_mu_nu = (1/2) Sc(E_mu^sharp E_nu + E_nu^sharp E_mu),

with the *actual* canonical sharp and scalar projection, not an arbitrarily substituted Hermitian conjugation.

### Fork A: antilinear sharp on the central complex phase

If (u E)^sharp=u^* E^sharp, then for |u|=1:

g'_mu_nu=(1/2)Sc(u^*u E_mu^sharp E_nu+u^*u E_nu^sharp E_mu)=g_mu_nu.

This is an algebraic sufficient condition for metric invariance, assuming the metric really has the displayed form and Sc commutes with central scalars.

### Fork B: complex-linear sharp on the central complex phase

If (u E)^sharp=u E^sharp, then g'_mu_nu=u^2 g_mu_nu. A real-valued metric is generally not preserved by a continuously variable phase. Only u^2=1 gives exact invariance on a nondegenerate metric. Taking a real part afterwards does not restore invariance for generic complex tetrads: Re(u^2 z) differs from Re(z).

### Independent obstruction: Lorentz-real slice

Even if Fork A holds for the full complex metric, multiplying a Lorentz-real tetrad by a non-real phase generally leaves the real tetrad slice. Therefore the already established Lorentz-real split-jet chart is not automatically preserved. One must either construct a U(1)-invariant physical real projection or show the phase acts vertically on the true physical quotient.

### Central connection constraint

Canonical `canonical/geometry/connection.tex` uses B=-Omega^ddagger with A=Omega modulo common center cancellation. One cannot simply postulate an arbitrary independent relative U(1) vector field in this reduced representative. Its survival must be demonstrated using the actual ddagger action on central iI, the admissible connection bundle, and reality constraints. If the relative central connection is constrained away, the carrier-phase candidate does not furnish an independent photon.

### Quantization consequence

Metric invariance is necessary but not sufficient for a physical U(1) gauge symmetry. A full action and measure invariant under the phase, a Maxwell kinetic term with correct sign, a Gauss constraint, a charged fermion module, and a Ward identity remain independent gates. No alpha prediction follows from either fork.

**Next repo task:** inspect the defining source of the canonical sharp and central-sharp metric, record its action on iI, and test the real slice and reduced two-sided connection. Do not silently equate sharp with Hermitian adjoint.
