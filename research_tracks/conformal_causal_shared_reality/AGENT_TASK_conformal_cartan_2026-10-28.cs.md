<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: conformal-cartan-agent-g1.scope -->
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

# Zadání agenta: konformní Cartanův G1 z Theta, kauzality a sdílené reality

**2026-10-28 · PR #809 · C_working · OPEN.** Pracuj jen na izolované větvi PR #809. Neměň PR #807, PR #808, kanonické zdroje, claims, původní autorská potvrzení ani rozhodnutí o provenienčních úrovních. Nic nemerguj. Po kontrole G1 práci zastav.

## Výchozí ověřené výsledky [PROVED, omezeně]

Prostuduj RESEARCH.en.md, G1_NEGATIVE_CONTROL.en.md, G1_INDUCED_GEOMETRY.en.md, G1_RT_EXTRA_SOLUTION.en.md, G1_CONNECTION_RANK.en.md a G1_COMPOSITE_WEYL.en.md. Kompozitní reálná dilatace pouze z normy má nulovou křivost; proud komplexního tvaru má nenulovou křivost, ale neprošel přísnou realitní podmínkou neprojektované tetrády. Bodová hodnost 10 metriky nedokazuje propagaci spinových módů. Gradientové vnoření s převzatou Einsteinovou akcí připouští neeinsteinovská stacionární řešení. Jde o omezené výsledky, nikoliv kanonickou fyziku.

## Jediný další přípustný úkol [OPEN]

Sestroj skutečně z Theta odvozené, lokálně kovariantní uzavření konexe nebo zdůvodněný omezený Cartanův systém prvního řádu. Ověř nosič polí a reálný řez, přesný transformační zákon, nedegenerovanou tetrádu, nenulovou křivost, všechny nezávislé variace, metrický Jacobián po vazbách a redukovaný lineární hlavní symbol se dvěma zdravými helicity. Odmítni konstrukce, které skrytě zavádějí volnou solder formu.

Kauzální a informační princip sdílené reality používej jako explicitní testovatelné předpoklady. Samotný překryv kauzálních diamantů neurčuje kladný Weylův faktor metriky. Bez důkazu nezaváděj nový potenciál ani netvrď SU(2,2)-kovarianci, zdravé módy GR či informačně odvozenou akci.

## Ověření a zpráva

Spusť přesné testy:

```bash
python -m pytest -q tests/test_theta_conformal_gate.py tests/test_theta_gradient_solder.py tests/test_theta_induced_geometry.py tests/test_theta_rt_extra_solution.py tests/test_theta_connection_metric_rank.py tests/test_theta_exact_dilation.py tests/test_theta_composite_weyl.py
```

Uveď předpoklady, přesnou algebru, protipříklady, zbývající mezery a stav nezávislého CI. Udrž česko-anglické párové poznámky, C_working a zastavení k recenzi na G1. G2/G3/G4 zůstávají PARKED.

## Kontrola sdílené reality na konečném diamantu [PROVED jako modelová algebra, OPEN jako fyzika]

Viz G1_FINITE_DIAMOND_INFORMATION.en.md a tests/test_theta_finite_diamond_info.py.
Explicitně zadané kauzální uspořádání a libovolná skalární mapa výsledků
z invariantu B(Theta,Theta) vytvářejí konečné stavy konzistentní na překryvu.
Informační Hessian při shodě s referenčním stavem má hodnost jedna na
regulárním osmireálném testovacím nosiči; dva pozorovatelé nerozpoznají
korelaci krajních událostí, kterou neobsahují ani jejich úplné lokální
marginály. Kladné redukované skalární Hamiltoniány i Markovovy modely
s kontrakcí entropie zůstávají při stejné informační rovnováze nejednoznačné.
**Nepovažovat** to za odvození lokální algebry pozorovatelných, kauzálních
kuželů, vybraného Hamiltoniánu, redukce fázového prostoru ani fyzikální akce.

Další informační úkol musí sestavit kauzální diamant, skutečné
kalibračně invariantní pozorovatelné a referenční stav z téže
dynamicky uzavřené geometrie Theta a získat kvantitativní
predikci schopnou vyloučit jinak přípustný generátor.
Nejde o oprávnění povýšit G2 před recenzí G1.
