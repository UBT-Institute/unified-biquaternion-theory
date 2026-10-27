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

# Explicit ADM Hamiltonian of the existing split-jet MacDowell–Mansouri gravity sector

**2026-10-26. Standard conditional bulk gravity reduction, NOT the full UBT Hamiltonian.** This is the requested concrete canonical bridge from the *already specified* MM curvature-square action, not a new independent fundamental action. Source: `research_tracks/action_selection/single_theta_macdowell_mansouri_candidate.en.md`.

On the non-null X²!=0, invertible E patch, the established local stationary solution set of the composite MM candidate agrees with vacuum Hilbert–Palatini/Einstein–Lambda. With kappa=g_G² ell²/2=8πG and Lambda=3 epsilon_psi/ell², its metric bulk action after eliminating torsion is S=(1/(2 kappa))∫sqrt(-g)(R-2Lambda)d⁴x plus Euler/boundary terms. Assuming global hyperbolicity, an ADM foliation and the **usual Einstein–Hilbert boundary prescription**, its canonical bulk Hamiltonian is
 H_ADM[N,N^i]=∫d³x (N C + N^i C_i),
 C=(2kappa/sqrt h)(pi_ij pi^ij-pi²/2)-(sqrt h/(2kappa)) (³R-2Lambda),
 C_i=-2 D_j pi^j_i,
 pi^ij=(sqrt h/(2kappa))(K^ij-h^ij K).
Add boundary charges H_boundary depending on asymptotics/edge conventions. The canonical lapse and shift momenta vanish as primary constraints, while their preservation yields C≈0 and C_i≈0. The bulk constraint algebra is the usual hypersurface deformation algebra: {C[N],C[M]}=C_i[h^ij(N partial_j M-M partial_j N)], {C_i[v],C[N]}=C[L_v N], {C_i[v],C_j[w]}=C_i[[v,w]], with boundary qualifications.

**Very important:** this is the ADM Hamiltonian of the on-shell-equivalent Einstein sector after *choosing the torsionless/metric reduction*, not an independently demonstrated canonical equivalence between full original first-order composite MM phase space and ADM. A full proof would need the symplectic pullback, resolution of torsion/connection second-class constraints, split-jet vertical first-class generators, Lorentz Gauss constraints and their boundaries. The Euler term can affect boundary charges/symplectic potential but not Einstein bulk EOM. The full eight-real Theta and compact psi dynamics remain missing; no dynamical SU(3) gluons are implied. Also C is indefinite off constraint surface; this by itself is not a ghost test.

**Mini-superspace cross-check** for spatially flat FLRW h_ij=a(t)²δ_ij (unit comoving spatial volume), N=N(t), shift zero and no matter:
 L=-3a dot a²/(kappa N) - Lambda N a³/kappa
 up to a boundary term,
 p_a=-6 a dot a/(kappa N),
 H=N[-kappa p_a²/(12a)+Lambda a³/kappa].
The constraint H/N=0 gives (dot a/(aN))²=Lambda/3. This exact relation matches vacuum Friedmann in flat slicing for Lambda>0. For Lambda<0 no real flat vacuum FLRW solution with a>0, consistent with the same constraint. Thus the algebraic ADM normalization is checked against the existing MM kappa/Lambda identifications.

**Selection conclusion:** We now have a concrete gravity Hamiltonian H_grav, conditional on the established MM branch, but it does not determine the missing physical Theta complex/colour and toroidal sectors. Appending a separately guessed H_tor or information functional would violate the one-action derivation rule unless a common action and Dirac map are constructed. A decisive next gate is an explicit reduced presymplectic equivalence with ADM plus a nontrivial shift-invariant complex-Theta observable and its dynamics.

Verification: `tests/test_information_mm_adm_hamiltonian_bridge.py`.
