<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: psi-weak-multiplicity.provenance -->
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

# Opposite psi-winding modes: a conditional weak-multiplicity obstruction

**Status: exact conditional calculation; not a finalized UBT action or physical weak gauge theory.** This tests a proposed explanation of the hypothetical weak carrier in merged PR #702 using the existing complex-time fiber.

## 1. Restricted complex mode pair

On a fixed Lorentz background select one constant complex biquaternion polarization Y and opposite nonzero Fourier modes. The two amplitudes are independent only **if** the chosen reality and dynamical constraints permit them. They are not assumed to solve the final UBT field equations.

\[
X(x,\psi)=Yf(x,\psi),\quad
f(x,\psi)=u(x)e^{in\psi/R_\psi}+v(x)e^{-in\psi/R_\psi},\quad n\ne0.
\]

\[
A=|u|^2,\quad B=|v|^2,\quad
\langle|f|^2\rangle_\psi=A+B,\quad
\langle|\partial_\psi f|^2\rangle_\psi=\frac{n^2}{R_\psi^2}(A+B).
\]

## 2. Quartic SU(2) symmetry test

The quadratic mode norms are equal in a parity-even free model, but that fact does not imply an interacting gauge group. Exact circle averaging of a local quartic produces a mixed coefficient different from the invariant quartic of a single unitary doublet. The explicit rotation preserves the free norm yet changes the quartic.

\[
\boxed{\langle|f|^4\rangle_\psi=A^2+4AB+B^2=(A+B)^2+2AB.}
\]

\[
U=\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}\in SU(2),\quad
\mathcal Q(1,0)=1,\quad \mathcal Q\left(U\binom10\right)=\frac32.
\]

## 3. Existing classified UBT potential

The existing derivative-free invariant classification, without any newly postulated action, reduces the quartic to the listed independent invariants. Scalar polarization factorization gives two explicit witnesses. Requiring the mode-only SU(2) action on every unrestricted complex polarization forces both quartic coefficients to vanish. A special sector may still cancel; this is not a theorem on the Hermitian reality-restricted branch or on an unknown composite action.

\[
H(X)=\operatorname{Tr}(X^\sharp X^\dagger),\quad
V_4(X)=\lambda_1 H(X)^2+\lambda_2|\det X|^2.
\]

\[
H(fY)=|f|^2H(Y),\quad|\det(fY)|^2=|f|^4|\det Y|^2,\quad
\langle V_4(fY)\rangle_\psi=Q_Y\mathcal Q(u,v),\quad
Q_Y=\lambda_1H(Y)^2+\lambda_2|\det Y|^2.
\]

\[
Y_1=I_2:\quad H(Y_1)=2,\quad|\det Y_1|^2=1,\quad Q_{Y_1}=4\lambda_1+\lambda_2.
\]

\[
Y_2=\operatorname{diag}(1,i):\quad H(Y_2)=0,\quad|\det Y_2|^2=1,\quad Q_{Y_2}=\lambda_2.
\]

\[
Q_{Y_1}=Q_{Y_2}=0\Longleftrightarrow \lambda_1=\lambda_2=0.
\]

## 4. Translation-compatible weak symmetry

If an independent internal weak symmetry is required to commute with every circle translation, distinct opposite winding weights disallow their mixing. The commuting unitary transformations form a diagonal torus, not a full weak doublet group. Symmetries that intentionally do not commute with circle translation fall outside this conditional no-go.

\[
T_\alpha=\operatorname{diag}(e^{in\alpha/R_\psi},e^{-in\alpha/R_\psi}),\quad
P_\psi=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
P_\psi T_\alpha P_\psi=T_\alpha^{-1}.
\]

\[
M=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad
[M,\sigma_3]=\begin{pmatrix}0&-2b\\2c&0\end{pmatrix},\quad
[M,T_\alpha]=0\;\forall\alpha\Longrightarrow b=c=0.
\]

## 5. Fiber parity versus physical chirality

For the raw Lorentz-four-vector representation, the commutant of its boost and rotation generators is scalar. Adding opposite circle modes provides copies of the same Lorentz representation, not inequivalent left- and right-handed Weyl-spinor representations. Thus fiber reflection eigenstates are not by themselves gamma-five eigenspinors.

\[
\operatorname{End}_{\operatorname{Spin}(1,3)}(\mathbb C^4)=\mathbb C I_4,\quad
\operatorname{rank}\mathscr C_{\rm Lorentz}=15,\quad
\dim_{\mathbb C}\ker\mathscr C_{\rm Lorentz}=1.
\]

\[
\operatorname{End}_{\operatorname{Spin}(1,3)\times U(1)_\psi}
\left(\mathbb C^4\otimes(\mathbb C_{+n}\oplus\mathbb C_{-n})\right)
\simeq\mathbb C\oplus\mathbb C.
\]

## 6. Verdict and next dynamical test

**Proved under stated fixed-background and restricted-representation assumptions:** the exact quartic counterexample, translation commutant and Lorentz-vector commutant. **Still open:** the full physical constrained Theta Hessian, emergence of the weak multiplicity and physical chiral Weyl fermions. Composite collective sectors, nonlocal redefinitions, broken translation and nonminimal dynamics are not excluded. The phase-metric compatibility problem in draft PR #701 is separate. This result must not be promoted to fundamental action closure.

Verifier: tools/verify_psi_mode_weak_obstruction.py. Regression: tests/test_psi_mode_weak_obstruction.py. Grounding: canonical/ACTION.en.md, research_tracks/action_selection/theta_potential_invariants.en.md, canonical/chirality/step1_psi_parity.tex, research_tracks/T2_GAUGE/su3_su2_even_fock.en.md.

<!-- BILINGUAL-UNIT: psi_weak_multiplicity.verification -->

## Verification

Artifact: `tests/test_psi_mode_weak_obstruction.py`; 2 tests. Python 3.12; SymPy 1.14.0. 19 exact checks and 50 independent circle quadratures with 128 points; tolerance 1e-11. Analytic assumptions and scope are stated above. The encoded checks do not select a physical UBT action or prove its field equations. `LEAN-PENDING`: Lean is not installed in this runtime; no checked Lean proof is supplied. English is the translation source. Structural equality is machine-checked; human semantic review is not attested by this record.
