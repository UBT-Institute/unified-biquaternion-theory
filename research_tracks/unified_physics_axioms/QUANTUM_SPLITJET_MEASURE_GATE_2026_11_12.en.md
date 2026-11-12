# Quantum split-jet measure: finite regulator theorem and open continuum gates

**Status:** exact finite-dimensional gauge-fixed identity under explicitly stated assumptions. NOT a proof of the complete quantum UBT.

## Parent and assumptions

Take a finite lattice with N independent tetrad components and N auxiliary image components Q, plus carrier X of dimension m. Let the remaining base fields collectively be B=(omega,psi,barpsi,Lambda,C3,...), with a separately defined base measure. Fix s(B)>0. The parent constraint is

chi(E,X,Q;B)=s(B) E - D_B X - Q,

where D_B is a finite linear operator acting on X. Let S0(E,B) be the Einstein–Cartan–Dirac–HT comparator, independent of X and Q. Define the constrained integral

Z_P=1/Vol(G) integral dE dX dQ dB delta^N(chi) exp(i S0(E,B)/hbar),

with flat translation-invariant dQ and dX measures, compatible domains and boundary conditions, and G the m-dimensional shift X->X+epsilon, Q->Q-D_B epsilon (all other fields fixed).

## Exact finite-dimensional elimination

At fixed E,X,B, the derivative d chi/dQ=-I_N, hence |det(d chi/dQ)|=1, independent of B. Therefore

integral dQ delta^N(sE-D_B X-Q)=1.

Choose the gauge X=0. The Faddeev–Popov matrix is d(X+epsilon)/d epsilon=I_m, so Delta_FP=1. With the same normalization of Vol(G), the X integral cancels the shift volume:

Z_P = integral dE dB exp(i S0(E,B)/hbar) = Z_0.

The same identity holds for gauge-invariant insertions O(E,B). It holds for finite-dimensional, compatible measures and does not use equations of motion or the assumption that omega is torsion free. It also holds for independent Grassmann spinors because the shift does not act on them.

**Crucial distinction:** if one eliminates E rather than Q, delta(sE-DX-Q) yields |det s|^{-N} (for scalar s acting on each image component). This factor is a change-of-variable Jacobian, not an additional physical loop effect: the transformed measure and action must be treated together. Ignoring it while changing integration variables can manufacture a spurious dilaton effective potential.

## Failure conditions and continuum limitations

The identity can fail or require modification if:
- Q is restricted by additional reality, stabilizer, integrability or boundary constraints; its integration domain is not the full image space.
- The microscopic action or measure depends explicitly on X or Q, or on an imaginary-Theta sector that is not gauge.
- The shift transformation fails to preserve boundary conditions, introduces zero modes, or has an anomalous regulator.
- The path integral over the Lorentz connection, diffeomorphism constraints, HT three-form gauge symmetry or fermionic second-class constraints is not correctly gauge-fixed.
- The tetrad becomes degenerate, s=0, or the field chart ceases to be regular.

This finite regulator theorem does **not** establish BRST nilpotency for the full theory, UV renormalizability, anomaly cancellation, positivity, or a well-defined nonperturbative gravitational measure.

## Next checks

1. Specify the actual split-jet image map and its measure on each regular chart; derive the Jacobian for the original (X,K_J,w) -> (E,X,z) variables, not only the enlarged Q parent.
2. Prove compatibility of the carrier shift with boundary conditions and stabilizer quotient.
3. Build BV/BRST ghosts for independent shift, Lorentz, diffeomorphism and three-form symmetries, then test master equation and one-loop anomaly.
4. Quantize the independent complex Theta modes only after a nondegenerate, ghost-free kinetic and constraint system is supplied.

## Interpretation

The auxiliary parent can be *exactly* equivalent to the Einstein–Cartan–Dirac comparator at the finite regulated path-integral level. This is a conditional equivalence result, not a new quantum gravity theory or a claim that commuting Theta produces fermionic statistics.
