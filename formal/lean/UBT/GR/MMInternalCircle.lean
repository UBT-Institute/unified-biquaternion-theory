import Lean

namespace UBT.GR.MMInternalCircle

variable {α : Type} [Zero α]

/-- Multiplication on the left by the boost exchanging entries 0 and i. -/
def leftBoost (x : Fin 5 → Fin 5 → α) (i row col : Fin 5) : α :=
  if row = 0 then x i col else if row = i then x 0 col else 0

/-- Multiplication on the right by the same boost. -/
def rightBoost (x : Fin 5 → Fin 5 → α) (i row col : Fin 5) : α :=
  if col = 0 then x row i else if col = i then x row 0 else 0

private theorem finFiveCases (i : Fin 5) :
    i = 0 ∨ i = 1 ∨ i = 2 ∨ i = 3 ∨ i = 4 := by
  omega

/-- The three Lorentz boosts have trivial joint centralizer on zero-diagonal
matrices in five dimensions. The two MM real forms and their complexification
have zero diagonal in an orthogonal basis. -/
theorem lorentzBoostCentralizer_eq_zero (x : Fin 5 → Fin 5 → α)
    (diagonal : ∀ i, x i i = 0)
    (comm1 : ∀ row col, leftBoost x 1 row col = rightBoost x 1 row col)
    (comm2 : ∀ row col, leftBoost x 2 row col = rightBoost x 2 row col)
    (comm3 : ∀ row col, leftBoost x 3 row col = rightBoost x 3 row col) :
    x = fun _ _ => 0 := by
  have rowZero (col : Fin 5) (nonzero : col ≠ 0) : x 0 col = 0 := by
    by_cases first : col = 1
    · subst col
      simpa [leftBoost, rightBoost] using comm2 2 1
    · simpa [leftBoost, rightBoost, nonzero, first] using comm1 1 col
  have colZero (row : Fin 5) (nonzero : row ≠ 0) : x row 0 = 0 := by
    by_cases first : row = 1
    · subst row
      simpa [leftBoost, rightBoost] using (comm2 1 2).symm
    · simpa [leftBoost, rightBoost, nonzero, first] using (comm1 row 1).symm
  have spatialRow (i : Fin 5)
      (commutes : ∀ row col, leftBoost x i row col = rightBoost x i row col)
      (col : Fin 5) (nonzero : col ≠ 0) (distinct : col ≠ i) : x i col = 0 := by
    simpa [leftBoost, rightBoost, nonzero, distinct] using commutes 0 col
  funext row col
  by_cases same : row = col
  · subst col
    exact diagonal row
  by_cases colIsZero : col = 0
  · subst col
    exact colZero row same
  rcases finFiveCases row with rfl | rfl | rfl | rfl | rfl
  · exact rowZero col colIsZero
  · exact spatialRow 1 comm1 col colIsZero (Ne.symm same)
  · exact spatialRow 2 comm2 col colIsZero (Ne.symm same)
  · exact spatialRow 3 comm3 col colIsZero (Ne.symm same)
  · rcases finFiveCases col with rfl | rfl | rfl | rfl | rfl
    · exact (colIsZero rfl).elim
    · simpa [leftBoost, rightBoost] using (comm1 4 0).symm
    · simpa [leftBoost, rightBoost] using (comm2 4 0).symm
    · simpa [leftBoost, rightBoost] using (comm3 4 0).symm
    · exact (same rfl).elim

end UBT.GR.MMInternalCircle
