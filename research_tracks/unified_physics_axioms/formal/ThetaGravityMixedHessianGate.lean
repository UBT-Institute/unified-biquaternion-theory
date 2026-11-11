import Mathlib

/-!
# Mixed reduced graviton/complex-Theta velocity Hessian stability gate

A two-dimensional principal minor with a>0, a cross kinetic mixing b,
and spectator coefficient c is studied. This is only applicable when
both directions survive the Dirac quotient: a negative unreduced
principal minor alone is not proof of a physical ghost in full UBT.

The finite algebra here is new as an explicit gate for proposed
kinetic couplings. No microscopic one-Theta action is assumed.
-/

namespace UBTMixedHessian

def kineticForm (a b c x y : ℝ) : ℝ :=
  a*x^2 + 2*b*x*y + c*y^2

def determinant (a b c : ℝ) : ℝ :=
  a*c - b^2

/-- Completing the square without division is exact for every parameter. -/
theorem scaled_completed_square (a b c x y : ℝ) :
    a * kineticForm a b c x y =
      (a*x+b*y)^2 + determinant a b c * y^2 := by
  unfold kineticForm determinant
  ring

/-- If a>0 and the principal determinant is nonnegative,
the kinetic quadratic form is nonnegative on this two-mode space. -/
theorem nonnegative_iff_gate
    {a b c x y : ℝ}
    (ha : 0 < a) (hdet : 0 ≤ determinant a b c) :
    0 ≤ kineticForm a b c x y := by
  have hscaled : 0 ≤ a * kineticForm a b c x y := by
    rw [scaled_completed_square]
    have hx : 0 ≤ (a*x+b*y)^2 := sq_nonneg _
    have hy : 0 ≤ determinant a b c * y^2 :=
      mul_nonneg hdet (sq_nonneg _)
    linarith
  nlinarith

/-- A negative determinant gives a real negative kinetic direction. -/
theorem negative_det_witness
    {a b c : ℝ}
    (ha : 0 < a) (hdet : determinant a b c < 0) :
    kineticForm a b c (-b) a < 0 := by
  have hkey := scaled_completed_square a b c (-b) a
  have hsq : 0 < a^2 := sq_pos_of_ne_zero (ne_of_gt ha)
  have hneg : determinant a b c * a^2 < 0 :=
    mul_neg_of_neg_of_pos hdet hsq
  have hsimple : a * kineticForm a b c (-b) a =
      determinant a b c * a^2 := by
    convert hkey using 1 <;> ring
  have hproduct : a * kineticForm a b c (-b) a < 0 := by
    rw [hsimple]
    exact hneg
  nlinarith

/-- A negative spectator diagonal cannot be cured by arbitrary mixing. -/
theorem negative_spectator_witness
    {a b c : ℝ} (hc : c < 0) :
    kineticForm a b c 0 1 < 0 := by
  simpa [kineticForm] using hc

/-- A zero spectator diagonal coupled to a positive mode creates
an indefinite nondegenerate two-mode kinetic block. -/
theorem mixed_zero_spectator_is_ghost_candidate
    {a b : ℝ} (ha : 0 < a) (hb : b ≠ 0) :
    kineticForm a b 0 (-b) a < 0 := by
  apply negative_det_witness ha
  unfold determinant
  have hbsq : 0 < b^2 := sq_pos_of_ne_zero hb
  nlinarith

/-- Pure positive graviton + decoupled zero spectator has no *kinetic*
negative direction, but is singular and needs constraint analysis. -/
theorem decoupled_zero_is_semidefinite
    {a x y : ℝ} (ha : 0 ≤ a) :
    0 ≤ kineticForm a 0 0 x y := by
  simp only [kineticForm, mul_zero, zero_mul, add_zero]
  exact mul_nonneg ha (sq_nonneg _)

/-- The mixing threshold a*c=b² is a singular kinetic Hessian. -/
theorem threshold_det_zero {a b c : ℝ} (h : a*c=b^2) :
    determinant a b c = 0 := by
  unfold determinant
  linarith

end UBTMixedHessian
