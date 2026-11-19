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
# Kompaktní HT spor již vylučují globální vlastní hodiny z Theta

<!-- UNIT: scope -->
## Vyřešení zdánlivého sporu

Rovnice dC3=objem je neslučitelná s globální hladkou C3 na kompaktním uzavřeném prostoročasu. Nejde o rozpor celé UBT: tato globální topologie je neslučitelná také s dříve odvozenými vlastními hodinami Theta na všude časupodobné Lorentzově větvi. Smíchali jsme neslučitelné globální předpoklady. Stokesova překážka je standardní diferenciální geometrie a argument maxima hodin je standardní hladká analýza.

<!-- UNIT: theorem -->
## Dvě nezávislé globální překážky


Fix a smooth connected oriented four-dimensional Lorentz spacetime with nondegenerate coframe, and the restricted non-null *globally timelike* Lorentz carrier \(X\) satisfying
\[
e^a=\mathcal N_0^{-1/2}D_\omega X^a,\quad X^2<0,\quad \omega_{ab}=-\omega_{ba}.
\]
Define the globally smooth scalar \(T=\sqrt{-X^2/\mathcal N_0}\). Metric compatibility and the locked coframe imply
\[
\boxed{g^{-1}(dT,dT)=-1.}\tag{A}
\]
Thus \(dT\) is nowhere zero. On a compact boundaryless manifold a smooth real-valued \(T\) attains its maximum, where \(dT=0\), contradiction. This conclusion is independent of the auxiliary HT three-form: the globally timelike restricted carrier/clock already excludes a compact boundaryless spacetime. It does NOT exclude globally non-null carrier patches on a spacetime where X fails to be timelike everywhere, and does NOT constrain other full-complex UBT sectors without the eikonal identity.

Separately, for the **adopted effective** HT auxiliary equation
\[
dC_3=\nu_e,\qquad \nu_e=\sqrt{-g}\,d^4x,
\]
a single globally defined smooth \(C_3\) on compact boundaryless \(M\) gives \(\int_M\nu_e=\int_MdC_3=0\) by Stokes, while the oriented Lorentzian volume form has strictly positive integral. Thus the HT potential cannot be global under these separate hypotheses. These two contradictions have different premises and neither selects a cosmological constant.


<!-- UNIT: construction -->
## Explicitní řešení na časovém intervalu


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
## Kdy by byla podstatná lokální vyšší forma


On compact closed \(M\), one could replace a global ordinary \(C_3\) by locally defined higher-gauge potentials whose globally defined curvature four-form represents a nontrivial cohomology class. That changes the **global auxiliary bundle/gerbe assumption** and can evade the *HT* Stokes obstruction, but not the independent globally timelike exact-clock maximum principle; it also does not force \(\Lambda_{\rm eff}\) to a measured value.

This is not a new observational prediction. The correct conclusion is to specify the domain/boundary conditions first and not to impose a compact four-dimensional manifold in the global real-timelike-clock branch. For a locally timelike carrier, work on patches without asserting a globally defined T. The Palatini–HT gravity sector and its C3 field remain conditional EFFECTIVE structures, not the final microscopic single-Theta UBT action.


<!-- UNIT: grounding -->
## Vztah k současnému výzkumu a ověření

Rovnice vlastního času byla odvozena v research_tracks/T1_GR/gr_intrinsic_clock_foliation_2026_11_18.cs.md a globální HT překážka je v research_tracks/T1_GR/gr_ht_global_lambda_clock_2026_11_19.cs.md. Tato poznámka doplňuje chybějící logické propojení a konstruktivní globální řešení na časovém intervalu. Důkaz je analytický (věta o extrému, Stokesova věta, vnější derivace prostorové formy nejvyššího stupně); existující symbolické testy objemových hodin platí pro příklady FLRW. Lean, úplná topologie komplexního Theta, vazby na hmotu a dynamická selekce on-shell zůstávají neověřené.
