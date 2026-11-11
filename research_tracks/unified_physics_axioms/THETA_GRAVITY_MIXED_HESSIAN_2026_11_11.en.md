# Mixed Theta/gravity velocity Hessian: stability and constraint threshold

## Research question and inherited status

Existing work establishes an explicit rank-four split-jet Minkowski tetrad and, for a **chosen** positive-normalization gravity action, two positive quadratic TT gravity modes (splitjet_spatial_dirac_2026_10.en.md; full_spatial_dynamics_2026_10.en.md; SPLITJET_FULLRANK_TT_STABILITY_2026_11_11.en.md). Independently, the old free eight-real-Theta fixed-background minimal comparator exhibits negative kinetic directions, and a distinct MM gravity-only comparator has an unselected complex/psi principal block, sometimes identically zero (physics_closure_2026_10.en.md). Neither fact fixes the full mixed Hessian after all field and connection constraints.

This note is an **exact two-direction necessary stability gate**, NOT a derivation of the true coupling coefficients a,b,c. Let h represent an already reduced healthy gravity TT coordinate and psi an extra complex-Theta mode *only if both are verified physical after the Dirac quotient*. The quadratic velocity form is

\[
L^{(2)}_{\rm velocity}
=\frac12\bigl(a\dot h^2+2b\dot h\dot\psi+c\dot\psi^2\bigr),
\qquad a>0.
\]
\[
K_{\rm mixed}=\begin{pmatrix}a&b\\b&c\end{pmatrix},
\quad\det K_{\rm mixed}=ac-b^2.
\]
\[
a\,Q(x,y)=(ax+by)^2+(ac-b^2)y^2,
\quad Q(x,y)=ax^2+2bxy+cy^2.
\]
\[
K_{\rm mixed}\succeq0\ \Longleftrightarrow\ ac-b^2\ge0
\quad\text{(for }a>0\text{).}
\]


## Exact derived conclusions

1. If c<0, Q(0,1)=c<0 for **any** b. Merely mixing an independent negative-energy spectator with positive TT gravity does not erase its ghost direction.
2. If c=0 and b is nonzero, det K=-b²<0 and Q(-b,a)=-ab²<0. Thus a zero diagonal psi kinetic term is NOT proof of a harmless nondynamical spectator once cross velocity mixing is introduced: mixing can instead make the 2x2 velocity block invertible and indefinite. Conversely b=0 and c=0 makes a singular positive-semidefinite kinetic block, **not** yet a proof that a constraint removes psi; its Dirac preservation and spatial/potential interactions still matter.
3. For a>0, positive semidefiniteness of this genuine two-physical-coordinate velocity block requires and is equivalent to ac-b²>=0. If it is strictly greater than zero, the block is positive definite. If it is zero, the block has a null velocity direction and may produce a primary constraint, but the complete Dirac algebra and reduced physical Hamiltonian must still be computed.
4. Even satisfying the kinetic gate does **not** establish stability of the full mode: the potential Hessian, spatial-gradient principal matrix, hyperbolicity, boundaries and nonlinear interactions must independently pass. Kinetic ghosts and tachyonic instabilities are different.

A negative unreduced Hessian minor is **NOT** automatically a physical ghost when those coordinates are gauge, auxiliary or removed by first-/second-class constraints. This two-mode test applies to the **reduced** physical kinetic subspace, or conditionally when both modes are known to survive the quotient. The real full-complex-Theta action and its mixed coefficients have not been selected.

## Proof status and next exact task

Lean in formal/ThetaGravityMixedHessianGate.lean proves the no-division completion-of-square, the positive-semidefinite threshold, the explicit negative determinant witness, and the mixed zero-kinetic diagonal witness. Tests use exact SymPy arithmetic, including the rank change at b=0 versus nonzero b. These proofs do not build a full action, derive a Dirac quotient, identify whether psi is physical or establish stability of UBT.

Next derive a real common quadratic action for [h_TT, full complex Theta, physical spin connection, relative/jet connection] on the explicit nondegenerate Minkowski split-jet witness. Construct its full time-principal Hessian and primary constraints; determine b and c and test ac-b² before mode diagonalization. Do not inject a positive spectator term by hand, and do not conflate prior spectator zero principal symbol with stable physics.

## Evidence reused

- research_tracks/action_selection/full_spatial_dynamics_2026_10.en.md
- research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md
- research_tracks/action_selection/physics_closure_2026_10.en.md
- research_tracks/action_selection/theta_kinetic_spectrum.en.md
- research_tracks/unified_physics_axioms/SPLITJET_FULLRANK_TT_STABILITY_2026_11_11.en.md
