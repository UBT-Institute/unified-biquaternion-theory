import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
Finite cores for a local nonlinear Cartan comparison chart.
No canonical UBT metric, phase symmetry, selected action or physical mode
claim is supplied. The covariance-rank and Lie-field calculations are
independently encoded in CAS, not formalized by these lemmas.
-/

namespace UBT.GR.NonlinearCartanChart

theorem derived_norm (q phi ell : ℝ) (h : phi ^ 2 = ell ^ 2 - q) :
    q + phi ^ 2 = ell ^ 2 := by
  linarith

theorem tangent_lift (h phi : ℝ) (hp : phi ≠ 0) :
    h + phi * (-h / phi) = 0 := by
  field_simp [hp]
  ring

/-- Quotient-rule cancellation after the stated vector-field derivatives
have been computed. It is not a formalization of that differential step. -/
theorem quotient_derivative_core (phi h u v : ℝ) (hp : phi ≠ 0) :
    (-phi * v + h * u / phi) / phi - h * u / phi ^ 2 = -v := by
  field_simp [hp]
  ring

def coordinatePack {X Y U V : Type*} (f : X → U) (g : X → Y → V)
    (p : X × Y) : (X × U) × (Y × V) :=
  ((p.1, f p.1), (p.2, g p.1 p.2))

/-- Adding derived coordinates to both parts loses neither part.
For the actual chart the added functions are phi(X) and -<X,Y>/phi(X). -/
theorem coordinatePack_injective {X Y U V : Type*} (f : X → U) (g : X → Y → V) :
    Function.Injective (coordinatePack f g) := by
  intro a b h
  apply Prod.ext
  · exact congrArg (fun z : (X × U) × (Y × V) => z.1.1) h
  · exact congrArg (fun z : (X × U) × (Y × V) => z.2.1) h

end UBT.GR.NonlinearCartanChart
