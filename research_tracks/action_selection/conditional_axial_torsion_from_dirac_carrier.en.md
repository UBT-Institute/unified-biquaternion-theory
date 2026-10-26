<!-- BILINGUAL-UNIT: conditional_axial_torsion_from_dirac_carrier -->
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


# Conditional axial torsion source from one-biquaternion Dirac carrier

**Conditional derivation; 2026-10-25. NOT the fundamental UBT action, not the derivation of its Hamiltonian.** Following #724 Weyl-dual carrier, #742–#745 torsion and selector work.

Let the *derived* Dirac carrier be Psi=F(Theta)=(xi,epsilon chi*) where Theta=[xi,chi]. F is a real-linear representation map with chosen right column frame, not proven an intrinsic covariant physical spinor construction of full UBT. In a metric-compatible Lorentz frame, assume a standard symmetrized Dirac kinetic density
\[
L_D=\frac{ie}{2}\left[\bar\Psi\gamma^\mu\nabla_\mu\Psi-(\nabla_\mu\bar\Psi)\gamma^\mu\Psi\right]-me\bar\Psi\Psi,
\quad \nabla_\mu\Psi=\partial_\mu\Psi+\tfrac14\omega_{\mu ab}\gamma^{ab}\Psi,
\]
where \(\gamma^{ab}=\frac12[\gamma^a,\gamma^b]\), and the adjoint derivative has the opposite spin representation. Vary the spin connection **at fixed tetrad and spinor**:
\[
\delta_{\omega}L_D=\frac{ie}{8}\bar\Psi\{\gamma^\mu,\gamma^{ab}\}\Psi\,\delta\omega_{\mu ab}.
\]
The Clifford identity \(\{\gamma^c,\gamma^{ab}\}=2\gamma^{cab}\), with \(\gamma^{cab}\) totally antisymmetrized, implies that the Lorentz spin density \(S^{cab}\propto i\bar\Psi\gamma^{cab}\Psi\) is a three-form and is Hodge-dual to an axial Dirac current \(\bar\Psi\gamma_d\gamma^5\Psi\) (up to gamma and Levi-Civita sign conventions).

This is **positive evidence for an axial current source**, conditional on the *added* Dirac kinetic law. In an Einstein-Cartan-type auxiliary gravity model with a nondegenerate algebraic quadratic torsion sector, such a source generically produces a nonzero totally antisymmetric torsion (with coefficients depending on the gravitational action). That inference must not be promoted to UBT: variation with respect to omega independent of E and Theta is a diagnostic, whereas full UBT fixes E=DTheta/sqrt(N0) and reconstructs the connection. Full chain-rule variations and constraint reduction can alter both the source and equation, and no second independent fundamental field is permitted.

Important no-circularity gate: do not simultaneously assume standard Dirac action and Einstein-Cartan gravity and then claim to derive the unique fundamental Theta action. To close the problem, derive from locked Theta kinematics and a justified dynamical principle both the spinor evolution and a torsion constraint that reduces to this axial source, then compute phase-space constraints/Hamiltonian and stability. This note establishes a precise *candidate current* rather than its dynamical necessity.

Validation: exact flat Clifford anticommutator regression in tests/test_conditional_dirac_spin_torsion.py.
