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

## What this closes and what it does not

**Closed negatively:** the entire original bare kinetic-plus-arbitrary-C2-potential completion with independent algebraic Lorentz connection and central composite metric cannot give a nondegenerate **predictive timelike gravitational sector**. Choosing a cleverer scalar, pseudoscalar, vector, bivector, or tensor *algebraic* potential does not evade the volume-collapse mechanism if after invariant contraction it is just a local radial U. Such a change can alter complex transverse interactions but not restore a nontrivial restricted local gravitational Hessian.

**Open:** whether a *separately justified* connection-curvature invariant, different field-value orbit or new variational principle follows from already accepted UBT principles. Current canonical sources do NOT uniquely derive one action with Einstein/graviton/Yang–Mills dynamics; adding Palatini–Holst by hand is a comparison theory, not a completion. Future work must either derive that term from an independently stated principle, or register that the minimal original formulation fails the gravitational test. No more ad-hoc corrections are authorized by this proof.

**Checker:** `tools/verify_minimal_all_C2_potentials.py` and focused pytest; exact determinant/cofactor, sample witness, C2 plateau and quadratic degeneracy checks. **Prior work:** `canonical/ACTION.en.md`, Proposition 9 `canonical_family_hamiltonian_bridge.en.md`, `timelike_orbit_unitclock.en.md` and merged PR #694.
