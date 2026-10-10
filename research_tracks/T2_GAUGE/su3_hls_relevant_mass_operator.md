<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# The hidden-local vector mass is a relevant gauge-invariant operator

**Status:** exact operator-classification constraint for the Stiefel HLS route.

## 1. Gauge-covariant difference

The hidden-local variables transform as
\[
B_\mu
\to
h^{-1}B_\mu h-h^{-1}\partial_\mu h,
\]
and
\[
C_{\mu,0}
\to
h^{-1}C_{\mu,0}h+h^{-1}\partial_\mu h.
\]

Therefore
\[
\boxed{
V_\mu:=B_\mu-C_{\mu,0}
}
\]
transforms homogeneously:
\[
V_\mu\to h^{-1}V_\mu h.
\]

Hence
\[
\boxed{
\mathcal O_V
=
-\operatorname{tr}V_\mu V^\mu
}
\]
is exactly local-\(SU(3)\) gauge invariant.

## 2. Engineering dimension after the gauge field becomes dynamical

Once the 1PI action contains
\[
-\frac{Z_B}{4}
\operatorname{tr}F_{\mu\nu}F^{\mu\nu},
\]
the canonically normalized gauge field has four-dimensional mass dimension
\[
[B_\mu]=1.
\]

The frame current \(C_{\mu,0}\) contains one derivative and has the same
dimension in the nonlinear sigma description.

Therefore
\[
\boxed{
[\mathcal O_V]=2.
}
\]

Its coefficient
\[
c_V
\]
has
\[
\boxed{[c_V]=2.}
\]

Thus the HLS/Stueckelberg mass operator is a relevant operator.

## 3. Local SU(3) does not forbid it

For an ordinary fundamental Yang--Mills field, a bare Proca term
\[
\operatorname{tr}B_\mu B^\mu
\]
is not gauge invariant.

But the completed HLS term
\[
-\operatorname{tr}(B_\mu-C_{\mu,0})^2
\]
is gauge invariant.

Therefore
\[
\boxed{
\text{local }SU(3)\text{ redundancy alone does not protect }m_B=0
}
\]
in the Stiefel formulation.

This is why a generic fixed-frame HLS phase is vector-meson-like rather than
QCD-like.

## 4. Dimensionless critical variable

Define the running dimensionless mass parameter
\[
\boxed{
\widetilde m_B^2(k)
=
\frac{c_V(k)}
{Z_B(k)k^2}.
}
\]

A genuinely massless continuum/critical phase requires the renormalized
zero-momentum gauge mass to vanish.

In an FRG description this means the flow must lie on the critical surface
associated with the relevant HLS mass operator, rather than merely generating
\(Z_B>0\).

At minimum one needs
\[
c_V(k\to0)\to0
\]
sufficiently fast that the physical inverse propagator has no finite mass
intercept.

## 5. Naturalness consequence

Because \(\mathcal O_V\) is allowed by all currently stated HLS symmetries,
setting its renormalized coefficient to zero is not technically protected by
local colour gauge redundancy alone.

A viable UBT explanation therefore needs one of:

1. a quantum critical point/phase transition that dynamically selects the
   massless surface;
2. an additional exact symmetry or constraint forbidding \(\mathcal O_V\);
3. an infrared fixed structure making the operator irrelevant/nonphysical;
4. a different collective gauge mechanism without a Stueckelberg-completed
   relevant mass operator.

Absent such a mechanism, massless colour requires tuning.

## 6. Relation to known HLS vector manifestation

Hidden-local-symmetry literature contains critical symmetry-restoration phases
where a dynamical HLS vector becomes massless.

The lesson relevant to UBT is not that masslessness is automatic, but that a
nontrivial critical surface can in principle remove the allowed HLS mass while
retaining gauge dynamics.

UBT must derive its own finite noncompact critical surface.

## 7. FRG stage gate

A future flow calculation must track at least
\[
Z_B(k),
\qquad
c_V(k),
\qquad
c_3(k),
\qquad
c_1(k),
\]
and classify trajectories by
\[
\widetilde m_B^2(k)
=
c_V/(Z_Bk^2).
\]

A claimed QCD-like phase is rejected if the \(k\to0\) 1PI transverse inverse
propagator retains a nonzero mass intercept.

Verification:
\`verification/su3_hls_relevant_mass_operator_check.py\`.
