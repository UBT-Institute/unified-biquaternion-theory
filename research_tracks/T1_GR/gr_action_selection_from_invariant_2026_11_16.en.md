<!-- BILINGUAL-UNIT: gr-action-selection-ledger-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Action-selection audit; no new dynamical theorem.
UBT-AI-PROVENANCE-END
-->
# GAP: Why the biquaternion curvature invariant does not select an action

<!-- UNIT: scope -->
## Status and locked background
[RESEARCH / CONDITIONAL NO-SELECTION] Preserve the single Theta, canonical central metric, bivector Sigma and physical-connection restrictions. This note clarifies a dynamical selection gap, not an obstruction to the existence of the invariant.

<!-- UNIT: family -->
## Two-coefficient family
```text
I_B = R(omega) - i*P(omega),  P = 1/2 epsilon^mnrs R_mnrs(omega)
S[a,b] = integral sqrt(-g) (a*R+b*P)
Parity: R -> +R, P -> -P; if parity is required and a,b are scalar
constants with no pseudoscalar fields, parity invariance forces b=0
The overall a remains unrestricted by the bivector identity.
For Einstein–Cartan omega:
d(e^a wedge T_a) = T^a wedge T_a - e^a wedge e^b wedge R_ab
General torsion squared terms also remain symmetry-allowed.
```
The constants a and b (including a=0) label symmetry-compatible real functionals for a metric-compatible Lorentz connection. The existence of the canonical algebraic identity for I_B does **not** fix either constant. Under orientation/parity inversion P is a pseudoscalar and R a scalar. If one imposes parity invariance on the action, holds constants fixed and excludes any additional pseudoscalar coupling, b=0 follows; a is still undetermined. Reality and parity are distinct requirements; taking Re(I_B) is an action-choice, not a derived Euler–Lagrange principle. The orientation pseudoscalar changes sign under parity; no new independent fundamental observer-metric is postulated.

<!-- UNIT: torsion -->
## Torsion and Nieh–Yan redundancy
On a torsionful branch P need not vanish. The Nieh–Yan identity equates the corresponding Holst-type density to a torsion-square term modulo the exterior derivative of e^a wedge T_a, with convention-dependent factors. The imaginary/odd part can therefore modify torsion sourcing or boundary effects if given a coupling; it does not automatically propagate an independent bosonic mode. Further parity-even torsion-square invariants remain allowed by the same algebra and symmetries. The torsion equation, kinetic signature and physical selection must be calculated from the *full* composite Theta action.

<!-- UNIT: operational -->
## What would qualify as a genuine unifying principle?
A stronger principle must (i) specify a variational or statistical functional of Theta with no freely inserted GR term; (ii) select the reality/parity prescription and coefficients from mathematically stated conditions; (iii) admit at least one on-shell background; (iv) yield two healthy universally coupled massless spin-2 polarizations; (v) recover GR-tested equivalence and observer covariant predictions, while stating new falsifiable deviations or a precise equivalence claim.

<!-- UNIT: priority -->
## Shortest decisive roadmap
G1: inspect the finalized canonical action and audit whether it really produces any second-derivative metric kinetic principal symbol on constrained Lorentz slices, without treating an identity as a field equation.
G2: compute full reduced Euler equations with the derivative implicit-jet operator I-J_E and physical contortion, including zero modes, gauge and boundaries.
G3: find an on-shell background and calculate the complete quadratic action/Hessian, constraints and spin-2 residue.
G4: only if a healthy spin-2 sector exists, analyze its low-energy nonlinear consistency, universality, Newton coefficient and torsion parity-odd terms.
G5: maintain the observer-tidal-covariance benchmark; it is already GR, not a new observer-relative metric.
If G1/G3 fail, seek a genuinely derived information, spectral or collective *dynamical* principle rather than inserting EH by hand.

<!-- UNIT: verification -->
## Audit status
A symbolic parity/no-selection sanity check is in tools/verify_gr_bivector_action_selection_2026_11_16.py; it tests only the 2-parameter family and parity, not a Theta field equation. Cross-reference canonical/gr_closure/gap_10d_induced_gravity_endgame.tex (curvature-coefficient underdetermination already established) and research_tracks/T1_GR/gr_biquaternion_curvature_invariant_2026_11_16.en.md. No new claim of a complete GR derivation. Lean, CI, bilingual semantic verification and full Hamiltonian audit pending; do not merge yet.
