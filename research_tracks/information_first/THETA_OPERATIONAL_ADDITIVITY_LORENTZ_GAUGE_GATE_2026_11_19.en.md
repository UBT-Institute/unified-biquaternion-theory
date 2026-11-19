<!-- BILINGUAL-UNIT: theta-operational-additivity-gauge-gate-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional operational algebra; NOT a full-Theta dynamical derivation of Born probabilities or a new canonical metric.
UBT-AI-PROVENANCE-END
-->
# One-Theta information additivity: orthogonal tagging, interference and the Lorentz gauge gate

<!-- UNIT: scope -->
## The meaning of information additivity

The user proposed treating information additivity as a natural UBT principle. This is a useful direction but needs a sharp distinction between independent/orthogonal records and coherent alternatives. The note gives a NEW explicit full-Theta gauge compatibility test, reusing the previously merged conditional density uniqueness theorem. No change to the locked full biquaternion field, sharp metric or complex time.

<!-- UNIT: statement -->
## Conditional additive channel principle

The **user-motivated information principle** must be made more precise than "all information adds." For Shannon information,
\[
H(A,B)=H(A)+H(B)-I(A;B),
\]
so even classical information is simply additive only for independent subsystems \(I(A;B)=0\). Coherent amplitudes satisfy
\[
\boxed{|a+b|^2=|a|^2+|b|^2+2\operatorname{Re}(a^*b).}\tag{A}
\]
The cross term must survive when alternatives are coherently recombined. Therefore the prior theorem applies to **orthogonally tagged, unobserved** channels, not indiscriminately to all quantum alternatives.

In the previously declared candidate observer frame \(N\), let the **one original full biquaternion** be represented as \(T_N=N^{-1/2}\Theta N^{-1/2}=[v_1\ v_2]\). Adopt the conditional operational readout principle:
\[
\boxed{Q([v_1\ v_2])=q(v_1)+q(v_2),\qquad
Q(TV)=Q(T)\;(V\in U(2)),}\tag{B}
\]
where \(V\) changes only the **unresolved right-channel label** in this observer protocol, \(q\) is positive, unitarily equivariant on the observed output, and \(\operatorname{ran}q(v)\subseteq\operatorname{span}\{v\}\) (no signal in an output channel unsupported by its amplitude). The prior exact channel-splitting proof gives \(q(v)=c\,vv^\dagger\) with \(c>0\): writing \(q(v)=h(s)vv^\dagger/s\), \(s=v^\dagger v\), mixing \([v\ 0]\) by an arbitrary right unitary enforces \(h(x+y)=h(x)+h(y)\), and nonnegative additivity forces \(h(s)=cs\). Therefore
\[
Q(T_N)=c\,T_NT_N^\dagger,\qquad
\rho_N=\frac{T_NT_N^\dagger}{\operatorname{tr}(T_NT_N^\dagger)}.\tag{C}
\]
This is a mathematically sufficient CONDI­TIONAL theorem. It does not prove that the right index of \(\Theta\) is a physically unobserved subsystem, that a detector implements this decomposition, or that measurements obey the postulated effect rules. Crucially the right \(U(2)\) invariance is NOT automatically a physical gauge symmetry of \(\Theta\).

<!-- UNIT: interference -->
## Two-channel phase erasure keeps interference

An exact two-channel example shows why orthogonal coarse-graining and coherent phase recombination must be distinguished. Choose in a fixed observer frame
\[
v_1=\begin{pmatrix}1\\0\end{pmatrix},\quad
v_2=\begin{pmatrix}1\\1\end{pmatrix},\quad
T_\phi=[v_1\ e^{i\phi}v_2].
\]
The unobserved right-channel Gram response is independent of \(\phi\):
\[
\boxed{
Q_{\rm unres}=T_\phi T_\phi^\dagger=
\begin{pmatrix}2&1\\1&1\end{pmatrix}.
}\tag{D}
\]
But if a hypothetical, coherently calibrated detector **erases the tag before evaluating its output amplitude**, the output vector is proportional to \(w_\phi=v_1+e^{i\phi}v_2\). Then
\[
\boxed{
w_0w_0^\dagger=\begin{pmatrix}4&2\\2&1\end{pmatrix},
\qquad
w_\pi w_\pi^\dagger=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
}\tag{E}
\]
The phase is invisible in (D) but observable in the coherent comparison (E). This is textbook two-path interference/which-way algebra in the specific full-biquaternion matrix representation; **the existence of an admissible UBT tag-eraser detector is not derived**. Equation (E) is not an instruction to add quantum alternatives incoherently or to identify a random measurement outcome with \(\phi\)-rotation.

<!-- UNIT: geometry -->
## Observer right-channel symmetry is not automatically a geometry gauge

The decisive UBT-specific gate is whether the operational \(T\mapsto TV\) invariance can be imposed on the fundamental field without violating the **locked** canonical real Lorentz tetrad. Take a strict affine kinematic reference
\[
E_\mu=(iI_2,i\sigma_1,i\sigma_2,i\sigma_3),\qquad
g_{\mu\nu}=\eta_{\mu\nu},\qquad V=i\sigma_3\in SU(2).
\]
As a right change of the full matrix, \(V\) is unitary and determinant-one, so the **observer Gram** is unchanged:
\[
(TV)(TV)^\dagger=TT^\dagger.
\]
For a constant homogeneous right first-jet transform \(E_\mu'=E_\mu V\), the sharp central metric is ALSO unchanged:
\[
g[E']=g[E].
\]
Nevertheless
\[
\boxed{E'_0=iI_2(i\sigma_3)=-\sigma_3,\quad
E'_0{}^\dagger=E'_0\ne-E'_0.}\tag{F}
\]
Thus the right-\(SU(2)\) observer-channel relabeling can EXIT \(W_L=i\mathrm{Herm}_2\), despite leaving the metric and Gram response unchanged. It is **not** a demonstrated exact physical gauge redundancy of the canonical UBT geometry. In the canonical Lorentz sector the allowed frame transformations instead have the linked form \(E_\mu\mapsto L E_\mu L^\dagger\) (up to the discrete sign discussed in prior research); they need not act as an arbitrary independent right mixing.

This is an exact **off-shell algebraic obstruction** against silently promoting the partial trace/right-channel ambiguity to a microscopic UBT symmetry. It does NOT forbid a real physical detector from being insensitive to the right channel, nor does it forbid a different dynamical or coupled transformation that preserves the real tetrad. It isolates precisely the missing physical premise.

<!-- UNIT: decision -->
## Unfinished microscopic physics and next exact gate

Reverse engineering target, not a new locked axiom:

1. From the one-Theta microscopic action and the admissible Lorentz-real jet, identify a causal observer measurement algebra and an intrinsic positive form (explaining \(\dagger\) relative to the complex-bilinear \(\sharp\)).
2. Show that the observer can operationally ignore an **orthogonal channel tag**, while relative biquaternion phases remain available to coherent multi-reference comparisons, with dynamically selected physical transport and nondegenerate metric.
3. Derive physical detector support and unnormalized additivity by a local conservation/composition law. Do not conflate it with Shannon entropy additivity for correlated systems or the statement that quantum amplitudes have no interference.
4. Derive the positive effect algebra/probability functional and the measurement instrument from the actual dynamics; the unique trace density representation is conditional on these premises, not a microscopic derivation of Born's law.
5. Test observer Lorentz covariance and gravitational Hamiltonian constraints, as well as imaginary-time \(\psi\) stability, before promoting the channel model to the canonical theory.

The prior general algebraic uniqueness proof is \`research_tracks/information_first/THETA_DENSITY_REVERSE_PRINCIPLE_2026_11_19.en.md\` (already merged). This note adds the nontrivial physical distinction between **observer coarse-graining** and **fundamental gauge**, together with an exact coherent phase witness. Locked definitions: \`canonical/AXIOMS.md\`. Additional precedents: \`research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md\`; \`research_tracks/T1_GR/gr_full_biquaternion_multirotation_2026_11_19.en.md\`. Test: \`tools/verify_theta_operational_channel_reality_gate_2026_11_19.py\` (exact SymPy, locally PASS). Full dynamics and objective collapse remain OPEN.
