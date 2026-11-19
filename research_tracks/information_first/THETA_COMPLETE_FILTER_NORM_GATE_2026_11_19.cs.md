<!-- BILINGUAL-UNIT: theta-complete-filter-norm-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional finite invariant-form theorem; genuine UBT detector, Hilbert structure and Born instrument are not derived.
UBT-AI-PROVENANCE-END
-->
# Aditivita pozorovatelské informace vybere kvadratickou normu mezi Lorentzovsky kovariantními možnostmi

<!-- UNIT: scope -->
## Proč kovariance pozorovatele jednoznačně neurčí normu pravděpodobnosti

Navazujeme na odvození hustoty jediného Theta, matematickou purifikaci a test pozorovatelnosti fází. Cílem je minimální a průhledný operační princip *aditivity* a odvození relativních vah skalární a quaternionové amplitudy bez jejich náhodného dosazení.

<!-- UNIT: covariance -->
## Kovariance Lorentzova rámce připouští dvě nezávislé kladné váhy

The already declared one full biquaternion yields an observer-normalized faithful matrix \(T_N=N^{-1/2}\Theta N^{-1/2}\). Its transformation under simultaneous UBT proper Lorentz-frame and observer changes is **conjugation** by a unitary matrix \(U\in SU(2)\):
\[
T_N\longmapsto U T_N U^\dagger.
\]
We ask whether this covariance ALONE picks the positive response \(\operatorname{tr}(T_N^\dagger T_N)\). It does NOT. Expand
\[
T_N=t_0 I_2+\sum_{k=1}^3 t_k\sigma_k,\quad t_\mu\in\mathbb C.
\]
Under \(U T_NU^\dagger\), \(t_0\) is invariant and the complex triplet \(t_k\) transforms by a real rotation in \(SO(3)\). Scalar and triplet are inequivalent irreducible complex \(SU(2)\)-modules. Thus the most general spin-conjugation-invariant positive Hermitian quadratic form is
\[
\boxed{
h_{\alpha,\beta}(T_N)=2\alpha|t_0|^2+
2\beta\sum_{k=1}^3|t_k|^2,\qquad\alpha,\beta>0.}\tag{A}
\]
The first coefficient weights the scalar singlet and the second the quaternionic triplet. Therefore neither covariance nor positivity alone fixes the ratio \(\alpha/\beta\). The usual Hilbert–Schmidt norm corresponds exactly to \(\alpha=\beta\):
\[
\operatorname{tr}(T_N^\dagger T_N)
=2\big(|t_0|^2+\sum_k|t_k|^2\big).\tag{B}
\]
These are observer-positive quadratic forms, NOT replacements for the locked central sharp metric \(g_{\mu\nu}I_2=\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)\).

<!-- UNIT: completeness -->
## Aditivita úplného ortogonálního měření vybere standardní normu

We can now turn the user's **additivity of information** into a SHARP operational selection criterion that does not require promoting right \(U(2)\) to a fundamental geometric gauge.

Suppose that, for a physically realizable and LOSSLESS complete binary orthogonal filter \(P=P^\dagger=P^2\), the two detector responses are computed by the SAME positive quadratic form on the filtered amplitudes \(PT\) and \((I_2-P)T\). Assume **unnormalized response conservation under exhaustive alternative outcomes**:
\[
\boxed{h(T)=h(PT)+h((I_2-P)T).}\tag{C}
\]
This expresses additive recorded intensity/response for **orthogonal final detector outcomes**, NOT additivity of coherent alternatives in one identical output. It is a specific quantum-instrument/detector assumption, not yet a consequence of the one-Theta Euler equations.

Take the simplest allowed test \(T=I_2\) and \(P=\operatorname{diag}(1,0)=\tfrac12(I_2+\sigma_3)\). The candidate invariant form (A) yields
\[
\boxed{
h_{\alpha,\beta}(I_2)=2\alpha,\quad
h_{\alpha,\beta}(P)=h_{\alpha,\beta}(I_2-P)=\frac{\alpha+\beta}{2}.}\tag{D}
\]
Equation (C) now enforces
\[
2\alpha=\alpha+\beta\quad\Longrightarrow\quad
\boxed{\alpha=\beta.}\tag{E}
\]
Conversely for \(\alpha=\beta\) the condition holds for ALL \(T\in M_2(\mathbb C)\) and ALL orthogonal projectors \(P\), because
\[
\operatorname{tr}(T^\dagger T)=
\operatorname{tr}(T^\dagger P T)+
\operatorname{tr}(T^\dagger(I_2-P)T).
\]
Therefore **positivity + observer spin covariance + additive exhaustive orthogonal filtering** uniquely select the positive Hilbert–Schmidt quadratic norm up to an irrelevant overall constant. The separate stronger unresolved right-\(U(2)\) invariance would also imply \(\alpha=\beta\) using \(I_2\mapsto i\sigma_3\), but such an invariance need NOT be promoted to physical gauge; the filter criterion isolates the operational assumption more cleanly.

For instance \(\alpha=2,\beta=1\) would give the total fraction \(\{h(P)+h(I-P)\}/h(I)=3/4\), contradicting the assumed completeness of the two detector channels. This is exact algebra, not an empirical measurement of UBT.

<!-- UNIT: decision -->
## Fyzikální předpoklady, Bornův tvar a další dynamický test

Combining the selected quadratic response with the CONDITIONAL partial-trace construction in the accompanying \`THETA_PURIFICATION_COMPOSITION_GATE_2026_11_19.en.md\` yields
\[
Q_N=T_NT_N^\dagger,\qquad
\rho_N=\frac{Q_N}{\operatorname{tr}Q_N},
\]
and for an assumed positive effect \(0\le M\le I_2\) with a chosen linear filter \(K^\dagger K=M\),
\[
\boxed{
\frac{h(KT_N)}{h(T_N)}
=\operatorname{tr}(\rho_N M).
}\tag{F}
\]
This is a CONDITIONAL reconstruction of Born-form RESPONSE fractions using orthogonal outcome additivity. It still assumes an observer-selected positive inner product, physically meaningful matrix filters \(T\mapsto KT\), and experimental probabilities proportional to those responses. The microscopic action has not selected them, and no stochastic unique-outcome law or objective quantum collapse follows.

The theorem sharpens the remaining fundamental UBT question: can the ordinary single-\(\Theta\) local action yield an observer-positive CONSERVED detector response with a genuinely complete orthogonal decomposition, respecting the canonical Lorentz-real jet, Hamiltonian constraints, and phase/complex-time sector? This is a dynamical conservation/measurement problem, NOT a task of choosing ad hoc normalization constants.

Exact finite symbolic regression: tools/verify_theta_complete_filter_norm_gate_2026_11_19.py. Canonical sources: canonical/AXIOMS.md and prior research_tracks/information_first/THETA_DENSITY_REVERSE_PRINCIPLE_2026_11_19.en.md. Research tier C_working; no locked axiom modification.
