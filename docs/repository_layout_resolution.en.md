<!-- BILINGUAL-UNIT: repository_layout_resolution -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Repository layout after integrating the historical reorganization

The directory proposal in PR #292 predates the current canonical/research/archive layout. The merge retains the current locations. Its original source is preserved in Git ancestry; 324 proposed payload blobs had byte-identical copies in the inspected current tree. A root compatibility import now delegates to the supported forensic package, and test path helpers resolve the archived variants. No historical theory variant becomes the canonical model.

| Purpose | Current path |
|---|---|
| Canonical definitions | `canonical/` |
| Active forensic package | `tools/forensic_fingerprint/` |
| Compatibility import | `forensic_fingerprint/` |
| Historical variant with chronofactor | `ARCHIVE/archive_legacy/ARCHIVE/legacy_variants/ubt_with_chronofactor/` |
| Historical variant without chronofactor | `ARCHIVE/archive_legacy/ARCHIVE/legacy_variants/ubt_no_chronofactor/` |

The old comparison scaffolding is resolved as navigation among these existing layers. Algebraic similarity does not establish equivalent dynamics, identical observables, or a validated CMB prediction. The legacy chronology and the present single-field tetrad formulation must remain distinct. The active statistical tests use synthetic data; external observation files are separate inputs.

Verification: `tests/test_merged_repo_layout.py`, `tests/test_forensic_fingerprint.py` and `tests/test_planck_units_and_strict_mode.py`. These exercise imports, archived path resolution and the active forensic implementation. This is repository compatibility work, not a physics theorem.
