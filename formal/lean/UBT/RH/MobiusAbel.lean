import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt
import Mathlib.Tactic

/-!
# Exact arithmetic foundations of the Möbius RH route

Classical identities, with mathlib attribution. Dirichlet convolution is
algebraic: no analytic continuation or bounded operator inverse is asserted.
The finite Abel identity holds for every cutoff and every weight in a ring.
-/

namespace UBT.RH.MobiusAbel

open scoped ArithmeticFunction.zeta ArithmeticFunction.Moebius

theorem mobius_left_inverse :
    (μ * ζ : ArithmeticFunction ℂ) = 1 :=
  ArithmeticFunction.coe_moebius_mul_coe_zeta

theorem mobius_right_inverse :
    (ζ * μ : ArithmeticFunction ℂ) = 1 :=
  ArithmeticFunction.coe_zeta_mul_coe_moebius

/-- The formal inverse is unique, without an infinite-series hypothesis. -/
theorem inverse_unique (f : ArithmeticFunction ℂ)
    (hf : f * ζ = 1) : f = μ := by
  calc
    f = f * (ζ * μ) := by rw [mobius_right_inverse, mul_one]
    _ = (f * ζ) * μ := by rw [mul_assoc]
    _ = μ := by rw [hf, one_mul]

theorem mangoldt_convolution :
    (μ : ArithmeticFunction ℝ) * ArithmeticFunction.log =
      ArithmeticFunction.vonMangoldt :=
  ArithmeticFunction.moebius_mul_log_eq_vonMangoldt

theorem mangoldt_prime_power (p k : ℕ) (hp : p.Prime) (hk : k ≠ 0) :
    ArithmeticFunction.vonMangoldt (p ^ k) = Real.log p := by
  rw [ArithmeticFunction.vonMangoldt_apply_pow hk,
    ArithmeticFunction.vonMangoldt_apply_prime hp]

theorem mangoldt_support (n : ℕ) :
    ArithmeticFunction.vonMangoldt n ≠ 0 ↔ IsPrimePow n :=
  ArithmeticFunction.vonMangoldt_ne_zero_iff

section FiniteAbel
variable {R : Type*} [Ring R]

def partialSum (a : ℕ → R) (N : ℕ) : R :=
  ∑ k ∈ Finset.range N, a (k + 1)

theorem partialSum_succ (a : ℕ → R) (N : ℕ) :
    partialSum a (N + 1) = partialSum a N + a (N + 1) := by
  simp only [partialSum, Finset.sum_range_succ]

/-- Exact endpoint convention: A(N) w(N+1), with differences through N. -/
theorem finite_abel (a w : ℕ → R) (N : ℕ) :
    (∑ k ∈ Finset.range N, a (k + 1) * w (k + 1)) =
      partialSum a N * w (N + 1) +
        ∑ k ∈ Finset.range N,
          partialSum a (k + 1) * (w (k + 1) - w (k + 2)) := by
  induction N with
  | zero => simp [partialSum]
  | succ N ih =>
    simp only [Finset.sum_range_succ]
    rw [ih, partialSum_succ]
    noncomm_ring

end FiniteAbel

/-- Complex weights may be n^(-s); convergence is a separate obligation. -/
theorem mobius_finite_abel (w : ℕ → ℂ) (N : ℕ) :
    (∑ k ∈ Finset.range N, (μ (k + 1) : ℂ) * w (k + 1)) =
      partialSum (fun n => (μ n : ℂ)) N * w (N + 1) +
        ∑ k ∈ Finset.range N,
          partialSum (fun n => (μ n : ℂ)) (k + 1) *
            (w (k + 1) - w (k + 2)) :=
  finite_abel (fun n => (μ n : ℂ)) w N

end UBT.RH.MobiusAbel
