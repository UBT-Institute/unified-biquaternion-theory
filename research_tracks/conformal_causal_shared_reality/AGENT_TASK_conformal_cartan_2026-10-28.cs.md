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

## Kontrola invariantních pozorovatelných a projektivní signatury G1 [PROVED / OPEN]

Prostudovat G1_INVARIANT_CAUSAL_BRIDGE.en.md a G1_PROJECTIVE_SIGNATURE.en.md
a testy tests/test_theta_invariant_causal_bridge.py a
tests/test_theta_projective_signature.py. Bodová klasická
podalgebra pozorovatelných generovaná H(Theta) a |det Theta|²
má generickou Fisherovu/Jacobiho hodnost 2 na 8-reálném
testovacím nosiči, ale nevybírá fázově citlivou kauzální metriku
ani při znalosti všech jetů těchto invariantů. Kompozitní
konexe pouze pro fázi tento drift v omezené gradientové
metrice kompenzuje. Pokud **současně** odstraníme fázi i reálné
přeškálování přirozeným B-ortogonálním projektorem na větvi N>0,
šestirozměrný cílový doplněk má inertii (0,6), takže indukovaná
metrika nemůže mít Lorentzovu signaturu. Pro N<0 má doplněk
inercii (2,4) a bodový Lorentzův jet existuje, nikoli fyzikální řešení.

**Další omezená nekruhová kontrola [OPEN]:** na neplochém
regulárním pozadí testovat kalibrační kovarianci čistě fázové
konexe společně s přísnou realitou tetrády i·Herm a vázanou
akcí/hlavním symbolem; alternativně zkoumat, zda UBT připouští
větev N<0. Nevyvozovat ze sdílené reality, že reálné
přeškálování musí být kalibrací, ani nepřidávat bez přiznání
nezávislé soldering pole. Zachovat C_working, G1 PARTIAL a stop
před nezávislou recenzí.

## Hranice reality přímé tetrády [PROVED, omezeně]

Prostudovat G1_PHASE_STRICT_REALITY.en.md a tests/test_theta_phase_strict_reality.py.
Pro Theta=X+iY má čistě fázová kompozitní derivace kolmá k iTheta,
pokud navíc musí ležet v Herm, reálnou hodnost nejvýše tři při
nenulovém Y. Se společnou projekcí fáze a měřítka má přímá
Hermitovská tetráda hodnost nejvýše tři pro jakékoli nenulové Theta
a nejvýše dvě pro nezávislá X,Y. Záporně normovaný čtyřnohý Gramův
příklad vyžaduje nehermitovský jet a neprochází tímto **přímým**
čtením. Explicitně zakřivená čistě fázová Gramova metrika zůstává
Lorentzova, ale její bezestopou imaginární prostorovou derivaci
nelze v kontrolním bodě opravit libovolnou dvoustrannou Lorentzovou
konexí, reálnou centrální dilatací ani centrální fází. Nejde
o univerzální no-go pro jiné tetrádové mapy ani jiné nosiče Theta.

## Další rozhodnutí o přísné realitě [OPEN]

Sestrojit explicitní *nepřímou* tetrádu nebo skutečně kompozitní
necentrální konexi a ukázat přesný lokální transformační zákon,
Lorentzovu realitu, nedegenerovanou tetrádu, zakřivené řešení,
vázané variace a fyzikální hlavní symbol. Pokud tetráda vzniká
faktorizací Gramovy metriky, dokázat, že tato operace plyne z UBT
a nevkládá volnou tetrádu nebo převzaté Einsteinovy rovnice.
Nepovyšovat G1 bez této brány a nepovažovat informace konečných
kauzálních diamantů za dokončený výběr dynamiky.

## Oprava: reálná geometrie je složenou veličinou komplexního Theta [PROVED, omezeně]

Prostudovat G1_COMPLEX_REAL_COFRAME.en.md a
tests/test_theta_phase_real_derived_coframe.py. Nepožadovat
Hermitovost přímých jetů jako univerzální bránu.
Jde o negativní kontrolu konkrétní identifikace
E_mu=i D_mu Theta. V alternativní konstrukci celá
komplexní projektovaná derivace Theta určuje *reálnou*
B-Gramovu metriku; na regulární Lorentzově oblasti
lze její ortonormální tetrádu a maticovou tetrádu
v i-Herm **vypočítat** bez nezávislého tetrádového pole.
Fázově kompenzovaný zakřivený příklad má R_txtx(0)=kappa²
a nehermitovské komplexní jety. Tetráda není volné pole;
její lokální Lorentzova kalibrační nejednoznačnost je očekávaná.

## Nové podmínky přípustnosti [OPEN]

*Metrika* má být operačně reálnou, fázově kovariantní
pozorovatelnou; nevyžadovat, aby každý komplexní mezikrok
byl Hermitovský. Gramův srovnávací model však stále
není totožný s kanonickou geometrií UBT z centrálního
antikomutátoru. Dále tuto identifikaci dokázat či vyvrátit
a odvodit nekruhovou dynamickou akci/hlavní symbol,
nikoli přebírat Einsteina.
Informační princip a sdílená realita musí působit na
kalibračně invariantní **reálné pozorovatelné** komplexního Theta.

## Výsledek mostu ke kanonickému sharp [PROVED, omezeně; OPEN dynamicky]

Prostudovat G1_CANONICAL_SHARP_BRIDGE.en.md a
tests/test_theta_canonical_sharp_bridge.py. Kanonická metrika
je centrálním *komplexně bilineárním* antikomutátorem sharp
ze **stejných** kovariantních jetů Theta, nikoli reálnou
Hermitovskou/dagger Gramovou formou. Centralita platí
algebraicky pro libovolné jety Mat(2,C), ale realitu
a Lorentzovu signaturu je nutné kontrolovat samostatně.
V zakřiveném fázově kompenzovaném příkladu pro kappa=1
má regulární bod C_tt=1, C_xx=-2i, zatímco dagger-Gram
B_tt=1, B_xx=-2. Společná skalární fáze neudělá
kanonický tenzor reálným. Faktorizace reálné tetrády
z dagger-Gramovy metriky je nekanonickým srovnáním,
**nikoliv** hotovým kanonickým zdvihem.

Při nulové konexi je regulární gradientová větev omezená:
pro Theta=X+iY s rank(dX)=4 vynucuje
Im C(dTheta,dTheta)=0 plochou Minkowského Killingovu
rovnici pro Y v souřadnicích X, takže nedegenerovaná
kanonická metrika je plochá. Komplexní jety však MOHOU
dávat reálnou centrální kanonickou metriku, jak ukazuje
afinní rámec po komplexní Lorentzově transformaci;
nezaměňovat s požadavkem i-Hermitovské reality jetů.

## Další jediná konstruktivní brána G1 [OPEN]

Začít od **deklarované** dvoustranné kanonické derivace
DTheta=dTheta+A Theta-Theta B a formulovat jeden
netautologický, z Theta odvozený a transformačně
kovariantní uzávěr A/B. Kandidát musí vytvořit
**reálnou nedegenerovanou zakřivenou kanonickou metriku
sharp ze svých skutečných kovariantních jetů**.
Při použití odvozené tetrády dokázat, že nejde jen
o faktorizaci metriky dosazenou za DTheta.
Přesně testovat fázový náboj, realitu/centralitu,
nosič, křivost, nezávislé variace, hlavní symbol
a fyzikální energii. Dodatečná volba
A=(target-E)/Theta je pouze algebraický pravý
inverz a NEVYBÍRÁ dynamiku. Zachovat C_working,
G1 PARTIAL, původní canonical a drafty #807/#808.
