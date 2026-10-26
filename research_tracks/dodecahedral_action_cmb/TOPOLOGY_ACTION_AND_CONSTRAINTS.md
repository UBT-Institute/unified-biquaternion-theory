<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# Dodecahedral topology: matched circles, local-action limitation, and observational gate

**Status 2026-10-20:** DERIVED_WITH_ASSUMPTIONS for topology geometry; OPEN_GAP for any UBT topological-selection mechanism. Builds on DERIVATION.md and CMB_KERNEL.md. The UBT three-layer architecture is unchanged.

## 1. Quaternionic proof of the six nearest circle pairs

Take the unit-quaternion round 3-sphere \(S^3\), and the 120-element binary icosahedral subgroup \(2I\). It acts freely by left multiplication, defining the Poincaré quotient \(S^3/2I\). The 120 group elements can be represented as the 120 vertices of the regular 600-cell:
- 8 vectors with a single coordinate \(+1\) or \(-1\);
- 16 vectors \((\pm1/2,\pm1/2,\pm1/2,\pm1/2)\);
- 96 vectors from the even permutations and independent signs on the three nonzero coordinates of \((0,1/2,\phi/2,1/(2\phi))\), where \(\phi=(1+\sqrt5)/2\).

For \(g=(\cos d,\sin d\,u)\), the spherical distance \(d(x,gx)=\arccos\Re g=d\) is independent of \(x\). The shortest nontrivial \(g\) have \(\Re g=\cos(\pi/5)=\phi/2\), giving precisely twelve shortest elements. They form six inverse pairs \((g,g^{-1})\). Consequently
\[
d_{\min}=\pi/5,\qquad r_{\rm inj}=\pi/10.
\]

Place an observer at \(1\in S^3\). The last-scattering sphere at dimensionless comoving radius \(\chi\in(0,\pi/2)\) consists of
\[
x(n)=(\cos\chi,\sin\chi\,n),\quad n\in S^2.
\]
A point belongs also to the image sphere centered at \(g\) iff
\[
\cos\chi=\langle x(n),g\rangle
=\cos\chi\cos d+\sin\chi\sin d(n\cdot u).
\]
Therefore
\[
n\cdot u=\cot\chi\tan(d/2)=\cos\alpha,\quad
\boxed{\alpha=\arccos[\tan(d/2)/\tan\chi]}.
\]
For \(d_{\min}=\pi/5\), the six pairs first appear **only when** \(\chi>\pi/10\). The two sky-circle centers are antipodal, \(u,-u\). Map corresponding sky points by \(x'=g^{-1}x\); the transverse tangent components are rotated by **\(-d=-36^\circ\)** in a fixed common right-handed tangent frame, with the usual reversal of centers. This proves the ideal geometric phase/twist, not an actual observed temperature match. Extra pairs for larger \(\chi\) and more distant deck elements are not analyzed here.

Exact numerical examples (all conditional):
| \(\chi\) (rad) | first-pair \(\alpha\) |
|---|---|
| 0.30 | none |
| 0.35 | 27.11149 degrees |
| 0.40 | 39.77996 degrees |
| 0.50 | 53.50437 degrees |
| 0.60 | 61.64496 degrees |

## 2. A significant observational constraint

For a curved FLRW model with present curvature radius \(R_c\) and comoving radial distance to the last-scattering surface \(D_*\), \(\chi_*=D_*/R_c\). Existence of nearest matched circles requires
\[
\boxed{R_c < 10 D_*/\pi.}
\]
Taking an **illustrative** \(D_*=13.87\) Gpc gives \(R_c<44.15\) Gpc. By contrast, Planck 2018 + BAO quotes a 95% lower limit of \(R_c>81\) Gpc for a closed model under the tested cosmological assumptions. Thus the regime with the **six shortest matched circles is incompatible with that parameter constraint**; do not claim a detection.

A rough (not direct dodecahedral-specific) Planck 2015 antipodal matched-circle search could detect radii at least about 15 degrees under its mask/noise assumptions. The geometric threshold for such a radius is
\[
\chi\ge\arctan[\tan(\pi/10)/\cos(15^\circ)]
\simeq0.32449.
\]
This is **not** an independently calibrated Planck exclusion for this model. Its geometry and observational selection must be checked using the full transfer, signal-to-noise and masks.

References:
- Planck 2018 X, curvature radius with lensing+BAO: https://doi.org/10.1051/0004-6361/201833887
- Planck 2013 XXVI, *specific dodecahedral* topology-likelihood constraint: https://doi.org/10.1051/0004-6361/201321546
- Planck 2015 XVIII, matched-circle and polarization methodology: https://doi.org/10.1051/0004-6361/201525829
- Planck best-fit approximate comoving LSS distance: D_* about 13.87 Gpc (independently reproducing Planck-parameter integration): https://web.mit.edu/8.286/www/quiz22/q3sols-euf22.pdf

## 3. What a local UBT action can and cannot select

**Structural proposition.** Let \(L\) be a diffeomorphism-covariant *local* scalar density (curvature, covariant jets of globally compatible fields), and suppose a \(\Gamma\)-invariant field configuration on \(S^3\) descends smoothly to \(S^3/\Gamma\). At the same local geometry and curvature radius,
\[
S_{\rm local}[S^3/\Gamma]
=\frac1{|\Gamma|} S_{\rm local}[S^3].
\]
**Proof:** the quotient map is an \(|\Gamma|\)-sheeted local isometry; the pull-back of the density is invariant, and the integral over the covering space is \(|\Gamma|\) times the quotient integral. End proof.

This is an exact covering-space identity **under the stated lift/invariance assumptions**, not a universal proof that classical gravity cannot prefer any topology. One cannot compare actions at equal curvature radius and mistake the simple volume factor for a preference; fixed physical volume, constraints, allowed competitors, time evolution, the matter spectrum and the path-integral measure all matter. Local field equations alone cannot identify the global quotient group from a single local patch. Moreover, for invertible \(\Theta\), \(g\Theta=\Theta\) with pure left multiplication implies \(g=1\); therefore a simple one-field stabilizer does not select \(2I\).

**A concrete nonlocal alternative (one-loop test determinant, not fundamental UBT action):** let \(L=-\Delta_{S^3}+\mu^2\) for a *positive-mass* Euclidean test scalar, \(\mu>0\). Write
\[
K_\Gamma(s)=\sum_n d_ne^{-s\lambda_n},\quad
K_{S^3}(s)=\sum_n(n+1)^2e^{-s\lambda_n},
\]
\[
\Delta K(s)=K_\Gamma(s)-K_{S^3}(s)/120
=\frac1{120}\sum_{g\ne1}\int_{S^3}
H_{S^3}(s;x,gx)\,dx.
\]
For \(s>0\), the scalar heat kernel \(H_{S^3}>0\), hence \(\boxed{\Delta K(s)>0}\). For small \(s\), the nonzero minimum deck distance gives exponential off-diagonal suppression, so the relative integral has no UV local divergences. For \(\mu>0\), the IR integral also converges. The relative Euclidean scalar one-loop determinant satisfies
\[
\boxed{
\Delta\Gamma_{\rm 1loop}(\mu)
=-\tfrac12\int_0^\infty \frac{ds}{s}e^{-\mu^2s}\Delta K(s)<0
}
\]
using the standard proper-time convention for \(+\frac12\log\det L\).
This is an **exact conditional sign result** for the 3D *relative determinant normalized by covering volume*, NOT a result that the universe favors \(2I\). Removing zero modes, matching full cosmological volume, introducing fermionic or gauge fields, dynamics/ghost constraints, four-dimensional fluctuations, or varying the curvature can alter the physical comparison. Never use this determinant alone as a topology-selection theorem.

## 4. Fundamental action/Hamiltonian: where the actual gap is

The previously derived effective scalar action and time-dependent oscillator Hamiltonian in DERIVATION.md are valid under (A1--A4), but **do not determine \(\Gamma\), \(R_c\), the primordial spectrum, or \(\Theta\to\zeta\)**. In canonical UBT the geometry is composite:
\[
E_\mu=D_\mu\Theta/\sqrt{\mathcal N_0},\qquad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}{\bf1}.
\]
The two-sided derivative and on-shell integrability restrict the possible kinetic and curvature couplings, and \([D_\mu,D_\nu]\Theta=0\) in the stated branch. A proposed fundamental action must satisfy:
1. Gauge/Lorentz covariance and the tetrad identity without treating \(g,\Theta,E\) as unrelated propagating fields;
2. a well-defined real variational principle, constraints, and bounded physical energy or justified noncompact sector;
3. a consistent curved solution and FRW/GR infrared limit with correct gravitational Hamiltonian constraints;
4. an independent mechanism for choosing or suppressing \(\Gamma=2I\) rather than inserting it as boundary data;
5. a computation of the gauge-invariant scalar/tensor power spectra and cosmological transfer functions with **predeclared** parameters.
Until these are obtained, no observational signal of this branch can be claimed as new UBT physics.

## 5. Reproducibility

Run:
\`python -m unittest discover -v -s research_tracks/dodecahedral_action_cmb -p 'test_*.py'\`

New code: \`matched_circles.py\`, \`test_matched_circles.py\`; these use the 120 unit quaternions in \`cmb_sachs_wolfe_kernel.py\` from merged PR #670. They are geometry and algebra tests only. Include positive/negative circles controls before any Planck analysis.


## 6. Formal angular projection of CMB toy covariance

Given the SW-only real-space kernel \(\mathcal C_{\mathrm{SW}}(\hat n,\hat m)\) from CMB_KERNEL.md and a **real** orthonormal spherical harmonic basis \(Y_{\ell m}^{(R)}\), the full angular mode covariance is
\[
\boxed{
C_{(\ell m),(\ell'm')}
=\int_{S^2}\!\!d\Omega_{\hat n}\int_{S^2}\!\!d\Omega_{\hat m}\,
Y_{\ell m}^{(R)}(\hat n)\,
\mathcal C_{\mathrm{SW}}(\hat n,\hat m)\,
Y_{\ell'm'}^{(R)}(\hat m).
}
\]
This is a real symmetric positive semidefinite matrix for nonnegative primordial modal powers \(P_n\), even when off-diagonal entries are nonzero. The familiar trace-average power is
\[
C_\ell^{\rm toy}=(2\ell+1)^{-1}\sum_{m=-\ell}^{\ell}
C_{(\ell m),(\ell m)}.
\]
The code \`low_l_covariance.py\` evaluates these integrals by Gauss–Legendre \(\cos\theta\)-quadrature and uniform \(\phi\)-quadrature, using a normalized real harmonic basis. The \`test_low_l_covariance.py\` suite checks orthonormality, covariance symmetry and nonnegative quadratic forms. **Quadrature convergence for each (\(\ell_{\max},n_{\max}\)) must be established before reporting any final numerical values.**

The outputs are **synthetic**, with freely specified \(\chi_\ast\) and \(P_n\); they are not physical UBT predictions for Planck or observed \(\Lambda\)CDM residuals. A physical test requires a derived gauge-invariant \(\zeta[\Theta]\), its primordial power, transfer functions, masks/noise and a predeclared likelihood. The magnitude of the \(\ell\ge2\) signal must also be checked in the curvature regime \(\chi_\ast\ll \pi/10\) actually permitted by Planck+BAO.
