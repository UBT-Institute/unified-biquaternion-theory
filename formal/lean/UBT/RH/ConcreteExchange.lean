import UBT.RH.MatchingCertificate

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

def matching100 : Finset (ℕ × ℕ) := {(1, 2), (6, 3), (10, 5), (14, 7), (15, 11), (21, 13), (22, 17), (26, 19), (33, 23), (34, 29), (35, 30), (38, 31), (39, 37), (46, 41), (51, 42), (55, 43), (57, 47), (58, 53), (62, 59), (65, 61), (69, 66), (74, 67), (77, 70), (82, 71), (85, 73), (86, 78), (87, 79), (91, 83), (93, 89), (94, 97)}

theorem matching100_valid : IsMatching matching100 := by
  constructor
  · apply card_image_iff.mp
    decide
  · apply card_image_iff.mp
    decide

theorem matching100_edges : matching100 ⊆ edges 100 := by decide

theorem matching100_size : matching100.card = 30 := by decide

theorem negative100_size : (negative 100).card = 30 := by decide

theorem positive100_size : (positive 100).card = 31 := by decide

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

theorem matching100_signs : ∀ e ∈ matching100, μ e.1 + μ e.2 = 0 := by
  intro e he
  have hp := mem_product.mp (mem_filter.mp (matching100_edges he)).1
  have hl := (mem_filter.mp hp.1).2
  have hr := (mem_filter.mp hp.2).2
  simp only [muEval_eq] at hl hr
  omega

end UBT.RH.ConcreteExchange
