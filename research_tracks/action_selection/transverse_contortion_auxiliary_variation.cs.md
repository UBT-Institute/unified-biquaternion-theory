<!-- BILINGUAL-UNIT: transverse_contortion_auxiliary_variation -->
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


# Příčná kontorze: podmíněný kvadratický pomocný variační selektor

**Podmíněný výsledek úrovně C, 2026-10-25. NENÍ odvozením fundamentální akce UBT.** Poznámka testuje, zda samostatně postulovaný algebraický člen může odstranit 12-rozměrné jádro rekonstrukce.

Nechť V má nenulovou normu, g je Lorentzovská a K=K0+C, kde C_{a mu b}=-C_{b mu a} a C_{a mu b} V^b=0. Zde je K0 partikulární kovariantní lokální rekonstrukcí z kanonických definic a C je její příčná odchylka. Uvažujme pomocný funkcionál

S_C = (lambda/2) int d^4x sqrt(-g) C_{a mu b} C^{a mu b},

s nenulovou reálnou lambda, přičemž pro *omezenou* variaci podle C považujeme g,V a K0 za pevné. Tento funkcionál je **zkušebním členem**; lambda ani partikulární K0 nejsou vybrány uzamčenými axiomy UBT. Zvolené V nenulové normy zajišťuje dobře definovaný projektor na svůj ortogonální doplněk.

Pro každé mu patří antisymetrická dvojice (a,b) do Lambda^2(V_perp); její indukovaná metrika je tedy pro V nenulové normy nedegenerovaná. Protože je nedegenerovaná také metrika na indexu mu, je omezená kvadratická Hessova matice ve všech 12 složkách nedegenerovaná. Eulerova–Lagrangeova rovnice pro lambda != 0 bez dalších částí závislých na C má jednoznačné řešení C=0. Pro časupodobné V tvoří 12 složek čtyři kopie trojice prostorových dvouformových složek. V ortonormálním klidovém rámci je Hessova matice nenulovým diagonálním násobkem diag(-1,-1,-1,+1,+1,+1,+1,+1,+1,+1,+1,+1), přičemž celkové znaménko závisí na konvencích signatury a pořadí. Zejména je tato kvadratická forma v Lorentzově signatuře indefinitní: stacionarita nedokazuje kladné energetické minimum.

Obecněji, pokud další členy poskytují příčný lineární zdroj J bez dalších nelineárních členů závislých na C, dává S_trial=S_C+int sqrt(-g) J^{a mu b} C_{a mu b} řešení C=-lambda^{-1} P_transverse J s odpovídajícími polohami horních/dolních indexů. Jde o algebraický vztah; nevyvozovat ztotožnění s fyzikálním spinovým proudem bez odvození vazby.

Úplná variace pouze v Theta není omezenou variací delta_C. C není prokázaným nezávislým fundamentálním stupněm volnosti. Je-li již definováno C=C[Theta], musí se použít řetězové pravidlo pro delta_Theta C a zahrnout implicitní variace g,V,K0. Alternativní zacházení s C jako pomocnou integrační proměnnou je jinou kandidátní formulací, která musí být zdůvodněna jako ekvivalentní a vázaná, nikoli tiše přijata. Obecný člen křivosti R(omega0+C) i látkové vazby zavádějí další závislost na C; jejich úplné Eulerovy–Lagrangeovy rovnice mohou výsledek C=0 změnit. Vliv na torzi, lokální Lorentzovu/difeomorfní symetrii, kinetický hlavní symbol, Hamiltonovy vazby, pozitivitu a fyzikální módy zde není prokázán.

**Závěr:** algebraické 12-rozměrné jádro *lze odstranit přidaným kvadratickým pomocným členem*, ale jde o existenční konstrukci, nikoli selektor dynamiky nebo akce UBT bez dalších axiomů. Další test: zda stejný invertibilní příčný operátor plyne z kanonicky zdůvodněného stávajícího Palatiniho/torzního sektoru nebo z variační identity pouze v Theta bez nového volného postulátu.

Východiska: canonical/CANONICAL_DEFINITIONS.md §3; research_tracks/action_selection/composite_contortion_kernel.en.md; transverse_contortion_dual.en.md; contortion_stabilizer_invisibility.en.md.
