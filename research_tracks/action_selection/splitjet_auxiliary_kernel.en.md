<!-- BILINGUAL-UNIT: splitjet_auxiliary_kernel -->
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


# Exact split-jet auxiliary kernel and off-shell shift redundancy

**C-tier structural result, 2026-10-24.** Adopted classical Palatini–HT gravity sector only; full microscopic UBT Hessian and Dirac algebra remain open.

Let q=sqrt(N0)>0, X^a timelike nonzero, and E_mu^a=q^-1(d_mu X^a+omega_mu^a_b X^b+K_J,mu^a_b X^b+w_mu X^a). For each fixed coordinate index mu, K_J,mu is Lorentz-antisymmetric (6 real components) and w_mu one real component. At timelike X=(r,0,0,0), r!=0, define columns z=(w, K^1_0,K^2_0,K^3_0,K^2_3,K^3_1,K^1_2). The exact Jacobian is
\[
J=\frac r q\begin{pmatrix}1&0&0&0&0&0&0\\0&1&0&0&0&0&0\\0&0&1&0&0&0&0\\0&0&0&1&0&0&0\end{pmatrix}.
\]
Rank 4; nullity 3. For four independent mu columns, the block-diagonal map has rank 16 and nullity 12. (These dimensions count auxiliary connection *components*, not 16 physical tetrad degrees of freedom; six further Lorentz frame directions are standard metric redundancies.)

**Exact off-shell property:** at fixed X and omega, a local shift δK_J satisfying δK_J^a_b X^b=0 and δw=0 leaves E and hence the *adopted gravity functional* unchanged identically. For timelike X the stabilizer is the spatial rotation algebra so(3) (dimension 3 per mu). Since E depends *linearly* on K_J, the finite shift K_J -> K_J+ΔK_J with ΔK_J X=0 is also an exact symmetry of this action sector, not merely an on-shell infinitesimal accident. In more general non-null frames the stabilizer still has dimension 3, isomorphic to so(3) or so(1,2) according to X's causal type. The shift is not necessarily a standard Lorentz gauge transformation of the full theory and may be broken if additional terms depend directly on K_J or its derivatives.

This gives a useful **off-shell auxiliary redundancy certificate**. It does *not* justify claiming twelve first-class Hamiltonian constraints: that requires independent canonical coordinates, primary constraints, consistency algorithm, possible boundary terms, and gauge-generator analysis. It also does not alter the standard two-mode ADM endpoint count or prove a physical Hamiltonian for Theta. The rank is valid only when X^2 != 0 and all 7 auxiliary component variations are independent, as declared by the local GR postulate.

**Next gate:** explicitly write the first-order presymplectic form in (Theta, omega, K_J,w,Lambda,C3) and show whether the 12 kernel shifts appear as first-class gauge generators after all primary/secondary constraints; track psi and source terms separately.

Check: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_splitjet_kernel.py' -v\` (SymPy).