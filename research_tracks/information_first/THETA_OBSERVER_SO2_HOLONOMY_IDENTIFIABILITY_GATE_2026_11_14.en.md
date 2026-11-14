<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Restricted algebraic/kinematic result, not a photon, QED, or unified action.
UBT-AI-PROVENANCE-END
-->

# Theta observers cannot identify the residual SO(2) curvature from local first jets

**2026-11-14. Status: exact conditional theorem and counterexample; microscopic UBT dynamics OPEN.**

## Reused prior results (not new proofs)

The previously derived two-carrier SO(2) stabilizer nonselection and first-jet blindness are in:
- research_tracks/fundamental_dynamics/field_built_so2_connection_family.en.md
- research_tracks/fundamental_dynamics/residual_so2_curvature_decision_gate.md
- research_tracks/fundamental_dynamics/so2_transport_selector_compatibility.md

The existing observer tomography and central-phase obstruction are in:
- research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md
- research_tracks/action_selection/central_phase_metric_gate.en.md
- research_tracks/information_first/THETA_OBSERVER_QED_BERRY_VACUUM_LINEARIZATION_GATE_2026_11_14.en.md (this PR)

**New cross-sector test:** even the FULL Theta and ALL local quantum observer density matrices, together with the canonical nondegenerate tetrad and its first covariant jets, can agree while the residual transverse SO(2) connection has different gauge-invariant curvature. Hence quantum local state reconstruction cannot select a physical photon connection without a dynamical transport principle or additional physical holonomy observations.

## 1. Explicit ONE full-complex Theta

Use sigma_0=I_2 and sigma_j the Pauli matrices; eta=diag(-,+,+,+), N0=1. On a future-timelike patch write
\[
V^a=(t,x,y,z),\quad W^a=(0,1,0,0),\quad
\boxed{\Theta=iV^a\sigma_a+W^a\sigma_a}.
\]
V and W are the two real four-vector components of the ONE complex biquaternion, not separate fundamental fields. On the flat initial Lorentz connection omega_0=0,
\[
D_\mu V^a=\delta_\mu{}^a,\quad D_\mu W^a=0,\quad
E_\mu=D_\mu\Theta=i\sigma_\mu\in W_L=i\mathrm{Herm}_2,
\]
\[
\boxed{\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=\eta_{\mu\nu}I_2}.
\]
The full Theta is invertible around p=(r,0,0,0), r>0, since det Theta(p)=-(r²+1) !=0.

## 2. A nonflat SO(2) connection invisible to the full Theta first jet

Fix the positive scalar r of the reference point p and let eps_0123=+1. Define
\[
J^a{}_b=\frac1r\,\eta^{ac}\epsilon_{cbde}V^dW^e.
\]
Direct antisymmetry gives
\[
\boxed{J^T\eta+\eta J=0,\quad JV=JW=0}.
\]
At p, J^2{}_3=+1, J^3{}_2=-1, so J is a transverse rotation of the y-z plane and tr(J(p)^2)=-2.

Compare
\[
\boxed{\omega_0=0,\qquad\omega_1=y\,J\,dz}.
\]
Since J annihilates BOTH carriers at every local point,
\[
D^{(1)}_\mu\Theta=D^{(0)}_\mu\Theta=i\sigma_\mu,\qquad
g_1=g_0=\eta,\qquad\Theta_1=\Theta_0=\Theta.
\]
Nevertheless,
\[
\mathcal R[\omega_0]=0,\qquad
\mathcal R[\omega_1]_{yz}(p)=J(p)\ne0.
\]
Indeed \(\mathcal R_1=d(yJdz)+(yJdz)\wedge(yJdz)\) and y(p)=0, hence only dy wedge dz times J remains. The connections are NOT gauge-equivalent, since a flat curvature cannot be conjugated to a nonzero one. Omega_1 has different torsion away from y=0, so uniqueness of the torsion-free Levi-Civita connection is not violated. The infinitesimal loop holonomy at p differs at first order in the enclosed area. These are two compatible *kinematic* configurations, not two claimed solutions to one microscopic action.

## 3. Local multi-clock observer records cannot determine this connection

Use the PREVIOUSLY defined conditional observer channel with any calibrated positive clock N determined by the same tetrad and observer direction:
\[
T_N=N^{-1/2}\Theta N^{-1/2},\qquad
\rho_N=T_NT_N^\dagger/\mathrm{tr}(T_NT_N^\dagger).
\]
Theta and g are identical in both constructions. Thus ALL pointwise rho_N, even complete calibrated three-clock tomographic records, and their ordinary coordinate derivatives coincide. Complete knowledge of Theta and E still does not fix the SO(2) connection in this restricted branch.

This does NOT preclude a physical observer sensitive to spin transport or an interferometric Wilson loop from detecting the *curvature* difference. Such probes depend on inter-point dynamics, which must be selected by the full quantum UBT. It also does not prove that this SO(2) is the electromagnetic U(1): SO(2) frame rotations can be solely gravitational/torsional unless an independent physical charge and constraint structure is demonstrated.

## 4. First-jet information and kinetic nonselection

For a local functional only of Theta, DTheta, the locked metric g[Theta,DTheta], and a finite set of local density readouts rho_N[Theta], the shift omega->omega+alpha J changes NONE of these arguments. Therefore
\[
\boxed{\delta_\alpha L(\Theta,D\Theta,g,\rho_N)=0.}
\]
No such first-jet/local-readout action fixes alpha or gives an independent kinetic term to this residual connection. An action using torsion, curvature, higher covariant jets or physically transported quantum correlations may remove the degeneracy; selecting such a term and its coefficient remains the dynamical task. Information/entropy alone cannot be used to conceal this missing selection.

## 5. A separate no-go for the central determinant phase

For invertible Theta and a traceless Lorentz spin matrix Omega in sl_2(C), consider the most direct central phase connection
\[
a_{\det}=\tfrac12\,\operatorname{Im}\operatorname{tr}\{
\Theta^{-1}(d\Theta+\Omega\Theta+\Theta\Omega^\dagger)\}.
\]
Trace cyclicity gives tr(Omega)=tr(Omega^dagger)=0, so
\[
\boxed{
a_{\det}=\tfrac12\,\mathrm{Im}\,d\ln\det\Theta
=\tfrac12\,d\arg\det\Theta,\qquad da_{\det}=0
}
\]
on every smooth invertible simply connected patch. Adding a real Weyl one-form wTheta shifts only the REAL trace and does not alter this result. Formal Theta->exp(i chi)Theta changes a_det by dchi, but leaves its field strength zero. Global winding/singularities are separate and do not provide ordinary smooth photon radiation.

The already established central_phase_metric_gate.en.md shows that if E transforms as exp(i chi)E then its sharp metric transforms as exp(2i chi)g and W_L is lost generically. Thus local observer phase blindness must NOT be promoted to an exact physical central U(1) gauge symmetry without a derived compensating geometric action.

## 6. Physical interpretation, priority

The residual transverse SO(2) curvature can be nonzero and linear under a connection perturbation, unlike the naive relative Berry curvature that starts at second order about a projectively trivial reference. This makes it a WORTHWHILE **candidate transport sector**, not a derived massless photon.

Decisive next tests:
1. Derive from one microscopic Theta action a unique physical composite connection or its constrained dynamical residual SO(2) quotient, including torsion and observer reference transport.
2. Determine if there is a *genuine internal* U(1) gauge generator distinct from local Lorentz frame transformations; calculate Gauss/first-class constraints and a massless positive spin-1 mode with two helicities. A separately inserted Maxwell curvature-square action is ONLY a comparator.
3. Derive charged matter and the Ward identities; verify common causal cone with the locked sharp metric and quantum-to-classical Maxwell limit on the emergent GR background.
4. Only then test Standard Model embedding and the quantitative information principle as a selector.

## Verification

Seven focused exact SymPy tests were run locally and passed, including J in so(1,3), JV=JW=0, identical full sharp metric and tetrad for both connections, the nonzero local curvature mismatch, observer readout nonidentifiability, determinant-phase flatness and first-jet action blindness. Regression: tests/test_theta_observer_so2_identifiability_gate.py. All conclusions are restricted to this comparator; no global UBT connection, photon, or field equations were proved.
