<!-- BILINGUAL-UNIT: gr-kinetic-volume-2026-11-16 -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact restricted identity, not complete UBT dynamics.
UBT-AI-PROVENANCE-END -->
# Locked kinetic volume and flat-gradient diagnostic

<!-- UNIT: scope -->
## Exact restricted result; no full UBT claim

The canonical central-sharp tetrad and single Theta are unchanged. Existing work already mentions the kinetic-to-volume identity; here the tetrad derivative and its gradient-branch consequence are made explicit. The Lorentz-invariant sharp pairing is assumed.

<!-- UNIT: identity -->
## Kinetic and its first variation


S_kin = (1/2) integral sqrt(-g) g^mn <D_m Theta,D_n Theta>
<D_m Theta,D_n Theta> = N0*g_mn on canonical Lorentz slice
=> S_kin = 2 N0 integral sqrt(-g)
delta S_kin / delta E_mu^a = 2 N0 det(E) (E^-1)_a^mu
If E_mu^a=partial_mu Y^a, partial_mu Cofactor(E)_a^mu=0 (Piola).
=> delta S_kin=0 for compactly supported delta Y.
Implicit E=J(Theta,E,K), A=I-J_E:
EL_K(red S)=S_K+J_K^*(A^*)^-1 S_E, only where inverses exist.


<!-- UNIT: piola -->
## Gradient-sector obstruction

For nondegenerate E=dY, the induced metric is a local pullback of Minkowski space, hence flat. By cofactor divergence (Piola), the four-dimensional Jacobian determinant is a null Lagrangian and the volume action has no bulk Euler equations under compact-supported Y variations. It does not produce Einstein curvature dynamics. This is restricted to the pure-gradient kinetic sector; independent potential and curvature terms change the conclusion.

<!-- UNIT: composite -->
## Remaining composite gap

Because E depends implicitly on the reconstructed omega(E,K), the parent tetrad Euler derivative is NOT the reduced Theta/K derivative. A=I-J_E is a differential operator whose invertibility needs gauge, boundary and functional domain analysis. Neither the physical source rank nor a spin-2 kinetic term follows from the displayed volume formula. The full torsionful composite calculation is still OPEN.

<!-- UNIT: next -->
## Exact remaining action-selection question

The already canonical audit canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex identifies the Einstein-Hilbert/Palatini term as imported. A non-ad-hoc GR completion requires a specified microscopic action or derived quantum effective action that fixes curvature dynamics, plus an on-shell solution, composite Hessian and constraint analysis. This note is not a GR derivation.

<!-- UNIT: verification -->
## Verification boundaries

Test source tools/verify_gr_locked_kinetic_volume_2026_11_16.py checks the volume factor, 16 cofactor first-variation slots and a nontrivial four-dimensional gradient Piola identity with exact SymPy arithmetic. Full repository CI, Lean, bilingual semantic verification and the true on-shell composite dynamics are not established; retain as draft.
