import Mathlib

/-!
# Full off-diagonal 2-by-2 biquaternion energy: real-subcase proof kernel

The complex matrix formulas and Lorentz interpretation are checked by
independent symbolic tests, not formalized in this Lean file. This
restricted real subcase proves that positive Hilbert-Schmidt size
cannot be identified with the indefinite trace-adjugate pairing.
-/

namespace UBTOffDiagonalEnergy

def positivePairing (a b c d : ℝ) : ℝ :=
  a^2 + b^2 + c^2 + d^2

def adjugatePairing (a b c d : ℝ) : ℝ :=
  2 * (a*d - b*c)

theorem positivePairing_nonneg (a b c d : ℝ) :
    0 ≤ positivePairing a b c d := by
  unfold positivePairing
  positivity

/-- A matrix with strong off-diagonal coupling has a negative
    adjugate pairing even though the HS pairing is positive. -/
theorem negative_offdiagonal_example :
    adjugatePairing 1 2 2 1 = -6 ∧
      positivePairing 1 2 2 1 = 10 := by
  norm_num [adjugatePairing, positivePairing]

/-- An off-diagonal shear preserves determinant/adjugate pairing. -/
theorem shear_adjugate_constant (t : ℝ) :
    adjugatePairing 1 t 0 1 = 2 := by
  simp [adjugatePairing]

theorem shear_positive_pairing (t : ℝ) :
    positivePairing 1 t 0 1 = 2 + t^2 := by
  ring

/-- Positive HS pairing is strictly changed by every nonzero shear. -/
theorem shear_hs_not_invariant (t : ℝ) (ht : t ≠ 0) :
    2 < positivePairing 1 t 0 1 := by
  rw [shear_positive_pairing]
  have hsq : 0 < t^2 := sq_pos_of_ne_zero ht
  linarith

end UBTOffDiagonalEnergy
