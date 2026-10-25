# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""Generate concrete data, never proof axioms, for kernel-checked certificates."""
from pathlib import Path
import re
from verify_prime_exchange_matching import arithmetic, experiment


def generate(n=100):
    result = experiment(n, arithmetic(n), include_certificates=True)
    pairs = result['exchange']['certificate']['pairs']
    literal = ', '.join(f'({a}, {b})' for a,b in pairs)
    source = '''import UBT.RH.MatchingCertificate

/-! Generated matching data, checked by the Lean kernel using `decide`.
Regenerate with tools/export_prime_exchange_lean.py. No native_decide. -/
namespace UBT.RH.ConcreteExchange
open Finset
open UBT.RH.MatchingCertificate
open scoped ArithmeticFunction.Moebius
set_option maxRecDepth 100000
set_option maxHeartbeats 8000000

def positive (N : ℕ) : Finset ℕ :=
  (range (N + 1)).filter (fun n => muEval n = 1)

def negative (N : ℕ) : Finset ℕ :=
  (range (N + 1)).filter (fun n => muEval n = -1)

theorem positive_eq (N : ℕ) :
    positive N = (range (N + 1)).filter (fun n => μ n = 1) := by
  simp only [positive, muEval_eq]

theorem negative_eq (N : ℕ) :
    negative N = (range (N + 1)).filter (fun n => μ n = -1) := by
  simp only [negative, muEval_eq]

theorem mertens_counts (N : ℕ) :
    UBT.RH.PrimePairing.mertens N = (positive N).card - (negative N).card := by
  have hs (v : ℤ) : (∑ n ∈ range (N + 1), if μ n = v then (1 : ℤ) else 0) =
      (((range (N + 1)).filter (fun n => μ n = v)).card : ℤ) := by
    rw [← sum_filter]
    simp
  unfold UBT.RH.PrimePairing.mertens
  calc
    _ = (∑ n ∈ range (N + 1), if μ n = 1 then (1 : ℤ) else 0) -
        (∑ n ∈ range (N + 1), if μ n = -1 then (1 : ℤ) else 0) := by
      rw [← sum_sub_distrib]
      apply sum_congr rfl
      intro n hn
      rcases ArithmeticFunction.moebius_eq_or n with h | h | h <;> simp [h]
    _ = _ := by rw [hs 1, hs (-1), positive_eq, negative_eq]

def Allowed (x y : ℕ) : Prop :=
  let a := (x / Nat.gcd x y).primeFactorsList.length
  let b := (y / Nat.gcd x y).primeFactorsList.length
  (a = 0 ∧ b = 1) ∨ (a = 1 ∧ b = 0) ∨
    (a = 1 ∧ b = 2) ∨ (a = 2 ∧ b = 1)

instance (x y : ℕ) : Decidable (Allowed x y) := by
  unfold Allowed
  infer_instance

def edges (N : ℕ) : Finset (ℕ × ℕ) :=
  ((positive N).product (negative N)).filter (fun e => Allowed e.1 e.2)

def matching100 : Finset (ℕ × ℕ) := {''' + '@@PAIRS@@' + '''}

theorem matching100_valid : IsMatching matching100 := by
  constructor
  · apply card_image_iff.mp
    decide +kernel
  · apply card_image_iff.mp
    decide +kernel

theorem matching100_checks : ∀ e ∈ matching100,
    e.1 ≤ 100 ∧ muEval e.1 = 1 ∧ e.2 ≤ 100 ∧ muEval e.2 = -1 ∧ Allowed e.1 e.2 := by
  decide +kernel

theorem matching100_edges : matching100 ⊆ edges 100 := by
  intro e he
  obtain ⟨hx, hmx, hy, hmy, ha⟩ := matching100_checks e he
  apply mem_filter.mpr
  refine ⟨mem_product.mpr ⟨?_, ?_⟩, ha⟩
  · simp only [positive, mem_filter, mem_range, Nat.lt_succ_iff]
    exact ⟨hx, hmx⟩
  · simp only [negative, mem_filter, mem_range, Nat.lt_succ_iff]
    exact ⟨hy, hmy⟩

theorem matching100_size : matching100.card = 30 := by decide +kernel

theorem negative100_size : (negative 100).card = 30 := by decide +kernel

theorem positive100_size : (positive 100).card = 31 := by decide +kernel

theorem right_cover (N : ℕ) : Covers (edges N) ∅ (negative N) := by
  intro e he
  right
  exact (mem_product.mp (mem_filter.mp he).1).2

theorem matching100_maximum (K : Finset (ℕ × ℕ))
    (hK : IsMatching K) (hsub : K ⊆ edges 100) : K.card ≤ matching100.card := by
  apply certificate_maximum matching100 (edges 100) ∅ (negative 100)
    (right_cover 100) _ K hK hsub
  simp [matching100_size, negative100_size]

theorem matching100_unmatched :
    (positive 100).card + (negative 100).card - 2 * matching100.card = 1 := by
  rw [positive100_size, negative100_size, matching100_size]

theorem mertens100 : UBT.RH.PrimePairing.mertens 100 = 1 := by
  rw [mertens_counts, positive100_size, negative100_size]
  norm_num

theorem matching100_signs : ∀ e ∈ matching100, μ e.1 + μ e.2 = 0 := by
  intro e he
  have hp := mem_product.mp (mem_filter.mp (matching100_edges he)).1
  have hl := (mem_filter.mp hp.1).2
  have hr := (mem_filter.mp hp.2).2
  simp only [muEval_eq] at hl hr
  omega

end UBT.RH.ConcreteExchange
'''

    source = re.sub(r'\b100\b', str(n), source)
    for prefix in ['matching', 'negative', 'positive', 'mertens']:
        source = source.replace(prefix+'100', prefix+str(n))
    if n != 100:
        source = source.replace('ConcreteExchange', 'ConcreteExchange'+str(n))
    source = source.replace('card = 30 :=', 'card = '+str(len(pairs))+' :=')
    source = source.replace('card = 31 :=', 'card = '+str(result['positive'])+' :=')
    source = source.replace('= 1 := by\n  rw', '= '+str(abs(result['M']))+' := by\n  rw')
    return source.replace('@@PAIRS@@', literal)


if __name__ == '__main__':
    Path('formal/lean/UBT/RH/ConcreteExchange.lean').write_text(generate())
    Path('formal/lean/UBT/RH/ConcreteExchange1000.lean').write_text(generate(1000))
