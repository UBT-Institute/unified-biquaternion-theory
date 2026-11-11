import Mathlib

/-!
# Finite modular obstruction for two-square theta spectrum

The finite-ring theorem encodes an exact obstruction to
a putative two-mode energy level n = a²+b² when n≡3 mod4.
It does NOT prove Fermat's sufficiency for primes ≡1 mod4,
the general Jacobi representation count, or any UBT physics.
-/

namespace UBTThetaPrimeResidues

/-- Every square in Z/4Z is 0 or 1. -/
theorem squares_mod_four (x : ZMod 4) :
    x ^ 2 = 0 ∨ x ^ 2 = 1 := by
  fin_cases x <;> decide

/-- Two integer square classes cannot add to 3 modulo 4. -/
theorem no_three_mod_four_two_squares (x y : ZMod 4) :
    x ^ 2 + y ^ 2 ≠ 3 := by
  fin_cases x <;> fin_cases y <;> decide

/-- In particular the residue 3 itself has no two-square representation. -/
theorem three_unrepresentable :
    ¬ ∃ x y : ZMod 4, x ^ 2 + y ^ 2 = 3 := by
  intro h
  obtain ⟨x,y,hxy⟩ := h
  exact (no_three_mod_four_two_squares x y) hxy

/-- A residue of 1 is possible (so the obstruction is selective). -/
theorem one_representable :
    ∃ x y : ZMod 4, x ^ 2 + y ^ 2 = 1 := by
  refine ⟨1,0,?_⟩
  decide

end UBTThetaPrimeResidues
