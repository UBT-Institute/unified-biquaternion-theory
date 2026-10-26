<!-- BILINGUAL-UNIT: splitjet_chain_variation -->
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


# Úplná řetězová variace rozděleného jetu přijatého Einsteinova–Lambda gravitačního sektoru

**2026-10-24 — odvození a kontrola úrovně C, nikoli mikroskopický výběr akce UBT.** Vychází z [přijatého gravitačního postulátu](../../canonical/gr_closure/gravity_dynamical_postulate.cs.md), #635 a [upozornění na řetězové pravidlo nezávislých a složených proměnných](trace_torsion_curvature_bridge.cs.md). Samostatná úplná kalibrační, hmotová a kvantová akce je OPEN.

## Obecná první variace a složené řetězové pravidlo

Nechť \(q=\sqrt{N_0}>0\) a použijme stávající kofrámeček rozděleného jetu nenulové normy
\[
E^a=q^{-1}(dX^a+\omega^a{}_bX^b+K_J{}^a{}_bX^b+wX^a).
\]
Pro *již přijatý* funkcionál Palatini–HT zapišme první variaci (až na okrajové členy) jako
\[
\delta S_G=\int\delta E^a\wedge\mathcal P_a+
\delta\omega^{ab}\wedge\mathcal Q_{ab}
+\delta\Lambda\,\mathcal V_\Lambda+\delta C_3\wedge\mathcal V_C .
\]
Zde \(\mathcal P_a\) je Eulerova trojforma tetrády, \(\mathcal Q_{ab}\) Eulerova trojforma konexe **při pevném E** a poslední dvě Eulerovy formy reprodukují \(\nu_E=dC_3,\ d\Lambda=0\). \(\mathcal P_a=0\) dává Einsteinovu–Lambda tetrádovou rovnici s normalizací již určenou kanonickým postulátem GR; \(\mathcal Q_{ab}=0\) dává v této větvi Cartanovu rovnici torze. Nenahrazujeme tyto zdrojové rovnice novými postuláty.

Přesná složená první variace je
\[
\delta E^a=q^{-1}\left[D\delta X^a+
(\delta\omega^a{}_b+\delta K_J{}^a{}_b)X^b+\delta w\,X^a\right],
\quad D\delta X^a=d\delta X^a+(\omega^a{}_b+K_J{}^a{}_b+w\delta^a_b)\delta X^b.
\]
Eulerovy rovnice jsou proto **zpětnými přenosy** \(\mathcal P,\mathcal Q\): rovnice rozděleného jetu \((\delta K_J{}^a{}_bX^b)\wedge\mathcal P_a=0,\ (\delta w X^a)\wedge\mathcal P_a=0\); rovnice konexe \(\mathcal Q_{ab}+q^{-1}X_{[b}\mathcal P_{a]}=0\) (s ohledem na přesnou normalizační konvenci antisymetrické variace); a rovnice X daná integrací per partes členu \(D\delta X^a\wedge\mathcal P_a\). Jakmile \(\mathcal P=0\), všechny složené členy řetězového pravidla úměrné \(\mathcal P\) vymizí, takže zbývající rovnice konexe je \(\mathcal Q=0\) a rovnice X nemá v tomto čistě gravitačním sektoru nezávislý zbytek.

## Explicitní certifikát hodnosti — co umožňuje argument

V X nenulové normy zobrazuje infinitesimální Lorentzovsky antisymetrické \(\delta K_J^{ab}\) vektor X na jeho 3-rozměrný ortogonální doplněk; \(\delta w X\) generuje zbývající rovnoběžný směr. Jejich součet generuje všechny čtyři tetrádové směry. V časupodobném klidovém rámci \(X^a=(r,0,0,0),r\ne0\) zvolme tři nezávislé boostové složky tak, aby \((\delta K_J)^i{}_0=k_i\). Potom
\[
\delta E^a=\frac r q(s,k_1,k_2,k_3),\quad
\det\frac{\partial(\delta E^0,\ldots,\delta E^3)}{\partial(s,k_1,k_2,k_3)}=\frac{r^4}{q^4}\ne0.
\]
Z neomezených lokálních variací pomocných polí rozděleného jetu v tomto deklarovaném sektoru tedy plyne \(\mathcal P_a=0\). Argument je lokální a předpokládá, že akce a regularita nenulové normy skutečně připouštějí tyto čtyři variace nezávisle.

## Zásadní logická hranice

Tím se dokazuje podmíněná **identita přenosu variace** přijatého gravitačního postulátu. Neodvozuje Palatiniho koeficient z energie Theta ani neurčuje fundamentální akci. Sama nepočítá fyzikální hamiltonián, nedokazuje vazbu kalibračních a hmotových zdrojů ani UV stabilitu. Variace ansatzu *před* variací úplného funkcionálu může ztratit rovnice: nevyvozovat tento výsledek z omezeného Diracova modelu FLRW #710. Samostatný Hilbertův tenzor energie a hybnosti z modelu pevného pozadí (#709) rovněž nelze mlčky dosadit za úplný složený zdroj.

**Další podmínka:** rozšířit přesně tutéž variaci na *specifikovaný* zdrojový člen hmoty či Theta, sledovat indukované závislosti \(\delta E\) a \(\delta\omega\) a ukázat, zda se jeho Eulerova forma tetrády po redukci vazeb stává Hilbertovým hmotovým tenzorem. Netvrdit to, dokud není vybrána jednoznačná úplná akce.

Symbolická kontrola: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_splitjet_variation_rank.py' -v\`.
