# ADM Hessian and constraint audit of the adopted UBT Einstein–Lambda branch

**Scope: classical local Einstein–Lambda endpoint only (C-tier comparison), 2026-10-24. NOT the Hessian of the microscopic full single-Theta theory.** Based on [gravity dynamical postulate](../../canonical/gr_closure/gravity_dynamical_postulate.en.md) and merged #635/#711. The postulate already recovers the local vacuum Einstein equations on its regular split-jet patch, but its microscopic matter/gauge/quantum completion is open.

## ADM endpoint kinetic Hessian

After solving the torsionless Cartan equation *in the spinless vacuum GR endpoint*, take \(h_{ij}\) positive definite, lapse \(N>0\), shift \(N^i\), and \(K_{ij}=(\dot h_{ij}-D_iN_j-D_jN_i)/(2N)\). The Einstein–Hilbert + appropriate boundary action's kinetic density is
\[
\mathcal L_{\rm kin}=\frac{\sqrt h\,N}{2\kappa_{\rm EH}}(K_{ij}K^{ij}-K^2).
\]
Here \(\kappa_{\rm EH}>0\) denotes the standard positive GR normalization after matching the adopted \(\kappa\) convention; no new coupling is introduced.

In a local orthonormal spatial frame (\(h_{ij}=\delta_{ij}\) at the point), define six orthonormal symmetric-velocity components
\[
x=(\dot h_{11},\dot h_{22},\dot h_{33},\sqrt2\dot h_{12},\sqrt2\dot h_{13},\sqrt2\dot h_{23}).
\]
Up to a strictly positive normalization, the kinetic quadratic form is
\[
Q=x^Tx-(x_1+x_2+x_3)^2,\quad \nabla_x^2Q=2(I_6-vv^T),\quad v=(1,1,1,0,0,0).
\]
Eigenvalues are \(-4\) in the trace direction and \(2\) on its five-dimensional orthogonal complement. Thus the 6x6 spatial kinetic Hessian has rank six and inertia (5 positive, 1 negative). Since no \(\dot N,\dot N^i\) occur, the full 10x10 ADM velocity Hessian has rank **six**, four null directions, and inertia \((5+,1-,4\cdot0)\). This is the *expected* gravitational degeneracy, not evidence of a pathological extra mode.

## Constraint count and physical graviton number

With the standard full first-class hypersurface-deformation constraint algebra and appropriate nondegenerate vacuum boundary conditions, the ADM phase space has 20 dimensions per spatial point: six h_ij and four lapse/shift with their ten momenta. Four primary constraints \(p_N\approx0,p_{N^i}\approx0\) plus four secondary constraints \(\mathcal H_\perp\approx0,\mathcal H_i\approx0\) form eight first-class constraints. Hence
\[
N_{\rm DOF}=\frac{20-2(8)}2=\boxed{2}.
\]
Equivalently, eliminate nondynamical lapse/shift from the count, retain 12-dimensional (h_ij,pi^ij) phase space and four first-class Hamiltonian/momentum constraints: (12-8)/2=2. The single negative DeWitt conformal direction is not by itself a propagating ghost. Positivity of local energy density is not asserted; after physical gauge fixing, the two TT graviton polarizations have standard positive quadratic wave energy on suitable stable backgrounds.

This is a **conditional GR endpoint** count. It presumes precisely the adopted local Einstein–Lambda solution-set equivalence and its gauge/constraint structure. It does not independently establish the full split-jet auxiliary constraint algebra, UV stability, extra Theta/psi modes, or that microscopic kinetic inertia (2,6) reduces to just these two modes.

## Hard gate for full UBT

1. Specify the final *single* UBT action including gravity and source/gauge sectors (the gravity postulate alone is not that action).
2. Before restricting to FLRW, list true independent velocities \(\dot\Theta,\dot\omega,\dot K_J,\dot w,\ldots\); differentiate the **full composite** functional, including \(\dot E[D\Theta]\) and possible higher derivatives. For higher-derivative actions use a justified auxiliary/Ostrogradsky or first-order treatment.
3. Find all primary and secondary constraints, calculate their Poisson bracket rank, identify first-/second-class sets and count local propagating modes. Compare with the two-mode Einstein–Lambda endpoint.
4. Check whether any extra scalar, torsional, or complex-time mode is physically stable after reduction; do not infer health from four ADM null directions or the fixed-background Hilbert-energy bridge (#709).

**Reproducibility:** \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_adm_gr_hessian.py' -v\` (SymPy); exact matrix, eigenvalues, rank and DOF arithmetic. These checks validate the benchmark algebra, not the full UBT spectrum.
