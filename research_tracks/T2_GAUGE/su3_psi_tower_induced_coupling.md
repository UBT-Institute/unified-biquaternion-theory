<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Compact-psi tower stress test for induced SU(3) coupling

**Status:** conditional exact KK heat-trace benchmark.  It tests whether the
existing compact \(S^1_\psi\) spectrum can naturally amplify the minimal
induced-colour coefficient.

## 1. KK-resolved induced coupling

Assume one charged complex \(SU(3)\) fundamental triplet with KK masses
\[
M_n^2=m^2+\frac{n^2}{R_\psi^2},
\qquad n\in\mathbb Z,
\]
and a minimal Laplace-type Hessian.

With a proper-time cutoff \(\Lambda\), the induced inverse coupling is
\[
\boxed{
\frac1{g_{\rm ind}^2}
=
\frac{1}{96\pi^2}
I_0^{\rm KK}(\Lambda,R_\psi,m)
}
\]
with
\[
I_0^{\rm KK}
=
\int_{\Lambda^{-2}}^\infty
\frac{ds}{s}\,
e^{-m^2s}
\vartheta_3(0,e^{-s/R_\psi^2}).
\]

Equivalently,
\[
\boxed{
I_0^{\rm KK}
=
\sum_{n\in\mathbb Z}
E_1\!\left(
\frac{m^2+n^2/R_\psi^2}{\Lambda^2}
\right).
}
\]

For \(m=0\), the zero mode is infrared divergent, so separate the finite
nonzero-KK contribution
\[
\Delta_{\rm KK}(a)
=
2\sum_{n=1}^\infty
E_1\!\left(\frac{n^2}{a^2}\right),
\qquad
a:=\Lambda R_\psi.
\]

## 2. Self-dual scale does not provide a large enhancement

At
\[
a=1,
\]
the exact numerical value is
\[
\boxed{
\Delta_{\rm KK}(1)
=
0.446351481601138664\ldots
}
\]

Thus the entire tower of nonzero KK modes adds less than one unit to the
proper-time logarithmic factor.  It cannot repair the minimal one-triplet
coupling deficit.

This is directly relevant to the optional self-dual identification already
used in the conditional induced-gravity branch,
\[
\Lambda R_\psi=1.
\]

Therefore:
\[
\boxed{
\text{self-dual } \Lambda R_\psi=1
\text{ does not generate a strong induced }SU(3)\text{ coupling.}
}
\]

## 3. Large-radius / high-cutoff asymptotic

For \(a\gg1\),
\[
\Delta_{\rm KK}(a)
=
2\sqrt\pi\,a+O(\log a).
\]

The leading term follows from replacing the sum by an integral:
\[
2\sum_{n\ge1}E_1(n^2/a^2)
\sim
2a\int_0^\infty E_1(x^2)\,dx
=
2\sqrt\pi\,a.
\]

Thus a sufficiently dense KK tower can strongly enhance the induced coupling,
but the enhancement is power-like in the dimensionless hierarchy
\[
a=\Lambda R_\psi.
\]

## 4. Required hierarchy

For one complex triplet and the orientation target \(g_{\rm ind}=1\), the
required total threshold factor is
\[
I_0^{\rm KK}\sim96\pi^2\approx947.48.
\]

If the nonzero tower is asked to provide this magnitude by itself,
the exact KK sum gives approximately
\[
\boxed{
\Lambda R_\psi\approx271.3.
}
\]

For the smaller reference target
\[
I_0^{\rm KK}\approx636.6,
\]
the required value is still
\[
\Lambda R_\psi\approx183.4.
\]

Hence the compact tower can rescue the magnitude only if UBT derives a large
separation between the ultraviolet cutoff and the compactification scale.

## 5. Physical interpretation

This is not automatically inconsistent.  It gives a concrete fork:

### Branch A — self-dual / modest hierarchy

If the finalized theory fixes
\[
\Lambda R_\psi=O(1),
\]
the nonzero KK tower gives only an \(O(1)\) threshold correction.  The
induced-only one-triplet route remains far too weak unless additional charged
sectors or another normalization mechanism are derived.

### Branch B — large KK tower

If the action independently yields
\[
\Lambda R_\psi\gg1,
\]
many KK modes contribute below the cutoff and the induced inverse coupling can
be large enough.

But this branch must then explain:
- why such a large hierarchy is selected;
- why the effective four-dimensional description remains controlled;
- how the same \(R_\psi\) and cutoff choice remain compatible with the GR,
  theta, and compactification sectors;
- how thresholds and running match ordinary QCD.

The hierarchy must not be fitted to \(g_s\).

## 6. Relation to the existing N_eff audit

This KK sum must not be replaced by the historical unqualified
\(N_{\rm eff}=12\).

The current repository distinguishes
\[
N_{\rm eff}^{\rm loop}=3
\]
in the direct scalar-loop audit from
\[
N_{\rm eff}^{\rm twist}=12
\]
in the separate twist route.  Neither count is equivalent to the complete KK
proper-time trace above.

For the coset-colour problem the correct quantity is the actual charged
spectral trace of the derived Hessian.

## 7. Next decision

The next action-level question is therefore:

\[
\boxed{
\text{What fixes } \Lambda R_\psi
\text{ in the same finalized UBT action?}
}
\]

The current torus/compactification audit already shows that a self-dual point
is not automatically a dynamical minimum.  Consequently a large
\(\Lambda R_\psi\) cannot be introduced merely to obtain the observed strong
coupling.

Verification:
\`verification/su3_psi_tower_coupling_check.py\`.
