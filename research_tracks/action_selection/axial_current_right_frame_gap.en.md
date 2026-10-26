<!-- BILINGUAL-UNIT: axial_current_right_frame_gap -->
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


# Axial Dirac source from Theta is right-column-frame dependent

**Exact algebraic obstruction to an intrinsic current; 2026-10-25.** Refines conditional spin-torsion PR #746. Does not assert unrestricted right SU(2) is an actual gauge symmetry of locked UBT.

Let Theta=[xi,chi] in Mat_2(C). As in #724, choose F(Theta)=(xi,epsilon chi*) as left/right Weyl columns, epsilon=[[0,1],[-1,0]]. In the conventional Weyl representation, the temporal axial bilinear satisfies, up to the fixed chirality sign convention,
\[
j_5^0=\Psi^\dagger\gamma^5\Psi
=\|\chi\|^2-\|\xi\|^2
=-\operatorname{Tr}(\Theta^\dagger\Theta\,\sigma_3)
\]
when gamma^5=diag(-I_2,+I_2) and sigma_3=diag(1,-1). The last expression is a *right-frame-sensitive* quadratic function of Theta. The central contrast: the positive scalar Tr(Theta†Theta)=||xi||²+||chi||² is invariant under Theta→Theta U for U∈SU(2), while j5^0 generally is not.

Explicitly, choose xi=(1,0)^T, chi=0 and U=epsilon. Then Theta' = Theta U = [0,xi], so j5^0 changes from -1 to +1 while Tr(Theta†Theta) stays 1. Thus a unique intrinsic axial source constructed via this F cannot be claimed without fixing/proving a physical right-column frame or showing invariance under the *actual* permitted right transformations.

**Scope and caveats.** This is an obstruction under arbitrary right SU(2) mixing of columns; right SU(2) need not preserve the locked Lorentz-valued tetrad W_L pointwise, and UBT's admissible right-frame gauge group has not been fully established. Thus it is NOT a proof that all physical axial currents are impossible. However any proposal using F must state and derive the right-frame/complex-structure selector rather than hiding it in notation. Combined with #746, the standard conditional Dirac spin density does not yet determine UBT's torsion or fundamental Hamiltonian/action.

Next gate: specify which right transformations preserve the *full* composite connection, Lorentz slice, constraints and physical presymplectic form; derive an intrinsic chiral projector or a different Theta-bilinear independent of the arbitrary frame if the gauge symmetry demands it.
