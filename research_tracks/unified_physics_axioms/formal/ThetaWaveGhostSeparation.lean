import Mathlib

/-!
# Oscillatory high-k ghosts in the old eight-real Theta comparator

Finite mode algebra, conditional on the fixed-background kinetic and
potential matrices already derived in theta_kinetic_spectrum.en.md.
No claim about a nondegenerate on-shell UBT vacuum or its constrained
physical spectrum follows.
-/

namespace UBTWaveGhostSeparation

/-- A negative generalized squared mass -mu2 can still have a
positive oscillator frequency above the momentum threshold. -/
theorem high_momentum_oscillates
    {k2 mu2 : ℝ} (hmu : 0 < mu2) (hk : mu2 < k2) :
    0 < k2 - mu2 := by
  linarith

/-- Below the same threshold the squared frequency is negative. -/
theorem low_momentum_exponential
    {k2 mu2 : ℝ} (hmu : 0 < mu2)
    (hk : 0 ≤ k2) (hlt : k2 < mu2) :
    k2 - mu2 < 0 := by
  linarith

/-- A genuine negative kinetic coefficient stays negative in the
momentum Hamiltonian even when the oscillator frequency is real.
Take initial displacement zero and nonzero initial velocity. -/
theorem high_momentum_negative_energy_witness
    {c k2 mu2 : ℝ} (hc : 0 < c) (hmu : 0 < mu2)
    (hk : mu2 < k2) :
    0 < k2 - mu2 ∧
    (-c) * (1 ^ 2 + (k2 - mu2) * (0 : ℝ) ^ 2) < 0 := by
  constructor
  · linarith
  · simp
    linarith

/-- In normalized mode coordinates the signed energy is conserved
under qdot=p, pdot=-(k2-mu2)q regardless of its overall sign. -/
theorem mode_energy_flow_cancels
    (sgn k2 mu2 q p : ℝ) :
    sgn * (p * (-(k2 - mu2) * q) + (k2 - mu2) * q * p) = 0 := by
  ring

/-- An instability cutoff does not select the sign of the kinetic form. -/
theorem sign_does_not_change_frequency
    (k2 mu2 : ℝ) :
    (1 : ℝ) * (k2 - mu2) = (-1) * (-(k2 - mu2)) := by
  ring

end UBTWaveGhostSeparation
