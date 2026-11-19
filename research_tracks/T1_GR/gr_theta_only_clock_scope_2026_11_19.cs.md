<!-- BILINGUAL-UNIT: gr-theta-only-clock-scope-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Explicit algebraic scope test, not a selected UBT time or graviton dynamics.
UBT-AI-PROVENANCE-END
-->
# Invarianty úplného biquaternionu samy neurčují univerzální hodiny Theta

<!-- UNIT: scope -->
## Axiomy a rozsah globálních hodin

Výhrada k předchozímu postupu je oprávněná: FLRW/synchronní hodiny byly **zvoleným srovnávacím ansatzem**, nikoli odvozenou kosmologickou historií. Audit se vrací k obecnému maticovému vyjádření Theta a stávajícím symetriím potenciálové větve. Netvrdíme fyzikální hodiny celé UBT, výběr reality ani akci; klasická centrální metrika musí zůstat určena kanonickým axiomem C, nikoli novou stopou či reálnou projekcí.

<!-- UNIT: orbit -->
## Neutrální invarianty samy nevyberou reálné Lorentzovy hodiny

The locked fundamental object is a full biquaternion \(\Theta\in\mathbb B\simeq\operatorname{Mat}_2(\mathbb C)\) with four complex (eight real) coefficients, and the locked spacetime geometry is a Lorentz-real **first jet** \(E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\in W_L\) only in its admitted classical sector. The background coordinate \(\tau=t+i\psi\) is already in Axiom B. Therefore a scalar extracted from a timelike projection \(X\) is not a derivation of fundamental time or a universal physical clock.

The existing polynomial-potential calculation uses the action
\[
X\longmapsto e^{i\alpha}SXS^\dagger,\quad S\in SL(2,\mathbb C),
\quad
H(X)=\operatorname{Tr}(X^\sharp X^\dagger),\quad D(X)=|\det X|^2.
\]
Here \(X^\sharp=\operatorname{adj}X\) in the faithful \(2\times2\) representation, NOT Hermitian conjugation. The already classified real potential through degree four depends on \(H,H^2,D\). On an anti-Hermitian Lorentz-real carrier \(X^\dagger=-X\) one has
\[
H(X)=-2\det X,\qquad D(X)=H(X)^2/4.
\]
The particular timelike clock expression \(T_H=\sqrt{H/(2\mathcal N_0)}\) agrees there with \(T=\sqrt{-X^2/\mathcal N_0}\), but this does not make the clock identity valid at generic complex \(\Theta\) values.

**Exact same-orbit witness.** Choose
\[
X_0=i\sqrt2\,I_2,\quad
S=\operatorname{diag}(2^{1/4},2^{-1/4}),\quad
X_1=\operatorname{diag}(2,1)=-i\,SX_0S^\dagger.
\]
Then \(\det S=1\) and
\[
H(X_0)=H(X_1)=4,\quad D(X_0)=D(X_1)=4,\quad
X_0^\dagger=-X_0,\quad X_1^\dagger=X_1.
\]
Thus a **single orbit of the declared potential-sector group** contains a Lorentz-real and a non-Lorentz-real carrier. No invariant function on that full group orbit (polynomial or not) can distinguish the two. The criterion \(D=H^2/4\) also does not characterize the Lorentz-real branch by itself.

**Phase-metric caveat from existing work.** The canonical sharp metric is complex-bilinear:
\[
g_{\mu\nu}I_2=\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu),\quad
g_{\mu\nu}[e^{i\alpha}E]=e^{2i\alpha}g_{\mu\nu}[E].
\]
Hence a continuous scalar central phase as multiplication of E is *not* a physical gauge redundancy preserving the unchanged real central metric. We use the declared potential-sector orbit solely to disprove selection of W_L from its neutral value invariants; we DO NOT assert both orbit representatives are gauge-equivalent physical metrics. This phase incompatibility was established before this note.


<!-- UNIT: constant -->
## Překážka univerzálních hodin: konstantní Theta se split-jet konexí

There is a further independent obstruction to promoting every \(\Theta\)-**value** scalar into a universal unit-gradient clock. In the previously documented independent split-jet *comparison* (not the pure Lorentz spin-lift), there are regular coframes with constant value \(\Theta=iI_2\). For example, with \(\mathcal N_0=1\) and auxiliary split-jet one-forms chosen to realize the coframe, take
\[
\Theta=iI_2,\quad
e^0=dt,\quad e^j=(1+t^2)\,dx^j,\quad
g=-dt^2+(1+t^2)^2d\mathbf x^2.
\]
Then \(H(\Theta)=2\), so \(T_H=\sqrt{H/(2\mathcal N_0)}=1\) and \(dT_H=0\) although \(g\) is nondegenerate. Consequently
\[
g^{-1}(dT_H,dT_H)=0\ne-1.
\]
This is an OFF-SHELL kinematic counterexample in a specifically declared split-jet class; it does not establish that constant \(\Theta\) satisfies the as-yet unknown fundamental UBT Euler equations. Nor does it contradict the earlier pure metric-compatible Lorentz-vector theorem, whose allowed connections enforce \(X\cdot e=\frac1{2\sqrt{\mathcal N_0}}d(X^2)\), excluding the displayed constant-X coframe.

The full dynamical theory might select a timelike branch, a field-jet/holonomy clock, or observer-dependent clocks, but no such global selection follows from the known low-degree invariant potential or the canonical kinematic axioms. In particular any globally smooth time with a unit gradient is a further *branch hypothesis*, not evidence that a closed compact spacetime is dynamically forbidden by UBT.


<!-- UNIT: decision -->
## Co musíme odvodit dále

Nejprve je nutné určit fyzikálně správné transformace úplného dvoustranného biquaternionového jetu a dokázat dynamické zachování či výběr reálné Lorentzovy metriky; samotné H a D to neumějí. Pak musíme z jediné mikroskopické akce Theta odvodit selektor fyzikální torze a relativní konexe. Teprve potom lze ověřit, zda časupodobné hodiny přežijí úplné Eulerovy rovnice, jejich vazby a sektor imaginárního času psi. Pokud se univerzální hodiny nevyberou, není pozorovatelsky lokální čas rozporem. Již známý mimetický test upozorňuje, že předčasné zafixování jednotkových hodin může zavést zachovávaný prachový mód místo GR. Návaznost: canonical/AXIOMS.md A–D; research_tracks/action_selection/theta_potential_invariants.cs.md; research_tracks/action_selection/phase_central_metric_compatibility.cs.md; research_tracks/action_selection/theta_unit_clock_mimetic_constraint.cs.md; research_tracks/action_selection/physics_closure_bare_action_2026_10.cs.md. Přesný symbolický test: tools/verify_gr_theta_only_clock_scope_2026_11_19.py. Úplné on-shell/globální/Lean závěry NEDOKÁZÁNY.
