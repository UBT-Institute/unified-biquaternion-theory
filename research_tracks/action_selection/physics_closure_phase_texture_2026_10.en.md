<!-- BILINGUAL-UNIT: physics-closure.appendix-phase-texture -->
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

# Phase, texture and quotient checks

[Audit overview](physics_closure_2026_10.en.md).

<!-- BILINGUAL-UNIT: physics-closure.phase-audit -->
## Phase and temporal-center proposals checked against the full tetrad

Use the original pure pair, real spatial boost $B$, real rotation and $\Theta=Ve^{i\varphi}I_2$. Its time derivative has coefficients
\[
\operatorname{Re}\dot\Theta=(\dot V\cos\varphi-V\dot\varphi\sin\varphi)I_2,
\qquad
\operatorname{Im}\dot\Theta=(\dot V\sin\varphi+V\dot\varphi\cos\varphi)I_2.
\]
The spatial derivative is $VB e^{i\varphi}\sigma_j\upsilon^j$. Membership of the complete tetrad in the fixed slice $i\operatorname{Herm}_2$ requires $VB\cos\varphi=0$. On a nondegenerate patch with $VB\ne0$, a smooth phase therefore has $\cos\varphi=0$ and $\dot\varphi=0$, so $N=\pm\dot V$. Reading only the imaginary time coefficient and discarding the spatial or temporal real part would change the locked readout. The field phase is also not by definition the complex-time coordinate $\psi$: for the holomorphic example $\Theta(\tau)=e^{i\tau}$, one has $\Theta(t+i\psi)=e^{-\psi}e^{it}$.

A genuine temporal $u(1)$ generator is anti-Hermitian. For real $\chi$ and any Theta, centrality gives
\[
\Omega_t=i\chi I_2
\quad\Longrightarrow\quad
\Omega_t\Theta+\Theta\Omega_t^\dagger=0.
\]
It does not release the lapse. A real central coefficient instead gives a dilation: $\Omega_t=(u/2)I_2$ produces $u\Theta$ and, for $\Theta=iVI_2$, $N=\dot V+uV$. Such a term is not a phase or a metric-compatible physical Lorentz generator. It can only be compared as an explicitly distinguished relative jet component with its composite/auxiliary origin and variation stated. The existing split-jet architecture already makes this distinction. Lean and independent matrix calculations verify the phase cancellation and real-dilation coefficient.

<!-- BILINGUAL-UNIT: physics-closure.texture-audit -->
## The proposed sphere texture is not yet an admissible replacement

Take exactly the suggested $\Theta=Ve^{i\varphi}g$, $g=x_0I_2+i\mathbf x\cdot\boldsymbol\sigma\in SU(2)$, with $x_0^2+|\mathbf x|^2=1$, the fixed Lorentz slice and the same traceless pure pair. At the old phase $\varphi=\pi/2$ and $g=I_2$, $dg=i\sigma_j\upsilon^j$ contributes $-V\sigma_j\upsilon^j$ to $d\Theta$. The real-parameter connection contributes $iVB\sigma_j\upsilon^j$. The resulting Hermitian part is nonzero, so this suggested substitution already fails the original tetrad reality condition.

Freeing the phase does not cure this particular texture under any traceless pure pair. Its Hermitian part has
\[
H_\Theta=V(\cos\varphi\,x_0I_2-\sin\varphi\,\mathbf x\cdot\boldsymbol\sigma),
\qquad
\det H_\Theta=V^2(x_0^2-\sin^2\varphi).
\]
The preceding full-carrier identity requires $D_\Omega H_\Theta=0$. A traceless Lorentz pure pair preserves the determinant of a parallel Hermitian matrix, but this determinant varies spatially on every open sphere patch for $V\ne0$. CAS verifies the determinant and its infinitesimal connection invariance independently. This excludes the specified texture with this derivative and fixed real slice; it does not classify other equivariant textures or carrier actions. The general bundle/PDE classification is `LEAN-PENDING` because the representation and symmetry lift have not been selected.

A consistent change of carrier trivialization must transform the connection as well. In the general two-sided notation, the right change $\Theta'=\Theta g$, $\mathcal A'=\mathcal A$, $\mathcal B'=g^{-1}\mathcal B g+g^{-1}dg$ gives $D'\Theta'=(D\Theta)g$. The apparent extra $dg$ term cancels. Lean verifies the noncommutative cancellation; whether this right action is an admissible gauge transformation preserving the real structure needs a separate intertwiner. The geometric $+1$ in $w=C+1$ was already produced by the Maurer–Cartan coframe; it cannot be counted as new dynamics from a gauge twist.

On the left quotient $(2I)\backslash SU(2)$, $g$ is not an ordinary globally defined matrix-valued function: already $\Theta(-g)=-\Theta(g)$ because $-I_2\in2I$. An equivariant section of an associated bundle is a possible different specification, but its transition representation, connection and Lorentz-real tetrad must all descend together. The quotient supplies a locally round FLRW geometry; full global rotational isotropy must not be assumed from the covering sphere. No valid reduced texture action or Dirac count is claimed before these kinematic gates.
