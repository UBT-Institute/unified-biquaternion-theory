<!-- BILINGUAL-UNIT: physics-closure.scope -->
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

# Physics closure audit: action freedom and a constrained Holst Hamiltonian

**28 October 2026; PR #807; C_working.** This report uses the existing covariant tetrad, split-jet and homogeneous calculations. It does not select a microscopic action. The effective gravity postulate is an `AXIOMATIC_CANDIDATE` with `CONDITIONAL` physical consequences. Its local mathematical implications remain valid under their stated assumptions; observational confirmation of UBT does not follow. English is the translation source.

<!-- BILINGUAL-UNIT: physics-closure.reuse -->
## Reused results and claim corrections

The rank theorem, split-jet right inverse, auxiliary multiplier theorem, Clifford trace classification, potential classification, determinant null Lagrangian and homogeneous curvature calculation already exist. Relevant sources are `canonical/ACTION.en.md`, `canonical/gr_closure/gravity_dynamical_postulate.en.md`, `formal/lean/UBT/GR/VolumePrincipalSymbol.lean`, `research_tracks/action_selection/clifford_palatini_trace_selector.en.md`, `research_tracks/action_selection/composite_palatin_holst_flrw.en.md`, and `research_tracks/observer_information_hamiltonian_2026_10_holst_causal_selector.en.md`. They are premises with their original scope, not new discoveries in this PR.

Einstein–Lambda recovery, Schwarzschild inclusion and its Regge–Wheeler/Zerilli reductions have status `CONDITIONAL` as UBT claims: they require the adopted gravity functional. Their mathematical implication is not retracted. Microscopic selection of that functional and direct on-shell selection by a finalized one-Theta equation remain `OPEN_GAP`. The current paired claim matrix and machine-readable gravity ledger now distinguish these levels. Older unpaired ledgers retain their historical text; their open microscopic gaps must not be read as disproof of the conditional effective branch.

The alpha ledger remains `OPEN_GAP`. Values near $B\simeq46.28$ are fitted/phenomenological inputs or numerical matches in alternative formulas, not a parameter-free derivation. The nearby historical values are not a measured universal constant. Algebraic colour carriers do not establish propagating QCD, and winding labels do not derive three chiral generations. No author signature, attestation date or provenance tier is changed.

<!-- BILINGUAL-UNIT: physics-closure.class -->
## A finite action class requires extra assumptions

Work in natural units $\hbar=c=1$ on an oriented smooth Lorentzian four-manifold with invertible tetrad, metric-compatible Lorentz connection, and compactly supported variations or specified boundary data. The same tetrad satisfies $E_\mu=N_0^{-1/2}D_\mu\Theta$ and the central anticommutator metric. In the gravity comparison, independent split-jet variations are permitted only on $X^2\ne0$. This is not a replacement of the frozen architecture.

For an explicitly restricted, constant-coefficient geometric expansion, count torsion as derivative order one and curvature as order two; exclude derivatives of torsion, curvature squares, and explicit Theta-dependent coefficients. This geometric counting differs from counting derivatives of an independently varied connection. With $x^\mu$ of length dimension and dimensionless $e_\mu{}^a$, $[e^a]=L$, $[T^a]=L$, $[R^{ab}]=1$, $[\nu_e]=L^4$, and $[N_0]=[\Theta]^2L^{-2}$. The following is a restricted operator basis, not a classification of all local UBT actions.

| Invariant | Algebraic origin / parity | Order | Coefficient dimension | Role |
|---|---|---|---|---|
| $\nu_e=\epsilon_{abcd}e^ae^be^ce^d/24$ | Oriented scalar density / even | 0 | $L^{-4}$ | Allowed cosmological density |
| $\epsilon_{abcd}e^ae^bR^{cd}$ | Graded Clifford trace / even | 2 | $L^{-2}$ | Allowed Palatini term |
| $e^ae^bR_{ab}$ | Ungraded Clifford trace / odd | 2 | $L^{-2}$ | Allowed Holst term |
| $v_av^a\nu_e$, $s_as^a\nu_e$, $q_{abc}q^{abc}\nu_e$ | Three irreducible torsion norms / even | 2 | $L^{-2}$ | Three independent coefficients |
| $v_as^a\nu_e$, $\epsilon^{abde}q_{abc}q_{de}{}^c\nu_e$ | Torsion pseudoscalars / odd | 2 | $L^{-2}$ | Two coefficients before boundary reduction |
| $d(e_a\wedge T^a)$ | Nieh–Yan exact form / odd | 2 | $L^{-2}$ | Redundant in bulk with fixed boundary coefficient |

Products of forms in the table are wedge products. Here $v_a=\eta^{bc}T_{bac}$, $s^d=\epsilon^{dabc}T_{abc}/6$, and $q$ is the trace-free and axial-free remainder, with the antisymmetric pair chosen first in $T_{abc}$. The spacetime torsion components have dimension $L^{-1}$. The standard irreducible-torsion classification is imported from [Baekler–Hehl](https://arxiv.org/abs/1105.3504); its complete field-theoretic formalization is `LEAN-PENDING`. Nieh–Yan removes one linear combination of the odd torsion terms and the Holst coefficient modulo the stated boundary term, not every odd interaction. A spacetime-dependent coefficient invalidates that constant-coefficient boundary elimination.

Proper local Lorentz symmetry and diffeomorphisms allow these operators; they require none of their coefficients to take a specified nonzero value. Adding parity invariance would exclude odd bulk operators, but that is an additional assumption. Nonmetricity is excluded by the specified connection class. Scalar, vector, bivector, pseudovector and pseudoscalar Clifford grades provide contractions and duals; they are not extra independent fundamental fields. The full Clifford representation must not enlarge the eight real components of the biquaternion Theta by assertion.

Allowing arbitrary invariant functions of Theta restores infinitely many coefficients. Even the previously proved quartic potential family leaves independent coefficients. The locked kinetic contraction can reduce to a volume density in the real four-component determinant branch; it cannot simply be counted as an independent healthy propagating scalar term. Internal gauge kinetic terms require an action-derived connection and physical carrier; algebraic subgroup membership is insufficient. A finite list therefore requires a declared truncation and representation, neither selected by the kinematics alone.

<!-- BILINGUAL-UNIT: physics-closure.variation -->
## Minimal effective comparator and full variation within its declared branch

Retain the real Holst coefficient $b$ rather than setting it to zero. A minimal constant-coefficient comparator, with optional unimodular completion as in the adopted branch, is
$$
S_b=\frac1{4\kappa}\int\epsilon_{abcd}e^a\wedge e^b\wedge R^{cd}
+\frac b{2\kappa}\int e^a\wedge e^b\wedge R_{ab}
-\frac1\kappa\int\Lambda(\nu_e-dC_3),\qquad\kappa>0,\ b\in\mathbb R.
$$
Here $[\kappa]=L^2$, $[\Lambda]=L^{-2}$, $[b]=1$, and $[C_3]=L^4$. A fixed-Lambda comparison instead omits the three-form sector and treats Lambda as an external parameter. Torsion-square coefficients are set to zero only as an explicit minimal comparator choice, not by an alleged UBT prohibition. The adopted one-coupling postulate is the further chosen subcase $b=0$; imposing one coupling is not a proof that the other allowed invariants are forbidden.

Put $\Sigma^{ab}=e^a\wedge e^b$ and $P_b=\star+b$ on Lorentz bivectors. Before any connection elimination the first variation is
$$
\delta S_b=\int\delta e^a\wedge\mathcal E_a
-\frac1{2\kappa}\int D\Sigma^{ab}\wedge(P_b\delta\omega)_{ab}
-\frac1\kappa\int\delta\Lambda(\nu_e-dC_3)
-\frac1\kappa\int d\Lambda\wedge\delta C_3+\int_{\partial M}\theta,
$$
$$
\mathcal E_a=\frac{\epsilon_{abcd}}{2\kappa}e^b\wedge R^{cd}
+\frac b\kappa e^b\wedge R_{ab}
-\frac\Lambda{6\kappa}\epsilon_{abcd}e^b\wedge e^c\wedge e^d,
\qquad
\theta=\frac1{2\kappa}\Sigma^{ab}\wedge(P_b\delta\omega)_{ab}
+\frac\Lambda\kappa\delta C_3.
$$
These signs use $\delta R=D\delta\omega$. Compact support removes the surface integral; another boundary prescription needs its own boundary action and charges. Restricting to torsion zero before varying is not this calculation.

For the adopted split-jet expression, with $r=\sqrt{N_0}$,
$$
e=r^{-1}(D_\omega X+K_JX+wX),\quad
\delta e=r^{-1}\big[(D_\omega+K_J+w)\delta X+
(\delta\omega+\delta K_J+\delta w)X\big].
$$
The already proved surjectivity of $(\delta K_J,\delta w)\mapsto\delta e$ yields $\mathcal E_a=0$. The connection-induced tetrad term is proportional to this same Euler form and vanishes after that equation, leaving $P_bD\Sigma=0$. The X equation follows by integration by parts from the tetrad equation. The auxiliary equations give $d\Lambda=0$ and $dC_3=\nu_e$. This branch-level calculation includes the composite chain rule; it does not construct a unique metric as a functional of Theta alone or the missing microscopic measure.

In real Lorentz signature $\star^2=-1$ and
$$
P_b^{-1}=\frac{b-\star}{1+b^2},\qquad \det P_b=(1+b^2)^3>0.
$$
Consequently the invertible-tetrad, zero-spin Cartan equation gives $T^a=0$ for every real $b$. Bianchi then removes the Holst tetrad contribution and gives Einstein–Lambda, with Lambda constant. Complex self-dual parameters, degenerate tetrads, spin currents, extra torsion terms and nontrivial boundary data are outside this conclusion. The general field variation and Cartan-to-torsion implication remain `LEAN-PENDING`; Lean verifies the explicit bivector inverse and its zero kernel. This is the familiar conditional vacuum equivalence, consistent with [Holst](https://arxiv.org/abs/gr-qc/9511026) and [Barbero et al.](https://arxiv.org/abs/2201.12141), not a new derivation of gravity from information.

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

<!-- BILINGUAL-UNIT: physics-closure.prediction -->
## Nonuniqueness, information principles and prediction boundary

For independent-connection spinless vacuum the entire real $b$ family has the same torsion-free metric equations. Its gravitational characteristics and all protocols confined to that identical metric branch cannot distinguish $b$. This strengthens the existing torsion-free restriction comparison by explicitly checking the invertible vacuum connection operator. Information-access budgets and causal sharing of records restrict protocols; without a new coupling or selection rule they do not remove this degeneracy. Off shell the operators differ, and sourced torsion or other boundary prescriptions may distinguish them. This is nonuniqueness under the tested constraints, not impossibility of a future stronger principle.

On that conditional branch the metric wave characteristic obeys $g^{\mu\nu}k_\mu k_\nu=0$, so $c_{\rm GW}=c$ as in GR. [GW170817/GRB170817A](https://arxiv.org/abs/1710.05834) supplies a published comparison bound $-3\times10^{-15}\le(c_{\rm GW}-c)/c\le7\times10^{-16}$ under its emission-delay assumptions. This is a GR baseline check, not distinctive confirmation of UBT or a measurement of $b$. With spinless vacuum alone there is no nontrivial beyond-GR prediction from this family. A source/torsion experiment would require the same action to derive the normalized spin current and every allowed torsion coefficient first. [Kostelecky–Russell–Tasson](https://arxiv.org/abs/0712.4393) constrain specified fermion–background-torsion couplings; their limits cannot be transferred to an unspecified UBT coefficient. The homogeneous comparator is not a fitted cosmology or an observational prediction.

The precise remaining obstruction is that neither the complete single-Theta action, its composite connection law, its physical fluctuation quotient nor its source normalization has been selected. A surjective kinematic right inverse supplies none of these by itself. Full spatial variations, primary/secondary constraints and physical mode stability remain `OPEN_GAP`. The strongest new calculational result here is the constrained Hamiltonian and its coefficient-dependent strata for the already specified comparator.

<!-- BILINGUAL-UNIT: physics-closure.verification -->
## Verification and exact formal scope

| Result | Scientific status | Verification | Formal boundary |
|---|---|---|---|
| Real bivector inverse, square and zero kernel | PROVED | `formal/lean/UBT/Hamiltonian/PalatiniHolst.lean`; independent SymPy matrix | No derivation of the field Cartan equation |
| Comparator momentum/constraint, zero canonical energy, velocity inversion, completed square | PROVED | Same Lean module; direct CAS differentiation | Finite algebraic identities only |
| Continued canonical GR match and Hermitian-pair readout obstruction | PROVED | Same Lean module; `tests/test_holst_selfdual_canonical_gr.py` | Matching is algebraic; no admissible microscopic self-dual branch established |
| Full homogeneous Poisson matrix, Dirac brackets and constraint strata | CONDITIONAL | `tools/verify_physics_closure.py`; `tests/test_physics_closure.py` | LEAN-PENDING: Poisson/Dirac definitions and geometric reduction |
| Finite differences, covariance, trajectory convergence and precision | NUMERICALLY_TESTED | Same executable verifier, fixed seed and tolerances | Selected regular samples, not proofs |
| Generic torsionful single-Theta dynamics and new physical prediction | OPEN_GAP | Exact missing inputs stated above | LEAN-PENDING: full action, variational spaces and PDE constraints |
| Claim that the one-clock Palatini reduction automatically enforces all Einstein equations | REFUTED | Preserved exact normal-constraint counterexample | Only the stated homogeneous ansatz is excluded |

Run `python tools/verify_physics_closure.py` and `python -m pytest -q tests/test_physics_closure.py tests/test_composite_palatin_holst_flrw.py`. The verifier emits package versions, every exact check, the seed, finite-difference errors, independent integrator convergence and precision residuals. Run `lake build UBT --wfail`, the existing Lean checker and the axiom audit separately. No unchecked theorem source or successful numerical comparison is formal verification. Independent bilingual semantic approval is required before merge; a structurally matched translation alone does not close that gate.
