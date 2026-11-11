import Mathlib
import ThetaTwoSquaresPrimeResidues

/-!
# Prime pattern is not invariant under changing the positive mode energy.

Two different positive integral quadratic forms, a²+b² and a²+2b²,
have different representations at the same energy level.
The independent four-square witness shows that increasing mode number
also changes the exclusion. These are finite exact facts, not
a proof of UBT dynamics or a general theta transformation identity.
-/

namespace UBTThetaPrimeRobustness

/-- Identity quadratic form excludes class 3 modulo 4. -/
theorem ordinary_two_mode_exclusion (a b : ZMod 4) :
    a ^ 2 + b ^ 2 ≠ 3 :=
  UBTThetaPrimeResidues.no_three_mod_four_two_squares a b

/-- A positive diagonal quadratic form with weights 1,2 admits 3. -/
theorem weighted_level_three :
    (1 : ℕ) ^ 2 + 2 * (1 : ℕ) ^ 2 = 3 := by
  norm_num

/-- Both prime levels occur in the altered weighted two-mode spectrum. -/
theorem weighted_level_137 :
    (3 : ℕ) ^ 2 + 2 * (8 : ℕ) ^ 2 = 137 := by
  norm_num

theorem weighted_level_139 :
    (11 : ℕ) ^ 2 + 2 * (3 : ℕ) ^ 2 = 139 := by
  norm_num

/-- An extra pair of modes removes the two-square obstruction for 139. -/
theorem four_mode_level_139 :
    (11 : ℕ) ^ 2 + (3 : ℕ) ^ 2 + (3 : ℕ) ^ 2 + (0 : ℕ) ^ 2 = 139 := by
  norm_num

end UBTThetaPrimeRobustness
