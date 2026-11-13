<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Restricted mathematical lemmas and exact local example; no Maxwell/Einstein action or physical photon proved.
UBT-AI-PROVENANCE-END
-->

# Full complex Theta: spin-connection restriction, an exact constant-B composite witness, and eight-real signature gate

**Date:** 2026-11-13. **Status:** EXACT CONDITIONAL KINEMATICS / DYNAMICS OPEN.  
**Programme:** CURRENT_WORK_PROGRAM_THETA_FIELDS_GEOMETRY_INFORMATION_2026_11_12.en.md.  
**Warning:** The field's eight real VALUE coordinates are not by themselves an eight-dimensional spacetime base.

## 1. Setup, source consistency

In the faithful 2-by-2 complex representation of ONE biquaternion, let
\[
\sigma_a=(I,\sigma_1,\sigma_2,\sigma_3),\quad
\Theta=i A^a\sigma_a+C^a\sigma_a,\quad
A^a,C^a\in\mathbb R,\quad
\eta_{ab}=\operatorname{diag}(+,-,-,-).
\]
This is a chosen Lorentz-congruence representation for this research gate, NOT a new fundamental definition of Theta's transformation laws. The canonical locked tetrad remains
\[
E_\mu=s^{-1}D_\mu\Theta\in W_L=i\operatorname{Herm}_2,\quad
s=\sqrt{\mathcal N_0},\qquad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}I.
\]
No metric trace, Hermitian norm or projector replaces the canonical sharp metric.

The pure paired spin connection is
\[
D_\mu\Theta=\partial_\mu\Theta+
\Omega_\mu\Theta+\Theta\Omega_\mu^\dagger,
\quad\Omega_\mu\in\mathfrak{sl}_2(\mathbb C),
\]
as in canonical/geometry/biquaternion_connection.tex. The induced Lorentz derivative acts on Hermitian matrices, with real vector components denoted \(\nabla_\mu A^a,\nabla_\mu C^a\).

## 2. Exact restriction in the pure Lorentz-pair branch

Because Hermitian and anti-Hermitian matrices are independently preserved by the pure congruence covariant derivative,
\[
D_\mu\Theta
=i(\nabla_\mu A^a)\sigma_a+
(\nabla_\mu C^a)\sigma_a .
\]
Consequently
\[
\boxed{E_\mu\in W_L\quad\Longleftrightarrow\quad\nabla_\mu C^a=0
\ \ \text{for all }a,\mu.}
\]
Thus merely making the existing metric-compatible *Lorentz spin* connection nonzero does not make the other four real Theta components freely dynamical. Integrability yields
\[
[\nabla_\mu,\nabla_\nu]C^a
=R^a{}_{b\mu\nu}(\omega)C^b=0.
\]
This is a parallel-vector/holonomy restriction even with metric-compatible torsion (the tetrad-defined R here is curvature of the internal spin connection). A generic irreducible Lorentz holonomy admits no nonzero parallel C.

**This no-go is scoped to the specified homogeneous congruence transformation, pure Lorentz pair, and entire tetrad in W_L.** In particular, it does not exclude relative left/right composite terms, other nonlinear derived EM observables, or an 8D coordinate construction.

## 3. An exact closed-potential obstruction for a naive EM assignment

Under the same pure branch, \(e_\mu{}^a=s^{-1}\nabla_\mu A^a\). If one identifies a would-be EM 1-form by the natural direct frame contraction of the SAME vector,
\[
a_\mu=A_a e_\mu{}^a,
\]
then metric compatibility \(\nabla_\mu\eta_{ab}=0\) gives
\[
\boxed{a=\frac{1}{2s}\,d(A_aA^a),\qquad da=0.}
\]
This applies even if the Lorentz spin connection has curvature or torsion: contracting the vector with its own metric-compatible derivative makes an exact differential. It does NOT rule out a self-dual **field-strength** projection directly from Theta, a potential using different component combinations, or a relative connection. The result warns against identifying any convenient soldered one-form as a photon potential.

The companion \(C_a e^a\) is also exact when \(\nabla C=0\):
\[
C_a e^a=s^{-1}d(C_aA^a),\quad d(C_a e^a)=0.
\]

## 4. Positive exact witness using an ALREADY STUDIED relative central jet

The prior research_tracks/action_selection/full_theta_hermitian_compensator_2026_10.en.md investigated a REAL, relative central one-form
\[
D_\mu\Theta=
\partial_\mu\Theta+\Omega_\mu\Theta+
\Theta\Omega_\mu^\dagger+w_\mu\Theta,
\quad w_\mu=-\frac12\partial_\mu\ln|\det H|,
\quad H=\frac12(\Theta+\Theta^\dagger).
\]
Here \(w\) is a derived function of original Theta, not postulated as a new independent field; this is an explicitly noncanonical **research candidate for the action**, though the 4D sharp metric definition is unchanged.

Set \(s=1\) and \(\Omega=0\). On a local real patch with \(B\ne0\), \(k\ne0\), define
\[
f=e^{kx}>0,\qquad w=-k\,dx,
\]
\[
h(t,x,y,z)=\sqrt{1+t^2-x^2-z^2-(B/k)y},\qquad
A^a=(t,x,h,z),
\]
\[
\boxed{\Theta=fI+iA^a\sigma_a.}
\]
The patch is chosen where the square-root argument is positive. Then \(H=fI\), \(\det H=f^2\), and the displayed \(w\) is exactly the determinant-derived relative jet. Compute
\[
D\Theta=d\Theta+w\Theta
=i(dA^a+w A^a)\sigma_a,
\]
so \(E_\mu\in i\operatorname{Herm}_2\) EXACTLY, without projection. Define
\[
e^a=dA^a+wA^a,\qquad g=\eta_{ab}e^a\otimes e^b
\]
with canonical quaternion sharp. The tetrad is nondegenerate near the origin because
\[
\boxed{\det(e_\mu{}^a)\big|_{0}=-\frac{B}{2k}\ne0.}
\]
Thus \(g\) is a regular Lorentz metric on a sufficiently small patch.

Now define a natural *candidate* 1-form via the SAME original Theta coefficients and the derived tetrad,
\[
a=A_a e^a
=\frac12 d(A^2)+A^2 w,\quad A^2=A_aA^a=-1+(B/k)y.
\]
Its exterior derivative is EXACTLY
\[
\boxed{
F=da=d(A^2)\wedge w
=\frac Bk\,dy\wedge(-k\,dx)=B\,dx\wedge dy .
}
\]
So a constant, nonzero, real two-form is obtained from one complete Theta with the derived w and a nondegenerate canonical classical tetrad. No external Maxwell potential was inserted. Unlike the pure spin-pair result of section 3, the relative scalar w evades the exact-differential cancellation. Even though \(dw=0\), the cross-term \(d(A^2)\wedge w\) need not vanish.

**Narrow, crucial limitations:**
- The ansatz for A and f was chosen to realize B, not solved from any UBT Euler–Lagrange equation. This is a constructive kinematic existence proof.
- The resulting a and F are candidate geometric observables. They are NOT shown to have the physical local U(1) gauge redundancy, conserved charge, two photon helicities, or positive Maxwell action. In particular, a scalar w is not itself a Maxwell potential.
- Because \(w\) is exact, the entire ansatz \(F=d(A^2)\wedge w\) is decomposable, hence \(F\wedge F=0\). It cannot realize generic electromagnetic configurations with \(E\cdot B\ne0\). It does include uniform purely magnetic configurations.
- The candidate relative w is not the pure metric-compatible Lorentz spin connection; canonical action selection, gauge compatibility, curved composite connections and propagation remain OPEN. Do not declare this the physical UBT EM sector.

## 5. Eight real components and the possible 8D signature: exact representation restriction

If the same Theta under Lorentz congruence represents two real Lorentz four-vectors A,C, the real symmetric *constant, Lorentz-invariant* quadratic forms on \(\mathbb R^{1,3}\oplus\mathbb R^{1,3}\) are
\[
Q(A,C)=k_{11}\eta(A,A)+2k_{12}\eta(A,C)+k_{22}\eta(C,C)
=\eta\otimes K,
\]
with real symmetric \(K\) of size 2x2. This follows because the ordinary Lorentz-vector representation has invariant symmetric bilinear form only proportional to eta, and there is no invariant antisymmetric 2-form; cross terms are also eta-proportional.

Diagonalize nondegenerate K. Its signatures (++), (+-), (--) produce respective 8-real signatures
\[
\boxed{(2,6),\quad(4,4),\quad(6,2)}
\]
with the pair denoting (positive,negative) eigenvalues. A Lorentz-invariant constant quadratic form of signature (1,7) is therefore impossible **under this two-four-vector representation**.

Two useful concrete forms:
\[
\mathrm{Re}\det\Theta=\eta(C,C)-\eta(A,A)
\quad\Rightarrow\quad \operatorname{sig}=(4,4);
\]
\[
\mathrm{Tr}[\operatorname{adj}(\Theta)\Theta^\dagger]
=2[\eta(A,A)+\eta(C,C)]
\quad\Rightarrow\quad \operatorname{sig}=(2,6).
\]
The scalar coefficient normalizations/overall signs do not change the restricted no-(1,7) conclusion. This is a theorem about the 8-real **value representation** and its invariant bilinears. It is NOT a no-go for an eight-coordinate physical base with a different representation (e.g. 4D spacetime plus four internal scalars), nonconstant bundle metric, dynamical reduction, or another observer/metric structure. Those alternatives require explicit construction; counting eight real Theta components alone does not select them.

A genuine 8D Maxwell 1-form with 28 field-strength components requires a justified 8D base metric and Lorentzian causal signature before importing the conventional 8D photon polarization count.

## 6. Direction for the programme and information-first-later gate

- EM-B direct potential with the PURE metric-compatible Lorentz spin pair, soldered as A_a e^a: **excluded as nonzero F** by exact differential identity.
- EM-B with a derived relative central jet: **constant nonzero F kinematically possible**, but remains restricted to decomposable F and has no Maxwell action or U(1) derivation.
- EM-A: a self-dual field-strength observable in the complex bivector representation remains a separate live candidate; do not conflate it with a vector potential.
- EM-C: an actual eight-dimensional 1-form remains a separate possible extension, not derivable from a field component count.
- NEXT decisive test: select a non-scalar/composite relative piece from ONE Theta whose invariant F spans general six-dimensional 4D electromagnetic field strengths including F wedge F != 0, without violating E in W_L; then compute its linearized gauge constraints and wave operator from ONE action.
- Information principle should constrain/predict action or correlations only after a healthy causal principal symbol is identified; do not cure multiple-time ghost modes by verbal entropy arguments.

## Verification

Exact symbolic test suite: tests/test_theta_complex8_em_gate.py. Four focused SymPy tests passed locally (2026-11-13): invariant eight-real bilinear signatures; Hermitian/anti-Hermitian separation for general traceless spin connection; exact differential potential identity for a general infinitesimal Lorentz connection; and the nondegenerate constant B witness with determinant-derived w. This is algebraic/kinematic verification only.
