<!-- BILINGUAL-UNIT: residual-so2-quadratic-cone -->
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


# Metric cone tuning and the transverse obstruction for quadratic torsion

**Status.** Restricted two-carrier comparison, 2026-11-07. The regular pure quadratic family has a two-branch metric cone at principal order for a parity-odd tuning. The metric polarizations and the exact trace equation give separate obstructions to Einstein recovery.

<!-- BILINGUAL-UNIT: residual-so2-quadratic-cone.reduction -->
## Regular stationary reduction

Use the same two-carrier transport equations $DV=\kappa e$, $DW=0$ and the same transverse metric chart as in the [commutator-square comparison](residual_so2_commutator_hamiltonian.en.md). Take real constant coefficients in $L=c_1I_1+c_2I_2+c_3I_3+\beta O_1+g_o O_2$, with $g_o=\gamma$ of the [torsion matching](residual_so2_torsion_matching.en.md). A constant Holst term is included via Nieh–Yan. The curvature-even Hilbert–Palatini term, other derivative operators and matter are outside this pure torsion calculation. The torsion invariants are standard metric and orientation contractions. [Baekler and Hehl](https://arxiv.org/abs/1105.3504).

Set $K=2c_1+c_2$, $L_\parallel=4c_1-2c_2$, $L_\perp=K+c_3$, $\lambda=\tfrac23\beta+2g_o$ and $\mu=\lambda+2g_o$. Assume $L_\parallel L_\perp\ne0$ so that the residual one-form can be eliminated by its stationary equation. Write $B,C$ for the reference transverse blocks with traces $d_u,d_n$, and $x$ for the transverse bracket variable. In the oriented orthonormal transverse frame let $\Omega(B,C)=\epsilon^{AB}B_{DA}C_{DB}$ with $\epsilon^{23}=1$.

The reference contractions are

$$
I_1(T_0)=2(\|C\|^2-\|B\|^2)-8|x|^2,\quad I_2(T_0)=\|C\|^2-\|B\|^2,\quad
I_3(T_0)=d_n^2-d_u^2,\quad O_1(T_0)=0,\quad O_2(T_0)=-2\Omega(B,C).
$$

They follow by contracting the displayed reference torsion in the matching note. In particular the trace and axial vectors at $T_0$ are orthogonal, and only the mixed $B,C$ wedge contributes to $O_2$. Adding the stationary density correction gives the exact reduced scalar

$$
L_{\rm red}=K(\|C\|^2-\|B\|^2)+\Sigma(d_n^2-d_u^2)-X_c|x|^2-2g_o\Omega(B,C),\quad
\Sigma=c_3+\frac{\lambda^2}{4L_\parallel},\quad X_c=8c_1+\frac{\mu^2}{4L_\perp}.
$$

<!-- BILINGUAL-UNIT: residual-so2-quadratic-cone.symbol -->
## Removal of the trace and two principal branches

Freeze at the flat stationary $T=0$ background of the preceding comparison. Write $H$ for the transverse metric amplitude and $N,Z$ for the normalized time and longitudinal shift amplitudes. At a real principal covector $(\omega,k,q_A)$, use $B_q v=q_Av_B+q_Bv_A$ and

$$
U=\omega H-B_qN,\qquad V=kH-B_qZ,\qquad F=\omega Z-kN.
$$

The principal scalar is $[K(\|V\|^2-\|U\|^2)+\Sigma((\operatorname{tr}V)^2-(\operatorname{tr}U)^2)-X_c|F|^2-2g_o\Omega(U,V)]/4$. For $q_A=0$ and $k\ne0$, the skew pairing vanishes on the principal covector and the trace is a third wave when $\Sigma+K/2\ne0$. Positive traceless kinetic energy and absence of this trace wave require $K<0$ and $\Sigma+K/2=0$. On this surface both the symmetric difference and the skew pairing depend only on the trace-free blocks. The trace is a null direction of the quadratic action and has a separate nonlinear equation below.

For $q=|q_A|>0$ rotate the transverse basis so $q_A=(q,0)$. The trace-free part of $B_q$ is $\sqrt{2}q$ times the identity in orthonormal symmetric-tensor coordinates. The two transverse diffeomorphisms thus set $H^\circ=0$. Define $Q^2=2q^2$, $A=-K>0$, $E=-X_c$ and $J=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$. Up to the common factor $1/4$, the gauge-fixed scalar is

$$
A Q^2(|N|^2-|Z|^2)+E|\omega Z-kN|^2-2g_o Q^2 N^T J Z.
$$

With $E>0$, the auxiliary $N$ has invertible block $S_N=AQ^2+Ek^2$. Eliminating it gives the same scalar coefficient for both components of $Z$,

$$
\frac{Q^2}{S_N}\left[AE(\omega^2-k^2)-(A^2+g_o^2)Q^2\right].
$$

Its velocity coefficient is positive. The two branches have $\omega^2=k^2+2(A^2+g_o^2)q^2/(AE)$. For a metric cone, $E=2(A^2+g_o^2)/A>0$ is also necessary, as can be seen by evaluating at $k=0$.

<!-- BILINGUAL-UNIT: residual-so2-quadratic-cone.coefficients -->
## Exact coefficient locus

The trace condition gives $4L_\parallel L_\perp=2K L_\parallel-\lambda^2$. Use $8c_1=2K+L_\parallel$ and $\mu=\lambda+2g_o$ to factor the cone condition,

$$
4K L_\parallel L_\perp\left(X_c-2K-\frac{2g_o^2}{K}\right)
=2(K L_\parallel+\lambda g_o)^2.
$$

Thus in the regular real family with positive traceless kinetic sign, the two metric-cone branches at principal order occur exactly when

$$
\Sigma+K/2=0,\qquad K L_\parallel+\lambda g_o=0,\qquad K<0 .
$$

In particular $g_o\ne0$ is required here. One rational example is $(c_1,c_2,c_3,\beta,g_o)=(-1/8,-3/4,1/4,-3/2,1)$, with $K=-1$, $\Sigma=1/2$, $L_\parallel=1$, $L_\perp=-3/4$ and $X_c=-4$.

<!-- BILINGUAL-UNIT: residual-so2-quadratic-cone.polarization -->
## Transverse tidal and Ricci tests

In the fixed carrier chart the inverse metric on $\mathrm dr,\mathrm dz$ is prescribed by the carrier scalars. Its variation gives $h_{uu}=h_{un}=h_{nn}=0$. At a purely transverse covector $k=0$, the principal tidal component $\delta R_{unun}$ is proportional to $\omega^2h_{nn}$ and vanishes. In the Einstein wave plane spanned by $n$ and the other direction perpendicular to the wave, the usual plus polarization has nonzero $\delta R_{unun}$. Thus the same chart admits at most one of the two Einstein tidal amplitudes in this direction, independently of the torsion coefficients.

The regular tuned family has a sharper Ricci test. For $q_A=(q,0)$, $k=0$, $\omega^2=q^2$ and $H^\circ=0$, substituting the real null covector in the Ricci symbol gives $\delta R_{01}=\omega q Z_2/2$ and $\delta R_{22}=-\omega q N_2$. Both are independent of the arbitrary linear trace. The shift equation gives $N=(g_o/A)JZ$. Since $g_o\ne0$, vacuum Ricci then requires both $Z_2=0$ and $Z_3=0$. The nonzero purely transverse tuned amplitudes violate the Einstein vacuum equation at principal order.

<!-- BILINGUAL-UNIT: residual-so2-quadratic-cone.trace -->
## Quadratic obstruction from the exact trace equation

On the trace-tuned surface the exact reduced scalar depends on $B^\circ,C^\circ,x$. Under a local positive rescaling of the transverse metric by $v$ at fixed shifts and carrier coordinates, the two trace-free contractions and their skew pairing stay invariant. Indeed the derivative of $v$ appears only in the discarded trace. The volume density and $|x|^2$ each acquire a factor $v$. Writing $\mathscr A=K(\|C^\circ\|^2-\|B^\circ\|^2)-2g_o\Omega(B^\circ,C^\circ)$ and $\mathscr B=E|x|^2$, the density therefore scales as $v\mathscr A+v^2\mathscr B$ times the original volume. The exact trace equation is $\mathscr A+2\mathscr B=0$.

At the flat stationary point this equation starts at quadratic order. For a nonzero single-phase characteristic amplitude with $q>0$, the principal quadratic action vanishes on shell. The trace equation therefore retains the additional term $E|F|^2/4$. In fact

$$
F=\frac{Q^2}{S_N}(A\omega I-kg_oJ)Z,\qquad
|F|^2=\frac{Q^4}{S_N^2}(A^2\omega^2+k^2g_o^2)|Z|^2>0.
$$

Because the trace equation has zero linearization there, a second-order field correction cannot cancel this leading quadratic term. This is a local obstruction to lifting a nonzero oblique or transverse one-phase principal wave to a smooth perturbative family on the flat branch. The result concerns the declared regular torsion reduction. A full nonlinear mode count on other backgrounds and the constraint equations at singular residual blocks are separate questions.

<!-- BILINGUAL-UNIT: residual-so2-quadratic-cone.verification -->
## Verification

[Exact SymPy 1.14.0 tests](../../tests/test_residual_so2_quadratic_cone.py) check the Schur complement, coefficient locus and example, Ricci components and quadratic trace obstruction. The [matching tests](../../tests/test_residual_so2_torsion_matching.py) check all reference contractions. [Lean 4.33.1](../../formal/lean/UBT/Hamiltonian/ResidualSO2QuadraticCone.lean) checks the three finite polynomial identities for the cone factorization, the shift complement and the bracket norm. The continuum trace variation and the scope of the principal obstructions are analytic.
