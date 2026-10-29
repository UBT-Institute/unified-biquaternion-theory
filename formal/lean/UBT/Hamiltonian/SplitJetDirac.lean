import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring

/-!
Finite cores for the conditional gravity-only split-jet parent reduction.
The noncommutative ring can itself be a finite matrix ring. Functional
Poisson brackets, the Palatini base reduction and full UBT are not formalized.
-/

namespace UBT.Hamiltonian.SplitJetDirac

def blockMul {R : Type*} [Ring R] (a b : (R × R) × (R × R)) :
    (R × R) × (R × R) :=
  ((a.1.1 * b.1.1 + a.1.2 * b.2.1,
    a.1.1 * b.1.2 + a.1.2 * b.2.2),
   (a.2.1 * b.1.1 + a.2.2 * b.2.1,
    a.2.1 * b.1.2 + a.2.2 * b.2.2))

def graphBlock {R : Type*} [Ring R] (k : R) : (R × R) × (R × R) :=
  ((0, -1), (1, k))

def graphInverse {R : Type*} [Ring R] (k : R) : (R × R) × (R × R) :=
  ((k, 1), (-1, 0))

theorem graph_inverse_right {R : Type*} [Ring R] (k : R) :
    blockMul (graphBlock k) (graphInverse k) = ((1, 0), (0, 1)) := by
  simp [blockMul, graphBlock, graphInverse]

theorem graph_inverse_left {R : Type*} [Ring R] (k : R) :
    blockMul (graphInverse k) (graphBlock k) = ((1, 0), (0, 1)) := by
  simp [blockMul, graphBlock, graphInverse]

/-- The graph-graph block of the inverse is zero, so observables independent
of the eliminated auxiliary pair receive no Dirac correction. -/
theorem zero_graph_correction {R : Type*} [Ring R] (k u v : R) :
    (0 * k + u * (-1)) * 0 + (0 * 1 + u * 0) * v = 0 := by
  simp

/-- Counts are supplied by the separate constraint analysis; this proves
only their dimension-independent arithmetic cancellation. -/
theorem no_extra_phase_dimension (d m k : ℤ) :
    2 * (d + (m + 1) * d + (m + 1) * d + (m + 1) * k)
      - (2 * d + 4 * m * d) - 2 * (2 * d + (m + 1) * k) = 0 := by
  ring

/-- The actual covariant derivative is additive only at fixed connection.
This algebraic result does not choose that connection dynamically. -/
theorem vertical_lift_invariant {V : Type*} [AddCommGroup V]
    (D : V →+ V) (x q e : V) :
    D (x + e) + (q - D e) = D x + q := by
  rw [map_add]
  abel

/-- Radial part of the field-dependent cotangent momentum shift. -/
theorem cotangent_radial_core (r a p t dx dq : ℝ) :
    p * dx + t * (dq / r - a * dx / r ^ 2) =
      (p - a * t / r ^ 2) * dx + (t / r) * dq := by
  ring

end UBT.Hamiltonian.SplitJetDirac
