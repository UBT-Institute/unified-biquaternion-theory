import UBT.RH.MobiusAbel
import Mathlib.Analysis.Normed.Group.InfiniteSum

/-! Conditional infinite Abel transfer and certified truncation error.
The original series is summed in natural order. No cancellation estimate for
the Möbius function, and no UBT action-level premise, is assumed proved here. -/

namespace UBT.RH.AbelLimit
open Filter
open scoped Topology
open UBT.RH.MobiusAbel

noncomputable def abelTerm (a w : ℕ → ℂ) (k : ℕ) : ℂ :=
  partialSum a (k + 1) * (w (k + 1) - w (k + 2))

/-- The transformed series is summable; the original is only claimed to
converge in its specified natural order. -/
theorem ordered_limit (a w : ℕ → ℂ)
    (hb : Tendsto (fun N => partialSum a N * w (N + 1)) atTop (𝓝 0))
    (ht : Summable (abelTerm a w)) :
    Tendsto (fun N => ∑ k ∈ Finset.range N, a (k + 1) * w (k + 1))
      atTop (𝓝 (∑' k, abelTerm a w k)) := by
  have h := hb.add ht.hasSum.tendsto_sum_nat
  simpa only [zero_add, abelTerm, ← finite_abel] using h

/-- A pointwise summable majorant suffices for the transformed terms. -/
theorem ordered_limit_of_majorant (a w : ℕ → ℂ) (g : ℕ → ℝ)
    (hb : Tendsto (fun N => partialSum a N * w (N + 1)) atTop (𝓝 0))
    (hg : Summable g) (hbound : ∀ k, ‖abelTerm a w k‖ ≤ g k) :
    Tendsto (fun N => ∑ k ∈ Finset.range N, a (k + 1) * w (k + 1))
      atTop (𝓝 (∑' k, abelTerm a w k)) :=
  ordered_limit a w hb (hg.of_norm_bounded hbound)

/-- Exact remainder before estimating its norm; no boundary limit needed. -/
theorem remainder_identity (a w : ℕ → ℂ) (N : ℕ)
    (ht : Summable (abelTerm a w)) :
    (∑ k ∈ Finset.range N, a (k + 1) * w (k + 1)) -
      (∑' k, abelTerm a w k) =
      partialSum a N * w (N + 1) - ∑' k, abelTerm a w (k + N) := by
  have hsplit := ht.sum_add_tsum_nat_add N
  rw [finite_abel]
  change partialSum a N * w (N + 1) +
    (∑ k ∈ Finset.range N, abelTerm a w k) - (∑' k, abelTerm a w k) = _
  rw [← hsplit]
  ring

/-- Certified error bound. Calling the target a limit additionally needs hb. -/
theorem remainder_bound (a w : ℕ → ℂ) (g : ℕ → ℝ) (N : ℕ)
    (hg : Summable g) (hbound : ∀ k, ‖abelTerm a w k‖ ≤ g k) :
    ‖(∑ k ∈ Finset.range N, a (k + 1) * w (k + 1)) -
      (∑' k, abelTerm a w k)‖ ≤
      ‖partialSum a N * w (N + 1)‖ + ∑' k, g (k + N) := by
  rw [remainder_identity a w N (hg.of_norm_bounded hbound)]
  have htail : Summable (fun k => g (k + N)) :=
    (summable_nat_add_iff N).2 hg
  exact (norm_sub_le _ _).trans (add_le_add le_rfl
    (tsum_of_norm_bounded htail.hasSum (fun k => hbound (k + N))))

end UBT.RH.AbelLimit
