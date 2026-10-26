<!-- BILINGUAL-UNIT: stabilizer_presymplectic_decision -->
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


# Stabilizer-sector presymplectic decision gate

**2026-10-25. Conditional Hamiltonian diagnostics, NOT a derived UBT action.** Follows #763 and #765. Twelve components of the local timelike-little-group stabilizer can change torsion and spin curvature while leaving the restricted pure-Lorentz-lift Theta tetrad unchanged. This does not imply twelve propagating degrees of freedom.

Introduce c^I (I=1..12) only as local auxiliary coordinates labeling this stabilizer ambiguity; **not independent fundamental fields**. Compare two illustrative candidate sectors.

(1) Algebraic auxiliary density l_aux=1/2 c^T M c+J^T c with nonsingular symmetric M. Primary momenta p_c=0; stationarity fixes c=-M^{-1}J. Primary and secondary constraints together form second-class pairs when M invertible; physical c mode count is zero. Eliminated potential is -1/2 J^T M^{-1}J. Whether such M and J emerge from single Theta is unknown.

(2) A time-derivative term l_kin=1/2 dot(c)^T K dot(c)-V(c), with nonsingular K. Kinetic Hessian rank=12, so these auxiliary coordinates would appear dynamical in an *independent-field toy extension*. This extension is not a valid one-field UBT derivation; genuine propagating modes require reduction to Theta and a gauge/constraint analysis.

(3) Degenerate K or mixed terms can generate additional constraints. Distinct actions may assign distinct canonical status to the same geometrical stabilizer family. The locked tetrad and algebraic symmetries do not fix the presymplectic current or kinetic matrix K.

For the actual one-field theory, do NOT postulate independent c variables. The correct diagnostic is to determine c[Theta,partial Theta,...] from a selected composite torsion equation, substitute it into a unique Theta action, compute its covariant presymplectic current omega=delta theta, perform gauge reduction, then test its rank along variations associated with the stabilizer directions and closure/energy. If variations have delta Theta=0 identically and connection is strictly a single-valued functional of Theta, nonzero delta c at fixed Theta is *not a tangent vector* in the physical configuration space. If connection reconstruction remains multivalued, one must first resolve the branch or its equivalence relation; it is not automatically a genuine physical phase-space mode.

All sign, constraint and stability statements below are toy diagnostics only and cannot select H_UBT or S_UBT.

Regression: exact 12x12 Hessian and elimination example, test_stabilizer_presymplectic_decision.py.
