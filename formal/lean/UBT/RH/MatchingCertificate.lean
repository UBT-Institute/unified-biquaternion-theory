import UBT.RH.PrimePairing
import Mathlib.Data.Finset.Sum

/-! A matching/vertex-cover certificate proves optimality without trusting
an augmenting-path implementation. No asymptotic matching bound is assumed. -/
namespace UBT.RH.MatchingCertificate
open Finset
open scoped ArithmeticFunction.Moebius

def IsMatching (M : Finset (ℕ × ℕ)) : Prop :=
  Set.InjOn Prod.fst (M : Set (ℕ × ℕ)) ∧ Set.InjOn Prod.snd (M : Set (ℕ × ℕ))

def Covers (E : Finset (ℕ × ℕ)) (CL CR : Finset ℕ) : Prop :=
  ∀ e ∈ E, e.1 ∈ CL ∨ e.2 ∈ CR

theorem matching_le_cover (M E : Finset (ℕ × ℕ)) (CL CR : Finset ℕ)
    (hM : IsMatching M) (hsub : M ⊆ E) (hC : Covers E CL CR) :
    M.card ≤ CL.card + CR.card := by
  let tag : ℕ × ℕ → ℕ ⊕ ℕ := fun e =>
    if e.1 ∈ CL then Sum.inl e.1 else Sum.inr e.2
  have hm : Set.MapsTo tag (M : Set (ℕ × ℕ)) (CL.disjSum CR : Set (ℕ ⊕ ℕ)) := by
    intro e he
    have hc := hC e (hsub he)
    by_cases h : e.1 ∈ CL
    · simpa [tag, h] using h
    · simpa [tag, h] using hc.resolve_left h
  have hi : Set.InjOn tag (M : Set (ℕ × ℕ)) := by
    intro e he f hf hef
    by_cases hec : e.1 ∈ CL <;> by_cases hfc : f.1 ∈ CL
    · apply hM.1 he hf
      simpa [tag, hec, hfc] using hef
    · simp [tag, hec, hfc] at hef
    · simp [tag, hec, hfc] at hef
    · apply hM.2 he hf
      simpa [tag, hec, hfc] using hef
  simpa only [card_disjSum] using card_le_card_of_injOn tag hm hi

/-- Equal matching and cover sizes certify optimality against every competitor. -/
theorem certificate_maximum (M E : Finset (ℕ × ℕ)) (CL CR : Finset ℕ)
    (hC : Covers E CL CR) (hsize : M.card = CL.card + CR.card)
    (K : Finset (ℕ × ℕ)) (hK : IsMatching K) (hsub : K ⊆ E) :
    K.card ≤ M.card := by
  rw [hsize]
  exact matching_le_cover K E CL CR hK hsub hC

theorem matched_sum_zero (M : Finset (ℕ × ℕ)) (f g : ℕ → ℤ)
    (hM : IsMatching M) (hsign : ∀ e ∈ M, f e.1 + g e.2 = 0) :
    (∑ x ∈ M.image Prod.fst, f x) + (∑ y ∈ M.image Prod.snd, g y) = 0 := by
  rw [sum_image hM.1, sum_image hM.2, ← sum_add_distrib]
  exact sum_eq_zero hsign

theorem residual_sum (M : Finset (ℕ × ℕ)) (L R : Finset ℕ) (f g : ℕ → ℤ)
    (hM : IsMatching M) (hsign : ∀ e ∈ M, f e.1 + g e.2 = 0)
    (hL : M.image Prod.fst ⊆ L) (hR : M.image Prod.snd ⊆ R) :
    (∑ x ∈ L, f x) + (∑ y ∈ R, g y) =
      (∑ x ∈ L \ M.image Prod.fst, f x) +
        (∑ y ∈ R \ M.image Prod.snd, g y) := by
  have hl : (∑ x ∈ L \ M.image Prod.fst, f x) +
      (∑ x ∈ M.image Prod.fst, f x) = ∑ x ∈ L, f x := sum_sdiff hL
  have hr : (∑ y ∈ R \ M.image Prod.snd, g y) +
      (∑ y ∈ M.image Prod.snd, g y) = ∑ y ∈ R, g y := sum_sdiff hR
  have hz := matched_sum_zero M f g hM hsign
  linarith

/-- Arithmetic validity of replacing one prime with two coprime primes. -/
theorem prime_exchange_cancel (a p q r : ℕ) (hp : p.Prime) (hq : q.Prime)
    (hr : r.Prime) (hap : a.Coprime p) (haqr : a.Coprime (q * r))
    (hqr : q.Coprime r) : μ (a * p) + μ (a * (q * r)) = 0 := by
  rw [ArithmeticFunction.IsMultiplicative.map_mul_of_coprime
      ArithmeticFunction.isMultiplicative_moebius hap,
    ArithmeticFunction.IsMultiplicative.map_mul_of_coprime
      ArithmeticFunction.isMultiplicative_moebius haqr,
    ArithmeticFunction.IsMultiplicative.map_mul_of_coprime
      ArithmeticFunction.isMultiplicative_moebius hqr,
    ArithmeticFunction.moebius_apply_prime hp,
    ArithmeticFunction.moebius_apply_prime hq,
    ArithmeticFunction.moebius_apply_prime hr]
  ring

end UBT.RH.MatchingCertificate
