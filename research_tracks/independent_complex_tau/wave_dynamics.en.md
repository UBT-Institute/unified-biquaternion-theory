<!-- BILINGUAL-UNIT: c5-wave.scope -->
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

# Wave dynamics: composite jets and transverse complex fluctuations

Date: 2026-10-10. Status: **DERIVED_WITH_ASSUMPTIONS [L1] / OPEN_GAP**. The previous [auxiliary test](auxiliary_action.en.md) has no derivative term in its quadratic action. Here we test two remaining restricted possibilities and state a conditional propagation diagnostic. A first-order equation can propagate waves; a vanishing second-order symbol alone is not a no-wave theorem.

The common-coordinate composite test uses the same real five-dimensional model as the overview. The transverse test separately uses the existing four-dimensional symplectic action on the full eight-real-component field space. It is not an action derived on the complete complex coordinate domain. Tau remains independent; no identification with spacetime time is made. These are tests of existing candidate structures, not new fundamental terms or a change of canonical status.

<!-- BILINGUAL-UNIT: c5-wave.composite -->
## A derivative-dependent connection can still be a coordinate change [L1]

On a smooth oriented real patch, set the extra fixed form to ds and consider

\[
E^a=M^a{}_b(X,s)\,dX^b+N^a(X,s)\,ds,\qquad
e=(E^a,ds),\quad \det e>0,\quad \det M>0.
\]

Take an invertible map Y below and the same self-contracted kinetic family as before. The determinant and action reduce exactly to

\[
Y=(X^0,X^1,X^2,X^3,s),\qquad
\det e=\det M\,\det DY,
\]
\[
S=\mathcal T\int F(X,s)\det e\,d^5Z
=\mathcal T\int Y^*\!\left[F(X,s)\det M(X,s)\,d^4X\wedge ds\right].
\]

The target form has top degree, so its exterior derivative vanishes. Cartan's variation formula makes the complete bulk variation zero for compactly supported field variations. This includes the variation of M and N. All bulk variations of this restricted functional vanish; a nonintegrable M need not give a flat metric, but its target geometry is fixed and Y only changes coordinates. Opposite fixed orientation signs do not change the local null-variation conclusion.

This is a genuine derivative-connection example. In a flat reference frame, let the Lorentz correction and relative-central form be

\[
K_{Aab}=f(X^2,s)(X_a\partial_A X_b-X_b\partial_A X_a)
+h(X^2,s)\epsilon_{abcd}X^c\partial_A X^d,
\quad w_A=b(X^2,s)X\cdot\partial_A X+c(X^2,s)(ds)_A.
\]
\[
E_A=\partial_A X+K_AX+w_AX
=(1-fX^2)\partial_A X+(f+b)X(X\cdot\partial_A X)+cX(ds)_A.
\]

Thus this entire displayed family has the preceding form. The dual term annihilates X. Its two-sided biquaternion action is the one specified in the auxiliary note, with the jet coefficients now prescribed composites and the reference connection zero. They are not independently varied. This does not classify every derivative-dependent connection: dependence coupling distinct coordinate directions, higher jets or an implicit differential connection remains outside this theorem. The result extends the existing gradient-volume argument [U1, U2].

<!-- BILINGUAL-UNIT: c5-wave.transverse -->
## Quadratic action of the transverse complex components [L1]

Use the existing symplectic candidate [U3, U4], with a fixed flat connection in its zero gauge. All fields are smooth on a contractible real spacetime patch and variations have compact support. The Lorentz-real background has an invertible ordinary coframe. Write

\[
\Theta_0=b_aX^a,\quad b_0=iI,\quad b_k=-i\sigma_k,
\quad \delta\Theta=b_a\chi^a+i b_a\xi^a,
\quad H_{ab}=-2\eta_{ab},\quad \eta=\operatorname{diag}(-1,1,1,1).
\]
\[
S_F=\frac12\int F(\Theta)Q\wedge Q,\qquad
Q=\frac12\omega(d\Theta\wedge d\Theta),\qquad
\omega(b_au^a,i b_bv^b)=H_{ab}u^av^b.
\]

Here F is the coefficient of the existing symplectic action, unrelated to the coefficient in the preceding volume test. The field-space symplectic form is not used to define a new physical metric. The Lorentz slice is Lagrangian, so the background Q and its first variation along chi vanish. The background is stationary for this action. For the unrestricted transverse perturbation define

\[
a:=\omega(\delta\Theta,d\Theta_0)=-H_{ab}\xi^a dX^b,
\qquad \delta Q=da,\qquad F_0=F(\Theta_0).
\]

The map from xi to the one-form a is invertible because H and the coframe are invertible. The quadratic coefficient of the complete action is therefore

\[
\boxed{S^{(2)}=\frac12\int F_0\,da\wedge da
=-\frac12\int dF_0\wedge a\wedge da
+\frac12\int_{\partial U}F_0a\wedge da.}
\]

Variations of F first enter at higher order because the background Q is zero. No restricted jet-density Hessian is substituted for the bulk action here. The tangent components chi are in the full quadratic kernel. Transverse variations need not preserve a real physical metric; their physical admissibility is a separate question.

<!-- BILINGUAL-UNIT: c5-wave.symbol -->
## First-order symbol and local degeneracy [L1]

Varying the displayed quadratic functional gives

\[
\boxed{dF_0\wedge da=0.}\qquad
v=dF_0,\qquad
A^{\mu\nu}(k)=\epsilon^{\mu\nu\rho\sigma}v_\rho k_\sigma,
\quad A(k)v=A(k)k=0.
\]

The epsilon is the coordinate permutation symbol; the Fourier factor i is omitted from the symbol. For independent covectors v and k, A has rank two. Its Pfaffian vanishes identically, and a linear change of basis sending v and k to the first coordinate covectors gives one nonzero antisymmetric block. For parallel v and k its rank is zero. A determinant zero for every k is not a light-cone dispersion relation.

If F is constant on the patch, the entire quadratic bulk action is a boundary term. On a patch where v never vanishes, use F as a local coordinate. The equation says that a restricts to a closed one-form on every level hypersurface. The local Poincare lemma then gives

\[
a=d\chi+f\,dF_0.
\]

Here chi and f are local scalar functions; chi is distinct from the tangent components above. Both shifts in this expression are local null symmetries of the quadratic bulk functional: the first leaves da unchanged; the second leaves its integrated bulk term unchanged. Thus every local solution is degenerate in that quadratic theory, including the exceptional parallel-covector directions. This calculation supplies no conventional propagating local polarization or distinguished wave cone. It does not exclude boundary/global modes. These symmetries may be accidental to quadratic order; they are not declared gauge symmetries of the full nonlinear UBT theory. Nonlinear constraints or strong coupling require a separate analysis. Curved or composite connections change the step identifying delta Q with da and are not covered.

<!-- BILINGUAL-UNIT: c5-wave.diagnostic -->
## What a successful propagation calculation must yield

For comparison only, suppose a selected physical mode has the following constant-coefficient quadratic action after its constraints are resolved, in units with light speed and the reduced Planck constant equal to one:

\[
S_q^{(2)}=\frac Z2\int dt\,d^3x\,ds\,
\left[(\partial_tq)^2-|\nabla q|^2-\sigma(\partial_sq)^2-m^2q^2\right],
\quad Z>0,\quad m^2\geq0,\quad \sigma\in\{+1,-1\}.
\]
\[
\partial_t^2q-\nabla^2q-\sigma\partial_s^2q+m^2q=0,
\qquad \boxed{\omega^2=|\mathbf k|^2+\sigma k_s^2+m^2.}
\]

This is a diagnostic, not a new fundamental action or a derived UBT Hessian. A spacelike extra direction has positive sigma and real frequencies. With negative sigma, unrestricted sufficiently large extra-direction momentum gives exponential growth in t. The completed massless Clifford symbol in the overview supplies the corresponding five-dimensional characteristic cone, but it does not establish that an action has this physical fluctuation operator or positive norm.

If the spacelike s direction is additionally periodic, its assumed boundary condition gives

\[
s\sim s+2\pi R,\quad k_s=n/R,\quad n\in\mathbb Z,
\qquad m_n^2=m^2+n^2/R^2.
\]

This is conditional mode quantization, with the radius still an input. It concerns a real spacelike coordinate, not ordinary periodicity in imaginary time. Neither this spectrum nor the radius is derived from UBT here.

<!-- BILINGUAL-UNIT: c5-wave.reality -->
## The full complex coordinate proposal still needs a physical signature

The real part of the completed complex symmetric metric has signature (5,5), as checked in the overview. Choosing one of its negative directions as evolution time leaves four more negative directions. An unrestricted scalar wave operator with that signature has

\[
\omega^2=|\mathbf k_+|^2-|\mathbf k_-|^2+m^2,
\qquad \mathbf k_+\in\mathbb R^5,\quad \mathbf k_-\in\mathbb R^4.
\]

It therefore includes arbitrarily fast exponential modes on unrestricted data. This is a conditional realified wave-operator test, not a theorem against every holomorphic or constrained complex theory. Craig and Weinstein [S1] show why appropriate nonlocal data constraints can change the well-posedness conclusion. UBT must derive its own admissible data/reality prescription; counting ten real parameters does not supply it.

<!-- BILINGUAL-UNIT: c5-wave.verification -->
## Verification, scope and next step

`verify_wave_dynamics.py` checks the composite factorization, the volume identity, the normal quadratic density, the complete component Euler equations, the first-order symbol and the conditional dispersion/growth witnesses. A separate Python Fraction implementation checks symbol kernels and volume determinants. `wave_dynamics_results.json` records counts, versions and exclusions. These finite checks support the displayed analytic arguments; they do not formalize the Poincare lemma or prove a physical spectrum.

**LEAN-PENDING:** Lean and Lake executables are unavailable in this runtime; the new local exterior/PDE argument has no checked Lean formalization. The next unresolved calculation requires an explicit connection functional outside the factorized family, its full chain-rule Hessian and a defined physical reality/constraint sector. The already conditional Einstein effective branch remains separate and unaffected. English is the translation source; human semantic review remains required before merge.

<!-- BILINGUAL-UNIT: c5-wave.sources -->
## Sources

- [U1] [Existing gradient-volume argument](../action_selection/theta_gradient_kinetic_null_lagrangian.en.md).
- [U2] [Complete composite Hessian chain rule](../action_selection/biquaternionic_induced_gravity_boundary.en.md).
- [U3] [Existing invariant symplectic action](../action_selection/theta_invariant_multisymplectic_action.en.md).
- [U4] [Existing Lorentz-slice Hessian result](../action_selection/multisymplectic_lorentz_slice_audit.en.md).
- [S1] Craig and Weinstein, [On determinism and well-posedness in multiple time dimensions](https://arxiv.org/abs/0812.0210).
