<!-- BILINGUAL-UNIT: stabilizer_curvature_not_gauge -->
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


# Stabilizer torsion ambiguity can alter Lorentz curvature and spin transport

**Exact conditional counterexample, 2026-10-25. Not full UBT dynamics or a proof of physical propagating degrees of freedom.** Follows #763.

Assume the restricted Lorentz-vector carrier v of the single Theta satisfies e=N0^(-1/2) D^omega v on a patch where v is timelike and e is nondegenerate. An so(1,3)-valued one-form C with Cv=0 leaves v and e invariant when omega→omega+C, while changing torsion by C∧e. The curvature changes **exactly** as
\[
R(\omega+C)-R(\omega)=D_\omega C+C\wedge C.
\]
Therefore invariant tetrad and metric do not imply invariant spin curvature.

**Explicit smooth local witness.** Set N0=1, coordinates x^a=(t,x,y,z), region t²>x²+y²+z² and t>0, v^a=x^a, e^a=dx^a, omega=0. Choose a smooth local Lorentz transformation L(v) that takes v to (sqrt(-eta(v,v)),0,0,0); choose the spatial rotation generator J with J^1{}_3=1,J^3{}_1=-1 (others zero), and define K(v)=L(v)^{-1}JL(v). Then K(v)v=0 everywhere. Define C=x K(v)dy, where x=x^1 and dy=dx². Therefore D^{omega+C} v=dv, so **the same exact canonical tetrad and metric** hold throughout the patch; nevertheless T'=C∧e generally nonzero.

At p=(t0,0,0,0), t0>0, C(p)=0 but
\[
R(\omega+C)_{p}=dC|_p = J\, dx\wedge dy,
\]
which is nonzero while R(omega)=0. The local curvature of the Lorentz/spin connection can therefore differ even at a point where the connection coefficients coincide. Around sufficiently small loops in the xy plane, a spinor carrying a nontrivial spin representation acquires a different infinitesimal holonomy, subject to choosing the physical spin coupling.

This **does not** establish whether the stabilizer directions are genuine observables of UBT or gauge: the full Theta carrier representation, coupling to material sectors, allowed local transformations, and Hamiltonian constraints are not finalized. A gauge equivalence preserving physical spin curvature up to conjugation cannot map zero curvature to nonzero curvature; however dynamics could exclude one branch, and no identification of these two backgrounds as solutions of the unique action is claimed.

**Selection gate:** the one-Theta action must specify whether this nontrivial stabilizer curvature is constrained, auxiliary and eliminated, or propagating; deriving the torsion source/physical symplectic form is still essential. The pure spin-lift construction is only a controlled branch, not general two-sided relative UBT.
