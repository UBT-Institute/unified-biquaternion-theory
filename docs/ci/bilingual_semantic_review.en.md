<!-- BILINGUAL-UNIT: bilingual-semantic-review -->
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


# Automatic translation review

## Meaning and scope

The semantic module `tools/verify_bilingual_semantics.py` replaces mandatory human translation sign-off when both structural and independent semantic checks pass. English and Czech remain equally normative. It compares complete changed pairs in both directions, including assumptions, domains, negation, quantifiers, proof status, caveats, and added or missing information. A separate model request reviews the translations without repository instructions or access to tools. It does not generate replacement translations.

Each run first tests the reviewer on equivalent translations and deliberately wrong negations, quantifiers, assumptions, and proof claims, including an instruction-injection example. Calibration failure prevents document approval. Calibration is a useful check, not a measured guarantee of translation accuracy. The reviewer can still miss an error; scientific validity and author attestations remain separate.

## Workflow and configuration

The `semantics` job in `.github/workflows/bilingual_docs.yml` runs after structural parity. It uses the built-in `GITHUB_TOKEN` with `copilot-requests: write` in an organization-owned repository. An organization administrator must enable the policy **Allow use of Copilot CLI billed to the organization** and allow the requested model. No personal API key is stored. If access is unavailable, the job fails and retains the blocked report; it never substitutes a successful structural check for semantic approval. The initial live request was denied by organization policy before calibration; no semantic approval is claimed by the implementation or its unit tests.

The runtime is pinned to `@github/copilot@1.0.103`, Node `24`, and the requested model `claude-sonnet-5.5`. Model availability and provider internals may change; the requested identifier is recorded, not asserted to be an immutable backend revision. Updating the model or runtime requires a code change and fresh calibration. Inference consumes the organization's Copilot allowance or budget; this implementation does not enable a paid plan or change spending limits.

The administrator setup steps are documented in [GitHub's Copilot CLI in Actions guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli-in-actions). After enabling the policy and model, rerun the failed semantic job on the unchanged commit. Any later source change requires a new review for that source.

The module permits at most `64` requests per run, including calibration, with at most `4` pairs and `80000` prompt characters per document request. The document-review prompt budget is `1500000` characters. Requests run with `2` workers by default and a `240` second timeout each; the job has a `45` minute timeout. Oversized pairs must be split into paired source documents; no text is silently truncated. The manual workflow runs all pairs, while pull requests and master pushes select pairs whose raw source bytes or paths changed relative to their base. This includes whitespace and generated-header changes in already paired sources, without requiring migration of unchanged legacy prose.

## Evidence and failure handling

The workflow uploads `build/bilingual/semantic-review.json` and its summary as an artifact retained for `30` days. The JSON records the commit, exact raw source hashes, requested model, runtime, verifier and policy hashes, calibration, every reviewed paragraph alignment, and verdicts. A changed source invalidates the old evidence. Generated provenance is omitted only from model input; its bytes remain covered by the source hashes. Committed reports are never accepted as approvals or a cache.

Every paragraph must occur exactly once on each language side of the alignments. Missing coverage, duplicate IDs or JSON keys, stale hashes, invalid fields, nonboolean checks, inconsistent pass verdicts, timeout, missing access, and provider errors block the gate. Any failed or uncertain comparison blocks merge until the text is corrected and rechecked. An optional human review may resolve a disputed finding; the automated gate itself has no manual bypass. Protect the `semantics` status check in repository branch rules if enforcement against direct merges is required; workflow code does not modify repository settings.

## Local use and validation

Run the structural checker before the semantic module. The same pinned runtime and an authorized Copilot token are needed for live local review. The following commands review committed changes from a chosen base and run the protocol regression tests:

```sh
python tools/check_bilingual_pairs.py --root . --changed-base BASE_SHA
python tools/verify_bilingual_semantics.py --root . --changed-base BASE_SHA
python -m pytest tests/test_bilingual_gate.py tests/test_bilingual_semantics.py
```

Unit tests use simulated responses to verify failure handling, hash binding, coverage, calibration enforcement, and runtime isolation. They do not establish the model's translation accuracy. Only a live, calibrated workflow run can produce the automatic semantic approval described here. The result is machine verification of a translation, not human review, a provenance-tier upgrade, or a proof of the scientific claims.
