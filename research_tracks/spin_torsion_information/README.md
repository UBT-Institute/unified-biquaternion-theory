# Spin, composite torsion and information in canonical UBT

**Status:** research hypothesis / conditional derivation, not canonical closure.  
**Scope:** canonical covariant-tetrad metric and the existing paired-connection/contortion branch.  
**Date:** 2026-11-10

## 1. Compatibility with the existing metric theorem

Let \(\mathbb B=\mathbb C\otimes\mathbb H\) and \(E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\). On the canonical real Lorentz slice,

\[
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf1,
\qquad
\Sigma_{\mu\nu}=\tfrac12(E_\mu^\sharp E_\nu-E_\nu^\sharp E_\mu).
\]

Hence \(E_\mu^\sharp E_\nu=g_{\mu\nu}\mathbf1+\Sigma_{\mu\nu}\).
The algebraic bivector companion is **not** spacetime torsion, a spin current, or connection curvature. For each fixed pair of coordinate directions (no summation),

\[
\Sigma_{\mu\nu}^2=(g_{\mu\nu}^2-g_{\mu\mu}g_{\nu\nu})\mathbf1.
\]

This follows from the quadratic identity for the quaternionic product and supplies an exact local diagnostic. No independent propagating bivector modes follow from it.

## 2. Intrinsic quantum spin is not classical rotation

Spin labels representations of the (cover of the) local Lorentz group. A classical macroscopic angular velocity, Kerr angular momentum, and a local intrinsic-spin current are distinct objects. Neither frame dragging nor rotating coordinates alone forces torsion. In standard torsion-free GR, Kerr spacetime has zero torsion. In Einstein–Cartan theory, intrinsic spin is an algebraic source of torsion.

Use a tetrad \(e^a\), metric-compatible spin connection \(\omega^{ab}=-\omega^{ba}\), and contortion \(K^{ab}\):

\[
\omega^{ab}=\mathring\omega^{ab}(e)+K^{ab},\qquad
T^a=de^a+\omega^a{}_b\wedge e^b=K^a{}_b\wedge e^b,
\]
\[
R^{ab}(\omega)=R^{ab}(\mathring\omega)+\mathring D K^{ab}+K^a{}_c\wedge K^{cb}.
\]

The exact metric-compatible decomposition is standard geometry, not a derivation of nonzero torsion from UBT.

## 3. Conditional spin–torsion field equation

For a first-order benchmark, consider a specifically chosen Einstein–Cartan-type action

\[
S_{\mathrm{bench}}[e,\omega,\Psi]
=\frac{1}{4\kappa}\int\epsilon_{abcd}\,e^a\wedge e^b\wedge R^{cd}(\omega)
+S_m[e,\omega,\Psi].
\]

Define the spin three-form by \(\delta_\omega S_m=\tfrac12\int\delta\omega^{ab}\wedge\tau_{ab}\) (the coefficient and signs are convention-dependent). Variation in \(\omega\) gives an algebraic equation linking \(\epsilon_{abcd}T^a\wedge e^b\) to \(\tau_{cd}\), up to the specified normalization/sign convention. When the algebraic linear map is invertible, \(K\) is fixed by the spin current. Substitution then generates effective spin-contact interactions. This is a **benchmark conditional on the chosen action**; it is not yet the UBT canonical action.

A UBT-specific spin source must be obtained as the functional derivative of a concrete \(\Theta\)/matter action with respect to the actual paired spin connection:

\[
\tau^{\mathrm{UBT}}_{ab}:=2\frac{\delta S_{\mathrm{UBT,matter}}}{\delta\omega^{ab}}.
\]

An algebraic \(\Sigma_{\mu\nu}\) by itself cannot be identified with \(\tau^{\mathrm{UBT}}_{ab}\).

## 4. The existing canonical obstacle and possible escape

The canonical compatible one-connection pair takes the form

\[
D_\mu X=\partial_\mu X+\Omega_\mu X+X\Omega_\mu^\ddagger.
\]

For the pure torsion-free generated tetrad, the existing GAP-10I concurrent-vector theorem implies \(\nabla_\mu V^\nu=\delta_\mu{}^\nu\), and excludes generic Einstein geometries including the nonflat Schwarzschild exterior in that branch. The existing **composite-contortion local representer** permits local tetrad kinematics with torsion, but does not dynamically select \(K\) or establish that intrinsic spin sources it. Do not infer that Kerr geometry itself requires torsion.

## 5. Information and quantum fluctuations: gated proposal

A gauge-invariant geometric-information measure must account for diffeomorphism and local Lorentz redundancy. An initial **regulated** correlation observable may be built from smeared curvature or holonomies, with parallel transport to compare distinct spacetime points:

\[
\mathcal C(C_1,C_2)=
\langle\delta\operatorname{tr}U(C_1)\,
\delta\operatorname{tr}U(C_2)\rangle
\]

for closed loops and a specified physical state. A separate, appropriately transported and smeared torsion-correlator may be investigated after the state, measure, and connection dynamics exist. Such correlators do not, by themselves, prove spacetime discretization or a simulation hypothesis.

The quantum closure remains open: physical phase space/constraints; gauge fixing; positive state space; measure or commutators; propagator/correlation functions; and recovery of GR/known spin-coupling limits. Do not equate component counts (20 Riemann components in 4D; 825 in 10D) with quantum noise channels or propagating degrees of freedom.

## 6. Falsifiable staged tests

1. **Algebra:** verify the central metric, bivector companion and \(\Sigma^2\) identity for generic nondegenerate Lorentz tetrads. Check covariance under local Lorentz frame changes.
2. **Connection:** implement \(\omega=\mathring\omega+K\) with the *same* existing UBT paired-connection convention and verify both Cartan structure equations, curvature decomposition and the tetrad postulate.
3. **Dynamics:** supply a concrete UBT action and compute \(\delta S/\delta\omega\), not a postulated spin source. Determine whether its spin current is nonzero, whether \(K\) is auxiliary or propagating, and whether the full constrained Hessian is ghost-free.
4. **GR limit:** test Schwarzschild/Kerr tetrad representatives and whether on-shell equations select them; off-shell representation alone is insufficient.
5. **Quantum:** only after the physical modes are identified, derive the state and regularized spin/torsion/holonomy correlators and compare to torsion-free GR and Einstein–Cartan benchmarks.

### Gate and claim status

- **[L0 / known identity]:** metric/bivector decomposition and quadratic bivector identity on the Lorentz slice.
- **[STD]:** Cartan torsion/curvature definitions, contortion decomposition, and conditional Einstein–Cartan spin–torsion coupling.
- **[L1 per canonical repo]:** rank-ten metric map and existing GAP-10I paired-connection and local contortion results (as documented in canonical sources).
- **[OPEN]:** unique UBT action, UBT-derived spin current, on-shell nonzero torsion, Hamiltonian/quantum closure, observational predictions.
- **[SPECULATIVE]:** informational microstructure or simulation interpretation. Neither follows from nonzero torsion.

## Existing canonical references

- `canonical/gr_closure/covariant_tetrad_rank_theorem.tex`
- `canonical/gr_closure/gap_10i_paired_connection_audit.tex`
- `canonical/gr_closure/gap_10i_torsionful_local_representer.tex`
- `docs/QUANTUM_ROADMAP.md`
- `docs/quantum_sector_status.md`

This document proposes an audit-ready research direction without overriding the canonical claim status.
