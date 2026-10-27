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

# Antilinear chiral reconstruction from one biquaternion: exact representation bridge

**2026-10-26. Algebraic spin representation only; does not establish a fundamental Dirac action, Grassmann statistics or composite-tetrad compatibility.**

Write Theta=(u,v) with two independent complex 2-spinor columns and let Theta->S Theta, S in SL(2,C). Define epsilon=i sigma_2=[[0,1],[-1,0]] and J(v)=epsilon conjugate(v). Then epsilon conjugate(S) epsilon^(-1)=(S^dagger)^(-1). Therefore
 Psi_D(Theta)=(u,J(v)) in (1/2,0)⊕(0,1/2)
intertwines the proper Lorentz spin action **as a real-linear, antilinear-on-second-column map**:
 Psi_D(S Theta)=diag(S,(S^dagger)^(-1))Psi_D(Theta).
Inverse: u=Psi_L, v=epsilon^(-1) conjugate(Psi_R), with appropriate conjugation placement (epsilon real and epsilon^(-1)=-epsilon); explicitly since Psi_R=epsilon bar(v), v=bar(epsilon^(-1) Psi_R)=epsilon^(-1) bar(Psi_R). Thus all eight real components survive; no independent fundamental second field is added.

IMPORTANT correction to an overbroad earlier claim: if one applies J to **the same** u and writes (u,J(u)), the resulting constrained Majorana-like 4-spinor has only four real independent components; for two independent columns u,v, the resulting Psi_D has eight real independent components and is an unconstrained Dirac representation under proper Lorentz transformations. Further, J²=-I on Weyl C² (epsilon is real, epsilon²=-I), and J is antilinear: J(i v)=-i J(v). Hence the map changes the natural global U(1) charges: Theta->e^(iφ)Theta yields Psi_L->e^(iφ)Psi_L, Psi_R->e^(-iφ)Psi_R, an **axial**, not vector-like, phase. A standard Dirac mass m(bar Psi_L Psi_R+bar Psi_R Psi_L) is not invariant under that original global phase for general φ; it would require breaking/compensating the symmetry or a justified different action on Theta columns. This is a concrete new selection gate.

The Dirac symplectic term and Grassmann CAR **do not arise from algebraic real-linear relabeling** of a commuting biquaternion. Any derived spinor Hamiltonian must still demonstrate: (i) admissible physical graded structure; (ii) spinorial soldering compatible with locked E=DTheta/sqrt(N0) and split-jet shifts; (iii) U(1) charge/mass selection; (iv) full canonical constraints and energy positivity. Algebraic bridge is a genuine step, not the complete theory.

Tests: tests/test_information_antilinear_spinor_bridge.py.
