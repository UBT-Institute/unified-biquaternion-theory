<!-- BILINGUAL-UNIT: adm_constraint_negative_theta_witness -->
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


# ADM constraint solvability is not positive-energy stability

**Conditional exact initial-data example, 2026-10-26.** Assumes an independently dynamical 4D metric with Einstein-Hilbert ADM kinetic term and the already tested indefinite Theta kinetic term, not the locked composite-metric UBT action. Spatial three-torus, unit flat metric, coordinate volume normalized to one, vanishing spatial gauge fields and homogeneous Theta data.

At q=q0=i r I, choose momentum solely in the non-boost Im(z3) component, p_Theta=lambda. All six Theta Gauss charges vanish exactly. The Theta kinetic density is -lambda²/4 with G=diag(2,-2,-2,-2,2,-2,-2,-2). Write the fixed scalar potential V(q0)=V0, and choose constant ADM gravitational momenta pi^ij=diag(k,-k,0), which are transverse traceless for the flat spatial metric. The spatial curvature is zero and gravitation's momentum constraint -2 h_ij D_k pi^jk=0. Homogeneous scalar data have vanishing momentum current; gauge field momenta are zero. Thus all three spatial momentum constraints hold.

In the convention
C_perp=(2 kappa/sqrt(h))(pi^ij pi_ij - pi²/2) - sqrt(h) R3/(2 kappa) + H_Theta,
the remaining scalar Hamiltonian constraint is
C_perp = 4 kappa k² - lambda²/4 + V0 = 0.
For kappa>0 and lambda² >= 4 V0, choose
k²=(lambda²/4-V0)/(4 kappa).
There are solutions for arbitrarily large |lambda| on this compact slice. This constructs an unbounded family of negative matter kinetic contributions *on the full scalar and momentum constraint surface* of the adopted minimally coupled GR-plus-Theta initial-data model. It is not a proof of a negative reduced physical Hamiltonian or a negative ADM mass. On compact topology the canonical Hamiltonian is a sum of constraints and vanishes on shell; an ADM surface energy is not defined without asymptotically flat ends and suitable falloff.

The example is NOT a fully demonstrated solution of a new single UBT action: it assumes independence of g, a particular GR-plus-Theta matter action, that the Theta potential depends only on q, and no additional psi fiber constraints or composite spin-connection relations. It does not establish well-posed time development for these data, nor a gauge-invariant physical ghost count. It does show that *even full classical ADM scalar and spatial constraints of this conventional candidate* do not simply eliminate arbitrary negative Theta kinetic data.

For reference, pure trace pi^ij=p sqrt(h)h^ij contributes -3 p² h/2 before the factor 2kappa/sqrt h and therefore cannot compensate a negative Theta contribution on flat h with zero V. The tracefree choice above is the appropriate explicit algebraic witness.

Next: derive the full model's unique action and symplectic constraints, then analyze physical energy on noncompact/asymptotically flat solutions or gauge-fixed local reduced degrees. Avoid confusing the ADM constraint density with an observable conserved energy.
