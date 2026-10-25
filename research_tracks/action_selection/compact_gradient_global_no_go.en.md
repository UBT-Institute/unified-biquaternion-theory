<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: compact-gradient-global-no-go.provenance -->
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

# No compact spacelike slice from one global pure-gradient Lorentz tetrad

**Status: DERIVED_WITH_ASSUMPTIONS.** This is a classical global obstruction for the restricted single-field gradient branch, strengthening the local pure-boundary result in merged PR #680 and the local Dirac result in draft PR #682.

## Theorem: compact spatial section obstruction

Let \(\Sigma\) be a smooth compact boundaryless 3-manifold, embedded as a spacelike hypersurface in a 4-dimensional Lorentzian spacetime \(M\). Suppose there exist **single-valued global real fields**
\[
y=(y^0,y^1,y^2,y^3):M\longrightarrow\mathbb R^{1,3}
\]
with everywhere invertible derivative \(\det dy\ne0\) and a metric defined **exactly** by
\[
\boxed{g=y^*\eta,\qquad\eta=\operatorname{diag}(-1,1,1,1).}
\]
Then these assumptions are inconsistent: no such global \(y\) exists.

## Proof

Let \(f=y|_\Sigma:\Sigma\to\mathbb R^{1,3}\). Since the induced metric on \(\Sigma\) is positive definite, \(f\) is a spacelike immersion. Let the standard spatial projection be
\[
p:\mathbb R^{1,3}\longrightarrow\mathbb R^3,\qquad
p(z^0,z^1,z^2,z^3)=(z^1,z^2,z^3).
\]
For nonzero \(v\in T_x\Sigma\), assume \(d(p\circ f)_x(v)=0\). Then \(df_x(v)\) is either zero or purely timelike. It cannot be zero because \(\det dy\ne0\), and it cannot be timelike because \(g(v,v)>0\). Thus \(d(p\circ f)\) is injective and, by equal source/target dimensions, is an isomorphism at every point. The inverse function theorem says \(p\circ f:\Sigma\to\mathbb R^3\) is a local diffeomorphism. Its image is therefore open. Compactness of \(\Sigma\) makes that image compact, hence closed. A nonempty subset of connected \(\mathbb R^3\) that is both open and closed must be all of \(\mathbb R^3\), which is not compact. Contradiction.

Therefore
\[
\boxed{\text{global single-valued pure-gradient tetrad}
\quad\Longrightarrow\quad
\text{no compact spacelike spatial slice}.}
\]

## UBT consequence and limitations

The spherical Poincaré quotient \(\Sigma=S^3/(2I)\) is compact and boundaryless. Consequently the same **global single-valued** pure-gradient tetrad cannot provide its spacetime geometry, regardless of the choice of derivative-free potential. In particular, taking the exact local Dirac branch of PR #682 and imposing dodecahedral CMB eigenmodes cannot produce a globally consistent complete cosmology within those assumptions.

**This is not a theorem that curved UBT or a dodecahedral topology is impossible.** Local functions \(y\) defined only patchwise with nontrivial transition functions, an independent nontrivial two-sided connection, torsion, nonzero curvature and a different completed action fall outside the proof. Indeed compact flat spatial quotients with affine monodromy illustrate why global single-valued fields matter.

The result also does not select \(\Sigma=S^3/(2I)\) or provide a measured CMB signal. The observational status in the existing CMB track remains NO OBSERVATIONAL FIT.

**Standard geometric context:** the nonexistence of compact boundaryless spacelike immersions in Minkowski space is classical; the projection proof given here explicitly identifies the assumption that obstructs the **UBT gradient branch**. See https://www.researchgate.net/publication/295253182_Spacelike_Hypersurfaces_in_Lorentzian_Spacetimes .

**Next gap:** construct a nondegenerate, dynamically consistent curved composite tetrad with nontrivial connection and carry out the full constrained physical-mode Hamiltonian analysis before inferring primordial perturbations or a CMB power spectrum.
