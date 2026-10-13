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

# Dorau–Much (PRL 2026): modular relative entropy as a conditional GR-selection bridge

Date: 2026-10-13. Research note; AI-assisted; noncanonical. Source: Philipp Dorau and Albert Much, "From Quantum Relative Entropy to the Semiclassical Einstein Equations," Physical Review Letters **136**, 091602 (published March 2, 2026), DOI: https://doi.org/10.1103/lmq8-nsty ; arXiv:2510.24491v3 https://arxiv.org/html/2510.24491v3 .

## Audit: proved step and independent input

The authors use algebraic QFT and modular theory for a **minimally coupled scalar Klein–Gordon field**, a quasifree Hadamard reference state, and its **coherent excitation** on a local Rindler / bifurcate Killing horizon (in the local Minkowski approximation). They compute the Araki–Uhlmann relative entropy as a weighted expectation value of null energy flux, schematically

 S_rel(vac||coh) = -2*pi ∫_{horizon wedge} U < :T_UU: >_coh dU dA.

Exact coordinate and sign conventions matter (U is negative on the selected wedge). The area-variation proportionality is a **separate input**: delta A = (alpha / 2*pi) S_rel. An area response via Raychaudhuri's equation plus the requirement for every local null direction gives R_ab k^a k^b = alpha <T_ab> k^a k^b. Bianchi identity plus conservation then yield

 G_ab + Lambda g_ab = alpha <T_ab>.

The Newton normalization alpha=8*pi in gravitational natural units uses the Bekenstein–Hawking coefficient S_rel=delta A/4; alpha and Lambda are not predicted by scalar relative entropy alone. Physical units restore G and hbar as appropriate. This is a conditional quantum-informational derivation of **semiclassical** GR, not a first-principles construction of an independent quantum-gravity microtheory.

Source exact: article Eqs. (12), (13), (20), (22), (25)–(28). The authors explicitly restrict proof to coherent states and describe it as a leading-order argument needing higher-order control.

## New UBT observation: metric-only scalar entropy cannot select connection stabilizers

Suppose the UBT Lorentz-real branch has V, omega and invertible e=s^-1 D_omega V, defining g[e]. Let omega'=omega+C with C V=0. Then e'=e and g'=g.

**Conditional proposition.** Assume the local scalar QFT algebra, its reference/coherent states, the horizon regions and its modular dynamics are defined **solely from the metric background g and identical scalar initial/state data**; suppose the scalar is minimally coupled using the metric Levi-Civita derivative, *not* omega. Then

 S_rel[g, scalar states; omega'] = S_rel[g, scalar states; omega]

since every input to the relative-entropy functional is unchanged. The horizon cross-section areas and null Levi-Civita focusing are likewise unchanged. Therefore the Dorau–Much scalar information/area principle **cannot** distinguish, fix or make physical the 12 pointwise stabilizer connection components identified in the sibling UBT audits. This result is kinematical and does not depend on a proposed gravitational action.

The hypothesis of metric-only scalar matter is crucial: if scalar/matter observables or states depend on spin/connection torsion, the conclusion need not hold. Also the number 12 is a pointwise count on a non-null V patch, not particle degrees of freedom.

## Implications for a viable UBT programme

1. Derive or independently motivate a quantum *local observable net*, state family, and modular flow for UBT Theta or justified matter degrees of freedom. The finite algebra Mat_2(C) *by itself* is not a local type-III QFT observable algebra, and does not automatically have vacuum modular horizon entropy.
2. Establish the horizon-area response delta A as a **theorem** of these states and composite geometry; do not import delta A/4G silently while claiming to have derived G or gravity.
3. Choose explicitly whether matter sectors couple to (i) g alone or (ii) full Lorentz/biquaternion connection. For choice (i), relative entropy cannot resolve C; for (ii) determine connection-sensitive modular observables and check positivity, covariance and null limit.
4. Raychaudhuri's geometric derivation assumes the usual torsion-free Levi-Civita null focusing. A torsionful UBT branch must derive when this metric null focusing law applies, rather than replacing curvature tensors without justification.
5. Do not infer global flatness from S_rel=0. Vacuum Einstein equations permit nonflat Ricci-flat geometries; at nonzero Lambda, even Ricci curvature need not vanish. The article's statement is local within its Minkowski expansion.

## Relation to operator-first work

This gives a useful **infrared consistency target** for UBT: *if* UBT recovers the standard metric+scalar QFT+horizon regime and derives a universal area response, its effective geometry should satisfy the semiclassical Einstein equation. It does NOT solve GAP-B-MASTER, uniquely choose Omega, determine Newton's constant from microphysics, or prove healthy spin-2 propagation.

Next proof gate: build a Theta-specific local algebra and metric/connection coupling table; examine whether modular relative entropy depends on the stabilizer C. If not, the information route can constrain the metric IR equations but not the connection-selection gap.

Status: sourced related-work analysis and new conditional no-go for connection selection; not promoted to UBT dynamics.
