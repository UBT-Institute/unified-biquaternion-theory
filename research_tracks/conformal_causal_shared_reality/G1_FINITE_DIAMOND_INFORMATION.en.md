<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: g1-finite-diamond-information -->
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

# Finite causal diamond: a Theta-invariant information trial and a uniqueness counterexample

**2026-10-28 · PR #809 · C_working · G1-SR trial.** This is a finished *finite algebraic test*, not a completed field-theoretic G1/G2 gate, a derived local quantum observable algebra, physical metric, symplectic form or microscopic UBT Hamiltonian. The user-defined finite-signal-speed and Shared Reality principles motivate the experiment; neither is claimed derived from it.

## Externally fixed causal order [AX CANDIDATE]

Use a toy causal poset (the light cones and metric are **not yet derived** from Theta). Two observers access overlapping finite diamonds:

\[
D_L=\{a,o\},\quad D_R=\{o,b\},\quad D_L\cap D_R=\{o\},
\qquad a\prec o\prec b.
\]

Associate to each event the commutative two-outcome algebra of a binary observable. The operational interpretation of this observable is *assumed*, not produced by the field algebra or quantum measurement theory.

## Trial reference states from one existing invariant [PROVED as conditional algebra]

For the declared Mat(2,C) trial carrier and real congruence invariant B, take the positive-N branch. The logistic probability map uses an **arbitrary** positive inverse-scale beta; it is not predicted by the principles:

\[
N(\Theta):=B(\Theta,\Theta)
=2(u_0^2+v_0^2-u_1^2-u_2^2-u_3^2-v_1^2-v_2^2-v_3^2),
\quad p_\beta(\Theta)=\frac{1}{1+e^{-\beta N(\Theta)}}.
\]

The reference distribution is invariant under the already declared SL(2,C) congruence and constant complex phase because N is invariant. A boost and a phase were checked exactly in the symbolic tests; full SU(2,2) covariance and operational quantum measurement interpretation are **OPEN**. For a convenient explicit arithmetic choice:

\[
\beta=\frac{\log 2}{2},\quad
\Theta_a=I,\quad\Theta_o=2I,\quad\Theta_b=3I,
\quad (p_a,p_o,p_b)=\left(\frac23,\frac{16}{17},\frac{512}{513}\right).
\]

## Overlap-consistent construction and overcounting [PROVED in product toy]

Choosing independent event outcomes gives an explicit global extension and compatible restrictions:

\[
\omega_{aob}(x_a,x_o,x_b)=\omega_a(x_a)\omega_o(x_o)\omega_b(x_b),
\quad \omega_{ao}|_o=\omega_o=\omega_{ob}|_o.
\]

For arbitrary compatible **product** observed/reference measures the relative entropy of the union is the inclusion-exclusion combination:

\[
D(\rho_{ao}\Vert\omega_{ao})
+D(\rho_{ob}\Vert\omega_{ob})
-D(\rho_o\Vert\omega_o)
=D(\rho_{aob}\Vert\omega_{aob})\quad
\text{(product distributions only).}
\]

The subtraction of the overlap avoids counting its information twice. This identity is **not** a general quantum or correlated-state entropy inclusion-exclusion theorem. With correlated observations additional mutual/conditional information enters.

## Two global extensions invisible to the two observers [COUNTEREXAMPLE]

Choose the same nonzero Theta=I at each event and the corresponding invariant Bernoulli marginal. On endpoints allow a correlated but positive joint distribution, independent of the overlap outcome:

\[
p_a=p_o=p_b=\frac23,\qquad
P_{ab}^{(c)}(x_a,x_b)=p_a(x_a)p_b(x_b)+c(-1)^{x_a+x_b},
\quad c=\frac1{18}.
\]

The independent and correlated global states have **identical full marginals on both accessible diamonds**, not only on their intersection. Yet they differ globally, with a strictly positive relative entropy:

\[
P_{ab}^{(c)}
=\begin{pmatrix}1/6&1/6\\1/6&1/2\end{pmatrix},
\qquad
D(P_{aob}^{(c)}\Vert P_{aob}^{(0)})
=\frac16\log\frac32+\frac13\log\frac34+\frac12\log\frac98>0.
\]

This finite counterexample establishes that overlap agreement and the specified local measurements leave at least one global correlation undetermined. It does not prove nonexistence of a global state: both explicit extensions exist. A larger accessible region or additional operational correlations could distinguish them.

## First variation and Fisher rank [PROVED, conditional]

For a fixed observed Bernoulli probability r and local field coordinates q, the relative-entropy derivative is exactly:

\[
\mathcal I(q;r)=D_{\rm Bern}(r\Vert p_\beta(N(q))),\quad
\partial_A\mathcal I=\beta(p_\beta-r)\partial_A N.
\]

At a matched reference state the first variation vanishes. The second variation is:

\[
r=p_\beta(N(q_*)),\quad
\left.\partial_A\partial_B\mathcal I\right|_{q_*}
=\beta^2p_\beta(1-p_\beta)\,\partial_A N\,\partial_B N,
\quad \operatorname{rank}\mathcal F=1\quad(\nabla N(q_*)\ne0).
\]

At q_*=I the normalized gradient of N is nonzero, so the Fisher Hessian on the **eight-real-dimensional trial carrier** has rank one and seven null directions. Those directions are **not automatically ghosts or physical modes**: gauge reductions and constraints must be tested independently. An information criterion depending on this sole invariant cannot determine them.

## Positive equilibrium and entropy monotonicity do not select evolution [COUNTEREXAMPLE]

In a hypothetical reduced scalar invariant phase space (not the derived UBT phase space), two positive Hamiltonians have the same equilibrium but different linearized oscillation frequencies:

\[
H_\lambda(n,\pi)=\frac12\pi^2+\lambda(n-2)^2,\quad
\lambda\in\{1,3\},\quad
\ddot n+2\lambda(n-2)=0.
\]

Likewise choose a classical binary Markov comparator with the reference probability inherited from Theta. Its stationary distribution and a family of stochastic reversible transition matrices are:

\[
\omega=(1/3,2/3),\qquad
T_\gamma=\begin{pmatrix}
1-\frac{2\gamma}{3}&\frac{2\gamma}{3}\\
\frac{\gamma}{3}&1-\frac{\gamma}{3}
\end{pmatrix},
\quad\gamma\in\left\{\frac14,\frac12\right\}.
\]

Both kernels preserve the same reference state, obey detailed balance and contract the relative entropy (data processing), yet have different relaxation eigenvalues:

\[
\omega T_\gamma=\omega,\qquad
D(\rho T_\gamma\Vert\omega)\le D(\rho\Vert\omega),
\qquad\operatorname{det}T_\gamma=1-\gamma.
\]

The Markov example is **not** a fundamental Hamiltonian or unitary UBT model. Together the two comparators show precisely why positivity, agreement of accessible observations, and an information arrow are not by themselves a unique dynamical selector.

## Bounded decision for UBT [OPEN]

This calculation **partially realizes** the previously proposed shared-reality operational test by constructing an explicit invariant-based finite reference probability, overlap restrictions and a differentiable information functional. It does NOT derive its observable algebra, its beta normalization, the causal order, the Lorentzian metric, the true Theta modular state, gauge quotient, or action. The model decisively fails to select the Hamiltonian.

The next noncircular gate is to derive an actual local observable/state map and finite-c propagation cone from the same constrained Theta geometry, then show a **new falsifiable information relation** that excludes an otherwise viable generator. Higher-order/jet invariants or inter-region correlations may help, but must be independently normalized and should not import the target dynamics. Keep G1 PARTIAL and later G2 PARKED until that bridge is independently audited. No changes to PR #807 or PR #808.

Verification: `python -m unittest discover -s tests -p 'test_theta_finite_diamond_info.py' -v` — all seven symbolic tests passed locally. GitHub workflow checks are independent.
