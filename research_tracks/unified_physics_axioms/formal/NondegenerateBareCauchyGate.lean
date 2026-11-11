import Mathlib

/-!
# Exact geometry-flat action and loss of coercivity

Finite algebraic lemmas for the previously established split-jet
bare-action critical-zero branch S = ∫ det(E) F(Theta).
Here F(Theta_*) = 0, so every volume variation is flat.
This file does not formalize the full functional integral, FLRW curvature,
Dirac algorithm, or well-posedness of the PDE.
-/

namespace UBTNondegenerateCauchyGate

def density (volume f : ℝ) : ℝ := volume * f

theorem density_zero_at_critical_field (volume : ℝ) :
    density volume 0 = 0 := by
  simp [density]

theorem arbitrary_geometric_deformation_flat (volume delta eps : ℝ) :
    density (volume + eps * delta) 0 = density volume 0 := by
  simp [density]

/-- There can be no strictly positive quadratic lower bound in a freely
variable tetrad direction at the critical zero, because S is identical there. -/
theorem no_strict_geometric_coercivity (c : ℝ) (hc : 0 < c) :
    ¬ ∀ x : ℝ,
      c * x ^ 2 ≤ density (1 + x) 0 - density 1 0 := by
  intro h
  have hh := h 1
  simp only [density, mul_zero, sub_self, one_pow, mul_one] at hh
  linarith

/-- Two regular FLRW scale-factor jets agree at the initial slice. -/
def scale (alpha t : ℝ) : ℝ := 1 + alpha * t ^ 2

theorem initial_scale_independent_of_acceleration (alpha : ℝ) :
    scale alpha 0 = 1 := by
  simp [scale]

/-- Formula for the first derivative of the polynomial scale factor. -/
theorem initial_scale_slope (alpha : ℝ) :
    2 * alpha * (0 : ℝ) = 0 := by
  ring

/-- The second derivative coefficients differ, so curvature can differ. -/
theorem different_second_derivatives :
    2 * (1 : ℝ) ≠ 2 * (2 : ℝ) := by
  norm_num

/-- Closed FLRW scalar curvature at the initial slice, computed from
the conventional geometric expression and treated here as a definition. -/
def curvatureAtZero (alpha : ℝ) : ℝ := 6 * (2 * alpha + 1)

theorem curvature_witnesses :
    curvatureAtZero 1 = 18 ∧ curvatureAtZero 2 = 30 := by
  norm_num [curvatureAtZero]

end UBTNondegenerateCauchyGate
