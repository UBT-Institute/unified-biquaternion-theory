# Conditional Dirac current on the composite UBT tetrad

**C-tier conditional theorem (2026-10-25). Not a derivation of a fundamental action or Hamiltonian.**

Assume the locked tetrad is a real, invertible Lorentz slice of E_mu=N0^(-1/2) D_mu Theta, inducing g_mu nu and an inverse e_a^mu. Assume a *specified compatible spin connection* on the associated Dirac carrier with ∇_mu gamma^nu=0 and Dirac equations
\[
(i\gamma^\mu\nabla_\mu-m)\Psi=0,\qquad
i(\nabla_\mu\bar\Psi)\gamma^\mu+m\bar\Psi=0
\]
in natural units, where Psi is a **derived chosen carrier** from Theta (for example F in #724). Then the ordinary bilinear
\[
j^\mu=\bar\Psi\gamma^\mu\Psi,\qquad
\nabla_\mu j^\mu=0
\]
follows by product differentiation and cancellation of opposite mass terms. This proof does not need Einstein equations, but it **does require** the two Dirac equations and compatible connection; it does not generate them from UBT.

For any Cauchy hypersurface Sigma, the sesquilinear conserved pairing
\[
\langle\Psi_1,\Psi_2\rangle_\Sigma
=\int_\Sigma d\Sigma_\mu\,\bar\Psi_1\gamma^\mu\Psi_2
\]
is independent of homologous slices when flux through the boundary vanishes. Positivity is the usual positive future-directed normal result, conditional on the spinor bundle, orientation, and regular globally hyperbolic Lorentz sector. Its imaginary part is a candidate **solution-space** symplectic form, not necessarily the phase-space Omega_B from #717 and not a covariant presymplectic current of the unknown Theta-only action.

**Composite-geometry subtlety:** if E=E(Theta,DTheta), then gamma^mu and the volume form vary with Theta. Merely substituting Psi=F(Theta) into the standard Dirac current does not make the full *nonlinear* UBT presymplectic current; tangent variations also induce δE, δomega, δgamma and potential constraints. The conserved Dirac current is a bilinear in *solutions of the specified linear Dirac equation on a common background*. For two different self-consistent composite solutions with different metrics, current conservation cannot be invoked by mixing them. Even on one composite solution, using the Dirac equation is a new conditional dynamical assumption unless it follows from the single Theta equation.

**Torsion gate:** UBT may admit metric-compatible torsion. The exact divergence relevant to the integration measure requires the connection's torsion-trace/volume integration identity, or a torsion-free Levi-Civita companion plus correctly derived spin coupling. Do not freely replace a torsionful covariant divergence by ∂_mu(sqrt(-g)j^mu) without accounting for the torsion trace.

**Hamiltonian-first criterion:** derive (a) the emergent chiral Dirac carrier and its complex structure from the locked representation, (b) an evolution law on Theta whose induced equation is Dirac, (c) a conserved covariant presymplectic current of the full Theta system, and (d) constraint reduction and a bounded physical generator. Only then may the positive hypersurface pairing select a Hamiltonian and support reconstruction of the unique action.

The accompanying algebra test checks gamma-matrix pseudo-Hermiticity and positive density, not nonlinear composite conservation.
