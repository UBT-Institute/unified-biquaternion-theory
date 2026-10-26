# Exact local Lorentz-connection reconstruction: solvability and 12-function ambiguity

2026-10-26. Integrated Fundamental Dynamics track. EXACT algebraic result for restricted real Lorentz-vector lift, NOT a torsion selector or complete two-sided UBT closure.

For a nonnull Lorentz vector carrier v in W_L, nondegenerate e and nonzero N0, consider
sqrt(N0) e_mu^a = partial_mu v^a + omega_mu^a_b v^b,
where each omega_mu belongs to so(1,3). Define u_mu^a=sqrt(N0)e_mu^a-partial_mu v^a, and v²=eta_ab v^a v^b !=0.

**Theorem.** A metric-compatible omega exists at a point if and only if
v_a u_mu^a = 0 for each mu=0,1,2,3.
When true, the FULL affine solution space is
omega_mu^a_b = (u_mu^a v_b-v^a u_{mu b})/v² + C_mu^a_b,
with C_mu in so(1,3) and C_mu^a_b v^b=0.

**Proof.** Necessity follows from v_a omega_mu^a_b v^b=0 by antisymmetry. For sufficiency, the displayed first term is eta-antisymmetric and applied to v equals u_mu - v (u_mu·v)/v²=u_mu. The difference of any two solutions annihilates v. For timelike v, its stabilizer is so(3), of dimension three per mu: twelve independent smooth local functions. For spacelike v, the stabilizer is so(1,2), still three per mu; the null case is EXCLUDED because division by v² fails and requires separate treatment.

Geometric form of the compatibility equation:
v·e_mu = [partial_mu(v²)]/[2 sqrt(N0)].
This is an extra integrability/representation constraint on (v,e) within this branch, NOT a new fundamental axiom.

The corresponding torsion is T^a=de^a+omega^a_b ∧ e^b, and changing C preserves v,e,g but shifts T by C∧e exactly. This theorem *constructs* all local Lorentz connections compatible with a given restricted vector carrier and tetrad, completing the interpretation of #759/#763. This does not establish compatibility for arbitrary candidate pairs (v,e), nor does it show that all 12 differences survive full Theta dynamics and gauge reduction.

**Implication for H and graviton.** There is no unique functional omega[v,e] or T[v,e] from these kinematic equations. An exact torsion selector or a physical equivalence quotient and a genuine action remain indispensable to define the reduced E-L operator, symplectic current, Hamiltonian and TT wave propagation. The general canonical two-sided Theta, psi, and holomorphic constraints are untouched.

**Verification.** A nontrivial timelike v=(2,1,0,0), u=(1,2,0,0) with eta=(-,+,+,+) has v²=-3 and v·u=0; the formula yields the nonzero Lorentz boost omega^0_1=omega^1_0=1. Regression verifies existence, necessity, nonzero connection, Lorentz algebra and 3-dimensional stabilizer rank.
