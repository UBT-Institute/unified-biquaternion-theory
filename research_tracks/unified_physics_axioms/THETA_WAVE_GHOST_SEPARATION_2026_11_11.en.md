# Full complex Theta wave propagation versus physical stability

## Status and actual input

This track uses the ALREADY-DERIVED eight-real-component, fixed-background kinetic and quartic vacuum Hessians from research_tracks/action_selection/theta_kinetic_spectrum.en.md. It tests the user's Huygens/wave-stability question. It is not a new single-field action, not a statement about a proven nondegenerate UBT physical vacuum, and not a complete field-theoretic Dirac reduction.

## Eight component dispersion, not just scalar or GR tensor sector


\[
K_c=2c\,\mathrm{diag}(1,-1,-1,-1,1,-1,-1,-1),
\quad
M=\mathrm{diag}(0,8\lambda_2r^2,8\lambda_2r^2,8\lambda_2r^2,8(4\lambda_1+\lambda_2)r^2,0,0,0).
\]
\[
\omega^2_{\rm orbit}=k^2\quad(4~\text{modes}),\qquad
\omega^2_{u_j}=k^2-\frac{4\lambda_2r^2}{c}\quad(3~\text{modes}),
\qquad
\omega^2_{v_0}=k^2+\frac{4(4\lambda_1+\lambda_2)r^2}{c}\quad(1~\text{mode}).
\]
\[
c>0:\quad k_{\rm crit}^2=\frac{4\lambda_2r^2}{c}
\ \text{for three transverse modes};\qquad
c<0:\quad k_{\rm crit}^2=\frac{4(4\lambda_1+\lambda_2)r^2}{|c|}
\ \text{for the radial mode}.
\]


Here k² is nonnegative spatial squared wave number and the original model used c as kinetic normalization; do not confuse it with the physical speed of light. The massless orbit directions (u0,v1,v2,v3) are zeroes of the POTENTIAL Hessian, not automatically gauge directions. The generalized squared masses on the normal four-dimensional sector have opposite signs. For c>0 there are three transverse long-wavelength growing modes; for c<0 there is one radial growing mode. A negative squared frequency gives solutions cosh(gamma t) and sinh(gamma t) with gamma²=kcrit²-k², and growth for k²<kcrit². At k²=kcrit² the solutions may drift linearly (zero frequency). For k²>kcrit² the same modes oscillate.

## Key new diagnostic: an oscillatory ghost

Choose the dimensionless sample lambda1=0, lambda2=r=c=1. The u1 mode has Kc=-2 and M=8, hence omega²=k²-4. At k²=9 the mode oscillates with omega²=5. An exact nonzero solution is q(t)=sin(sqrt(5)t)/sqrt(5), for which the canonical energy is E=Kc*(qdot²+k²q²)/2 + M*q²/2 = -1 at all times. Thus REAL frequency and conserved energy coexist with NEGATIVE energy. This is distinct from infrared exponential growth (e.g. k²=1 gives omega²=-3).

The negative kinetic energy direction is not removed by making the wave number large or by observing propagation on the light cone. A stable, constrained full UBT could still remove the mode; that has NOT been shown. This example is a diagnostic for the specified frozen-background eight-component comparator whose pointwise vacuum has a degenerate composite tetrad.

## Huygens principle versus causal cone

The PRINCIPAL characteristic determinant is det P = 256 c^8 (k²-omega²)^8 when physical light speed units are 1. The mass Hessian M changes lower-order dispersion, not this principal cone. A signal-front characteristic is therefore independent of the long-wave growth threshold. The strict Huygens property (retarded Green support only on the null cone) is stronger than having a common characteristic cone and does NOT automatically follow for massive or tachyonic Klein–Gordon-type modes. In generic curved geometry wave tails may occur too. Hence wavefront/Huygens analysis cannot replace the Hamiltonian ghost and Cauchy stability tests.

## Exact verification boundary and the next physical gate

Lean formal/ThetaWaveGhostSeparation.lean proves finite sign implications of an assumed negative mass² at low/high spatial wave number, a simple negative-energy high-k witness and conservation algebra for the signed oscillator. The full matrix/Hessian and representative oscillatory solution are checked in exact SymPy tests. Neither Lean nor SymPy has derived physical UBT normal modes from a FULL nondegenerate action. Actual next physics task remains: find a regular nondegenerate on-shell solution to a selected single complex-Theta action, derive full constraints, and evaluate a bounded physical Hamiltonian plus gauge-reduced hyperbolic principal symbol and retarded Green function.

## References

- research_tracks/action_selection/theta_kinetic_spectrum.en.md
- research_tracks/causality/einstein_causal_principle.en.md
- research_tracks/unified_physics_axioms/DEWITT_TT_POSITIVE_GATE_2026_11_11.en.md
- canonical/ACTION.en.md
