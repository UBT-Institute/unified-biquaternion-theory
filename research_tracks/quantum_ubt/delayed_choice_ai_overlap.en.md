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

# AI-controlled delayed-choice interference: conditional overlap model and UBT gaps

**Date:** 2026-10-16 · **Authors:** UBT Institute research working draft (AI-assisted; author review pending).

<!-- UNIT: DC-01 -->
## 1. Scope and claim status

**Status: RESEARCH TRACK / DERIVED_WITH_ASSUMPTIONS (mathematics), OPEN_GAP (UBT-to-photon and measurement dynamics).** This note does **not** derive Born's rule, objective collapse, branching universes, or an observer-consciousness coupling from UBT. It does **not** assert a novel quantitative UBT prediction. The deterministic checker verifies only standard Hilbert-space algebra.

The canonical single-field carrier remains \(\Theta(q,\tau)\in\mathbb C\otimes\mathbb H\) with \(\tau=t+i\psi\). Treat \(\psi\) as an auxiliary/internal coordinate in the stated compact-mode ansatz; do not modify the locked covariant-tetrad metric or average its definition over the fiber. The unique full fundamental action and quantum reduction are not finalized.

<!-- UNIT: DC-02 -->
## 2. Explicit assumptions and two-path mode expansion

Assume (H1) a balanced two-path interferometer; (H2) a chosen positive, normalized Hilbert–Schmidt pairing on the internal mode amplitudes, using the \(2\times2\) complex-matrix representation of biquaternions; (H3) ordinary Born probabilities and unitary beam splitters as external benchmark rules; (H4) periodic internal coordinate \(\psi\) with radius \(R_\psi>0\); and (H5) a laboratory photon-to-\(\Theta\) correspondence **only as an unproved working ansatz**. At fixed external \(q\), write path components:

$$
\Theta_j(t,\psi)=\sum_{n\in\mathbb Z}a_{j,n}(t)\,
\frac{e^{in\psi/R_\psi}}{\sqrt{2\pi R_\psi}},\qquad j\in\{A,B\}.
$$

$$
\langle a,b\rangle=\frac12\sum_n\operatorname{Tr}(a_n^\dagger b_n),
\qquad\langle a,a\rangle=\langle b,b\rangle=1,\qquad
\gamma_\psi=\langle a,b\rangle.
$$

<!-- UNIT: DC-03 -->
## 3. Conditional detector probabilities

Under H1–H5, the closed interferometer has the standard interference law shown below; its phase-scan visibility is \(V\). The open interferometer has equal detector marginals **provided** both arms and detection efficiencies are balanced. These are identities within the assumed benchmark quantum description, **not** consequences of the not-yet-finalized UBT action.

Proof sketch: the output-0 amplitude for each normalized mode is \((a_n+e^{i\phi}b_n)/2\). Expand its squared norm; the two diagonal terms sum to \(1/2\) and the cross terms supply \(\operatorname{Re}(e^{i\phi}\gamma_\psi)/2\). Cauchy–Schwarz yields \(V\le1\).

$$
P(D_0\mid\mathrm{closed},\phi)=
\frac12\left[1+\operatorname{Re}(e^{i\phi}\gamma_\psi)\right],
\quad
P(D_1\mid\mathrm{closed},\phi)=1-P(D_0\mid\mathrm{closed},\phi),
\quad V=|\gamma_\psi|\le1.
$$

$$
P(D_0\mid\mathrm{open})=P(D_1\mid\mathrm{open})=\frac12.
$$

<!-- UNIT: DC-04 -->
## 4. AI, detector memory, and interpretation

An AI controller that selects open/closed configuration after the photon enters the interferometer does not, merely by being AI, modify the above probabilities **conditional on the realized configuration**. Decisions may depend on earlier outcomes; analysis must condition on the actual settings and prevent history- or time-dependent confounds.

If physical apparatus states correlated with paths are \(|E_A\rangle,|E_B\rangle\), then a factorized internal/apparatus model gives the following overlap. The visibility can vanish before any human reads a record when these states are orthogonal. This is standard entanglement/decoherence mathematics; it proves neither objective collapse nor Everett branching and requires no consciousness premise. Nonfactorizing dynamics require the full joint-state overlap rather than this product.

$$
\gamma_{\mathrm{eff}}=\gamma_\psi\langle E_A\mid E_B\rangle
\qquad\text{(only if the internal and apparatus states factorize).}
$$

<!-- UNIT: DC-05 -->
## 5. Illustrative internal-phase candidate (not UBT-specific)

Introduce **a new unproved ansatz** that only path B picks up a winding-dependent shift \(\delta\), with no change in mode magnitudes. The relative overlap follows from mode orthogonality. For equal weights of modes \(n=0,1\), the phase-dependent visibility has the form below. Here \(\delta\) is **not** a derived optical coupling, \(R_\psi\) is **not** fixed, and identical behavior can be engineered in conventional multimode quantum optics. The result alone cannot discriminate UBT from ordinary quantum mechanics.

$$
b_n=a_n e^{in\delta/R_\psi},\qquad
p_n=\tfrac12\operatorname{Tr}(a_n^\dagger a_n),\quad
\sum_n p_n=1,\qquad
\gamma_\psi(\delta)=\sum_n p_n e^{in\delta/R_\psi}.
$$

$$
p_0=p_1=\tfrac12,\quad p_{n\notin\{0,1\}}=0
\quad\Longrightarrow\quad
V(\delta)=\left|\cos\frac{\delta}{2R_\psi}\right|.
$$

<!-- UNIT: DC-06 -->
## 6. Conditional global-holomorphy obstruction

For each complex component \(f(\tau)\) of a declared reduced \(\Theta\) sector, assume entire holomorphy in \(\tau=t+i\psi\), periodicity in imaginary \(\psi\) with period \(2\pi R_\psi\), and a uniform bound for every real \(t\) and \(\psi\). Liouville's theorem forces \(f\) to be constant. Equivalently, nonzero Fourier modes of the displayed analytic form grow in at least one time direction. This is a **conditional no-go for simultaneously imposing all these assumptions**, not a no-go for \(\Theta\) or winding modes generally. The current UBT status limits strict holomorphy to explicitly stated reduced sectors; no global frame-independent holomorphy is asserted.

$$
\partial_{\bar\tau}f=0,\quad f(t+i[\psi+2\pi R_\psi])=f(t+i\psi),
\quad \sup_{t,\psi}|f(t+i\psi)|<\infty
\quad\Longrightarrow\quad f=\mathrm{constant}.
$$

$$
f_n(t,\psi)=c_n e^{n(t+i\psi)/R_\psi}.
$$

<!-- UNIT: DC-07 -->
## 7. Proposed discriminating experiment

Compare (i) an adaptive AI controller, (ii) a deterministic replay of the **same recorded settings and timing** through the same hardware, and (iii) a randomized baseline, with source, optics, losses, phase, environmental coupling, and detection thresholds controlled. The choice must be physically applied only after photon entry; log precise timing and reject invalid trials by preregistered rules. Randomize/blind phase-scan blocks, retain an untouched holdout, and estimate conditional \(P(D_0\mid c,\phi)\) and visibility with confidence intervals. An AI-specific effect requires a reproducible difference **after** matched physical histories and multiple-comparison controls, not an unblinded comparison of aggregate counts. No 'human looking only later' design by itself distinguishes quantum interpretations.

<!-- UNIT: DC-08 -->
## 8. Open gaps and promotion criterion

**OPEN_GAP:** finalize the unique \(\Theta\) action and physical quantum reduction; derive a positive physical Hilbert space and Born probabilities; identify path states \(a_n,b_n\) with measurable photon states; derive any path-dependent phase displacement \(\delta\) and radius \(R_\psi\) **without fitting the target observation**; compute standard-model backgrounds, uncertainties, and a genuine falsifiable deviation. Observer-consciousness coupling, objective collapse, and Everett branching are **not** established in canonical UBT. Until these gaps close this is a benchmark plus research hypothesis, **not** a grant-ready UBT-specific prediction.

**Smallest next step:** derive or rule out a physically observable operator for \(\psi\)-dependent photon–apparatus coupling from the *same* action, with a zero-free-parameter comparison against conventional quantum optics. If no such coupling follows, record that negative result.

<!-- UNIT: DC-09 -->
## 9. Verification and provenance

**Analytic:** direct expansion of two balanced output norms; mode orthogonality; Cauchy–Schwarz; conditional Liouville argument. **Numerical:** \`check_delayed_choice_overlap.py\`, Python standard library, deterministic seed 20261016, 500 randomly normalized complex mode pairs and 401 two-mode phase points; locally executed with PASS on 2026-10-16. The numerical test checks the standard Hilbert-space algebra **only**, not a UBT-derived physical prediction. **LEAN-PENDING:** exact Hilbert-space overlap lemma and the holomorphy no-go have not been formalized/compiled in Lean here. **Human review:** pending, including explicit Czech–English semantic-equivalence approval; exhaustive human review is not claimed. Translation source: English edition.

<!-- UNIT: DC-10 -->
## 10. Anchoring references

- [Canonical action / one-action audit](../../canonical/ACTION.en.md)
- [Canonical \(\Theta\) and tetrad definitions](../../canonical/THEORY/math/fields/theta_field.tex)
- [Complex-time canonical choice](../../canonical/THEORY/complex_time_canonical_choice.tex)
- [Quantum-sector status / open Born-rule gap](../../docs/quantum_sector_status.md)
- [Retracted Born-rule proof — historical audit](../../canonical/qm_emergence/step7_born_rule.tex)
- [Current UBT status, including holomorphy scope](../../STATUS_OF_UBT.md)
- [Provenance policy](../../AI_PROVENANCE.md)
