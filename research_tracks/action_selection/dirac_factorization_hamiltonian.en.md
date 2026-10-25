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

# Dirac factorization as a Hamiltonian-first selection test for UBT

**Status: exact conditional linear-algebra result; not a derived unique UBT Hamiltonian.** One fundamental field remains Theta in Mat(2,C). This compares to the candidate 8-real symplectic construction of draft #717 and quadratic-gradient flow of #718.

## Two-component obstruction
With Hermitian Pauli matrices σ_i, a two-component massless Weyl operator h=σ·p squares to |p|² I₂. But there is no nonzero 2×2 complex matrix β such that {β,σ_i}=0 for all three i and β²=I₂. Indeed β=a I₂+Σ b_i σ_i: {β,σ_j}=2a σ_j+2b_j I₂=0 implies a=b_j=0. Thus the **standard local constant-matrix massive Dirac factorization** cannot fit in a single irreducible two-component Weyl block.

## Four-complex-component factorization within Theta
Theta has four complex entries, so a *chosen* linear identification vec(Theta)=Ψ=(ψ_L,ψ_R) with two 2-spinors is dimensionally available, without a new fundamental field. On prescribed flat spacetime define
\[
H_D(\mathbf p)=\begin{pmatrix}-c\,\sigma\cdot\mathbf p&mc^2 I_2\\mc^2 I_2&c\,\sigma\cdot\mathbf p\end{pmatrix}
=c\,\alpha^i p_i+\beta mc^2.
\]
Direct multiplication gives
\[
\boxed{H_D^2=(c^2|\mathbf p|^2+m^2c^4)I_4};
\quad \alpha_i^\dagger=\alpha_i,\ \beta^\dagger=\beta.
\]
Thus iℏ∂tΨ=H_DΨ has relativistic dispersion E=±sqrt(c²p²+m²c⁴). This is a **factorization candidate**, not the origin of its mass scale, c, ℏ, tetrad, or gauge constraints. Flattening the matrix Theta into a spinor does not by itself show covariance under the *locked* UBT congruence representation X→e^{iφ} SXS†: its vectorized transformation generally differs from the Dirac spinor representation S⊕(S†)^(-1). An explicit intertwiner or a justified symmetry reduction is mandatory before calling H_D a UBT operator.

## Critical symplectic compatibility
The earlier candidate Ω_B(X,Y)=B(X,iY), with B signature (2,6), is **not automatically** the standard positive Dirac inner-product symplectic form Im Ψ†Φ. The usual Schrödinger equation with Hermitian H_D is Hamiltonian with the latter positive pairing, but that pairing is not invariant under arbitrary nonunitary Lorentz congruence. Do not silently replace Ω_B by it, nor claim the Dirac operator is Hamiltonian with Ω_B. The compatibility equation K A=A†K for the relevant K (and chosen action convention) must be tested explicitly, including the symplectic form, field representation and constraints.

**Next falsification gate:** determine if a first-order spatial symbol A(p) exists on Theta which simultaneously (i) transforms covariantly under the canonical UBT representation, (ii) generates flow with Ω_B after imposing justified constraints, and (iii) squares to the Lorentzian mass shell. If not, record a precise representation/positivity obstruction instead of adding arbitrary fields.

Checks: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_dirac_factorization.py' -v\`.
