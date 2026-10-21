<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: unrestricted-composite-spin-variation.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact Lorentz-real variational chain rule, not a completed UBT action.
UBT-AI-PROVENANCE-END -->
# Unrestricted composite spin variation: exact normal-blindness and connection rank

**Status: EXACT KINEMATIC VARIATION / PHYSICAL UBT ACTION OPEN.** Continue merged PR #693 without imposing homogeneous FLRW symmetry. Use the existing positive-Hermitian Lorentz-real field sector and its only Lorentz spin connection.

## Composite tetrad, independent Euler forms

Let X be the Lorentz vector representing the field and omega its metric-compatible spin connection. The coframe is

\[
e^a=\frac1qD_\omega X^a,\quad
D_\omega X^a=dX^a+\omega^a{}_bX^b,\quad q=\sqrt{\mathcal N_0}.
\]

For a parent functional that temporarily treats e and omega as independent, define all Euler forms at fixed other fields by

\[
\delta S_{\mathrm{parent}}=\int_M
\delta e^a\wedge\mathcal E_a+
\sum_{a<b}\delta\omega^{ab}\wedge\mathcal C_{ab}
+\delta X^a\mathcal U_a+\text{boundary}.
\]

The coframe variation required by the single-Theta theory is exactly

\[
\boxed{\delta e^a=
\frac1q\left(D_\omega\delta X^a+\delta\omega^a{}_bX^b\right).}
\]

After substitution and covariant integration by parts the **spatially unrestricted** composite Euler equations become

\[
\boxed{
\mathcal E^{\mathrm{comp}}_{X,a}
=\mathcal U_a-\frac1qD_\omega\mathcal E_a,\qquad
\mathcal C^{\mathrm{comp}}_{ab}
=\mathcal C_{ab}+\frac1q(X_b\mathcal E_a-X_a\mathcal E_b).
}
\]

The parent Euler three-forms include all metric, curvature, torsion and matter contributions. An explicit field-value source is represented by U. These identities are general variational calculus, not selection of a new fundamental action.

## Gauge identity and true pointwise rank

Local Lorentz invariance gives the parent and composite Noether relations, assuming no explicit Lorentz-breaking source and U=0:

\[
\boxed{
D_\omega\mathcal C_{ab}
+e_b\wedge\mathcal E_a-e_a\wedge\mathcal E_b=0,
\quad
D_\omega\mathcal C^{\mathrm{comp}}_{ab}
+X_b\mathcal E^{\mathrm{comp}}_{X,a}
-X_a\mathcal E^{\mathrm{comp}}_{X,b}=0.
}
\]

These relations imply dependencies between field equations. They do not determine the number of propagating modes or the local Einstein normal constraint.

At a timelike field value adopt the local Lorentz frame

\[
X^a=(r,0,0,0),\quad
\delta_\omega e_\mu^0=0,\quad
\delta_\omega e_\mu^i=(r/q)\delta\omega_\mu{}^i{}_0,
\qquad
\boxed{\operatorname{rank}J_{\omega\to e}=12,\quad
\dim\ker J_{\omega\to e}=12.}
\]

With X fixed, each coordinate direction has three boost directions affecting the tetrad and three rotational directions annihilating X. The full pointwise spin-to-tetrad map therefore has rank twelve with a twelve-dimensional kernel, out of the twenty-four spin-connection coefficients. This is **not** the rank of the complete spin Euler system: curvature enters through the independent parent spin Euler form.

## Normal projected tetrad equation does not enter the coframe-induced spin source

If the parent tetrad Euler form is entirely aligned with the clock vector, then

\[
\mathcal E_a=X_a\mathcal J,\quad
\boxed{X_b\mathcal E_a-X_a\mathcal E_b=0,\quad
\mathcal E^{\mathrm{comp}}_{X,a}
=-q^{-1}D_\omega(X_a\mathcal J).}
\]

Thus the antisymmetric **additional** spin source vanishes. The field equation still differentiates the normal residual and can supply a conservation equation rather than an algebraic vanishing condition. The independent spin curvature Euler form may add further restrictions; nothing here proves the full Palatini–Holst action lacks a normal equation.

## Test imported Palatini–Holst operator without FLRW reduction

Let the **external comparison action** be defined by the curvature bivector polynomial

\[
S_{\mathrm{PH}}[e,\omega]=
\int_M P_{ab}(e)\wedge R^{ab}(\omega)
-\Lambda\,\mathrm{vol}(e),\quad
P_{ab}=c_{\mathrm{EC}}\epsilon_{abcd}e^c\wedge e^d
+c_{\mathrm H}e_a\wedge e_b .
\]

With the stated convention delta e wedge E and delta omega wedge C, the parent spin Euler form is D P. Hence the genuinely composite spin and field equations are

\[
\boxed{
D_\omega P_{ab}+
q^{-1}(X_b\mathcal E_a-X_a\mathcal E_b)=0,\quad
\mathcal U_a-q^{-1}D_\omega\mathcal E_a=0.
}
\]

Setting D P to zero as if the coframe were independent would omit an essential source. Conversely, setting the full parent metric Euler form to zero by hand would impose stronger equations than the actual composite theory supplies. Deriving these unrestricted equations is a prerequisite for checking whether the curved homogeneous configuration of merged PR #693 satisfies full field equations.

## Fully explicit parent curvature equations (no FLRW imposed)

Beyond the abstract chain rule, the parent Palatini–Holst Euler forms can be calculated without choosing any spacetime symmetry. Sum antisymmetric spin pairs only once and define
\[
P_{ab}=c_{\rm EC}\epsilon_{abcd}e^c\wedge e^d
+c_{\rm H}e_a\wedge e_b,\qquad
S_{\rm parent}=\sum_{a<b}\int_M P_{ab}\wedge R^{ab}
-\Lambda\int_M\mathrm{vol}(e).
\]
Direct **independent tetrad variation** produces the curvature-dependent three-form
\[
\boxed{
\mathcal E_a=
2c_{\rm EC}\sum_{b<c}\epsilon_{bcad}\,
e^d\wedge R^{bc}
+c_{\rm H}\sum_{b<c}(\eta_{ba}e_c-\eta_{ca}e_b)
\wedge R^{bc}
-\frac{\Lambda}{3!}\epsilon_{abcd}
e^b\wedge e^c\wedge e^d.
}
\]
while independent spin variation of curvature, using (D_omega e^a=T^a), yields the Cartan three-form
\[
\boxed{
\mathcal C_{ab}=D_\omega P_{ab}
=2c_{\rm EC}\epsilon_{abcd}\,T^c\wedge e^d
+c_{\rm H}(T_a\wedge e_b-e_a\wedge T_b).
}
\]
The resulting **actual composite** spin Euler equation is therefore
\[
\boxed{
2c_{\rm EC}\epsilon_{abcd}T^c\wedge e^d+
c_{\rm H}(T_a\wedge e_b-e_a\wedge T_b)+
q^{-1}(X_b\mathcal E_a-X_a\mathcal E_b)=0.
}
\]
The tetrad Euler expression also enters the composite field equation through (-q^{-1}D_omegamathcal E_a). Even for vanishing direct matter spin current, the spin equation is generally **not** the torsion-free Cartan condition. Conversely, these coupled equations do not automatically force the parent (mathcal E_a=0); the time-normal component remains the central Hamiltonian question. The parity-odd coefficient (c_{m H}) must be justified by the declared symmetries.

An independent exterior-algebra script evaluates the original four-form variation directly in arbitrary invertible sample coframes with generic symbolic couplings and verifies **every tetrad component**; it separately checks the covariant torsion derivative of (P_{ab}) for each spin-bivector pair. This is a numerical-coframe polynomial identity audit, not a proof of existence of full nondegenerate solutions.

## Boundary of result and next step

The result is exact on a smooth invertible Lorentz-real patch. It does **not** derive a unique UBT action, justify the Holst coefficient, establish physical ghost-free tensor modes, recover GR constraints or provide CMB predictions. Next calculate the curvature parent Euler forms in a general tetrad and linearize **their coupled composite equations**, without imposing homogeneity before variation.

**Reproducibility:** `tools/verify_unrestricted_composite_spin_variation.py`, `tests/test_unrestricted_composite_spin_variation.py` and isolated CI. Canonical grounding: `canonical/geometry/connection.tex`; merged PR #693 and merged PR #684.
