<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Flat-affine tetrad no-go for an exact constant-h SU(1,3)/SU(3) vacuum

**Status:** exact local no-go for combining the enhanced pointwise vacuum with
the simplest flat inertial Theta representer.

## 1. Flat affine representer

The canonical tetrad construction admits, in the flat inertial branch with
trivialized connection,
\[
\Theta(x)
=
\Theta_0
+
\sqrt{\mathcal N_0}\,E_\mu x^\mu,
\]
where \(E_\mu\) is a constant nondegenerate Lorentz tetrad.

Let
\[
h(x)=\Theta(x)^\dagger G\Theta(x),
\qquad
G=\operatorname{diag}(1,-1,-1,-1).
\]

On the canonical Lorentz slice,
\[
E_\mu^\dagger G E_\nu=-g_{\mu\nu}.
\]

## 2. Exact Hessian of h

Differentiate the affine expression.  Since
\[
\partial_\mu\Theta=\sqrt{\mathcal N_0}E_\mu,
\]
one obtains
\[
\partial_\mu\partial_\nu h
=
2\mathcal N_0\,
\operatorname{Re}
(E_\mu^\dagger G E_\nu).
\]

The tetrad Gram matrix is already real, hence
\[
\boxed{
\partial_\mu\partial_\nu h
=
-2\mathcal N_0\,g_{\mu\nu}.
}
\]

For a nondegenerate spacetime metric this matrix is nonzero and nondegenerate.

Therefore \(h(x)\) cannot be constant on any open set.

## 3. Consequence for the enhanced potential vacuum

The symmetry-enhanced branch
\[
\lambda_2=0,\qquad
V=V_0+\mu H+\lambda_1H^2
\]
has pointwise minima at
\[
H=H_*,
\qquad
h=h_*=H_*/2.
\]

The flat affine representer therefore cannot remain exactly on the pointwise
vacuum manifold while also generating a nondegenerate constant tetrad:

\[
\boxed{
\text{flat affine nondegenerate tetrad}
\quad\Longrightarrow\quad
h(x)\ \text{is not constant}.
}
\]

Equivalently,
\[
\boxed{
\text{exact }SU(1,3)/SU(3)\text{ pointwise vacuum}
+
\text{flat affine Theta representer}
+
\det e\neq0
}
\]
is impossible.

## 4. What can evade the no-go

The result is intentionally narrow.  It does not exclude:

1. a nontrivial two-sided connection for which \(D_\mu\Theta\neq\partial_\mu
   \Theta\);
2. torsion/relative-connection backgrounds that keep \(h\) fixed while moving
   Theta along its timelike orbit;
3. a physical background that does not sit exactly at the pointwise minimum;
4. a spacetime-dependent radial mode whose potential and derivative energy
   balance in the full Euler--Lagrange equations.

But it establishes that the enhanced colour vacuum cannot simply be combined with
the repository's simplest flat affine GR representer.

## 5. Implication for the full Hessian programme

A physically relevant Hessian for the enhanced branch must be expanded around
an **action-selected nontrivial connection/torsion background**, or around a
non-vacuum radial profile.

Expanding around a constant Theta vacuum with an externally held flat metric
is therefore not the same problem as expanding around a canonical
single-Theta spacetime solution.

The next required background equation is
\[
D_\mu\Theta
=
\sqrt{\mathcal N_0}E_\mu
\]
together with:
- \(h(\Theta)=h_*\) if the exact vacuum manifold is imposed;
- the connection/torsion field equations;
- the nondegenerate tetrad condition;
- the full Theta Euler--Lagrange equation.

Verification:
\`verification/su3_flat_affine_vacuum_no_go.py\`.
