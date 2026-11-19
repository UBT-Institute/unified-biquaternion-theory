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
# Reverzní odvození kladné kvantové hustoty z jediného Theta: podmíněná jednoznačnost

<!-- UNIT: scope -->
## Přesný cíl reverzního odvození

Cíl: najít nejslabší *dodatečné* pozorovatelské a informační předpoklady, z nichž plyne naše dřívější kladná matice hustoty rho_N z jediného úplného biquaternionu Theta, místo jejího skrytého převzetí z QM. Žádný z těchto předpokladů není novým uzamčeným axiomem UBT; fundamentální fyzikální akce a zákon skutečného měření stále chybějí. Níže uvedené věty jsou podmíněné standardní matematické výsledky.

<!-- UNIT: trace -->
## Kladná aditivní odezva pozorovatele vynucuje reprezentaci stopou

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
## Podmíněná jednoznačnost kvadratické Gramovy odezvy Theta

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

<!-- UNIT: additivity -->
## Silnější věta: aditivita kanálů vynucuje kvadratické váhy

Odstraníme nejvíce libovolný předpoklad předchozího důkazu: místo postulování kvadratické pravděpodobnostní váhy ji odvodíme z konzistence při slučování nerozlišených kanálů. Výsledek je matematická věta o jednoznačnosti při výslovně uvedených operačních předpokladech, nikoli odvození skutečné fyziky měření v UBT.

Write \(T=[v_1\ v_2]\) in a fixed calibrated observer frame. Instead of assuming quadraticity, suppose a **single** unobserved channel \(v\in\mathbb C^2\) has an unnormalized matrix response \(q(v)\ge0\), with \(q(0)=0\), satisfying:
\[
q(Uv)=Uq(v)U^\dagger\quad(U\in U(2)),\qquad
\operatorname{ran}q(v)\subseteq\operatorname{span}\{v\}.
\]
Unitary covariance and support imply, for \(v\ne0\),
\[
\boxed{q(v)=h(s)\frac{vv^\dagger}{s},\quad s=v^\dagger v,\quad h(s)\ge0.}\tag{G}
\]
No power law or quadratic scaling is assumed. Now add two separate **operational assumptions**:
\[
\boxed{
Q([v_1\ v_2])=q(v_1)+q(v_2)
\quad\text{(additive unresolved channels)},}\tag{H}
\]
\[
\boxed{
Q(TV)=Q(T)\quad(V\in U(2))
\quad\text{(unobserved channel-basis invariance).}}\tag{I}
\]
For \(T=[v\ 0]\), a right-unitary rotation can split its first column into \((\cos\gamma)v\) and \((\sin\gamma)v\). Equation (I), evaluated through (H) and (G), forces
\[
h(s)=h(s\cos^2\gamma)+h(s\sin^2\gamma).
\]
For arbitrary \(x,y\ge0\) with \(s=x+y>0\), choose \(\cos^2\gamma=x/s\), \(\sin^2\gamma=y/s\). Then
\[
\boxed{h(x+y)=h(x)+h(y),\qquad h\ge0.}\tag{J}
\]
A nonnegative additive function on \(\mathbb R_{\ge0}\) is automatically monotone: \(y\ge x\Rightarrow h(y)-h(x)=h(y-x)\ge0\). Rational approximation then yields \(h(s)=cs\), \(c\ge0\), WITHOUT a separate continuity or degree assumption. Nonzero response gives \(c>0\). Hence
\[
\boxed{q(v)=c\,vv^\dagger,\quad Q(T)=c\,TT^\dagger.}\tag{K}
\]
This is a STRONGER **conditional** derivation than assuming a (1,1)-quadratic response at the outset. The only imposed response structure is additive unresolved channels, unitary basis blindness, output support and positivity; quadratic intensity follows.

**Explicit alternative-law failure:** \(q_p(v)=(v^\dagger v)^{p-1}vv^\dagger\) gives \(h(s)=s^p\). Under equal splitting \(v\mapsto(v/\sqrt2,v/\sqrt2)\), the sum in (H) changes by \(2^{1-p}\); for \(p=2\) it is halved. The globally right-unitary-invariant nonlinear map \(Q_p(T)=(TT^\dagger)^p\) is still possible, but it FAILS the separate decomposition rule (H) for generic \(T\). The assumptions are independent.

**Physical status:** This theorem does not show that the right index of a biquaternion matrix is a physically unresolved detector channel, or that its response should add incoherently, or that the detector effect algebra emerges from the UBT action. The right-unitary basis change is a symmetry of this *one proposed observer protocol*, not automatically of the microscopic \(\Theta\) action or of joint multi-clock comparisons. Precisely these operational hypotheses must be tested, not secretly called established UBT axioms. Exact finite regression: tools/verify_theta_density_channel_additivity_2026_11_19.py; the functional-equation proof above is analytic.

<!-- UNIT: gaps -->
## Alternativní mocniny, sdružení a kovariance

**Uniqueness requires genuine assumptions, not numerology.** Even with positivity, left/right unitary covariance, support and rescaling invariance of the *normalized* state, the family
\[
\rho_N^{(p)}
=\frac{(T_NT_N^\dagger)^p}
{\operatorname{tr}[(T_NT_N^\dagger)^p]},\qquad p>0,
\]
is algebraically admissible. For \(T_N=\operatorname{diag}(2,1)\), \(p=1\) gives \(\operatorname{diag}(4/5,1/5)\) but \(p=2\) gives \(\operatorname{diag}(16/17,1/17)\). Only the explicit unnormalized (1,1)-quadratic-response postulate selects \(p=1\). It should be sought as a conserved positive quadratic current or a constrained microscopic response, not announced as a new UBT theorem.

**Sharp versus dagger is indispensable.** Canonical geometric quaternion conjugation satisfies \(\Theta^\sharp\Theta=(\det\Theta)I\) and is complex-bilinear, not positive. For \(\Theta=\operatorname{diag}(1,i)\), it equals \(iI\), which is not Hermitian. Positivity instead requires the observer *-algebra and \(\dagger\) (or a dynamically derived equivalent). The positive \(N\) is a reference derived conditionally from admissible Lorentz geometry, not a second fundamental propagating field. The geometry is STILL the locked central-sharp metric of \(D_\mu\Theta\): no trace/reality redefinition is proposed.

**Conditional Lorentz covariance.** Under \(\Theta'=S\Theta S^\dagger\), \(N'=SNS^\dagger\), \(S\in SL(2,\mathbb C)\), the induced \(U=N'^{-1/2}SN^{1/2}\) is unitary and \(T_{N'}'=UT_NU^\dagger\). Hence \(\rho_{N'}'=U\rho_NU^\dagger\) and \(p_{N'}(UMU^\dagger\mid\Theta')=p_N(M\mid\Theta)\). This is an algebraic property of the declared observer protocol, not the physical selection of \(N\) or its measurement instrument.

<!-- UNIT: topological-p -->
## Stejná topologická fáze, odlišné nelineární pravděpodobnostní váhy

**A topological invariant cannot select the Born exponent.** Reuse the rank-one projector family \(P(\theta,\varphi)\) on the auxiliary parameter sphere from the previous UBT phase-transport note, and let \(Q_P=2P-I_2\). For \(\beta>0\), choose a positive invertible full-biquaternion observer amplitude \(T_\beta=\exp(\frac{\beta}{2}Q_P)\). The family of alternative normalized response laws gives
\[
\boxed{
\rho_\beta^{(p)}
=\frac{(T_\beta T_\beta^\dagger)^p}
{\operatorname{tr}[(T_\beta T_\beta^\dagger)^p]}
=\tfrac12[I_2+\tanh(p\beta)Q_P],\qquad p>0.
}\tag{F}
\]
All these laws have the SAME nondegenerate higher-eigenvalue projector \(P\), hence the SAME standard eigenline Berry curvature and Chern number \(c_1(P)=1\), but their probabilities differ. Therefore even the previously found integer Berry/Chern invariant cannot determine \(p=1\) or Born's rule. The choice of quadratic unnormalized response is an independent unresolved physical task, not forced by phase topology.

<!-- UNIT: pure -->
## Čisté stavové hodnoty a regulární gravitační geometrie

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
