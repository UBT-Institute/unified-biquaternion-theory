import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
Finite algebraic cores of a CONDITIONAL spatial-metric Hamiltonian selector.
No functional Poisson bracket, UBT reduction, microscopic action selection,
or full physical mode theorem is formalized by this module.
-/

namespace UBT.Hamiltonian.SpatialClosure

/-- The two independent local tensor coefficients after integration by parts.
The derivation of this expression is analytic/CAS, not a premise-free result
about the full UBT field equations. -/
def bracketDefect (a b chi divergence traceGradient : ℝ) : ℝ :=
  (a * b - 1) * divergence +
    2 * a * b * (1 - 2 * chi) * traceGradient

theorem coefficient_selection (a b chi : ℝ) :
    (∀ d t : ℝ, bracketDefect a b chi d t = 0) ↔
      a * b = 1 ∧ chi = (1 / 2 : ℝ) := by
  constructor
  · intro h
    have hd := h 1 0
    have ht := h 0 1
    simp only [bracketDefect, mul_one, mul_zero, zero_add, add_zero] at hd ht
    have hab : a * b = 1 := by linarith
    have ht' : 2 * (1 - 2 * chi) = 0 := by
      calc
        2 * (1 - 2 * chi) = 2 * (a * b) * (1 - 2 * chi) := by simp [hab]
        _ = 2 * a * b * (1 - 2 * chi) := by ring
        _ = 0 := ht
    have hchi : chi = (1 / 2 : ℝ) := by linarith
    exact ⟨hab, hchi⟩
  · rintro ⟨hab, rfl⟩ d t
    simp [bracketDefect, hab]

/-- Trace contraction in three spatial dimensions. -/
theorem curvature_contraction (chi p q r : ℝ) :
    r - chi * p * q - (p - 3 * chi * p) * q =
      r - (1 - 2 * chi) * p * q := by
  ring

/-- At the selected trace coefficient the Legendre quadratic form agrees
with K_ij K^ij - K^2, after its norm/trace contractions are supplied. -/
theorem dewitt_inverse_core (a normP traceP : ℝ) :
    a ^ 2 * (normP - traceP ^ 2 / 4) - (a * traceP / 2) ^ 2 =
      a ^ 2 * (normP - traceP ^ 2 / 2) := by
  ring

theorem tt_wave_coefficient (a b lap : ℝ) :
    2 * a * (b / 2 * lap) = a * b * lap := by
  ring

theorem selected_tt_wave (a b lap : ℝ) (hab : a * b = 1) :
    2 * a * (b / 2 * lap) = lap := by
  rw [tt_wave_coefficient, hab, one_mul]

theorem tt_energy_nonnegative (a b momentumSquare gradientSquare : ℝ)
    (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hp : 0 ≤ momentumSquare) (hg : 0 ≤ gradientSquare) :
    0 ≤ a * momentumSquare + b / 4 * gradientSquare := by
  exact add_nonneg (mul_nonneg ha hp) (mul_nonneg (by linarith) hg)

end UBT.Hamiltonian.SpatialClosure
