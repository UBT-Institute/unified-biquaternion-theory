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

# Composite-tetrad FLRW/CAR Hamiltonian: exact symplectic bridge and single-Theta gate

**2026-10-27 — exact homogeneous GR/CAR reference computation and exact split-jet non-injectivity. NOT the derived fundamental one-Theta UBT Hamiltonian/action.** Sources: `research_tracks/action_selection/single_theta_macdowell_mansouri_candidate.en.md`, `research_tracks/action_selection/splitjet_presymplectic_gate.en.md`, `research_tracks/information_first/HAMILTONIAN_EQUALITY_FLRW_CAR_CONSTRAINT.md`, and `canonical/ACTION.en.md`.

## 1. Explicit off-shell FLRW lift with Theta entirely fixed

Set the internal metric eta=diag(1,-1,-1,-1) and use
 E_mu^a = N0^(-1/2) [partial_mu X^a + omega_mu^a_b X^b + (K_J)_mu^a_b X^b + w_mu X^a],
where X is the Lorentz-real projection of Theta, N0>0 and X²>0. **Hold the whole Theta fixed**, including Im Theta, so that X^a=r delta^a_0 (r>0) and partial_mu X=0.

For ANY positive a(t), lapse L(t)>0, let the torsionless flat-FLRW spin connection and auxiliary jet have boost components
 omega_i^j_0 = [dot(a)/L] delta_i^j,
 (K_J)_i^j_0 = [sqrt(N0) a/r - dot(a)/L] delta_i^j,
 w_0 = sqrt(N0) L/r,
with other shown components zero and Lorentz-antisymmetric completions of omega,K_J. Substitution is exact:
 E_mu^a=diag(L,a,a,a),  g_munu=diag(L²,-a²,-a²,-a²).

Thus distinct scale factors a(t) and extrinsic curvatures are realized at the SAME fixed Theta by changing omega,K_J,w. Even if two scale factors agree at a time t0, different dot(a)(t0) gives identical instantaneous E and different gravitational momenta. **There is therefore no single-valued a[Theta] or p_a[Theta] in the existing off-shell split-jet chart**, absent an additional derived rule fixing the auxiliaries/connection. This is not a universal no-go against different UBT dynamics: surjectivity of the auxiliary variation reproduces the Palatini field equations, not a unique solution of K_J,w in terms of Theta.

## 2. Gauge-invariant (under split-jet carrier shifts) geometric variables

Work in the homogeneous comoving spatial gauge with unit fiducial volume, no spatial shift. Define
 q_ij = -eta_ab E_i^a E_j^b,
 a(E)=[det(q_ij)]^(1/6),
 H(E,omega)=[sum_(i=1)^3 omega_i^i_0]/[3a(E)],
 p_a(E,omega)=-6 a(E)^2 H(E,omega)/kappa, kappa=8 pi G.

The H(omega) identification holds in the torsionless FLRW connection gauge, not generally. Under carrier shifts X→X+epsilon, Q→Q-D_omega epsilon, with omega unchanged and Q=K_J X+wX, E is unchanged; hence the displayed a and p_a are invariant under that **pure-gravity** redundancy. This is a homogeneous coordinate-gauge quantity, not a general diffeomorphism-invariant local observable.

In the ADM reference theory q_ij=a² delta_ij and pi^ij=−a H delta^ij/kappa. Pulling back its symplectic potential gives
  ∫ pi^ij delta q_ij = (-6a²H/kappa)delta a=p_a delta a.
The gravitational ADM scalar constraint is
  C_GR=(2kappa/sqrt(q))(pi_ij pi^ij-pi²/2)−sqrt(q)(3R−2Lambda)/(2kappa)
      =−kappa p_a²/(12a)+Lambda a³/kappa
on the flat homogeneous branch. This is a proven restricted pullback of the **reference ADM** potential, NOT a proof that the complete MM split-jet presymplectic form is canonically equivalent including all gauge kernels and boundaries.

## 3. Common reduced Hamiltonian constraint and state action

Let c_j (j=1,...,4) be orthogonal-quaternion/Jordan–Wigner CAR operators and N_f=Σc_j†c_j, with occupations n=0,...,4 and multiplicities (1,4,6,4,1). Take zero comoving momenta and m>0. A homogeneous/isotropic matter interpretation additionally restricts the Fock state to rotationally invariant states or suitable spin-unpolarized mixtures: a generic polarized occupation state does not automatically give an isotropic stress tensor.

The **reference** combined scalar constraint is
  C(E,omega,c)=−kappa p_a(E,omega)²/(12a(E))+Lambda a(E)³/kappa+m N_f ≈ 0.
In an N_f=n sector it yields H²=Lambda/3+kappa m n/(3a³).

The corresponding **single reduced reference phase-space action**, not the canonical S_UBT, is
  S_mini[a,p_a,Phi,L,lambda] = ∫dt [
   p_a dot(a)+(i/2)(Phi†dot(Phi)-dot(Phi†)Phi)
   −L(−kappa p_a²/(12a)+Lambda a³/kappa+m Phi†N_f Phi)
   +lambda(Phi†Phi−1) ].
Variation of L gives C=0; of p_a gives dot(a)=−L kappa p_a/(6a); of Phi† gives i dot(Phi)=(L m N_f−lambda)Phi. Number N_f is conserved for this toy Hamiltonian. Eliminating p_a reproduces the usual gravitational Lagrangian −3a dot(a)²/(kappa L)−L Lambda a³/kappa and CAR matter term. Gravity a,p_a and finite Fock Phi are independent variables of this reference action: this is NOT a one-Theta fundamental derivation.

## 4. What we have actually excluded / next constructive test

The current off-shell split-jet map (Theta,omega,K_J,w)→E is not injective even when Theta is fixed. The separate CAR occupation also requires quantum-state data: in a reference representation the vacuum and one-particle state at the SAME Theta and E have distinct N_f. Therefore the Hamiltonian equality alone does not construct a[Theta], p_a[Theta], N_f[Theta] without a derived state/geometry identification.

Also, if the physical Dirac spinor is the invertible real-antilinear image Psi=F(Theta), changing Theta by an arbitrary local carrier shift changes Psi. The ordinary Dirac kinetic/mass action is generically not invariant under such a spinor shift. One cannot retain the entire pure-gravity split-jet shift as first-class symmetry in the full theory without recomputing it. This is compatible with the earlier spinor mass split-jet obstruction.

**Next gate:** compute the actual composed MM+matter *covariant presymplectic form* and its kernel, checking whether the quotient supports both ADM brackets and CAR without independent microscopic fields. A successful finite model can then be extended to the already constructed infinite CAR algebra. Do not alter `canonical/ACTION.en.md` FINALIZED status.

Regressions: `tests/test_information_composite_tetrad_flrw_bridge.py` — nine focused symbolic tests, passed locally.
