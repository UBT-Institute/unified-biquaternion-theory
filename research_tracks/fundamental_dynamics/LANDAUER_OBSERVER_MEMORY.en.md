<!-- BILINGUAL-UNIT: landauer.scope -->
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


# Landauer erasure and finite observer records

Status: **research proposal; OPEN**, 2026-11-09. This extends the information-first selector with thermodynamic admissibility, not a new canonical axiom. Memory and reservoir are effective subsystems, not extra fundamental UBT fields. The single biquaternionic field, complex time, two-sided covariant derivative, tetrad and central anticommutator metric remain unchanged. No consciousness ontology, unique action, ghost cure or quantum emergence is derived.

<!-- BILINGUAL-UNIT: landauer.observer -->

## Operational observer and records

An observer is specified by an accessible observable algebra, finite memory M, allowed protocols and environmental access. For a classical source label X, distinguish memory entropy H(M), retained information I(X;M), and uncertainty H(X|M). A reset can lower H(M) while increasing H(X|M). These are not the thermodynamic entropy of the entire observer. The source label is a diagnostic variable, not an assumption that all observers share a global hidden state. A finite memory of dimension d can retain at most log(d) nats of classical information. Continued acquisition of independent records requires compression where possible, export, erasure, or stopping; there is no universal heat price per measurement.

<!-- BILINGUAL-UNIT: landauer.balance -->

## Thermal balance with explicit assumptions

Use finite-dimensional density operators and natural logarithms, so S is dimensionless. Assume a reservoir R with fixed Hamiltonian H_R, positive finite temperature T, an initially thermal marginal, and unitary joint evolution U. Work supplied by the controller is allowed; reservoir energy gain Q_R is not automatically total work. These are local effective quantum-thermodynamic assumptions, not a derivation of quantum mechanics or of a global state for all observers.

\[
S(\rho)=-\operatorname{Tr}\rho\ln\rho,\quad
\beta=(k_{\rm B}T)^{-1},\quad
\gamma_R=Z^{-1}e^{-\beta H_R},\quad
\rho_R^i=\gamma_R,\quad \rho_{MR}^f=U\rho_{MR}^i U^\dagger,
\quad Q_R=\operatorname{Tr}[H_R(\rho_R^f-\gamma_R)].
\]

<!-- BILINGUAL-UNIT: landauer.identity -->

## Entropy identity and the reset limit

Define D as quantum relative entropy and I as mutual information. Unitary entropy conservation gives Delta S_M + Delta S_R = I_f - I_i. The Gibbs identity gives beta Q_R = Delta S_R + D(rho_R^f || gamma_R). Combining them yields the displayed equality. For an initially uncorrelated memory and reservoir, I_i vanishes and both remaining correction terms are nonnegative, recovering the Landauer bound. This is standard information thermodynamics [1], reused here, not a new UBT theorem.

\[
D(\rho\Vert\sigma)=\operatorname{Tr}\rho(\ln\rho-\ln\sigma),\qquad
I(M:R)=S_M+S_R-S_{MR},\qquad \Delta S_M=S_M^f-S_M^i,
\]
\[
\boxed{\beta Q_R=-\Delta S_M+I_f(M:R)-I_i(M:R)+D(\rho_R^f\Vert\gamma_R).}
\]
\[
\rho_{MR}^i=\rho_M^i\otimes\gamma_R
\quad\Longrightarrow\quad Q_R\ge k_{\rm B}T(S_M^i-S_M^f).
\]

<!-- BILINGUAL-UNIT: landauer.limits -->

## Limits, correlations and global information

For an initially uniform bit and ideal pure reset, the entropy decrease is ln(2), giving Q_R >= k_B T ln(2) under the product-state assumptions. A biased bit has a different entropy; a permitted reset error leaves residual entropy. An exact pure reset of a full-rank memory with a finite full-rank thermal reservoir is impossible by a unitary, because rank is preserved; the ideal limit must not be claimed as achieved by the finite example. The thermal SWAP below only performs partial erasure. Initial correlations, accessible side information and nonthermal resources require explicit accounting; do not add independent per-observer costs when records or reservoirs are correlated.

<!-- BILINGUAL-UNIT: landauer.gluing -->

## Compatibility after losing records

Within a declared finite classical diagnostic, let p_a be context distributions and r_a the marginal maps from a candidate joint distribution P. Define the extension set below without assuming it is nonempty or unique. This classical joint model is not imposed on incompatible quantum observables. If a common stochastic map C on the joint records induces consistent local maps C_a, every old extension pushes forward to an extension of the erased records. Thus erasure cannot invalidate an existing extension in this setup, but it can hide an incompatibility or merge distinct candidate histories. The converse does not follow: compatibility after erasure proves neither prior compatibility nor a unique physical world.

\[
\mathcal G(p)=\{P\ge0:\ \sum P=1,\ r_aP=p_a\ \forall a\},\qquad
r'_a C=C_a r_a\quad\Longrightarrow\quad
C\mathcal G(p)\subseteq\mathcal G((C_ap_a)_a).
\]

<!-- BILINGUAL-UNIT: landauer.examples -->

## Two diagnostic examples

First, equal mixtures of records (0,0),(1,1) and of records (0,1),(1,0) have identical individual marginals but opposite correlations. Comparing both records distinguishes them; resetting the second record maps both distributions to the same output. Second, the pairwise requirements A=B, B=C and A!=C, each with uniform bit marginals, have no joint classical distribution despite agreeing on overlaps. Resetting B removes the first two constraints and leaves a compatible A!=C model. This is information loss in a toy model, not evidence that inconsistent worlds exist physically. Without new input, data processing prevents a local reset from improving distinguishability; new measurements or access to environmental records change that premise.

<!-- BILINGUAL-UNIT: landauer.principle -->

## Addition to the information principle

Proposal: restrict allowed observer protocols by finite memory, causal access and a thermodynamic resource ledger before attempting to infer dynamics from record consistency. For each reset satisfying the uncorrelated thermal assumptions, define Sigma_a below. A specified heat budget gives a necessary entropy-reduction budget, not a sufficient realizability criterion. No entropy minimization action or saturation of the bound is postulated. Joint accounting replaces the sum when resources are correlated.

\[
\Sigma_a=\Delta S_{M_a}+\beta_a Q_{R_a}\ge0,\qquad
\sum_a Q_{R_a}\le Q_{\max}
\quad\Longrightarrow\quad
\sum_a k_{\rm B}T_a(S_{M_a}^i-S_{M_a}^f)\le Q_{\max}.
\]

<!-- BILINGUAL-UNIT: landauer.bridge -->

## Open UBT bridge and falsification

OPEN: derive memory states, reservoir coupling, temperature and physically allowed comparison channels from the unchanged Theta architecture. Derive their resource balance and reduced dynamics without replacing the canonical metric by Fisher information. A protocol violating the thermal identity under its actual hypotheses is rejected; an apparent violation with initial correlations is not. Passing the ledger does not select a unique Hamiltonian: the identity holds for every joint unitary with the stated initial reservoir. Distinct worlds remain an unselected interpretation, not a result. The added constraint sharpens the information principle but closes no canonical dynamics gap.

<!-- BILINGUAL-UNIT: landauer.verification -->

## Verification and related work

The companion test checks the balance numerically for coherent memory states and partial SWAP interactions, a correlated zero-heat reset, and exact finite classical record examples. Symbolic substitution independently checks the entropy-balance algebra. This does not verify physical realizability in UBT or prove the general quantum entropy inequalities. LEAN-PENDING: no Lean executable is available and no formal entropy proof is supplied. Independent bilingual semantic review remains pending before merge. Tool versions and actual results are recorded in reports/landauer_observer_memory_2026_11_09.json. The English edition is the translation source; both editions carry the same claims.


- [1] Reeb & Wolf, *An improved Landauer principle with finite-size corrections*, New J. Phys. 16, 103011 (2014), https://doi.org/10.1088/1367-2630/16/10/103011 ; https://arxiv.org/abs/1306.4352 .
- [2] Bérut et al., *Experimental verification of Landauer’s principle linking information and thermodynamics*, Nature 483, 187–189 (2012), https://doi.org/10.1038/nature10872 .
