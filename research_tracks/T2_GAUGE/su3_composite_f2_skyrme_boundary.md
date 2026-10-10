<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Induced F^2 is a quartic coset/Skyrme term, not a gluon kinetic term

**Status:** exact local order-counting theorem for the conditional
\(SU(1,3)/SU(3)\) collective-frame branch.

## 1. Reductive coset variables

Let
\[
G/H=SU(1,3)/SU(3),
\qquad
\mathfrak g=\mathfrak h\oplus\mathfrak m,
\]
with
\[
\mathfrak h=su(3).
\]

Choose a local representative
\[
g(x)=e^{\pi(x)},
\qquad
\pi(x)\in\mathfrak m
\]
near a constant reference configuration.

Write the Maurer--Cartan form as
\[
\omega=g^{-1}dg=A+E,
\]
where
\[
A=P_{\mathfrak h}\omega,
\qquad
E=P_{\mathfrak m}\omega.
\]

## 2. Small-field expansion

The Baker--Campbell--Hausdorff expansion gives
\[
e^{-\pi}de^\pi
=
d\pi
+\frac12[d\pi,\pi]
+\frac16[[d\pi,\pi],\pi]
+\cdots .
\]

Since
\[
d\pi\in\mathfrak m,
\]
the leading coset vielbein is
\[
\boxed{
E=d\pi+O(\pi\,d\pi).
}
\]

The connection has no term linear in \(\pi\):
\[
\boxed{
A
=
\frac12P_{\mathfrak h}[d\pi,\pi]
+O(\pi^2d\pi)
=
O(\pi\,d\pi).
}
\]

Thus the composite \(SU(3)\) frame connection begins at second order in the
small coset field counting.

## 3. Curvature order

The Maurer--Cartan identity
\[
d\omega+\omega\wedge\omega=0
\]
implies, in the reductive split,
\[
F_A
=
dA+A\wedge A
=
-\bigl(E\wedge E\bigr)_{\mathfrak h}
\]
up to the convention for the Lie-bracket/wedge normalization.

Therefore
\[
\boxed{
F_A
=
O(d\pi\wedge d\pi)
+
O(\pi(d\pi)^2).
}
\]

In particular there is no term linear in \(\pi\):
\[
\boxed{
F_A^{(1)}=0.
}
\]

## 4. Meaning of the heat-kernel term

The conditional one-loop heat-kernel calculation produces
\[
\Gamma_{\rm 1PI}
\supset
c_F
\int
\operatorname{tr}(F_A\wedge *F_A).
\]

Substituting the exact composite connection gives
\[
\boxed{
\operatorname{tr}F_A^2
=
O\!\left((d\pi)^4\right)
}
\]
around the constant coset vacuum.

Hence this term contributes no quadratic two-point kernel for \(\pi\).

It is a four-derivative quartic interaction of the sigma-model/coset
fluctuations, analogous to a Skyrme-type term.

## 5. Why this is not an independent Yang--Mills kinetic term

If \(A_\mu^a\) were an independent gauge field, then
\[
\int\operatorname{tr}F_A^2
\]
would contain the ordinary quadratic operator
\[
A_\mu
\left(
-p^2\eta^{\mu\nu}+p^\mu p^\nu
\right)
A_\nu
\]
and would define a gauge-field propagator after gauge fixing.

For the composite
\[
A=A[\pi],
\]
the linear piece \(A^{(1)}\) vanishes, so this quadratic gauge-field operator
does not appear in the original \(\pi\) variables.

Therefore
\[
\boxed{
\text{heat-kernel }F_A^2
\text{ on the composite frame}
\neq
\text{eight propagating gluon kinetic terms}.
}
\]

The heat-kernel result is a valid background-response/higher-derivative
statement, but not a derivation of independent QCD gauge modes.

## 6. Relation to the induced-coupling estimate

Earlier estimates of
\[
1/g_{\rm ind}^2
\]
remain useful **if** an independent/collective \(SU(3)\) connection is first
derived.

They must not be interpreted as a physical strong coupling for the purely
composite Maurer--Cartan/projection connection by itself.

Without an independent gauge-field 1PI variable, the coefficient instead
normalizes a four-derivative operator in the coset effective action.

## 7. Consequence for the P2 endgame

The following chain is now excluded:
\[
\text{moving colour bundle}
\to
\text{composite }A[\Theta]
\to
a_4\supset F_A^2
\to
\text{QCD gluons}.
\]

The correct statement is:
\[
\boxed{
\text{moving colour bundle}
\to
\text{composite frame curvature}
\to
\text{Skyrme-like higher-derivative interaction}.
}
\]

A physical Yang--Mills sector still requires a collective variable whose
connection has an independent linear fluctuation and whose full 1PI action
satisfies the non-Abelian gauge identities.

Verification:
\`verification/su3_composite_f2_order_check.py\`.
