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

# Exact boundary theorem for the zero-connection four-real composite volume branch

**2026-10-26 — proved in the restricted rank-four Lorentz-vector lift, not a full UBT no-go.** This addresses P0 (fundamental action and Hamiltonian) ahead of speculative vacuum counting.

Assume a smooth map v:M^4->R^4 on an oriented coordinate patch, N0>0 constant, and zero Lorentz connection, such that E_mu^a=N0^(-1/2) partial_mu v^a is nondegenerate. Let F(v) be any smooth scalar function of the four real carrier components (no explicit x, derivatives, psi, or independently varying other fields). Work within one orientation-preserving region so the sign of det(dv) does not change. Consider the *restricted comparison* four-form:

  L d^4x = N0^(-2) F(v) det(partial_mu v^a) d^4x = N0^(-2) v^*( F(y) dy^0 wedge dy^1 wedge dy^2 wedge dy^3).

Every smooth top-degree form on R^4 is locally exact. More constructively, define

  G(y)=int_0^1 t^3 F(t y) dt,
  beta(y)=G(y) i_R(dy^0 wedge dy^1 wedge dy^2 wedge dy^3), R=y^a partial/partial y^a.

Then div(G R)=4G + R(G)=F, by differentiation of t^4 F(ty). Hence d beta=F(y) dy^0 wedge ... wedge dy^3 and

  L d^4x = N0^(-2) d(v^* beta).

Therefore the unrestricted *bulk* first variation of this particular volume term with respect to v vanishes identically on compact-support variations, as does its Euler–Lagrange operator. Its canonical velocity Hessian is zero because a 4x4 determinant is affine in its temporal row. The canonical momentum cofactor formula yields primary constraints; since this term is a total derivative, its local bulk symplectic current is trivial modulo boundary subtleties, and it cannot alone provide nontrivial wave equations or a propagating graviton.

An explicit polynomial check uses F(y)=1+lambda*(y0²+y1²+y2²+y3²), G=1/4+lambda*sum(y²)/6; div(GR)=F.

**Limits of theorem:** for the Lorentzian metric volume sqrt(-g)=|det E|, the formula holds patchwise where det E has fixed sign (orientations account for that sign). A nonzero external Lorentz connection Dv=dv+omega v can spoil the exact pullback; reconstructed omega[v], torsion and R(omega), matter dependence, explicit position dependence, compact psi extra dynamics, nontrivial global maps or boundary observables may prevent the reduction to a pure boundary. A function F depending on derivatives or extra dynamical fields also invalidates this proof. It is therefore **incorrect** to extrapolate the theorem to every UBT action.

**Decision gate:** A fundamental candidate whose only zero-connection nondegenerate Lorentz-real sector term is F(v)det(dv) contains no local bulk dynamics *within that restricted sector*. Any attempt to extract a GR graviton or nontrivial Hamiltonian must exhibit an additional truly derived, non-boundary contribution and show its Dirac constraint structure. This is a falsification gate for insufficient action ansätze, not a derivation of a new one.

Verifier: tests/test_volume_pullback_boundary.py.
