import UBT.RH.MatchingCertificate
import Mathlib.Combinatorics.Hall.Finite

/-! Hall's theorem with a finite budget of unmatched vertices.
The arithmetic expansion hypothesis is explicit and is NOT proved here. -/
namespace UBT.RH.HallBudget
open Finset
open scoped ArithmeticFunction.Moebius

section Finite
variable {ι α : Type*} [Fintype ι] [DecidableEq α]

/-- Adding d distinct auxiliary targets converts a deficit bound into Hall's condition. -/
theorem hall_with_budget (t : ι → Finset α) (d : ℕ)
    (h : ∀ s : Finset ι, s.card ≤ (s.biUnion t).card + d) :
    ∃ f : ι → α ⊕ Fin d, Function.Injective f ∧
      (∀ i, f i ∈ (t i).disjSum (univ : Finset (Fin d))) ∧
      ((univ : Finset ι).filter (fun i => (f i).isRight)).card ≤ d := by
  classical
  let u : ι → Finset (α ⊕ Fin d) := fun i => (t i).disjSum univ
  have hu : ∀ s : Finset ι, s.card ≤ (s.biUnion u).card := by
    intro s
    by_cases hs : s.Nonempty
    · have he : s.biUnion u = (s.biUnion t).disjSum (univ : Finset (Fin d)) := by
        ext z
        cases z with
        | inl a => simp [u]
        | inr b => simp [u, hs]
      rw [he, card_disjSum]
      simpa using h s
    · have he : s = ∅ := not_nonempty_iff_eq_empty.mp hs
      simp [he]
  obtain ⟨f, hf, ht⟩ := (all_card_le_biUnion_card_iff_existsInjective' u).mp hu
  refine ⟨f, hf, ht, ?_⟩
  have hm : Set.MapsTo f
      (↑((univ : Finset ι).filter (fun i => (f i).isRight)))
      (↑((∅ : Finset α).disjSum (univ : Finset (Fin d)))) := by
    intro i hi
    have hr := (mem_filter.mp hi).2
    cases he : f i with
    | inl a => simp [he] at hr
    | inr b => simp
  have hc := card_le_card_of_injOn f hm hf.injOn
  simpa using hc

/-- The same subset deficit condition is necessary for an auxiliary-target injection. -/
theorem budget_necessary (t : ι → Finset α) (d : ℕ)
    (f : ι → α ⊕ Fin d) (hf : Function.Injective f)
    (ht : ∀ i, f i ∈ (t i).disjSum (univ : Finset (Fin d)))
    (s : Finset ι) : s.card ≤ (s.biUnion t).card + d := by
  classical
  have hm : Set.MapsTo f (↑s)
      (↑((s.biUnion t).disjSum (univ : Finset (Fin d)))) := by
    intro i hi
    have hh := ht i
    cases he : f i with
    | inl a =>
      have ha : a ∈ t i := by simpa [he] using hh
      simpa using (mem_biUnion.mpr ⟨i, hi, ha⟩ : a ∈ s.biUnion t)
    | inr b => simp
  have hc := card_le_card_of_injOn f hm hf.injOn
  simpa using hc
end Finite

noncomputable def positive (N : ℕ) : Finset ℕ :=
  (range (N + 1)).filter (fun n => μ n = 1)

noncomputable def negative (N : ℕ) : Finset ℕ :=
  (range (N + 1)).filter (fun n => μ n = -1)

/-- The relation E is an explicit choice of allowed arithmetic exchanges. -/
noncomputable def neighbors (N : ℕ) (E : ℕ → ℕ → Prop) (n : ℕ) : Finset ℕ := by
  classical
  exact (positive N).filter (fun m => E n m)

/-- Conditional global matching, specialized to actual Mobius sign classes.
No assumption about subset expansion is discharged by this theorem. -/
theorem mobius_matching_with_budget (N d : ℕ) (E : ℕ → ℕ → Prop)
    (h : ∀ s : Finset (negative N),
      s.card ≤ (s.biUnion (fun n => neighbors N E n.val)).card + d) :
    ∃ f : (negative N) → ℕ ⊕ Fin d, Function.Injective f ∧
      (∀ (n : negative N) (m : ℕ), f n = Sum.inl m →
        m ≤ N ∧ E n.val m ∧ μ n.val + μ m = 0) ∧
      ((univ : Finset (negative N)).filter (fun n => (f n).isRight)).card ≤ d := by
  classical
  obtain ⟨f, hf, ht, hd⟩ := hall_with_budget (fun n : negative N => neighbors N E n.val) d h
  refine ⟨f, hf, ?_, hd⟩
  intro n m hm
  have hh : m ∈ neighbors N E n.val := by simpa [hm] using ht n
  have he : m ∈ positive N ∧ E n.val m := mem_filter.mp hh
  have hp : m ∈ range (N + 1) ∧ μ m = 1 := mem_filter.mp he.1
  have hn : μ n.val = -1 := (mem_filter.mp n.property).2
  refine ⟨Nat.le_of_lt_succ (mem_range.mp hp.1), he.2, ?_⟩
  rw [hn, hp.2]
  norm_num

end UBT.RH.HallBudget
