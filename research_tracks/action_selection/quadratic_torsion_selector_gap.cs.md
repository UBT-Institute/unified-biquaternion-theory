<!-- BILINGUAL-UNIT: quadratic_torsion_selector_gap -->
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


# Algebraický potenciál torze sám nedokáže budit torzi

**Podmíněná variační věta pomocných polí (2026-10-25). NENÍ akcí či hamiltoniánem UBT pouze pro Theta.** Navazuje na rozklad torze #744 a kanonickou složenou metriku se zakřivenou větví s torzí.

Při pevné regulární Lorentzově tetrádě rozložme metricky kompatibilní torzi ireducibilně T=V(t)+A(a)+Q, dimenze 4+4+16. S těmito 24 složkami zacházejme **pouze pro tuto diagnostiku** jako s nezávislými pomocnými variacemi. Uvažujme paritně sudou diagonální algebraickou hustotu torze
\[
{\cal L}_{\mathrm{aux}}=e\left(\frac{\alpha}{2}t_\mu t^\mu+
\frac{\beta}{2}a_\mu a^\mu+
\frac{\gamma}{2}Q_{\lambda\mu\nu}Q^{\lambda\mu\nu}\right),
\]
s nenulovými reálnými \(\alpha,\beta,\gamma\), bez lineárního zdroje, bez derivací torze, bez smíšených členů křivosti a s pevným e při variaci torze. Variace v nezávislých ireducibilních podprostorech dávají přesně
\[
\alpha t^\mu=0,\quad\beta a^\mu=0,\quad\gamma Q^{\lambda\mu\nu}=0.
\]
Z nedegenerovanosti Lorentzovy metriky plyne T=0 ve stacionárních bodech. Jde o lokální algebraické tvrzení o kritickém bodě, **nikoli** o pozitivitu či stabilitu: Lorentzova signatura obecně činí kvadratickou formu indefinitní.

S lineárními odvozenými proudy \({\cal L}_{source}=e(J_t^\mu t_\mu+J_a^\mu a_\mu+J_Q^{\lambda\mu\nu}Q_{\lambda\mu\nu})\) dává formální pomocná extremalizace místo toho t=-J_t/alpha, a=-J_a/beta, Q=-J_Q/gamma. Jde o *vzorec podmíněný takovými odvozenými zdroji*, NIKOLI jejich odvození z Theta. Degenerované koeficienty ponechávají ploché směry; vazby na derivace torze a křivost mohou dát diferenciální rovnice torze; při vázaném implicitním složeném zobrazení tyto variace **nejsou** nezávislé a tuto větu nelze použít beze změny.

**Důsledek pro UBT.** Pokud zakřivená složená reprezentace potřebuje nenulovou torzi, nejjednodušší nedegenerovaná kvadratická algebraická hustota torze bez zdroje k jejímu vytvoření nestačí. Oprávněná fundamentální akce jediného pole Theta by musela dodat nenulový indukovaný zdroj či vazbu torze nebo zcela odlišnou variační strukturu; přidání pomocného potenciálu torze se nepočítá jako odvození S_UBT[Theta]. Uzávěra vazeb, fyzikální symplektická forma, energie a limita GR zůstávají neprokázané.

Test cílí konkrétně na omezený ansatz. Nedokazuje zákaz všech invariantů pouze torze ani nevybírá koeficienty. Rovněž nezávisle nedokládá nutnost fyzikální torze ve všech zakřivených větvích (kanonické vyloučení se týká konkrétní dvojice konexí bez torze).

Reprodukce: research_tracks/action_selection/tests/test_quadratic_torsion_selector.py.
