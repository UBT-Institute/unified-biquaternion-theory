<!-- BILINGUAL-UNIT: theta-purification-composition-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Purification and operator-composition mathematics only; the physical tensor split, on-shell quantization, Born instrument and gravity constraints remain OPEN.
UBT-AI-PROVENANCE-END
-->
# Jediné úplné Theta, purifikovaná hustota pozorovatele a chybějící fyzikální tenzorový zákon

<!-- UNIT: scope -->
## Cíl: odvodit stopu bez přidání druhého pole

Navazujeme na podmíněný důkaz jednoznačnosti: přímo ukážeme, jak jedno původní úplné Θ poskytne dvouindexovou amplitudu, jak ignorování indexu vede ke kandidátní hustotě a které fyzikální předpoklady nadále chybějí. Jde o maticovou identitu a srovnávací model měření, nikoli dokončenou kvantovou dynamiku UBT.

<!-- UNIT: purification -->
## Jediný biquaternion jako podmíněná purifikace pozorovatelského stavu

For the already DECLARED candidate observer reference \(N=N^\dagger>0\), define \(T_N=N^{-1/2}\Theta N^{-1/2}\in M_2(\mathbb C)\) and its four-component **vectorization**
\[
\boxed{|T_N\rangle\rangle=\sum_{i,j=0}^{1}(T_N)_{ij}|i\rangle_A|j\rangle_B
\quad\in\mathbb C^2\otimes\mathbb C^2.}\tag{A}
\]
The two labels \(A,B\) are at this stage mathematical matrix indices, NOT demonstrated separate particles, detectors, causally independent regions or a new fundamental field. The positive Hilbert norm requires the **observer-selected Hermitian involution** \(\dagger\), NOT the canonical complex-bilinear gravitational sharp.

For \(T_N\ne0\), normalize \(|\Phi_N\rangle=|T_N\rangle\rangle/\sqrt{\langle\langle T_N|T_N\rangle\rangle}\); then
\[
\langle\langle T_N|T_N\rangle\rangle=\operatorname{tr}(T_N^\dagger T_N),
\]
\[
\boxed{
\operatorname{Tr}_B(|\Phi_N\rangle\langle\Phi_N|)
=\frac{T_NT_N^\dagger}{\operatorname{tr}(T_NT_N^\dagger)}
=\rho_N.}\tag{B}
\]
Proof by matrix entries: \((\operatorname{Tr}_B|\Phi\rangle\langle\Phi|)_{ik}=\sum_j (T_N)_{ij}\overline{(T_N)_{kj}}/\operatorname{tr}(T_N^\dagger T_N)\). This is a UNIQUE finite-dimensional algebraic identity for the **CHOSEN** factorization. It is not yet an ontic claim that UBT contains a second physical subsystem \(B\).

This makes the trace a partial trace of one amplitude over an **assumed unresolved index**, not a free numerical normalization trick. The interpretation of that index, positivity and Hilbert tensor product are the actual undetermined physical assumptions.

<!-- UNIT: filter -->
## Kvadratické filtrační odezvy: kde se stále předpokládá Bornovo pravidlo

Given a positive hypothetical detector effect \(0\le M\le I_2\) acting on the \(A\) index and a linear filter \(K\) satisfying \(K^\dagger K=M\), the **conditional relative transmitted quadratic response** is
\[
\boxed{
p(M|T_N)=\frac{\|(K\otimes I_2)|T_N\rangle\rangle\|^2}
{\||T_N\rangle\rangle\|^2}
=\frac{\operatorname{tr}(T_N^\dagger M T_N)}
{\operatorname{tr}(T_N^\dagger T_N)}
=\operatorname{tr}(\rho_NM).}\tag{C}
\]
For example take \(M=\operatorname{diag}(1/4,3/4)\), \(K=\operatorname{diag}(1/2,\sqrt3/2)\). The two effects \(M\) and \(I_2-M\) sum to identity and have total transmitted fraction \(1\). Exact SymPy calculation with \(T_N=\begin{psmallmatrix}1&2+i\\3-i&4\end{psmallmatrix}\) gives \(p(M)=21/32\).

If an outcome is **postselected**, the normalized filtered \(A\)-state is the usual conditional map \(K\rho_NK^\dagger/\operatorname{tr}(M\rho_N)\). But no physical detector or dynamically stochastic outcome is supplied by the mathematical identity (C): assuming a positive Hilbert norm and a linear effect filter already assumes substantial QM structure. Neither \(\sqrt M\), outcome probabilities in repeated experiments, detector-pointer decoherence, nor actual collapse is derived from the locked UBT action.

<!-- UNIT: phase -->
## Lokálně skrytá fáze SU(2) a společná dvouindexová korelace

A small exact phase witness illustrates what one observer cannot see. Let
\[
\Theta_+=I_2,\qquad\Theta_-=i\sigma_3,\qquad N=I_2.
\]
Both are full invertible biquaternions and \(\Theta_-= \Theta_+ (i\sigma_3)\) with the right factor in \(SU(2)\). Yet
\[
\boxed{\rho_I[\Theta_+]=\rho_I[\Theta_-]=\tfrac12 I_2.}\tag{D}
\]
Their normalized vectorizations are \(|\Phi_+\rangle=(|00\rangle+|11\rangle)/\sqrt2\) and \(|\Phi_-\rangle=i(|00\rangle-|11\rangle)/\sqrt2\). A **joint mathematical operator**, if physically available, distinguishes the relative phase:
\[
\boxed{
\langle\Phi_+|\sigma_1\otimes\sigma_1|\Phi_+\rangle=1,\qquad
\langle\Phi_-|\sigma_1\otimes\sigma_1|\Phi_-\rangle=-1.}\tag{E}
\]
Embedding each constant value \(B\in\{\Theta_+,\Theta_-\}\) in the SAME one-field affine jet
\[
\Theta_B(t,x,y,z)=B+i(tI_2+x\sigma_1+y\sigma_2+z\sigma_3)
\]
yields \(E_\mu=i\sigma_\mu\in W_L\) and the locked sharp \(g=\eta\) for **both configurations**, at every ordinary 4D point. The displayed \(\rho_I\) equality is asserted at the coordinate origin; away from it the readouts can differ. This is OFF-SHELL flat kinematics, not two selected full UBT solutions or an observed Bell experiment.

It is crucial that \(i\sigma_3\) is also one of the observer-blind right transformations that generally fail to preserve the entire Lorentz-real slice when applied to a **whole first jet**. The affine example instead changes only the x-constant value \(B\) and keeps \(E_\mu\) fixed; these transformations MUST NOT be conflated. Whether the difference in \(B\) is a physical observable or a hidden global/gauge direction requires a selected action and detector law.

<!-- UNIT: lorentz -->
## Kovariance formální purifikace při společné Lorentzově transformaci

Under the already proven joint Lorentz-spin/observer reference change
\[
\Theta'=S\Theta S^\dagger,\quad N'=SNS^\dagger,\quad
U=N'^{-1/2}SN^{1/2}\in SU(2),
\]
we have \(T_{N'}'=UT_NU^\dagger\). With the row-first vectorization convention,
\[
\boxed{
|T_{N'}'\rangle\rangle=(U\otimes\overline U)|T_N\rangle\rangle,\qquad
\rho_{N'}'=U\rho_NU^\dagger.}\tag{F}
\]
This supplies a consistent CANDIDATE observer frame transformation, where the two mathematical factors transform **correlatively**, not as two independently derived physical local gauge groups. Physical multi-observer synchronization and the connection needed for between-point comparison remain unspecified. The fixed canonical sharp-derived tetrad and the complex-time definition \(\tau=t+i\psi\) are not altered.

<!-- UNIT: composites -->
## Bez operační faktorizace nevznikne druhá nezávislá lokální maticová algebra

**The new compositional obstruction is not "a \(2\times2\) matrix cannot describe two-qubit entanglement."** As (A)–(E) show, the vector space \(M_2(\mathbb C)\simeq\mathbb C^4\) CAN be algebraically factorized as \(\mathbb C^2\otimes\mathbb C^2\) for an individual *pure* bipartite mathematical state. The issue is that the underlying **physical tensor-factor and local operator algebras are not selected by the canonical UBT axioms**. In particular, if one insists that two independent full qubit observable algebras live as commuting unital subalgebras INSIDE the same single \(M_2(\mathbb C)\) output algebra, this is impossible: any faithful embedded \(M_2(\mathbb C)\) is all of \(M_2(\mathbb C)\), whose commutant is just \(\mathbb C I_2\). Hence a second independent commuting copy cannot also fit there.

One may instead let left and right multiplication act on the **vectorized \(\mathbb C^4\)**, where the tensor algebra is \(M_2(\mathbb C)\otimes M_2(\mathbb C)\simeq M_4(\mathbb C)\). This is mathematically consistent but **an additional operational factorization**, not a physical discovery of two qubits from the one-field action. Its row/column split is frame/reference dependent and the full right-unitary family is not canonical Lorentz tetrad gauge.

Moreover a single pointwise \(\mathbb C^4\) amplitude cannot represent an arbitrary pure state of THREE independently addressable qubits (complex dimension \(8\)); multi-particle physics must use nonlocal/multimode quantum states, an appropriate Fock/operator construction, or other justified emergent compositional structures from the ONE spatially extended field \(\Theta\). This does NOT require extra fundamental classical fields, but DOES require a selected microscopic symplectic form, quantization, locality and causal commutativity.

Finally a deterministic classical map \(\Theta\mapsto\rho_N\) alone cannot select a genuinely random unique detector outcome. A dynamical measurement instrument (or a justified hidden-variable or branching account) and its probability calculus are independent missing parts.

<!-- UNIT: next -->
## Mikroskopická dynamika potřebná pro skutečnou kvantovou kompozici

**Concrete next derivation.** Fix an admissible full-\(\Theta\) microscopic action, identify its reduced physical phase space and symplectic two-form, and derive the fundamental positive observer representation. Then test whether two **spacelike separated smeared observable algebras** can be constructed with physically justified commutation/factorization rather than by arbitrarily labeling two matrix indices as particles. Only then derive the detector filter effect, frequencies, projection/update and Born weights without assuming the latter. Analyze the same canonical \(D_\mu\Theta\) Lorentz-real constraints, possible torsion, ghost/energy positivity and \(\psi\)-sector stability.

This note is NOT a claimed new proof of standard purification or Bell correlations. It is a scoped reverse-engineering result and a concrete **missing-physics gate** for UBT.

Earlier merged sources: canonical/AXIOMS.md, research_tracks/information_first/THETA_DENSITY_REVERSE_PRINCIPLE_2026_11_19.en.md, research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md. Existing draft predecessor: research_tracks/information_first/THETA_OPERATIONAL_ADDITIVITY_LORENTZ_GAUGE_GATE_2026_11_19.en.md. Checker: tools/verify_theta_purification_composition_gate_2026_11_19.py.
