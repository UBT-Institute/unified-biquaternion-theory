# Conditional stability theorem and spacetime-rank obstruction for radial UBT branch

## Grounding in canonical action selection

The existing Hamiltonian bridge, research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md, Propositions 7–9, already distinguishes a reduced positive Lorentz-real radial scalar from a physically nondegenerate composite spacetime. This note states the precise simultaneous stability/rank gate rather than proposing a new UBT action. All results are CONDITIONAL on a dynamically consistent positive-Hermitian Lorentz-real slice, a prescribed fixed static Lorentz background, no extra connection-curvature term, the auxiliary-connection equations yielding vanishing boost terms, and the existing quartic potential parameter regime.

## Derived radial sector, energy and mode stability


\[
\Theta=i\rho I,\qquad A=4\lambda_1+\lambda_2>0,\quad c>0,\quad r>0.
\]
\[
U_{\rm rel}(\rho)=A(\rho^2-r^2)^2,\qquad
U''(r)=8Ar^2>0.
\]
\[
\mathcal H_{\rm rel}=
\frac{p_\rho^2}{4c}+c\,|\nabla\rho|^2+
A(\rho^2-r^2)^2\ge0.
\]
\[
\omega_k^2=k^2+\frac{4Ar^2}{c}>0,\quad k^2\ge0.
\]
\[
D_\mu\Theta=i(\partial_\mu\rho)I,\qquad
\mathrm{rank}\,E_\mu{}^a\le1,\qquad
\det g_{\rm composite}=0.
\]


The reduced scalar Lagrangian with gradient has the kinetic form c[(partial_t rho)^2-|grad rho|²]-U(rho). For its momentum p_rho=2c partial_t rho, the Legendre transform has the vacuum-subtracted Hamiltonian density displayed above. Its nonnegativity is global within the prescribed scalar sector when the spatial metric is Riemannian and the scalar potential coefficients obey the stated signs. Vanishing momentum, spatial gradient and rho=r produce a minimum; the linearized radial oscillator has strictly positive squared frequency for every nonnegative spatial Laplace eigenvalue. Time-translation symmetry of the prescribed static setup yields the usual conservation law under boundary conditions preventing energy flux, but full PDE energy conservation is not claimed as Lean-formalized here.

## Why this is NOT a proof of full UBT stability

The same eliminated-connection equation removes boost parts of D_mu Theta. All tetrad columns then lie along the single internal direction iI, so every 2-by-2 tetrad minor vanishes and the emergent metric has rank at most one. A nondegenerate Lorentzian spacetime requires rank four. The radial branch therefore cannot simultaneously furnish a healthy scalar AND the nondegenerate composite spacetime in this minimal auxiliary-connection setup.

In the separate unconstrained or gauge-eliminated *normal* branch, the older kinetic block retains inertia (1,3); ghost directions remain. Restricting that normal sector by hand to a positive radial mode is not a legitimate proof of a full local Dirac reduction. The consistency of the Lorentz-real patch, all composite connection/metric variations and full first-/second-class constraint algebra remain OPEN. The already derived bare-action volume-collapse restriction presents a further independent obstruction.

## Proof and regression status

The new Lean file formal/RadialStabilityRankObstruction.lean proves nonnegative finite radial energy, positive radial squared frequency and vanishing minors of a scalar outer product. It does not formalize constrained Hamiltonian field theory, gauge orbits, PDE well-posedness, the full four-dimensional metric-rank theorem, or generalized ghost absence. Python/SymPy checks the exact scalar Legendre transform and fluctuation curvature; sample energies and exact rank-one composite-metric structure are regression gates, not physical experiments.

A proof of full theory stability now needs: one complete real UBT action, an admissible nondegenerate background, full Dirac-Bergmann constraint closure for Theta/metric/connections, reduced symplectic form and bounded-below physical Hamiltonian, causal hyperbolic perturbations and stable nonlinear evolution. No extra positive quadratic matrix may be inserted by fiat. Jacobi theta prime arithmetic remains separate until a physical mode spectrum is derived.

## Repo references

- research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md (Propositions 7–9)
- research_tracks/action_selection/theta_kinetic_spectrum.en.md
- research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md
- canonical/ACTION.en.md
