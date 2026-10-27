<!-- BILINGUAL-UNIT: transverse_contortion_dual -->
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


# Jádro příčné kontorze jako prostorový duál

**Stav:** přesná bodová algebraická parametrizace podmíněná orientovaným nedegenerovaným Lorentzovým čtyřprostorem a vektorem V nenulové normy. Výzkumná poznámka úrovně C (2026-10-25). Nejde o dynamické pravidlo výběru torze.

## Nastavení

Stávající rekonstrukce určuje K pouze až na C s
```
C_{a m b} = -C_{b m a},  C_{a m b} V^b = 0.
```
Zafixujme orientaci a časoprostorovou objemovou formu epsilon_{abcd}. Potom
```
C_{a m b} = epsilon_{ab cd} V^c Z_m^d,   V_d Z_m^d = 0.
```
Zobrazení Z -> C je izomorfismem ze čtyř kopií, jedné pro každé m, vektorů kolmých k V na jádro kontrakce s V na antisymetrických 2-formách. Plyne to z Hodgeova duálu v 3-prostoru kolmém k V a z nenulovosti normy V. Celkovou normalizaci a konvenci orientace lze zahrnout do definice Z. Pro pevné m jsou rozměry 3 -> 3, tedy 12 pro všechna m.

Pro úplnost lze Z zvolit z C, v závislosti na znaménkových konvencích epsilon, jako konstantní násobek `epsilon^{d a b c} V_c C_{a m b}/V^2`, přičemž násobek určuje kontrakční identita epsilon. Žádná znaménková ani normalizační konvence nemění tvrzení o izomorfismu.

## Rozklad podle teorie reprezentací

Je-li V časupodobné, tvoří Z_m^i v jeho lokálním klidovém rámci pole 4 krát 3. Rozdělme kovektorový index m na časovou a prostorovou část. Časový řádek dává prostorový 3-vektor, zatímco prostorová matice 3 krát 3 se rozkládá na:
- skalární prostorovou stopu: 1;
- antisymetrickou část: 3;
- symetrickou bezestopou část: 5.

Tedy 12 = 3 + 1 + 3 + 5 vzhledem ke klidové SO(3). Jde o **sektory algebraické reprezentace**, nikoli spiny fyzikálních částic, propagující excitace, generátory SU(3) nebo zákon chirálního výběru. Pro prostorupodobné V je stabilizátorem SO(1,2) a názvosloví SO(3) se nepoužije.

Další torzní nebo variační rovnice může tyto sektory eliminovat či propojit. Samotná uzamčená kinematika Theta to nedělá.

## Proč nastavení Z=0 není odvozením

Partikulární Gaussova rekonstrukce K0 nastavuje jádro C=0, ale tím vybírá jedno řešení nedourčené algebraické rovnice. Taková volba není stávajícími rovnicemi UBT zdůvodněna jako kanonický dynamický výběr a nelze ji tiše použít k tvrzení o jednoznačném Hamiltoniánu, Diracově vazbě nebo gravitonových módech.

## Další reprodukovatelná kontrola

Společně linearizovat vázané zobrazení Theta -> E -> g a zvolenou kompozitní dvojici (A[Theta], B[Theta]) na ploché oblasti mimo nulový kužel. Výslovně zahrnout variace sektoru Z, lokální Lorentzovy a difeomorfní směry i veškeré kalibrační vazby. Testovat, zda výsledné rovnice skutečně omezují všech 12 směrů jádra. Teprve potom uvažovat hlavní symboly a počítání fyzikálních módů ve fázovém prostoru.

**Zdroje:** canonical/CANONICAL_DEFINITIONS.md (lokální rekonstrukce torze), research_tracks/action_selection/composite_contortion_kernel.en.md (hodnost 12), research_tracks/action_selection/linearized_flat_theta_pure_gauge_no_go.en.md (omezený plochý no-go).
