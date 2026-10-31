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

<!-- BILINGUAL-UNIT: physics-closure.free-jet-tensor -->
## Test hlavní tensorové části volného jetu

[Tensorový výpočet volného jetu](free_jet_torsion_principal_2026_10.cs.md) dovoluje zakřivené Lorentzovy jety a neomezenou reálnou dilataci na časupodobné izotropní větvi. Zadaná rodina kvadratické torze znovu získá časový tensorový kinetický člen s kladnou normalizací Einsteinova znaménka, ale algebraická variace všech pomocných rotačních složek jetu odstraní prostorový TT gradient pro každou volbu koeficientů včetně singulárních. Jde o nutnou překážku v hlavním bloku, nikoli úplný počet módů. Regulární přesné stacionární pozadí v původních polích není Einsteinovo pro žádnou kosmologickou konstantu. Než tato rodina obnoví tensorový vlnový operátor GR, potřebuje další odvozený zákon konexe nebo funkcionál; mikroskopický výběr zůstává otevřený.

<!-- BILINGUAL-UNIT: physics-closure.composite-connection-rank-20261031 -->
## Variace fyzikální Lorentzovy konexe: přesná hranice normálového kokernelu

[Dvojjazyčný přesný audit projekce](composite_lorentz_variation_rank_2026_10.cs.md)
neopakuje dřívější výsledky Cartana, Holsta ani split-jetu.
Pro pevný neizotropní reálný nosič X vyvolá porucha **čistě
fyzikální Lorentzovy** konexe změny tetrády s hodností 12,
ale odezva kompozitní kanonické metriky má hodnost **9**:
v tomto jednom variačním kanálu chybí normálová Eulerova
projekce podél prostoročasového vektoru V indukovaného
nosičem. Odlišná *relativní* reálná dilatace obnoví hodnost
**10** algebraicky, ale nejde o vybranou fyzikální konexi.

Ve srovnávacím Cliffordově modelu nižšího řádu s pevnými
gama maticemi dávají předchozí spinová kontrakce 24 ku 8
a metrická projekce s hodností 9 společnou mapu 24 ku 16
s jádrem dimenze **8**. Jde o bodové algebraické počítání
viditelnosti, nikoli o větu o fyzikálních módech mimo
rovnice pohybu; úplný operátor variuje gama matice i křivost.
Další mikroskopickou branou je dovolený variační svazek
jediné Theta a přežívající normálová rovnice po všech
vazbách, nikoli nezávisle převzatý Palatiniho člen nebo
volně vybraná konexe. Přesné testy 11/11;
C_working, dynamická akce OPEN.

<!-- BILINGUAL-UNIT: physics-closure.normal-transport-adjoint-20261031 -->
## Eulerova variace nosiče: transport je slabší než normálová metrická rovnice

[Přesný lokální příklad formálně adjungovaného jádra](composite_normal_transport_adjoint_2026_10.cs.md)
navazuje na výsledek metrické variace hodnosti 9 při
ryze fyzikální Lorentzově konexi z PR #817.
Při pevné škále, regulární e=D_omega X/s a nezávisle
variované Lorentzově omega je Eulerova rovnice nosiče
kovariantní divergencí tetrádové Eulerovy hustoty.
Když zmizí zdroj konexe C_omega při pevné tetrádě,
společné rovnice nosiče a Lorentzovy konexe stále
připouštějí P^mu_a=lambda V^mu X_a s
partial_mu(lambda V^mu)+s lambda=0 namísto lambda=0.
Hladká časupodobná oblast s X=x a lambda=t^-5
poskytuje **nenulový symetrický metrický Eulerův zdroj**,
který anuluje všech 24 Lorentzových variací i všechny
4 Eulerovy rovnice nosiče.

Jde o zkonstruovaný formálně adjungovaný zdroj,
NIKOLIV o stacionární řešení nedokončené S_UBT
ani o no-go na úrovni fundamentální akce.
Dříve známá nezávisle variovaná relativní dilatace w
tento zbytkový zdroj algebraicky detekuje, avšak její
fyzikální přípustnost a dynamika stále vyžaduje jedinou
vybranou fundamentální akci.
11/11 přesných kontrol SymPy; C_working, akce OPEN.

<!-- BILINGUAL-UNIT: physics-closure.theta-normal-adjoint-20261031 -->
## Úplná variace X a fyzikální Lorentzovy konexe: normálové adjungované jádro

[Přesný omezený audit adjungované mapy](theta_normal_adjoint_kernel_2026_10.cs.md)
jde za dřívější výsledek hodnosti 9 při pevném X a variuje
původní Lorentzovo reálné pole X i jeho fyzikální Lorentzovu
konexi. Eulerova rovnice pole je kovariantní divergencí
hustoty nezávislé tetrádové Eulerovy rovnice, NIKOLI
celou rovnicí tetrády.

Nenulový normálový zdroj E^mu_a=h V^mu X_a je neviditelný
všem antisymetrickým variacím konexe. Lokální transportní
rovnice prvního řádu pro h anuluje i jeho Eulerovu
variaci pole. Explicitní časupodobný zdroj h=(-X^2)^(-5/2)
a předepsaný EXTERNÍ funkcionál metrického zdroje dokládají
obě vyrušení v 13 nezávislých přesných testech SymPy.
Test je zesílen neplochou stabilizátorovou konexí SO(3)
s omega_mu X=0: skutečná definující tetráda zůstává
regulární a společné normálové adjungované jádro přetrvá.
Druhá homogenní transportní rodina potvrzuje lokální
nejedinečnost profilu, nikoliv fyzikální propagující módy.
Úplný omezený ověřovač má nyní 13 přesných testů SymPy.
Externí funkcionál NENÍ přípustnou mikroskopickou akcí UBT
a neplyne z něj žádné fyzikální neeinsteinovské řešení.

Úkolem výběru akce je nyní určit, zda se SKUTEČNÝ obraz
Eulerových zdrojů vybrané akce jediného komplexního Theta
protíná s tímto formálním jádrem po zahrnutí fyzikálních
Cartanových zdrojů, všech Cliffordových stupňů, relativních
jetů, hranic a vazeb. C_working; dynamika jediného Theta
zůstává OPEN.

<!-- BILINGUAL-UNIT: physics-closure.exact-relative-weyl-norm-gate -->
## Exaktní relativní dilatace: normálové obnovení a normová degenerace

[Dvojjazyčný audit exaktní Weylovy selekce](exact_relative_weyl_norm_gate_2026_10.cs.md)
navazuje na dříve známou konstrukci uzavřené relativní
dilatace a nevydává ji za nový mechanismus pole.
Je-li exaktní skalár phi variován NEZÁVISLE na X,
spřažená variace delta X=epsilon X, delta phi=-epsilon
dává delta e=epsilon e bez derivací epsilon.
S dřívějším 9-rozměrným Lorentzovým metrickým obrazem
dosáhne bodová odezva hodnosti 10 a zachytí normálový
formální Eulerův zdroj z PR #819.

Musí-li však být phi **Lorentzovsky invariantní
ultralokální funkcí pouze druhé mocniny X**,
jediná kompenzační volba je phi=-log(abs(X squared))/2.
Ta vynutí nulovou kontrakci X s e, takže regulární
tetráda a její kanonická metrika sharp degenerují
(hodnost nejvýše 3). Výsledek je omezeným no-go
pro tuto normovou cestu, nikoli pro úplné komplexní
Theta, jeho nezávislé Cliffordovy stupně, derivované
uzávěry či nedokončenou jedinou akci.
11 přesných regresí SymPy; mikroskopický výběr dynamiky OPEN.

<!-- BILINGUAL-UNIT: physics-closure.full-theta-hermitian-relative-20261031 -->
## Úplné Theta: relativní člen z hermitovského determinantu a zakřivená metrika sharp

[Dvojjazyčný audit celého Theta](full_theta_hermitian_compensator_2026_10.cs.md)
přebírá existující hermitovský/antihermitovský rozklad TÉHOŽ
bikvaternionu se čtyřmi komplexními složkami. Na nedegenerované
oblasti s pozitivním hermitovským H vynucuje požadavek,
aby celý definující jet zůstal na klasickém řezu i-Herm,
spolu s bezestopou spinovou konexí SL(2,C) relaci
w=-d log(det H)/2. Zbývající úplná maticová podmínka
požaduje kovariantně paralelní normalizované H;
samotné vybrání w z její stopy to nezajišťuje.

Tento relativní jet závislý na již existujícím poli
umožňuje lokální škálovací variaci PŮVODNÍHO Theta s
delta e=epsilon e a nenulovým párováním normálového
Eulerova zdroje bez samostatného skalárního pole.
Explicitní příklad neploché metriky sharp má
det e=-1-4ab z^2, R^x_yxy=-12ab v prostorovém počátku
a nekomutující křivost SU(2). Celá původní metrika
sharp a Cliffordův antikomutátor 4 krát 4 se kontrolují
ve 20 přesných lokálních regresích SymPy.

Mechanismus je podmíněnou kinematikou, nikoli výběrem
mikroskopické akce. Pozitivní H omezuje spinovou holonomii,
kovariance centrální komplexní fáze není automatická
a hermitovský determinant není holomorfní funkcí
neomezeného komplexního pole. Skutečné rovnice konexe,
vazby fyzikální torze a redukovaná zdravá dynamika
zůstávají OPEN.

<!-- BILINGUAL-UNIT: physics-closure.dynamics-reuse-H-MM-adjoint -->
## Integrovaný audit dynamiky a odvozená H-MM adjungovaná brána

[Souhrnná evidence](dynamics_reuse_hermitian_mm_adjoint_2026_10.cs.md)
výslovně používá existující podmíněnou akci GR, důkazy
Palatiniho/Cartana a split-jetu, ADM módy i prokázanou
neurčenost fundamentální akce. Přidává novou omezenou větu
o **injektivitě formální diferenciálně adjungované mapy**:
pro čistě gravitační přenos již vybrané MM/Palatiniho akce
vynutí volné algebraické variace K_J, původní Eulerova rovnice
X a společné přeškálování H/X celou tetrádovou Eulerovu
rovnici, i když relativní jednofoma je odvozená jako
w=-d ln(det H)/2 místo volně variované. Následně plyne
úplná Cartanova rovnice při pevném e.
15/15 lokálních přesných regresí SymPy prošlo.

**Zásadní oddělení konexí:** varpi je definující jetový spin paralelizující H a omega je nezávisle variovaný fyzikální spin v geometrické akci. Starší pomocnou souřadnici lze posunout jako K_J=K_old+omega-varpi; tato oddělená proměnná není vybrána původním bimodulem celého Theta. Ztotožnění varpi s fyzikální omega bez torze by vynutilo paralelní časupodobný směr a vyloučilo obecná Einsteinova vakua s nenulovým Lambda. Důkaz nezajišťuje úplnou ekvivalenci množin řešení bez tohoto oddělení.

**Nepřekročitelná brána reprezentace:** předpokládá se
samostatné reálně lineární pomocné působení K_J na jet X.
Stejný spinový koeficient SL(2,C) působící na H i X
tento předpoklad porušuje: realita H vyloučí boostové
směry potřebné pro hodnost. Pouze antihermitovská projekce
není komplexně lineární na neomezeném Theta.
Úplný dvoustranný/gradovaný intertwiner a jeho přípustná
akce, další komplexní sektory i fyzikální vazby zůstávají
OPEN. Nebyl přijat další gravitační ansatz.

<!-- BILINGUAL-UNIT: physics-closure.full-theta-graded-reallinear -->
## Ekvivariantní gradovaný pomocný jet celého Theta: reprezentační brána v reálně lineární kategorii

[Dvojjazyčná přesná konstrukce](full_theta_reallinear_graded_jet_2026_10.cs.md)
nezavádí nové fundamentální pole ani gravitační funkcionál.
Algebraický pomocný tenzor K z algebry sl2(C) působí jen
na již existující antihermitovskou složku P_-(Theta),
ve tvaru K P_-(Theta)+P_-(Theta) K†. Tento **reálně
lineární** gradovaný jet je přesně Lorentzovsky
ekvivariantní vůči lokální kongruenci SL2(C) a zachovává
podmínku paralelnosti H i kanonickou centrální metriku
sharp. Nezávislé K na neizotropním nosiči má hodnost 12
v odezvě tetrády; dříve odvozené relativní w z determinantu
vyruší gradienty lokálního REÁLNÉHO přeškálování.

Tatáž věta vylučuje nenulové KOMPLEXNĚ lineární mapy
na Mat2(C) anulující všechny hermitovské směry.
Sestrojený gradovaný jet není ekvivariantní vůči
nezávislé centrální komplexní fázi. Již dříve víme,
že tato fáze není homogenní kalibrací zamčené metriky
sharp (starší věta #701); nejde o nové fázové no-go.
18 přesných lokálních regresí SymPy pokrývá výsledek.
Předchozí podmíněná MM věta o přenosu Eulerových rovnic
může použít tuto **explicitní kandidátní reprezentaci**,
avšak mikroskopický výběr akce, přípustnost fáze/času,
komplexní hmota a Diracovy vazby zůstávají OPEN.

<!-- BILINGUAL-UNIT: physics-closure.complex-time-graded-reflection-fork -->
## Volba přípustné větve komplexního času pro existující gradovanou reálně lineární konexi

[Přesný dvojjazyčný audit větví](complex_time_graded_reflection_fork_2026_10.cs.md)
PŘEBÍRÁ starší kanonickou interpretaci skalárního vlákna
a no-go přísné Lorentzovy holomorfie ve všech rámcích.
Lokální hladká větev Theta(x,psi) zachovává dagger-gradovaný
operátor K lokální bez požadavku holomorfie tau=t+i psi.

Redukovaný PŘÍSNĚ holomorfní sektor může nahradit dagger
Schwarzovým zrcadlením F*(tau)=F(conjugate(tau))†:
zachovává holomorfii polí i transformovaného Lorentzova jetu.
Zároveň však používá ZRCADLENÝ bod psi. Pro každý konečný
řád jetu N existuje polynom s nulovým N-jetem v mimoreálném
tau0 a nenulovou zrcadlenou hodnotou tamtéž.
Náhrada proto není lokálním diferenciálním operátorem
konečného řádu pro obecné pole na kompaktním skalárním vlákně.

Globálně periodický analytický hermitovský příklad má
vinutí determinantu n a holonomii relativního členu (-1)^n;
normalizované H změní na lichém oběhu znaménko.
Jde o podmíněné globální topologické kontroly,
nikoli o fyzikální předpovědi částic.
Výsledek pokrývá 17 přesných testů. Dřívějších
33 testů gradované/MM větve zůstává ve stejném CI.
Výběr akce jediného Theta, kinetická dynamika psi
a redukce fyzikálních vazeb zůstávají OPEN.
