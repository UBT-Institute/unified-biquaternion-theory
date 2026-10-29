<!-- BILINGUAL-UNIT: palatini_cartan_compatibility_gate -->
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


# Podmínka Palatiniho–Cartanovy kompatibility pro geometrii Theta s jednotkovou kovariantní derivací vektoru

**Stav: podmíněný geometrický/variační test kompatibility (2026-10-25), nikoli odvození hlavní akce UBT.**

## Dvě odděleně prokázané složky
1. Kanonický lokální reprezentant s nenulovou normou: s jedinou metricky kompatibilní Lorentzovou konexí Gamma, Theta=sqrt(N0) V^a u_a a nabla^Gamma_mu V^nu=delta_mu^nu, ekvivalentně g_mu nu=nabla^Gamma_mu V_nu. Jeho torze je obecně nenulová a rekonstruující kontorze obsahuje 12-rozměrné příčné jádro.
2. Pro nezávisle variovanou **minimální** Hilbertovu–Palatiniho akci s invertibilní tetrádou je rovnice konexe algebraická a invertibilní ve 24 složkách torze, schematicky M(T)=kappa spin_current. Pokud spin_current=0, pak T=0 a Gamma=Gamma_LC. Obě tvrzení platí pod podmínkou zvolené Palatiniho akce a variací nezávislé konexe.

## Silná překážka kompatibility
Pokud se tyto *dva* požadavky uloží současně při mizejícím spinovém proudu, pak
```
nabla^LC_mu V^nu=delta_mu^nu.
```
Komutace derivací bez torze okamžitě dává
```
R^rho_{sigma mu nu}(LC) V^sigma=0.
```
Obecné zakřivené geometrie nemají nenulový vektor s kovariantní derivací rovnou identitě; zejména Schwarzschildův vnějšek je vyloučen stávajícím kanonickým no-go výsledkem. Prostý výběr Palatiniho řešení torze s nulovým spinem tedy obecně není slučitelný s uzamčenou rekonstrukcí čistou Lorentzovou dvojicí. Jde o podmíněnou neslučitelnost větví, NIKOLI no-go pro všechny limity UBT/GR.

Ve větvi s torzí dává komutace úplné afinní kovariantní druhé derivace při správném zacházení s dodatečným derivačním indexem, s konvencí [nabla_mu,nabla_nu] působící na kontravariantní vektor = R^rho_{sigma mu nu} V^sigma - T^lambda_{mu nu} nabla_lambda V^rho pro *tenzorové druhé derivace*,
```
R^rho_{sigma mu nu}(Gamma) V^sigma = T^rho_{mu nu}
```
pokud nabla_mu V^rho=delta_mu^rho. Jde o identitu integrability, v níž torze může vyvažovat křivost, nikoli o novou nezávislou rovnici vybírající 12 složek jádra. Znaménka závisejí na konvenci torze a R.

## Nenulový spinový zdroj: skutečná podmínka výběru

Nechť K_Cartan[e,spin_current] označuje jednoznačnou metricky kompatibilní kontorzi určenou *zvolenou* rovnicí konexe HP + látky a K0[e,V] partikulární Gaussovu kontorzi rekonstruující tetrádu Theta. Kompatibilita vyžaduje
```
(K_Cartan)^rho_{mu nu} V^nu = W_mu^rho
```
kde W je defekt LC derivace z canonical/CANONICAL_DEFINITIONS.md, ekvivalentně
```
K_Cartan - K0 belongs to ker(K -> K V).
```
Jde o netriviální 12-složkovou podmínku obrazu na spinový zdroj spolu se zvolenými e,V. Dalších 12 algebraických složek kontorze je pak Cartanovou rovnicí určeno **teprve po** zadání zdroje; není zaručeno, že přípustný spinový proud odvozený z Theta tuto podmínku splňuje.

Úplná variace pouze v Theta **není** variací HP s nezávislou omega. Eliminace nezávislé pomocné omega její rovnicí je v kandidátní teorii přípustná pouze s pečlivým důkazem ekvivalence a vazeb; pokud byla omega od počátku stanovena jako kompozitní, variace musí zahrnout delta omega[Theta] i indukované delta e[Theta]. Je nutné dosadit a ověřit stávající výsledek spinového proudu látky v čisté párové reprezentaci se správnými znaménkovými konvencemi a nosičem reprezentace; obecné symbolické J není odvozeným zdrojem UBT. Nevybírá se zde žádný nový hmotový člen torze ani nastavitelná lambda.

**Další podmínka:** spočítat M(T) promítnuté na 12-rozměrný obraz a jádro kontrakce s V; dosadit skutečný kanonický zdroj a na neplochém pozadí testovat 12 rovnic kompatibility obrazu. Teprve potom existuje možnost dokázat jednoznačnou kompozitní kontorzi a přejít k úplné analýze Hamiltonových vazeb.

Odkazy: canonical/CANONICAL_DEFINITIONS.md §3 (podmíněný GAP-10T-PALATINI, GAP-10I-TORSION-LOCAL), research_tracks/action_selection/{composite_contortion_kernel,transverse_contortion_auxiliary_variation,contortion_stabilizer_invisibility}.en.md.
