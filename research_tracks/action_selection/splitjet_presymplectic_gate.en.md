<!-- BILINGUAL-UNIT: splitjet-presymplectic-gate -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional presymplectic benchmark; no derived Theta Hilbert space.
UBT-AI-PROVENANCE-END -->
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

# P0: split-jet gravitational solutions do not automatically imply the physical Theta phase space

**26 October 2026.** Directly follows the existing `single_theta_macdowell_mansouri_candidate.en.md` and `adm_gr_hessian_constraint_audit.en.md`.

## Actual obstacle

The chosen candidate maps the fundamental Lorentz-real carrier and auxiliary variables into tetrads:
E^a_mu = N0^(-1/2) (partial_mu X^a + omega_mu^a_b X^b + K_{J,mu}^a_b X^b + w_mu X^a).
For non-null X the map from variations of (K_J,w) to δE is pointwise onto. This is enough to reproduce the Palatini **Euler-Lagrange equations** on that patch. It is NOT proof of equivalent covariant phase spaces, canonical brackets or physical quantum Hilbert spaces: E includes derivatives of X, so a solution-space correspondence must separately respect the presymplectic form, boundary charges and gauge kernels.

At fixed background omega (to isolate the map), define Q_mu^a := K_{J,mu}^a_b X^b+w_mu X^a. Then E=N0^(-1/2)(dX+omega X+Q). Where Q spans all four tetrad directions via the split-jet auxiliaries, the infinitesimal shift δX=epsilon with δQ= -D_omega epsilon yields δE=0 (and δomega=0). Such shifts are **null for any presymplectic form obtained solely by pulling back the Palatini presymplectic form through E**, provided they respect boundary conditions. Note Q is composite of K_J,w,X, so implementing δQ requires a local auxiliary lift on the non-null patch. This is a redundancy of the representation, not a ghost-removal theorem for the full 8-real Theta and psi dynamics.

For a differential field map F: (X,Q)->E, the covariant presymplectic potential must be derived by varying the actual composed action and integrating by parts. One cannot simply identify canonical momentum P_X with Palatini momentum P_E, because δE contains D δω and D δX and boundary contributions. In a strict first-order Palatini formulation θ_HP~ε_abcd E^a∧E^b∧δω^cd/(4kappa), not a naive P_E δE term; the derivative-dependent lift can produce additional boundary pieces proportional to tetrad equations before going on shell.

## Exactly solvable toy demonstration of the issue (NOT UBT)

Take E=dot x+u and L=(1/2) (dot E)^2 with independent auxiliary u. The action is invariant under δx=ε(t), δu=-dot ε(t), since δE=0 identically. The invariant physical coordinate is E, with momentum p_E=dot E, symplectic form Ω=δp_E∧δE, and Hamiltonian H=p_E²/2≥0. There is one physical mechanical degree of freedom after quotienting the shift redundancy. The apparent higher derivatives of x in L do not automatically imply an Ostrogradsky ghost: the invertible change of variables (x,u)->(x,E) involves one time derivative, and x is pure gauge. This is only a counterexample to naive Hessian counting; it does not imply that all derivative-defined tetrads are healthy.

## Binding P0 to the actual MM candidate

1. Compute the complete covariant variation of the composed MM functional, retaining all E[X,K_J,w,omega] chain-rule and boundary terms.
2. Derive the presymplectic current on the non-null stationary solution space and find its kernel including split-jet stabilizer, Lorentz, diffeomorphism and possible X/Q shifts.
3. Show the kernel directions are true gauge transformations (off-shell action invariance with admissible boundary conditions), not merely zero-velocity Hessian directions.
4. Establish symplectomorphism of **reduced** solution spaces with the Palatini sector (including horizon boundary charges), or exhibit its failure.
5. Only then quantize positive physical degrees and introduce the observer algebras used in the entropy programme.
6. Full complex Theta, matter, psi, and Lorentz-real projection remain separate open checks; a healthy gravitational quotient alone does not prove positivity of the total theory.

**Decision:** The current conditional GR solution-set theorem is useful but insufficient to justify physical-Hilbert-space claims. The immediate missing result is a presymplectic equivalence theorem, not an arbitrary horizon cell size.
