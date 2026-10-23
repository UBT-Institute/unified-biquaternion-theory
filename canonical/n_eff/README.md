<!-- © 2025–2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# N_eff status — current authoritative split

**Current status (2026-10-10): do not use a single unqualified \(N_{\rm eff}\).**

The repository contains two distinct quantities:

1. **Direct loop count**
   \[
   N_{\rm eff}^{\rm loop}=3
   \]
   for the minimal charged complex-scalar sector explicitly present in the
   audited kinetic action.  This is the count relevant to a direct one-loop
   vacuum-polarization coefficient unless additional propagating charged modes
   are independently derived.

2. **SU(2)-twist count**
   \[
   N_{\rm eff}^{\rm twist}=12
   \]
   in the separate Scherk--Schwarz/twist route.  This is an [L1] result for
   that route, but its identification with the direct loop count is **OPEN**.

Authoritative reconciliation:
- \`canonical/n_eff/step2_AUDIT.tex\`
- \`canonical/n_eff/neff_reconciliation.tex\`

Historical files \`step1_mode_decomposition.tex\`,
\`step2_vacuum_polarization.tex\`, and \`step3_N_eff_result.tex\` retain the
older stronger \(N_{\rm eff}=12\) wording for provenance.  They must not be
cited as proving
\[
N_{\rm eff}^{\rm loop}=12.
\]

For the October 2026 SU(3) induced-coupling benchmark, the coset calculation
starts from **one complex fundamental triplet**, not from the historical
unqualified value 12.  Any enhancement \(N_{\rm eff}>1\) must be derived from
an actual charged spectrum/tower and its Hessian.

## Legacy summary

Earlier work used the shorthand
\[
12=3\times2\times2
\]
for three phase directions, two helicity/twist states, and two charge sectors.
The later audit showed that these factors cannot all be multiplied into the
minimal scalar loop coefficient without an additional physical derivation.

The distinction is now mandatory throughout UBT.
