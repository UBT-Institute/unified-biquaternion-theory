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

# Causal access, shared reality, light speed and Hamiltonian selection

**2026-10-27 — first genuine causal-horizon addition to the information-first/operational-shared-reality selector, not the derivation of a unique S_UBT[Theta].**

Cross-references already on master:
- `research_tracks/fundamental_dynamics/SHARED_REALITY_FIRST_PRINCIPLES_RESTART.en.md` — SR0 observer equivariance does not select H.
- `research_tracks/fundamental_dynamics/SHARED_REALITY_INFORMATION_SELECTOR.en.md` — strong information selector remains speculative.
- `research_tracks/information_first/SHARED_REALITY_PRINCIPLE.md` — quantum marginal extension and dynamical nonselection.
- `research_tracks/information_first/OVERLAPPING_ALGEBRAS_HAMILTONIAN_GATE.md` — overlapping local derivations can determine H modulo common commutant if sufficiently rich.
- `research_tracks/information_first/RINDLER_MODULAR_TIME_CALIBRATION.md` — observer wedge modular flow has a conditionally known normalization.
- `research_tracks/causality/einstein_causal_principle.en.md` — universal causal cone does not establish positive Hamiltonian energy.
- `research_tracks/information_first/HAMILTONIAN_EQUALITY_FLRW_CAR_CONSTRAINT.md` — on-shell GR/CAR scalar constraint benchmark.

## 1. Refine the observer primitive: a causal algebra, not global access

Given a *physical* Lorentzian metric g, speed c in local orthonormal units, an observer history worldline gamma and its admissible protocol, define its record domain O as the accessible portion of the causal past J^-(gamma), or an observer-specific causally complete diamond/wedge. Associate to each causally complete region D a physical observable algebra A(D), a normalized positive state omega restricted to A(D), and overlap comparison maps respecting inclusions and gauge/edge equivalences.

Physical **causal shared reality (CSR)** asks for:
  (i) isotony: D1⊂D2 => A(D1)⊂A(D2);
  (ii) microcausality/graded locality for spacelike separated observables;
  (iii) a shared global state (or compatible extension) whose restrictions agree in comparable overlaps, not merely equal single overlap marginals;
  (iv) a dynamical automorphism/covariant evolution whose signal front cannot escape the physical null cone;
  (v) observer agreement about accessible conditional probabilities after proper frame/protocol transport.

At a finite observation event, being *outside the past light cone* is not equivalent to being *behind a true event horizon*. Event horizons are global properties of spacetime and a worldline (and are different from the Rindler horizon of an accelerated observer). Spacelike quantum entanglement can create shared correlations without usable superluminal messages. Therefore CSR is a rule about accessible controllable information, not absence of quantum correlations.

These are **proposed selection criteria** for the existing UBT causal geometry, not additional free fields or a second action. In particular the causal metric g must arise from the UBT composite tetrad for a real UBT derivation; using a prescribed Minkowski metric below is a benchmark.

## 2. Exact 1+1 Dirac counterexample: SAME light cone, DIFFERENT H

On fixed Minkowski spacetime, let the 1+1-dimensional single-particle Hamiltonian family be
  H_m = -i hbar c sigma_x partial_x + m c² sigma_z, m>=0.
Write mu=m c²/hbar. The evolution is
  partial_t psi=-c sigma_x partial_x psi-i mu sigma_z psi.
Its principal symbol is P(w,k)=w I - c k sigma_x and det P=w²-c² k², INDEPENDENT OF m. Therefore the characteristics propagate at speed ±c for every m.

Define rho=psi†psi>=0, j=c psi†sigma_x psi. Then
  partial_t rho+partial_x j=0,
  c rho±j = c |psi_1±psi_2|²>=0,
hence |j|<=c rho. For smooth solutions with compact initial support |x|<=R, differentiating the probability outside the *moving boundaries* x=±(R+ct) shows the outward-tail integrals are nonincreasing from zero. Thus support remains inside |x|<=R+ct for **every m**. This is an exact finite-signal-speed statement, not merely a claim based on group velocity. In the second-quantized local CAR Dirac field with ordinary QFT assumptions it corresponds to the usual graded microcausality.

Two observers restricting the same time-evolved physical state to overlapping causal algebras obtain compatible records for EVERY m. But the Hamiltonians differ in measurable local dynamics: for p=0 and initial spinor |+x>=(1,1)/sqrt(2),
  <sigma_x>(t)=cos(2 m c² t/hbar).
Thus e.g. m=0 versus m≠0 are distinguishable inside the observer's causal domain even though both have exactly the same c-limited signal horizon. This is a constructive **no-uniqueness** result for the proposition that causal access + shared reality alone uniquely determine the Hamiltonian.

## 3. Information is quantitatively affected by c, but not uniquely selected

Measure sigma_x at time t. At p=0 the two probabilities are
  p_+(m)=cos²(m c² t/hbar),  p_-(m)=sin²(m c² t/hbar).
Away from zero-probability singular parameter values, the classical Fisher information per successful independent local sample about m is
  I_m=Σ_(outcomes) (partial_m p)^2/p = 4 c⁴ t²/hbar².
This follows from the standard FI formula, not a new UBT quantum bound; the appropriate limiting value exists for generic nearby parameters. Time and energy resources, number of repetitions, measurement protocol, and finite observational horizon constrain which samples are actually available. The formula demonstrates exactly how c calibrates local information acquisition without selecting m.

Another exact illustration: global |0_A0_B> and |0_A1_B> have the same reduced density matrix for an observer with access only to A, but differ in a B-local observable. An inaccessible region is therefore *informationally hidden from that observer*, while a larger accessible domain could distinguish the global states. A finite-dimensional tensor split is a toy, not a faithful QFT horizon split (type-III local algebras, edge constraints, and renormalization matter).

## 4. What a stronger information-to-gravity derivation would actually require

A promising NONCIRCULAR route combines a causal local algebra, a state, information change, and geometry. Let K_D=-log rho_D in a regulated full-rank finite model, or the appropriate modular generator in a QFT wedge. The first-order entanglement law
  delta S_D = delta <K_D>
is an exact first-order identity around a fixed reference state; by itself it contains NO gravitational dynamics. In special Minkowski vacuum Rindler wedge models, with appropriate Bisognano–Wichmann hypotheses, the modular generator is geometrically related to the Lorentz boost:
  K_W ∼ (2pi / (hbar c)) int_(x>0) x T_00(0,x,y,z) d³x + constant.
This is the **wedge modular/boost generator**, not the global Minkowski-time H. The normalization 2pi/hbar c uses physical light speed and fixes the modular clock only after a state, quantum net and boost geometry have been supplied.

A physically stronger candidate stipulates a *separately justified* horizon entropy-area coefficient
  S_geom/k_B = c³ Area/(4 G hbar)
and local generalized-entropy stationarity/thermodynamic equilibrium for all sufficiently small causal horizons/diamonds. Jacobson's 1995 local-Rindler Clausius argument and 2016 small-ball entanglement-equilibrium theorem show that, under their respective additional assumptions, relations of this sort can produce Einstein equations. These are **external, conditional reference results**, not proofs that existing UBT Theta dynamics satisfy them, or derivations of a unique microscopic Hamiltonian.

To obtain the UBT-specific ADM/CAR equality C_GR+C_CAR+C_mix≈0 rather than importing GR, one must: (a) construct g[Theta], causal diamond/wedge observer algebras and valid states from the SAME Theta field; (b) derive physical modular-energy and geometric-area response plus coefficient, instead of assuming G; (c) show compatibility of the local equations in every observer frame; (d) calculate the full composite gravitational presymplectic/Dirac constraints including edge/horizon charges, and rule out invariant deformations of the kinetic/mass sectors; (e) only then reconstruct one global H/S, not by equating region-specific K_D directly to H.

## 5. Status and decisive result

CSR + universal c **select an admissible causal class of kinetic principal symbols**, not a unique Hamiltonian or arbitrary mass/interactions. Even knowing the full principal cone is insufficient to infer the lower-order generator. Quantitative Fisher information tells observers how well they can *estimate* parameters, not why the microscopic parameters take those values.

This makes the proposed enhanced shared-reality principle operational and testable without falsely claiming to have derived GR or a unique UBT action. It provides a direct research path from horizons → local modular information → response of composite Theta geometry → constrained Hamiltonian. Retain `canonical/ACTION.en.md` status `DEFINED_FAMILY_NOT_FINALIZED`.

Regression: `tests/test_information_causal_access_shared_reality.py` (seven locally passing SymPy tests, including exact continuity/current bound, principal cone, local Fisher information, horizon restriction and counterexample to uniqueness).

Relevant published references: Ted Jacobson, PRL 75, 1260 (1995), https://doi.org/10.1103/PhysRevLett.75.1260 ; Ted Jacobson, PRL 116, 201101 (2016), https://doi.org/10.1103/PhysRevLett.116.201101 ; Bisognano–Wichmann theorem standard modular-wedge reference: https://ncatlab.org/nlab/show/Bisognano-Wichmann+theorem .
