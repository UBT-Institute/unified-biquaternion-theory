<!-- BILINGUAL-UNIT: full-clifford-operator -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Full geometric algebra rather than a gradient-only model

<!-- BILINGUAL-UNIT: context -->
## Established repository context
Canonical `canonical/geometry/biquaternion_dirac_lift.tex` constructs a block Clifford lift of the **same** covariant tetrad. Existing `research_tracks/action_selection/clifford_axial_pseudoscalar.en.md`, `bivector_potential_invariants.en.md`, and `research_tracks/information_first/ORTHOGONAL_CLIFFORD_HAMILTONIAN_SELECTOR_GATE.md` already examine pseudoscalar, bivector, axial torsion and the Hamiltonian selector. The earlier fixed-connection scalar-gradient no-go must not be generalized to this richer canonical setting.

<!-- BILINGUAL-UNIT: algebra -->
## Grade decomposition and canonical operator
$$
Cl(1,3)=\bigoplus_{k=0}^4\Lambda^k\mathbb R^{1,3},
\quad \dim=(1,4,6,4,1),\quad
Cl^+(1,3)\cong\mathbb C\otimes\mathbb H.
$$

$$
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\quad
\Gamma_\mu=\mathcal C(E_\mu),\quad
\{\Gamma_\mu,\Gamma_\nu\}=2g_{\mu\nu}I_4.
$$

$$
\slashed{\mathscr D}=\Gamma^\mu\mathscr D_\mu,\qquad
\slashed{\mathscr D}^{\,2}
=g^{\mu\nu}\mathscr D_{(\mu}\mathscr D_{\nu)}
+\frac14[\Gamma^\mu,\Gamma^\nu][\mathscr D_\mu,\mathscr D_\nu]
+\text{terms from }\mathscr D\Gamma,
$$


The last displayed formula is **schematic** unless the chosen Clifford module connection is compatible, $\mathscr D_\mu\Gamma^\nu=0$, and index conventions are stated. Under Clifford compatibility the extra derivative-of-$\Gamma$ term vanishes in a suitable covariant formulation; torsion and representation-dependent curvature may modify the standard Lichnerowicz identity. The precise coefficients and adjoints require a separate audit. Odd Clifford grades are not additional fundamental fields.

<!-- BILINGUAL-UNIT: implication -->
## Dynamics and selection
The full geometric product for a vector is $\nabla A=\nabla\cdot A+\nabla\wedge A$: retaining the wedge term avoids the scalar-divergence-only truncation. Nevertheless, adding a Clifford lift alone changes no dynamical degrees of freedom. One must classify allowed local curvature/torsion invariants and verify which are independent, non-topological and compatible with the canonical single-$\Theta$ architecture. A squared Dirac-type operator may generate curvature couplings, but it does not determine their coefficients or prove positivity. Do not promote a hypothetical Dirac action to a canonical UBT action without an independent selection principle.

<!-- BILINGUAL-UNIT: gate -->
## Required next computation
Compute the compatible $\mathscr D_\mu$ from the already specified two-sided connection, square $\slashed{\mathscr D}$ including curvature and torsion, and compare its principal symbol and constraint structure against the frozen canonical action. Track independently the axial torsion, commutator bivectors and any scalar/pseudoscalar projections. **Status: research candidate; full-Hamiltonian OPEN; LEAN-PENDING; CAS-PENDING; bilingual semantic check PENDING.**
