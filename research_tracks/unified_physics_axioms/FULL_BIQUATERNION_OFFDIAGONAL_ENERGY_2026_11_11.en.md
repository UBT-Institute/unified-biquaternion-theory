# Full off-diagonal biquaternion pairings: positivity is not automatic dynamics

## Exact full-matrix identities


\[
X=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad
P(X)=\operatorname{Tr}(X^\dagger X)
=|a|^2+|b|^2+|c|^2+|d|^2.
\]

\[
H(X)=\operatorname{Tr}(\operatorname{adj}(X)X^\dagger)
=2\operatorname{Re}(a\bar d-b\bar c).
\]

\[
X_{\rm off}=\begin{pmatrix}1&2\\2&1\end{pmatrix},
\quad P(X_{\rm off})=10,\quad H(X_{\rm off})=-6.
\]

\[
A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\quad
X'=AA^\dagger=\begin{pmatrix}5&2\\2&1\end{pmatrix},
\quad\det X'=1,\quad P(X')=34,\quad H(X')=2.
\]


The complex biquaternion is represented by a general complex matrix without imposing diagonality, a unit normalization, or commuting components. The Hilbert–Schmidt expression includes *all* off-diagonal entries but is not an invariant scalar under unrestricted noncompact Lorentz spinor congruence. The existing UBT Lorentz/phase quadratic pairing H includes cross terms explicitly and can be negative even for a nonzero matrix. Its stated invariance must always be interpreted with the representation's prescribed transformation law; do not infer H is invariant under every arbitrary two-sided transformation. The Hermitian matrix example X'=AA† demonstrates that determinant is invariant under the selected determinant-one congruence while the HS size changes from the identity value. Here H=2det on Hermitian two-by-two matrices; that does not establish this identity for general complex matrices.

## Norm alternatives and pitfalls

The complex quadratic determinant det(X) is an algebraic invariant under left/right determinant-one multiplications, but abs(det(X))² is quartic, not a positive definite norm, because nonzero complex matrices can be singular. Replacing the old indefinite kinetic form with positive P or abs(det)² changes the action and the velocity Hessian. Neither eliminates physical ghosts without a new covariant action and a complete constrained Hamiltonian derivation.

A physical observer-dependent positive energy density can be a covariant tensor contraction with a chosen timelike unit observer rather than an invariant positive *scalar* in the original representation. This is a candidate research direction, not an established positive energy theorem for UBT. The information/energy optimization objective also needs genuinely defined operational costs, not arbitrary quadratic matrix size.

## Verification boundary and next experiment

Lean file formal/FullBiquaternionOffDiagonalEnergy.lean proves the real-matrix sign counterexample and the non-invariance of HS size under an off-diagonal shear. The complex all-entry identities, determinant-one congruence example and singular nonzero matrix are checked by SymPy; Lean does not formalize full complex transformation groups. The positive physical energy, gauge constraints and actual scalar/tensor interaction dynamics are OPEN. Derive the action first, solve constraints, and only then extract a positive physical quadratic Hessian and its (possibly non-diagonal) Jacobi theta-mode lattice.

## Repo grounding

- research_tracks/action_selection/theta_kinetic_spectrum.en.md
- research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md
- research_tracks/unified_physics_axioms/formal/BiquaternionJordan.lean
- canonical/ACTION.en.md
