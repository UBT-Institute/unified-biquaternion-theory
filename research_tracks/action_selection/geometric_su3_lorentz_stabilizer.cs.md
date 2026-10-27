<!-- BILINGUAL-UNIT: geometric-su3-lorentz-stabilizer -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional pointwise equivariance obstruction, not universal no-go.
UBT-AI-PROVENANCE-END -->
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

# Cesta A: ekvivariantní barevný projektor SU(3) nelze vybrat samotnou Lorentzovou tetrádou

**2026-10-26; nový přesný bodový argument se stabilizátorem.** Předchozí `mm_geometry_colour_selection.en.md` ukázal neslučitelnost pohyblivého projektoru Theta s kalibračními posuny split-jet. Zde testujeme, zda lze náhradní projektor vytvořit **pouze** z E, omega bez dodatečných voleb.

V bodě vezměme invertibilní tetrádu E. Konstrukce používající pouze tetrádu, její metriku a kanonickou orientaci, bez derivací či vnějších polí, která je kovariantní vůči nezávislým lokálním transformacím Lorentzova rámce, nemůže vybrat nenulový časupodobný Lorentzův vektor n(E) ve své vnitřní vektorové reprezentaci. Ekvivalentně má ortonormální rámec z hlediska vnitřních dat metriky/orientace úplnou vlastní ortochronní Lorentzovu izotropii, takže kanonicky vybraný vektor by musel splňovat Lambda n=n pro každé Lambda v SO^+(1,3). Prostorové rotace by n v libovolném zvoleném rámci vynutily v časovém směru a následné boosty by vynutily n=0. To odporuje n† G n=1. Ze samotné metriky/tetrády tedy neplyne žádný algebraicky přirozený projektor kladné přímky hodnosti jedna P_+=nn†G ani jeho pohyblivá záporná trojrovina SU(3).

Jde o podmíněný **no-go výsledek pro přirozenou konstrukci nultého řádu**, nikoli zákaz používání křivosti, derivací, nelokálních dat či dynamicky vybraného časupodobného pole. Složky tetrády vůči libovolné souřadnicové mapě mohou vybrat směr, ale tím porušují požadavek přirozenosti a fakticky zavádějí data pozorovatele/foliace. Metrická křivost může vybrat vlastní vektory na obecných zvláštních pozadích, avšak například Minkowského a maximálně symetrické časoprostory žádný jednoznačný takový časupodobný směr nemají. Je nutné ošetřit degenerované vlastní hodnoty a singulární vrstvy křivosti.

**Rozhodnutí:** samotná algebraická geometrie tetrády neposkytuje univerzálně definované `P_+(E)` invariantní vůči split-jet se stabilizátorem SU(3) kanonické časupodobné přímky. Pro pokračování cestou A bez nového principu buď (i) vytvořit lokální projektor z křivosti na omezených pozadích a dokázat jeho regularitu/Lorentzovu kovarianci i slučitelnost s dynamikou; nebo (ii) zachovat fyzikální barevnou normálu Theta a vypočítat její vazby a zdravost kinetiky. Ani jedna možnost zatím nezakládá propagující gluony SU(3).

Přesný symbolický příklad: `tests/test_geometric_su3_lorentz_stabilizer.py`.
