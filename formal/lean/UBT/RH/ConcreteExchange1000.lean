import UBT.RH.MatchingCertificate

/-! Generated matching data, checked by the Lean kernel using `decide`.
Regenerate with tools/export_prime_exchange_lean.py. No native_decide. -/
namespace UBT.RH.ConcreteExchange1000
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

def matching1000 : Finset (ℕ × ℕ) := {(1, 2), (6, 231), (10, 5), (14, 7), (15, 11), (21, 13), (22, 17), (26, 19), (33, 23), (34, 29), (35, 30), (38, 31), (39, 37), (46, 41), (51, 42), (55, 43), (57, 47), (58, 53), (62, 59), (65, 61), (69, 66), (74, 67), (77, 70), (82, 71), (85, 73), (86, 78), (87, 79), (91, 83), (93, 89), (94, 97), (95, 101), (106, 102), (111, 103), (115, 105), (118, 107), (119, 109), (122, 110), (123, 113), (129, 114), (133, 127), (134, 130), (141, 131), (142, 137), (143, 139), (145, 149), (146, 138), (155, 151), (158, 154), (159, 157), (161, 163), (166, 167), (177, 165), (178, 170), (183, 173), (185, 179), (187, 181), (194, 174), (201, 186), (202, 182), (203, 191), (205, 190), (206, 193), (209, 197), (210, 195), (213, 199), (214, 211), (215, 223), (217, 227), (218, 222), (219, 229), (221, 233), (226, 230), (235, 239), (237, 987), (247, 241), (249, 246), (253, 251), (254, 238), (259, 257), (262, 258), (265, 255), (267, 263), (274, 266), (278, 269), (287, 271), (291, 273), (295, 277), (298, 281), (299, 283), (301, 293), (302, 282), (303, 285), (305, 290), (309, 307), (314, 286), (319, 311), (321, 313), (323, 317), (326, 310), (327, 318), (329, 322), (330, 345), (334, 331), (335, 337), (339, 347), (341, 349), (346, 353), (355, 359), (358, 354), (362, 366), (365, 367), (371, 357), (377, 373), (381, 379), (382, 370), (386, 374), (390, 402), (391, 383), (393, 389), (394, 397), (395, 385), (398, 401), (403, 409), (407, 418), (411, 399), (413, 406), (415, 410), (417, 419), (422, 421), (427, 431), (437, 433), (445, 430), (446, 426), (447, 429), (451, 439), (453, 435), (454, 434), (458, 438), (462, 474), (466, 442), (469, 443), (471, 449), (473, 457), (478, 461), (481, 455), (482, 463), (485, 465), (489, 467), (493, 479), (497, 483), (501, 487), (502, 470), (505, 491), (510, 498), (511, 499), (514, 494), (515, 503), (517, 506), (519, 509), (526, 518), (527, 521), (533, 523), (535, 530), (537, 534), (538, 541), (542, 547), (543, 555), (545, 557), (546, 574), (551, 563), (553, 569), (554, 571), (559, 577), (562, 582), (565, 587), (566, 590), (570, 606), (573, 561), (579, 593), (581, 595), (583, 599), (586, 598), (589, 601), (591, 607), (597, 609), (611, 613), (614, 602), (622, 610), (623, 617), (626, 618), (629, 619), (633, 615), (634, 631), (635, 641), (649, 627), (655, 643), (662, 638), (667, 647), (669, 642), (671, 653), (674, 646), (679, 651), (681, 645), (685, 659), (687, 654), (689, 661), (690, 670), (694, 658), (695, 665), (697, 663), (698, 673), (699, 677), (703, 683), (706, 678), (707, 691), (713, 682), (714, 742), (717, 701), (718, 709), (721, 719), (723, 705), (731, 727), (734, 710), (737, 715), (745, 730), (746, 733), (749, 739), (753, 741), (755, 743), (758, 751), (763, 757), (766, 754), (767, 761), (770, 790), (771, 759), (778, 762), (779, 769), (781, 773), (785, 787), (789, 777), (791, 797), (793, 806), (794, 782), (798, 786), (799, 809), (802, 811), (803, 814), (807, 795), (813, 821), (815, 805), (817, 823), (818, 822), (831, 827), (835, 829), (838, 826), (842, 830), (843, 834), (849, 839), (851, 853), (858, 894), (862, 854), (865, 857), (866, 859), (869, 863), (870, 885), (871, 877), (878, 874), (879, 861), (886, 881), (889, 883), (893, 887), (895, 890), (898, 902), (899, 907), (901, 911), (905, 915), (910, 938), (913, 919), (914, 906), (917, 903), (921, 897), (922, 929), (923, 937), (926, 941), (930, 942), (933, 947), (934, 946), (939, 953), (943, 967), (949, 962), (951, 957), (955, 935), (958, 970), (959, 971), (965, 977), (966, 978), (973, 983), (974, 986), (979, 991), (982, 994), (985, 997), (989, 3), (993, 969)}

theorem matching1000_valid : IsMatching matching1000 := by
  constructor
  · apply card_image_iff.mp
    decide +kernel
  · apply card_image_iff.mp
    decide +kernel

theorem matching1000_checks : ∀ e ∈ matching1000,
    e.1 ≤ 1000 ∧ muEval e.1 = 1 ∧ e.2 ≤ 1000 ∧ muEval e.2 = -1 ∧ Allowed e.1 e.2 := by
  decide +kernel

theorem matching1000_edges : matching1000 ⊆ edges 1000 := by
  intro e he
  obtain ⟨hx, hmx, hy, hmy, ha⟩ := matching1000_checks e he
  apply mem_filter.mpr
  refine ⟨mem_product.mpr ⟨?_, ?_⟩, ha⟩
  · simp only [positive, mem_filter, mem_range, Nat.lt_succ_iff]
    exact ⟨hx, hmx⟩
  · simp only [negative, mem_filter, mem_range, Nat.lt_succ_iff]
    exact ⟨hy, hmy⟩

theorem matching1000_size : matching1000.card = 303 := by decide +kernel

theorem negative1000_size : (negative 1000).card = 303 := by decide +kernel

theorem positive1000_size : (positive 1000).card = 305 := by decide +kernel

theorem right_cover (N : ℕ) : Covers (edges N) ∅ (negative N) := by
  intro e he
  right
  exact (mem_product.mp (mem_filter.mp he).1).2

theorem matching1000_maximum (K : Finset (ℕ × ℕ))
    (hK : IsMatching K) (hsub : K ⊆ edges 1000) : K.card ≤ matching1000.card := by
  apply certificate_maximum matching1000 (edges 1000) ∅ (negative 1000)
    (right_cover 1000) _ K hK hsub
  simp [matching1000_size, negative1000_size]

theorem matching1000_unmatched :
    (positive 1000).card + (negative 1000).card - 2 * matching1000.card = 2 := by
  rw [positive1000_size, negative1000_size, matching1000_size]

theorem mertens1000 : UBT.RH.PrimePairing.mertens 1000 = 2 := by
  rw [mertens_counts, positive1000_size, negative1000_size]
  norm_num

theorem matching1000_signs : ∀ e ∈ matching1000, μ e.1 + μ e.2 = 0 := by
  intro e he
  have hp := mem_product.mp (mem_filter.mp (matching1000_edges he)).1
  have hl := (mem_filter.mp hp.1).2
  have hr := (mem_filter.mp hp.2).2
  simp only [muEval_eq] at hl hr
  omega

end UBT.RH.ConcreteExchange1000
