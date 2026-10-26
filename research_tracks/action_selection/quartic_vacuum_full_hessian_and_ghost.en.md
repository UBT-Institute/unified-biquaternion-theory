<!-- BILINGUAL-UNIT: quartic_vacuum_full_hessian_and_ghost -->
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


# Stationary quartic vacuum and negative-kinetic transverse instability

**2026-10-26 — exact Hessian verification, conditional independent-metric minimally coupled Theta branch.** The model is not the finalized UBT master action.

In coordinates X=z0 I+sum_{j=1}^3 zj i sigma_j, with z_j=x_j+i y_j and H=2(|z0|²-sum_j |zj|²), det X=sum_{j=0}^3 zj², consider V=V0+m² H+lambda1 H²+lambda2 |det X|². At X0=i r I, r real !=0, the eight-real gradient vanishes iff m²+(4lambda1+lambda2)r²=0. This admits r²=-m²/(4lambda1+lambda2)>0 for m²<0 and 4lambda1+lambda2>0.

With q=(x0,x1,x2,x3,y0,y1,y2,y3), the Hessian after enforcing stationarity is exactly diag(0,0,0,0, 8r²(4lambda1+lambda2),8lambda2 r²,8lambda2 r²,8lambda2 r²). Thus for lambda1>=0,lambda2>0 it is positive semidefinite (not positive definite), with four flat orbit-related directions. At this stationary vacuum V(X0)=V0-(4lambda1+lambda2)r^4. A Minkowski background requires an additional cosmological-constant/vacuum-energy compatibility equation; in the simplest flat independent-metric zero-CC normalization it needs V0=(4lambda1+lambda2)r^4. This is parameter tuning, not a prediction or a derivation from UBT.

For the previously adopted kinetic pairing with real-coordinate matrix G=diag(2,-2,-2,-2,2,-2,-2,-2), the three y_j directions are nongauge at X0 in the congruence representation and have generalized mass squared (G^{-1} V'')_y_j=-4lambda2 r². Hence for lambda2>0 they have wrong-sign kinetic quadratic form AND exponential infrared modes in the fixed-background linearized equations. Linearized Einstein momentum/Hamiltonian constraints have zero first-order matter source at a constant stationary vacuum, so they do not eliminate these modes in the usual regular perturbative setup. This is a conditional test, not a full coupled nonlinear ADM theorem.

The radial y0 direction has generalized mass²=4(4lambda1+lambda2)r²>0. Four zero-Hessian directions include three boost-orbit directions and one phase-orbit direction, but a zero eigenvalue alone is not a physical particle count.

For lambda2=0, the particular three transverse generalized masses vanish; the negative kinetic inertia remains, so removing the tachyon does not automatically remove the ghost. For lambda2<0, the stationary vacuum's potential Hessian has negative transverse curvatures and fails the same local-minimum acceptance gate. No assertion is made about other vacua or other kinetic/composite models.

Verified by tools/verify_theta_quartic_vacuum_hessian.py and tests/test_theta_quartic_vacuum_hessian.py. This is a falsification result for the explicitly tested minimal branch, not all UBT.
