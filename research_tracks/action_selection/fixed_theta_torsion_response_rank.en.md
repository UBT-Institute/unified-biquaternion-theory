<!-- BILINGUAL-UNIT: fixed_theta_torsion_response_rank -->
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


# Exact rank of torsion response at fixed non-null Lorentz-valued Theta

**Conditional pointwise result, 2026-10-25. NOT a count of UBT propagating degrees of freedom or a full action selector.**

At a chosen spacetime point hold a nondegenerate tetrad e fixed, so the metric-compatible spin connection depends invertibly on the 24 torsion components T^a_{mu nu} (as in #743). Assume the *value* of Theta identifies with a nonzero timelike Lorentz vector v∈W_L, and the relevant two-sided pure spin lift acts on that vector in the ordinary Lorentz vector representation. For a variation in the Lorentz spin connection at fixed e and Theta,
\[
\delta(D_\mu\Theta)^a=\delta\omega_\mu{}^a{}_b\,v^b.
\]
A Lorentz generator is antisymmetric after lowering its two Lorentz indices. The linear map \(\mathfrak{so}(1,3)\to\mathbb R^{1,3}\), \(\lambda^a{}_b\mapsto\lambda^a{}_b v^b\), has rank 3 for non-null v, since its image is v-orthogonal and the stabilizer of a timelike v is \(\mathfrak{so}(3)\) of dimension 3. At each independent mu the map has a three-dimensional kernel; for four mu values the full map from 24 connection components to 16 tetrad variation components has
\[
\boxed{\operatorname{rank}=12,\quad\dim\ker=12.}
\]
Since the fixed-e linear map T↔omega is invertible, the same pointwise rank and nullity hold for the **restricted torsion-induced variation** at fixed e and Theta.

This is *not* a count of 12 independent dynamical missing equations: first-jet variations of Theta, reality constraints, full implicit metric-connection closure, torsion selector, gauge quotient and spacetime PDE may mix/remove/change these directions. The connection linearization probes only its Lorentz action on the value of one nonzero timelike Theta. If Theta is not in W_L or the two-sided derivative contains a nontrivial relative representation, this rank need not apply. Fixing e while studying a variation does not mean e is an independent fundamental field.

An exact 16×24 integer test builds four independent blocks, with 6 antisymmetric Lorentz generators per mu acting on v=(1,0,0,0); verifies rank=12 and nullity=12. This is a valid exact algebraic witness, not a full canonical UBT solution. The required next result is the rank/principal symbol of the fully implicit Θ→(e,T,omega) map and its physical gauge-reduced Hessian once a torsion equation is derived.
