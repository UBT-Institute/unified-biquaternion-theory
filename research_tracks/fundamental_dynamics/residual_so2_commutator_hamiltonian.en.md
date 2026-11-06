<!-- BILINGUAL-UNIT: residual-so2-commutator-hamiltonian -->
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


# Three local degrees of freedom in the two-carrier commutator square

**Status.** Conditional comparison, 2026-11-06. This calculation takes the existing commutator-square candidate through residual elimination, the nonlinear local constraint algebra and the physical principal symbol on a stationary flat background.

<!-- BILINGUAL-UNIT: residual-so2-commutator-hamiltonian.action -->
## Action matching and stationary connection

Use the oriented two-carrier Lorentz branch $\Theta=V+iW$, $DV=\kappa e$, $DW=0$, $\kappa=\sqrt{\mathcal N_0}>0$, with future timelike $V$ and $W$ nonparallel to $V$. The derivative acts by the complexified Lorentz-vector representation. In the declared canonical first-jet family, varying $\omega=\omega_0+\alpha J$ at fixed $\Theta,e$ leaves both covariant derivatives unchanged. Its residual equation is identically zero. This follows directly from the [canonical action registry](../../canonical/ACTION.en.md) and the [invariant-basis calculation](residual_so2_invariant_basis.en.md).

For the existing commutator-square candidate, choose the real pairing $B$ whose restriction to the real vector image is $\eta$. Here $T=D_\omega e$ gives the exact relation

$$
[D_\mu,D_\nu]\Theta=\kappa T_{\mu\nu},\qquad
L_{\rm C}=-\frac{\nu}{\kappa^2}
g^{\mu\rho}g^{\nu\sigma}B([D_\mu,D_\nu]\Theta,[D_\rho,D_\sigma]\Theta)
=-\nu I_1,\quad \nu>0 .
$$

The sign gives positive kinetic terms in the reduced quadratic problem below. The commutator identity and the invariant alone leave $\nu$ free. This is the [existing comparison operator](../action_selection/commutator_invariant_action_selection_audit.en.md) restricted to the stated transport family. The [torsion matching](residual_so2_torsion_matching.en.md) gives $c_1=-\nu$, $c_2=c_3=\beta=\gamma=0$ and $\boldsymbol j=0$. Its residual Hessian is invertible and $\alpha_*=0$ throughout the patch. For this comparison, eliminating $\alpha$ is stationary elimination.

<!-- BILINGUAL-UNIT: residual-so2-commutator-hamiltonian.chart -->
## Exact reduced field variables

Keep $c=W^2$ fixed on the local branch and set $r=\sqrt{-V^2}$, $z=(V\cdot W)/r$, $s=\sqrt{c+z^2}$, $m=\kappa s/r$, $h=\kappa/r$ and $l=\kappa z/(rs)$. The transport identities make $\mathrm dr$ and $\mathrm dz$ independent. In coordinates $(r,z,y^2,y^3)$ the metric and unit vectors are

$$
g=-\frac{\mathrm dr^2}{\kappa^2}+\frac{\mathrm dz^2}{m^2}
+\gamma_{AB}(\mathrm dy^A+\beta_r^A\mathrm dr+\beta_z^A\mathrm dz)
(\mathrm dy^B+\beta_r^B\mathrm dr+\beta_z^B\mathrm dz),\qquad
u=\kappa(\partial_r-\beta_r),\quad n=m(\partial_z-\beta_z).
$$

Here $\gamma$ is an arbitrary positive transverse metric and $\beta_r,\beta_z$ are transverse vector fields. The chart reconstructs admissible carriers and connection for all these data. Taking $r,z$ as coordinates fixes two diffeomorphisms. Any compactly supported variation of the carriers within this chart can be compensated in $r,z$ by a compactly supported diffeomorphism since their differentials are independent. Invariance of the comparison action then justifies varying the gauge-fixed data. The remaining transformations are the transverse diffeomorphisms of the leaves at fixed $r,z$. This use of a $2+2$ decomposition is related to the geometric construction of [Yoon](https://arxiv.org/abs/gr-qc/9611050).

Let $\|\cdot\|_\gamma$ denote full transverse contractions, $\rho=\sqrt{\det\gamma}/(\kappa m)$ the volume density, and $[\ ,\ ]$ the transverse Lie bracket. The reference-torsion blocks and the transverse bracket are

$$
\begin{aligned}
\mathcal B&=\tfrac{\kappa}{2}(\partial_r\gamma-\mathcal L_{\beta_r}\gamma)-h\gamma,&
\mathcal C&=\tfrac{m}{2}(\partial_z\gamma-\mathcal L_{\beta_z}\gamma)-l\gamma,\\
\mathcal F&=\partial_r\beta_z-\partial_z\beta_r-[\beta_r,\beta_z],&
2x&=\kappa m\,\mathcal F .
\end{aligned}
$$

The projected Lie derivatives give the two symmetric blocks, and $2x=-P[u,n]$ gives the bracket term. In the reference torsion $T_0$ the mixed components are $\mathcal B,\mathcal C$ and $2x$ with raised transverse output. Their norm is $I_1(T_0)=2(\|\mathcal C\|_\gamma^2-\|\mathcal B\|_\gamma^2-4|x|_\gamma^2)$. The exact stationary density, including its measure, is therefore

$$
\mathcal L_{\rm red}=2\nu\rho\left(
\|\mathcal B\|_\gamma^2-\|\mathcal C\|_\gamma^2+
\kappa^2m^2\|\mathcal F\|_\gamma^2
\right).
$$

<!-- BILINGUAL-UNIT: residual-so2-commutator-hamiltonian.constraints -->
## Nonlinear Hamiltonian and constraint algebra

Use $r$ as time and symmetric tensor contraction for the momentum of $\gamma$. The independent velocities of $\gamma$ and $\beta_z$ have an invertible five-dimensional Hessian, with momenta

$$
P^{AB}=2\nu\rho\kappa\,\mathcal B^{AB},\qquad
\Pi_A=4\nu\rho\kappa^2m^2\gamma_{AB}\mathcal F^B .
$$

The two momenta of $\beta_r$ vanish. The Legendre transform is $H=H_0+G[\beta_r]$ up to a boundary term and primary multipliers, where the integrals are over $z,y^2,y^3$ and

$$
\begin{aligned}
H_0 &=\int\left[
\frac{P^{AB}P_{AB}}{2\nu\rho\kappa^2}
+\frac{\Pi_A\Pi^A}{8\nu\rho\kappa^2m^2}
+\frac{2h}{\kappa}P^{AB}\gamma_{AB}
+2\nu\rho\,\|\mathcal C\|_\gamma^2\right],\\
G[\xi]&=\int\left[P^{AB}\mathcal L_\xi\gamma_{AB}
+\Pi_A(\partial_z\xi+[\xi,\beta_z])^A\right].
\end{aligned}
$$

Preserving the primary constraints gives $G[\xi]=0$ for every compactly supported transverse $\xi$. The canonical generator acts on $(\gamma,\beta_z)$ by $(\mathcal L_\xi\gamma,\partial_z\xi+[\xi,\beta_z])$. The commutator of the field-dependent coefficients in the canonical bracket gives the Lie bracket of the parameters. In the affine component it uses $\partial_z[\xi,\eta]=[\partial_z\xi,\eta]+[\xi,\partial_z\eta]$. Thus $\{G[\xi],G[\eta]\}=G[[\xi,\eta]]$. The terms in $H_0$ are transverse densities and their coefficients depend only on $r,z$. Hence $\{H_0,G[\xi]\}=0$ for the stated support, and preservation ends at the secondary constraints.

The two primary and two secondary constraints are first class. At every regular point an orthonormal transverse frame and the horizontal longitudinal direction put the spatial symbol of the two transverse generators into the rank-two form below. On the regular local sector the count is $(14-2\cdot4)/2=3$ physical canonical pairs per spatial point. This is the Dirac count of the specified reduced comparison.

<!-- BILINGUAL-UNIT: residual-so2-commutator-hamiltonian.symbol -->
## Stationary background and principal frequencies

In Cartesian coordinates $X^a$, take $e^a=\mathrm dX^a$, $V^a=\kappa X^a$, constant nonzero spacelike $W$ and $\omega=0$ on a future-timelike patch. This has $T=0$ and is stationary for the pure square, whose first variation is proportional to $T$. Freeze the principal coefficients in its adapted orthonormal frame. Write $H_{AB}$ for the transverse metric perturbation and $N_A,Z_A$ for the normalized perturbations of the two shifts. Let $k_\parallel$ be the wave covector component along $n$ and $q_A$ its transverse components. The principal quadratic density, up to the frozen volume, is

$$
\frac{\nu}{2}\big(
\|\partial_u H-2\partial_{(A}N_{B)}\|^2
-\|\partial_n H-2\partial_{(A}Z_{B)}\|^2
+4\|\partial_u Z-\partial_n N\|^2\big).
$$

On the five spatial amplitudes $(H,Z)$ the gauge generator has symbol $(B_q\xi,k_\parallel\xi)$, with $(B_q\xi)_{AB}=q_A\xi_B+q_B\xi_A$. It has rank two at any nonzero spatial covector. The potential map $R(H,Z)=k_\parallel H-B_q Z$ annihilates these gauge directions. The kinetic metric is the Frobenius form on symmetric tensors and four times the Euclidean form on vectors. Solving the two momentum constraints and taking the quotient therefore gives the squared frequencies from

$$
R\,\operatorname{diag}(I_3,\tfrac14 I_2)\,R^\dagger
=k_\parallel^2 I_3+\tfrac14 B_qB_q^\dagger .
$$

This equality uses orthonormal tensor coordinates and their adjoints. The nonzero eigenvalues are those of the physical generalized eigenproblem. On the three-dimensional quotient a rank drop of $R$ contributes zero eigenvalues. With $q^2=q_Aq^A$, the three squared frequencies are

$$
\boxed{\omega^2=k_\parallel^2+q^2,\qquad
\omega^2=k_\parallel^2+\tfrac12 q^2,\qquad
\omega^2=k_\parallel^2.}
$$

For a wave along $n$, the transverse trace is the third amplitude in addition to the two traceless amplitudes. For $k_\parallel=0$ and $q\ne0$, one direction has vanishing principal spatial stiffness. These results exclude the pure commutator square as a two-polarization Einstein kinetic sector on this branch. Other operators can change the constraints and principal symbol. A microscopic selection of the full action and composite connection remains open.

<!-- BILINGUAL-UNIT: residual-so2-commutator-hamiltonian.verification -->
## Verification

The [SymPy 1.14.0 tests](../../tests/test_residual_so2_commutator_hamiltonian.py) check the torsion norm, Legendre transform at an arbitrary screen metric, affine generator closure in exact polynomial examples, and the general directional principal symbol. The [Lean 4.33.1 module](../../formal/lean/UBT/Hamiltonian/ResidualSO2Commutator.lean) checks the polynomial gauge-kernel identity and characteristic factorization. The analytic calculation supplies the continuum constraint algebra and the scope of the count.
