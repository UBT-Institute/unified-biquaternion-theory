<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact scoped kinematic constraints and symbolic witnesses, NOT Maxwell or Einstein dynamics.
UBT-AI-PROVENANCE-END
-->

# Electromagnetic completion gate: why the covariant one-form is simple, and what a full Theta bivector can do

**2026-11-13 — status: scoped algebraic results (verified), full UBT dynamics OPEN.**

**Context:** The current UBT plan first seeks EM, gravitational curvature and scalar sectors from one complete complex-biquaternion Theta and only later tests an information principle. This note audits the recent constant-B construction and tests whether it can generate a fully general electromagnetic tensor.

## 1. Scope and variables

On a chosen local 4D physical Lorentz slice write the faithful 2-by-2 matrix carrier as
\[
\Theta=(C^a+i A^a)\sigma_a,\quad
\sigma_a=(I,\sigma_1,\sigma_2,\sigma_3),\qquad A,C\in\mathbb R^{1,3}.
\]
This is a value-space decomposition; it does NOT declare a genuine 8D Maxwell 1-form or an extra fundamental field. The two real four-vectors are parts of the same Theta. The canonical locked tetrad requires
\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\in i\,{\rm Herm}_2,\qquad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}I.
\]

Consider the candidate *Lorentz + Weyl* composite transport
\[
\mathbb D_\mu V^a=\partial_\mu V^a+
\omega_\mu{}^a{}_b V^b+w_\mu V^a,
\qquad \omega\in\mathfrak{so}(1,3),\quad w\ \text{real}.
\]
The exact reality constraint is \(\mathbb D C=0\), and \(e^a=\mathbb D A^a/\sqrt{\mathcal N_0}\). This restriction is met by the previously studied determinant-derived relative central jet. It is NOT the only possible UBT connection or a theorem about arbitrary 8D base spaces.

## 2. The normalized complex phase current is a simple two-form: exact theorem

Let \(u=C\cdot C,\ v=A\cdot A,\ \ell=A\cdot C,\ s=u+v\) with Minkowski \(\eta\). Work on a patch where \(u\ne0\) and \(s\ne0\).

The natural normalized phase-current one-form is
\[
a=\frac{\operatorname{Im}(\overline{\mathcal Z}_a\,\mathbb D \mathcal Z^a)}
        {\overline{\mathcal Z}_a\mathcal Z^a},
\qquad \mathcal Z=C+iA.
\]
Because \(\mathbb DC=0\), its numerator is \(C\cdot\mathbb DA\). Metric compatibility of omega and the Weyl part give
\[
du=-2wu,\qquad
d\ell=C\cdot\mathbb DA-2w\ell.
\]
Thus
\[
C\cdot\mathbb DA=d\ell-\frac{\ell}{u}du
=u\,d(\ell/u)
\]
and therefore
\[
\boxed{a=\frac{u}{u+v}\,d(\ell/u)}
\quad\Longrightarrow\quad
\boxed{F=da=d\!\left(\frac{u}{u+v}\right)\wedge d\!\left(\frac{\ell}{u}\right)}.
\]
Consequently
\[
\boxed{F\wedge F=0}
\]
IDENTICALLY, even for nontrivial omega, as long as \(\mathbb DC=0\). This is an exact decomposability/rank-at-most-two restriction. In four-dimensional Lorentzian EM language \(F_{\mu\nu}{}^\star F^{\mu\nu}=0\), equivalently \(\mathbf E\cdot\mathbf B=0\) in the standard convention. It therefore cannot represent generic EM backgrounds with parallel nonzero E and B.

A closely related potential from the *same* A,
\[
a_A=\frac{A\cdot \mathbb DA}{u+v}
=\tfrac12d\ln\left|1+\frac vu\right|,
\]
is locally exact and has \(da_A=0\).

**The theorem excludes only these specific one-form identifications with the stated connection/reality constraints.** It does not exclude EM field strength read directly as a (self-dual) bivector in Theta or a more general relative/composite connection.

## 3. The tempting noncovariant escape is spurious without more structure

If instead one writes the ordinary-derivative current
\[
a_{\rm raw}=\frac{C\cdot dA-A\cdot dC}{u+v},
\]
it may have arbitrary rank. Example in coordinates \((t,x,y,z)\), with \(\eta=\mathrm{diag}(+---)\):
\[
A=(t,x,y,z),\quad C=(1,\alpha y,0,\beta t).
\]
Near the origin \(H=C^a\sigma_a\) is positive-definite and \(A=0\) at the origin. SymPy gives
\[
F_{\rm raw}(0)=-2\beta\,dt\wedge dz+2\alpha\,dx\wedge dy,
\]
with four-form coefficient \(F_{\rm raw}\wedge F_{\rm raw}=-8\alpha\beta\,dt\wedge dx\wedge dy\wedge dz\) in this coordinate orientation. Therefore the noncovariant current can produce nonzero \(\mathbf E\cdot\mathbf B\).

But this raw current uses \(dC\) instead of the appropriate local Lorentz transport. For any Hermitian invertible \(H\) there is a local, specified (not yet canonical) traceless connection choice
\[
\Omega_\mu=-\tfrac12(\partial_\mu H)H^{-1}
+\tfrac14\operatorname{tr}(H^{-1}\partial_\mu H)I,\qquad
w_\mu=-\tfrac12\operatorname{tr}(H^{-1}\partial_\mu H)
\]
such that
\[
\partial_\mu H+\Omega_\mu H+H\Omega_\mu^\dagger+w_\mu H=0,\qquad \operatorname{tr}\Omega_\mu=0.
\]
Thus it is possible to preserve the ENTIRE canonical i-Hermitian tetrad on a local positive-H patch (with the anti-Hermitian part determining e). At the example's origin \(e^a{}_\mu=\delta^a_\mu\) for \(\sqrt{\mathcal N_0}=1\), so it is nondegenerate. Under this induced covariant transport the normalized phase current reduces to section 2: \(F\wedge F=0\) identically and in this example \(F(0)=0\). The apparent generic rank of the *raw* current is NOT evidence of a correct Lorentz-gauge-invariant EM observable.

This particular H-derived Omega is a local gauge-fixed representative satisfying the compatibility equation; its uniqueness, full local Lorentz-gauge covariance, torsion constraints, and selection by a single action are NOT established. The exact identity above does not certify it as the canonical microscopic connection.

## 4. A direct relative bivector spans the full six EM algebraic components, but fails the dynamical gate

The prior transformation result suggests a different, *field-strength-level* candidate. For a chosen invertible reference/background Theta_bar that transforms together with Theta by Lorentz congruence, define
\[
X=\Theta\,\bar\Theta^{-1},\qquad
\mathcal F_\Theta=X-\tfrac12\operatorname{tr}(X)I.
\]
Then \(X\to SXS^{-1}\), and its three complex traceless coefficients transform as a self-dual/anti-self-dual Lorentz bivector. They are NOT limited by \(F\wedge F=0\); at a point they span all six real electromagnetic field-strength components.

**An exact cautionary flat example:** set
\[
\bar\Theta=i[(T+t)I+x\sigma_1+y\sigma_2+z\sigma_3],\quad T\ne0,
\]
\[
\Theta=\bar\Theta-T(1+i)\sigma_3.
\]
Then \(D=\partial\), the physical tetrad is unchanged and is precisely \(D_\mu\Theta=i\sigma_\mu\), with flat Minkowski metric. At the coordinate origin the relative traceless matrix is
\[
\mathcal F_\Theta(0)=(1+i)i\sigma_3,
\]
which is algebraically E_z=B_z=1 (under the declared convention), corresponding to a real bivector with \(F\wedge F\ne0\). SymPy verifies both the unchanged tetrad and the non-simple algebraic field strength.

This shows a *full-rank algebraic field-strength candidate can be created by a constant shift of Theta while its metric is entirely unchanged*. There is no proof that this constant shift is a propagating photon or sources the metric correctly. A successful unified UBT action must (a) give the candidate a real wave equation, two healthy photon helicities, U(1) gauge symmetry and stress-energy, and (b) avoid physical dependence on an arbitrary choice of reference Theta_bar. In particular, this is a diagnostic, not an observational prediction.

## 5. What to test next, without introducing an independent photon field by hand

1. **Do not recycle one-form-only candidates that are identically exact or decomposable.** Their Lorentz-covariant restrictions are now explicit.
2. Keep the 3-complex self-dual bivector interpretation alive as an **observable**, but derive its actual Theta-background/tetrad map and first-jet variation. Fix the ambiguity of the reference field.
3. Calculate the linearized principal symbol / constraints of a selected single-Theta action in the full eight-real-value space before identifying 2 photon modes. The bare fixed-background Theta kinetic signature and the metric-lock collapse remain caveats.
4. A distinct physically justified eight-real-dimensional base could support a genuine generalized eight-vector one-form and 28-component two-form. Nothing in this note falsifies that route, and it must not be conflated with a 4D field of eight real values.
5. Information/Fisher/Landauer principles are a later selection layer, not a way to hide an incorrect photon DOF count.

**Verdict:** The prior constant-B mechanism is genuine *kinematics*, but the simplest normalized Lorentz-covariant Theta phase-current is always decomposable under the exact classical-tetrad reality constraint. The direct relative traceless Theta channel spans the right bivector representation while leaving its dynamics open. This is a useful narrowing of the unification programme, not a no-go for UBT.

## Verification and repo context

- Focused runnable regression: tests/test_theta_em_covariant_gate.py; four algebraic tests passed with SymPy in the working environment.
- Prior context: FULL_THETA_COMPLEX8_COMPOSITE_CONSTANT_B_AND_SIGNATURE_GATE_2026_11_13.en.md; EM_LORENTZ_DECOMPOSITION_CORRECTION_2026_11_12.en.md; GENERALIZED_EM_COMPLEX4_VS_EIGHT_DIMENSIONAL_VECTOR_GATE_2026_11_12.en.md; canonical/geometry/biquaternion_connection.tex; research_tracks/action_selection/full_theta_hermitian_compensator_2026_10.en.md.
