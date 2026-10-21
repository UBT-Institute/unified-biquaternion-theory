import UBT.RH.HallBudget
import UBT.RH.ConcreteExchange

/-! The Hall budget includes the global Mobius imbalance already.
This audit does not prove the missing arithmetic estimate or RH. -/
namespace UBT.RH.HallObstruction
open Finset
open UBT.RH.HallBudget

/-- The full source set is one of the subsets required by Hall's condition. -/
theorem card_bound_of_hall (A B : Finset ℕ) (t : A → Finset ℕ) (d : ℕ)
    (ht : ∀ a, t a ⊆ B)
    (h : ∀ s : Finset A, s.card ≤ (s.biUnion t).card + d) :
    A.card ≤ B.card + d := by
  have hs : (univ : Finset A).biUnion t ⊆ B := by
    intro b hb
    obtain ⟨a, ha, hab⟩ := mem_biUnion.mp hb
    exact ht a hab
  have hc := (h univ).trans (Nat.add_le_add_right (card_le_card hs) d)
  simpa using hc

/-- Complete opposite-sign adjacency, with no arithmetic restriction. -/
def CompleteHall (A B : Finset ℕ) (d : ℕ) : Prop :=
  ∀ s : Finset A, s.card ≤ (s.biUnion (fun _ => B)).card + d

theorem complete_hall_iff_card (A B : Finset ℕ) (d : ℕ) :
    CompleteHall A B d ↔ A.card ≤ B.card + d := by
  constructor
  · exact card_bound_of_hall A B (fun _ => B) d (fun _ => subset_refl B)
  · intro h s
    by_cases hs : s.Nonempty
    · have he : s.biUnion (fun _ => B) = B := by
        ext b
        simp only [mem_biUnion]
        constructor
        · rintro ⟨a, ha, hb⟩
          exact hb
        · intro hb
          obtain ⟨a, ha⟩ := hs
          exact ⟨a, ha, hb⟩
      rw [he]
      have hc : s.card ≤ A.card := by simpa using (card_le_univ s)
      exact hc.trans h
    · have he : s = ∅ := not_nonempty_iff_eq_empty.mp hs
      simp [he]

theorem actual_mertens_counts (N : ℕ) :
    PrimePairing.mertens N = ((positive N).card : ℤ) - (negative N).card := by
  simpa only [ConcreteExchange.positive_eq, ConcreteExchange.negative_eq,
    positive, negative] using ConcreteExchange.mertens_counts N

/-- Even with every edge allowed, the two-sided budget is exactly |M(N)| ≤ d. -/
theorem complete_both_iff_mertens (N d : ℕ) :
    (CompleteHall (negative N) (positive N) d ∧
      CompleteHall (positive N) (negative N) d) ↔
      |PrimePairing.mertens N| ≤ (d : ℤ) := by
  rw [complete_hall_iff_card, complete_hall_iff_card, actual_mertens_counts, abs_le]
  omega

/-- Restricted arithmetic neighborhoods cannot evade the global imbalance. -/
theorem restricted_both_imply_mertens (N d : ℕ)
    (tn : negative N → Finset ℕ) (tp : positive N → Finset ℕ)
    (hn : ∀ n, tn n ⊆ positive N) (hp : ∀ p, tp p ⊆ negative N)
    (hhn : ∀ s : Finset (negative N), s.card ≤ (s.biUnion tn).card + d)
    (hhp : ∀ s : Finset (positive N), s.card ≤ (s.biUnion tp).card + d) :
    |PrimePairing.mertens N| ≤ (d : ℤ) := by
  have h1 := card_bound_of_hall (negative N) (positive N) tn d hn hhn
  have h2 := card_bound_of_hall (positive N) (negative N) tp d hp hhp
  rw [actual_mertens_counts, abs_le]
  omega

end UBT.RH.HallObstruction
