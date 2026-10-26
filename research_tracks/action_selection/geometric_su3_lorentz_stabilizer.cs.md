<!-- BILINGUAL-UNIT: geometric-su3-lorentz-stabilizer -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Podmíněná bodová překážka ekvivariance, nikoli univerzální no-go.
UBT-AI-PROVENANCE-END -->
# Cesta A: holá Lorentzova tetráda nevybere kanonický SU(3) projektor

**26. 10. 2026. Přesný bodový argument stabilizátoru.** Navazuje na `mm_geometry_colour_selection.en.md`. Pokud chceme projektor barevného prostoru sestavit jen z tetrády, metriky a orientace bez derivací a externích polí, musíme zachovat lokální Lorentzovu kovarianci. Taková konstrukce však nedokáže vybrat nenulový časupodobný vektor n: ten by musel být invariantní vůči všem rotacím i boostům SO^+(1,3). Rotace vynutí prostorové složky nulové, boosty pak i časovou. Z n=0 nelze sestrojit normalizovaný projektor P_+=nn†G ani náš pohyblivý záporný trojrozměrný prostor s orientovanými rámci SU(3).

Jde o **no-go pro algebraickou konstrukci n z holé geometrie**, nikoli důkaz nemožnosti použít zakřivení, derivace či speciální řešení. Souřadnicově zvolená časová složka tetrády by navíc znamenala skrytý preferovaný rámec. Zakřivení může na některých pozadích vybrat časupodobný vlastní vektor, ale Minkowského či maximálně symetrická řešení ho obecně neurčí a degenerované spektrum je nutné ošetřit.

**Rozhodnutí:** bez dodatečných struktur není přirozený Lorentzovsky kovariantní projektor P_+(E) pro všechny geometrie. Dále zkoumat buď omezenou konstrukci z křivosti včetně singulárních případů, nebo ponechat barevnou orientaci Theta fyzikální a spočítat její dynamickou stabilitu. Samotná SU(3) algebra není odvozením gluonové dynamiky.

Symbolický test: `tests/test_geometric_su3_lorentz_stabilizer.py`.
