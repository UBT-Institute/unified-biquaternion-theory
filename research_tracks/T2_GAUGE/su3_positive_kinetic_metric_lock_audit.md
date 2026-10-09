<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Metric-lock audit of the positive timelike kinetic candidate

**Status:** exact algebraic compatibility result.  It shows that the healthy
fixed-background sigma-model spectrum does not survive as an independent
internal colour kinetic sector once the canonical Theta-derived metric is
imposed.

## 1. Candidate kinetic metric

On
\[
h:=\Theta^\dagger G\Theta>0,
\qquad
G=\operatorname{diag}(1,-1,-1,-1),
\]
the positive field-dependent metric is
\[
K_\Theta^+(u,v)
=
-u^\dagger Gv
+
2\frac{(u^\dagger G\Theta)(\Theta^\dagger Gv)}{h}.
\]

Define
\[
c_\mu:=\Theta^\dagger G D_\mu\Theta.
\]

Then
\[
K_\Theta^+(D_\mu\Theta,D_\nu\Theta)
=
-(D_\mu\Theta)^\dagger G(D_\nu\Theta)
+
2\frac{\bar c_\mu c_\nu}{h}.
\]

## 2. Exact relation on the canonical Lorentz tetrad slice

The canonical tetrad is
\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta
\]
with Lorentz-real coefficient form
\[
E_\mu
=
i e_\mu{}^0\,1+e_\mu{}^k e_k,
\qquad e_\mu{}^a\in\mathbb R.
\]

For the coefficient-space Hermitian form \(G\),
\[
E_\mu^\dagger G E_\nu
=
e_\mu{}^0e_\nu{}^0
-
e_\mu{}^ke_\nu{}^k
=
-g_{\mu\nu},
\]
because the canonical spacetime metric is
\[
g_{\mu\nu}
=
-e_\mu{}^0e_\nu{}^0
+
e_\mu{}^ke_\nu{}^k.
\]

Therefore
\[
\boxed{
-(D_\mu\Theta)^\dagger G(D_\nu\Theta)
=
\mathcal N_0 g_{\mu\nu}.
}
\]

This identity is independent of the field potential and uses only the
canonical Lorentz tetrad slice.

## 3. Metric-locked kinetic collapse

Contracting with the same derived inverse metric gives
\[
\boxed{
g^{\mu\nu}
K_\Theta^+(D_\mu\Theta,D_\nu\Theta)
=
4\mathcal N_0
+
\frac{2}{h}
g^{\mu\nu}\bar c_\mu c_\nu.
}
\]

Thus for the action convention with a factor \(1/2\),
\[
\boxed{
\mathcal L_{\rm kin}^{(+)}
=
\sqrt{|g|}
\left[
2\mathcal N_0
+
\frac1h g^{\mu\nu}\bar c_\mu c_\nu
\right].
}
\]

The first term is only a volume/cosmological term.  All dependence beyond the
metric lock is carried by the single complex one-form \(c_\mu\).

This is the nonlinear analogue of the existing metric-lock collapse theorem
for the constant sharp/Minkowski kinetic pairing.

## 4. Constant-h branch

If the connection is compatible with \(G\), then
\[
D_\mu h
=
\bar c_\mu+c_\mu
=
2\operatorname{Re}c_\mu.
\]

On the symmetry-enhanced potential vacuum
\[
h=h_*=\text{constant},
\]
one therefore has
\[
\operatorname{Re}c_\mu=0.
\]

Write
\[
c_\mu=i j_\mu,
\qquad j_\mu\in\mathbb R.
\]

Then
\[
\boxed{
\mathcal L_{\rm kin}^{(+)}
=
\sqrt{|g|}
\left[
2\mathcal N_0
+
\frac1{h_*}g^{\mu\nu}j_\mu j_\nu
\right].
}
\]

So after the metric lock and restriction to the potential vacuum, the
additional kinetic information is a **single real singlet/phase current**.

The six real tangent directions forming the candidate complex colour triplet
do not appear as an independent internal quadratic kinetic sector.

## 5. Consequence for the fixed-background 1+7 spectrum

On a fixed external metric the positive kinetic candidate plus
\(\lambda_2=0\) potential has one radial massive mode and seven massless tangent
modes.

That statement remains correct for the fixed-background action.

But it must not be promoted to the canonical single-Theta theory with
\[
g=g[D\Theta].
\]

After the canonical metric is substituted back, the same kinetic scalar
collapses to a volume term plus the singlet current above.  The apparent
triplet kinetic modes have become part of the composite metric/tetrad
description rather than a separate internal matter sector.

Therefore
\[
\boxed{
\text{healthy fixed-background colour-triplet modes}
\not\Rightarrow
\text{independent colour modes in the metric-locked theory}.
}
\]

## 6. Fixed-background Euler--Lagrange equation

For completeness, when \(g_{\mu\nu}\) and a \(G\)-compatible connection are
held fixed, define
\[
u_\mu=D_\mu\Theta,
\qquad
K_\Theta=-G+2\frac{G\Theta\Theta^\dagger G}{h}.
\]

Treating \(\Theta\) and \(\Theta^\dagger\) independently in the usual complex
variation, the equation obtained from
\[
S=\int\sqrt{|g|}\,
\left[
g^{\mu\nu}u_\mu^\dagger K_\Theta u_\nu
-
V(h)
\right]
\]
can be written
\[
\boxed{
D_\mu(K_\Theta D^\mu\Theta)
-
\frac{2}{h}\bar c_\mu\,G D^\mu\Theta
+
\left(
\frac{2}{h^2}\bar c_\mu c^\mu
+
V'(h)
\right)G\Theta
=0
}
\]
up to the declared convention for the adjoint covariant divergence.

For the enhanced potential,
\[
V(h)=V_0+2\mu h+4\lambda_1h^2,
\]
so
\[
V'(h)=2\mu+8\lambda_1h.
\]

At the constant timelike vacuum
\[
h_*=-\frac{\mu}{4\lambda_1},
\]
the potential derivative vanishes and the fixed-background principal kinetic
metric is \(K_{\Theta_0}=I_4\).

This equation is **not** the complete metric-locked Euler--Lagrange equation,
because varying the canonical single-Theta action also varies
\(g[D\Theta]\), the connection/torsion composites, the measure and the
constraints.

## 7. What remains of the candidate

The positive metric is still useful as:
- a fixed-background fluctuation metric;
- a possible nonlinear sigma-model effective branch;
- a diagnostic positive metric on the timelike field cone.

But it does not solve the main colour problem inside the canonical
metric-locked single-field architecture.

The colour programme therefore returns to the harder collective-gauge
question: a physical gluon sector must arise from an additional exact
collective/quantum mechanism, not from interpreting the tangent
\(\mathbf3_{\mathbb C}\) of Theta as six independent colour matter modes.

## 8. Next canonical calculation

The remaining honest calculation is the complete second variation of
\[
\sqrt{|g[D\Theta]|}
\left[
2\mathcal N_0+\frac1h g^{\mu\nu}\bar c_\mu c_\nu
-\kappa V(h)
\right]
\]
including the implicit variations of:
- the tetrad \(E_\mu[D\Theta]\);
- \(g_{\mu\nu}[E]\);
- the selected two-sided connection/torsion branch;
- the volume measure;
- gauge/constraint zero modes.

Until an admissible nondegenerate background solving the full defining system
is specified, that composite Hessian cannot be replaced by the fixed-background
eight-scalar Hessian.

Verification:
\`verification/su3_positive_kinetic_metric_lock_check.py\`.
