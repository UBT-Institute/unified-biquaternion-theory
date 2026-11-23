<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.scope -->
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

# Real sharp metric with two Lorentz carriers

**2026-11-07 · C_working · conditional local result.** The parallel reference still loses a transverse Einstein tidal amplitude when the first-order deformation is allowed to have a complex tetrad. Explicit flat backgrounds with a complex tetrad and a real sharp metric recover both amplitudes kinematically. A separate principal-symbol result uses a supplied metric action. The comparison continues the [quadratic torsion polarization obstruction](residual_so2_quadratic_cone.en.md).

The 2026-11-16 extension gives the local degree count for this supplied action and detects nonreal scalar frequencies at its flat vacuum reference.

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.domain -->
## Exact metric reality and transport

Use smooth fields on a four-dimensional patch, a timelike $V$ and an independent real $W$, with $\Theta=V+iW$ in the complexified Lorentz-vector representation. Set $\kappa=\sqrt{\mathcal N_0}>0$ and $\eta=\operatorname{diag}(-1,1,1,1)$. The defining connection is real Lorentz transport $D_\omega Z=\mathrm d Z+\omega Z$ extended complex linearly. Its two-sided spin realization is $D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu$ with $A_\mu=\Omega_\mu$, $B_\mu=-\Omega_\mu^\ddagger$. A dot denotes the complex bilinear extension of the Lorentz pairing. Matrices have the base index in their columns.

\[
X=\kappa^{-1}D_\omega V,\qquad Y=\kappa^{-1}D_\omega W,\qquad
E=X+iY,\qquad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf 1,\qquad
g=E^T\eta E .
\]

Here $X$ is invertible and the entire central coefficient of the sharp anticommutator equals a real Lorentzian $g$. This comparison allows $Y\ne0$ outside the classical Lorentz slice for $E$. The real metric is imposed as an exact condition on the full identity. The independent variables for the kinematic test are $V,W$ and compatible choices of the defining $\omega$, prior to any composite selector. Local Lorentz frame changes and diffeomorphisms act on the original fields. The action comparison below uses the same admissible variations.

Set $G=X^T\eta X$ and $\Lambda=YX^{-1}$. The imaginary coefficient vanishes precisely when $\Lambda^T\eta+\eta\Lambda=0$. Metric reality then gives the first formula below. The second identity follows from $\mathrm d\chi=2\kappa E^T\eta\Theta$, since the connection preserves the bilinear pairing and $E$ is invertible.

\[
g=X^T\eta(I+\Lambda^2)X,\qquad
\chi=\Theta\cdot\Theta,\qquad
g^{-1}(\mathrm d\chi,\mathrm d\chi)=4\kappa^2\chi,\qquad
t=E^{-1}\Theta=\frac{g^{-1}\mathrm d\chi}{2\kappa}.
\]

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.parallel -->
## Linear obstruction at a flat parallel reference

Write $r=\sqrt{-V^2}$, $z=V\cdot W/r$, $c=W^2$, $s=\sqrt{c+z^2}$, $v=X^{-1}V$, $w=X^{-1}W$ and $\ell=X^{-1}\Lambda X$. Metric-compatible transport of the three scalar pairings gives the following identities, with $a=G^{-1}\mathrm d(rz)/\kappa$. In the second line use the skewness of $\ell$ with respect to $G$.

\[
v^\flat_G=-\frac r\kappa\,\mathrm dr,\qquad
\ell v=w-a,\qquad \ell w=-\frac{G^{-1}\mathrm dc}{2\kappa},
\qquad w(c)=0 ,
\]
\[
G^{-1}(\mathrm dr,\mathrm dr)=-\kappa^2,\qquad
G^{-1}(\mathrm dr,\mathrm dz)=0,\qquad
G(a,a)=c-\kappa^{-1}v(c)+G(\ell v,\ell v).
\]

At a parallel reference $Y=0$, $c$ is constant, $a=w$ and $\delta g=\delta G=h$. The gradients of $r,z$ are independent by the two carrier transport equations and invertibility of $X$. Fix $\delta r=\delta z=0$ by diffeomorphisms and set $u=v/r$ and $n=(w+zu)/s$ on the reference. Linearization of the preceding identities gives
\[
h(u,u)=h(u,n)=0,\qquad
H:=s^2 h(n,n)=\kappa^{-1}v(\delta c)-\delta c,\qquad
w(\delta c)=0.
\]
For the flat affine parallel reference in Cartesian gauge, $X=I$, $\omega=0$, $V=V_0+\kappa x$ and $W=W_0$. Then $[w,v]=\kappa w$, so $w(H)=0$ exactly at first order. There is also an exact curvature transport statement. Use $R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho_{\nu\sigma}-\partial_\nu\Gamma^\rho_{\mu\sigma}+\cdots$ and let $\partial^2_{a,b}h$ denote Cartesian second partial derivatives with $a,b$ held fixed in the differentiation. The product rule, $\partial_\mu v^\nu=\kappa\delta_\mu^\nu$, and $h(v,v)=h(v,w)=0$ give
\[
2\delta R(v,w,v,w)=2(\partial^2_{v,w}h)(v,w)
-(\partial^2_{v,v}h)(w,w)-(\partial^2_{w,w}h)(v,v)
=-v(v(H))-\kappa v(H).
\]
It follows from the commutator that $w(\delta R(v,w,v,w))=0$. This linearized curvature is gauge invariant on the flat reference. Since $\delta R(v,w,v,w)=r^2s^2\delta R_{unun}$, its principal tidal amplitude vanishes when $p(w)\ne0$. For a nonzero null $p$ with $p(n)=0$ and $z\ne0$, one has $p(w)=-z p(u)\ne0$. The transverse plus polarization has a nonzero value of $\delta R_{unun}$. The transport test leaves the exceptional covectors $p(w)=0$ open. The conventional Einstein polarization tensors are given in [the linearized GR notes](https://www.damtp.cam.ac.uk/user/us248/Lectures/Notes/short.pdf#page=75).

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.rank -->
## Fixed-carrier image on a regular complex background

Assume $V,W,\Lambda V,\Lambda W$ are linearly independent at the point. Hold the values and first derivatives of $V,W$ fixed. Normalize $X=I$ at the point by a real base change, write $v=V$, $w=W$ in these components and set $P=\delta X$, $Q=\delta Y$. By the [two-vector compatibility theorem](two_vector_connection_kernel.md), the response to $\delta\omega$ is exactly the set satisfying $v^\flat P=w^\flat Q=w^\flat P+v^\flat Q=0$. The kernel of the response has four real components, one stabilizer parameter per base index.

The reality tangent is $Q=\Lambda P+L$ with $L$ real Lorentz-skew. The three transport constraints become
\[
v^\flat P=0,\qquad
(\Lambda w)^\flat P=w^\flat L,\qquad
(w-\Lambda v)^\flat P=-v^\flat L .
\]
The three covectors on the left are independent. For each of the six parameters in $L$ there are four free components of $P$, one per column. The constrained $(P,Q)$ space thus has dimension ten. In the original connection variables the imaginary-metric differential has rank ten, since the unconstrained $(P,Q)$ response has dimension twenty. The implicit function theorem gives a smooth local reality chart at fixed carriers and allows these tangent variations with compact support.

For zero real metric response in this space, the full complex response also vanishes. Writing $J=I+i\Lambda$, every such variation is $\delta E=(R+iS)J$ with $R,S$ real Lorentz-skew. It gives $P=R-S\Lambda$, $Q=S+R\Lambda$. The three transport constraints imply
\[
Rv=-\Lambda Sv,\qquad Sw=\Lambda Rw,\qquad
(I+\Lambda^2)(Rw+Sv)=0 .
\]
The last factor $I+\Lambda^2$ is invertible. For $m=Sv$, the four images are $Sv=m$, $Rw=-m$ and $Rv=Sw=-\Lambda m$. The skewness of $R,S,\Lambda$ makes $m$ orthogonal to $v,w,\Lambda v,\Lambda w$. Thus $m=0$. Both $R,S$ may be chosen independently in the one-dimensional common stabilizer. The zero metric kernel in $(P,Q)$ has dimension two, and the real metric image has rank eight. The total fixed-carrier connection kernel on the reality tangent has dimension six.

Write $t=a+ib$ for the real and imaginary parts of $t$. From $Jt=v+iw$ one obtains $(I+\Lambda^2)a=v+\Lambda w$ and $(I+\Lambda^2)b=w-\Lambda v$. Thus $a,b$ are real linearly independent. Holding the carriers fixed holds $\chi$ and $\mathrm d\chi$ fixed. The linearization of the complex eikonal identity imposes two independent real conditions. These characterize the rank-eight image.
\[
\boxed{\ \operatorname{im}(\delta_\omega g\mid\delta g\ \text{real})
=\{h\in\operatorname{Sym}^2_{\mathbb R}:h(t,t)=0\}\ .\ }
\]
On the parallel reference with $w^2\ne0$, $Q$ is skew and annihilates $w$, so it has three free components. At fixed $Q$, the constraints on $P$ leave eight free components. The zero metric kernel consists of skew $P$ with $Pv=0$, $Pw=-Qv$, which has one free component per $Q$ by two-vector compatibility. The image rank there is $11-4=7$.

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.null -->
## Null polarizations and the singular parallel limit

At any real covector $p$ with $p(t)\ne0$, a real symmetric amplitude $h_0$ has a diffeomorphism representative in the rank-eight image. Choose a real covector $\xi$ with $\xi(t)=-h_0(t,t)/(2p(t))$, possible because $a,b$ are independent. Then $h=h_0+p\otimes\xi+\xi\otimes p$ satisfies $h(t,t)=0$. This adjustment preserves the principal linearized Riemann tensor. If $\operatorname{Re}t$ is timelike, every nonzero real null $p$ meets the condition.

For an explicit flat family let $e_0,e_1,e_2,e_3$ be the standard internal basis and take
\[
V_0=e_0,\quad W_0=\tfrac12e_0+e_1,\quad
\Lambda=\varepsilon
\begin{pmatrix}
0&0&1&0\\
0&0&0&-1\\
1&0&0&0\\
0&1&0&0
\end{pmatrix},\quad
V=V_0+\kappa x,\quad W=W_0+\kappa\Lambda x,\quad \omega=0 .
\]
Then $X=I$, $Y=\Lambda$ and $g=\operatorname{diag}(-1-\varepsilon^2,1-\varepsilon^2,1+\varepsilon^2,1-\varepsilon^2)$ is constant and Lorentzian for $|\varepsilon|<1$. At the origin the determinant of $[V,W,\Lambda V,\Lambda W]$ is $\varepsilon^2$. The real part of $t$ is timelike there for sufficiently small $|\varepsilon|$, by continuity from $t=V+iW$ at $\varepsilon=0$. These properties extend to a patch at each sufficiently small nonzero $\varepsilon$.

The fixed-carrier lifts need not stay bounded in the parallel limit. At the origin and $p=(1,0,1,0)$, the component $h_{11}$ is unaffected by the symbol diffeomorphism. Reality gives $(P_1)^1=-2\varepsilon(P_1)^3$ for the column $P_1$ because $(Q_1)^1=(P_1)^1/2$. Hence
\[
h_{11}=-4\varepsilon(P_1)^3-2\varepsilon(Q_1)^3 .
\]
A fixed nonzero $h_{11}$ therefore requires a fixed-carrier connection variation of size at least a constant times $|\varepsilon|^{-1}$ in this family.

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.stationarity -->
## Conditional test with a metric action

Supply a diffeomorphism-invariant metric action $S_0[g]$ without direct carrier or defining connection dependence. Use compactly supported variations in the regular reality chart. Denote its metric Euler tensor by $\Pi^{\mu\nu}$ using the metric volume density. At a stationary point of the pullback, the fixed-carrier $\omega$ variation forces $\Pi$ into the span of $a\otimes a-b\otimes b$ and $a\otimes b+b\otimes a$. Around a background with $\Pi=0$, the leading linearized Euler tensor has the same normal form with coefficients $A,B$. The diffeomorphism identity $\nabla_\mu\Pi^{\mu\nu}=0$ gives at principal order
\[
p_\mu\delta\Pi^{\mu\nu}
=(A p(a)+B p(b))a^\nu+(-A p(b)+B p(a))b^\nu=0 .
\]
The determinant $p(a)^2+p(b)^2$ is nonzero for $p(t)\ne0$. Therefore $\delta\Pi=0$ at such covectors. Conversely the vanishing metric Euler symbol satisfies all leading pullback variations. For the supplied Einstein–Hilbert action on the flat family, this reproduces the Einstein **metric** symbol on the nonzero null covectors, including both tidal polarizations. The metric-only action is insensitive to the four common-stabilizer additions exactly because they leave $D_\omega\Theta$ fixed.


<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.quotient -->
## Local metric and scalar variables

On the regular branch of the rank calculation, hold the first jet of $\Theta$ fixed and impose exact metric reality. The map from the fourteen remaining real connection components to the eight metric coordinates has constant rank eight. At fixed $\chi,\mathrm d\chi$ the complex equation
\[
C(g,\chi)=g^{-1}(\mathrm d\chi,\mathrm d\chi)-4\kappa^2\chi=0
\]
has rank two in the real metric variables, since $D_g C[h]=-4\kappa^2 h(t,t)$ and $a,b$ are independent. The implicit function theorem gives a local chart with eight metric coordinates and six free connection coordinates. It also gives a local inverse for each nearby metric satisfying $C=0$. The theorem applies with the carrier jet as a parameter. The map $(V,W)\mapsto\chi$ has rank two because the gradients of $\operatorname{Re}\chi$ and $\operatorname{Im}\chi$ are independent for independent $V,W$. Thus the other six real coordinates of $\Theta$ can be varied at fixed $\chi$ in the chart. The two remaining metric components are determined by $C=0$ and depend only on the eight metric coordinates and $\chi,\mathrm d\chi$.

The action $S_0[g]$ is independent of the six connection coordinates along each fiber and the six carrier coordinates left at fixed $\chi$. Variations of these coordinates can have arbitrary compact support with $g,\chi$ fixed. In a chart with these coordinates the momenta conjugate to them vanish as first-class constraints with no secondary constraints. Four of the six fixed-carrier connection directions are the arbitrary one-form shifts in the common $SO(2)$ stabilizer. The other two change the tetrad while preserving its metric and $\chi$.

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.multiplier -->
## Equivalent constrained action and presymplectic current

For the Hamiltonian analysis take $S_0$ to be the supplied Einstein–Hilbert action with its usual boundary convention and compactly supported interior variations. The local chart gives the same stationary equations modulo its arbitrary coordinates as the multiplier formulation
\[
S_{\mathrm{ext}}[g,\chi,\lambda]
=S_0[g]+\int \sqrt{-g}\,\operatorname{Re}\bigl(\lambda C(g,\chi)\bigr)\,\mathrm d^4x,\qquad
\lambda\in\mathbb C .
\]
Both constraints are enforced by varying $\lambda$. The original connection variations force $\Pi$ into the real span of the two normals of $C$ and therefore determine a unique smooth $\lambda$. For variations with $\delta C=0$, the chain rule gives
\[
\Pi^{\mu\nu}=4\kappa^2\operatorname{Re}(\lambda t^\mu t^\nu),\qquad
\Pi^{\mu\nu}h_{\mu\nu}
=\operatorname{Re}\!\left(\lambda\left[2\partial^\mu\chi\,\partial_\mu\delta\chi-4\kappa^2\delta\chi\right]\right).
\]
Variations of $\chi$ are arbitrary with the two solved metric components adjusted. Integration by parts yields $\nabla_\mu(\lambda t^\mu)+\kappa\lambda=0$. This equation also follows from the contracted Bianchi identity. Indeed, $t^\flat=\mathrm d\chi/(2\kappa)$ and $g(t,t)=\chi$ imply $\nabla_t t=\kappa t$. Taking the real part of the divergence of $\lambda t^\mu t^\nu$ then gives the complex transport equation because $a,b$ are independent. Conversely, solutions of the multiplier equations give stationary configurations in the original chart by the local inverse.

The integration by parts adds the boundary potential
\[
\vartheta^\mu_\chi
=2\sqrt{-g}\,\operatorname{Re}(\lambda\,\partial^\mu\chi\,\delta\chi).
\]
It agrees with the scalar contribution of $S_{\mathrm{ext}}$. The gravitational potential also agrees since the metric is the same. The identities hold along every solution and tangent in the chart, so the local covariant presymplectic currents agree on shell up to the usual boundary ambiguity.

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.dirac -->
## Dirac reduction including zero multiplier

Use a spacelike slice with spatial metric $\gamma_{ij}$, determinant $\gamma$, lapse $N>0$ and shift $N^i$. Use a patch where $a$ is timelike, as in the flat family for small nonzero $\varepsilon$. The complex normal derivative of $\chi$ is nonzero. Introduce a temporary complex normal derivative variable $\zeta$ and a complex momentum density $P$. Put $s_\chi=\gamma^{ij}\partial_i\chi\,\partial_j\chi-4\kappa^2\chi$. The scalar part of the first-order Lagrangian density is
\[
\operatorname{Re}\bigl[P(\dot\chi-N^i\partial_i\chi-N\zeta)\bigr]
+N\sqrt{\gamma}\,\operatorname{Re}\bigl[\lambda(s_\chi-\zeta^2)\bigr].
\]
Eliminating $P$ recovers $S_{\mathrm{ext}}$. The primary momenta for $\zeta,\lambda$ vanish. Their four real secondary constraints are the two complex relations
\[
s_\chi-\zeta^2=0,\qquad P+2\sqrt{\gamma}\lambda\zeta=0,\qquad
\det_{\mathbb R}\frac{\partial(s_\chi-\zeta^2,\ P+2\sqrt{\gamma}\lambda\zeta)}
{\partial(\zeta,\lambda)}=16\gamma|\zeta|^4 .
\]
The determinant follows by taking the squared modulus of the complex triangular determinant. Thus these constraints and the four primary momenta are second class even at $P=\lambda=0$. Eliminate them using the local square-root choice $Z^2=s_\chi$ with $Z\ne0$. The reduced scalar symplectic potential and the additions to the Hamiltonian and momentum constraints are
\[
\operatorname{Re}(P\,\delta\chi),\qquad
\mathcal H_\chi=\operatorname{Re}(P Z),\qquad
\mathcal D_i^\chi=\operatorname{Re}(P\,\partial_i\chi).
\]
The scalar normal-normal bracket is
\[
\{H_\chi[N],H_\chi[M]\}=
\int (N\partial_i M-M\partial_i N)\gamma^{ij}\mathcal D_j^\chi\,\mathrm d^3x .
\]
Indeed $Z\,\partial Z/\partial(\partial_i\chi)=\gamma^{ij}\partial_j\chi$, and all terms with no derivatives of the smearing functions cancel. The antisymmetrized cross bracket with the gravitational normal constraint vanishes because $\mathcal H_\chi$ has no spatial metric derivatives or metric momentum and the momentum derivative of the gravitational constraint is algebraic. The total momentum constraint generates spatial diffeomorphisms on the scalar and metric variables. The four total ADM constraints are first class together with the four lapse and shift momenta. After eliminating the chart coordinates and the algebraic constraints there are twelve configuration variables including lapse and shift. The local Dirac count is $(24-2\cdot 8)/2=4$. Two canonical pairs come from $\chi$, in addition to the two of the metric tensor sector.

The subspace $P=0$ is invariant under the Hamiltonian equations when the evolution exists, because the Hamiltonian dependence on $\chi$ is linear in $P$. There the metric satisfies the vacuum Einstein equation and the restriction of the scalar presymplectic potential vanishes. In the full action variations of $P$ are present even at $P=0$, and the scalar symplectic form has its two canonical pairs.

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.hyperbolicity -->
## Nonreal scalar frequencies on the flat branch

Linearize about a flat solution with $\lambda=0$ in the regular family. Set $\delta g=\delta\lambda=0$. The remaining equation is
\[
(t^\mu\partial_\mu-\kappa)\delta\chi=0 .
\]
These perturbations lift to the original chart. At the flat reference a diffeomorphism preserving $\delta g=0$ is generated by a Killing vector, and the arbitrary chart coordinates preserve $\chi$. The high-frequency scalar amplitudes therefore survive the gauge quotient. For a real spatial covector $k_i$ the determinant of the real two-component principal symbol is
\[
(a^0\nu-a^i k_i)^2+(b^0\nu-b^i k_i)^2,\qquad
\operatorname{disc}_{\nu}=-4\bigl[(a^0 b^i-b^0 a^i)k_i\bigr]^2 .
\]
Here $\nu$ is the frequency relative to $x^0$. Since $a$ is timelike and independent of $b$, the discriminant is negative for an open set of $k_i$ in any spacelike slicing. At the affine origin for $\varepsilon=1/3$ and a wave along $x^1$, one of the two frequencies is exactly $\nu=(1/2+i)k_1$. The conjugate pair exhibits frozen principal growth with rate proportional to $|k_1|$. Hence the full linearized comparison fails strong hyperbolicity even at zero scalar momentum. The earlier Einstein result concerns the metric amplitudes at real null covectors. The hyperbolicity condition follows from the reality of characteristic speeds. [Reula, Hyperbolic Methods for Einstein's Equations](https://doi.org/10.12942/lrr-1998-3).

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.verification -->
## Verification and scope

[Exact SymPy 1.14.0 tests](../../tests/test_two_carrier_sharp_reality.py) check the affine metric, complex eikonal identity, parallel scalar and curvature transport, rank change, both transverse amplitudes with vanishing Ricci symbol and explicit connection solutions, and the singular limit. The [Lean 4.33.1 module](../../formal/lean/UBT/Hamiltonian/TwoCarrierSharpReality.lean) checks the finite kernel elimination, the commutator steps of the transport argument and real two-by-two symbol algebra. The analytic proof supplies the geometric linearizations, rank dimensions and local chart.

The Hamiltonian extension adds exact SymPy tests of the auxiliary Jacobian, square-root Hamiltonian and bracket coefficient, the discriminant, a rational flat-branch witness and affine transport. Independent exact integer arithmetic checks the auxiliary determinant and discriminant on finite examples, including zero multiplier, and the rational frequency. **LEAN-PENDING at preparation.** The added Lean lemmas specify the finite determinant, bracket coefficient and discriminant, with compilation recorded by repository CI. The rank argument, variational equivalence and Dirac count are analytic.

The comparison changes the tetrad reality condition relative to the classical Lorentz-slice requirement while using the original sharp identity and one real Lorentz connection. Its rank and symbol conclusions are local. A microscopic action, its composite connection selector and compatibility with full complex-time evolution remain open. The degree count and hyperbolicity result apply to the supplied metric action on its regular branch.
