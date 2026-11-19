<!-- BILINGUAL-UNIT: gr-global-clock-stokes-compatibility-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional global clock and volume-form topology theorem; no full UBT dynamics or Lambda prediction.
UBT-AI-PROVENANCE-END
-->
# Local HT volume potential needs no global Theta time

<!-- UNIT: scope -->
## Correction: global time was an extra assumption

The earlier title and explanation overstated what the UBT kinematics implies. The restricted real Lorentz-vector identity yields a **local** proper-time scalar on any patch where the carrier X is timelike and the physical connection is metric compatible. An FLRW/synchronous coframe was only a **chosen diagnostic geometry**, not cosmological evolution derived from Theta. Neither the locked kinematics nor the example proves X is timelike everywhere, that such a scalar extends smoothly over all of spacetime, or that the full complex-Theta theory requires a global time.

The HT equation dC3=volume and its potential Stokes contradiction are logically separate from the clock identity. On arbitrary local patches the HT equation is solved without using a time variable derived from Theta at all. The maximality argument below is a valid **conditional theorem** only after imposing a globally timelike carrier; it cannot be used to rule out closed spacetime topology for UBT in general.

<!-- UNIT: local -->
## Direct local C3 primitive without any cosmology

On an arbitrary oriented coordinate chart \(U\), write the metric volume form as
\[
\nu_e=f(x^0,x^1,x^2,x^3)\,dx^0\wedge dx^1\wedge dx^2\wedge dx^3,
\qquad f=\sqrt{-\det g}>0.
\]
Fix a reference coordinate value \(x^0_\ast\) inside the chart and define
\[
\boxed{
C_3=\left(\int_{x^0_\ast}^{x^0}
f(\tau,x^1,x^2,x^3)\,d\tau\right)
dx^1\wedge dx^2\wedge dx^3 .
}\tag{D}
\]
Its exterior derivative is exactly \(dC_3=\nu_e\), since all spatial-derivative contributions contain a repeated spatial differential. The coordinate \(x^0\) is **arbitrary** here: it is NOT a derived global time, NOT the intrinsic \(T=\sqrt{-X^2/\mathcal N_0}\), and NOT an FLRW or synchronous ansatz. This construction is a local instance of the Poincare lemma. It works on every oriented chart with nondegenerate volume form without assuming that the carrier \(X\) is timelike. The exact global existence question is instead whether the de Rham class \([\nu_e]\in H^4_{\rm dR}(M)\) vanishes for the chosen manifold and auxiliary potential model.

<!-- UNIT: theorem -->
## Two independent global obstructions


Fix a smooth connected oriented four-dimensional Lorentz spacetime with nondegenerate coframe, and the restricted non-null *globally timelike* Lorentz carrier \(X\) satisfying
\[
e^a=\mathcal N_0^{-1/2}D_\omega X^a,\quad X^2<0,\quad \omega_{ab}=-\omega_{ba}.
\]
Define the globally smooth scalar \(T=\sqrt{-X^2/\mathcal N_0}\). Metric compatibility and the locked coframe imply
\[
\boxed{g^{-1}(dT,dT)=-1.}\tag{A}
\]
Thus \(dT\) is nowhere zero. On a compact boundaryless manifold a smooth real-valued \(T\) attains its maximum, where \(dT=0\), contradiction. This conclusion follows from the ADDITIONAL global timelike carrier/clock hypothesis, independent of the auxiliary HT three-form. No global clock existence theorem follows for the complete Theta field. It does NOT exclude globally non-null carrier patches on a spacetime where X fails to be timelike everywhere, and does NOT constrain other full-complex UBT sectors without the eikonal identity.

Separately, for the **adopted effective** HT auxiliary equation
\[
dC_3=\nu_e,\qquad \nu_e=\sqrt{-g}\,d^4x,
\]
a single globally defined smooth \(C_3\) on compact boundaryless \(M\) gives \(\int_M\nu_e=\int_MdC_3=0\) by Stokes, while the oriented Lorentzian volume form has strictly positive integral. Thus the HT potential cannot be global under these separate hypotheses. These two contradictions have different premises and neither selects a cosmological constant.


<!-- UNIT: construction -->
## Explicit solution on a time slab


A consistent comparison class is a globally hyperbolic product spacetime \(M=I\times\Sigma\), with interval \(I\subseteq\mathbb R\) and an oriented spatial three-manifold \(\Sigma\). \(\Sigma\) may be compact and boundaryless (for example \(S^3\)), because **spatial compactness is not four-dimensional spacetime compactness** when time remains an interval.

For Gaussian time \(T\) and a positive spatial metric \(h_{ij}(T,y)\),
\[
g=-dT^2+h_{ij}(T,y)\,dy^i dy^j,\quad
\nu_e=dT\wedge \operatorname{vol}_{h(T)}.
\]
On a product with smooth identification of the spatial slices, fix \(T_\ast\in I\) and define the *auxiliary* global three-form
\[
\boxed{C_3(T,\cdot)=\int_{T_\ast}^{T}\operatorname{vol}_{h(\tau)}\,d\tau.}\tag{B}
\]
This is a smooth spatial top-degree form. On a three-dimensional \(\Sigma\) its spatial exterior derivative vanishes identically, hence
\[
dC_3=dT\wedge\operatorname{vol}_{h(T)}=\nu_e.
\]
No new local fundamental field, quantization or tuning is needed for this **auxiliary reconstruction**; it does not derive the HT comparator from Theta. On a finite slab \([T_0,T_1]\times\Sigma\) with boundaryless \(\Sigma\),
\[
\boxed{\int_M\nu_e=\int_{\partial M}C_3
=\int_\Sigma C_3(T_1)-\int_\Sigma C_3(T_0).}\tag{C}
\]
If \(I=\mathbb R\) one must state falloff, admissibility and boundary conditions at temporal infinity before using integration-by-parts arguments.


<!-- UNIT: boundary -->
## When a local higher form would matter


On compact closed \(M\), one could replace a global ordinary \(C_3\) by locally defined higher-gauge potentials whose globally defined curvature four-form represents a nontrivial cohomology class. That changes the **global auxiliary bundle/gerbe assumption** and can evade the *HT* Stokes obstruction, but not the independent globally timelike exact-clock maximum principle; it also does not force \(\Lambda_{\rm eff}\) to a measured value.

This is not a new observational prediction. The correct conclusion is to specify the domain/boundary conditions first and not to impose a compact four-dimensional manifold in the global real-timelike-clock branch. For a locally timelike carrier, work on patches without asserting a globally defined T. The Palatini–HT gravity sector and its C3 field remain conditional EFFECTIVE structures, not the final microscopic single-Theta UBT action.


<!-- UNIT: grounding -->
## Relationship to current research and verification

The clock eikonal identity was derived in research_tracks/T1_GR/gr_intrinsic_clock_foliation_2026_11_18.en.md, and the HT flux/global obstruction is discussed in research_tracks/T1_GR/gr_ht_global_lambda_clock_2026_11_19.en.md. This note supplies the missing logical connection and a constructive global solution on a time slab. The proof is analytic (extreme-value theorem, Stokes, exterior derivative of a spatial top-form); the existing SymPy volume-clock checks apply to FLRW examples. Lean, complete global topology of full Theta, coupling to matter and on-shell physical selection remain unchecked.
