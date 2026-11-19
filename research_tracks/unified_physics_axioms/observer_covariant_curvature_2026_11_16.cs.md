<!-- BILINGUAL-UNIT: observer-covariant-curvature-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact GR comparator; novel observer-information proposal remains conjectural.
UBT-AI-PROVENANCE-END
-->
# Kovariantní slapové zakřivení pro libovolného pozorovatele v GR — základ Relativity na druhou

<!-- UNIT: status -->
## Rozsah a status tvrzení
[PŘESNÝ GR KOMPARÁTOR / INFORMAČNÍ HYPOTÉZA OTEVŘENÁ / OPEN] Pracujeme s jedinou Lorentzovskou metrikou a společným Riemannovým tenzorem. Závislost měřených slapových složek na pozorovateli je již součástí GR. Samostatně lze zkoumat pozorovatelsky podmíněný informační *odhad* geometrie, ale uvedené vzorce jej neimplikují. Nejde o skalární invariant druhé mocniny křivosti R^2. Neměníme uzamčené kanonické Theta, kovariantní tetrádu ani metriku UBT.

<!-- UNIT: general -->
## Libovolný pozorovatel a boost
```text
signature=(-,+,+,+),  u.u=-1, n.n=1, u.n=0
h_ab(u)=g_ab+u_a u_b
E_ab(u)=R_aμbν u^μ u^ν
v=gamma (u+beta*n), gamma=(1-beta^2)^(-1/2)
E_ab(v)=gamma^2 [E_ab(u)+beta*R_aμbν(u^μ n^ν+n^μ u^ν)
                          +beta^2*R_aμbν n^μ n^ν]
E^obs_ij(v)=e'_i{}^a e'_j{}^b E_ab(v)
Schwarzschild k=GM/(c^2 r^3):
E_static/k=diag(-2,1,1)
tangential boost (along e2): E_tangent/k=diag(-gamma^2*(2+beta^2),1,gamma^2*(1+2*beta^2))
radial boost (along e1): E_radial/k=diag(-2,1,1)
Kretschmann R_abcd R^abcd=48*k^2, both observers
```
Vzorce platí bodově pro libovolné Lorentzovské zakřivení při zvolené znaménkové konvenci. Skutečně naměřené složky druhého pozorovatele vyžadují přenesenou/místní ortonormální tetrádu e'_i kolmou na v. Elektrická slapová projekce Riemannova tenzoru E_ab(v) je kolmá na v, nemusí však být beze stopy: g^ab E_ab(v)=R_munu v^mu v^nu, s výhradou zvolené konvence Riemannova a Ricciho tenzoru. Ve vakuu je beze stopy. Obecný transformační vzorec nepotřebuje Einsteinovy rovnice, pouze tenzorovou algebru.

<!-- UNIT: vacuum -->
## Vakuový Weylův tenzor a celé zakřivení
Ve vakuu R_ab=0 je elektrický slapový tenzor elektrickou částí Weylova tenzoru. Magnetická Weylova část rovněž závisí na rychlosti pozorovatele a při boostu se obecně mísí s elektrickou částí. Pozorovatelsky závislé elektrické normy nejsou skalárními invarianty celého zakřivení. Například tečný boost ve Schwarzschildově geometrii dává E'_ij E'^{ij}-E_ij E^{ij}=18*k^2*beta^2/(1-beta^2)^2, ale Kretschmannův skalár zůstává 48*k^2. Při radiálním boostu podél hlavního Weylova směru zůstávají tři elektrická vlastní čísla stejná; změna rychlosti tedy nemusí změnit každé slapové měření. Statický pozorovatel ve Schwarzschildově geometrii zrychluje; boostovaná soustava je okamžité lokální porovnání, nikoli automaticky geodetický vlak.

<!-- UNIT: operational -->
## Operační rozdíl: vlak a světlo
Volně padající hmotné těleso sleduje v běžné GR časupodobnou geodetiku a testovací světelný paprsek nulovou geodetiku stejné fyzikální metriky. Hmotný vlak nemusí být ve volném pádu; jeho zrychlení je samostatný negeodetický efekt. Foton nemá klidovou soustavu a není pozorovatelem s časupodobnou čtyřrychlostí. Odchylka geodetik popisuje relativní zrychlení volně padajících těles pomocí R(u,xi)u při odpovídající znaménkové konvenci. Prostorový řez, změna souřadnic, relativní Lorentzův boost a rozdílná informace jsou odlišné efekty.

<!-- UNIT: information -->
## Přesné rozhraní k silnější hypotéze Relativity na druhou
Nechť existuje univerzální fyzikální geometrie g[Theta] v klasickém limitu a I_O označuje fyzikálně dostupná relační data pozorovatele O. Předběžný odhad g_hat[Theta|I_O] musí být (i) kovariantně definovaný tenzor/podmíněný objekt s explicitním pravděpodobnostním prostorem nebo prostorem stavů, (ii) konzistentní při porovnání společných experimentů a (iii) při úplné relevantní klasické informaci se musí redukovat na totéž univerzální g. Naivní složkové podmíněné středování koeficientů metriky není obecně difeomorfně invariantní bez relační identifikace bodů; nepoužívat je jako definici. Žádná informační dynamika zde zatím odvozena není. Nový fyzikální princip vyžaduje invariantní měřitelný zbytek, nikoli známý boostovaný slapový tenzor.

<!-- UNIT: tests -->
## Rozhodující testy UBT
T1. Na skutečné on-shell kanonické geometrii Theta reprodukovat místní Riemannův tenzor pro libovolný rámec a Schwarzschildovy radiální/tečné referenční případy.
T2. Spočítat Ricciho i Weylovu část v hmotových pozadích, například FLRW; oddělit zrychlení zvolené kongruence pozorovatelů od zakřivení.
T3. Teprve po T1–T2 definovat kovariantní zobrazení pozorovatelské informace, dokázat slučitelnost sdílených měření a porovnat invariantní předpovědi.
T4. Vyžadovat klasický limit principu ekvivalence a nezavádět další nezávislé fundamentální metriky pozorovatelů.

<!-- UNIT: checks -->
## Stav ověření
Schwarzschildův referenční výsledek plyne z přesných kontrakcí tenzorů v tetrádě; samostatný ověřovací program SymPy je v tools/verify_gr_observer_generalization_2026_11_16.py. Jde o známou algebru GR; odvození Schwarzschildova řešení z Theta zůstává otevřené. Nezávislé dvojjazyčné významové ověření, Lean, úplné CI repozitáře a spřažené rovnice polí UBT pro tento dokument dosud NEBYLY dokončeny.
