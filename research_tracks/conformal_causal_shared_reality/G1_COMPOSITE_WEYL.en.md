<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: composite-weyl-g1.scope -->
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

# G1: a composite Weyl connection from Theta — exact versus nonexact branches


**2026-10-28 · PR #809 · C_working.** Exact restricted Mat(2,C) first-jet calculation, not a canonical action, conformal Cartan closure, physical graviton or selected carrier dimension.


## Norm-only connection [PROVED, restricted]


On a regular positive-norm patch, write:


\[
 N:=B(\Theta,\Theta)>0,\qquad J\Theta=i\Theta,\qquad
 u_{\mathrm{norm}}=-\tfrac12\,d\ln N.
\]


Take the scale weight of Theta to be positive unity. If a natural first-order local one-form is required to depend only on N and dN, then u=f(N)dN. The coefficient of d lambda in the transformed u forces f(N)=-1/(2N), uniquely in this restricted ansatz. Consequently:


\[
 \Theta\mapsto e^\lambda\Theta,\quad N\mapsto e^{2\lambda}N,\quad
 u_{\mathrm{norm}}\mapsto u_{\mathrm{norm}}-d\lambda,\quad du_{\mathrm{norm}}=0.
\]


This is an integrable Weyl geometry with no new dilation field-strength. It does not itself choose a gravitational scale or propagating spin-two mode.


## Complex shape current [PROVED as algebra, CANDIDATE as physics]


The real bilinear B has inertia (2,6), and J is a B-isometry with B(Jv,w)=-B(v,Jw). For an independently specified Lorentz connection Omega compatible with B and J, the following real first-jet current is invariant under local Lorentz transformations and under real rescaling of Theta:


\[
 j_\mu=\frac{B(J\Theta,D^\Omega_\mu\Theta)}{N},\quad
 u_a=u_{\mathrm{norm}}+a\,j,\quad a\in\mathbb R.
\]


Under an *independent* local complex phase rotation without an additional phase connection, this current shifts:


\[
 \Theta\mapsto e^{i\alpha}\Theta\quad\Longrightarrow\quad
 j\mapsto j+d\alpha,\qquad u_a\mapsto u_a+a\,d\alpha.
\]


Therefore u_a is not invariant under an independently gauged local phase unless a vanishes or another compensating transformation is justified. A mixed gauge interpretation is a new hypothesis, NOT a result of the earlier PR.


## Exact nonzero-curvature example [COUNTEREXAMPLE to norm-only closure]


Choose the special matrix chart:


\[
 \Theta=(1+it)I+x\sigma_1,\quad N=1+t^2-x^2>0,\quad
 j=\frac{dt}{N},\qquad (du_a)_{xt}=\frac{2ax}{N^2}.
\]


On the patch N>0, the composite curvature is nonzero for nonzero a and generic x. No independent Weyl one-form was introduced. This is a standard Berry-like shape current in indefinite signature; do not portray it as a novel discovery or as a solution of UBT dynamics.


## Strict reality and rank gates [OPEN]


For purely Hermitian Theta and a Hermiticity-preserving Lorentz derivative, j vanishes identically because the complex JTheta is orthogonal to the Hermitian subspace. On a timelike value Theta=rI, the exact norm-only choice enforces:


\[
 \Theta=rI,\qquad B(\Theta,D^{u_{\mathrm{norm}}}\Theta)=0,\qquad
 \operatorname{rank}(\mathrm{Hermitian\ readout})\le3.
\]


The Hermitian readout therefore loses its time direction and has rank at most the spatial dimension on this slice. In the nonexact shape-current example, if additional spatial Hermitian jets are supplied, at the origin the time derivative instead becomes:


\[
 D_t^{u_a}\Theta(0)=iI+aI\notin\operatorname{Herm}_2,\qquad
 D_t^{u_a}\Theta(0)\notin i\operatorname{Herm}_2\quad(a\ne0).
\]


Thus restoring a Hermitian time projection via the a-term simultaneously introduces a non-Hermitian piece; the **strict unprojected** tetrad-reality gate has not passed. Taking a projection by fiat is not a fully SU(2,2)-equivariant construction and may hide another assumption.


## Scientific decision [OPEN]


An algebraically derived nonflat real dilation current exists using Theta's complex shape, but it comes with an unfixed coefficient, a local-phase mixing problem and failure of the demonstrated strict tetrad readout. Neither this nor the exact norm branch has a Dirac or principal-symbol calculation or stable spin-two propagation. Keep G1 PARTIAL. Preserve PR #807 and #808; do not promote or merge.


## Evidence


Tests: `python -m unittest discover -s tests -p 'test_theta_composite_weyl.py' -v`; eight exact symbolic cases passed in a local SymPy run. GitHub CI and full theory review are separate.


Related integrable-Weyl context: https://link.springer.com/article/10.1007/s10714-020-02693-z .
