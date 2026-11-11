import Mathlib

/-!
# Conditional tensor mode stability in an assumed Palatini comparator

The one-action UBT selection problem is OPEN. The input for this file
is the standard transverse-traceless reduced quadratic vacuum GR
Hamiltonian on Minkowski with positive coupling and positive wave
number. The GR TT reduction, the Palatini split-jet lift, and the
full Dirac/PDE arguments are NOT proven here. Lean proves finite
energy inequalities and oscillator conservation algebra only.
-/

namespace UBTSplitJetTTGate

/-- Canonically normalized quadratic Hamiltonian for one TT oscillator.
omega2 is the *nonnegative squared spatial wave number*. -/
noncomputable def oscillatorEnergy (omega2 q p : ℝ) : ℝ :=
  (p ^ 2 + omega2 * q ^ 2) / 2

theorem oscillator_energy_nonnegative
    {omega2 q p : ℝ} (h : 0 ≤ omega2) :
    0 ≤ oscillatorEnergy omega2 q p := by
  unfold oscillatorEnergy
  positivity

theorem two_polarization_energy_nonnegative
    {omega2 qplus pplus qcross pcross : ℝ}
    (h : 0 ≤ omega2) :
    0 ≤ oscillatorEnergy omega2 qplus pplus +
      oscillatorEnergy omega2 qcross pcross := by
  have ha := oscillator_energy_nonnegative (q := qplus) (p := pplus) h
  have hb := oscillator_energy_nonnegative (q := qcross) (p := pcross) h
  linarith

/-- Substituting the Hamilton equations qdot=p and
pdot=-omega2*q makes the formal energy derivative vanish. -/
theorem canonical_energy_flow_cancels (omega2 q p : ℝ) :
    p * (-omega2 * q) + omega2 * q * p = 0 := by
  ring

/-- With positive gravitational normalization, TT density has
nonnegative quadratic time- and spatial-derivative contributions. -/
noncomputable def ttEnergyDensity (kappa kinetic2 gradient2 : ℝ) : ℝ :=
  (kinetic2 + gradient2) / (8 * kappa)

theorem tt_density_nonnegative
    {kappa kinetic2 gradient2 : ℝ}
    (hk : 0 < kappa) (h1 : 0 ≤ kinetic2)
    (h2 : 0 ≤ gradient2) :
    0 ≤ ttEnergyDensity kappa kinetic2 gradient2 := by
  unfold ttEnergyDensity
  positivity

end UBTSplitJetTTGate
