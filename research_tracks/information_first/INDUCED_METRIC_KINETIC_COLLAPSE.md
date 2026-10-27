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

# Exact induced-metric kinetic collapse in a four-real Theta carrier slice

**2026-10-26 — P0 conditional identity, not a UBT fundamental action.**

Assume a nondegenerate square tetrad E_mu^a=N0^(-1/2)D_mu v^a built from a four-real Lorentz carrier v^a, internal metric eta_ab=diag(-1,1,1,1), and **the same** tetrad defines g_mu nu=E_mu^a eta_ab E_nu^b. Assume N0>0 fixed and omega either prescribed velocity-independent or otherwise such that E's spatial rows have no time velocities. Consider a restricted kinetic term with no other Theta components:
  L_kin = c sqrt(-g) g^mu nu eta_ab (D_mu v^a)(D_nu v^b).
Since Dv=sqrt(N0) E and g^mu nu E_mu^a E_nu^b=eta^ab, the contracted term is exactly 4 N0. Also sqrt(-g)=|det E|. Hence

  L_kin=4 c N0 |det E|.

On any orientation-fixed nondegenerate patch, det E is linear in the temporal row, so the velocity Hessian of this restricted density is identically ZERO. This is the exact opposite of treating the composite metric as a fixed background with Hessian signature (2,6): that result does not transfer to the induced-metric carrier-only sector. Here the first-order kinetic density collapses to volume. If omega=0 and E=dv/sqrt(N0), it is additionally a local boundary term (see zero_connection_volume_pullback_boundary.md).

**Important:** a vanishing velocity Hessian signals primary-constraint candidates, not proof that constraints eliminate ghosts or generate the correct gravity. The momenta may be boundary/cofactor functions and no nontrivial local equations follow in zero-connection case. If Dv includes an omega[Theta] that itself depends on velocities/higher derivatives, or if the full eight-real Theta kinetic form involves extra independent degrees, internal pairings and different composite maps, this identity DOES NOT cover their action. Higher derivative dependence requires an Ostrogradsky/degenerate higher-order analysis; it must not be silently treated as first-jet Dirac mechanics.

The result narrows the selection target: the genuinely composite kinetic family may be too degenerate to propagate a graviton in this sector, while the fixed-background generic family has indefinite directions. Determine the full eight-real representation, independent vs composite omega and kinetic coefficients before declaring a stable Hamiltonian.

Test: tests/test_information_induced_metric_kinetic_collapse.py.
