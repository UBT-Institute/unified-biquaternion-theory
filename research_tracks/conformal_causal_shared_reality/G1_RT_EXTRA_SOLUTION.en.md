<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# G1: exact non-Einstein stationary point of an imported Einstein–Hilbert metric action

**2026-10-28 · PR #809 · C_working · RESTRICTED COMPARATOR ONLY.**
This follows [G1 induced geometry](G1_INDUCED_GEOMETRY.en.md). It does **not**
change PR #807 or #808, choose a UBT action, specify the physical
conformal connection or establish graviton propagation.

## Assumptions (do not omit)

Trial carrier \(\Theta\in\mathbb C\otimes\mathbb H\simeq\mathrm{Mat}_2(\mathbb C)\)
with eight real trial coordinates \(Y^A\). Let
\(B_{AB}=\mathrm{diag}(+,-,-,-,+,-,-,-)\) be the real polarization
of the already classified Lorentz-congruence-invariant quadratic form.
On a nondegenerate patch choose \(\Omega=0\), and define *only in this
comparison model*

\[
 g_{\mu\nu}=B_{AB}\partial_\mu Y^A\partial_\nu Y^B.
\]

Choose the **imported** Einstein–Hilbert functional
\[
 S_{\mathrm{EH}}[Y]=\frac1{2\kappa_G}\int\sqrt{-g[Y]}\,R[g[Y]]\,d^4x
\]
with fixed boundary data/compactly supported variations, no matter and
no cosmological constant. This is **not** the finalized
\(S_{\mathrm{UBT}}\); varying an independent connection or enforcing
the original central anticommutator readout could change the answer.

## Complete first variation: the Regge–Teitelboim projection

Let \(\mathcal E^{\mu\nu}=G^{\mu\nu}\) for the vacuum comparator.
With the usual boundary prescription, the induced metric variation
gives, up to an overall convention-dependent sign,
\[
 \delta S_{\mathrm{EH}}
 \propto\int\sqrt{-g}\,\mathcal E^{\mu\nu}
 B_{AB}\partial_\mu Y^A\partial_\nu\delta Y^B .
\]
Integrating by parts and using the contracted Bianchi identity,
\(\nabla_\mu G^{\mu\nu}=0\), yields
\[
 \boxed{G^{\mu\nu}b^A_{\mu\nu}=0,\qquad
 b^A_{\mu\nu}:=\partial_\mu\partial_\nu Y^A
              -\Gamma^\rho_{\mu\nu}\partial_\rho Y^A.}
\]
The vector \(b^A_{\mu\nu}\) is orthogonal to the tangent space.
Tangential variations are the diffeomorphism Noether identity,
not extra Einstein equations. With codimension \(8-4=4\), the
pointwise algebraic map \(G^{\mu\nu}\mapsto G^{\mu\nu}b^A_{\mu\nu}\)
has rank at most 4 and a kernel in the ten-dimensional symmetric
tensor space of dimension at least 6. This bound alone does not
prove existence of extra solutions; the explicit witness below does.

## Exact non-Einstein stationary witness

Use the same trial field as the previous constructive study:
\[
 \Theta=tI+x\sigma_1+y\sigma_2+z\sigma_3+i k t x\,\sigma_1,
 \qquad k\in\mathbb R\setminus\{0\}.
\]
Equivalently \(Y=(t,x,y,z,0,ktx,0,0)\) with the target quadratic
form above. On \(A:=1+k^2(t^2-x^2)>0\),
\[
 ds^2=dt^2-dx^2-dy^2-dz^2-k^2(x\,dt+t\,dx)^2.
\]
The metric is the direct product
\(g=g_{(t,x)}\oplus(-dy^2-dz^2)\), with exact scalar curvature
\[
 \boxed{R=-\frac{2k^2}{A^2}}.
\]
In two dimensions \(\mathrm{Ric}_{ij}=\tfrac12 R g_{ij}\),
so the four-dimensional Einstein tensor obeys
\[
 G_{ij}=0\quad(i,j=t,x),\qquad
 \boxed{G_{yy}=G_{zz}=\frac R2=-\frac{k^2}{A^2}\ne0}.
\]
Every embedded target coordinate is affine in \(y,z\), and all
Christoffels with lower \(yy\) or \(zz\) vanish, hence
\[
 b^A_{yy}=b^A_{zz}=0 \quad\hbox{for all }A.
\]
The only nonzero components of \(G^{\mu\nu}\) are \(yy,zz\);
consequently
\[
 \boxed{G^{\mu\nu}b^A_{\mu\nu}=0\quad\forall A,
        \qquad G_{\mu\nu}\ne0.}
\]
The extrinsic curvature is nontrivial:
at the origin \(b^{(\mathrm{Im}\,\sigma_1)}_{tx}=k\ne0\).
The construction is not a flat-gauge artifact.

**G1-RT EXTRA SOLUTION [COUNTEREXAMPLE / exact under assumptions]:**
Importing the Einstein–Hilbert functional but varying only this
eight-real-component gradient-Theta embedding is *insufficient* to
force the Einstein equations. This is a concrete instantiation of
the Regge–Teitelboim embedding-gravity "extra solutions" already
known in the literature. It is **not** a new discovery of
embedding gravity and not a no-go for the full UBT architecture.

## Consequences for an eventual covariant connection

To recover Einstein equations dynamically one must justify additional
independent variations/constraints. A connection with enough
variational freedom to span the missing metric directions may work,
but if \(e^a\) is freely contained as the broken/translation part
of a conformal Cartan connection, a GR comparator has simply imported
a tetrad rather than derived it from \(\Theta\). This must be audited.

**Next gate, before action classification:** construct a specific,
gauge-covariant \(\mathcal A[\Theta]\), or a constrained independent
\(\mathcal A\) with derivable equations, and show both:
(1) the metric first variation has sufficient rank **after**
constraints, reality and diffeomorphism gauge;
(2) the linearized physical sector actually supports the two
healthy Einstein helicities rather than extra embedding solutions.
A fixed arbitrary \(\mathcal A\) or a free soldering 1-form does not
satisfy this gate. The shared-reality information principle is
retained as an **additional** explicit state/entropy filter, not
silently assumed to fix missing equations.

## Executable verification

`python -m unittest discover -s tests -p 'test_theta_rt_extra_solution.py' -v`

Four exact symbolic tests reproduce the metric, \(R\),
the nonzero Einstein tensor, all eight embedding Euler equations,
orthogonality of the second fundamental form and the rank bound.
Verified locally in an equivalent Python/SymPy environment.
GitHub CI and independent theoretical peer review are separate.

## Literature for context

- Regge–Teitelboim embedding gravity and its extra solutions:
  https://www.mdpi.com/2073-8994/12/5/722
- Paston and collaborators, weak-field extra solutions:
  https://www.mdpi.com/2218-1997/8/12/635
