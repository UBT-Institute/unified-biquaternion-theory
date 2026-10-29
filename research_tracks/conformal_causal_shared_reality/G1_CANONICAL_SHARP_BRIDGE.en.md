<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: g1-canonical-sharp-bridge -->
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

# G1: Canonical sharp anticommutator versus Hermitian Gram metric

**2026-10-29 · PR #809 · C_working · scoped algebraic comparison.** This is not a new UBT action or a proof of gravity. It corrects the potential conflation in G1_COMPLEX_REAL_COFRAME. Fundamental complex Theta is retained throughout; the reality requirement belongs to the physical geometric observable, not to all intermediate field components.

## Exact canonical source [PROVED, repo-grounded]

`canonical/CANONICAL_DEFINITIONS.md`, the `canonical/fields/theta_field.tex` first jet and `canonical/THEORY/canonical/canonical_action.tex` declare the *same* canonical local metric, with fixed global normalization and quaternion-only conjugation sharp:

\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\quad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=g^{\rm can}_{\mu\nu}I_2,\qquad
E_\mu\in i\operatorname{Herm}_2\quad\text{on the declared classical slice}.
\]

The classical i-Hermitian slice is a declared sufficient reality convention, not an algebraic assertion that the underlying complex Theta must be real. The canonical documents explicitly exclude trace/real-part or fiber projection as the *definition* of the local metric.

For any complex matrices of size two, sharp is the linear adjugate, and polarization of the determinant is central **without** taking a real part. The central coefficient can nevertheless be complex:

\[
A^\sharp=(\operatorname{tr}A)I_2-A,\quad
C(A,B):=\tfrac12\operatorname{tr}(A^\sharp B),\quad
\tfrac12(A^\sharp B+B^\sharp A)=C(A,B)I_2.
\]

## The noncanonical Hermitian Gram comparator [PROVED, inequivalent]

The existing G1_COMPLEX_REAL_COFRAME construction instead uses the dagger-dependent real B pairing and a phase-only projected first jet:

\[
B(A,B):=\tfrac12\operatorname{Re}\operatorname{tr}(A^\sharp B^\dagger),
\qquad
g^{\rm trial}_{\mu\nu}=B(U_\mu,U_\nu),
\quad U_\mu=\partial_\mu\Theta-i j_\mu\Theta.
\]

They are inequivalent even before selecting an action. When both jets transform by a common local phase, the canonical bilinear is phase-charged, while the Hermitian Gram is invariant:

\[
C(e^{i\alpha}A,e^{i\alpha}B)=e^{2i\alpha}C(A,B),
\qquad
B(e^{i\alpha}A,e^{i\alpha}B)=B(A,B).
\]

No constant scale/sign can identify them on the full complex carrier:

\[
C(I,I)=1,\quad C(iI,iI)=-1,\qquad
B(I,I)=B(iI,iI)=1.
\]

On the special i-Hermitian classical slice they do agree up to a global sign fixed by the chosen Pauli/metric convention:

\[
C(iA,iB)=-B(iA,iB),\qquad
A,B\in\operatorname{Herm}_2.
\]

Hence the previous algebraically reconstructed real tetrad is a legitimate factorization of the **trial** Gram metric, but does not by itself satisfy the defining canonical equality with the same Theta derivative. A free coframe field must not be silently substituted for the canonical first jet.

## Exact curved-witness mismatch [COUNTEREXAMPLE]

For the previously used complex field, the composite phase connection vanishes at the indicated regular event. Its four phase-covariant jets are:

\[
\Theta_c=(t+2)I+x\sigma_1+y\sigma_2+z\sigma_3
+i\kappa tx\,\sigma_1,\quad
U_\mu|_{(1,0,0,0)}=(I,(1+i\kappa)\sigma_1,\sigma_2,\sigma_3).
\]

The two full metric matrices computed from those *same* jets are:

\[
C(U_\mu,U_\nu)|_p
=\operatorname{diag}(1,-(1+i\kappa)^2,-1,-1),\quad
B(U_\mu,U_\nu)|_p
=\operatorname{diag}(1,-1-\kappa^2,-1,-1).
\]

For the explicit normalization shown, the canonical central metric has an imaginary spatial diagonal component whereas the Gram metric is real:

\[
\kappa=1:\quad C_{tt}=1,\quad C_{xx}=-2i,\quad
B_{tt}=1,\quad B_{xx}=-2.
\]

No single compensating unit phase can make both canonical time and space components simultaneously real in this example. Inserting a uniform factor i into all jets reverses the overall sign of C, but leaves the nonreal spatial entry. There is no claim here that a more general dynamically derived two-sided connection cannot repair the field.

## Algebraic equality and its restricted rigidity [PROVED, exact]

For arbitrary complex first jets split into two Hermitian collections A,Y, the canonical complex metric separates exactly as:

\[
U_\mu=A_\mu+iY_\mu,\quad A_\mu,Y_\mu\in\operatorname{Herm}_2,
\quad C(U_\mu,U_\nu)=
C(A_\mu,A_\nu)-C(Y_\mu,Y_\nu)
+i\{C(A_\mu,Y_\nu)+C(Y_\mu,A_\nu)\}.
\]

By contrast the real Gram metric is the sum of the two real Lorentz pairings. Equality of *both complete complex tensors* is equivalent to two independent constraints:

\[
B(U_\mu,U_\nu)=
C(A_\mu,A_\nu)+C(Y_\mu,Y_\nu),\quad
C(U,U)=B(U,U)
\Longleftrightarrow
\begin{cases}
C(Y_\mu,Y_\nu)=0,\\
C(A_\mu,Y_\nu)+C(Y_\mu,A_\nu)=0
\end{cases}\ \forall\mu,\nu.
\]

When the four Hermitian A jets span the Lorentz vector module, the condition that all Y jets span a totally null subspace forces them into one common null line (Witt index one). The mixed constraint with full-rank A then forces its coefficients to vanish:

\[
\operatorname{rank}\{A_\mu\}_{\mu=0}^3=4,\quad
C(U_\mu,U_\nu)=B(U_\mu,U_\nu)
\quad\Longrightarrow\quad Y_\mu=0\quad\forall\mu.
\]

This does NOT say a real canonical metric requires Hermitian jets; it only says that equality with this distinct dagger Gram tensor is rigid on that specified regular branch. Nontrivial null degeneracies exist if the real A rank is deficient.

## Pure-gradient real-canonical-metric flatness lemma [PROVED, conditional]

Suppose the Lorentz/bimodule connection vanishes, the real Hermitian part X of Theta is a local diffeomorphism, and the canonical metric is exactly real. In the real coordinates given by X the vanishing imaginary part is the ordinary Minkowski Killing equation for Y:

\[
\Theta=X+iY,\quad D=d,\quad
\operatorname{rank}(dX)=4,\quad
\operatorname{Im} C(d\Theta,d\Theta)=0
\quad\Longrightarrow\quad
\partial_aY_b+\partial_bY_a=0
\text{ in coordinates }X^a.
\]

Differentiating and permuting the Killing equations gives the exact differential identity:

\[
\partial_kK_{ij}+\partial_iK_{jk}-\partial_jK_{ki}
=2\partial_i\partial_kY_j,\quad
K_{ij}:=\partial_iY_j+\partial_jY_i,
\quad K_{ij}=0\Longrightarrow\partial_i\partial_kY_j=0.
\]

Therefore Y is a translation plus a constant infinitesimal Lorentz transformation in X coordinates. Its Jacobian is constant; the resulting real canonical metric is constant and, if regular, intrinsically flat:

\[
Y_a(X)=c_a+\omega_{ab}X^b,\quad\omega_{ab}=-\omega_{ba},
\quad
g^{\rm can}=C(dX,dX)-C(dY,dY)
\quad\Longrightarrow\quad R[g^{\rm can}]=0
\text{ wherever the metric is regular}.
\]

An explicit complex gradient that satisfies every assumption is:

\[
\Theta=(tI+x\sigma_1+y\sigma_2+z\sigma_3)
+i\lambda(xI+t\sigma_1),\quad
C(d\Theta,d\Theta)
=\operatorname{diag}(1+\lambda^2,-1-\lambda^2,-1,-1).
\]

This is an obstruction for full-rank X and a frozen zero connection only; it does not cover a rank-deficient real projection, nonzero justified A/B connections, another carrier or a physical action.

## Complex jets can still yield a real canonical metric [PROVED, existence]

An explicit constant complex-Lorentz transformation of an i-Hermitian frame gives complex jets, not themselves in i-Herm, whose canonical metric is exactly real and Minkowskian:

\[
E_0=i(\cos\varphi\,I+i\sin\varphi\,\sigma_1),\quad
E_1=i(i\sin\varphi\,I+\cos\varphi\,\sigma_1),\quad
E_2=i\sigma_2,\quad E_3=i\sigma_3,
\quad C(E_\mu,E_\nu)=\operatorname{diag}(-1,1,1,1).
\]

These jets integrate to an affine complex Theta field at zero connection. This **does not establish** complex Lorentz transformations as a physical UBT gauge group. It establishes the narrower mathematical point: complex Theta and even non-i-Hermitian jets are compatible with a real central canonical metric; reality is a condition on the composite tensor, not a universal component restriction.

## Decision and exact verification [OPEN]

The G1_COMPLEX_REAL_COFRAME note remains a **noncanonical comparator**. A genuinely canonical curved positive result must specify the two-sided derivative DTheta=dTheta+ATheta-Theta B, construct and transform the composite A/B, obtain a real nondegenerate central sharp tensor **using those same jets**, and test independent variations, curvature and the physical spectrum. A right-inverse connection chosen after demanding the target tetrad is not a noncircular derivation. The information and Shared Reality principles remain quantitative selection tests, not a license to replace sharp by dagger.

**Reproducibility:** `python -m unittest discover -s tests -p 'test_theta_canonical_sharp_bridge.py' -v`, 12 exact tests passed locally. Sources: `canonical/CANONICAL_DEFINITIONS.md:164-190`; `canonical/fields/theta_field.tex:101-160`; `canonical/THEORY/canonical/canonical_action.tex:22-30`; restricted comparator `G1_COMPLEX_REAL_COFRAME.en.md`. Keep G1 PARTIAL and PR #809 draft; #807/#808 and canonical untouched.
