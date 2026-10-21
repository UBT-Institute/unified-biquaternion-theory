<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: composite-palatin-holst-homogeneous.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact homogeneous parity-curvature comparator, not final fundamental UBT action or full untruncated Euler system.
UBT-AI-PROVENANCE-END
-->
# Composite Palatini–Holst action: exact homogeneous trace/axial spin variation

**Status: CONDITIONAL EXACT MINISUPERSPACE RESULT / FULL UBT DYNAMICS OPEN.** Advances beyond the algebraic auxiliary-torsion no-rescue of draft PR #692. An Einstein–Cartan curvature four-form and independent Holst parity-odd coefficient are **supplied comparison operators**, not derived from the current sole unfinished fundamental Theta action. The composite relationship is enforced **before the homogeneous variation**, but the spatially general field equations have not been verified.

## Unfixed homogeneous spin connection, single Theta and topology

Work on a positive-clock patch of the left icosahedral quotient of the unit group sphere. Keep the homogeneous boost B and spatial rotation C as independent reduced variables until after Euler variation. Choose

\[
\Theta=iq V(t)I,\qquad
\Omega=\tfrac12\big(B(t)+iC(t)\big)\sigma_j\upsilon^j,\quad
e^0=dV,\quad e^j=V B\,\upsilon^j=:a\,\upsilon^j,\quad
N=\dot V>0,\quad B=a/V.
\]

The left-invariant three-coframe and Lorentz spin lift satisfy

\[
d\upsilon^i=-\epsilon^i{}_{jk}\upsilon^j\wedge\upsilon^k,\qquad
\omega^0{}_i=\omega^i{}_0=B\upsilon^i,\quad
\omega^i{}_j=C\epsilon^i{}_{jk}\upsilon^k,\quad
V_\Sigma=\pi^2/60.
\]

The separate spatial rotation C is essential. Setting C to its Levi–Civita-like value before variation would hide the parity-odd first-order equation. All forms descend under the left deck group.

## Independently computed curvature and torsion

Direct calculation with Maurer–Cartan exterior forms (cyclic indices understood) gives

\[
R^0{}_i=
\dot B\,dt\wedge\upsilon^i-
B(C+1)\epsilon^i{}_{jk}\upsilon^j\wedge\upsilon^k,\quad
R^1{}_2=\dot C\,dt\wedge\upsilon^3+
(B^2-C^2-2C)\upsilon^1\wedge\upsilon^2 .
\]

while the Cartan torsion is

\[
T^0=0,\quad
T^i=(\dot a-NB)\,dt\wedge\upsilon^i
-a(C+1)\epsilon^i{}_{jk}\upsilon^j\wedge\upsilon^k.
\]

The two normalized invariant four-forms are exactly

\[
\frac1{12}\epsilon_{abcd}e^a\wedge e^b\wedge R^{cd}
=a\big[N(B^2-C^2-2C)+a\dot B\big]\,
dt\wedge\upsilon^1\wedge\upsilon^2\wedge\upsilon^3.
\]

\[
\frac13\sum_{a<b}e_a\wedge e_b\wedge R^{ab}
=a\big[2NB(C+1)+a\dot C\big]\,
dt\wedge\upsilon^1\wedge\upsilon^2\wedge\upsilon^3.
\]

The first is the parity-even Palatini tetrad-bivector curvature contraction; the second is the parity-odd Holst contraction. These formulae fix the chosen normalization and orientation explicitly. No claim of unique Holst coefficient follows from the biquaternion algebra.

## Composite one-clock action and exact reduced variation

After spatial integration choose the normalized external comparison action

\[
L_\alpha=\mathscr C\left[
a\big(N(B^2-C^2-2C)+a\dot B\big)
+\alpha a\big(2NB(C+1)+a\dot C\big)
-\frac{\Lambda}{3}Na^3
\right],\qquad
\mathscr C=\frac{3V_\Sigma}{8\pi G}.
\]

The composite Theta relation fixes the spin boost in terms of a and V, but **does not** fix C. Substituting that relation and integrating total derivatives leads to

\[
\boxed{
L_\alpha\simeq\mathscr C\left\{
N\left[a+\frac{a^3}{3V^2}-\frac{\Lambda a^3}{3}
-a w^2+\frac{2\alpha a^2w}{V}\right]
-2\alpha a\dot a\,w
\right\},\quad w=C+1.
}
\]

Here the symbol of equality up to a boundary term is explicit; such a boundary adjustment does not alter compactly supported bulk Euler equations. Vary C (equivalently w) now, not earlier:

\[
\frac{\delta L_\alpha}{\delta w}=0
\quad\Longrightarrow\quad
\boxed{w=\alpha\left(\frac aV-\frac{\dot a}{N}\right).}
\]

Substituting the algebraic rotation equation into the same reduced action yields

\[
\boxed{
L_{\alpha,\mathrm{red}}\simeq\mathscr C\,N\left[
a+\frac{a^3}{3V^2}-\frac{\Lambda a^3}{3}
+\alpha^2 a\left(\frac aV-\frac{\dot a}{N}\right)^2
\right].
}
\]

**New structural finding:** the Holst operator generally induces nonzero spatial torsion w, and the homogeneous scale-factor velocity obtains a new quadratic term. At zero parity coupling the rotation equation is w=0, leaving only the temporal trace torsion. This is not the same as putting all Cartan torsion to zero.

## Decisive bare-Palatini result and missing normal constraint

For the bare external Palatini comparator with vanishing Holst and cosmological terms, the exact scale Euler derivative is

\[
\alpha=0,\quad\Lambda=0
\quad\Longrightarrow\quad
\frac1{\mathscr C}\frac{\delta L_{\mathrm{red}}}{\delta a}
=N\left(1+\frac{a^2}{V^2}\right)>0
\quad (N,a,V>0).
\]

Thus no smooth regular positive-clock, positive-scale homogeneous stationary trajectory exists in this restricted branch. The statement is confined to this explicit composition and symmetry-reduced trial family, not all Lorentz frames, torsion structures, or full UBT actions.

With an **imported** positive cosmological constant but no Holst, the reduced equation has the stationary algebraic branch

\[
\alpha=0,\quad\Lambda>0,\quad\Lambda V^2>1
\quad\Longrightarrow\quad
a(V)=\frac{V}{\sqrt{\Lambda V^2-1}}.
\]

This does not generically satisfy the independent-metric Einstein lapse constraint. At a specific unit choice one gets the exact residual

\[
\Lambda=1,\quad V=2:\qquad
\dot a^2+1-\frac{\Lambda a^2}{3}=\frac{16}{27}\ne0
\qquad (N=1).
\]

Thus stationary dynamics of the one-clock composite Palatini *homogeneous reduction* is not equivalent to imposing the complete vacuum Einstein equations. In particular the normal constraint has not been restored merely by adding the parity-even curvature four-form.

The reduced radial velocity Hessian is

\[
\frac{\partial^2L_{\alpha,\mathrm{red}}}{\partial\dot a^2}
=\frac{2\mathscr C\,\alpha^2 a}{N},
\qquad
\frac{\partial^2L_{0,\mathrm{red}}}{\partial\dot a^2}=0.
\]

The Holst coupling makes the homogeneous radial Hessian nonzero but its sign alone is NOT a physical ghost or stability theorem. The lapse remains N=dV/dt and is not independently variable. Reparameterization invariance leaves a primary relation; its full local Dirac algebra and all perturbative modes remain uncomputed.

## Strict limitations and next discriminating result

The action is a curvature **comparator**, not a completed foundational UBT action. Reducing to SU(2)-homogeneous fields before varying can remove field equations, especially normal/lapse and anisotropic constraints. No solution of the full unfixed field equations, dynamical 24-component torsion, positive Hamiltonian, quantitative CMB, or automatic dodecahedral topology selection follows.

The exact next task is to compute the unrestricted composite spin Euler derivative of a parity-even Palatini four-form with the existing no-new-field lift, identify the normal-component rank, and test whether a derived Holst coefficient improves or worsens its constrained principal symbol. A parity-odd interaction is not automatically allowed by the full U(1) and parity rules; any such parameter remains a candidate until justified.

**Verification:** `tools/verify_composite_palatin_holst_flrw.py`, `tests/test_composite_palatin_holst_flrw.py`, isolated CI. All calculations use real symmetric coframes and exterior forms; no Planck data or CMB fit is used.
