<!-- BILINGUAL-UNIT: exact_stabilizer_torsion_ambiguity -->
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


# Exact torsion ambiguity at fixed Theta and canonical tetrad

**Exact conditional finite deformation, 2026-10-25; not a Hamiltonian or selected action.** Advances #759 and #762.

Restrict to the pure vector Lorentz-lift realization of the locked two-sided derivative, where the value v of the *single* Theta lies in W_L, e^a=N0^-1/2 (dv^a+omega^a_b v^b), with nondegenerate e, time-like nonzero v and metric-compatible spin connection omega (torsion not assumed zero). Let C^a_b be ANY smooth so(1,3)-valued one-form satisfying C^a_b v^b=0 pointwise (the little-group stabilizer of v). Then omega'=omega+C still metric compatible and, EXACTLY,
\[
e'=N0^{-1/2}(dv+omega'v)=e,\quad g'=g,
\quad T'^a-T^a=C^a{}_b\wedge e^b.
\]
Thus the full constrained tetrad identity at fixed (Theta,e) does not in general select torsion. The stabilizer is so(3) with dimension 3 for each of four base indices mu = **12 independent real functions locally**. This is not a dynamical DOF count and cannot be extended without proof to complex/non-vector branches or relative two-sided connections.

An explicit local witness: use N0=1, v=(t,x,y,z) on t²>x²+y²+z², e^a=dv^a and omega=0. Choose any smooth local Lorentz frame L(v) sending v to (r,0,0,0), r=sqrt(t²−x²−y²−z²), and any nonzero spatial rotation generator J with J^a_b (r,0,0,0)^b=0. Set C_mu=L(v)^(-1) J L(v) times a one-form c_mu dx^mu (consistent convention L v = (r,0,0,0)); C v=0. Then D^{omega'}v=dv, so e stays exactly dv and nondegenerate; nevertheless at the point (t,0,0,0) choose c=dx², J^1_3=1,J^3_1=−1 and find (T'^1−T^1)=dx²∧dx³≠0. Lorentz curvature of omega' need not vanish; unlike the #758 toy counterexample, this one satisfies the pure-lift canonical tetrad equation pointwise on its patch.

Significant caveat: omega' here is a choice of **different composite torsion branch**, not an additional independently propagating fundamental field. For fixed tetrad and prescribed torsion the reconstruction omega(e,T) stays unique and consistent with Axiom C. The theorem does NOT claim that both choices satisfy a yet-to-be-derived UBT torsion equation, full Theta E-L equations, or physical global/holomorphic constraints. The missing action-level selector must eliminate or interpret this ambiguity. Treating the 12 stabilizer directions as gauge would require proof that they preserve the full matter/spin coupling, symplectic form and observables; they can modify torsion and spin transport, so gauge status cannot be asserted.
