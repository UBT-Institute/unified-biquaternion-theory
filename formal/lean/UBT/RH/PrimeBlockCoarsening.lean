import UBT.RH.PrimePairing
import UBT.RH.SubsetCancellation
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-! Coarsening actual Mobius prime-support blocks contracts their absolute mass.
All cutoffs are arbitrary. No asymptotic contraction rate is assumed. -/
namespace UBT.RH.PrimeBlockCoarsening
open Finset
open scoped ArithmeticFunction.Moebius

section Grouping
variable {α β γ : Type*} [DecidableEq α] [DecidableEq β] [DecidableEq γ]

def block (s : Finset α) (f : α → β) (w : α → ℤ) (b : β) : ℤ :=
  ∑ x ∈ s.filter (fun x => f x = b), w x

def mass (s : Finset α) (f : α → β) (w : α → ℤ) : ℤ :=
  ∑ b ∈ s.image f, |block s f w b|

theorem block_total (s : Finset α) (f : α → β) (w : α → ℤ) :
    (∑ b ∈ s.image f, block s f w b) = ∑ x ∈ s, w x := by
  exact sum_fiberwise_of_maps_to (fun x hx => mem_image_of_mem f hx) w

theorem total_le_mass (s : Finset α) (f : α → β) (w : α → ℤ) :
    |∑ x ∈ s, w x| ≤ mass s f w := by
  rw [← block_total s f w]
  exact abs_sum_le_sum_abs _ _

theorem block_comp (s : Finset α) (f : α → β) (g : β → γ)
    (w : α → ℤ) (c : γ) :
    block s (fun x => g (f x)) w c =
      ∑ b ∈ (s.image f).filter (fun b => g b = c), block s f w b := by
  unfold block
  rw [sum_fiberwise_eq_sum_filter]
  apply sum_congr
  · ext x
    simp only [mem_filter]
    constructor
    · intro h
      exact ⟨h.1, mem_image_of_mem f h.1, h.2⟩
    · intro h
      exact ⟨h.1, h.2.2⟩
  · intro x hx
    rfl

/-- Merging disjoint blocks cannot increase the sum of absolute block sums. -/
theorem mass_comp_le (s : Finset α) (f : α → β) (g : β → γ) (w : α → ℤ) :
    mass s (fun x => g (f x)) w ≤ mass s f w := by
  unfold mass
  rw [← image_image]
  simp_rw [block_comp]
  calc
    _ ≤ ∑ c ∈ (s.image f).image g,
        ∑ b ∈ (s.image f).filter (fun b => g b = c), |block s f w b| := by
      apply sum_le_sum
      intro c hc
      exact abs_sum_le_sum_abs _ _
    _ = _ := sum_fiberwise_of_maps_to
      (fun b hb => mem_image_of_mem g hb) (fun b => |block s f w b|)

theorem mass_of_constant (s : Finset α) (hs : s.Nonempty) (f : α → β)
    (w : α → ℤ) (c : β) (hf : ∀ x ∈ s, f x = c) :
    mass s f w = |∑ x ∈ s, w x| := by
  have hi : s.image f = {c} := by
    ext b
    simp only [mem_image, mem_singleton]
    constructor
    · rintro ⟨x, hx, rfl⟩
      exact hf x hx
    · intro hb
      obtain ⟨x, hx⟩ := hs
      exact ⟨x, hx, (hf x hx).trans hb.symm⟩
  have hfilter : s.filter (fun x => f x = c) = s := by
    ext x
    simp only [mem_filter]
    exact ⟨And.left, fun hx => ⟨hx, hf x hx⟩⟩
  simp [mass, hi, block, hfilter]
end Grouping

/-- Prime factors outside the selected finite set label the disjoint blocks.
Nonsquarefree inputs have zero Mobius weight and do not affect the sums. -/
def core (P : Finset ℕ) (n : ℕ) : Finset ℕ := n.primeFactors \ P

noncomputable def remainder (P : Finset ℕ) (N : ℕ) : ℤ :=
  mass (range (N + 1)) (core P) (fun n => μ n)

theorem core_coarsen (P Q : Finset ℕ) (hPQ : P ⊆ Q) (n : ℕ) :
    core Q n = core P n \ Q := by
  ext p
  simp only [core, mem_sdiff]
  constructor
  · intro h
    exact ⟨⟨h.1, fun hp => h.2 (hPQ hp)⟩, h.2⟩
  · intro h
    exact ⟨h.1.1, h.2⟩

/-- Actual arithmetic Mobius remainder, for every N and every nested selection. -/
theorem remainder_antitone (P Q : Finset ℕ) (hPQ : P ⊆ Q) (N : ℕ) :
    remainder Q N ≤ remainder P N := by
  have hf : core Q = fun n => core P n \ Q := by
    funext n
    exact core_coarsen P Q hPQ n
  unfold remainder
  rw [hf]
  exact mass_comp_le _ _ (fun S => S \ Q) _

theorem remainder_insert_le (P : Finset ℕ) (p N : ℕ) :
    remainder (insert p P) N ≤ remainder P N :=
  remainder_antitone P (insert p P) (subset_insert p P) N

theorem mertens_le_remainder (P : Finset ℕ) (N : ℕ) :
    |PrimePairing.mertens N| ≤ remainder P N :=
  total_le_mass _ _ _

/-- Selecting all prime factors of the interval leaves exactly |M(N)|.
This identity supplies no upper bound on that quantity. -/
theorem remainder_terminal (P : Finset ℕ) (N : ℕ)
    (hP : ∀ n ∈ range (N + 1), n.primeFactors ⊆ P) :
    remainder P N = |PrimePairing.mertens N| := by
  apply mass_of_constant _ ⟨0, mem_range.mpr (Nat.zero_lt_succ N)⟩ _ _ ∅
  intro n hn
  exact sdiff_eq_empty_iff_subset.mpr (hP n hn)

/-- Local gain when the two pre-toggle cutoff sums have the same sign. -/
theorem same_sign_gain (a b : ℤ) (h : 0 ≤ a * b) :
    |a| + |b| - |a - b| = 2 * min |a| |b| := by
  rcases le_total 0 a with ha | ha <;> rcases le_total 0 b with hb | hb
  · rw [abs_of_nonneg ha, abs_of_nonneg hb]
    rcases le_total a b with hab | hab
    · rw [min_eq_left hab, abs_of_nonpos (by omega : a - b ≤ 0)]
      omega
    · rw [min_eq_right hab, abs_of_nonneg (by omega : 0 ≤ a - b)]
      omega
  · have hz : a = 0 ∨ b = 0 := by
      by_contra hz
      push_neg at hz
      nlinarith
    rcases hz with rfl | rfl <;> simp
  · have hz : a = 0 ∨ b = 0 := by
      by_contra hz
      push_neg at hz
      nlinarith
    rcases hz with rfl | rfl <;> simp
  · rw [abs_of_nonpos ha, abs_of_nonpos hb]
    rcases le_total (-a) (-b) with hab | hab
    · rw [min_eq_left hab, abs_of_nonneg (by omega : 0 ≤ a - b)]
      omega
    · rw [min_eq_right hab, abs_of_nonpos (by omega : a - b ≤ 0)]
      omega

end UBT.RH.PrimeBlockCoarsening
