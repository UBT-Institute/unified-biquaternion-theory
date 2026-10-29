<!-- BILINGUAL-UNIT: physics-closure.scope -->
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

# Audit fyzikálního uzavření: volnost akce a Holstův Hamiltonián s vazbami

**28. října 2026; PR #807; C_working.** Tato zpráva používá stávající kovariantní tetrádu, split-jet a homogenní výpočty. Nevybírá mikroskopickou akci. Efektivní gravitační postulát je `AXIOMATIC_CANDIDATE` s fyzikálními důsledky `CONDITIONAL`. Jeho lokální matematické implikace zůstávají platné při uvedených předpokladech; pozorovací potvrzení UBT z nich neplyne. Zdrojem překladu je angličtina.

<!-- BILINGUAL-UNIT: physics-closure.reuse -->
## Použité výsledky a opravy tvrzení

Věta o hodnosti, pravá inverze split-jet, věta o pomocném multiplikátoru, klasifikace Cliffordových stop, klasifikace potenciálu, determinantový nulový lagrangián a homogenní výpočet křivosti již existují. Příslušnými zdroji jsou `canonical/ACTION.cs.md`, `canonical/gr_closure/gravity_dynamical_postulate.cs.md`, `formal/lean/UBT/GR/VolumePrincipalSymbol.lean`, `research_tracks/action_selection/clifford_palatini_trace_selector.cs.md`, `research_tracks/action_selection/composite_palatin_holst_flrw.cs.md` a `research_tracks/observer_information_hamiltonian_2026_10_holst_causal_selector.cs.md`. Jde o předpoklady s jejich původním rozsahem, nikoli nové objevy v tomto PR.

Obnova Einsteinovy–Lambda gravitace, zahrnutí Schwarzschilda a jeho Regge–Wheelerovy/Zerilliho redukce mají jako tvrzení UBT status `CONDITIONAL`: vyžadují přijatý gravitační funkcionál. Jejich matematická implikace se neruší. Mikroskopický výběr tohoto funkcionálu a přímý výběr řešení finalizovanou rovnicí jediného Theta zůstávají `OPEN_GAP`. Aktuální párová matice tvrzení a strojově čitelný gravitační registr tyto úrovně nyní rozlišují. Starší nepárované registry zachovávají svůj historický text; jejich otevřené mikroskopické mezery nelze chápat jako vyvrácení podmíněné efektivní větve.

Registr alfy zůstává `OPEN_GAP`. Hodnoty poblíž $B\simeq46.28$ jsou fitované/fenomenologické vstupy nebo numerické shody v alternativních vzorcích, nikoli odvození bez volných parametrů. Blízké historické hodnoty nejsou měřenou univerzální konstantou. Algebraické barevné nosiče nedokazují propagující QCD a označení vinutí neodvozují tři chirální generace. Žádný podpis autora, datum osvědčení ani úroveň provenience se nemění.

<!-- BILINGUAL-UNIT: physics-closure.proof-outcome -->
## Výsledek důkazu nezávislého na rozměru

Autor upřesnil, že počet složek je předběžný; tento audit nevybírá náhradní prostor hodnot. Nová věta používá libovolný reálný prostor variací. V uvedené holé rodině se shodnou dvojicí/volným jetem dává stacionarita pouze kritickou nulu objemové váhy a připouští explicitní neeinsteinovskou metriku. Tato rodina tedy neodvozuje GR. Jiné kinetické kanály, dynamicky vybrané uzavření jetu nebo odvozená kvantová efektivní akce zůstávají mimo tuto překážku. Podrobný důkaz, příklad s původním vyčítáním a hranice formalizace jsou v příloze o holé akci. Přibylo 7 deklarací Lean; úplný funkcionální/PDE závěr nepředkládáme jako zcela formalizovanou prostoročasovou větu.

<!-- BILINGUAL-UNIT: physics-closure.details-index -->
## Podrobná odvození

Toto je jediný přehled auditu; párové přílohy zachovávají podrobné rovnice, předpoklady, důkazy a protipříklady.

- [Rodina akcí a nezávislá variace](physics_closure_action_family_2026_10.cs.md)
- [Hamiltonián s jedinými hodinami a samoduální srovnání](physics_closure_hamiltonian_2026_10.cs.md)
- [Prostor hodnot, symetrie a věta o společné konexi](physics_closure_carrier_2026_10.cs.md)
- [Kontroly fáze, textury a kvocientu](physics_closure_phase_texture_2026_10.cs.md)
- [Reálná dilatace a úplná řetězová variace](physics_closure_dilation_2026_10.cs.md)
- [Důkaz holé akce nezávislý na rozměru](physics_closure_bare_action_2026_10.cs.md)
- [Odezva spinového zdroje a objemová identifikovatelnost koeficientů](physics_closure_spin_source_2026_10.cs.md)

<!-- BILINGUAL-UNIT: physics-closure.prediction -->
## Nejednoznačnost, informační principy a hranice predikce

Pro bezspinové vakuum s nezávislou konexí má celá reálná rodina $b$ stejné metrické rovnice s nulovou torzí. Její gravitační charakteristiky a všechny protokoly omezené na tuto totožnou metrickou větev nemohou rozlišit $b$. To zesiluje existující srovnání omezené na nulovou torzi explicitní kontrolou invertibilního operátoru vakuové konexe. Rozpočty informačního přístupu a kauzální sdílení záznamů omezují protokoly; bez nové vazby nebo pravidla výběru tuto degeneraci neodstraňují. Mimo řešení se operátory liší a torze buzená zdroji nebo jiné hraniční předpisy je mohou rozlišit. Jde o nejednoznačnost při testovaných omezeních, nikoli nemožnost budoucího silnějšího principu.

Na této podmíněné větvi splňuje charakteristika metrické vlny $g^{\mu\nu}k_\mu k_\nu=0$, takže $c_{\rm GW}=c$ jako v GR. [GW170817/GRB170817A](https://arxiv.org/abs/1710.05834) poskytuje publikovanou srovnávací mez $-3\times10^{-15}\le(c_{\rm GW}-c)/c\le7\times10^{-16}$ za předpokladů dané práce o zpoždění emise. Jde o kontrolu základního modelu GR, nikoli rozlišující potvrzení UBT nebo měření $b$. Ze samotného bezspinového vakua neplyne z této rodiny žádná netriviální predikce nad rámec GR. Experiment se zdroji/torzí by nejprve vyžadoval odvodit z téže akce normalizovaný spinový proud a všechny přípustné torzní koeficienty. [Kostelecky–Russell–Tasson](https://arxiv.org/abs/0712.4393) omezují určené vazby fermionů na torzní pozadí; jejich limity nelze přenést na neurčený koeficient UBT. Homogenní srovnávací model není fitovaná kosmologie ani pozorovací predikce.

Přesnou zbývající překážkou je, že nebyla vybrána úplná akce jediného Theta, její zákon složené konexe, její fyzikální kvocient fluktuací ani normalizace zdrojů. Samotná surjektivní kinematická pravá inverze nic z toho nedodává. Úplné prostorové variace, primární/sekundární vazby a stabilita fyzikálních módů zůstávají `OPEN_GAP`. Nejsilnějším novým výpočetním výsledkem je zde Hamiltonián s vazbami a jeho vrstvy závislé na koeficientu pro již určený srovnávací model.

<!-- BILINGUAL-UNIT: physics-closure.verification -->
## Ověření a přesný rozsah formalizace

| Výsledek | Vědecký status | Ověření | Hranice formalizace |
|---|---|---|---|
| Reálná bivektorová inverze, druhá mocnina a nulové jádro | PROVED | `formal/lean/UBT/Hamiltonian/PalatiniHolst.lean`; nezávislá matice v SymPy | Bez odvození polní Cartanovy rovnice |
| Momenty/vazba srovnávacího modelu, nulová kanonická energie, inverze rychlosti, doplnění na čtverec | PROVED | Tentýž modul Lean; přímé diferencování v CAS | Pouze konečné algebraické identity |
| Pokračované kanonické přiřazení GR a překážka vyčítání hermitovskou dvojicí | PROVED | Tentýž modul Lean; `tests/test_holst_selfdual_canonical_gr.py` | Přiřazení je algebraické; přípustná mikroskopická samoduální větev není stanovena |
| Algebra prostoru hodnot, fáze, kalibračního vyrušení a reálných Cartanových rovnic | PARTIAL | Tentýž modul Lean; `tests/test_holst_carrier_assumptions.py` | Šest nových lemmat Lean; přesné maticové příklady ověřuje CAS; obecná klasifikace ekvivariantních bandlů/PDE je LEAN-PENDING |
| Podmíněná variace reálné dilatace a uzavřený de Sitterův příklad | CONDITIONAL | `tools/verify_physics_closure.py`; tentýž test prostoru hodnot | Importovaná akce a odlišený relativní jet; žádný nový postulát UBT ani neomezená Diracova věta |
| Stacionarita holé vážené objemové akce a neeinsteinovský příklad | PARTIAL | `formal/lean/UBT/GR/BareSplitJet.lean`; `firstVariation_at_vacuum`; `tools/verify_bare_splitjet_selection.py` | Algebra/derivace nezávislé na rozměru a konečný spor; hladká funkcionální interpretace a interpretace křivosti je LEAN-PENDING a nezávisle ověřena |
| Úplná homogenní Poissonova matice, Diracovy závorky a vrstvy vazeb | CONDITIONAL | `tools/verify_physics_closure.py`; `tests/test_physics_closure.py` | LEAN-PENDING: definice Poissonových/Diracových závorek a geometrická redukce |
| Konečné diference, kovariance, konvergence trajektorie a přesnost | NUMERICALLY_TESTED | Tentýž spustitelný ověřovač, pevný seed a tolerance | Vybrané regulární vzorky, nikoli důkazy |
| Obecná torzní dynamika jediného Theta a nová fyzikální predikce | OPEN_GAP | Přesné chybějící vstupy jsou uvedeny výše | LEAN-PENDING: úplná akce, variační prostory a vazby PDE |
| Tvrzení, že Palatiniho redukce s jedinými hodinami automaticky ukládá všechny Einsteinovy rovnice | REFUTED | Zachovaný přesný protipříklad normálové vazby | Vyloučen je pouze uvedený homogenní ansatz |

Spusťte `python tools/verify_physics_closure.py` a `python -m pytest -q tests/test_physics_closure.py tests/test_holst_selfdual_canonical_gr.py tests/test_holst_carrier_assumptions.py tests/test_composite_palatin_holst_flrw.py`. Ověřovač vypisuje verze balíčků, každou přesnou kontrolu, seed, chyby konečných diferencí, konvergenci nezávislého integrátoru a rezidua přesnosti. Samostatně spusťte `lake build UBT --wfail`, stávající Lean checker a audit axiomů. Nezkontrolovaný zdroj věty ani úspěšné numerické srovnání nejsou formální ověření. Před sloučením je vyžadováno nezávislé schválení významové shody jazykových verzí; samotná strukturálně shodná translace tuto podmínku neuzavírá.

<!-- BILINGUAL-UNIT: physics-closure.full-spatial -->
## Úplná prostorová dynamika po metrické redukci

Výpočet [úplné prostorové dynamiky](full_spatial_dynamics_2026_10.cs.md) odvozuje lokální závorku změn časových řezů v deklarované rodině redukované kanonické metriky, vybírá Einsteinův poměr stopy a relativní koeficient křivosti a dává úplnou vakuovou evoluci metriky a dva ploché tenzorové módy. Kanonický fázový prostor a požadavek změn řezů mimo řešení jsou explicitní dodatečné předpoklady. Výpočet nevybírá mikroskopickou akci Theta, velikost Newtonovy konstanty, Holstův koeficient ani dynamiku dalších sektorů.

<!-- BILINGUAL-UNIT: physics-closure.spatial-jet-dirac -->
## Kanonická jetová redukce zvolené gravitační větve

[Lokální prostorová Diracova redukce](splitjet_spatial_dirac_2026_10.cs.md) sestavuje ekvivalentní čistě gravitační rodičovskou akci, zachovává posun hybnosti nosiče závislý na poli a eliminuje smíšené bloky pomocných vazeb beze změny základních závorek. Dodatečné jetové proměnné nepřispívají lokálním fyzikálním módem v regulárním souřadnicovém okolí s nenulovou normou. Tím se řeší jetová část mostu k metrickému fázovému prostoru pro zvolenou akci, zatímco původ a kladná normalizace této akce i všechny další komplexní/hmotové sektory zůstávají otevřené.

<!-- BILINGUAL-UNIT: physics-closure.flat-jet-torsion -->
## Test kvadratické torzní akce plochého jetu

[Výpočet torzní akce plochého jetu](flat_jet_torsion_action_2026_10.cs.md) plně variuje deklarovaný konfigurační prostor plochého Lorentzova spojení a uzavřené reálné dilatace. Každá paritně sudá kvadratická torzní akce s konstantními koeficienty se zde redukuje na konformní skalární akci. Kombinace s kladným Einsteinovým znaménkem má záporný redukovaný skalární kinetický směr; opačné znaménko dává kladnou skalární energii, ale žádný tenzorový sektor. Regulární zakřivený příklad na slupce nesplňuje Einsteinovu vakuovou rovnici pro žádnou kosmologickou konstantu. To vylučuje tuto přesnou větev jako původ obecné GR, zatímco neploché jety, jiná relativní působení a mikroskopický výběr zůstávají otevřené.
