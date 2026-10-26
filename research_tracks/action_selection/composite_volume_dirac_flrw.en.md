<!-- BILINGUAL-UNIT: composite_volume_dirac_flrw -->
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


# Exact Dirac reduction of the existing composite-volume FLRW truncation

**2026-10-24 — C-tier conditional calculation; not a full-UBT Dirac analysis.** References: [composite Lorentz-jet volume identity](lorentz_jet_volume_boundary.en.md), [closed FLRW coframe](connection_closed_flrw.en.md), [Hilbert–canonical fixed-background bridge](energy_charge_bridge.en.md), and merged #700.

## Premises

Use the existing real Lorentz-slice identity \(\mathcal L_{\rm kin}=4c\mathcal N_0\sqrt{-g}\) and an *algebraic* potential \(-U(i\rho I)\sqrt{-g}\). Define \(F(\rho)=4c\mathcal N_0-U(i\rho I)\). Restrict before variation to the radial single-Theta closed FLRW coframe on a compact spatial section of volume \(\mathcal V>0\), with \(N=\dot\rho/q>0\), \(q=\sqrt{\mathcal N_0}>0\), \(a>0\). The restricted Lagrangian is
\[
L_{\rm red}=\frac{\mathcal V}{q}\dot\rho\,a^3 F(\rho).
\]
Here \(\rho\) is a coordinate, \(a\) is an independent ansatz variable parameterizing the spatial connection, and the equality holds only on the restricted configuration family.

## Constraint algebra for \(F(\rho)\neq0\)

The conjugate momenta and two primary constraints are
\[
p_a=0,\quad p_\rho=\frac{\mathcal V}{q}a^3F(\rho),\qquad
\phi_a=p_a\approx0,\quad\phi_\rho=p_\rho-\frac{\mathcal V}{q}a^3F(\rho)\approx0.
\]
With \(\{a,p_a\}=\{\rho,p_\rho\}=1\), their bracket is
\[
\boxed{\{\phi_a,\phi_\rho\}=\frac{3\mathcal V}{q}a^2F(\rho).}
\]
Therefore, wherever \(a>0,F\ne0\), both constraints are **second class** and the reduced homogeneous phase-space dimension is \(4-2=2\), corresponding to one formal canonical degree of freedom. **Correction to a tempting inference:** two second-class constraints do *not* remove both of the two original configuration degrees of freedom. However the canonical Hamiltonian is identically zero and Dirac consistency determines the multipliers to vanish; hence \(\dot a=\dot\rho=0\). This contradicts the assumed nondegenerate cosmic-time branch \(\dot\rho/q=N>0\): **there is no stationary trajectory in this regular \(F\ne0\) branch of the reduced variational problem.**

Equivalently, its Euler equations are
\[
\frac{\delta L_{\rm red}}{\delta a}=\frac{3\mathcal V}{q}a^2F(\rho)\dot\rho=0,\quad
\frac{\delta L_{\rm red}}{\delta\rho}=-\frac{3\mathcal V}{q}a^2F(\rho)\dot a=0.
\]
With \(N>0\) and \(a>0\), the first forces \(F=0\). At such zeros the Poisson matrix loses rank; treating its constraints as regular second-class is invalid, and a separate singular analysis is required. If \(F\) vanishes on an open interval of \(\rho\), the action itself vanishes along that branch, so it supplies no local dynamics in this truncation.

## Physical scope / nonclaims

This exact reduced system is **not** the result of varying the complete unconstrained Theta/connection action first. In general, restriction and variation do not commute; missing transverse connection and Theta variations may introduce more equations, not rescue a purported solution automatically. The closed-FLRW coframe in #685 is kinematic and need not solve the full field equations. This constraint calculation gives neither the full gravitational Hamiltonian nor stable scalar energy. In particular, its zero canonical Hamiltonian does not establish positive energy, and its second-class pair is not a proof of hidden UBT gauge invariance.

**Impact on action selection:** the minimal composite quadratic pairing plus algebraic potential cannot deliver ordinary closed-FLRW expansion through these *restricted* Euler equations for a regular nonzero F. A genuinely selected derivative/curvature-dependent term and its full composite variation remain necessary; simply reusing the fixed-background Hilbert energy/Hamiltonian from #709 is incorrect.

## Verification

Run \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_composite_volume_dirac.py' -v\` with SymPy. The test covers momenta, constraint bracket, Euler derivatives and the zero Legendre Hamiltonian. Tests are finite-dimensional algebra checks, not physical validation.
