<!-- BILINGUAL-UNIT: torsion_connection_rank -->
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


# Exact 24×24 linear contortion-to-torsion rank check

**Exact pointwise linear algebra at a fixed Minkowski tetrad; 2026-10-25. Not a dynamical torsion selector or a fundamental Hamiltonian.**

Take metric signature \(\eta_{ab}=(-,+,+,+)\), fix the orthonormal tetrad \(e_\mu{}^a=\delta_\mu{}^a\), and write a metric-compatible spin-connection perturbation \(\delta\omega_{\mu ab}=-\delta\omega_{\mu ba}\). There are 4×6=24 independent components, as in #742.

At fixed tetrad, the first Cartan structure equation linearizes to
\[
\delta T^a{}_{\mu\nu}=\delta\omega_\mu{}^a{}_\nu-\delta\omega_\nu{}^a{}_\mu,\quad \mu<\nu.
\]
Use ordered connection columns \((\mu,a,b)\) with \(a<b\), torsion rows \((a,\mu,\nu)\) with \(\mu<\nu\), and \(\omega_\mu{}^a{}_\nu=\eta^{aa}\omega_{\mu a\nu}\). The resulting exact rational 24×24 matrix \(M\) has
\[
\boxed{\operatorname{rank} M=24,\quad \det M=16.}
\]
The determinant depends on basis normalization/orientation; nonzero determinant and rank are the invariant statements. This explicitly verifies the local isomorphism at a fixed tetrad between torsion and metric-compatible contortion. For arbitrary nondegenerate tetrads this is carried by invertible frame transformations.

**Critical logical direction:** given torsion, unique connection; **not** given geometry, selected torsion. To determine the latter from a single Theta, UBT still needs a genuine algebraic or differential torsion constraint obtained from the dynamics or a separately justified selection principle. Such a constraint must remain compatible with the implicit E_mu=N0^(-1/2)D_mu Theta relation, gauge identities and the desired GR limit. In the torsion-free generated-tetrad branch the canonical repo documents a non-flat Schwarzschild obstruction; setting T=0 is not a free resolution of that issue.

The matrix check does not show that any arbitrary a_mu,b_mu of #741 is a valid composite connection; admissibility additionally requires the locked two-sided action and no independently propagating connections.

Verification: tests/test_torsion_connection_matrix_rank.py uses exact integer matrices with SymPy; independent computation produced rank 24 and determinant 16.
