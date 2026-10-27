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

# Explicit one-biquaternion Dirac evolution and pullback action

**2026-10-26. Closed FLAT-BACKGROUND Dirac subsystem conditional on the left-spinor representation and a specified kinetic term; not a derived unified UBT action.** Follows `ANTILINEAR_BIQUATERNION_DIRAC_BRIDGE.md` and `GRASSMANN_SPINOR_HAMILTONIAN_ACTION_GATE.md`.

Let Theta=[u v], epsilon=i sigma2, J(Theta)=epsilon conjugate(Theta) sigma1^(col) where the final sigma1 swaps Theta's two columns. Define Psi_L=u, Psi_R=epsilon conjugate(v) and p=-i nabla. Use Dirac h_D=diag(-sigma·p,+sigma·p)+m beta, beta offdiagonal.

**Exact one-matrix evolution:**
  i partial_t Theta = -sigma·p Theta +m epsilon conjugate(Theta) sigma1^(col).
Equivalently
  i dot u=-sigma·p u +m epsilon conjugate(v),
  i dot v=-sigma·p v +m epsilon conjugate(u).
The second equation is the complex conjugate of the right-handed Dirac equation after applying epsilon. The key pseudoreality identities are epsilon sigma_i* epsilon^(-1)=-sigma_i and epsilon²=-I₂. Thus Psi(Theta) obeys
  i dot Psi= h_D Psi.
Conversely every solution of flat Dirac maps back bijectively to Theta. The field Theta therefore satisfies the componentwise Klein–Gordon equation (partial_t²-Delta+m²)Theta=0 in this fixed frame. **Do not claim** that the naive real-antilinear right-hand-side map H_Theta has a complex-linear Hermitian spectral square: the pullback of multiplication by i on Psi acts with opposite complex structures on the two Theta columns.

**An explicit conditional flat action, not guessed separately:** pull back the standard first-order Dirac action along the invertible real-linear map,
  S_spin^flat[Theta]=∫d⁴x [i Psi(Theta)† partial_t Psi(Theta)-Psi(Theta)† h_D Psi(Theta)].
This is a single Theta variable and its conjugate, with background Minkowski tetrad specified EXTERNALLY and Dirac kinetic coefficient assumed. Its Euler–Lagrange equation is exactly the displayed one-matrix evolution (up to boundary assumptions). As a commuting c-number field it is classical/first-quantized spinor wave dynamics, not fermionic field statistics; as odd field it requires graded derivatives/ordering. The mass bilinear is 2m Re det Theta only for commuting entries; for odd entries it is -m(B+B†), B=u^T epsilon v, from the companion gate.

**Limitations:** This does not derive an invertible classical composite tetrad and fermionic CAR from the SAME homogeneous microscopic Theta. It does not prove local Lorentz soldering consistent with locked E_mu=D_mu Theta/sqrt(N0), nor provide ADM+matter off-shell symplectic equivalence. Mass m and Dirac kinetic coefficient remain input choices. The covariant Einstein–Dirac reference action in GRASSMANN_SPINOR_HAMILTONIAN_ACTION_GATE.md is separate. Never promote this flat action to S_UBT or mark the canonical family FINALIZED.

Algebra regression: tests/test_information_one_theta_dirac_evolution.py.
