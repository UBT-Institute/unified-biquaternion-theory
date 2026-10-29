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

# Information-first derivation program for UBT action and Hamiltonian

**2026-10-26. Exploratory research track. No derived fundamental action or physical Hamiltonian claimed. Priority P0.**

## A disciplined separation of three objects

1. **Microscopic dynamics**: the single biquaternion Theta with tau=t+i psi, its actual configuration space, quantum algebra, state and physical inner product (not yet selected).
2. **Observer information**: a region/causal-algebra A_O, reduced density operator rho_O, reference sigma_O, relative entropy D(rho_O||sigma_O)>=0, and modular Hamiltonian K_sigma=-log sigma_O. Observer dependence of accessible entropy need not imply observer-dependent underlying EOM.
3. **Geometric/holographic response**: composite g[Theta], causal wedges and boundary area entropy S_geom=Area/(4G hbar) only where a derivation or explicit benchmark assumption warrants it.

## First-law identity (exact, fixed reference)

For sigma full rank and rho(epsilon)=sigma+epsilon delta rho+..., Tr delta rho=0:

delta S(rho)|sigma = Tr(delta rho K_sigma) = delta <K_sigma>.

For exact relative entropy,
D(rho||sigma)=delta<K_sigma>-[S(rho)-S(sigma)] >=0.
It has zero first derivative at rho=sigma, so *linearizing D alone supplies no independent linearized Einstein equation*. This is a critical falsification gate: a proposal S_UBT = integral D with no extra structure has stationary first variation at the reference vacuum and does not specify Lorentzian symplectic time evolution.

## Information metric is not yet a kinetic action

The positive quadratic relative-entropy expansion defines a distinguishability susceptibility (a quantum Fisher/Bogoliubov–Kubo–Mori-type metric depending on choice of information geometry). A positive information metric cannot simply replace the indefinite Lorentz/phase invariant Theta kinetic pairing found in canonical/ACTION.en.md; invariance, locality, unitarity and composite constraints must be established. Euclidean positive-definite information distance versus Lorentzian kinetic signature must be handled explicitly.

## Constrained route to geometry

Test the Jacobson-type local horizon balance as an *effective* condition on each admissible causal wedge:
delta S_geom + delta S_matter =0 at fixed generalized volume, together with an independently defined horizon modular-energy/heat flux. Its Einstein-equation reduction is a benchmark conditional on the entropy-area coefficient, vacuum assumptions, local Lorentz symmetry and field content, not automatically the UBT microscopic action or unique coupling.

For non-equilibrium horizons use entropy production rather than forcing reversible Clausius equality. For a boundary-first holographic proposal, provide a genuine algebra-to-bulk reconstruction map and entropy renormalization; do not merely call Theta holographic.

## Provisional, falsifiable research workflow

A. Specify an actual finite-dimensional local/regulated state map Theta -> rho_O (or explain no such map exists); verify positivity, trace, gauge invariance and covariance across observer descriptions.
B. Compute first and second variations of D, modular energy and observer entropy; check data processing under coarse graining.
C. Define which information functional is varied and which constraints hold. Distinguish maximum-entropy inference from time evolution and from an action principle. Demonstrate existence of a real Lorentzian phase term/symplectic potential, not just a dissipative entropy gradient.
D. Match the geometry response to the exact composite tetrad and identify the dependence on torsion, psi and the surviving SO(2) curvature.
E. Derive one well-defined Theta-only local or controlled nonlocal action (including measure and boundaries), then run EL and full Dirac/Hamiltonian reduction. The registry remains DEFINED_FAMILY_NOT_FINALIZED until accomplished.
F. Compare observables: Einstein/Clausius limit, graviton poles, ghosts, horizon entropy and at least one novel prediction.

## Concrete first failure mode

For any fixed sigma, the nonnegative D(rho||sigma) is a minimization functional, not necessarily an action generating unitary dynamics. A naive variational law delta D=0 can select rho=sigma in a permitted full space of states but produces no Hamiltonian time flow. **Adding an ad hoc canonical term by hand would merely move the unsolved action-selection problem.**

References:
- T. Jacobson, 'Thermodynamics of Spacetime', PRL 75 (1995) 1260, DOI 10.1103/PhysRevLett.75.1260.
- T. Jacobson, 'Entanglement Equilibrium and the Einstein Equation', PRL 116 (2016) 201101, DOI 10.1103/PhysRevLett.116.201101.
- C. Eling, R. Guedens, T. Jacobson, 'Nonequilibrium Thermodynamics of Spacetime', PRL 96 (2006) 121301, DOI 10.1103/PhysRevLett.96.121301.
