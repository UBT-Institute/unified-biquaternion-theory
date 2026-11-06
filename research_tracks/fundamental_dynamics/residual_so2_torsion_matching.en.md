<!-- BILINGUAL-UNIT: residual-so2-torsion-matching -->
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


# Exact residual SO(2) coefficients for quadratic torsion

**Status.** Conditional local comparison, 2026-11-06. The coefficients below are the projection of the existing quadratic geometric action family onto the two-carrier Lorentz lift. They give the complete stationary residual equation for that comparison.

<!-- BILINGUAL-UNIT: residual-so2-torsion-matching.scope -->
## Geometry and action class

Use the [two-carrier invariant basis](residual_so2_invariant_basis.en.md) with $DV=\kappa e$, $DW=0$, $\kappa=\sqrt{\mathcal N_0}$, future timelike $V$ and a nonzero transverse component of $W$. Retain its variables $r,z,s,u,n,P,J$ and its reference $\omega_0$ with vanishing transverse contortion. Use an adapted oriented coframe with $e^0=-u^\flat$, $e^1=n^\flat$, $\eta=\operatorname{diag}(-1,1,1,1)$ and $J^2{}_3=-J^3{}_2=1$. At fixed carrier geometry write $\omega=\omega_0+\alpha J$ and $\alpha=a e^0+b e^1+p_Ae^A$, where $A=2,3$. The variations are local with compact support.

Use the three parity-even torsion squares and two parity-odd squares formed with the metric and orientation alone. This is the quadratic torsion part of the [geometric action family](../action_selection/physics_closure_action_family_2026_10.en.md), using the basis of [Baekler and Hehl](https://arxiv.org/abs/1105.3504) up to changes of normalization. The explicit contractions here are

$$
\begin{gathered}
T^a=\tfrac12 T^a{}_{bc}e^b\wedge e^c,\quad
t_b=T^a{}_{ab},\quad S^a=\tfrac16\epsilon^{abcd}T_{bcd},\quad \epsilon_{0123}=1,\\
I_1=T_{abc}T^{abc},\quad I_2=T_{abc}T^{cba},\quad I_3=t_at^a,\quad
O_1=t_a S^a,\quad O_2=\frac{T_a\wedge T^a}{\mathrm{vol}},\\
L=c_1 I_1+c_2 I_2+c_3 I_3+\beta O_1+\gamma O_2.
\end{gathered}
$$

$L$ is the density divided by the volume. The formulas for these contractions hold pointwise also with smooth coefficients of the carrier invariants. For a constant Holst coefficient its bulk contribution is included in $\gamma$ by the Nieh–Yan identity. Carrier-indexed contractions, matter and higher derivative terms are outside this comparison. The ordinary Hilbert–Palatini and first-jet terms are residual-independent in the bulk on this branch, as established in the invariant-basis note and the [first-jet blindness theorem](field_built_so2_connection_family.en.md).

<!-- BILINGUAL-UNIT: residual-so2-torsion-matching.contractions -->
## Reference torsion and the five contractions

Write $X=\mathring\nabla u$, $Y=\mathring\nabla n$, $x=P\mathring\nabla_n u$ and define the symmetric transverse blocks

$$
h=\kappa/r,\qquad l=\kappa z/(rs),\qquad
B=X_P-hI_2,\qquad C=Y_P-lI_2,\qquad d_u=\operatorname{tr}B,\quad d_n=\operatorname{tr}C .
$$

The transport equations give $\omega_0{}^1{}_0=h e^1$, $\omega_0{}^A{}_0=h e^A$ and $\omega_0{}^A{}_1=l e^A$. Subtracting the Levi-Civita components from the first-jet matrices gives the contortion entries

$$
K_0{}^1{}_0=-x_A e^A,\qquad
K_0{}^A{}_0=-B_{AB}e^B-x_A e^1,\qquad
K_0{}^A{}_1=-C_{AB}e^B+x_A e^0,\qquad
K_0{}^2{}_3=0.
$$

Lorentz antisymmetry fixes the exchanged entries. Wedge with the coframe to obtain

$$
T_0^0=T_0^1=0,\qquad
T_0^A=B_{AB}e^0\wedge e^B+C_{AB}e^1\wedge e^B+2x_Ae^0\wedge e^1,\qquad
\Delta T^A=\alpha\wedge J^A{}_B e^B .
$$

In $I_1$ and $I_2$ the mixed contractions of $T_0$ with $\Delta T$ vanish because $B,C$ are symmetric, $J$ is antisymmetric, and the other index slots have disjoint support. The reference trace is $-d_u e^0-d_n e^1$, and the shift adds the transverse trace $-Jp$. The reference axial vector is $-2Jx/3$, and the shift adds $2(bu-an)/3$. In $O_2$ the shift squared vanishes by $\alpha\wedge\alpha=0$. These observations give the exact differences at fixed geometry

| Contraction | Difference |
| --- | --- |
| $I_1$ | $4(b^2-a^2)+2p^2$ |
| $I_2$ | $-2(b^2-a^2)+p^2$ |
| $I_3$ | $p^2$ |
| $O_1$ | $\tfrac23(d_n a-d_u b+p\cdot x)$ |
| $O_2$ | $2(d_n a-d_u b+2p\cdot x)$ |

Here $p^2=p_2^2+p_3^2$. The $O_2$ source agrees with the constant-coefficient Holst calculation in the invariant-basis note.

<!-- BILINGUAL-UNIT: residual-so2-torsion-matching.stationarity -->
## Residual Hessian, source and elimination

For $\boldsymbol a=(a,b,p_2,p_3)^T$, set

$$
L_{\parallel}=4c_1-2c_2,\qquad L_\perp=2c_1+c_2+c_3,\qquad
\lambda=\tfrac23\beta+2\gamma,\qquad \mu=\tfrac23\beta+4\gamma.
$$

Then $\Delta L=\tfrac12\boldsymbol a^T M\boldsymbol a+\boldsymbol j^T\boldsymbol a$ with

$$
M=2\,\operatorname{diag}(-L_{\parallel},L_{\parallel},L_\perp,L_\perp),\qquad
\boldsymbol j=(\lambda d_n,-\lambda d_u,\mu x_2,\mu x_3)^T.
$$

For matching directly in the irreducible basis, let $Q$ be the trace-free and axial-free torsion. Orthogonality gives $I_1=\tfrac23 t^2-6S^2+Q^2$. The vector and axial cross term in the wedge square gives $O_2=2O_1+Q_a\wedge Q^a/\mathrm{vol}$. If $g_t,g_S,g_Q$ multiply $t^2,S^2,Q^2$, respectively, and $g_{tS},g_{\wedge Q},f_H$ multiply $O_1,Q_a\wedge Q^a/\mathrm{vol}$ and the constant-coefficient Holst term, the same map reads

$$
L_{\parallel}=\tfrac43 g_Q-\tfrac49 g_S,\qquad L_\perp=g_t+\tfrac43 g_Q,
\qquad \beta=g_{tS}-2g_{\wedge Q},\qquad \gamma=g_{\wedge Q}+f_H.
$$

The algebraic block has rank $2\mathbf 1_{L_{\parallel}\ne0}+2\mathbf 1_{L_\perp\ne0}$. The parity-even terms supply the entire block. Parity-odd terms supply the source. If both blocks are invertible, the stationary residual one-form has components

$$
a_*=\frac{\lambda d_n}{2L_{\parallel}},\qquad
b_*=\frac{\lambda d_u}{2L_{\parallel}},\qquad
p_*=-\frac{\mu x}{2L_\perp}.
$$

The correction to the density at the reference is

$$
L(\alpha_*)-L(0)
=-\frac{\lambda^2}{4L_{\parallel}}(d_u^2-d_n^2)
-\frac{\mu^2}{4L_\perp}|x|^2 .
$$

The parity-even regular case therefore selects $\omega_0$. In particular $T_0$ may be nonzero there. For example the metric chart from the invariant-basis proof permits $X_P=Y_P=0$ and $x=0$, for which $B=-hI_2$ and $h>0$. This is a stationary example for the residual variation at fixed geometry. The other field equations are separate.

If $L_{\parallel}=0$, the corresponding equations are $\lambda d_u=\lambda d_n=0$. If $L_\perp=0$, the corresponding equation is $\mu x=0$. Compatible zero blocks leave the corresponding components of $\alpha$ free in this comparison. The even kernel is exactly $(c_1,c_2,c_3)\propto(1,2,-4)$, which includes the Einstein-sign torsion combination $(-1/4,-1/2,1)$ used in the [free-jet comparison](../action_selection/free_jet_torsion_principal_2026_10.en.md). It has zero residual variation for all admissible geometries. The Holst-only case has $M=0$ and gives geometric conditions through $\boldsymbol j$. The geometry and first-jet terms that are blind to $\alpha$ have $M=\boldsymbol j=0$.

This is the independent residual equation on the declared transport family. To use stationary elimination for a specified single-$\Theta$ pullback, the composite rule must yield the stationary branch above, or the adjoint chain-rule term of the invariant-basis note must be evaluated. The microscopic coefficients and the physical constraint reduction remain open.

<!-- BILINGUAL-UNIT: residual-so2-torsion-matching.verification -->
## Verification

The [SymPy 1.14.0 tests](../../tests/test_residual_so2_torsion_matching.py) reconstruct the reference contortion and check all five contractions, the irreducible wedge identity and the stationary solution. The [Lean 4.33.1 module](../../formal/lean/UBT/Hamiltonian/ResidualSO2Torsion.lean) verifies the even coefficient map, its kernel over a characteristic-zero field and the exact translation to the stationary quadratic form. Formal verification covers this finite algebra. The geometric derivation and the full composite dynamics lie outside that formalization.
