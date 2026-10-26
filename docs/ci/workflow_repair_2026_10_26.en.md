<!-- BILINGUAL-UNIT: workflow-repair-2026-10-26 -->
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


# Workflow repair verification record

2026-10-26. Baseline: master commit `6c822976bcc489eea37ee6e81cb70ca44dbec172`.
Implementation and review: [PR #783](https://github.com/UBT-Institute/unified-biquaternion-theory/pull/783).

## Failures and repairs

| Workflow | Observed cause | Repair |
|---|---|---|
| Verify Lorentz Invariance | Stale provenance metadata/checksums and structural equality of equivalent SymPy gradients | Normalize generated headers and manifests; compare exact polynomial residuals |
| Bilingual document parity | Missing Czech editions and incomplete existing translations | Add 42 editions, synchronize 39 editions, and identify all 81 repaired pairs with matching content units |
| Build all LaTeX PDFs | Source provenance gate fails before compilation | Repair checked-in metadata; retain the signed editorial/review gates |
| Repo Integrity Gate | Source archive exceeds the size limit | Exclude four reproducible PDF outputs from source exports, retaining the files in Git and retaining every TeX source |

Generated-header maintenance alone does not materially edit legacy prose. The changed-file detector ignores the generated marker and its copyright separator; it continues to reject new unpaired prose and substantive unpaired edits. All registered pairs still undergo the complete structural check.

## Local verification

- Full pytest: **890 passed, 5 skipped**. After the final copyright-separator regression was added, the focused bilingual-gate suite passed **5 tests**.
- All-pairs and changed-base bilingual checks: **177 pairs passed** before this verification pair was added.
- Provenance headers, signed editorial/review gates, documentation lint, and all **83** declared SHA-256 entries passed.
- Symbolic Lorentz interval, quaternion norm multiplicativity, and SL(2,C) sandwich identities passed.
- Source archive: **11,276,490 bytes**, below the unchanged **12,582,912-byte** limit before this verification pair was added. Four publication PDFs remain tracked.
- Local LaTeX audit: **358 roots attempted, 250 PDFs built, 108 document failures recorded**. Both required curated PDFs built and passed PDF provenance checks. Other document failures remain visible in the audit; this patch does not claim that every TeX root compiles.

## Scope and review

No scientific claim tier, editorial assignment, or author attestation was changed. The English editions were the translation sources. Equations, symbols, assumptions, proof boundaries, status labels, and caveats are intended to remain identical in the Czech editions; structural checks do not establish semantic equivalence.

The repository owner authorized replacing mandatory human translation sign-off with independent automatic semantic review. Under the updated `BILINGUAL_CONTENT_POLICY.en.md` and `AGENTS.md`, this PR remains draft until the semantic module produces a passing, calibrated report bound to the current source hashes. GitHub Actions results must be assessed on the final PR commit separately from these local checks.
