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
The determinant $p(a)^2+p(b)^2$ is nonzero for $p(t)\ne0$. Therefore $\delta\Pi=0$ at such covectors. Conversely the vanishing metric Euler symbol satisfies all leading pullback variations. For the supplied Einstein–Hilbert action on the flat family, this reproduces the Einstein **metric** symbol on the nonzero null covectors, including both tidal polarizations. The metric-invisible directions and $p(t)=0$ require a separate constraint analysis. The metric-only action is insensitive to the four common-stabilizer additions exactly because they leave $D_\omega\Theta$ fixed.

<!-- BILINGUAL-UNIT: two-carrier-sharp-reality.verification -->
## Verification and scope

[Exact SymPy 1.14.0 tests](../../tests/test_two_carrier_sharp_reality.py) check the affine metric, complex eikonal identity, parallel scalar and curvature transport, rank change, both transverse amplitudes with vanishing Ricci symbol and explicit connection solutions, and the singular limit. The [Lean 4.33.1 module](../../formal/lean/UBT/Hamiltonian/TwoCarrierSharpReality.lean) checks the finite kernel elimination, the commutator steps of the transport argument and real two-by-two symbol algebra. The analytic proof supplies the geometric linearizations, rank dimensions and local chart.

The comparison changes the tetrad reality condition relative to the classical Lorentz-slice requirement while using the original sharp identity and one real Lorentz connection. Its rank and symbol conclusions are local. A microscopic action, its composite connection selector, compatibility with full complex-time evolution, stability and the physical Dirac count remain open for this comparison.
