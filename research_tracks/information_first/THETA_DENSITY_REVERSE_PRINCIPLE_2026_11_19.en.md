<!-- BILINGUAL-UNIT: theta-density-reverse-principle-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional reverse-engineering; operational measurement and quadratic weighting are not derived from the canonical UBT action.
UBT-AI-PROVENANCE-END
-->
# Reverse-engineering a positive quantum density from one full Theta: conditional uniqueness

<!-- UNIT: scope -->
## Precise reverse-engineering target

Goal: determine the weakest *additional* observer/information postulates which force the already proposed positive density rho_N from one full biquaternion Theta, rather than silently importing it from standard QM. None of these postulates is a new locked UBT axiom; the physical fundamental action and Born measurement law are still absent. Theorem statements below are conditional standard mathematical identities.

<!-- UNIT: trace -->
## Positive additive operational response forces trace representation

Let a calibrated observer's proposed local measurement effects be the ordered set
\[
\mathcal E=\{M\in M_2(\mathbb C):M=M^\dagger,\;0\le M\le I_2\}.
\]
Assume a **noncontextual** effect probability assignment \(p(M)\in[0,1]\), normalized by \(p(I_2)=1\), and additive over effects representing mutually exclusive alternatives in a complete POVM. In finite dimension, the generalized effect version of Gleason's theorem (Busch, Phys. Rev. Lett. 91, 120403 (2003), DOI 10.1103/PhysRevLett.91.120403) gives a unique density matrix \(\rho\ge0\), \(\operatorname{tr}\rho=1\), such that
\[
\boxed{p(M)=\operatorname{tr}(\rho M).}\tag{A}
\]
Equivalently, assume a positive unital *linear functional* \(\omega:M_2(\mathbb C)\to\mathbb C\). On matrix units \(E_{ij}\), define \(\rho_{ji}:=\omega(E_{ij})\). Then \(\omega(M)=\operatorname{tr}(\rho M)\) by linearity, \(\operatorname{tr}\rho=\omega(I)=1\), and positivity on \(vv^\dagger\) gives \(v^\dagger\rho v\ge0\), proving \(\rho\ge0\). Uniqueness follows from the matrix-unit basis.

**Important dimension gate:** the usual projection-only Gleason theorem assumes Hilbert-space dimension at least three; here the model is \(2\times2\), so the additional POVM/effect assumption or explicitly positive linear functional is ESSENTIAL. This standard result shows why the TRACE represents an operational probability state, not why UBT dynamics has the required effect algebra, additivity or noncontextuality. All those premises must eventually be derived/justified.

<!-- UNIT: quadratic -->
## Conditional uniqueness of the quadratic Theta Gram response

Return to the canonical ONE field \(\Theta\in\mathbb B\simeq M_2(\mathbb C)\) without changing Axiom A or the Axiom C central-sharp metric. Reuse the existing observer reference \(N=N^\dagger>0\), \(\det N=1\), selected from a future-timelike direction of the already-derived physical tetrad, and set
\[
T_N=N^{-1/2}\Theta N^{-1/2}.
\]
Propose the following **candidate observer-local quadratic support principle** for an *unnormalized* response matrix \(Q(T)\) before defining a density:
1. \((1,1)\)-quadratic response: every \(Q_{ab}(T)\) is linear in \(T_{i\alpha}\) and antilinear in \(\overline{T}_{j\beta}\); it is local and continuous;
2. positivity, nonzero response for \(T\ne0\);
3. covariance under \(T\mapsto UT\), \(Q\mapsto UQU^\dagger\) and invariance under a basis change \(T\mapsto TV\) of **unresolved right channels**, for \(U,V\in U(2)\);
4. support/no invented signal: whenever an orthogonal output projector \(\Pi\) satisfies \(\Pi T=0\), then \(\operatorname{tr}(\Pi Q(T))=0\).

**Conditional uniqueness theorem.** By \(U(2)\times U(2)\) invariant tensor contraction, the general sesquilinear equivariant response in \(M_2(\mathbb C)\) is
\[
Q(T)=a\,TT^\dagger+b\,\operatorname{tr}(TT^\dagger)I_2,\qquad a,b\in\mathbb R.
\]
For \(T=\operatorname{diag}(1,0)\) and \(\Pi=\operatorname{diag}(0,1)\) the support condition gives \(\operatorname{tr}(\Pi Q)=b=0\). Nonzero positivity then requires \(a>0\). Thus
\[
\boxed{
Q(T_N)=a T_NT_N^\dagger,\quad
\rho_N=\frac{Q(T_N)}{\operatorname{tr}Q(T_N)}
=\frac{T_NT_N^\dagger}{\operatorname{tr}(T_NT_N^\dagger)}.
}\tag{B}
\]
The arbitrary overall \(a>0\) cancels. Inserting (B) into (A) yields for any effect \(M\)
\[
\boxed{
p_N(M\mid\Theta)=
\frac{\operatorname{tr}(T_N^\dagger M T_N)}
{\operatorname{tr}(T_N^\dagger T_N)}.
}\tag{C}
\]
The trace and Gram form are therefore consequences **within these explicit proposed assumptions**; they are not yet consequences of the locked microscopic UBT axioms. The independently postulated quadraticity and effect probability requirements carry substantial QM content. In particular, right-unitary blindness belongs to ONE observer readout; it must not be promoted to a symmetry of the canonical action or all other observer readouts.

**Why no-signal support is needed.** Merely preserving pure rank-one states does NOT eliminate the alternative \(Q(T)=\operatorname{tr}(TT^\dagger)I-TT^\dagger\), which produces the *orthogonal* pure state for any rank-one \(T\) in dimension two. It violates the no-signal support condition.

<!-- UNIT: gaps -->
## Alternative powers, adjoints, and covariance gates

**Uniqueness requires genuine assumptions, not numerology.** Even with positivity, left/right unitary covariance, support and rescaling invariance of the *normalized* state, the family
\[
\rho_N^{(p)}
=\frac{(T_NT_N^\dagger)^p}
{\operatorname{tr}[(T_NT_N^\dagger)^p]},\qquad p>0,
\]
is algebraically admissible. For \(T_N=\operatorname{diag}(2,1)\), \(p=1\) gives \(\operatorname{diag}(4/5,1/5)\) but \(p=2\) gives \(\operatorname{diag}(16/17,1/17)\). Only the explicit unnormalized (1,1)-quadratic-response postulate selects \(p=1\). It should be sought as a conserved positive quadratic current or a constrained microscopic response, not announced as a new UBT theorem.

**Sharp versus dagger is indispensable.** Canonical geometric quaternion conjugation satisfies \(\Theta^\sharp\Theta=(\det\Theta)I\) and is complex-bilinear, not positive. For \(\Theta=\operatorname{diag}(1,i)\), it equals \(iI\), which is not Hermitian. Positivity instead requires the observer *-algebra and \(\dagger\) (or a dynamically derived equivalent). The positive \(N\) is a reference derived conditionally from admissible Lorentz geometry, not a second fundamental propagating field. The geometry is STILL the locked central-sharp metric of \(D_\mu\Theta\): no trace/reality redefinition is proposed.

**Conditional Lorentz covariance.** Under \(\Theta'=S\Theta S^\dagger\), \(N'=SNS^\dagger\), \(S\in SL(2,\mathbb C)\), the induced \(U=N'^{-1/2}SN^{1/2}\) is unitary and \(T_{N'}'=UT_NU^\dagger\). Hence \(\rho_{N'}'=U\rho_NU^\dagger\) and \(p_{N'}(UMU^\dagger\mid\Theta')=p_N(M\mid\Theta)\). This is an algebraic property of the declared observer protocol, not the physical selection of \(N\) or its measurement instrument.

<!-- UNIT: pure -->
## Pure state values and regular gravitational geometry

For nonzero \(T_N\), (B) gives
\[
\boxed{
\rho_N^2=\rho_N\iff\operatorname{rank}T_N=1
\iff\det\Theta=0\quad(\Theta\ne0,\ N>0).
}\tag{D}
\]
The last equivalence uses invertible \(N\). A rank-one pure OBSERVER READOUT therefore corresponds to singular **field value** \(\Theta\), but need not mean singular canonical tetrad. One explicit flat off-shell family (with \(\mathcal N_0=1,N=I,D_\mu=\partial_\mu\)) is
\[
\Theta_\lambda(t,x,y,z)
=\operatorname{diag}(1,\lambda)
+i(tI+x\sigma_1+y\sigma_2+z\sigma_3),\quad
E_\mu=i\sigma_\mu,\quad g=\eta,\quad \det g=-1.
\]
At the coordinate origin
\[
\rho_\lambda(0)=
\frac{\operatorname{diag}(1,\lambda^2)}{1+\lambda^2},
\quad \rho_1=I/2,\quad\rho_0=\operatorname{diag}(1,0).
\]
This is a continuous KINEMATIC interpolation from a mixed readout to a pure readout with the SAME nondegenerate classical Minkowski metric. It does NOT show a measurement outcome, a Born-distributed jump, a stable on-shell solution or a physical collapse. It does show that the potential \(\det\Theta=0\) issue and canonical \(\det g=0\) are distinct.

**No proof of UBT quantum mechanics yet.** Axiom C supplies the Lorentz-real first jet in its classical sector, but the fundamental action is unfinished. To make the proposed principle non-ad-hoc, derive: (i) observer effects and the relevant positive *-involution from a selected local causal/measurement algebra; (ii) a local conserved quadratic response/current from ONE \(\Theta\), rather than imposing it; (iii) the zero-support principle and positivity from the physical detector coupling; (iv) a dynamical outcome instrument and composition rule, not merely probabilities; (v) preservation of tetrad reality/rank, Hamiltonian constraints and \(\psi\)-sector stability. Without these derivations, this is a transparent reverse-engineering **target**, not a QM derivation.

Relation to established results: Busch, Phys. Rev. Lett. 91, 120403 (2003), DOI 10.1103/PhysRevLett.91.120403; existing UBT observer protocol in research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md; locked axioms in canonical/AXIOMS.md. Focused exact checker: tools/verify_theta_density_reverse_principle_2026_11_19.py; Python/SymPy local regression PASS.
