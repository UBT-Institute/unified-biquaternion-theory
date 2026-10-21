<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: torsionfree-vacuum-rigidity.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional local rigidity for the torsion-free parent-Einstein shell; NOT a no-go for the full composite UBT field equations.
UBT-AI-PROVENANCE-END
-->
# Rigidity theorem: a torsion-free timelike single-Theta vacuum has no gravitational waves

**Status: EXACT CONDITIONAL MATHEMATICS / FULL UBT DYNAMICS OPEN.** This strengthens the canonical torsion-free Schwarzschild obstruction and follows merged PR #694. The result applies only where the original Lorentz-real single-field tetrad is invertible, the vector X is timelike, the compatible Lorentz connection is torsion-free, and the **independent parent Einstein equation** is imposed. It does not exclude an on-shell torsionful solution of the complete composite field equations.

## Hypotheses and the concurrent vector identity

Fix the one-connection Lorentz-real coframe and assume a nonzero timelike vector field with vanishing Cartan torsion:

\[
e_\mu{}^a=q^{-1}D_\mu X^a,\qquad q=\sqrt{\mathcal N_0}>0,\qquad
X^aX_a<0,\qquad T^a=de^a+\omega^a{}_b\wedge e^b=0.
\]

The tetrad postulate then identifies X with a spacetime vector whose normalized vector X/q has the identity as its covariant gradient. Commuting derivatives yields

\[
\nabla_\mu(X^\nu/q)=\delta_\mu{}^\nu,\qquad
\boxed{R^\rho{}_{\sigma\mu\nu}X^\sigma=0.}
\]

Because torsion is zero, there is no torsional commutator term. This is an exact local integrability condition, not a field equation chosen by hand.

## Prove flatness from vacuum Ricci and a timelike curvature kernel

In a local orthonormal frame aligned with X, the curvature annihilation condition gives

\[
X^a=(r,0,0,0),\qquad r>0,\qquad
\boxed{R_{\mu\nu\rho0}=0.}
\]

Riemann antisymmetry and exchange of index pairs remove every component containing a time index. The only remaining algebraic curvature is the purely spatial symmetric bivector block. The spatial Ricci tensor is

\[
R_{abcd}=R_{cdab},\qquad
\mathrm{Ric}_{ij}=\delta^{kl}R_{kilj}=0,\qquad
\boxed{R_{ijkl}=0\quad (i,j,k,l\in\{1,2,3\}).}
\]

In three spatial dimensions the intrinsic algebraic Riemann tensor is completely determined by its Ricci tensor. Here its six independent components map to the six spatial Ricci components via an **invertible six-by-six linear map** (symbolically certified). Therefore vacuum Ricci flatness implies

\[
\boxed{\mathrm{Ric}_{\mu\nu}=0,\quad T^a=0,\quad
e^a=D X^a/q,\quad X^2<0\quad\Longrightarrow\quad
R_{\mu\nu\rho\sigma}=0.}
\]

**Scope:** this uses the independent parent vacuum Einstein equation and a torsion-free Levi–Civita connection. The previous curved **torsionful** local representation theorem is not contradicted.

## Einstein vacuum with cosmological constant

The curvature-kernel identity forces the Ricci contraction along X to vanish. For an Einstein space this yields

\[
\mathrm{Ric}_{\mu\nu}=\Lambda g_{\mu\nu},\quad
R^\rho{}_{\sigma\mu\nu}X^\sigma=0
\quad\Longrightarrow\quad
\mathrm{Ric}_{\mu\nu}X^\nu=0
\quad\Longrightarrow\quad \boxed{\Lambda=0}.
\]

Hence the torsion-free concurrent timelike vacuum branch cannot produce a positive or negative cosmological-constant Einstein background either. It does not exclude a composite UBT solution with nonzero spin torsion and non-Einstein parent Euler terms.

## Why real Holst mixing does not evade this restricted branch

For Lorentzian internal bivectors, the Hodge star obeys a complex-structure identity. For arbitrary real Palatini and Holst coefficients

\[
(*F)_{ab}=\frac12\epsilon_{ab}{}^{cd}F_{cd},
\qquad *^2=-\mathrm{id}_{\Lambda^2},\qquad
\boxed{\det(c_{\mathrm H}\mathrm{id}+c_{\mathrm{EC}}*)=
(c_{\mathrm H}^2+c_{\mathrm{EC}}^2)^3.}
\]

The curvature-to-Cartan bivector operator is algebraically invertible for any nonzero real coefficient pair. Under the **standard invertible nondegenerate Palatini–Holst Cartan torsion map** already recognized conditionally in the canonical registry, vanishing independent spin current gives T=0. In the *actual composite* spin equation of merged PR #694, however, the parent tetrad source also appears:

\[
\mathcal E_a^{\rm parent}=0,\qquad
\mathcal C_{ab}^{\rm comp}
=\mathcal C_{ab}^{\rm parent}
+q^{-1}(X_b\mathcal E_a^{\rm parent}
-X_a\mathcal E_b^{\rm parent})=0
\quad\Longrightarrow\quad
\mathcal C_{ab}^{\rm parent}=0.
\]

If the parent tetrad Euler equation vanishes too, the composite spin equation reduces to the parent Cartan equation; standard regularity then forces T=0 and the above rigidity applies. **Conversely**, if the parent Euler source is nonzero, the composite spin equation may balance it by nonzero torsion: this theorem cannot discard such branches.

## Explicit first-order gravitational-wave exclusion on the restricted branch

Choose a standard plane transverse-traceless (TT) perturbation of Minkowski space, propagating along the z-axis. It solves the **linearized vacuum Einstein equation** but has nonzero electric linearized Riemann curvature:

\[
h_{11}=-h_{22}=A\cos[k(t-z)],\qquad
\mathrm{Ric}^{(1)}_{\mu\nu}[h]=0,\qquad
\boxed{R^{(1)}_{0101}[h]=\frac{Ak^2}{2}\cos[k(t-z)]\ne0.}
\]

For nonzero amplitude and wave number at a generic phase, this violates the necessary condition that the timelike X lie in the kernel of every Riemann curvature two-form. Therefore usual Einstein-parent-shell plane gravitons cannot be lifted using **zero torsion** on this timelike sector. This is stronger than the known Schwarzschild no-go, but does NOT rule out radiative metrics represented with torsion and nonzero parent Euler residuals.

## Decision for UBT

Exactly what the theorem forces is

\[
\boxed{\text{Nonflat vacuum curvature in the timelike composite branch}
\quad\Longrightarrow\quad
\neg(T=0\ \wedge\ \mathcal E^{\rm parent}=0).}
\]

The next real test is **not another potential**. Linearize the **joint unrestricted composite** Palatini–Holst field and spin Euler equations from merged PR #694 about a proven flat on-shell affine representer; do not set the parent tetrad Euler form or torsion to zero. Count the solutions and gauge directions of the full constrained system and determine whether torsion supports healthy tensor curvature or forces a pathology. The minimal fixed-background eight-real kinetic signature also needs a separate physical Dirac reduction.

**Code verification:** `tools/verify_torsionfree_vacuum_rigidity.py` and `tests/test_torsionfree_vacuum_rigidity.py`, exact SymPy checks including six-by-six Ricci inversion, the internal Hodge determinant, and linear TT-wave Ricci/Riemann tensors. **Repo grounding:** `canonical/geometry/connection.tex` and `canonical/CANONICAL_DEFINITIONS.md` (existing torsion-free Schwarzschild obstruction); merged PR #694 (full composite spin equation); merged PR #693 (conditional Palatini–Holst comparator). No unique fundamental UBT action or CMB prediction claimed.
