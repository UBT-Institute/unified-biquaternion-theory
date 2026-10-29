<!-- BILINGUAL-UNIT: physics-closure.appendix-action-family -->
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

# Action family and independent variation

[Audit overview](physics_closure_2026_10.en.md).

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
