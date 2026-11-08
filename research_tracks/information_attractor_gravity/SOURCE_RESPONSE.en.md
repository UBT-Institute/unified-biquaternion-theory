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


# Source-driven theta roots: a mathematical sanity check
Status: WORKING / NONCANONICAL. Date: 2026-11-08.

## Definitions
Fix a complex tau with Im(tau)>0, a dimensionless target a, and a dimensionless prescribed source profile rho(x). Introduce a **chosen** coupling kappa and solve the algebraic toy equation

theta_3(z(x),tau) - a - kappa*rho(x) = 0.

Here z is a scalar complex sandbox variable. It is **not** the full UBT biquaternion Theta, rho is not yet the stress-energy tensor, and x is merely a sampling coordinate. No metric or spacetime dynamics has been derived.

## Exact local result
At any simple root theta_3'(z,tau) != 0, the implicit function theorem gives
dz/d rho = kappa / theta_3'(z,tau).

For a differentiable profile, dz/dx = [kappa/theta_3'(z,tau)] * d rho/dx. A small theta derivative yields large local susceptibility or loss of the simple-root continuation. This is a response diagnostic, **not** Newton's law. Root switching is algorithm-dependent unless continuation, solution branches and a physical evolution are independently specified.

## Discriminating tests
- kappa=0: altering rho must not affect roots.
- kappa != 0: compare numerical finite-difference response with the exact formula; monitor root stability and failed convergence.
- Vary source width and amplitude to identify effects of the assumed coupling.
- Avoid inferring attraction forces from gradients of z; a separately derived metric and geodesic or matter equations are essential.
- Recovering a 1/r potential requires a spatial field equation/Green function not supplied by this local algebraic equation.

## Status of information principle
The kappa*rho coupling has been stipulated. Neither Fisher information nor a variational information functional produces it here. This is a falsifiable prototype for numerical diagnostics, not evidence of gravitational emergence.
Code: UBT-Institute/ubt-theta-lab, projects/fractal_basins_information/source_response.py.
