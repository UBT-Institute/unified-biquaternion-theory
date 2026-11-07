<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Hypothesis and test plan; no derivation of gravity claimed.
UBT-AI-PROVENANCE-END -->

# Information-driven attractors and emergent gravity — research proposal
Status: SPECULATIVE / OPEN, not canonical. Date: 2026-11-07.

## Scope and guardrails
Recent numerical research on riddled/fractal attraction basins in neural-network training motivates testing sensitivity to initial conditions. It does **not** demonstrate that gravity is an attractor, nor that Jacobi theta kernels induce fractal basins. Avoid importing a learning algorithm's optimization time as physical time.

Maintain the established canonical UBT kinematics: Theta in C tensor H, covariant tetrad E_mu=N0^(-1/2)D_mu Theta, and the central anticommutator metric identity. No new metric projection, fiber averaging, arbitrary scalar-Theta truncation or unapproved change to the two-sided derivative is introduced here.

## Hypothesis (H1)
A separately specified gauge-compatible information functional I[Theta,T] and explicitly stated dynamics may admit stable geometric configurations whose effective metric responds to the stress-energy tensor T_munu. This must be independently derived, not fitted by inserting Einstein-Hilbert/Newtonian gravity as an input. Mass density rho is only a valid source in the nonrelativistic limit; covariantly the source is T_munu.

## Formal questions
Introduce an auxiliary relaxation parameter s, explicitly not physical time:
d Theta/ds = - grad_G I[Theta,T].
The configuration-space metric G, transformation law of Theta, boundary conditions, gauge degeneracy and functional derivative must all be defined before claiming existence of this flow. Gauge-equivalent fixed points must be identified rather than counted as distinct attractors.
At a stationary point delta I/d Theta = 0, evaluate the already defined UBT metric from E_mu. Ask whether a vacuum branch gives a Lorentzian nondegenerate Minkowski metric and sourced solutions produce the weak-field limit:
g_00 = -(1+2 Phi/c^2)+O(c^-4);  Delta Phi = 4 pi G_N rho.
Neither equation is currently derived in this proposal. G_N and c must not be hidden in a chosen fitting term.

## Information principle
Candidate Fisher/relative-information terms require a positive probability measure, well-defined normalization, coordinate/gauge invariance, units, an explicit coupling to T_munu, and a variational calculation. A Fisher information of rho alone contributes nothing to variation with respect to Theta when rho is held fixed. Do not conflate local information geometry with global attraction basins.

## Fractal basin diagnostic (independent of gravity)
For a specified dynamical flow and physical, gauge-invariant observable labeling its end state A, test P[A(Theta_0)!=A(Theta_0+delta Theta)] ~ ||delta Theta||^alpha over a documented finite scaling interval. A near-zero measured alpha is not proof of a mathematically riddled basin. Measure resolution dependence, finite precision, seeds and independent numerical baselines. Lyapunov exponents and basin uncertainty are different observables.

## Falsification gates
1. Supply explicit well-posed evolution and functional, including stress-energy coupling and units.
2. Demonstrate nondegenerate real Lorentzian metric and gauge-invariant observable attraction basins.
3. Recover sourced 1/r potential and inverse-square acceleration without baking the target equations into I.
4. Check energy-momentum conservation, equivalence-principle and relativistic weak-field constraints.
5. Compare against trivial gradient-flow and standard-GR baselines; report negative results.
No step is currently closed. This proposal is not a claim that UBT dynamics, GR, dark matter or gravity has been derived.

## Implementation
Numerical sandbox in UBT-Institute/ubt-theta-lab project fractal_basins_information; keep kernel baselines separate from physical Theta dynamics.

## External motivation
Ly and Gong, *Fractal basin geometry and the limits to predictability and reproducibility in deep learning*, Nature Machine Intelligence (2026), https://www.nature.com/articles/s42256-026-01336-3 . Inspiration only, not physical evidence.
