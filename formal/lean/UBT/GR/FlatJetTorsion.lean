import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite cores for a restricted flat Lorentz jet with closed real dilation.
These do not formalize the differential geometry, the functional Noether
identity, a selected UBT action or the full complex-Theta dynamics.
-/

open scoped BigOperators

namespace UBT.GR.FlatJetTorsion

theorem coframe_cancellation (s c y dc dy : ℝ) (hs : s ≠ 0) (hc : c ≠ 0) :
    (s * dc * y + s * c * dy - dc / c * (s * c * y)) / s = c * dy := by
  field_simp [hs, hc]
  ring

theorem einstein_coefficient :
    6 * (-1 / 4 : ℝ) + 3 * (-1 / 2 : ℝ) + 9 * 1 = 6 := by
  norm_num

/-- Volume-weighted Ricci/torsion boundary cancellation after the geometric
contractions have been supplied by a separate calculation. -/
theorem boundary_core (c box gradientSquare : ℝ) :
    -6 * c * box = 6 * gradientSquare - 6 * (gradientSquare + c * box) := by
  ring

/-- An invertible field-value change cannot erase a stationary equation.
This is the finite chain-rule core, not a formal functional-variation theorem. -/
theorem chain_stationarity {I : Type*} [Fintype I]
    (a c scalarEuler : ℝ) (y vectorEuler : I → ℝ)
    (ha : a ≠ 0) (hc : c ≠ 0)
    (hx : ∀ i, a * vectorEuler i = 0)
    (hf : (∑ i, y i * vectorEuler i) - c * scalarEuler = 0) :
    (∀ i, vectorEuler i = 0) ∧ scalarEuler = 0 := by
  have hv : ∀ i, vectorEuler i = 0 := by
    intro i
    exact (mul_eq_zero.mp (hx i)).resolve_left ha
  have hz : (∑ i, y i * vectorEuler i) = 0 := by simp [hv]
  rw [hz, zero_sub] at hf
  have hp : c * scalarEuler = 0 := neg_eq_zero.mp hf
  exact ⟨hv, (mul_eq_zero.mp hp).resolve_left hc⟩

theorem legendre_energy (a v p gradientSquare : ℝ) (hp : p = -2 * a * v) :
    p * v - a * (-v ^ 2 + gradientSquare) = -a * (v ^ 2 + gradientSquare) := by
  rw [hp]
  ring

theorem negative_kinetic_energy (a p : ℝ) (ha : 0 < a) (hp : p ≠ 0) :
    -(p ^ 2 / (4 * a)) < 0 := by
  have hs : 0 < p ^ 2 := sq_pos_of_ne_zero hp
  have hd : 0 < 4 * a := by linarith
  have hq : 0 < p ^ 2 / (4 * a) := div_pos hs hd
  linarith

theorem nonEinstein_witness (lambda : ℝ)
    (ht : (3 / 4 : ℝ) = lambda * (-4))
    (hx : (1 / 4 : ℝ) = lambda * 4) : False := by
  linarith

end UBT.GR.FlatJetTorsion
