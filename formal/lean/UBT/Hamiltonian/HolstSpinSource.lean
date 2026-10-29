import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Sourced Holst comparator and a bulk coefficient degeneracy

These are finite algebraic identities for a declared fixed-tetrad effective
comparator.  The 24-component exterior-form variation is checked separately
in CAS.  Neither an intrinsic UBT spin current nor a microscopic action,
physical mode spectrum, functional variation, or boundary theorem is assumed
to have been derived here.
-/

noncomputable section

namespace UBT.Hamiltonian.HolstSpinSource

def effective (b zeta : ℝ) : ℝ := b + zeta

def axial (k beta j : ℝ) : ℝ := -k * j / (6 * (1 + beta ^ 2))

def traceVector (k beta j : ℝ) : ℝ := k * beta * j / (6 * (1 + beta ^ 2))

def density (k beta j a v : ℝ) : ℝ :=
  3 / k * (a ^ 2 - v ^ 2 - 2 * beta * a * v) + j * a

theorem denominator_pos (beta : ℝ) : 0 < 1 + beta ^ 2 := by positivity

theorem effective_shift (b zeta shift : ℝ) :
    effective (b + shift) (zeta - shift) = effective b zeta := by
  dsimp [effective]
  ring

/-- Multiplied-through scalar Cartan equations.  The physical interpretation
requires k>0 and the separately stated source and boundary assumptions. -/
theorem sourced_stationarity (k beta j : ℝ) :
    6 * (axial k beta j - beta * traceVector k beta j) + k * j = 0 ∧
    traceVector k beta j + beta * axial k beta j = 0 := by
  have h : (1 + beta ^ 2) ≠ 0 := ne_of_gt (denominator_pos beta)
  constructor <;> dsimp [axial, traceVector] <;> field_simp <;> ring

theorem on_shell_contact (k beta j : ℝ) (hk : k ≠ 0) :
    density k beta j (axial k beta j) (traceVector k beta j) =
      -k * j ^ 2 / (12 * (1 + beta ^ 2)) := by
  have h : (1 + beta ^ 2) ≠ 0 := ne_of_gt (denominator_pos beta)
  dsimp [density, axial, traceVector]
  field_simp
  ring

theorem response_shift (k b zeta shift j : ℝ) :
    (axial k (effective (b + shift) (zeta - shift)) j,
      traceVector k (effective (b + shift) (zeta - shift)) j) =
    (axial k (effective b zeta) j, traceVector k (effective b zeta) j) := by
  rw [effective_shift]

theorem trace_axial_relation (k beta j : ℝ) :
    traceVector k beta j = -beta * axial k beta j := by
  dsimp [traceVector, axial]
  ring

theorem contact_sign_degeneracy (k beta j : ℝ) :
    -k * j ^ 2 / (12 * (1 + (-beta) ^ 2)) =
      -k * j ^ 2 / (12 * (1 + beta ^ 2)) := by
  simp only [neg_sq]

end UBT.Hamiltonian.HolstSpinSource
