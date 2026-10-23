<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Underdetermination theorem for induced SU(3) coupling from the compact-psi tower

**Status:** exact monotonicity/underdetermination result for the conditional
KK-induced coupling branch.

## 1. Tower function

For the nonzero \(S^1_\psi\) KK modes define
\[
\Delta(a)
=
2\sum_{n=1}^\infty
E_1\!\left(\frac{n^2}{a^2}\right),
\qquad
a:=\Lambda R_\psi>0.
\]

This is the finite nonzero-mode contribution to the proper-time threshold
factor for a massless charged triplet.  A massive zero mode or matching scale
adds a separate logarithmic/threshold term and does not alter the conclusion
below.

## 2. Strict monotonicity

Using
\[
\frac{d}{dx}E_1(x)=-\frac{e^{-x}}{x},
\qquad
x=\frac{n^2}{a^2},
\]
one obtains term by term
\[
\frac{d}{da}
E_1\!\left(\frac{n^2}{a^2}\right)
=
\frac{2}{a}
e^{-n^2/a^2}.
\]

Therefore
\[
\boxed{
\Delta'(a)
=
\frac4a
\sum_{n=1}^\infty e^{-n^2/a^2}
>0
}
\]
for every \(a>0\).

Moreover,
\[
\lim_{a\to0^+}\Delta(a)=0,
\]
while Poisson/integral asymptotics give
\[
\Delta(a)\sim2\sqrt\pi\,a
\qquad(a\to\infty),
\]
so
\[
\lim_{a\to\infty}\Delta(a)=\infty.
\]

Hence
\[
\boxed{
\Delta:(0,\infty)\to(0,\infty)
}
\]
is continuous and strictly increasing.

## 3. Coupling underdetermination

In the minimal one-complex-triplet branch,
\[
\frac1{g_{\rm ind}^2}
=
\frac{1}{96\pi^2}
\left[
I_{\rm zero}
+
\Delta(\Lambda R_\psi)
\right],
\]
where \(I_{\rm zero}\) contains the zero-mode mass/matching dependence.

If \(I_{\rm zero}\) is fixed and the target inverse coupling is larger than
its zero-mode contribution, strict monotonicity implies that there is a
**unique** value of
\[
a=\Lambda R_\psi
\]
that reproduces that target.

Thus a desired strong coupling can always be matched by choosing \(a\).

This is not a prediction.

\[
\boxed{
\text{Without an independent derivation of }\Lambda R_\psi,
\quad
g_{\rm ind}
\text{ is underdetermined.}
}
\]

If the zero-mode threshold \(m/\Lambda\) is also free, the underdetermination
is stronger because the coupling depends on at least two undetermined
dimensionless ratios.

## 4. Relation to the radius-stabilisation audit

The newer exact scale audit in
\`research_tracks/theta_torus_potential/one_loop_scale_no_go.md\`
shows that the isolated massless determinant has only logarithmic scale
dependence and no finite minimum, while inversion symmetrisation makes the
scale direction flat.

Therefore the one-loop determinant does not independently select the value of
\(R_\psi\) needed by the induced-colour formula.

The older file
\`canonical/geometry/Rpsi_dynamical_fix.tex\`
contains a historical self-dual-stabilisation claim and an incompatible
Epstein-zeta scaling statement.  It is superseded as a status source by the
October 2026 scale audit.

## 5. Consequence for the SU(3) programme

The exact coset rewrite
\[
\Theta=\rho\,g e_0,
\qquad
g\sim g h(x),\quad h(x)\in SU(3),
\]
still provides a genuine local \(SU(3)\) redundancy.

What fails at present is predictive normalization:

- the projected/collective connection is kinematically derived;
- the heat kernel conditionally generates \(F^2\);
- the compact tower conditionally enhances its coefficient;
- but the coefficient is a monotone function of an undetermined
  \(\Lambda R_\psi\).

Thus
\[
\boxed{
\text{geometric }SU(3)\text{ redundancy: conditional exact;}
\qquad
\text{predicted }g_s:\text{ open.}
}
\]

## 6. Falsification/closure target

To turn the induced branch into a prediction, the same finalized UBT action
must independently determine:

1. the physical compact radius \(R_\psi\);
2. the UV/matching scale \(\Lambda\);
3. the charged Hessian spectrum and zero-mode threshold;
4. the physical gauge/ghost quotient.

Only then may the resulting \(g_{\rm ind}\) be compared with QCD.

Choosing \(\Lambda R_\psi\) after comparison with the observed strong coupling
is explicitly forbidden as a derivation.

Verification:
\`verification/su3_induced_coupling_underdetermination_check.py\`.
