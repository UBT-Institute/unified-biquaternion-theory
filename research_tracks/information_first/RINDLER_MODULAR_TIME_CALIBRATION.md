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

# Rindler modular time calibration: exact benchmark, not a fundamental UBT Hamiltonian

**Research gate, 2026-10-26.** Use natural units c=hbar=k_B=1. In flat 1+1 Minkowski spacetime choose right wedge x>|t| and coordinates t=rho sinh(eta), x=rho cosh(eta), rho>0. The induced metric is ds²=-rho² d eta²+d rho². For an observer at constant rho=rho0, proper time is tau=rho0 eta; its proper acceleration is a=1/rho0.

In a Lorentz-invariant QFT vacuum satisfying the appropriate wedge modular theorem (Bisognano–Wichmann hypotheses), the reduced right-wedge state has modular Hamiltonian K=-log rho_R=2 pi B+log Z, where B generates dimensionless boost parameter eta. The same observer's proper-time Hamiltonian is H_tau=B/rho0, thus:

  beta_tau = 2 pi rho0 = 2 pi/a,
  H_tau=(K-log Z)/(2 pi rho0).

This is **conditional** on a physical Hilbert space, QFT vacuum, wedge operator algebra, and the theorem's assumptions; the Rindler coordinate transformation alone does not derive the quantum state or thermal property. The apparent temperature is observer-dependent, and rho0 is arbitrary. Therefore the proportionality does not select a unique observer-independent microscopic H or its scale.

The QFT modular flow for a generic region/state need not be geometric or coincide with a globally conserved Hamiltonian. For interacting gravity, wedge algebras, diffeomorphism constraints, gauge-edge modes, entropy regularization and boundary contributions require new care.

**UBT proof obligations**
1. Construct nondegenerate composite tetrad and Lorentzian metric from Theta with correct time orientation.
2. Supply a quantum algebra/state assignment and demonstrate a Lorentz-invariant reference state for which modular covariance holds; do not postulate a Gibbs form solely to close the action gap.
3. Relate geometric boost generators to Theta phase-space charges using the *same* presymplectic potential and full composite connection variation. Boundary/edge charges must be included.
4. Compare two observers with different rho0. They may infer different proper-time H_tau and Unruh temperatures but must predict consistent underlying correlation functions.
5. Compute Dirac constraints, verify a positive physical-energy spectrum and a propagating spin-2 sector before declaring H_UBT.
6. Preserve canonical/ACTION.en.md status DEFINED_FAMILY_NOT_FINALIZED until a unique microscopic functional is established.

**Decision:** horizon modular flow can calibrate an observer's time against a known boost generator given substantial independent quantum assumptions. It cannot by itself derive Theta action, eliminate SO(2) connection, or fix G and hbar.

Exact coordinate/temperature tests: tests/test_information_rindler_modular_calibration.py.
