# Theta energy needs a positive physical UBT Hamiltonian

## Scope and pre-existing Hessian

The previously studied Gaussian theta prime spectrum assumed a positive energy matrix. It cannot simply be identified with the canonical complex-biquaternion Lorentz/phase-invariant kinetic pairing calculated in research_tracks/action_selection/theta_kinetic_spectrum.en.md. That established fixed-background, unconstrained eight-real-field comparator has an indefinite kinetic matrix and a normal fluctuation block with opposite-sign kinetic directions.

## Exact inherited identities


\[
K_{\rm kin}=2\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1),\qquad
\operatorname{inertia}(K_{\rm kin})=(2,6).
\]
\[
\operatorname{inertia}(K_{\rm normal})=(1,3).
\]
\[
m_{\rm rad}^2=\frac{4(4\lambda_1+\lambda_2)r^2}{c},\qquad
m_{\rm trans}^2=-\frac{4\lambda_2r^2}{c}.
\]
\[
\lambda_1\ge0,\quad\lambda_2>0,\quad r>0,\quad c\ne0.
\]


The radial and three degenerate transverse generalized mass-squared eigenvalues have opposite signs for either sign of c: positive c gives negative transverse eigenvalues, negative c gives a negative radial eigenvalue. In the unconstrained fixed-background model the kinetic Hamiltonian also has a negative momentum direction and is unbounded below. Consequently the naive positive-temperature Gibbs trace from that Hamiltonian cannot be identified with a convergent Euclidean Jacobi theta lattice partition function. Negative generalized mass squared and negative kinetic energy are different issues; both arise under the specified comparator assumptions.

## Consequences for prime selection

The positive quadratic lattice energy E_n=n^T K n used in the previous prime tracks was a model input, not the kinetic matrix of canonical UBT. Neither diagonal Gaussian norm nor a particular positive spectral lattice is derived from the one action. The observation that mode degeneracies separate prime congruence classes is valid mathematics, but currently no claim about UBT physical excitations.

## Formal verification and next gate

Lean formally verifies the **sign implications** of the existing radial/transverse eigenvalue formulas, for positive and negative c. Lean does not prove their underlying field-theoretic Hessian calculation, physical gauge reduction, actual mode spectrum, Gibbs convergence, or quantum gravity. SymPy verifies the matrix inertia and opposite-sign generalized eigenvalues and a negative Hamiltonian momentum direction on the assumed fixed background.

The next physics task must finalize the single real-valued action, derive and solve all connection/metric constraints, compute the reduced physical quadratic Hamiltonian and only then establish any compact phase and positive theta lattice. A bare curvature/Einstein-Hilbert or an extra positive K is not to be silently inserted. The fixed-background no-go is not a proof that every completion of UBT fails.

## References

canonical/ACTION.en.md
research_tracks/action_selection/theta_kinetic_spectrum.en.md
research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md
research_tracks/unified_physics_axioms/THETA_PRIME_ROBUSTNESS_2026_11_11.en.md
