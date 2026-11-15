# Canonical UBT right-action survival gate: geometry versus internal gauge

**Scope:** direct comparison with canonical/geometry/connection.tex and canonical/geometry/biquaternion_metric.tex (master inspected 2026-11-12). This is a conditional algebraic gate, not a derivation of weak SU(2).

The canonical metric is g_{mu nu} 1 = (E_mu^sharp E_nu+E_nu^sharp E_mu)/2 on the physical Lorentz slice W_L, with E_mu=N0^{-1/2} D_mu Theta. Canonical connection gives D_mu Theta=partial_mu Theta+A_mu Theta-Theta B_mu and the no-new-field representative A_mu=Omega_mu, B_mu=-Omega_mu^ddagger, modulo common central cancellation.

Let a constant right transformation E_mu -> E_mu U be considered. Assuming sharp is an anti-involution, (E_mu U)^sharp=U^sharp E_mu^sharp. Then g' 1=U^sharp (g 1) U=g U^sharp U. Thus metric preservation requires U^sharp U=1, AND the transformed E must still lie in W_L. For nonconstant U(x), the same pointwise metric criterion holds, but D_mu Theta transforms covariantly only if the right connection transforms B'_mu=U^{-1}B_mu U+U^{-1}partial_mu U (for Theta'=Theta U and A unchanged). This is a formal right gauge covariance identity, not proof that B'_mu is allowed by the canonical reduced connection.

Critical: the condition U^sharp U=1 is not generally the matrix-unitarity condition U^dagger U=1. If sharp is quaternion conjugation, its unit-norm complex-biquaternion group is the complex spin group SL(2,C), not compact U(2); the Hermitian-matrix Lorentz slice typically reduces admissible right actions further. Thus the previously found U(2) as a unitary subgroup of the abstract right commutant is **not established as a symmetry of the canonical metric or action**.

Moreover B'_mu must continue to satisfy B'_mu=-Omega'_mu^ddagger (modulo common central term) and the specified torsion/metric compatibility constraints. If Omega is fixed by the tetrad and torsion, an arbitrary independent local right U(2) transformation cannot be treated as a new physical gauge field. Even if a subgroup acts as a frame redundancy, that is not a propagating Yang-Mills sector.

**Exact algebraic statement:** right-multiplication commutes with left-multiplication on A=M2(C); it does NOT follow that arbitrary right multiplication preserves W_L, sharp, or the composite two-sided connection. A physical internal gauge group is the intersection of the commutant with the stabilizer of W_L, the sharp metric, the fermion action, and the dynamically allowed connection transformations.

**Outcome:** right U(2) as emergent electroweak gauge symmetry remains OPEN and is not presently derived from canonical UBT. Next decisive input: explicit sharp and ddagger maps, full W_L embedding and fermion module/action, so this intersection can be calculated rather than assumed.
