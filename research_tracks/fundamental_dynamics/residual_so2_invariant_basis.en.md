<!-- BILINGUAL-UNIT: residual-so2-invariant-basis -->
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


# Local invariant basis for the residual SO(2) connection

**Status.** Conditional local theorem for the two-carrier Lorentz lift, 2026-11-06. The result classifies the dependence on the residual connection within a specified derivative filtration. The microscopic UBT action and its physical mode count remain open.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.setup -->
## Branch, reference connection and derivative count

Work on a smooth, oriented and time-oriented Lorentzian four-dimensional patch with a nondegenerate tetrad $e$. In the restricted vector representation write $\Theta=V+iW$, where $V,W$ are the two real Lorentz vectors and $D=\mathrm d+\omega$ acts on each by the Lorentz-vector representation. Impose

$$DV=\kappa e,\qquad DW=0,\qquad \kappa=\sqrt{\mathcal N_0}>0.$$

Take $V$ future timelike and $W$ independent of $V$. Set

$$r=\sqrt{-V^2},\qquad z=(V\cdot W)/r,\qquad c=W^2,\qquad s=\sqrt{c+z^2}>0.$$

Here $c$ is locally constant. Convert $V/r$ and $(W+zV/r)/s$ to spacetime vectors $u,n$ with $e^{-1}$. Then $u^2=-1$, $n^2=1$ and $u\cdot n=0$. Let $P$ project onto the Euclidean plane perpendicular to both. Let $J$ generate its oriented rotations, with $J^2=-P$. We identify internal and spacetime tensors by the tetrad. The volume form and these carriers are the only zeroth-order tensor data, together with the metric. Coefficients may be arbitrary smooth functions of $r,z,c$. Matter, external tensors, global holonomies and boundary degrees of freedom are outside the classification.

Use the Levi-Civita spin connection $\mathring\omega(e)$ to define a reference $\omega_0$. Among the solutions of the two transport equations choose the one with $P(\omega_0-\mathring\omega)P=0$. Existence and uniqueness follow from the [two-carrier kernel theorem](two_vector_connection_kernel.md), since the difference of any two solutions has only the transverse rotation block. Write

$$\omega=\omega_0+\alpha J,\qquad A=A_0+\alpha,\qquad F=\mathrm dA=F_0+\mathrm d\alpha.$$

$A$ is the induced connection of the oriented transverse frame. Under a rotation of that frame, $A$ and $A_0$ both shift by $\mathrm d\chi$, and the difference $\alpha$ is a tensorial one-form. The branch treats $q=(g,r,z,c)$ as fixed when comparing its connection representatives. Write $\Delta_\alpha L=L(\omega_0+\alpha J)-L(\omega_0)$ at fixed $q$.

Use Levi-Civita jets in the reduced variables. Assign weight $1$ to $\alpha$ and to each derivative. Thus $\nabla^k\alpha$ has weight $k+1$ and Levi-Civita curvature has weight $2$. Assign weight $0$ to the algebraic carriers and coefficient functions. First use the transport identities to replace $\mathrm dr,\mathrm dz$ and constrained components of the first jets. This is a filtration on the reduced geometry, since the transport identities are inhomogeneous in derivative weight. Consider local covariant scalar densities polynomial in the weighted variables through weight $2$. The classification is modulo densities independent of $\alpha$ and local total divergences. This grading is a choice for the restricted branch. Counting derivatives after a pullback to the original $\Theta$ requires the composite map.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.reduction -->
## Curvature, torsion and integration by parts

With $T=D_\omega e$ and $R=\mathrm d\omega+\omega\wedge\omega$, the exact differences are

$$T-T_0=\alpha\wedge Je,\qquad R-R_0=J\,\mathrm d\alpha+(D_0J)\wedge\alpha.$$

In particular the total Lorentz curvature difference can contain a term even when $\mathrm d\alpha=0$. The first and second Cartan Bianchi identities are $D_\omega T=R\wedge e$ and $D_\omega R=0$. The induced Abelian curvature satisfies $\mathrm dF=0$. The two-derivative Nieh–Yan relation is

$$\mathrm d(e_a\wedge T^a)=T_a\wedge T^a-e^a\wedge e^b\wedge R_{ab}.$$

For a variable multiplier $f$, integrating $f\,\mathrm d(e_a\wedge T^a)$ also leaves the bulk term $-\mathrm df\wedge e_a\wedge T^a$. For constant $f$ the combination is a boundary term.

The torsion is algebraically equivalent to the metric-compatible contortion. In particular $\alpha J=P(\omega-\mathring\omega)P$ can be extracted from it. The reference contortion $\omega_0-\mathring\omega$ is linear in the prescribed images $\kappa e-\mathring D V$ and $-\mathring D W$ by the two-carrier construction. It therefore has weight at most $1$. The same bound holds for $D_0J$. After the curvature and torsion substitutions, the only possible derivative of $\alpha$ through weight $2$ is linear. With Levi-Civita $\nabla$ and compactly supported variations, its reduction is

$$\sqrt{|g|}\,C^{\mu\nu}\nabla_\mu\alpha_\nu
\ \equiv\ -\sqrt{|g|}\,(\nabla_\mu C^{\mu\nu})\alpha_\nu,$$

where $C$ has weight $0$. Thus curvature-linear and differentiated-torsion terms contribute to the algebraic basis. The Bianchi identities hold for every smooth $\alpha$ in this parametrization and impose no further independent restriction on its jets.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.jets -->
## Independent first jets of the carriers

Metric compatibility gives $\mathrm d(V^2)=2\kappa V\cdot e$ and $\mathrm d(V\cdot W)=\kappa W\cdot e$. Hence

$$u^\flat=-\mathrm dr/\kappa,\qquad n^\flat=\frac{r}{\kappa s}\,\mathrm dz,\qquad
\mathrm du^\flat=0,\qquad \mathrm dn^\flat=-\frac{\kappa}{r}u^\flat\wedge n^\flat.$$

Write $X_{\mu\nu}=\nabla_\mu u_\nu$ and $Y_{\mu\nu}=\nabla_\mu n_\nu$. In the orthonormal frame $(u,n,e_2,e_3)$, use $A,B$ for the transverse indices and define

$$x=P\nabla_n u,\qquad k_u=P^{\mu\nu}X_{\mu\nu},\qquad k_n=P^{\mu\nu}Y_{\mu\nu}.$$

The unit and orthogonality identities together with the exterior derivatives above give

$$
X=\begin{pmatrix}
0&0&0\\
0&\kappa/r&x_B\\
0&x_A&X_{AB}
\end{pmatrix},
\qquad
Y=\begin{pmatrix}
0&0&-x_B\\
-\kappa/r&0&0\\
-x_A&0&Y_{AB}
\end{pmatrix},
\qquad X_{AB}=X_{BA},\quad Y_{AB}=Y_{BA}.
$$

The free entries are realizable. In coordinates $(r,z,y^2,y^3)$ take

$$
g=-\frac{\mathrm dr^2}{\kappa^2}+\frac{r^2\,\mathrm dz^2}{\kappa^2s^2}
+\gamma_{AB}\bigl(\mathrm dy^A+\beta^A\bigr)\bigl(\mathrm dy^B+\beta^B\bigr),
\qquad \beta^A=\beta_r^A\,\mathrm dr+\beta_z^A\,\mathrm dz.
$$

At a point take $\gamma_{AB}=\delta_{AB}$ and $\beta^A=0$. The derivatives $\partial_r\gamma,\partial_z\gamma$ set $X_{AB},Y_{AB}$ independently through the projected Lie derivatives of $g$. The derivatives $\partial_r\beta_z-\partial_z\beta_r$ set $x=-P[u,n]/2$ independently. The carrier fields reconstructed as $V=r\,e(u)$ and $W=-z\,e(u)+s\,e(n)$ satisfy the scalar transport compatibility conditions. The two-carrier kernel theorem therefore supplies a smooth local connection for these data.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.theorem -->
## Complete basis and independence

Let $a=\alpha(u)$, $b=\alpha(n)$ and $p=P\,g^{-1}\alpha$. A basis over smooth functions of $r,z,c$ is

| Weight | Dependence | Representatives |
| --- | --- | --- |
| $1$ | Linear | $a,\ b$ |
| $2$ | Linear | $a k_u,\ a k_n,\ b k_u,\ b k_n,\ p\cdot x,\ p\cdot Jx$ |
| $2$ | Quadratic | $a^2,\ ab,\ b^2,\ p\cdot p$ |

To see completeness, the transverse rotation group acts trivially on $a,b$ and by its standard real two-dimensional representation on $p$. Its invariant symmetric forms on the residual one-form are the three longitudinal forms and the transverse norm. The first jets provide two free scalar traces and one transverse vector. Their two traceless symmetric blocks transform with twice the frame angle, so they supply neither scalars nor vectors linearly. The vector $x$ and its oriented rotation $Jx$ are the two intertwiners into the transverse representation. The fixed entry $\kappa/r$ contributes only to coefficients of $a,b$. This exhausts the possible terms after integration by parts.

For independence, a relation modulo a divergence and an $\alpha$-independent density would have zero Euler derivative with respect to arbitrary compactly supported $\delta\alpha$ at fixed $q$. Its terms linear in $\alpha$ force all four quadratic coefficients to vanish. The independently realizable traces and $x$ then force the other eight coefficients to vanish. No equations of motion or field redefinitions are used in the equivalence.

An exact illustration distinguishes curvature and torsion. The [field-built shift](field_built_so2_connection_family.en.md) is $\Delta\alpha=(\lambda/r)n^\flat=\lambda\,\mathrm dz/(\kappa s)$. For constant $\lambda$, $\mathrm d\Delta\alpha=0$, while $\Delta T=\Delta\alpha\wedge Je$ is nonzero for $\lambda\ne0$. On the flat witness in that work its scalar norm is $4\lambda^2/r^2$. Equality of the induced curvatures therefore leaves inequivalent full connection representatives under ordinary frame rotations.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.palatini-holst -->
## Hilbert–Palatini and Holst in this basis

Consider the two curvature-linear comparison densities built with the defining connection $\omega$. Take $e^0=-u^\flat$, $e^1=n^\flat$, $J^{23}=1$ and $\sigma=e^2\wedge e^3$. Write $h=\kappa/r$, $l=\kappa z/(rs)$ and let $f=f(r,z,c)$. The transport equations give the mixed components $\omega^A{}_0=h e^A$ and $\omega^A{}_1=l e^A$ for each transverse index $A$. The mixed components of $D_0J$ are therefore proportional to the coframe form in the other transverse direction. In the Hilbert–Palatini contraction that same coframe form occurs in the complementary pair and the wedge product vanishes. The $\mathrm d\alpha$ coefficient is proportional to $f e^0\wedge e^1$, which is closed by the carrier identities. Hence

$$\Delta_\alpha\bigl(f\,\epsilon_{abcd}\,e^a\wedge e^b\wedge R^{cd}\bigr)\equiv0.$$

For Holst, integrate $f e_a\wedge e_b\wedge D_0(\alpha J^{ab})$ by parts. The remaining torsion contraction uses

$$T_0^2\wedge e^3-T_0^3\wedge e^2=\mathrm d\sigma-2(h e^0+l e^1)\wedge\sigma.$$

Evaluating $\mathrm d\sigma$ on the adapted frame gives

$$\mathrm d\sigma=k_u e^0\wedge\sigma+k_n e^1\wedge\sigma+2 e^0\wedge e^1\wedge\iota_x\sigma.$$

With $\mathrm{vol}=e^0\wedge e^1\wedge\sigma$, the bulk difference is

$$
\Delta_\alpha\bigl(f\,e_a\wedge e_b\wedge R^{ab}\bigr)
\ \equiv\ -2\,\mathrm{vol}\left[
  \bigl(u(f)+f(k_u-2h)\bigr)b-\bigl(n(f)+f(k_n-2l)\bigr)a-2f\,p\cdot x
\right].
$$

Thus Hilbert–Palatini is blind to the residual shift in the bulk, while a nonzero constant Holst coefficient imposes $k_u=2h$, $k_n=2l$ and $x=0$ in the independent residual comparison. Both have $M=0$. These restrictions come from varying within the two-carrier transport family with the same defining connection. Full Palatini variations and actions using a separate physical connection are different variational problems.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.hamiltonian -->
## First Hamiltonian consequence

For an independent residual variation at fixed $q$, use the component column $\boldsymbol a=(a,b,p_2,p_3)^T$. Up to the volume factor the general residual density is

$$
L_{\rm res}=\boldsymbol j^T\boldsymbol a+\tfrac12\boldsymbol a^T M\boldsymbol a,\qquad
M=M_{\parallel}\oplus m_\perp I_2,\qquad
\operatorname{rank}M=\operatorname{rank}M_{\parallel}+2\,\mathbf 1_{m_\perp\ne0}.
$$

The residual velocity Hessian vanishes. In the fixed-geometry Hamiltonian comparison the primary constraints are $\boldsymbol\pi=0$, the secondary equations are $M\boldsymbol a+\boldsymbol j=0$, and their mutual Poisson bracket block is $-M$ after removing the nonzero volume factor from the secondary equations. Where $M$ is invertible these are eight second-class constraints. The residual variable is auxiliary and its stationary elimination adds $-\tfrac12\boldsymbol j^T M^{-1}\boldsymbol j$ to the density divided by the volume factor. This term can change the kinetic Hessian of the other fields. Where $M$ is singular the source projected onto its kernel must vanish. With dynamical $q$, that condition can constrain the other fields, and terms linear in their velocities can alter the symplectic form. The full constraint algebra is required in that case. If $M=0$ and $\boldsymbol j=0$ identically, the independent bulk comparison has an arbitrary local shift symmetry in $\alpha$. Its status on the physical quotient also depends on the other sectors, observables and boundary conditions.

For a preassigned composite $\alpha[\Theta]$, the variation of a functional written as $S[\Theta,\alpha]$ obeys

$$
\mathcal E_\Theta S[\Theta,\alpha[\Theta]]
=\left.\mathcal E_\Theta S[\Theta,\alpha]\right|_{\alpha[\Theta]}
+(D\alpha[\Theta])^\dagger
\left.\mathcal E_\alpha S[\Theta,\alpha]\right|_{\alpha[\Theta]}.
$$

The dagger is the formal adjoint under the specified boundary conditions. In the first term the variation already includes the dependence of the other geometric data on $\Theta$. A smooth stationary branch of the auxiliary equation makes the second term vanish and justifies elimination. A kinematic composite recipe alone gives no such identity. The basis supplies the terms to match against the selected single-field action. Its coefficients, the actual composite response and the full physical reduction remain open.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.curvature-comparison -->
## Counting derivatives of an independent potential

The term quadratic in $\mathrm d\alpha$ has weight $4$ in the Cartan count above. In a comparison which counts an independent potential as order $0$, a quadratic curvature term instead uses two derivatives of that potential. In the frame above, write

$$E=F_{01},\qquad B=F_{23},\qquad {\bf E}_A=F_{0A},\qquad {\bf C}_A=F_{1A}.$$

The algebraic quadratic curvature block, using only the zeroth-order geometry, has seven monomials before boundary reductions:

$$
E^2,\ EB,\ B^2,\quad {\bf E}^2,\ {\bf C}^2,\ {\bf E}\cdot{\bf C},\
\epsilon^{AB}{\bf E}_A{\bf C}_B.
$$

Choose $\epsilon^{23}=1$ and the matching spacetime orientation. The combination $2(EB-\epsilon^{AB}{\bf E}_A{\bf C}_B)$ is $F\wedge F$ divided by the oriented volume. It is locally exact at constant coefficient, by $\mathrm dF=0$. With variable coefficient, the exact transgression relative to $F_0$ leaves

$$
f(F\wedge F-F_0\wedge F_0)\ \equiv\ -\mathrm df\wedge\alpha\wedge(F+F_0).
$$

The two electric squares alone contribute to the velocity Hessian of the independent potential. On the foliation normal to $u$, its spatial block has one longitudinal eigenvalue and a doubly degenerate transverse eigenvalue. A curvature-only comparison with both eigenvalues nonzero has the usual primary and Gauss constraints of an Abelian gauge potential, giving two local polarizations for fixed geometry. This count uses the exact-shift symmetry of that comparison and supplies no composite mode count.

<!-- BILINGUAL-UNIT: residual-so2-invariant-basis.verification -->
## Verification and related work

The [exact tests](../../tests/test_residual_so2_invariant_basis.py) pass with SymPy 1.14.0. They check the first-jet realization, the invariant and Euler map ranks, the closed field-built shift, the Palatini–Holst contractions, and the curvature block and its velocity Hessian. The [Lean proof](../../formal/lean/UBT/Hamiltonian/ResidualSO2Basis.lean) passes with Lean 4.33.1. It proves injectivity of the finite Euler map over a characteristic-zero field. The coordinate realization and the argument using arbitrary variations establish the stated continuum result. Formal verification is partial and covers the finite independence argument. Continuum geometry, the microscopic action and its physical constraints remain outside the formal check.

[Zhang, Hu and Gao](https://arxiv.org/abs/2611.08191) give a model for separating monomial enumeration, boundary reduction and constraint analysis. [Andrei and Dioguardi](https://arxiv.org/abs/2611.06750) illustrate stationary elimination in a metric-affine action with independent distortion. [Izaurieta, Lepe and Quinzacara](https://arxiv.org/abs/2611.08422) analyze spin-source selection in Einstein–Cartan cosmology. These are separate theories. Matter currents and observational predictions in this UBT branch require their own action and variation.
