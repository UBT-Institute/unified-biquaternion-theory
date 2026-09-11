<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# SU(3) Colour Sector — Derivation Index

---

## CANONICAL (current preferred derivation)

### `su3_stabilizer_exterior_fock.tex`

**Status**: PROVED [L1] — algebraic stabiliser and Fock representation.
**Machine verified**: `verification/su3_stabilizer_fock_check.py` — exact SymPy PASS (see script output).
**Lean**: LEAN-PENDING.

This is the preferred derivation.  It starts from the canonical UBT colour subspace
`V = C-span{I,J,K} ⊂ C⊗H` and:

1. Derives a canonical Hermitian form `h` from the biquaternionic adjoint `†`
   already present in UBT: `h(v,w) = Sc(v†w)`.
2. Derives a canonical complex volume form `Ω` from quaternion multiplication:
   `Ω(v,w,u) = -Sc(vwu) = det([v;w;u])`.
3. Proves `Stab_{GL(V)}(h,Ω) = SU(3)` without any postulate.
4. Constructs `Λ•V = 1 ⊕ 3 ⊕ 3-bar ⊕ 1` and the 8D second-quantised su(3)
   generator algebra on Fock space.

**Why preferred over earlier approaches:**
- No unitary-structure postulate.
- No dimension-count numerology (2^3 = 8).
- No error-correction premise.
- No incorrect global-group direct-product claim.
- Correct global: `U(3) ≅ (SU(3) × U(1)) / Z_3`.
- Clear separation of algebraic theorem from dynamical gauge gap.

**GAP-SU3-DYN: OPEN** — the dynamical identification of this SU(3) stabiliser
with the local QCD gauge field requires an action-level derivation not yet
performed.

---

## COMPLEMENTARY / HISTORICAL (preserved for provenance)

> These files are preserved intact. Do not delete or rewrite them.
> See `archive/README.md` for full provenance notes.

### `su3_from_involutions.tex`
Involution approach (Theorems G.A–G.D).
Proved: carrier selection `V_c ≅ C^3` from Z2×Z2×Z2 involutions.
Status: Conditional (unitary dynamics postulated; not derived from action).

### `step1_involution_summary.tex`
Summary of the involution-based derivation.
Status: HISTORICAL / COMPLEMENTARY.

### `step1_superposition_approach.tex`
Quantum-superposition/triqubit approach.
Proved: same C^3 carrier from superpositions.
Caveat: the global group statement `U(3) ≅ U(1) × SU(3)` in the original
Theorem 3.1 is INCORRECT; corrected in place to `(SU(3)×U(1))/Z_3`.
Status: HISTORICAL / COMPLEMENTARY.

### `step3_SU3_result.tex`
Collected earlier verdict (three approaches compared).
Status: HISTORICAL.

### `archive/README.md`
Full provenance notes on all historical approaches.

---

## Claim status

| Claim | Status |
|---|---|
| Algebraic SU(3) stabiliser of UBT colour sector | PROVED [L1] / machine verified |
| Fundamental **3** in Λ¹V | PROVED [L1] |
| Anti-fundamental **3-bar** in Λ²V | PROVED [L1] / machine verified |
| Eight su(3) generators on 8D Fock space | PROVED [L1] / machine verified |
| Local dynamical QCD gauge identification | OPEN — GAP-SU3-DYN |
| Dynamical confinement / mass gap | OPEN (Clay Millennium problem) |

