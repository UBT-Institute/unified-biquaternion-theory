<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional toy computation, not a detection.
UBT-AI-PROVENANCE-END -->
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


# A directly computable 2I-projected CMB covariance kernel

**Status:** exact mathematical spectral projection; Sachs--Wolfe-only toy CMB covariance **under assumptions**. See DERIVATION.md §5. This goes beyond merely listing multiplicities; it still does not calculate an observational \(C_\ell\). **Gate:** `NO OBSERVATIONAL FIT` — the exact full-sky \(\xi_{nj,\ell m}\) projection and a real Planck likelihood remain blocked.

Let \(S^3\subset\mathbb R^4=\mathbb H\) have unit curvature radius, and let the 120-element binary icosahedral group \(2I\subset S^3\) act by left quaternion multiplication. The addition theorem for unit-\(S^3\) scalar harmonics of degree \(n\) is
\[
K_n^{S^3}(x,y)=\sum_{a=1}^{(n+1)^2}Y_{na}(x)Y_{na}(y)
=\frac{n+1}{2\pi^2}U_n(\langle x,y\rangle),
\]
where \(U_n=C_n^{(1)}\) is Chebyshev of the second kind (Gegenbauer index 1). Quotient harmonics lifted back to \(S^3\) have norm smaller by \(\sqrt{120}\); using the invariant projector \((1/120)\sum_{g\in2I}g\) gives the **exact quotient addition kernel**
\[
\boxed{
K_n^{S^3/2I}(x,y)
=\frac{n+1}{2\pi^2}\sum_{g\in2I}U_n(\langle g x,y\rangle).
}
\]
It is symmetric, invariant under deck transforms, and positive semidefinite as a kernel. The mode multiplicity follows independently by setting \(x=y\) (quotient is homogeneous):
\[
K_n^{S^3/2I}(x,x)=\frac{120\,d_n}{2\pi^2},\qquad d_n=(n+1)a_n.
\]
This provides a THIRD independent computational cross-check of the Molien- and character-derived counts. The group is realized explicitly as the 120 600-cell vertices: 8 axial unit quaternions, 16 sign combinations of \((1/2,1/2,1/2,1/2)\), 96 even permutations and independent sign assignments of \((0,1/2,\varphi/2,1/(2\varphi))\).

With an observer at the identity, choose a last-scattering surface of *dimensionless comoving radius* \(\chi_\ast\) and a sky direction \(\hat n\):
\[
x_\ast(\hat n)=(\cos\chi_\ast,\sin\chi_\ast\,\hat n)\in S^3.
\]
For an **assumed** scalar primordial covariance \(\langle\zeta_{nj}\zeta^*_{mk}\rangle=P_n\delta_{nm}\delta_{jk}\), ordinary Sachs--Wolfe transfer \(\Delta T/T=\zeta/5\) gives directly
\[
\boxed{
\mathcal C_{\rm SW}(\hat n,\hat m)
=\frac1{25}\sum_{n>0}P_n\,K_n^{S^3/2I}
(x_\ast(\hat n),x_\ast(\hat m)).
}
\]
This is an explicit, implementable **full-sky real-space covariance** for any chosen nonnegative \(P_n\), cut-off and \(\chi_\ast\). \(n=0\) is excluded as a non-anisotropic monopole. It requires no individual quotient eigenbasis.

Crucial caveats: all sky maps produced with arbitrary \(P_n\), \(\chi_\ast\) and finite cut-off are *synthetic*. The scalar curvature perturbation \(\zeta\) has **not** been derived from the UBT field \(\Theta\); no SW+Doppler+ISW / polarization transfer, likelihood, Planck comparison or topology selection is supplied. Angular multipoles \(\ell\) are not the spatial harmonic degrees \(n\). This calculation by itself does not establish evidence for a dodecahedral universe.

**Next computational milestones:** sample pixel-pair covariance and its eigensystem; perform spherical-harmonic transform to \(\langle a_{\ell m}a^*_{\ell'm'}\rangle\); add full curved Boltzmann transfer functions and polarization; orientation and radius marginalization; Planck-like mask/noise and null simulations; independent prior-free comparison with \(\Lambda\)CDM and alternative topologies. Only then evaluate physical CMB residuals.

Run \`python -m unittest discover -s research_tracks/dodecahedral_action_cmb -p 'test_*.py'\`.
