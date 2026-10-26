# Algebraic and Bianchi identities do not fix transverse contortion

**2026-10-26. Explicit local counterexample, conditional on canonical Gaussian vector reconstruction.** For nonnull V, metric-compatible contortion has 12-dimensional transverse kernel C_(nu mu rho)=-C_(rho mu nu), C_(nu mu rho)V^rho=0.

Take Minkowski space with constant V=e0 and baseline flat metric connection, then choose a so(1,3)-valued one-form C=f(t) J_12 dx^1 (where J_12 is a purely spatial rotation). The connection matrix C_1 is skew with nonzero (1,2),(2,1) entries and C_mu V=0. The covariant derivative DV remains identical, as does any tetrad reconstructed purely from DV. But the curvature two-form changes by dC+C wedge C; as there is only one 1-form component, C wedge C=0, and F_01=f'(t) J_12. Thus the same DV may correspond to distinct curvature. Both connections satisfy metric compatibility and the Cartan/Bianchi identities by construction.

**Scope:** This example demonstrates underdetermination of a connection by metric compatibility, DV and Bianchi identities alone. It does NOT claim the constant-V example gives a nondegenerate UBT tetrad; the algebraic transverse ambiguity exists equally at any non-null point on the separate nondegenerate Gaussian construction. Nor does it assert that an extra physical field equation could never select a unique C.

Imposing vanishing torsion would select the Levi-Civita connection for a metric-compatible affine connection, but cannot be adopted silently: the locked nontrivial Gaussian realization requires a specific nonzero contortion projection W, and torsion-free compatibility with it must be checked. Bianchi identities are identities, not field equations. Consequently a uniquely defined curvature-dependent Hamiltonian requires an independently selected variational connection prescription or an existing equation of motion fixing/eliminating C. Setting C=0 is merely choosing a representative.

## Exact verification
A 4x4 antisymmetric spatial generator J_12 multiplied by f(t) has J V=0 and J+J^T=0, and F_01=f'(t)J. Verified by tools/verify_transverse_contortion_curvature.py.
