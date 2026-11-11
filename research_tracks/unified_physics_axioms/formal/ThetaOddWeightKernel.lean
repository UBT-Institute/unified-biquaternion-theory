import Mathlib

/-!
# Theta quadratic exponent: finite odd-weight combinatorial kernel

The full Jacobi triple-product identity and any proposed UBT energy
functional are NOT proved here. We prove the exact finite sum identity
which shows why multiplying factors with consecutive odd exponents
can yield a q^(n^2) weight.
-/

namespace UBTThetaEnergy

/-- The sum of the first n positive odd natural numbers is n². -/
theorem odd_weights_sum_to_square (n : ℕ) :
    (∑ k ∈ Finset.range n, (2 * k + 1)) = n ^ 2 := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [Finset.sum_range_succ, ih]
      ring

/-- The weight produced by choosing consecutive odd-weight factors
agrees with the quadratic mode weight q^(n²). -/
theorem mode_weight_from_odd_factors (q : ℝ) (n : ℕ) :
    q ^ (∑ k ∈ Finset.range n, (2 * k + 1)) = q ^ (n ^ 2) := by
  rw [odd_weights_sum_to_square]

/-- Concretely, four successive odd levels have total weight 16. -/
theorem first_four_levels : (∑ k ∈ Finset.range 4, (2*k+1)) = 16 := by
  norm_num

end UBTThetaEnergy
