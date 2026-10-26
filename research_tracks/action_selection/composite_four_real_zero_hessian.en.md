<!-- BILINGUAL-UNIT: composite_four_real_zero_hessian -->
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


# Four-real-component composite vector slice: zero velocity Hessian

**Conditional exact theorem (2026-10-26).** Not a calculation for unrestricted eight-real biquaternion Theta or a velocity-dependent reconstructed connection.

Assume a Lorentz-real vector carrier V^a, a nondegenerate composite tetrad E_mu^a=N0^(-1/2) D_mu V^a, and g_mu nu=eta_ab E_mu^a E_nu^b. Take the SAME Lorentz pairing in the trial kinetic contraction, so g^mu nu eta_ab D_mu V^a D_nu V^b=4N0. The minimal kinetic-plus-algebraic-potential density is therefore L=F(V) sqrt(-g), with F independent of derivatives; numerical normalization of F is not fixed here.

Choose a connected fixed-orientation patch and a time coordinate. Hold an independent auxiliary connection A_mu^a_b fixed under the velocity Hessian, with D_0 V^a=dot V^a+A_0^a_b V^b, D_i V^a=partial_i V^a+A_i^a_b V^b. With epsilon=sgn(det D_mu V^a), and sqrt(-g)=|det D V|/N0², the determinant is affine in the four dot V^a. Therefore
pi_a=epsilon F(V) Cofactor_(0,a)(D V)/N0²,
H_ab=d pi_a/d dot V^b=0.
All four cofactor coefficients depend only on spatial rows D_i V and not on dot V. Thus four **candidate primary momentum constraints** phi_a=pi_a-epsilon F(V) Cofactor_(0,a)/N0²≈0 hold in this chosen auxiliary-connection formulation. Their Poisson-bracket matrix, secondary consistency conditions and first/second-class decomposition have NOT been evaluated.

This is a degenerate first-order-in-velocities determinant Lagrangian, not a healthy four-scalar kinetic term. On a fixed oriented patch, the F=constant case is a Jacobian-type total derivative if the connection vanishes; with connection/potential there can be nontrivial couplings. In particular a vanishing Hessian does not prove a positive physical Hamiltonian.

**Important scope limit:** If A=A[Theta,DTheta] or torsion K[Theta] is reconstructed with velocity dependence, differentiating the substituted action introduces delta A/d dot Theta and may destroy the affine-velocity premise. Likewise the unconstrained biquaternion eight-real carrier need not satisfy a central real Lorentz metric identity off the real slice. The present result is exact for four real carrier components with independent velocity-free auxiliary A; it is NOT a claim about the full eight-by-eight Hessian of canonical UBT.

The timelike radial case is in the merged PR #775; this note generalizes the cofactor observation under the explicitly stated independent-connection assumptions. Existing Proposition 9 already excludes certain nondegenerate stationary solutions; this result does not evade that obstruction.

Reproduction: tools/verify_composite_vector4_hessian.py and tests/test_composite_vector4_hessian.py.
