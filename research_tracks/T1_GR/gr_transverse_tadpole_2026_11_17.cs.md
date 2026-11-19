<!-- BILINGUAL-UNIT: gr-transverse-tadpole-2026-11-17 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional first variation and comparator; no derived fundamental gravity action.
UBT-AI-PROVENANCE-END
-->
# Projektovaný Eulerův test: konstantní kvadratická torze neruší objemovou první variaci

<!-- UNIT: scope -->
## Přesný předpoklad

Jde o omezený test první variace pro reálný Lorentzovský nosič s nenulovou normou a volně pomocnou metrickou kontorzí. Zpřesňuje existující větu o realizaci tetrády a starší překážku holé split-jet akce. Kanonická metrika ani jediné fundamentální Theta se nemění; netvrdíme nové mikroskopické pole nebo dynamický postulat. Závěr neplatí automaticky, pokud fyzikální selektor kontorze K[Theta] omezí přípustné variace.

<!-- UNIT: projection -->
## Projektovaná Eulerova podmínka


For the restricted nonnull Lorentz carrier \(X\) with the auxiliary physical contortion allowed to vary freely:
\[
X_a\,\delta e_\mu{}^a=0,\qquad
P^a{}_b=\delta^a_b-\frac{X^aX_b}{X^2},\qquad
\delta e_\mu{}^a=P^a{}_b h_\mu{}^b.
\]
For any differentiable parent functional with coframe Euler density \(\mathcal E_a{}^\mu=\delta S/\delta e_\mu{}^a\), stationarity for *all* fixed-\(X\) constrained variations is equivalent to
\[
\boxed{P^b{}_a\mathcal E_b{}^\mu=0}
\quad\Longleftrightarrow\quad
\mathcal E_a{}^\mu=X_a\lambda^\mu.
\]
For a volume term \(\alpha\int\det e\,d^4x\) at the affine field \(X^a=sx^a\), \(e_\mu{}^a=\delta_\mu^a\),
\[
\mathcal E_a{}^\mu=\alpha\,\delta_a^\mu,\qquad
P^b{}_a\mathcal E_b{}^\mu=\alpha P^\mu{}_a;
\quad\mathrm{rank}(P)=3.
\]
Thus \(\alpha\ne0\) fails the fixed-\(X\) stationarity condition. The exact witness
\[
e_\mu{}^a(\varepsilon)=\delta_\mu^a+\varepsilon f P^a{}_\mu,\quad
\det e(\varepsilon)=(1+\varepsilon f)^3,\quad
\delta S_{\rm vol}=3\alpha\int f\,d^4x
\]
reproduces the preceding conditional coframe theorem.


<!-- UNIT: tests -->
## Rodina křivostních a torzních členů s konstantními koeficienty


For the strictly declared constant-coefficient comparison family
\[
S_{\rm test}=\int_M\alpha\,\nu_e
+a\int_M\epsilon_{abcd}\,e^a\wedge e^b\wedge R^{cd}(\omega)
+b\int_M e_a\wedge e_b\wedge R^{ab}(\omega)
+\int_M \nu_e\,Q(T)
+\int_M \nu_e\,W(R),
\]
where \(Q\) and \(W\) begin quadratically and the common affine point has \(T=R=0\), the first variation of \(Q,W\) vanishes at that point. For any compactly supported variation of the metric-compatible connection, at \(\omega=0,\ e^a=dx^a\),
\[
\delta R^{ab}=d(\delta\omega^{ab}),\qquad
\delta(e\wedge e\wedge R)=d(e\wedge e\wedge\delta\omega)
\]
with the appropriate internal contraction and orientation; hence the constant-coefficient Palatini and Holst linear-curvature first variations are pure boundary terms. Only \(\delta\int\alpha\nu_e\) remains, and it is nonzero on the explicit fixed-\(X\) coframe witness if \(\alpha\ne0\).

If a derivative-free potential contributes \(U(X)\nu_e\), stationary affine flat solutions require \(\alpha+U(X)=0\) pointwise on the entire patch. For analytic or polynomial \(U(X^2)\), because \(X^2\) varies through an open interval there, this means \(U=-\alpha\) on that interval (and globally for a polynomial). Such a tuned constant cancellation leaves the bare action with no curvature kinetic term: it does not derive a graviton.

In the already-adopted *effective* Henneaux–Teitelboim comparator,
\[
-\frac1\kappa\Lambda(\nu_e-dC_3)+\alpha\nu_e
=-\frac1\kappa(\Lambda-\kappa\alpha)(\nu_e-dC_3)+\alpha\,dC_3.
\]
The volume term can be absorbed into the integration constant in the bulk for fixed boundary data. This exact preexisting redundancy does **not** generate the imported Palatini term, fix Newton coupling, or establish a microscopic one-\(\Theta\) action.


<!-- UNIT: meaning -->
## Co se mění a co zůstává otevřené

Kvadratické členy torze a křivosti nemohou při plochém beztorzním afinním pozadí zrušit nenulový objemový člen v první variaci bez ohledu na své konstantní koeficienty. Stejně jej nemohou v první variaci rušit ani Einsteinův–Cartanův a Holstův člen s konstantním koeficientem. Jde o překážku stacionarity vakua v deklarované srovnávací rodině, nikoli o důkaz, že kvadratická torze nemůže jinde nést tenzorovou dynamiku. Ne-minimální koeficient křivosti závislý na nosiči, nezávislý spinový zdroj, fyzikálně vybraný zákon kontorze či neobjemová mikroskopická akce jsou mimo rozsah věty. Henneauxovo–Teitelboimovo přeznačení je existující efektivní srovnání a gravitace zde zůstává přijatým, nikoli odvozeným postulátem.

<!-- UNIT: grounding -->
## Návaznost na repozitář a hranice ověření

Srovnat research_tracks/action_selection/physics_closure_bare_action_2026_10.cs.md pro silnější větu o kritické nule holé akce, research_tracks/action_selection/ht_volume_shift_action_selection.cs.md pro HT posun konstanty, research_tracks/action_selection/full_composite_volume_variation.cs.md pro přesnou formální kompozitní první variaci a research_tracks/T1_GR/gr_fixed_carrier_volume_no_go_2026_11_17.cs.md pro explicitní pravou inverzi tetrády. Konečný přesný test SymPy tools/verify_gr_transverse_tadpole_2026_11_17.py potvrzuje hodnost projektoru, objemovou variaci, vyladění polynomiálního potenciálu, derivaci kvadratických invariantů v nulovém pozadí a HT algebru. Okrajový argument pro Palatiniho/Holstův člen je analytický důkaz diferenciálními formami, nikoli součást testu. Úplné nelineární rovnice jediného Theta, spin-dva Hessian, globální kalibrace/okraje, Lean a CI repozitáře nejsou tímto dokumentem ověřeny. Před splněním kontrol nemergovat.
