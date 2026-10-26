<!-- BILINGUAL-UNIT: BARE_THETA_TT_PRINCIPAL_SYMBOL -->
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


# Conditional principal-symbol obstruction: bare Theta derivative carries no spatial TT metric wave

**2026-10-26, addition to integrated GRAVITON_HAMILTONIAN_GATE, PR #773.**
This is an exact *conditional principal-symbol* calculation, NOT a claim that full UBT has no graviton.

For the locked canonical two-sided derivative,
\[
\delta E_\mu=N_0^{-1/2}
(D_\mu\delta\Theta+\delta A_\mu\,\bar\Theta-\bar\Theta\,\delta B_\mu).
\]
Its metric variation, in Lorentz tetrad components, is \(\delta g_{\mu\nu}=\eta_{ab}(\bar e_\mu^a\,\delta e_\nu^b+\delta e_\mu^a\,\bar e_\nu^b)\).
On a locally orthonormal background tetrad \(\bar e_\mu{}^a=\delta_\mu{}^a\), consider Fourier perturbations with nonzero spatial wavevector k. If the *composite connection response* \(\delta A,\delta B\) contributes no term of the same (or higher) derivative order in the linearized tetrad principal symbol, the bare \(\partial_\mu\delta\Theta\) yields an effective vector-symbol \(ik_\mu u^a\) in the real Lorentz slice, and
\[
\sigma(\delta g_{ij})=i(k_i u_j+k_j u_i).
\]
For \(P_{ij}=\delta_{ij}-\hat k_i\hat k_j\), \(\Lambda(H)=PHP-\frac12 P\,\operatorname{tr}(PH)\) on symmetric spatial matrices. Since \(Pk=0\),
\[
\boxed{\Lambda(\sigma(\delta g))=0}.
\]
This holds for every u, every nonzero spatial k. In particular a bare-gradient/velocity-independent-algebraic connection *cannot provide a leading spatial TT symbol by itself*. Lower order terms may generate nonzero TT metric components, and this algebraic result alone does NOT decide their propagation or on-shell dynamics.

**Critical condition:** if the true composite closure has \(\delta A_\mu[\Theta]\) or \(\delta B_\mu[\Theta]\) involving derivatives of \(\delta\Theta\) at the same or higher principal order, or if connection reconstruction yields a higher-derivative differential operator, the hypothesis fails. A nonzero background connection contributes lower-order matrix terms when varied at fixed connection but may change physical characteristic multiplicities via full coupled constraints. The full two-sided, nonzero torsion closure must be derived rather than frozen or declared zero.

**Positive proof obligation:** compute \(\sigma(\delta A[\Theta]),\sigma(\delta B[\Theta]),\sigma(\delta T[\Theta])\) from a selected composite law. Verify that the induced two-dimensional TT image has full rank at generic k, and separately that the physical reduced quadratic action yields wave propagation, first-class constraints, correct helicities, positive energy, and no ghost.

Test: tests/test_bare_theta_tt_principal_symbol.py checks the TT vanishing for arbitrary symbolic u with k parallel to z and independently rank-zero map from u to the two TT components. This is a concrete obstruction test within the unique single-Theta theory, not an adopted GR action.
