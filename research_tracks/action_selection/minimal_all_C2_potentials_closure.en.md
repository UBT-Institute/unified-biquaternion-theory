<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: minimal-C2-action-closure.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact minimal timelike action-family closure; not a no-go for nonminimal or general complex UBT actions.
UBT-AI-PROVENANCE-END -->
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

# Minimal single-Theta action: complete no-dynamics dichotomy for every C2 potential

**Status: EXACT CONDITIONAL NO-GO / WHOLE UBT STILL UNDERDETERMINED.** This strengthens Proposition 9 of `canonical_family_hamiltonian_bridge.en.md`: the negative result no longer requires a quartic, polynomial, analytic, coercive, or nonconstant potential. It uses precisely the already specified minimal kinetic/potential action, positive-Hermitian timelike Lorentz orbit, composite metric, and independent auxiliary spin connection. **No new fundamental term has been proposed.**

## Reused hypotheses, not new assumptions

Consider a connected, oriented smooth four-dimensional patch. On the positive-Hermitian timelike one-Theta branch choose local Lorentz radial gauge and let the independent traceless Lorentz spin connection carry unrestricted boost components. Define the generated coframe:

\[
e_\mu{}^a=\frac1q(\partial_\mu\rho,\rho b_\mu{}^1,\rho b_\mu{}^2,\rho b_\mu{}^3),
\quad q=\sqrt{\mathcal N_0}>0,\quad \rho>0,\quad
g_{\mu\nu}=e_\mu{}^a\eta_{ab}e_\nu{}^b.
\]

Keep the original real Lorentz-invariant bilinear kinetic pairing, the composite metric from its own covariant first derivative, a nonzero real kinetic normalization c, and any real potential U of class C2. Crucially, there are **no independent curvature, connection-derivative or additional action terms**. The exact Lorentz pairing identity from the original Proposition 9 gives

\[
\mathcal B(D_\mu\Theta,D_\nu\Theta)=-2\mathcal N_0g_{\mu\nu},
\quad
S_{\min}=\int_M d^4x\,
|\det e|\,[4c\mathcal N_0-U(\rho)].
\]

## The complete dichotomy theorem

The twelve independent boost variations do not differentiate the connection and give, at fixed orientation,

\[
\frac{\delta S_{\min}}{\delta b_\mu{}^i}=
[4c\mathcal N_0-U(\rho)]\,\frac{\rho}{q}
|\det e|(e^{-1})_i{}^\mu=0.
\]

For an invertible matrix the cofactor/inverse entries associated with each of its spatial columns cannot all vanish. Therefore any stationary nondegenerate configuration must satisfy

\[
\boxed{\det e\ne0\quad\Longrightarrow\quad
U(\rho(x))=4c\mathcal N_0\quad\text{for all }x.}
\]

An invertible tetrad cannot have a zero radial-gradient column:

\[
\det e=\frac{\rho^3}{q^4}
\det[\partial\rho,b^1,b^2,b^3]\ne0
\quad\Longrightarrow\quad d\rho\ne0.
\]

By the submersion theorem the image of rho contains an open interval near every point. The boost Euler equation therefore forces the potential to have a **constant-level plateau** at exactly the kinetic volume coefficient:

\[
\boxed{
d\rho\ne0\quad\Longrightarrow\quad \rho(\mathcal U)
\text{ contains an open interval }I\subset(0,\infty),\qquad
U|_I\equiv4c\mathcal N_0.
}
\]

This proves the unconditional **either-or classification for every C2 radial potential in the specified branch**: **(A)** if the relevant level set contains no open interval, no nondegenerate stationary solution exists; **(B)** if it contains a nonempty open interval, every stationary nondegenerate configuration takes its radial values locally inside such an interval and the entire minimal action is identically zero in a neighborhood of that configuration within the timelike reduced field space:

\[
S_{\min}\big|_{\rho\in I}=0,\qquad
\boxed{
\delta S_{\min}\big|_{\mathcal U}=0,\quad
\delta^2S_{\min}\big|_{\mathcal U}=0
}
\quad\text{for compactly supported variations staying inside }I.
\]

Thus the local Euler and Hessian operators vanish on all compactly supported variations kept within this plateau. The branch has **no nontrivial local gravitational equations or quadratic kinetic operator from this minimal action**. This is not a claim about transverse complex degrees of freedom away from the Lorentz-real timelike field manifold.

## Why allowing arbitrary smooth functions does not rescue the branch

An explicit globally nonconstant C2 example with a constant plateau is

\[
U(\rho)=4c\mathcal N_0+
\begin{cases}
(1-\rho)^4,&\rho<1,\\
0,&1\le\rho\le2,\\
(\rho-2)^4,&\rho>2,
\end{cases}
\quad U\in C^2,\quad U\not\equiv\mathrm{const}.
\]

On that plateau there are locally smooth nondegenerate solutions, for example

\[
\rho=qt,\quad 1<qt<2,\qquad
b_i{}^j=\frac{q}{\rho}\delta_i{}^j,\quad b_0{}^j=0
\quad\Longrightarrow\quad e_\mu{}^a=\delta_\mu{}^a.
\]

But they are only **unconstrained stationary geometries of an identically vanishing restricted action**, not derived gravitational dynamics. Polynomial and real-analytic nonconstant potentials do not have open plateaus and therefore fall in case (A). If U is constant and equals the required value, the entire action is trivial; if its constant differs, no invertible stationary coframe is allowed.

## Entire positive-Hermitian Lorentz orbit, not merely an arbitrary gauge choice

For a general positive Hermitian X, local SL(2,C) congruence gives a smooth radialization

\[
X>0,\quad r=\sqrt{\det X},\quad
S=\sqrt r\,X^{-1/2}\in SL(2,\mathbb C),\quad
SXS^\dagger=rI.
\]

Since the original minimal action and U are Lorentz invariant and the spin connection transforms accordingly, the dichotomy holds on the whole local positive-Hermitian timelike orbit under these stated premises. It does **not** cover generic non-Hermitian complex Theta, nonzero independent curvature terms, a different microscopic measure or a derived higher-derivative action.

## Independent obstruction: declared symmetries do not uniquely select an action

Even before testing equations of motion, the original Lorentz-congruence and U(1)-phase symmetries leave independent derivative-free scalar invariants. Take the existing quadratic invariant H and the determinant. At two explicit field values,
\[
X_1=I_2,\quad X_2=I_2+i\sigma_1,\qquad
(H(X_1)^2,|\det X_1|^2)=(4,1),\quad
(H(X_2)^2,|\det X_2|^2)=(0,4).
\]
\[
\boxed{\det\begin{pmatrix}4&1\\0&4\end{pmatrix}=16\ne0.}
\]
Their evaluation matrix has nonzero determinant; hence H² and |det X|² are linearly independent as functions on the full eight-real field space. Each separately respects the **same declared symmetries**. No symmetry argument using only those premises can fix their relative coefficients, choose an on-shell vacuum, or derive the missing curvature coefficient. Therefore the action-selection gap is a **real mathematical underdetermination**, not a bookkeeping issue. A dynamical selection principle must be independently derived or the theory must be acknowledged as underdetermined; selecting terms solely to fit GR is additional model input.

## Stronger closure: every natural algebraic first-jet Lagrangian

**Orbit-reduction theorem (no new axiom):** Consider any local differentiable action density, not necessarily polynomial, which is a scalar density under spacetime diffeomorphisms, invariant under local proper orthochronous Lorentz transformations, and constructed **algebraically only** from the existing timelike Lorentz vector X, its invertible coframe e=D X/q, the invariant Lorentz tensors eta and epsilon, and inverses/contractions. No other background tensors, explicit spin curvature, independent connection kinetic term, derivatives of e, or fields beyond X and its auxiliary Lorentz connection are allowed. Fix an orientation and time-orientation patch.

Under those *precise* conditions every such local density is

\[
\boxed{\mathcal L_{\mathrm{alg}}(X,e)=|\det e|\,F(r),\qquad
r=\sqrt{-\eta_{ab}X^aX^b},\qquad
e^a=q^{-1}D_\omega X^a.}
\]

**Proof:** At a given point, invertibility of e permits a linear change of spacetime coordinates taking the coframe matrix to the identity. There can be no independent spacetime-index invariant remaining after this operation, because all coordinate indices are contracted and no other spacetime tensors were supplied. The residual internal proper Lorentz symmetry acts transitively on each future-timelike hyperboloid, whose only invariant is r. Therefore the normalized scalar density is a smooth function F(r); epsilon contractions only affect the constant orientation factor. This proof covers nonlinear and nonpolynomial contractions of any degree, as long as they obey the explicitly stated algebraic first-jet field-content restriction.

Metric compatibility of the spin connection yields a **gauge-independent** radial-gradient identity:

\[
d(X^aX_a)=2X_aD_\omega X^a=2qX_ae^a,\qquad
\boxed{dr=-\frac{q}{r}X_ae^a,\quad g^{-1}(dr,dr)=-q^2.}
\]

In particular an invertible timelike coframe forces dr nonzero without any extra assumption of homogeneous clocks. In the local radial Lorentz gauge, each auxiliary boost varies one spatial column independently, so stationarity gives

\[
\frac{\delta S_{\mathrm{alg}}}{\delta b_\mu{}^i}=
\frac r q|\det e|\,(e^{-1})_i{}^\mu F(r)=0,
\qquad
\boxed{\det e\ne0\Longrightarrow F(r)=0.}
\]

Since dr is nowhere zero, its local image contains an open interval I, on which the reduced scalar coefficient vanishes identically:

\[
\boxed{r(\mathcal U)\supset I,\quad F|_I\equiv0,\quad
S_{\mathrm{alg}}|_{\mathcal U}=0,\quad
\delta S_{\mathrm{alg}}|_{\mathcal U}=0,\quad
\delta^2 S_{\mathrm{alg}}|_{\mathcal U}=0.}
\]

All allowed small compactly supported variations remaining within that interval have identically zero restricted action and all restricted variational derivatives. The result therefore rules out **predictive timelike gravitational dynamics throughout the entire natural algebraic first-jet class**, not merely the quadratic kinetic pairing or scalar/pseudoscalar/bivector potential labels.

**Sharp boundary:** The local group-orbit reduction is a geometric proof, not a finite computational exhaustive enumeration; the supplementary exact checker tests frame normalization, epsilon volume, Lorentz covariance, projector identities and boost cofactors in nontrivial examples. The theorem does NOT cover covariant derivatives of e, spin curvature, torsion terms containing de, derivative-dependent couplings, independent background structures, non-Hermitian Theta, global holonomies, or the transverse complex variation of the full field. In particular it cannot decide whether any such operator must arise from UBT principles. **Without a justified operator outside this class, the current premises do not provide a dynamical theory of gravity.**

## Why the remaining action choice is mathematically underdetermined

The above no-go closes the **algebraic first-jet class**. It does not follow from the existing field definition and Lorentz/diffeomorphism symmetry that a unique curvature or torsion term must replace it.

**Constructive non-uniqueness certificate, not a proposed action:** The earlier explicitly representable closed-FLRW coframe of merged PR #685 has pure trace torsion with

\[
T^0=0,\quad T^i=\chi\,e^0\wedge e^i,\quad
\chi=H-\frac1V,\quad
\boxed{T^a{}_{\mu\nu}T_a{}^{\mu\nu}=-6\chi^2.}
\]

Thus the parity-even diffeomorphism/Lorentz scalar built from the torsion square is not an identically vanishing function of the existing fields. Even if a curvature term had been selected, the equally symmetry-compatible family

\[
S_\lambda=S_{\mathrm{curv}}+
\lambda\int_M\sqrt{-g}\,
T^a{}_{\mu\nu}T_a{}^{\mu\nu}\,d^4x,\qquad
\lambda\in\mathbb R.
\]

contains a free coefficient not fixed by these symmetries. The torsion-square term has a nonzero first variation when (chi
e0), so it is not merely an irrelevant additive constant. This shows **why the advertised principles alone do not select unique dynamics**: no amount of algebraic rearrangement of the existing Theta pairing determines the independent higher-jet coefficient. The expression is an illustration of underdetermination, **NOT** an adopted UBT extension.

At this point the possible mathematically honest outcomes are: derive an extra selection principle from independently grounded prior physics; restrict the claimed target of UBT to its valid kinematic content; or explicitly acknowledge an **underdetermined dynamical theory**. Arbitrarily choosing a convenient (lambda), a Palatini–Holst coefficient, or a CMB kernel does not complete the original theory.

## Test of another existing premise: complex-time holomorphy

The preexisting exact audit `research_tracks/theta_complex_time_classification/holomorphy_lorentz_no_go.md` supplies a separate consistency obstruction. If `psi` is an independent Lorentz **scalar**, and the full microscopic field is strictly holomorphic in `tau` in every inertial frame, then the Cauchy–Riemann and opposite-boost equations are
\[
\tau=t+i\psi,\qquad \partial_\psi\Theta=i\partial_t\Theta,\qquad
\partial_{t'_\pm}=\gamma(\partial_t\pm v\partial_x).
\]
\[
(\gamma-1)\partial_t\Theta\pm\gamma v\partial_x\Theta=0
\quad\Longrightarrow\quad
\partial_t\Theta=\partial_x\Theta=\partial_\psi\Theta=0
\quad (v\ne0).
\]
Repeating the same argument for other spatial directions removes generic spacetime dependence. Therefore **that conjunction of old premises cannot independently select a nontrivial gravitational action**. This does NOT exclude a reduced holomorphic theta kernel, a distinguished frame not advertised as Lorentz invariant, or a fully covariant complexification of spacetime with transforming imaginary coordinates. Those are **different formulations**, whose field content and dynamics would need independent justification.

The proof is already separately verified; no new holomorphy axiom has been introduced here. It joins the minimal-action no-go and the explicit symmetry-only action nonuniqueness as a consistency audit, not a universal failure theorem for every possible UBT realization.

## What this closes and what it does not

**Closed negatively:** the entire original bare kinetic-plus-arbitrary-C2-potential completion with independent algebraic Lorentz connection and central composite metric cannot give a nondegenerate **predictive timelike gravitational sector**. Choosing a cleverer scalar, pseudoscalar, vector, bivector, or tensor *algebraic* potential does not evade the volume-collapse mechanism if after invariant contraction it is just a local radial U. Such a change can alter complex transverse interactions but not restore a nontrivial restricted local gravitational Hessian.

**Open:** whether a *separately justified* connection-curvature invariant, different field-value orbit or new variational principle follows from already accepted UBT principles. Current canonical sources do NOT uniquely derive one action with Einstein/graviton/Yang–Mills dynamics; adding Palatini–Holst by hand is a comparison theory, not a completion. Future work must either derive that term from an independently stated principle, or register that the minimal original formulation fails the gravitational test. No more ad-hoc corrections are authorized by this proof.

**Checker:** `tools/verify_minimal_all_C2_potentials.py` and focused pytest; exact determinant/cofactor, sample witness, C2 plateau and quadratic degeneracy checks. **Prior work:** `canonical/ACTION.en.md`, Proposition 9 `canonical_family_hamiltonian_bridge.en.md`, `timelike_orbit_unitclock.en.md` and merged PR #694.
