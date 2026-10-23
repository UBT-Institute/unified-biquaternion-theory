<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Weak fixed-frame HLS one-loop benchmark

**Status:** conditional perturbative benchmark for the finite Stiefel/HLS route.
It is not the nonperturbative phase calculation.

## 1. Canonically normalized triplet

The positive physical triplet kinetic is
\[
\mathcal L_{\beta}
=
c_3\,\partial_\mu\beta^\dagger\partial^\mu\beta+\cdots .
\]

Define
\[
\phi=\sqrt{c_3}\,\beta.
\]

Then \(\phi\) is one canonically normalized complex \(SU(3)\) fundamental
triplet.

The leading frame current is
\[
C_{\mu,0}
=
\frac12
\left[
\beta\,\partial_\mu\beta^\dagger
-
(\partial_\mu\beta)\beta^\dagger
\right]_0.
\]

The vertical HLS term contains
\[
2c_V\operatorname{tr}(B_\mu C_0^\mu).
\]

For
\[
B_\mu=iB_\mu^aT^a,
\qquad
\operatorname{tr}(T^aT^b)=\frac12\delta^{ab},
\]
this is the standard adjoint scalar current coupling, with magnitude
\[
\boxed{
g_0=\frac{c_V}{c_3}
}
\]
after canonical normalization of \(\phi\), up to the harmless overall sign
convention for \(B_\mu\).

## 2. Induced transverse kinetic coefficient

For one complex scalar in the fundamental representation,
\[
T(\mathbf3)=\frac12.
\]

The logarithmic one-loop vacuum polarization therefore gives
\[
\boxed{
Z_B^{(1)}
=
\frac{g_0^2}{96\pi^2}
\ln\frac{\Lambda^2}{\mu^2}
}
\]
in the convention
\[
\Gamma^{(2)}_{\mu\nu}
\supset
Z_B
(p^2\eta_{\mu\nu}-p_\mu p_\nu).
\]

Equivalently,
\[
\boxed{
Z_B^{(1)}
=
\frac{c_V^2}{96\pi^2c_3^2}
\ln\frac{\Lambda^2}{\mu^2}.
}
\]

The sign is positive.

Thus the weak finite triplet fluctuations do generate a dynamical transverse
kinetic response for the hidden-local connection.

This is the positive part of the HLS mechanism.

## 3. Tree HLS mass in the fixed-frame phase

At the reference fixed frame,
\[
C_{\mu,0}=0,
\]
and
\[
\mathcal L_V
=
-c_V\operatorname{tr}B_\mu B^\mu.
\]

With the generator normalization above,
\[
-\operatorname{tr}B_\mu B^\mu
=
\frac12B_\mu^aB^{a\mu}.
\]

Hence the unnormalized vector mass coefficient is \(c_V\).

After the loop-generated kinetic term is canonically normalized, the pole-mass
scale is parametrically
\[
\boxed{
m_B^2
\simeq
\frac{c_V}{Z_B}
=
\frac{96\pi^2c_3^2}
{c_V\ln(\Lambda^2/\mu^2)}
}
\]
within this leading-log fixed-frame approximation.

Therefore for finite positive
\[
c_V,\ c_3,\ \ln(\Lambda^2/\mu^2)
\]
one has
\[
\boxed{m_B^2>0.}
\]

## 4. No interacting massless weak limit

The induced canonical gauge coupling is
\[
g_H^2
=
\frac1{Z_B}
=
\frac{96\pi^2c_3^2}
{c_V^2\ln(\Lambda^2/\mu^2)}.
\]

Two naive limits illustrate the obstruction:

### c_V -> 0
\[
Z_B\to0,
\qquad
g_H^2\to\infty,
\]
while the induced gauge description disappears.

### c_V -> infinity
\[
m_B^2\to0,
\qquad
g_H^2\to0.
\]

The vector becomes massless only together with a vanishing interaction in this
simple leading-log scaling limit.

Hence the weak fixed-frame branch has no finite-coupling massless vector point.

## 5. Interpretation

This benchmark does **not** rule out the HLS route.

It proves something narrower and useful:
\[
\boxed{
\text{massless interacting colour is not a weak perturbation of the fixed
Stiefel frame.}
}
\]

A viable QCD-like phase must rely on a genuinely different quantum saddle or
critical phase in which the renormalized mass term vanishes nonperturbatively
while
\[
Z_B>0
\]
remains finite.

That is precisely the phenomenon known in some constrained large-\(N\)
Grassmannian/HLS systems, but it remains to be derived for the finite
noncompact UBT model.

## 6. Caveats

The numerical coefficient above is a leading weak-current benchmark.

A complete finite UBT calculation must include:
- nonlinear constraint contributions;
- HLS gauge fixing and ghosts;
- the singlet sector;
- the full positive two-coupling target metric;
- finite threshold terms;
- GR/tetrad backreaction.

Those effects can modify finite terms and the phase diagram.

They do not turn this fixed-frame leading-log calculation into a proof of an
unbroken phase.

## 7. Decision target

The next nonperturbative calculation must demonstrate a zero of the
renormalized HLS mass function at finite interaction:
\[
\boxed{
m_{B,\rm ren}^2=0,
\qquad
0<Z_B<\infty.
}
\]

Without such a point/phase, the Stiefel HLS route gives vector-meson-like
massive states rather than QCD colour.

Verification:
\`verification/su3_hls_fixed_frame_one_loop_check.py\`.
