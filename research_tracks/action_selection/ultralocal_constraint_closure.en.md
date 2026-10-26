# Hamiltonian-first UBT: ultralocal scalar constraint closure obstruction

**Conditional exact canonical theorem (2026-10-25), not a complete physical UBT Hamiltonian.**

On a chosen spatial slice suppose the eight real components q^A of Theta transform as spatial scalars and the independently introduced p_A as densities, with canonical {q^A(x),p_B(y)}=δ^A_B δ³(x-y). This cotangent structure is a **trial**, not selected by locked UBT axioms.

The spatial diffeomorphism generator D[ξ]=∫p_A ξ^i ∂_i q^A gives {q,D[ξ]}=ξ·∂q and {p,D[ξ]}=∂_i(ξ^i p). Under suitable boundaries it closes {D[ξ],D[η]}=D[[ξ,η]] (with the standard Poisson-generator convention).

Consider **any** ultralocal smooth scalar constraint density h(q(x),p(x)) of weight one with no spatial derivatives and no nontrivial field-dependent smearing. Set H[N]=∫N(x)h(q(x),p(x)). Its Poisson bracket is
\[
\{H[N],H[M]\}=\int d³x\,N(x)M(x)
\sum_A\big(h_{q^A}h_{p_A}-h_{p_A}h_{q^A}\big)=0.
\]
This is exact, independent of the specific invariant potential or internal spin algebra.

By contrast, **if** the reduced UBT gravitational constraints must realize the usual nondegenerate GR hypersurface deformation algebra with composite inverse metric h^{ij}[Theta],
\[
\{H[N],H[M]\}=D[h^{ij}(N\partial_jM-M\partial_jN)]
\]
(up to additional independently derived internal gauge constraints and possible constraints from composite variables). Generically this RHS is nonzero off the momentum-constraint surface. Thus an ultralocal scalar-density Hamiltonian on the above canonical field phase space **cannot reproduce the required nontrivial off-shell refoliation algebra**. On-shell weak vanishing of both sides is not sufficient evidence of equality of their structure functions.

**Important scopes:** The proof assumes canonical cotangent brackets and spatial-scalar transformation of q^A, and no derivative-dependent reduction, secondary constraints or noncanonical Dirac brackets. It does NOT exclude a different physical symplectic structure, a reduced or emergent gravitational phase space, or non-ultralocal h. It does NOT choose the derivative/curvature Hamiltonian or derive Einstein dynamics. Spatial gradients by themselves do not guarantee the GR algebra; the composite metric is derivative-dependent and constraint reduction may be essential.

**Next calculation:** choose *one* fully specified, allowed composite tetrad and torsion/connection reconstruction on a nondegenerate patch; compute induced primary constraints, reduced brackets and the structure functions of H and D. Do not equate the two-sided curvature commutator of #736 with Hamiltonian constraint brackets.

Regression: python -m unittest discover -s research_tracks/action_selection/tests -p 'test_ultralocal_constraint_closure.py' -v.
