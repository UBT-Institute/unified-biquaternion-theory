<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working research proposal, not a proof of a physical UBT prediction.
UBT-AI-PROVENANCE-END
-->

# Dodecahedral sector: conditional action, Hamiltonian, and CMB covariance

**Status (2026-10-20): DERIVED_WITH_ASSUMPTIONS / BLOCKED_OBSERVATIONAL_FIT.** Research only; not canonical UBT.
**Scope:** A mathematically controlled *test-field* model on a specified background, not the closed fundamental action of UBT.
**No observational detection is claimed.** This track implements an exact quotient spectrum and a synthetic Sachs–Wolfe toy covariance, but it does not claim a real Planck fit. The exact full-sky harmonic projection `xi_{nj,lm}` and any observational likelihood remain blocked.

**Explicit gate:** `NO OBSERVATIONAL FIT` — real TT/TE/EE data, masks, transfer functions, covariance and likelihood handling are not implemented in this research track.

## 0. Existing UBT and assumptions

The canonical UBT field is \(\Theta(q,\tau)\in\mathbb B=\mathbb H\otimes_{\mathbb R}\mathbb C\), with \(\tau=t+i\psi\) and four complex/eight real components; see \`canonical/fields/theta_field.tex\`. Its covariant derivative is a two-sided candidate
\[
D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu,
\quad
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta.
\]
The central tetrad anticommutator defines the *composite* canonical metric. Derivation of a full common action and a globally consistent curved solution is explicitly open in the mainline.

For the following **conditional toy sector** assume:
(A1) a prescribed FLRW-like Lorentz metric \(ds^2=-dt^2+a(t)^2R_c^2d\Omega_{\Sigma}^2\), where \(\Sigma=S^3/\Gamma\), \(\Gamma=2I\) acts freely by left multiplication and \(|\Gamma|=120\);
(A2) a normalized physical perturbation component \(\delta\Theta=\varphi Q\), \(\langle Q,Q\rangle=1\), whose linear kinetic operator reduces to a minimally coupled real Klein–Gordon scalar with effective mass \(m_{\rm eff}^2\ge0\);
(A3) trivial scalar holonomy under \(\Gamma\), so \(\varphi(gx)=\varphi(x)\);
(A4) \(R_c\), \(a(t)\), perturbation normalization, \(\Gamma\) and \(m_{\rm eff}\) are **inputs**, not predicted by UBT.

Here the positive Hermitian inner product on the biquaternion representation is \(h(X,Y)=\frac12\operatorname{Tr}[\rho(X)^\dagger\rho(Y)]\). This is for perturbation kinetic energy, **not** the canonical Lorentzian metric definition. If the perturbation is not gauge-invariant or is coupled to other channels, (A2) must be replaced by a genuinely covariant fluctuation operator.

## 1. A rigorous 24-real-dimensional *candidate bundle*, not 24 physical modes

On an oriented Lorentzian 4-manifold, Hodge star satisfies \(\star^2=-1\) on real 2-forms. The complex \(+i\) eigenspace has complex rank 3. Therefore
\[
W=\Lambda^2_+(T^*M\otimes\mathbb C)\otimes_\mathbb C\mathbb B
\quad\Rightarrow\quad
\dim_\mathbb C W=3\cdot4=12,\qquad \dim_\mathbb R W=24.
\]
This is a **rank identity**, not a new coordinate space or proof of 24 propagating degrees of freedom. Self-dual forms are complex; reality, constraints, gauge quotient and field dynamics can reduce the physical dimension. There is no natural identification between this characteristic-zero vector bundle, the finite field \(\mathrm{GF}(2^{24})\), the \(E_8^3\) lattice, or the Leech lattice.

**Important failed naive realization:** in the branch with \(F^A_{\mu\nu}=\Theta F^B_{\mu\nu}\Theta^{-1}\),
\[
[D_\mu,D_\nu]\Theta=F^A_{\mu\nu}\Theta-\Theta F^B_{\mu\nu}=0.
\]
Therefore the commutator acting *on \(\Theta\)* cannot furnish a nonzero field in \(W\) in that branch. Other curvature fields or non-integrable branches require independent specification.

## 2. Quotient spectrum from Klein invariants (standard mathematics)

Scalar eigenmodes on the unit round three-sphere obey \(-\Delta Y_{nj}=n(n+2)Y_{nj}\). Only left-\(2I\)-invariant modes descend to \(\Sigma\). The invariant polynomial Hilbert/Molien series is
\[
M(t)=\sum_{n\ge0} a_nt^n
=\frac{1-t^{60}}{(1-t^{12})(1-t^{20})(1-t^{30})}
=\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
\]
Peter–Weyl decomposition gives the scalar degeneracy
\[
d_n=(n+1)a_n.
\]
Selected \(n:\lambda_n:d_n\) are \(0:0:1\), \(12:168:13\), \(20:440:21\),
\(24:624:25\), \(30:960:31\), \(32:1088:33\), \(36:1368:37\),
\(60:3720:122\). No nonconstant scalar modes occur for \(1\le n<12\).
All odd degrees are forbidden because \(-1\in2I\). These are established spectral properties of the quotient, **not** derived from UBT. The first allowed degree is 12 (not degree 5); degrees 20 and 30 mean "everything is a multiple of 12 or 24" is false.

See: Kraemer, *The Laplacian Spectrum of the Poincaré Homology Sphere* (2026),
https://rxiverse.org/pdf/2604.0091v1.pdf ; Klein invariant theory.
The reproducible small-integer coefficient calculator is \`spectral_dodecahedron.py\`.

## 3. The effective action, Legendre transform, and Hamilton equations

Let \(h_{ij}=R_c^2\gamma_{ij}\) on \(\Sigma\), and choose **real**, volume-orthonormal quotient harmonics \(\int_\Sigma d{\rm vol}_h\,Y_{nj}Y_{mk}=\delta_{nm}\delta_{jk}\).
Define \(\varphi(t,x)=\sum_{nj}u_{nj}(t)Y_{nj}(x)\). Under A1--A4,
\[
S_{\rm test}=\frac12\int dt\,d{\rm vol}_h\,a^3
\left[(\partial_t\varphi)^2-a^{-2}|\nabla_h\varphi|^2-m_{\rm eff}^2\varphi^2\right]
=\frac12\int dt\sum_{nj}a^3\left[\dot u_{nj}^2-\omega_n^2u_{nj}^2\right],
\]
\[
\omega_n^2(t)=\frac{n(n+2)}{a(t)^2R_c^2}+m_{\rm eff}^2.
\]
The exact canonical momentum and **time-dependent** test Hamiltonian are
\[
p_{nj}=a^3\dot u_{nj},\qquad
H_{\rm test}(t)=\frac12\sum_{nj}\left(\frac{p_{nj}^2}{a^3}+a^3\omega_n^2u_{nj}^2\right).
\]
Hamilton's equations \(\dot u=p/a^3\), \(\dot p=-a^3\omega_n^2u\) give
\[
\ddot u_{nj}+3(\dot a/a)\dot u_{nj}+\omega_n^2u_{nj}=0.
\]
Even with \(m_{\rm eff}\) constant, \(H_{\rm test}\) is **not conserved** in an expanding background. This is not the ADM Hamiltonian constraint of dynamical gravity; neither the Friedmann equation nor the canonical composite-metric backreaction has been derived. For a nonminimal field coupling \(\xi R\varphi^2\) the replacement \(m_{\rm eff}^2\to m_{\rm eff}^2+\xi \mathcal R\) is needed.

The quotient has a spatial eigenvalue gap from the zero mode to 168/R_c^2. The positive-mode ratio \(k_{24}/k_{12}=\sqrt{624/168}=\sqrt{26/7}\simeq1.92725\) follows *conditionally*.

## 4. Candidate global topology-selection functional (not a selection proof)

A strictly local classical field equation cannot distinguish locally isometric patches of \(S^3\) and its quotient or by itself choose global deck group \(2I\). In particular, a single invertible biquaternion \(\Theta\) cannot have nontrivial left-multiplication stabilizer: \(g\Theta=\Theta\Rightarrow g=1\).

A concrete *nonlocal/spectral* discriminator may arise at one loop. Define the 3D scalar heat traces (unit-radius eigenvalues; dimensionless \(s\))
\[
K_\Gamma(s)=\sum_{n\ge0}d_ne^{-s n(n+2)},\quad
K_{S^3}(s)=\sum_{n\ge0}(n+1)^2e^{-s n(n+2)},\quad
\Delta K(s)=K_\Gamma(s)-K_{S^3}(s)/120.
\]
At small \(s\), local heat-kernel coefficients cancel (same local constant-curvature geometry, quotient volume \(1/120\)), making this difference UV-finite. For a **massive** Euclidean scalar toy determinant define
\[
\Delta\Gamma_{\rm 1loop}(\mu)
=-\frac12\int_0^\infty\frac{ds}{s}e^{-\mu^2s}\Delta K(s),\qquad\mu>0.
\]
This is a finite *relative 3D determinant under fixed curvature-radius comparison*; it is **not** the full four-dimensional gravitating effective action, and cannot be used alone to say that the Universe favors \(2I\). The classical gravity action, matching physical volume, allowed topological competitors, matter content, measure, counterterms and cosmological dynamics all remain to be specified. A purely local classical \(\Theta\)-action does **not** automatically generate this topological selection.

To avoid confusing the spatially constant mode with a CMB anisotropy, define the explicitly NON-CMB scalar gap diagnostic
\[
D(s)=\frac{K_\Gamma(s)-1}{K_{S^3}(s)/120-1/120},\quad s>0.
\]
This probes long-wavelength nonconstant eigenmodes. It is only a numerical spectral proxy; it must NEVER be relabeled \(C_\ell\) or a measured CMB fit.

## 5. Actual conditional CMB prediction: full-sky covariance

If the scalar curvature perturbation \(\zeta\) obeys the *same scalar invariant harmonic spectrum* and has a specified primordial modal covariance
\(\langle \zeta_{nj}\zeta^*_{n'j'}\rangle=P_n\delta_{nn'}\delta_{jj'}\),
then in the **instantaneous, ordinary Sachs–Wolfe-only** limit,
\[
\frac{\Delta T(\hat{\mathbf n})}{T}
=\frac15\sum_{nj}\zeta_{nj}Y_{nj}(x_\ast(\hat{\mathbf n})),
\]
\[
\xi_{nj,\ell m}(x_o,\mathcal O,\chi_\ast)
=\int_{S^2}d\hat{\mathbf n}\,Y_{nj}(x_\ast(\hat{\mathbf n}))Y_{\ell m}^*(\hat{\mathbf n}),
\]
\[
\boxed{
\langle a_{\ell m}a^*_{\ell'm'}\rangle=
\frac1{25}\sum_{n\ {\rm allowed}}P_n\sum_{j=1}^{d_n}
\xi_{nj,\ell m}\xi^*_{nj,\ell'm'}.
}
\]
Here \(x_o,\mathcal O,\chi_\ast\) respectively denote observer position, orientation and the dimensionless radius to the last-scattering surface. This covariance, not simply a table of \(n\)-values, is the actual model observable. The quotient can produce off-diagonal \((\ell m,\ell'm')\) correlations, topology-dependent large-angle suppression and potentially matched circles (if the last-scattering surface intersects an identified copy). It **does not** imply \(C_\ell=0\) for \(\ell<12\).

This formula is a conditional model prediction, not yet a quantitative UBT-vs-Planck prediction: \(P_n\), transfer functions, geometry, curvature radius, observer/orientation and physical field-to-\(\zeta\) bridge must be fixed. A production prediction requires a curved-universe Boltzmann solver, SW+Doppler+ISW+lensing+reionization, polarization \(E\), realistic masks/noise, and covariance-based likelihood, compared to \(\Lambda\)CDM and simulated null skies.

## 6. Existing observational constraints, not cherry-picked anomalies

Luminet et al. (2003) originally proposed the Poincaré dodecahedral model in response to WMAP wide-angle anomalies (Nature, https://www.nature.com/articles/nature01944). Planck 2013/2015 topology analyses **did not detect** a multiconnected topology on the tested scales. The 2013 model-dependent likelihood lower bound for a dodecahedral example was of order \(R_i\gtrsim 1.03\,\chi_{\rm rec}\) in the specified family; this is **not** a universal curvature-radius bound. The 2015 flat-torus matched-circle constraint must not be misquoted as a direct dodecahedral bound.
Sources: https://doi.org/10.1051/0004-6361/201321546 and https://doi.org/10.1051/0004-6361/201525829 .

## 7. Test and decision gates

- [x] Defined a **conditional** test-field action and correct time-dependent Hamiltonian.
- [x] Derived Euler--Lagrange/Hamilton equivalence.
- [x] Computed exact low-lying quotient scalar spectrum from the invariant Hilbert series.
- [x] Defined a scalar heat-kernel topological discriminator and a **non-CMB** numeric proxy.
- [x] Specified the formal SW-only full CMB covariance with required priors and orientation.
- [ ] Derive \(\Gamma=2I\) (or selection against alternatives) from a fundamental UBT action, rather than imposing topology.
- [ ] Resolve the single-\(\Theta\) commutator obstruction or derive a physical nonvanishing 24-component sector.
- [ ] Derive or justify \(\zeta[\Theta]\), \(P_n\), \(\omega_n\), physical reality/gauge constraints and metric backreaction.
- [ ] Compute actual \(C_\ell\), off-diagonal covariances, \(TE/EE\) and matched-circle templates with a curved Boltzmann solver.
- [ ] Pre-register null tests, alternative topologies, orientations, parameter priors, look-elsewhere correction and compare against published Planck exclusions.

**Scientific interpretation:** The known topological spectrum is genuinely exact; the action/Hamiltonian and CMB covariance are conditional mathematical derivations, *not* an independent proof of UBT, a new detection, or an observed reason to prefer the exponent 24. The established three-layer information-probe architecture remains unchanged, and RS/Golay/\(GF(2^m)\) codes are separate research hypotheses.
