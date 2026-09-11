<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Archive: Historical SU(3) Derivation Approaches

This directory (and the parent `canonical/su3_derivation/` directory) preserves
earlier approaches to deriving `SU(3)_c` colour symmetry within the Unified
Biquaternion Theory.  They are retained for **provenance and historical priority**
and must not be silently deleted or rewritten.

---

## Why this archive exists

The UBT project investigated SU(3) colour through several successive routes:

| Approach | Key files | Status |
|---|---|---|
| Discrete involutions on C⊗H | `su3_from_involutions.tex`, `step1_involution_summary.tex` | HISTORICAL — proved carrier selection conditionally |
| Direct 8D Gell-Mann embedding | (sections inside above files) | HISTORICAL — fails as C⊗H automorphism |
| Quantum superposition / triqubit | `step1_superposition_approach.tex` | HISTORICAL — proved carrier over C^3; U(3) structure argument needed correction |
| Previous step-by-step result | `step3_SU3_result.tex` | HISTORICAL — collected earlier verdicts |

---

## What these approaches showed

1. **Involution approach** (Theorems G.A–G.D in `su3_from_involutions.tex`):
   The three Z2 involutions on C⊗H select a complex rank-3 carrier
   `V_c = C-span{I,J,K}` that is isomorphic to C^3.  This is a genuine
   algebraic result.  It is **conditional**: the unitary/Yang–Mills dynamics on
   that carrier were *postulated*, not derived from the canonical UBT action.

2. **Superposition / triqubit approach** (`step1_superposition_approach.tex`):
   Superpositions of the three imaginary quaternion directions give a C^3
   colour space.  The approach correctly identifies the carrier but used an
   incorrect global group statement `U(3) ≅ U(1) × SU(3)` (the global group
   is `(SU(3) × U(1)) / Z_3`, not a direct product).  The Lie-algebra
   decomposition `u(3) = su(3) ⊕ u(1)` is valid.

3. **Error-correction / triqubit QEC motivation**:
   Some earlier discussions motivated the three-colour sector by analogy with
   three-qubit error correction or I-Ching trigrams.  This numerological
   motivation (2^3 = 8) was **never** part of the mathematical proof and does
   not belong in canonical derivations.  The canonical result rests on the
   stabilizer of an algebraically derived Hermitian form and volume form, not
   on error-correction or the coincidence 2^3 = 8.

---

## What the new canonical derivation does differently

The new canonical source is:

    canonical/su3_derivation/su3_stabilizer_exterior_fock.tex

It differs from all earlier approaches by:

* **No unitary-structure postulate** — the Hermitian form `h(v,w) = Sc(v† w)`
  is derived directly from the biquaternionic adjoint already present in UBT.
* **No dimension-count numerology** — SU(3) is characterised as the stabiliser
  of two canonically induced structures (h and Ω), not by counting.
* **No error-correction premise** — the Fock/exterior space 1⊕3⊕3-bar⊕1
  is a consequence of standard representation theory applied to the
  algebraically constructed SU(3) action on V = C-span{I,J,K}.
* **Correct global group structure** — U(3) ≅ (SU(3) × U(1)) / Z_3;
  the Lie-algebra split u(3) = su(3) ⊕ u(1) is noted as valid.
* **Explicit dynamical gap** — GAP-SU3-DYN remains OPEN; whether the
  canonical UBT action dynamically selects this SU(3) is stated explicitly as
  unresolved.

---

## Guidance for future contributors

* **Do not delete** the historical files.  They record the research lineage
  and priority.
* **Do not silently rewrite** old files as if they had always contained the
  new proof.
* **Do reference** the new canonical source when citing the SU(3) stabilizer
  theorem in new work.
* **Do not promote** the conditional/historical results to unconditional status
  without an explicit proof of GAP-SU3-DYN.
