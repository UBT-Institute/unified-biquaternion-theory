<!-- BILINGUAL-UNIT: gr-theta-only-clock-scope-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Explicit algebraic scope test, not a selected UBT time or graviton dynamics.
UBT-AI-PROVENANCE-END
-->
# Full-biquaternion value invariants do not determine a universal Theta clock

<!-- UNIT: scope -->
## Axiom and global-clock scope

The user concern is correct: the recent FLRW/synchronous clock was a **chosen comparison ansatz**, not a derived cosmological history. This audit returns to unrestricted matrix-value Theta and its existing potential-sector symmetries. No full-UBT physical clock, reality selection or action is asserted; the classical central metric must continue to follow the locked Axiom C rather than a new trace/real-part readout.

<!-- UNIT: orbit -->
## Neutral invariants cannot select a real Lorentz clock

The locked fundamental object is a full biquaternion \(\Theta\in\mathbb B\simeq\operatorname{Mat}_2(\mathbb C)\) with four complex (eight real) coefficients, and the locked spacetime geometry is a Lorentz-real **first jet** \(E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\in W_L\) only in its admitted classical sector. The background coordinate \(\tau=t+i\psi\) is already in Axiom B. Therefore a scalar extracted from a timelike projection \(X\) is not a derivation of fundamental time or a universal physical clock.

The existing polynomial-potential calculation uses the action
\[
X\longmapsto e^{i\alpha}SXS^\dagger,\quad S\in SL(2,\mathbb C),
\quad
H(X)=\operatorname{Tr}(X^\sharp X^\dagger),\quad D(X)=|\det X|^2.
\]
Here \(X^\sharp=\operatorname{adj}X\) in the faithful \(2\times2\) representation, NOT Hermitian conjugation. The already classified real potential through degree four depends on \(H,H^2,D\). On an anti-Hermitian Lorentz-real carrier \(X^\dagger=-X\) one has
\[
H(X)=-2\det X,\qquad D(X)=H(X)^2/4.
\]
The particular timelike clock expression \(T_H=\sqrt{H/(2\mathcal N_0)}\) agrees there with \(T=\sqrt{-X^2/\mathcal N_0}\), but this does not make the clock identity valid at generic complex \(\Theta\) values.

**Exact same-orbit witness.** Choose
\[
X_0=i\sqrt2\,I_2,\quad
S=\operatorname{diag}(2^{1/4},2^{-1/4}),\quad
X_1=\operatorname{diag}(2,1)=-i\,SX_0S^\dagger.
\]
Then \(\det S=1\) and
\[
H(X_0)=H(X_1)=4,\quad D(X_0)=D(X_1)=4,\quad
X_0^\dagger=-X_0,\quad X_1^\dagger=X_1.
\]
Thus a **single orbit of the declared potential-sector group** contains a Lorentz-real and a non-Lorentz-real carrier. No invariant function on that full group orbit (polynomial or not) can distinguish the two. The criterion \(D=H^2/4\) also does not characterize the Lorentz-real branch by itself.

**Phase-metric caveat from existing work.** The canonical sharp metric is complex-bilinear:
\[
g_{\mu\nu}I_2=\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu),\quad
g_{\mu\nu}[e^{i\alpha}E]=e^{2i\alpha}g_{\mu\nu}[E].
\]
Hence a continuous scalar central phase as multiplication of E is *not* a physical gauge redundancy preserving the unchanged real central metric. We use the declared potential-sector orbit solely to disprove selection of W_L from its neutral value invariants; we DO NOT assert both orbit representatives are gauge-equivalent physical metrics. This phase incompatibility was established before this note.


<!-- UNIT: constant -->
## Constant-Theta split-jet obstruction to a universal clock

There is a further independent obstruction to promoting every \(\Theta\)-**value** scalar into a universal unit-gradient clock. In the previously documented independent split-jet *comparison* (not the pure Lorentz spin-lift), there are regular coframes with constant value \(\Theta=iI_2\). For example, with \(\mathcal N_0=1\) and auxiliary split-jet one-forms chosen to realize the coframe, take
\[
\Theta=iI_2,\quad
e^0=dt,\quad e^j=(1+t^2)\,dx^j,\quad
g=-dt^2+(1+t^2)^2d\mathbf x^2.
\]
Then \(H(\Theta)=2\), so \(T_H=\sqrt{H/(2\mathcal N_0)}=1\) and \(dT_H=0\) although \(g\) is nondegenerate. Consequently
\[
g^{-1}(dT_H,dT_H)=0\ne-1.
\]
This is an OFF-SHELL kinematic counterexample in a specifically declared split-jet class; it does not establish that constant \(\Theta\) satisfies the as-yet unknown fundamental UBT Euler equations. Nor does it contradict the earlier pure metric-compatible Lorentz-vector theorem, whose allowed connections enforce \(X\cdot e=\frac1{2\sqrt{\mathcal N_0}}d(X^2)\), excluding the displayed constant-X coframe.

The full dynamical theory might select a timelike branch, a field-jet/holonomy clock, or observer-dependent clocks, but no such global selection follows from the known low-degree invariant potential or the canonical kinematic axioms. In particular any globally smooth time with a unit gradient is a further *branch hypothesis*, not evidence that a closed compact spacetime is dynamically forbidden by UBT.


<!-- UNIT: metric-real-slice -->
## Real metric does not enforce a real Lorentz jet

The full complex central product is algebraically meaningful beyond the physical Lorentz-real slice, but demanding merely that its scalar coefficient be a real Lorentzian metric does NOT force the jet itself into that slice. In the coefficient convention
\[
E_\mu=i\,e_\mu{}^0 I+\sum_{k=1}^3e_\mu{}^k\mathbf e_k,\qquad
g_{\mu\nu}=\eta_{ab}e_\mu{}^ae_\nu{}^b,
\]
take the **complex** constant coefficient matrix \(e=L\), where
\[
L=\begin{pmatrix}
c&is&0&0\\
is&c&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},\quad c=s=1/\sqrt2,\quad \eta=\operatorname{diag}(-1,1,1,1).
\]
Direct matrix multiplication gives
\[
\boxed{L^{\mathsf T}\eta L=\eta,\qquad L\notin O(1,3;\mathbb R).}\tag{E}
\]
Thus the resulting central metric is **exactly real Minkowski**, although the complex jet coefficients are not real and hence \(E_\mu\notin W_L\). An affine full-complex field with zero connection \(\Theta(x)=\Theta_0+\sqrt{\mathcal N_0}\sum_\mu E_\mu x^\mu\) realizes these constant jets locally; this is only a kinematic algebraic witness. It is NOT a physical solution of the unfinished full UBT equations, and the locked Axiom C still defines the admitted classical sector by \(E_\mu\in W_L\). The example rules out the tempting shortcut "real central metric automatically selects Lorentz-real jets". A dynamical reality/branch-selection law or a suitably justified quotient remains necessary.

<!-- UNIT: decision -->
## What must be determined next

First define a physically correct transformation law for the full two-sided biquaternion jet and prove dynamical preservation (or selection) of the real Lorentz metric, rather than inferring it from H and D. Then determine the physical torsion/relative-connection selector from one microscopic Theta action; only afterward test whether a timelike intrinsic clock branch survives the full Euler equations, its constraints, and the imaginary-time psi sector. If a universal clock is not selected, observer-local time is not a contradiction. The already known mimetic-unit-clock work warns that fixing a unit clock before full variation may introduce a conserved dust mode rather than restore GR. References: canonical/AXIOMS.md A–D; research_tracks/action_selection/theta_potential_invariants.en.md; research_tracks/action_selection/phase_central_metric_compatibility.en.md; research_tracks/action_selection/theta_unit_clock_mimetic_constraint.en.md; research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md. Exact symbolic regression: tools/verify_gr_theta_only_clock_scope_2026_11_19.py. Full on-shell/global/Lean conclusions NOT established.
