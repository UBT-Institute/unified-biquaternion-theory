<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Yang--Mills threshold matching benchmark for the Stiefel HLS route

**Status:** quantitative one-loop matching benchmark.  It shows that a weak
frame-loop induced kinetic term is too small to generate a large confinement
hierarchy without leaving perturbation theory.

## 1. Matching assumption

Assume a candidate quantum phase has been found with:

\[
m_{B,\rm ren}^2=0,
\qquad
Z_B(M_\beta)>0,
\qquad
M_\beta^2>0,
\]
where \(M_\beta\) is the mass gap of the charged frame/coset triplet.

Below
\[
\mu<M_\beta
\]
integrate out the charged frame matter.

If no additional light coloured matter remains, the leading colour EFT is
pure \(SU(3)\) Yang--Mills with
\[
\boxed{b_0=11}
\]
in
\[
\beta(g)
=
-\frac{b_0}{16\pi^2}g^3+\cdots .
\]

The matching convention is
\[
\boxed{
\frac1{g^2(M_\beta)}
=
Z_B(M_\beta).
}
\]

## 2. Pure-Yang--Mills running

At one loop,
\[
\frac{d}{d\ln\mu}\frac1{g^2}
=
\frac{b_0}{8\pi^2}.
\]

Therefore
\[
\boxed{
\frac1{g^2(\mu)}
=
Z_B(M_\beta)
+
\frac{11}{8\pi^2}
\ln\frac{\mu}{M_\beta}.
}
\]

Define the one-loop strong scale by the zero of the perturbative inverse
coupling:
\[
\boxed{
\Lambda_{\rm YM}
=
M_\beta
\exp\left[
-\frac{8\pi^2}{11}Z_B(M_\beta)
\right].
}
\]

Equivalently, for a desired hierarchy
\[
R:=\frac{M_\beta}{\Lambda_{\rm YM}},
\]
one requires
\[
\boxed{
Z_B(M_\beta)
=
\frac{11}{8\pi^2}\ln R.
}
\]

## 3. Numerical benchmarks

For illustration:

\[
R=10:
\qquad
Z_B\simeq0.321,
\qquad
g(M_\beta)\simeq1.77;
\]

\[
R=10^2:
\qquad
Z_B\simeq0.642,
\qquad
g(M_\beta)\simeq1.25;
\]

\[
R=10^3:
\qquad
Z_B\simeq0.962,
\qquad
g(M_\beta)\simeq1.02.
\]

Thus a substantial scale hierarchy requires an order-one inverse gauge
coefficient at the frame-matter threshold.

## 4. Compare with the weak induced coefficient

The fixed-frame weak-current benchmark gives
\[
Z_B^{\rm weak}
=
\frac{a_H^2}{96\pi^2}
L,
\qquad
L:=
\ln\frac{\Lambda_{\rm UV}^2}{M_\beta^2},
\]
where
\[
a_H=c_V/c_3
\]
in the corresponding normalization.

Combining with the Yang--Mills hierarchy condition yields
\[
\boxed{
a_H^2L
=
12b_0\ln R
=
132\ln R.
}
\]

For
\[
R=10^3,
\]
this requires
\[
\boxed{
a_H^2L
\simeq
9.12\times10^2.
}
\]

## 5. Weak-coupling self-consistency test

If
\[
a_H\lesssim1
\]
and the logarithm is of ordinary perturbative size,
\[
L=O(1\text{--}10),
\]
then
\[
Z_B^{\rm weak}\ll1.
\]

The resulting confinement scale is then close to the matching scale:
\[
\frac{M_\beta}{\Lambda_{\rm YM}}
=
\exp\left(
\frac{8\pi^2}{11}Z_B
\right)
\approx1.
\]

For example
\[
a_H=1,\qquad L=10
\]
gives
\[
Z_B\simeq0.0106
\]
and only
\[
M_\beta/\Lambda_{\rm YM}\simeq1.08.
\]

To obtain a hierarchy of \(10^3\) with a moderate
\[
L\simeq10
\]
would require
\[
a_H\simeq9.55,
\]
which is not a controlled weak-current expansion.

## 6. Consequence

The one-loop HLS calculation is valuable for establishing the **sign** and
existence of the induced gauge kinetic term.

It is not quantitatively sufficient to explain a well-separated Yang--Mills
confinement scale in its own weak-coupling regime.

Therefore
\[
\boxed{
\text{useful QCD-like scale separation}
\Rightarrow
\text{strong/critical HLS dynamics or another enhancement mechanism}.
}
\]

This conclusion is independent of the already open masslessness problem.

Both conditions must ultimately be solved:
- reach the zero-locking/massless gauge surface;
- generate a sufficiently large positive \(Z_B\).

## 7. Important compositeness-scale warning

One must not impose
\[
Z_B(\Lambda)=0
\]
at the same matching scale below which an already autonomous asymptotically
free pure-Yang--Mills EFT is assumed.

For \(b_0>0\), running downward from such a boundary would formally make the
one-loop inverse coupling negative.

The consistent picture requires a higher regime in which frame/collective
dynamics first generates a positive \(Z_B\), followed by matching onto the
autonomous Yang--Mills regime at a lower scale.

This supports the two-stage emergence picture:
\[
\boxed{
\text{generation regime}
\to
\text{critical/decoupling match}
\to
\text{Yang--Mills running}.
}
\]

Verification:
verification/su3_hls_ym_matching_check.py
