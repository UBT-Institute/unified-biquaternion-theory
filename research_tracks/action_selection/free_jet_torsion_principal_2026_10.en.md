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

# Free Lorentz-jet quadratic torsion: the missing tensor gradient

<!-- BILINGUAL-UNIT: free-jet-tensor.scope -->
## Status and precise question

**C_working; conditional principal-block obstruction.** The [flat-jet calculation](flat_jet_torsion_action_2026_10.en.md) has no tensor metric directions. Here the Lorentz jet is allowed to be curved and the relative real dilation is unrestricted. This restores local tensor coframe directions, but does not select an action. We test the supplied constant parity-even quadratic jet-torsion family on a timelike gravity-carrier patch and at a locally isotropic background. After all twelve rotational jet auxiliaries are varied, its principal transverse-traceless (TT) quadratic form has a time derivative but no spatial derivative. Changing its three coefficients cannot restore the GR tensor wave operator in this declared branch.

The principal calculation is a necessary high-frequency test, not a full constraint analysis, a physical mode count or a universal UBT no-go. A separate exact stationary background below is non-Einstein and shows that the supplied action also fails to select Einstein vacuum. Null, spacelike and anisotropic branches, additional jet functionals and the full complex-time/matter system are outside the calculation. The canonical tetrad and central sharp metric are retained; no projection, averaging, additional propagating connection or fundamental Theta component count is introduced.

<!-- BILINGUAL-UNIT: free-jet-tensor.chart -->
## Composite variables before the tensor test

Let $s=\sqrt{\mathcal N_0}>0$, $\eta=\operatorname{diag}(-1,1,1,1)$ and let $X$ be the Lorentz-real gravity representative of Theta. Specify the two-sided action and its vector realization by

\[
D_J\Theta=d\Theta+A_J\Theta-\Theta B_J,\quad
A_J=\Omega_J+\tfrac12wI,\quad B_J=-\Omega_J^\ddagger-\tfrac12wI,
\quad \Omega_J=\rho_*(\varpi),
\]
\[
sE^a=dX^a+\varpi^a{}_bX^b+wX^a,\qquad
g_{\mu\nu}=\eta_{ab}E^a_\mu E^b_\nu.
\]

The jet connection $\varpi$ is metric compatible and is distinct from the physical Levi-Civita connection. Neither $R(\varpi)=0$ nor $dw=0$ is imposed. On a smooth timelike patch choose a local Lorentz gauge $X=(r,0,0,0)$, $r>0$. This aligns a vector; it does not declare the original field to be a central scalar. Then

\[
w=\frac{sE^0-dr}{r},\qquad
\varpi^i{}_0=\varpi^0{}_i=\frac{s}{r}E^i,\qquad
Z_\mu{}^{ij}=\varpi_\mu{}^{ij}=-Z_\mu{}^{ji}.
\]

Thus a general nondegenerate coframe, $r$ and all twelve $Z_\mu{}^{ij}$ provide adapted local variables for this declared configuration space. The change includes $dr$: it is a change of field histories with compactly supported variations, not an asserted point canonical transformation. We do not reuse the independent-connection Einstein equations. The scalar and other helicity blocks are not solved here.

<!-- BILINGUAL-UNIT: free-jet-tensor.principal -->
## Principal quadratic torsion family

Use $T_J^a=dE^a+\varpi^a{}_b\wedge E^b$, $t_\mu=T^\nu{}_{\mu\nu}$ and metric-only contractions

\[
I_1=T_{\rho\mu\nu}T^{\rho\mu\nu},\qquad
I_2=T_{\rho\mu\nu}T^{\nu\mu\rho},\qquad I_3=t_\mu t^\mu,
\quad
S=\frac1{2\kappa}\int\sqrt{-g}(c_1I_1+c_2I_2+c_3I_3),\quad \kappa>0.
\]

At a locally orthonormal isotropic background put the spatial wave direction along $x^3$ and choose a symmetric TT coframe perturbation

\[
\delta E^0=0,\qquad \delta E^i{}_j=\tfrac12\gamma_{ij},\qquad
\gamma=\begin{pmatrix}u&v&0\\v&-u&0\\0&0&0\end{pmatrix}.
\]

Keep every rotational perturbation $Z_\mu{}^{ij}$. In the principal quadratic calculation $\partial\gamma$ and $Z$ have the same derivative order because $Z$ is eliminated algebraically. Background coefficients and the boost variation $(s/r)\delta E^i$ contribute lower derivative terms. The retained linear torsion is therefore

\[
\delta T^0{}_{\mu\nu}=0,\qquad
\delta T^i{}_{\mu\nu}
=\tfrac12(\partial_\mu\gamma_{i\nu}-\partial_\nu\gamma_{i\mu})
+Z_\mu{}^i{}_j\delta^j_\nu-Z_\nu{}^i{}_j\delta^j_\mu,
\qquad \gamma_{i0}=0.
\]

This is the leading quadratic form after algebraic elimination, not a claim that the full mixed differential/algebraic system has already been reduced. Rotational isotropy separates this tensor block from scalar and vector perturbations. The explicit stationary background below supplies a regular setting for this test, but no general background classification or stability result is inferred.

<!-- BILINGUAL-UNIT: free-jet-tensor.elimination -->
## Varying the auxiliaries removes spatial stiffness

The nine spatial rotations map invertibly to the nine spatial torsion components. An explicit stationary choice for every $(c_1,c_2,c_3)$ is

\[
Z_0{}^{ij}=0,\qquad
Z_k{}^{ij}=\tfrac12(\partial_j\gamma_{ik}-\partial_i\gamma_{kj}),
\qquad \delta T^i{}_{jk}=0.
\]

Write $u_t=\partial_0u$, $v_t=\partial_0v$, $u_z=\partial_3u$, $v_z=\partial_3v$. Direct contractions at that solution give

\[
I_1^{(2)}=-(u_t^2+v_t^2),\qquad
I_2^{(2)}=-\tfrac12(u_t^2+v_t^2),\qquad I_3^{(2)}=0.
\]

The conclusion also holds at singular coefficient choices: translating $Z$ by the displayed solution writes the principal numerator as $-(c_1+c_2/2)(u_t^2+v_t^2)+\tfrac12 y^THy$, where $H$ is the full twelve-dimensional auxiliary Hessian and is independent of $u_z,v_z$. Every stationary $y$ satisfies $Hy=0$, hence $y^THy=0$. Unfixed auxiliary directions cannot restore spatial tensor energy. The temporal rotational block is $2(c_2-2c_1)\sum_{i<j}(Z_0{}^{ij})^2$ and has no TT-velocity mixing.

For the positive Einstein-sign comparison use $(c_1,c_2,c_3)=(-1/4,-1/2,1)$, with the curvature convention fixed in the flat-jet note. The spatial auxiliary Hessian has rank nine and the three temporal rotations are undetermined in this principal block. To display the algebra, order spatial rotations as $(z_3,z_4,z_5)=(Z_1^{12},Z_1^{13},Z_1^{23})$, $(z_6,z_7,z_8)$ analogously for $Z_2$, and $(z_9,z_{10},z_{11})$ for $Z_3$. Define

\[
(a,b,c,d,e,f,g,h,i)
=(z_3,z_4-u_z/2,z_5-v_z/2,z_6,z_7-v_z/2,z_8+u_z/2,z_9,z_{10},z_{11}),
\]
\[
Q=2(hd-ia+bf-ce+cg-eg).
\]

The numerator is $(u_t^2+v_t^2)/2+Q$. Its nine linear auxiliary Euler equations have the unique spatial solution $a=b=\cdots=i=0$. This is stationarity of an indefinite auxiliary quadratic form, not minimization or proof that its unconstrained variables have positive energy.

<!-- BILINGUAL-UNIT: free-jet-tensor.hamiltonian -->
## Time kinetic term survives; the GR wave operator does not

The stationary principal tensor density and its regular Legendre transform are

\[
\mathcal L_{\rm TT,prin}=A_T(u_t^2+v_t^2),\qquad
A_T=-\frac{2c_1+c_2}{4\kappa},
\]
\[
p_u=2A_Tu_t,\quad p_v=2A_Tv_t,\qquad
\mathcal H_{\rm TT,prin}=\frac{p_u^2+p_v^2}{4A_T}\quad(A_T\ne0).
\]

The positive Einstein-sign choice gives $A_T=1/(4\kappa)>0$. Its tensor time kinetic term has the positive GR normalization, but both spatial derivatives have disappeared. For $A_T\ne0$ the principal equations are $\partial_0^2u=\partial_0^2v=0$; their Fourier polynomial is proportional to $\omega^2$ without $|\mathbf k|^2$. At $A_T=0$ this block has no kinetic term either. Neither case supplies the GR tensor wave operator. Lower derivative terms and additional constraints remain to be computed, so this is not a claim of two physical propagating modes or a complete dispersion relation.

Freezing every rotational perturbation before variation would instead give

\[
\mathcal L_{\rm TT,prin}\big|_{Z=0}
=A_T(u_t^2+v_t^2-u_z^2-v_z^2).
\]

That attractive wave form is not the stationary free-jet result. Ordinary teleparallel equivalence uses a flat inertial connection with a different admissible variation space; the present result does not refute it. See [Krššák et al., sections IV and IX](https://arxiv.org/abs/1810.12932) for that standard context. The next action-origin test must derive a connection law or additional functional that retains spatial tensor stiffness after the complete composite variation. Merely retuning $(c_1,c_2,c_3)$ in this family cannot do so. No such microscopic selection or Newton coefficient is derived here.

<!-- BILINGUAL-UNIT: free-jet-tensor.stationary-witness -->
## A regular exact stationary background outside Einstein vacuum

Use dimensionless local time $t>0$, $a(t)=\exp(t^2/2)$ and

\[
E^0=dt,\quad E^i=a(t)\,dx^i,\quad
X=(s/t,0,0,0),\quad
w=(t+1/t)dt,\quad
\varpi^i{}_0=\varpi^0{}_i=tE^i,\quad Z^{ij}=0.
\]

Direct substitution gives $sE=dX+\varpi X+wX$, $X^2=-s^2/t^2<0$ and $T_J=0$, while $R(\varpi)\ne0$. The jet and Levi-Civita connections happen to coincide on this background; they are not identified throughout the varied theory. For every coefficient choice the full first variation of the supplied action vanishes: terms linear in $\delta T$ contain a factor $T$, and variations of the metric, volume and composite readout multiply two factors of $T$. Compact support avoids boundary contributions. This argument includes the induced variation of $E$ and requires no gauge-fixed field equation.

Nevertheless the coordinate Ricci tensor obeys

\[
R_{00}=-3(1+t^2),\qquad
R_{ij}=(1+3t^2)g_{ij},\qquad
R_{00}+R_{11}/g_{11}=-2.
\]

The last quantity would be zero if $R_{\mu\nu}=\Lambda g_{\mu\nu}$, for any $\Lambda$. This is a local, regular, original-field non-Einstein stationary witness for the entire supplied family. It does not depend on solving the perturbation constraints, and does not classify all stationary metrics. Along this isotropic solution the missing principal tensor gradient is therefore not merely an off-shell-background artefact.

<!-- BILINGUAL-UNIT: free-jet-tensor.verification -->
## Verification and formal boundary

`tools/verify_free_jet_torsion_principal.py` performs 41 exact checks: full torsion contractions, all twelve auxiliary equations, the invertible spatial Cartan map, coefficient-independent translation, singular stationary values, the explicit Einstein polynomial, Legendre algebra, absent spatial principal coefficient, and the original-field stationary witness with coordinate Ricci curvature. Its independent NumPy path constructs original nonflat metric-compatible jets with $X=(r,0,0,0)$, reconstructs both $E$ and its derivative, and solves the full twelve-variable original quadratic action by a pseudoinverse. Thirty-two seeded samples rotate both TT polarizations and the wave direction and include generic and degenerate coefficient choices. At a node of the perturbation the coframe value is unperturbed, while its derivatives are nonzero; subtracting the exact background action isolates the principal quadratic density. The report states numerical errors and tolerances. These samples do not prove a general field theorem.

The 42 new pytest cases and 47 related flat-jet/composite-chain regressions are the targeted local suite. `formal/lean/UBT/GR/FreeJetTensor.lean` encodes seven finite algebraic cores: coefficient, recentering, nine-variable stationarity, stationary singular quadratic value, zero-torsion first variation, Legendre identity and positive time coefficient. **LEAN-PENDING** until strict root build, independent `leanchecker UBT` and axiom audit succeed; actual source-bound CI status is recorded in `reports/free_jet_torsion_principal_2026_10_29.json`. The continuum chart, derivative-order argument, helicity separation, complete constrained system and microscopic dynamics are outside these finite proofs. Structural EN/CS parity is not independent semantic approval. Canonical gap statuses and provenance tiers are unchanged.
