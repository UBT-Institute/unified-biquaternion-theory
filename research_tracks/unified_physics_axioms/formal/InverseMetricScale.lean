import Mathlib

/-!
# Inverse metric scale: conditional scalar-algebra kernel

These theorems formalize only the scalar scale-recovery step of
conformal Lorentzian metric reconstruction. They do NOT construct
a metric, a volume form, a quantum-information density or gravity.
No `sorry` or additional axioms are introduced here.
-/

/-! The hypotheses deliberately supply a scalar reference density; no theorem below
claims that a covariant information measure or spacetime metric has been derived. -/

namespace InverseMetricScale

/-- A nonzero conformal scale preserves the vanishing set of a
    quadratic-form evaluation (the pointwise null cone). -/
theorem nullCone_iff (omega q : ℝ) (homega : omega ≠ 0) :
    omega ^ 2 * q = 0 ↔ q = 0 := by
  constructor
  · intro h
    rcases mul_eq_zero.mp h with hscale | hq
    · exact False.elim ((pow_ne_zero 2 homega) hscale)
    · exact hq
  · intro h
    simp [h]

/-- The dimension-four determinant volume-density scaling identity,
    represented here by the positive scalar factor. -/
theorem volumeScale_four (omega baseVolume : ℝ) :
    (omega ^ 2) ^ 2 * baseVolume = omega ^ 4 * baseVolume := by
  ring

/-- For nonnegative scales, a fixed nonzero reference volume and equal
    fourth-power volume densities determine the scale uniquely. -/
theorem scale_unique_of_equal_volume
    {omega₁ omega₂ baseVolume : ℝ}
    (h₁ : 0 ≤ omega₁) (h₂ : 0 ≤ omega₂)
    (hbase : baseVolume ≠ 0)
    (hvol : omega₁ ^ 4 * baseVolume = omega₂ ^ 4 * baseVolume) :
    omega₁ = omega₂ := by
  have hpow : omega₁ ^ 4 = omega₂ ^ 4 := by
    exact (mul_right_cancel₀ hbase) hvol
  exact (pow_left_inj₀ h₁ h₂ (by norm_num : (4 : ℕ) ≠ 0)).mp hpow

/-- Conformal rescaling preserves a zero evaluated quadratic form
    even when the scalar density is not independently specified. -/
theorem nullCone_conformal_invariance
    (omega q : ℝ) (h : q = 0) :
    omega ^ 2 * q = 0 := by
  simp [h]

end InverseMetricScale
