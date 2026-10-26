<!-- BILINGUAL-UNIT: invariant_symplectic_theta -->
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


# Symplectic-first UBT: a natural invariant eight-real-dimensional 2-form

**C-tier exact algebraic result (2026-10-24), not a derivation of the fundamental UBT Hamiltonian or a full field-theoretic presymplectic structure.** Complements the Hamiltonian-first foundations draft #716. No new fundamental field or action.

## Construction from existing invariant data

Represent a biquaternion as X in Mat(2,C). On the underlying real eight-dimensional vector space use the known nondegenerate, phase- and SL(2,C)-congruence-invariant *real symmetric* form
\[
B(X,Y)=\operatorname{Re}\operatorname{Tr}[\operatorname{adj}(X)Y^\dagger].
\]
This is the polarization of H(X)=Tr(adj(X)X†) (the trace here is real on the diagonal). Its real inertia is (2+,6-), as established in canonical_family_hamiltonian_bridge.en.md. Multiplication J:X↦iX satisfies J²=-1, B(JX,JY)=B(X,Y), and B(JX,Y)=-B(X,JY). Consequently
\[
\boxed{\Omega(X,Y)=B(X,JY)}
\]
is an invariant, alternating, nondegenerate real 2-form. Nondegeneracy follows since J is invertible and B is nondegenerate. For a fixed real basis with K=diag(1,1,-1,-1,-1,-1,-1,-1), J is four 2x2 rotation blocks; the matrix Ω=KJ has rank eight, det 1. This defines a pseudo-Kähler-compatible *linear* symplectic vector space without introducing independent cotangent momenta. Symmetry invariance follows from congruence invariance of B and complex-linearity of the phase and SL(2,C) representation, hence commutation with J.

A putative spatial symplectic form \(\int_\Sigma \mu\,\Omega(\delta X,\delta X)\) requires an independently justified integration density \(\mu\), hypersurface, background dependence and treatment of gauge degeneracies. This construction is a *candidate*, not a unique physical Poisson structure; its overall scale is arbitrary and more general invariant structures have not been excluded. Crucially the indefinite B signature does not invalidate Ω as a symplectic form, but does affect candidate Hamiltonian boundedness.

## Exact simplest Hamiltonian flow

On this candidate symplectic space take the *known invariant* H₂(X)=B(X,X)/2 and define the convention \(\iota_{\dot X}\Omega=dH_2\). It follows exactly
\[
\boxed{\dot X=JX=iX.}
\]
Proof: Ω(\dot X,Y)=B(\dot X,JY)=-B(J\dot X,Y); equating dH₂(Y)=B(X,Y) gives \(-J\dot X=X\), hence \(\dot X=JX\). Thus the elementary quadratic generator is **only a uniform internal phase rotation**. It has no spatial propagation, curvature, or Einstein dynamics. Moreover H₂ is indefinite of inertia (2,6), not a physically positive energy.

This is a useful selection filter, not a no-go for other generators. The canonical cotangent structure in #716 is a distinct 16-real-dimensional candidate; the eight-real symplectic construction is *not* an automatic reduction of it, and neither is selected by the locked UBT axioms.

## Decisive further gates

1. Derive the role of complex time t+iψ and of the real physical time generator: determine whether Ω arises as a conserved covariant phase-space current of the **single** Theta theory without assuming the action being sought.
2. Construct intrinsic spatial-derivative / curvature Hamiltonian densities and check covariance and constraint closure, without borrowing the adopted GR action.
3. Identify constraint reduction and positivity on physical modes. Quotient out the phase motion only if a genuine gauge generator and constraint are demonstrated.
4. If a physical H emerges, reconstruct the unique action from this 2-form and H via a *local* symplectic potential, accounting for global/topological obstructions, and test its GR, matter and ψ reductions.

Verification: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_invariant_ubt_symplectic.py' -v\`. An eight-dimensional matrix check verifies algebra, not the field-theoretic theory.
