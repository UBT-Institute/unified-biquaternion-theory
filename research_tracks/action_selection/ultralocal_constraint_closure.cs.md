<!-- BILINGUAL-UNIT: ultralocal_constraint_closure -->
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


# UBT od hamiltoniánu: překážka ultralokální uzávěry skalárních vazeb

**Podmíněná přesná kanonická věta (2026-10-25), nikoli úplný fyzikální hamiltonián UBT.**

Na zvoleném prostorovém řezu předpokládejme, že osm reálných složek q^A Theta se transformuje jako prostorové skaláry a nezávisle zavedené p_A jako hustoty s kanonickými {q^A(x),p_B(y)}=δ^A_B δ³(x-y). Tato kotečná struktura je **zkušební**, nikoli vybraná uzamčenými axiomy UBT.

Generátor prostorových difeomorfismů D[ξ]=∫p_A ξ^i ∂_i q^A dává {q,D[ξ]}=ξ·∂q a {p,D[ξ]}=∂_i(ξ^i p). Při vhodných okrajích se uzavírá {D[ξ],D[η]}=D[[ξ,η]] (se standardní konvencí Poissonova generátoru).

Uvažujme **libovolnou** ultralokální hladkou hustotu skalární vazby h(q(x),p(x)) váhy jedna bez prostorových derivací a bez netriviálního rozmazání závislého na poli. Položme H[N]=∫N(x)h(q(x),p(x)). Její Poissonova závorka je
\[
\{H[N],H[M]\}=\int d³x\,N(x)M(x)
\sum_A\big(h_{q^A}h_{p_A}-h_{p_A}h_{q^A}\big)=0.
\]
To je přesné nezávisle na konkrétním invariantním potenciálu či vnitřní spinové algebře.

Naproti tomu **pokud** redukované gravitační vazby UBT musí realizovat obvyklou nedegenerovanou algebru deformací nadploch GR se složenou inverzní metrikou h^{ij}[Theta],
\[
\{H[N],H[M]\}=D[h^{ij}(N\partial_jM-M\partial_jN)]
\]
(až na další nezávisle odvozené vnitřní kalibrační vazby a případné vazby složených proměnných). Obecně je tato pravá strana nenulová mimo plochu hybnostních vazeb. Ultralokální hamiltonián skalární hustoty na uvedeném kanonickém fázovém prostoru pole tedy **nemůže reprodukovat požadovanou netriviální algebru změn foliace mimo pohybové rovnice**. Slabé vymizení obou stran na řešeních není dostatečným dokladem rovnosti jejich strukturních funkcí.

**Důležitá vymezení:** důkaz předpokládá kanonické kotečné závorky, prostorově skalární transformaci q^A a nepřítomnost redukce závislé na derivacích, sekundárních vazeb či nekanonických Diracových závorek. NEVYLUČUJE odlišnou fyzikální symplektickou strukturu, redukovaný či emergentní gravitační fázový prostor ani neultralokální h. NEVYBÍRÁ derivační či křivostní hamiltonián ani neodvozuje Einsteinovu dynamiku. Prostorové gradienty samy nezaručují algebru GR; složená metrika závisí na derivacích a redukce vazeb může být zásadní.

**Další výpočet:** zvolit *jednu* plně specifikovanou přípustnou složenou tetrádu a rekonstrukci torze a konexe na nedegenerované oblasti; spočítat indukované primární vazby, redukované závorky a strukturní funkce H a D. Neztotožňovat oboustranný komutátor křivosti z #736 se závorkami hamiltonovských vazeb.

Regrese: python -m unittest discover -s research_tracks/action_selection/tests -p 'test_ultralocal_constraint_closure.py' -v.
