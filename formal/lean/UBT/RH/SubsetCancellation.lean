import UBT.RH.MobiusAbel
import Mathlib.Algebra.BigOperators.Group.Finset.Powerset

/-! Exact subset-parity cancellation and its cutoff recurrence.
These combinatorial statements do not supply an asymptotic Mobius bound. -/
namespace UBT.RH.SubsetCancellation
open Finset

def cubeSum (P : Finset ℕ) (F : ℕ → ℤ) : ℤ :=
  ∑ S ∈ P.powerset, (-1 : ℤ) ^ S.card * F (∏ p ∈ S, p)

def cutoff (P : Finset ℕ) (N : ℕ) : ℤ :=
  cubeSum P (fun d => if d ≤ N then 1 else 0)

theorem subset_count (P : Finset ℕ) : P.powerset.card = 2 ^ P.card :=
  card_powerset P

/-- Insertion pairs each subset with the subset containing the new element. -/
theorem cube_insert (P : Finset ℕ) (p : ℕ) (hp : p ∉ P) (F : ℕ → ℤ) :
    cubeSum (insert p P) F = cubeSum P F - cubeSum P (fun d => F (p * d)) := by
  unfold cubeSum
  rw [sum_powerset_insert hp]
  have h : (∑ S ∈ P.powerset, (-1 : ℤ) ^ (insert p S).card *
      F (∏ q ∈ insert p S, q)) =
      -(∑ S ∈ P.powerset, (-1 : ℤ) ^ S.card * F (p * ∏ q ∈ S, q)) := by
    rw [← sum_neg_distrib]
    apply sum_congr rfl
    intro S hS
    have hn : p ∉ S := fun hs => hp ((mem_powerset.mp hS) hs)
    rw [card_insert_of_notMem hn, prod_insert hn, pow_succ]
    ring
  rw [h]
  ring

/-- Every nonempty full cube has equal even and odd subset counts. -/
theorem full_cube_cancel (P : Finset ℕ) (hP : P.Nonempty) :
    cubeSum P (fun _ => 1) = 0 := by
  obtain ⟨p, hp⟩ := hP
  have he : insert p (P.erase p) = P := insert_erase hp
  rw [← he, cube_insert _ _ (notMem_erase p P)]
  exact sub_self _

/-- The product cutoff retains the difference of two scales. -/
theorem cutoff_insert (P : Finset ℕ) (p N : ℕ) (hp : p ∉ P) (hpos : 0 < p) :
    cutoff (insert p P) N = cutoff P N - cutoff P (N / p) := by
  have hF : (fun d : ℕ => if p * d ≤ N then (1 : ℤ) else 0) =
      (fun d : ℕ => if d ≤ N / p then (1 : ℤ) else 0) := by
    funext d
    simp only [Nat.le_div_iff_mul_le hpos, mul_comm]
  unfold cutoff
  rw [cube_insert P p hp, hF]

end UBT.RH.SubsetCancellation
