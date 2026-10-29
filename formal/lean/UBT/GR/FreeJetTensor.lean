import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite algebraic cores for the principal tensor block of a declared timelike
free-jet torsion family. Differential geometry, the principal-order reduction,
complete field constraints and microscopic action selection are not formalized.
-/

open scoped BigOperators

namespace UBT.GR.FreeJetTensor

def auxiliaryQ (a b c d e f g h i : ℝ) : ℝ :=
  2 * (h * d - i * a + b * f - c * e + c * g - e * g)

theorem einstein_coefficient :
    2 * (-1 / 4 : ℝ) + (-1 / 2 : ℝ) = -1 := by
  norm_num

/-- The supplied quadratic torsion contraction can be translated to a form
with no spatial tensor derivative. The contraction itself is checked by CAS. -/
theorem einstein_recenter (u v p q a b c d e f g h i : ℝ) :
    (u ^ 2 + v ^ 2 - p ^ 2 - q ^ 2) / 2 + p * (b - f) + q * (c + e)
      + auxiliaryQ a b c d e f g h i =
    (u ^ 2 + v ^ 2) / 2
      + auxiliaryQ a (b - p / 2) (c - q / 2) d (e - q / 2) (f + p / 2) g h i := by
  unfold auxiliaryQ
  ring

/-- Linear Euler equations of the nine-variable polynomial force its unique
stationary point. No continuum connection equation is assumed formalized. -/
theorem auxiliary_stationarity (a b c d e f g h i : ℝ)
    (ha : -2 * i = 0) (hb : 2 * f = 0) (hc : 2 * (-e + g) = 0)
    (hd : 2 * h = 0) (he : 2 * (-c - g) = 0) (hf : 2 * b = 0)
    (hg : 2 * (c - e) = 0) (hh : 2 * d = 0) (hi : -2 * a = 0) :
    a = 0 ∧ b = 0 ∧ c = 0 ∧ d = 0 ∧ e = 0 ∧ f = 0 ∧ g = 0 ∧ h = 0 ∧ i = 0 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> linarith

/-- Even a singular homogeneous quadratic auxiliary form has zero value at
each stationary vector, given its matrix Euler equations. -/
theorem stationary_quadratic_value {I : Type*} [Fintype I]
    (matrix : I → I → ℝ) (y : I → ℝ)
    (hy : ∀ i, (∑ j, matrix i j * y j) = 0) :
    (∑ i, y i * (∑ j, matrix i j * y j)) / 2 = 0 := by
  simp [hy]

/-- At zero torsion the complete first variation of a bilinear torsion action
vanishes, including changes of the metric/volume contraction matrix. -/
theorem zero_torsion_first_variation {I : Type*} [Fintype I]
    (matrix deltaMatrix : I → I → ℝ) (t deltaT : I → ℝ)
    (ht : ∀ i, t i = 0) :
    (∑ i, ∑ j, deltaMatrix i j * t i * t j
      + matrix i j * (deltaT i * t j + t i * deltaT j)) = 0 := by
  simp [ht]

theorem tensor_legendre (a v p : ℝ) (hp : p = 2 * a * v) :
    p * v - a * v ^ 2 = a * v ^ 2 := by
  rw [hp]
  ring

theorem einstein_time_positive (kappa : ℝ) (hk : 0 < kappa) :
    0 < 1 / (4 * kappa) := by
  exact div_pos (by norm_num) (by linarith)

end UBT.GR.FreeJetTensor
