<!-- BILINGUAL-UNIT: sl2c_noncompact_yang_mills_inertia -->
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


# Noncompact SL(2,C) Yang-Mills kinetic signature: exact obstruction

**Status:** exact 6x6 finite-dimensional invariant-form calculation, 2026-10-26. Conditional no-go for conventional propagating real SL(2,C) Yang-Mills with nonzero invariant nondegenerate kinetic form on a Minkowski background. NOT full UBT Dirac/ADM proof.

With T=(i sigma_i/2, sigma_i/2), i=1..3, define R_ab=Re Tr(T_a T_b), Q_ab=Im Tr(T_a T_b). Direct Pauli multiplication gives
```
R=(1/2) diag(-I3,+I3)
Q=(1/2) [0 I3; I3 0].
```
Both real symmetric bilinear forms are Ad-invariant for the real Lie algebra sl(2,C). Every real symmetric Ad-invariant bilinear form on this real-simple algebra is a linear combination G(alpha,beta)=alpha R+beta Q. (The two-dimensionality follows from sl(2,C) as a complex simple algebra regarded as real; independently confirm under the declared representations if generalized matter couplings are introduced.) Direct multiplication yields
```
G^2=(alpha^2+beta^2) I6/4
det G=-(alpha^2+beta^2)^3/64.
```
For any (alpha,beta)!=(0,0) the eigenvalues are +/-sqrt(alpha^2+beta^2)/2 each with multiplicity 3: inertia (3,3). The zero form gives no conventional Yang-Mills kinetic term.

For standard Lorentzian gauge action L=-1/4 G_ab F^a_mu nu F^{b mu nu}, linearized around A=0 in flat Minkowski, choose temporal/transverse gauge and solve the Gauss constraints. Two transverse helicities remain for EACH of the six internal generators. The physical quadratic Hamiltonian per transverse Fourier mode is proportional to G_ab(E_T^a E_T^b+B_T^a B_T^b)/2. Gauss law removes longitudinal modes and does not eliminate all transverse negative-norm internal directions. Hence there are three negative-energy internal directions times two transverse helicities in this standard free gauge sector. Rescaling overall sign reverses both signs and leaves indefiniteness.

This is a **sharp conditional obstruction** to remedying the indefinite Theta kinetic pairing simply by promoting full noncompact SL(2,C) to ordinary propagating Yang-Mills. It does not exclude a compact subgroup, altered or constrained gauge sector, novel degeneracy, a different reality condition, or a complete constrained gravitational completion; those are different hypotheses and must be independently derived. Nor does it prove that negative kinetic entries survive a hypothetical nonstandard mixing with gravity; such a completion requires its own complete Hessian and constraints.

Exact checker: tools/verify_sl2c_yang_mills_inertia.py; regression: tests/test_sl2c_yang_mills_inertia.py. Proposed independent-metric/psi-circle ADR remains contingent, not accepted. No canonical action modified.
