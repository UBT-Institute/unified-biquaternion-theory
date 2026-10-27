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

# Does the canonical Theta action actually produce the torus Laplacian?

**2026-10-26. Exact conditional selection obstruction; not a new fundamental action.** Compare `canonical/ACTION.en.md`, `canonical/bridges/theta_parameter_separation.md`, `INDUCED_METRIC_KINETIC_COLLAPSE.md`, `TORUS_HAMILTONIAN_FULL_REVIVAL_GATE.md`.

## Minimal derivation under explicit additional assumptions

For a scalar coefficient u(x,psi) on S¹_R, the *separately assumed* compact kinetic term
 S_psi=-(c_psi/2)∫d⁴x dpsi sqrt(|g|) |partial_psi u|²
produces c_psi(-partial_psi²) in its Euler–Lagrange differential operator (up to the complete Lorentzian kinetic normalization and sign conventions). Its Fourier modes u_n exp(in psi/R) have eigenvalues c_psi n²/R². On a flat d-torus G with constant components, replace -partial_psi² by -Delta_G. This is a direct integration-by-parts fact, not a derivation of the compact term from canonical UBT.

**Missing premise:** the currently declared family `S_Theta = (1/2)∫d⁴x sqrt(-g)<D_mu Theta,D^mu Theta>-κV[Theta]` is a FOUR-DIMENSIONAL family; it does not itself specify a dpsi integration, a positive compact metric G_ab, or a (D_psi Theta)†(D_psi Theta) coefficient. Merely knowing complex time tau_UBT=t+i psi and the modular theta heat-kernel identity cannot supply that omitted differential operator. A higher-dimensional action candidate is inventoried in `canonical/ACTION.en.md` but has NOT been derived as the single finalized fundamental Theta action.

## Composite gravity gauge test

On the non-null Lorentz-real split-jet patch, E_mu=(D_mu X+Q_mu)/sqrt(N0), finite carrier replacement X' = X+epsilon and Q'_mu=Q_mu-D_mu epsilon leave (E_mu,omega) identical. If X and auxiliary fields depend on psi, the same equality holds **pointwise at every psi**, including epsilon(x,psi)=f(x) exp(in psi/R) when the allowed real/complex component domains are respected. Consequently any Fourier mode of the carrier X is invisible to the *pure* MM functional if it only enters through E and omega. Its psi-variation therefore cannot acquire a nonzero physical stiffness from that functional alone.

If Q_mu is restricted to be psi-independent or complex Theta carries a distinct psi-dependent, non-shifting physical sector, this particular fibre argument needs re-analysis; such restrictions cannot be silently inserted. Nor has a complex split-jet shift been proved for all four imaginary Theta components.

## Gate conclusion

The torus kinetic operator has been **mathematically derived from an explicitly assumed compact derivative term**, but not derived from the existing canonical four-dimensional Theta family or MM gravitational action. Its coefficient alpha and metric G remain genuinely free. Under the local split-jet carrier redundancy the Lorentz-real carrier modes cannot be promoted to physical torus excitations without altering the action/gauge structure. Therefore H_tor remains a valid conditional spectral sector, NOT an established physical summand of H_UBT.

The shortest noncircular next calculation: identify an existing canonical invariant with D_psi Theta, derive its pullback and kinetic Hessian on the full complex Theta/tetrad configuration, and test whether the resulting operator survives the Dirac quotient. Only then insert eigenvalues into observer correlation functions.

Regression: tests/test_torus_theta_action_bridge_gate.py.
