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

# Minimal information geometry to symplectic mechanics: qubit control example

**P0 controlled calculation, 2026-10-26. Not a Theta-derived quantum state or fundamental UBT action.**

Let z=(cos(theta/2), exp(i phi)sin(theta/2))^T be a normalized pure state, with ray space CP1. Direct substitution into the quantum geometric tensor Q_ij=<partial_i z|(1-|z><z|)|partial_j z> yields Q_theta theta=1/4, Q_phi phi=sin²(theta)/4, Q_theta phi=i sin(theta)/4 (convention for z). Its real part is Fubini-Study metric ds²=(dtheta²+sin²theta dphi²)/4; 2 Im Q_theta phi = sin(theta)/2 is a symplectic curvature, with choice of Berry-potential orientation. Set A=-i<z|dz>=sin²(theta/2)dphi; then dA=(sin(theta)/2)dtheta wedge dphi.

An explicit **trial** first-order action S=integral (A_i(q)dot q^i-H(q))dt has presymplectic form dA and Hamiltonian EOM Omega_ij dot q^j=partial_i H, with overall sign depending on convention for matrix indexing. Critically, CP1 geometry does not determine H: arbitrary distinct smooth H on the same state geometry yield inequivalent flows. Nothing in this computation proves the single biquaternion Theta admits a positive-definite quantum inner product or a CP1 identification.

Observer-dependence example: for the same pure z, a phase-insensitive observer accessing only the dephased diagonal subalgebra sees rho_diag=diag(cos²(theta/2),sin²(theta/2)), entropy S=-p log p -(1-p)log(1-p), which is independent of phi. A full observer sees pure-state von Neumann entropy zero. Hence entropy as a single scalar is information-losing: it cannot reconstruct the phase variable phi or the Berry symplectic curvature. Distinct observer entropies are consistent with a common objective pure state and do not alone generate unique time evolution.

**Action-selection gate:** Provide a justified, Lorentz-covariant map Theta -> physical state space and observables, a local quantum geometric tensor / renormalization, and a microscopic energy generator H[Theta] compatible with all constraints. Demonstrate that resulting Berry/phase term, including tau=t+i psi, reproduces composite geometry, nondegenerate tetrad and healthy Dirac-reduced spectrum. Without that, this is a quantum-information benchmark, not a UBT action/Hamiltonian solution.

Test: tests/test_information_quantum_geometry.py.
