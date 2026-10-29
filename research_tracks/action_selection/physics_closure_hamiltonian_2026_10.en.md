<!-- BILINGUAL-UNIT: physics-closure.appendix-hamiltonian -->
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

# One-clock Hamiltonian and self-dual comparison

[Audit overview](physics_closure_2026_10.en.md).

<!-- BILINGUAL-UNIT: physics-closure.hamiltonian -->
## Complete constrained calculation for the existing homogeneous comparator

This is a different, explicitly specified reduction with $a,V,N=\dot V>0$, rotation $w=C_{\rm rot}+1$, and positive constant $\mathscr C=3V_\Sigma/\kappa$. The quotient topology and the radial ansatz are supplied comparison data. The original curvature action differs by the endpoint derivative of $\mathscr C[a^3/(3V)+ba^2w]$ from
$$
L_1=\mathscr C\{\dot V[F-aw^2+2ba^2w/V]-2ba\dot a w\},
\qquad F=a+\frac{a^3}{3V^2}-\frac{\Lambda a^3}{3}.
$$
The endpoint term shifts canonical momenta by a canonical transformation. Use the displayed boundary-adjusted action throughout. The rotation equation and its exact elimination give
$$
w=b\left(\frac aV-\frac{\dot a}{N}\right),\qquad
L=\mathscr C N\left[F+b^2a\left(\frac aV-\frac{\dot a}N\right)^2\right].
$$
For $b\ne0$ the velocity Hessian on $(\dot a,N)$ has rank one, not two:
$$
W=\frac{2\mathscr C b^2a}{N}
\begin{pmatrix}1&-\dot a/N\\-\dot a/N&(\dot a/N)^2\end{pmatrix},\qquad
W\binom{\dot a}{N}=0.
$$
The momenta, canonical Hamiltonian and primary constraint are
$$
p=2\mathscr C b^2a\left(\frac{\dot a}N-\frac aV\right),\quad
p_V=\mathscr C\left[F+b^2a\left(\frac{a^2}{V^2}-\frac{\dot a^2}{N^2}\right)\right],\quad
H_c=0,\quad
\phi=p_V+\frac{ap}V+\frac{p^2}{4\mathscr C b^2a}-\mathscr C F=0.
$$
The unreduced first-order action has three primary constraints
$$
\chi_a=p+2\mathscr C ba w,\quad
\chi_V=p_V-\mathscr C(F-aw^2+2ba^2w/V),\quad\chi_w=p_w.
$$
Their full Poisson matrix is
$$
\{\chi_i,\chi_j\}=\begin{pmatrix}0&x&y\\-x&0&z\\-y&-z&0\end{pmatrix},\quad
x=\mathscr C(F_a-w^2+4baw/V),\quad y=2\mathscr C ba,\quad
z=2\mathscr C a(w-ba/V).
$$
Its rank is two everywhere on this patch because the $(a,w)$ minor is $y^2\ne0$; its null vector is $(z,-y,x)$. The pair $(\chi_a,\chi_w)$ is second class. Eliminating it gives $w=-p/(2\mathscr C ba)$, $p_w=0$, all retained Dirac brackets are canonical, and $\chi_V$ becomes $\phi$. The total Hamiltonian is $u\phi$; its self-bracket vanishes and generates no secondary constraint. There is one first-class and two second-class constraints in the original six-dimensional phase space: $(6-2-2)/2=1$ homogeneous physical degree of freedom. These are finite-dimensional constraints, not the spacetime hypersurface-deformation algebra.

Gauge fixing the monotone clock to $V=t$ gives
$$
H_V=\frac{ap}V+\frac{p^2}{4\mathscr C b^2a}-\mathscr C F,\qquad
\frac{da}{dV}=\frac aV+\frac p{2\mathscr C b^2a},\qquad
\frac{dp}{dV}=-\frac pV+\frac{p^2}{4\mathscr C b^2a^2}+\mathscr C F_a.
$$
The result is a genuine Legendre/Dirac reduction of the declared comparator. It is not the Hamiltonian of the independent split-jet GR branch or of a finalized microscopic UBT theory.

<!-- BILINGUAL-UNIT: physics-closure.degenerate -->
## The zero coefficient and energy diagnostic

At $b=0$ divide by no Holst coefficient. Rotation gives $w=0$; the remaining action is $\mathscr C\dot V F$. The primary constraints are $p=0$ and $p_V-\mathscr C F=0$. Consistency with the required $N>0$ adds $F_a=0$. On this secondary surface $F_{aa}=-2/a\ne0$: there are two second-class constraints and one first-class constraint in the remaining four-dimensional phase space, hence zero physical homogeneous degrees of freedom. Including the eliminated $(w,p_w)$ pair gives four second-class constraints in the original phase space. For $\Lambda\le0$ no regular positive-clock solution exists; for $\Lambda>0$ the branch is $a(V)=V/\sqrt{\Lambda V^2-1}$ on $\Lambda V^2>1$. The existing exact Einstein normal residual $16/27$ at $\Lambda=1,V=2$ is retained. Changing the Holst coefficient changes the constraint stratum; the singular limit at fixed momentum cannot be called a smooth GR limit.

Completing the square gives
$$
H_V=\frac{(p+2\mathscr C b^2a^2/V)^2}{4\mathscr C b^2a}
+\mathscr C\left[-a+\frac13\left(\Lambda-\frac{1+3b^2}{V^2}\right)a^3\right].
$$
Thus at fixed positive $V$ the Hamiltonian is bounded below on $a>0$ precisely when $\Lambda>(1+3b^2)/V^2$. Otherwise the minimizing-momentum ray tends to negative infinity as $a$ grows. This clock-dependent homogeneous energy diagnostic is not a full field-theoretic ghost or nonlinear stability theorem. Nor does an instantaneously bounded energy prove global stability for this explicitly time-dependent system. The global inequality formalization remains `LEAN-PENDING`; the square identity is separately formalized.

<!-- BILINGUAL-UNIT: physics-closure.selfdual -->
## Checking the proposed self-dual canonical match

A subsequent user-supplied review correctly identifies an additional algebraic result. Write $k=b^2$ as an independent continued parameter and use the extended generating function
$$
F_2=a\pi+VP_V+f(a,V),\qquad f=-\frac23\mathscr C k\frac{a^3}{V}.
$$
Then $p=\pi-2\mathscr C k a^2/V$, $p_V=P_V+2\mathscr C k a^3/(3V^2)$, and
$$
K=H_V\bigl(p=\pi+f_a\bigr)+f_V
=\frac{\pi^2}{4\mathscr C k a}-\mathscr C a+\frac{\mathscr C\Lambda a^3}{3}
-\frac{\mathscr C(1+k)a^3}{3V^2},\qquad \phi=P_V+K.
$$
Within this fixed-scale-factor, fixed-clock momentum shift and the specified positive normalization, the clock term disappears precisely at $k=-1$, giving the standard closed-FLRW GR Hamiltonian. Equivalently,
$$
L_{k=-1}=\mathscr C\left[-\frac{a\dot a^2}{N}+Na-\frac{\Lambda Na^3}{3}\right]
+\frac d{dt}\left(\frac{2\mathscr C a^3}{3V}\right),\qquad N=\dot V.
$$
This is a verified `PROVED` algebraic match for a formally complexified comparator. It requires $b=\pm i$, outside the real-coefficient family, and an additional GR-matching requirement rather than causality alone. At these values $P_b$ has complex rank three; the real-family inverse must not be used. The preserved reparametrization constraint exists already in the original model. Calling its absence a missing normal constraint was imprecise; the preserved $16/27$ example instead establishes failure of the separate **vacuum Einstein** constraint for that real zero-coefficient comparison.

In the transformed self-dual model $P_V$ is conserved; the original $p_V$ generally is not. Formally identifying $M=P_V$ and $\mathscr C=3V_\Sigma/\kappa$ gives
$$
\left(\frac{a'}a\right)^2+\frac1{a^2}=\frac\Lambda3+\frac\kappa3\rho,
\qquad \rho=\frac{M}{V_\Sigma a^3},\qquad a'=\frac{da}{dV}.
$$
This is a homogeneous dust-like integration constant, including the vacuum choice $M=0$. Neither its value nor its positive sign is selected. Deriving the full [Brown–Kuchar](https://arxiv.org/abs/gr-qc/9409001) dust action, inhomogeneous constraints and dust stability from Theta remains `OPEN_GAP`; an inverse-volume integration constant alone is not that derivation or a parameter-free new prediction.

There is a more immediate admissibility problem than an unspecified warning about [Ashtekar reality conditions](https://arxiv.org/abs/gr-qc/9410013). The original no-new-field derivative uses the **Hermitian** pair $D\Theta=d\Theta+\Omega\Theta+\Theta\Omega^\ddagger$. For each Hermitian Pauli matrix, a real rotation coefficient $c$ gives
$$
\Omega=\tfrac12(B+ic)\sigma,\qquad\Omega+\Omega^\ddagger=B\sigma.
$$
Continuing the solved rotation to $c=-1+id$, with real $d=a/V-a'$, instead gives
$$
\Omega+\Omega^\ddagger=(B-d)\sigma,\qquad
B=a/V\ \Longrightarrow\ a_{\rm generated}=V(B-d)=Va'.
$$
Thus the same continued connection no longer generates the assumed tetrad for generic trajectories. For example $V=2,a=1,a'=0$ gives a generated spatial scale of zero. If the rotation is kept real while $b=i$, its complex stationarity equation forces both $w=0$ and $d=0$. If it is allowed to become complex, the Hermitian readout must be recomputed; analytically continuing the already reduced polynomial does not commute with imposing that readout. Lean verifies the continued coefficient and scale identities; independent symbolic matrices check every Pauli direction. This refutes automatic compatibility of this naive continuation, not all possible self-dual completions.

Even the linearized homogeneous readout on a compatible background requires $V\delta a'-\delta a=0$ in the clock gauge. The perturbation $\delta a=\varepsilon V^2$ violates it at first order. Consequently a general inhomogeneous perturbation spectrum cannot yet be assigned to this continuation as a canonical UBT branch. The next required gate is an action-derived chiral/two-sided connection with reality conditions that preserves the original tetrad identity, followed by its unreduced variation and perturbations. This changes neither the real-family causal no-selection result nor the established one-connection no-go assumptions.

<!-- BILINGUAL-UNIT: physics-closure.real-subset -->
## Real subsets and the biquaternionic representation

Real numbers embed in complex numbers, and complex scalars embed centrally in the biquaternions. The spin connection is already biquaternion-valued in its traceless complex matrix representation; complex matrix entries do not by themselves imply a complex physical metric. The standard correspondence between complex spin matrices and real Lorentz transformations is reviewed by [Larsson–Larsson](https://arxiv.org/abs/2110.15118). The obstruction above concerns the action of the Hermitian pair on the specified tetrad, not a prohibition on using complex or biquaternionic variables. A quaternion unit also squares to minus one, but unlike the scalar imaginary unit it need not commute with the other generators: $[\mathbf e_1,\mathbf e_2]=2\mathbf e_3$. Substituting it for a commuting coupling changes the operator/ordering problem and requires a separately defined invariant action.

There are nonempty real sectors of the declared comparator. The real-coefficient case $b=1,\mathscr C=1,\Lambda=0$ with initial data $V=2,a=1,p=-1$ has $a'=0,p_V=4/3,w=1/2$. Its Hamiltonian vector field is smooth for positive scale and clock, so it has a real local trajectory; this is the same trajectory already checked by independent integrators above. Its rotation stays real and the original Hermitian tetrad readout applies. This establishes a real restricted model trajectory, not vacuum Einstein equivalence, microscopic selection, or stability of the full theory.

The proposed simultaneous real subset of the **self-dual continuation** can be tested exactly. In the unchanged closed homogeneous ansatz take a connected positive-clock interval, $a,V>0$, constant real $\Lambda$, and a twice differentiable scale factor. The original Hermitian readout and the continued GR-clock scale equation require
$$
a=Va',\qquad
\left(\frac aV\right)'=0,\qquad a=cV,\quad c\in\mathbb R,
$$
$$
\mathcal E_a/\mathscr C=(a')^2+2aa''+1-\Lambda a^2=0
\quad\Longrightarrow\quad
1+c^2-\Lambda c^2V^2=0.
$$
This residual cannot vanish throughout any nonempty open positive-clock interval. In fact it cannot vanish at two distinct positive clock values: subtracting the equations forces $\Lambda c^2=0$, while either equation would then require $1+c^2=0$. The theorem `no_closed_real_constant_ratio_trajectory` proves this incompatibility for arbitrary real coefficients and any two distinct positive times. CAS independently differentiates the action and verifies the constant-ratio substitution. The calculus implication from a differentiable constant ratio to its constant representative is stated analytically; Lean formalizes the resulting finite algebraic obstruction.

Consequently the naive continuation has no regular real trajectory satisfying both requirements within these unchanged assumptions. This is a corollary in the present ansatz of the existing pure-pair/concurrent-vector obstruction, not a new no-go for all UBT real slices. Flat real Minkowski representers and the separately postulated split-jet GR branch are not excluded. A real subset must be nonempty and preserved by the actual dynamics; inclusion of number systems alone does not establish those properties.
