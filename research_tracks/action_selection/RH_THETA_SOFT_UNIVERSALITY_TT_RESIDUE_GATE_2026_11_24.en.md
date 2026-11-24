<!-- BILINGUAL-UNIT: rh-theta-soft-universality-tt-residue-2026-11-24 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional soft and tensor propagator comparators, no derived physical Theta S-matrix or action.
UBT-AI-PROVENANCE-END
-->
# Universality of soft gravitons, trace-sector exchange, and physical TT residue: RH-to-UBT acceptance gate

**24 November 2026 — exact L0 conditional benchmark, C_working; physical one-Theta graviton NOT DERIVED.**

## Soft gauge decoupling forces equality of couplings across interacting species

Suppose the same emergent massless helicity-two particle appears as an asymptotic state in a Lorentz-invariant S-matrix with ordinary factorization of the leading soft emission pole. For stable hard external particle species with gravitational couplings \(g_i\), Weinberg's leading soft formula and the pure-gauge decoupling condition give:
\[
\mathcal M_{n+1}(q,\varepsilon)\xrightarrow{q\to0}
\left(\sum_{i=1}^{n}\eta_i g_i
\frac{p_i^\mu p_i^\nu\varepsilon_{\mu\nu}}{p_i\cdot q}\right)\mathcal M_n
+O(q^0),\qquad \eta_{\rm in}=-1,\ \eta_{\rm out}=+1.\tag{1}
\]
\[
\varepsilon_{\mu\nu}\mapsto\varepsilon_{\mu\nu}+q_\mu\xi_\nu+q_\nu\xi_\mu,\qquad
\boxed{\sum_i \eta_i g_i p_i^\mu=0.}\tag{2}
\]
\[
p_{A,\rm in}=(E,0,0,k),\quad p_{B,\rm in}=(E,0,0,-k),\quad
p_{A,\rm out}=(E,k,0,0),\quad p_{B,\rm out}=(E,-k,0,0).\tag{3}
\]
\[
\boxed{\sum_i\eta_i g_i p_i^\mu=(g_A-g_B)(0,k,0,-k)^\mu,\qquad
k\ne0\ \Longrightarrow\ g_A=g_B.}\tag{4}
\]
\[
\mathcal A_0(q)\propto \frac{T_{\mu\nu}T'^{\mu\nu}-\frac12 TT'}{q^2},
\qquad
\mathcal A_m(q)\propto \frac{T_{\mu\nu}T'^{\mu\nu}-\frac13 TT'}{q^2+m^2}.\tag{5}
\]
\[
\boxed{\lim_{m\to0}\mathcal N_m-\mathcal N_0=\frac16TT',
\qquad \mathcal N_0=T:T'-\frac12TT',\quad \mathcal N_m=T:T'-\frac13TT'.}\tag{6}
\]
\[
P_{ij}=\delta_{ij}-\hat k_i\hat k_j,\qquad
(\Pi_{\rm TT}H)_{ij}=P_i{}^lP_j{}^mH_{lm}
-\frac12 P_{ij}P^{lm}H_{lm},\qquad \boxed{\operatorname{rank}\Pi_{\rm TT}=2.}\tag{7}
\]
\[
\varepsilon^+=\frac{1}{\sqrt2}\operatorname{diag}(1,-1,0),\qquad
\varepsilon^\times=\frac1{\sqrt2}
\begin{pmatrix}0&1&0\\1&0&0\\0&0&0\end{pmatrix},\qquad
\boxed{\|\Pi_{\rm TT}H\|^2=|H:\varepsilon^+|^2+|H:\varepsilon^\times|^2.}\tag{8}
\]
\[
\boxed{\langle h_{\rm TT} h_{\rm TT}\rangle(p)\sim
\frac{Z\,\Pi_{\rm TT}(p)}{p^2},
\quad Z>0\ \text{required for a positive pole norm in this comparator}.}\tag{9}
\]

The explicit elastic right-angle process (3) is a valid equal-mass on-shell witness for \(E^2>k^2>0\) and conserves total energy-momentum. By (4), a **single** graviton coupled to both interacting species requires \(g_A=g_B\). This follows for any nonzero momentum transfer and connected interacting sectors, not only for this witness. For disconnected sectors the argument need not compare couplings. The test is conditional: neither asymptotic scattering states nor a physical \(g_i\) have been derived for UBT, and merely having both species built from the same \(\Theta\) does not imply equal effective couplings.

## The massless tensor exchange has a different trace coefficient from a massive spin-two limit

For conserved stress sources \(q_\mu T^{\mu\nu}=q_\mu T'^{\mu\nu}=0\), the linear flat-space massless and Pauli–Fierz massive exchange numerators are (5). At common overall coupling normalization the difference in the massive \(m\to0\) numerator is (6), **not zero** for traceful matter. An exact conserved test source \(T=T'=\operatorname{diag}(1,0,0,0)\) with static spatial \(q=(0,0,0,1)\) gives
\[
\boxed{\mathcal N_0=\frac12,\qquad \lim_{m\to0}\mathcal N_m=\frac23,\qquad
\Delta\mathcal N=\frac16.}\tag{10}
\]
This is the linear vDVZ trace-sector discontinuity. It is not a no-go for all nonlinear massive gravity (screening may change applicability), but it prevents claiming a GR exchange amplitude solely from the existence of a **spin-two massless pole** in a scalar RPA bubble. Traceless sources cannot distinguish the two numerators by this test; independent traceful sources must be included. The numerator and source coupling must come from the same candidate \(\Theta\) action, not from an imported Palatini endpoint.

## The correct physical residue is a two-polarization positive TT form

At a fixed **nonzero** spatial momentum direction, (7) defines the rank-two spatial TT projector and (8) its normalized polarization decomposition. Thus a candidate pole must have two physical propagating helicities, and the sign \(Z>0\) in (9) is a **necessary** positive-norm condition in this Euclidean polarization comparator. It does not establish Hilbert-space reflection positivity, Lorentzian unitarity or absence of other ghosts. The off-shell four-dimensional transverse traceless projector of rank five, studied in the preceding Ward note, must NOT be substituted for the two on-shell graviton states.

## The single-Theta metric chain-rule route: conditional sufficiency, not automatic equivalence

There is a direct *UBT-specific* positive conditional route. Assume an effective set of species \(\chi_a\) has been genuinely constructed from the physical reduced \(\Theta\) theory, and **assume** its effective matter functionals depend on \(\Theta\) *only through the same locked Axiom-C metric* \(g[\Theta]\). Defining \(T_a^{\mu\nu}=2\delta S_a/(\sqrt{|g|}\delta g_{\mu\nu})\), the full metric chain rule at fixed effective matter states gives:
\[
\boxed{\left.\delta_\Theta S_a[\chi_a,g(\Theta)]\right|_{\delta\chi_a=0}
=\frac12\int d^4x\sqrt{|g|}\,T_a^{\mu\nu}
\left(D_\Theta g[\delta\Theta]\right)_{\mu\nu}.}\tag{11}
\]
\[
S_a^{\rm toy}(q)=\frac12 T_a\,g(q)+\lambda_a I(q)\,O_a,\qquad
g(q)=1+q+q^2,\quad I(q)=q^2,\tag{12}
\]
\[
\boxed{\frac{d S_a^{\rm toy}}{dq}
=\frac12 T_a(1+2q)+2\lambda_a q O_a.}\tag{13}
\]

Equation (11) gives a **common metric source coefficient** for every species; after deriving one canonically normalized graviton field and the consistent physical state space, it can reproduce the universal \(h_{\mu\nu}\sum_aT_a^{\mu\nu}\) coupling. However metric-only matter dependence is currently an **unproved assumption**, especially because the would-be \(\chi_a\) are themselves composites of the very same \(\Theta\). Their induced variations add terms proportional to \(D_\Theta\chi_a\); possible symmetry-allowed direct \(\Theta\)-operators likewise add terms. The exact negative-control toy (12)-(13) exhibits species-dependent additional couplings \(2\lambda_a q O_a\), even with a common metric \(g(q)\). The toy is **not** a UBT Lagrangian. This identifies the actual microscopic selection question: can the single \(\Theta\) action and its Ward identities force *all physical low-energy species* to couple through the one canonical metric, excluding independent nonmetric long-range vertices? No result yet does so.

## Weinberg–Witten and the structural decision

If the emergent one-Theta sector is an **ordinary Lorentz-invariant local quantum field theory with a suitable conserved Lorentz-covariant gauge-invariant stress tensor**, a nontrivial energy-carrying massless composite spin-two state conflicts with the Weinberg–Witten theorem. To avoid its assumptions, UBT must explicitly demonstrate the origin of genuinely gravitational constraints and the relevant stress-energy/gauge structure (or identify and verify a different precise failed hypothesis). The axiomatic composite metric is a possible structural difference but does **not itself prove** a loophole. The arithmetic RH automorphic theta lift also does not establish a physical Ward identity or universal soft graviton.

**One-Theta acceptance requirement:** From a *single selected microscopic* \(S[\Theta]\), derive stable asymptotic species, a genuine gauge-reduced pole with \(Z>0\), the massless tensor trace factor \(1/2\), universal \(g_i\) across connected species, the soft Ward identity, and an explicit Weinberg–Witten assumptions audit. The present \(\Theta\)-based model supplies **none of the full chain**, despite useful exact comparator gates.

References: Weinberg, *Photons and Gravitons in Perturbation Theory*, Phys. Rev. 138 (1965) B988, https://doi.org/10.1103/PhysRev.138.B988 ; de Rham, *Massive Gravity*, Living Reviews in Relativity 17 (2014), https://pmc.ncbi.nlm.nih.gov/articles/PMC5256007/ ; Jenkins, *Constraints on emergent gravity*, https://arxiv.org/abs/0904.0453 .

Reproducibility: tools/verify_rh_theta_soft_universality_tt_residue_2026_11_24.py and research_tracks/action_selection/tests/test_rh_theta_soft_universality_tt_residue_2026_11_24.py. Tests prove exact finite algebra only; known Weinberg/Weinberg–Witten theorems are referenced, not machine-formalized here. **LEAN-PENDING, semantic review pending, do not merge as a UBT graviton proof.**
