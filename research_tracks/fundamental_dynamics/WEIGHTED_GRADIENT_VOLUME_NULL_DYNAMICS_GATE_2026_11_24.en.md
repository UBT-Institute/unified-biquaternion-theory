<!-- BILINGUAL-UNIT: weighted-gradient-volume-null-dynamics-2026-11-24 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact restricted four-real pure-gradient theorem and independent algebraic-contortion comparator. NOT a full UBT dynamics no-go.
UBT-AI-PROVENANCE-END
-->
# Stronger inverse-dynamics result: any field-weighted gradient volume is a null Lagrangian

**24 November 2026 — exact L0 conditional theorem in the four-real gradient Lorentz slice; microscopic UBT dynamics OPEN.**

\[
e^a{}_\mu=\partial_\mu Y^a,\qquad
g_{\mu\nu}=\eta_{ab}e^a{}_\mu e^b{}_\nu,\qquad
J^a{}_\mu=\partial_\mu Y^a,\qquad \det J>0.\tag{1}
\]
\[
S_f[Y]=\int d^4x\,f(Y)\det J,\qquad
C_a{}^\mu=\frac{\partial\det J}{\partial J^a{}_\mu}.\tag{2}
\]
\[
\boxed{\partial_\mu C_a{}^\mu=0,\qquad
C_a{}^\mu\,\partial_\mu Y^b=\delta_a{}^b\det J.}\tag{3}
\]
\[
\boxed{\frac{\delta S_f}{\delta Y^a}
=\partial_a f(Y)\det J-\partial_\mu[f(Y)C_a{}^\mu]=0.}\tag{4}
\]
\[
F(Y)=\int_0^{Y^0}f(s,Y^1,Y^2,Y^3)\,ds,\qquad
\boxed{f(Y)dY^0\wedge dY^1\wedge dY^2\wedge dY^3
=d\left(F(Y)dY^1\wedge dY^2\wedge dY^3\right).}\tag{5}
\]
\[
\boxed{W_{ab}=\frac{\partial^2[f(Y)\det J]}{\partial\dot Y^a\partial\dot Y^b}=0.}\tag{6}
\]
\[
L_K=J_a(Y)K^a+\frac12 K^a M_{ab}(Y)K^b,\quad
K_*=-M^{-1}J,\quad
L_{K,\mathrm{red}}=-\frac12 J^TM^{-1}J.\tag{7}
\]
\[
L_K^{\mathrm{velocity\ toy}}=\alpha \dot q\,K+\frac m2K^2
\quad\Longrightarrow\quad
L_{\mathrm{red}}=-\frac{\alpha^2}{2m}\dot q^2,\qquad
\boxed{W=-\frac{\alpha^2}{m}.}\tag{8}
\]

## Assumptions and precise scope

Keep Axiom A (one \(\Theta\in M_2(\mathbb C)\)) and locked central-sharp metric. Restrict to the **four-real**, zero-jet-connection, torsion-free nondegenerate sector where, after constant normalization, the real Lorentz coframe is an **exact Jacobian** (1). The region is oriented with fixed sign of \(\det J\); for negative sign apply the appropriate constant orientation sign to the volume. The four \(Y^a\) are restricted components of the same \(\Theta\), **not four new fundamental fields**. No independent metric, connection, or extra observer structure is introduced.

The already established sharp-pairing identity identifies the obvious canonical quadratic contraction with \(2\mathcal N_0\sqrt{|g|}\), i.e. a constant times the pullback volume. Here ask a stronger question: can one recover *any* dynamics by multiplying this density by a freely chosen smooth zeroth-order scalar **of precisely these four \(Y^a\)**, \(f(Y)\)? Equations (2)-(6) give a negative answer for the entire smooth family, independent of positivity or the shape of \(f\).

## Exact Euler–Lagrange and Hessian theorem

For \(J^a{}_\mu=\partial_\mu Y^a\), the cofactor identities are (3): the first is the Piola identity and the second follows from the adjugate formula. Hence the Euler derivative of \(S_f\) is identically zero by the chain rule, as in (4). The geometric proof (5) is stronger: \(f(Y)d^4Y\) is an exact top-degree form on the four-dimensional target patch. Pullback by \(Y(x)\) commutes with the exterior derivative, so the action is a boundary functional under compactly supported field variations.

Since \(\det J\) is **affine** in its time column \(J^a{}_0=\dot Y^a\), while \(f(Y)\) is velocity-independent, its four-by-four velocity Hessian (6) is **identically zero**. Its momenta are constrained; the theory has no local bulk Euler equations in this sector and therefore does not propagate a gravitational mode. The pure-gradient metric (1) is locally flat whenever \(J\) is invertible, so its Levi-Civita scalar curvature vanishes; an independently added Einstein–Hilbert term evaluated on this *particular* pure-gradient configuration cannot cure the missing local modes.

**Crucial limits:** This result does NOT extend by fiat to a general eight-real \(\Theta\) with a nonzero composite two-sided connection \(A[\Theta],B[\Theta]\), independent \(\psi\) jets, non-exact coframe, torsion, or a truly selected quantum nonlocal effective action. If \(f\) also depends on additional independent components, their jets, external \(x\), curvature or torsion, it is *not* the \(f(Y)\) theorem. Do not interpret a vanishing Hessian of this restricted coordinate parametrization as a claim about the full physical constrained Hessian.

## Algebraic torsion source alone is not an automatic rescue

Consider only a comparator with algebraic, invertible, velocity-independent \(M(Y)\) and velocity-independent \(J(Y)\) in (7). Stationary elimination gives a potential \(L_{K,\mathrm{red}}\) but **no kinetic Hessian**. The separate single-channel derivative-source toy (8) demonstrates the exact potential loophole: a *chosen* \(\alpha\dot q K\) generates a kinetic term after eliminating \(K\); its sign is governed by the *unselected* coefficient \(m\). Thus a velocity-sensitive composite torsion selector might generate dynamics but neither stability nor a unique sign follows from metric compatibility alone.

This algebraic toy does not describe all 24 real torsion components or the real full physical UBT connection, whose implicit derivative operator and source require separate calculation. In particular, arbitrary elimination of an independently varied \(K\) is not equivalent to solving a canonical single-valued \(K[\Theta]\).

## Concrete decision for UBT

**Reject** the full class \(f(Y)\sqrt{|g[Y]|}\) as a dynamical action in the pure-gradient four-real sector. Do NOT add an arbitrary scalar prefactor or a mass/potential and claim to have derived the propagating metric. The smallest remaining physical task is to derive from the locked single-\(\Theta\) invariants an actually selected, velocity-sensitive connection/torsion law or another nonlinear/quantum term **not reducible to the pullback top form**. Then calculate the reduced full eight-real Euler operator, on-shell vacuum, physical Hessian, gauge constraints, ghost signature and TT spectral pole. This is a **research obstruction**, not a complete no-go for UBT and not yet a stable fundamental dynamics.

Cross-check: research_tracks/T1_GR/gr_locked_kinetic_volume_2026_11_16.en.md; research_tracks/action_selection/sharp_kinetic_volume_collapse.en.md; research_tracks/action_selection/implicit_composite_legendre_gate.en.md; draft PR #909.

**Verification:** tools/verify_theta_weighted_gradient_volume_null_lagrangian_2026_11_24.py and the focused pytest wrapper. Exact symbolic proof checks a generic 4-by-4 Jacobian adjugate/Hessian, nontrivial nonaffine \(Y(x)\) with nonconstant \(f(Y)\), all four Euler identities, and the algebraic-torsion source contrast. **LEAN-PENDING, physical review required; no action selected, no merge as completed UBT dynamics.**

