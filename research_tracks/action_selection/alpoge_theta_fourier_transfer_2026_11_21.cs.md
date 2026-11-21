<!-- BILINGUAL-UNIT: alpoge-theta-transfer.scope -->
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

# Alpögeho důkaz RH: testy přenosu konečné Fourierovy/theta struktury do jediného pole UBT

**Zaznamenáno 2026-11-21 · C_working · pouze výzkum · LEAN-PENDING.**
Tato poznámka testuje *konečnou Fourierovu analogii*, **nikoli** Alpögeho aritmetický theta lift, a nemění kanonickou tetrádu, metriku ani akci jediného pole. Žádná fyzikální mezera UBT se neuzavírá.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.sources -->
## Zdroje a oddělení mechanismů

Alpögeho [původní poznámka](https://alpo.ge/remark.pdf) navrhuje iterované theta lifty jako aritmetický mechanismus násobnosti v důkazu GRH Stepanovova typu. Nezávislý [průvodce strukturou důkazu](https://nasqret.github.io/riemann-rev/guide/proof-guide.pdf) uvádí CM tělesa, unitární grupy, theta jádra, Heckeho charaktery, kohomologické a sklonové odhady. [Sutherlandův audit](https://math.mit.edu/~drew/grh/) kontroluje tvrzení Leanu včetně RH a GRH pro Dirichletovy L-funkce, ale neposkytuje větu o přenosu do UBT.

Běžná diskrétní Fourierova transformace, Jacobiho theta sumace, gaussovské tepelné vyhlazování a automorfní theta *lift* jsou různé operace. Níže uvedený experiment pokrývá pouze první operaci a neunitární gaussovskou kontrolu. Jakékoli propojení se skutečným iterovaným liftem zůstává **OPEN**.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.setup -->
## Přesný zkušební prostor a invarianty

Použijeme *existující* věrnou maticovou reprezentaci jediného bikvaternionu:
[
Xinmathbb Bcongoperatorname{Mat}_2(mathbb C),qquad
B(X,Y)=operatorname{Re}operatorname{Tr}[operatorname{adj}(X)Y^dagger],
qquad JX=iX,qquad Omega(X,Y)=B(X,JY).
]
Zde (operatorname{adj}) znamená adjungovanou matici (2	imes2) ve smyslu adjugátu, nikoli hermitovsky sdruženou matici. Reálná kvadratická forma (B) má signaturu ((2+,6-)). Forma (Omega) je alternující a nedegenerovaná; ani jedno tvrzení nečiní z (B) kladnou fyzikální energii.

Vezmeme čtyři *koeficienty módů* (X_ninmathbb B), (n=0,1,2,3), bez zavedení nového fundamentálního pole. Definujeme
[
mathcal B(X,Y)=sum_{n=0}^3 B(X_n,Y_n),quad
mathcalOmega(X,Y)=sum_{n=0}^3 Omega(X_n,Y_n),
quad
(F_4X)_k=rac12sum_{n=0}^3e^{-2pi i kn/4}X_n.
]
Jde o konečněrozměrný test s pevnými koeficienty; nepředpokládáme, že libovolné míchání módů je kalibrační transformací nebo že zachovává striktní holomorfii v (	au=t+ipsi).

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.positive -->
## Algebraický výsledek: přesné zachování forem v prostoru módů

**ALGEBRA-EXACT, podmíněně v tomto zkušebním prostoru.** Jelikož (F_4^dagger F_4=I_4) a (F_4) působí komplexně lineárně na indexu módu, zachovává obě formy:
[
oxed{mathcal B(F_4X,F_4Y)=mathcal B(X,Y)},qquad
oxed{mathcalOmega(F_4X,F_4Y)=mathcalOmega(X,Y)},qquad
F_4^4=I.
]
Tentýž důkaz platí pro normalizované (N)-módové DFT s identickou vnitřní formou (B) na každém módu. Pro čtyři módy je celková reálná signatura ((8+,24-)), kterou transformace nemění. Přesná symplektická kovariance tedy **neřeší indefinitnost kinetické/Hamiltonovy formy**. Nejde o tvrzení o kladnosti na řešeních pohybových rovnic.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.negative -->
## Dvě rozhodující negativní kontroly

1. Kladný gaussovský filtr módů (G=operatorname{diag}(2^{-n^2})), působící na všechny čtyři bikvaternionové koeficienty, **není** symplektický:
[
oxed{mathcalOmega(GX,GY)
eqmathcalOmega(X,Y)}
]
obecně. Váhu tepelného jádra nelze bez dalšího považovat za unitární/Weilovu symetrii.

2. DFT **není** symetrií kanonické metriky UBT při pevném (psi), přestože zachovává (mathcalOmega). V jednoduchém plochém příkladu s triviální konexí a (mathcal N_0=1) vložíme celé prostoročasově závislé (Theta_{m SR}(x)) do módu (n=0):
[
Theta(x,psi)=Theta_{m SR}(x),quad
Theta'(x,0)=sum_{k=0}^3(F_4X)_k=2Theta_{m SR}(x),
quad E'_mu(x,0)=2E_mu(x,0),
]
[
oxed{g'_{mu
u}(x,0)=4g_{mu
u}(x,0)}
]
při použití *nezměněné* kanonické definice (E_mu=mathcal N_0^{-1/2}D_muTheta) a centrálního sharp antikomutátoru. Jde o protipříklad k tvrzení, že Fourierova kovariance konečných módů sama implikuje fyzikální kalibrační symetrii. Plochý příklad je kinematický, nikoli řešení zvolené akce UBT.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.gates -->
## Podmínky skutečného přenosu — všechny OPEN

Navrhovaný přenos Alpögeho **aritmetického** mechanismu theta liftů musí nejdříve poskytnout (i) určený prostor reprezentace a skutečné jádro liftu/proplétající operátor včetně oborů a konvergence; (ii) kovarianci existující dvoustranné derivace (D_muTheta=partial_muTheta+A_muTheta-Theta B_mu), včetně případného míchání módů v (A_mu,B_mu); (iii) zachování nebo odvozený transformační zákon *centrální sharp metriky*, nikoli pouze (mathcalOmega); (iv) vybraný Hamiltonián s vazbami a test kladnosti; a (v) konkrétní důsledek specifický pro UBT, který neprojde triviálním nulovým modelem Fourierovy transformace/tepelného jádra. Aritmetický argument s dělitelností a sklonovými odhady dosud není fyzikální propagátor ani dynamika gravitace.

Dřívější no-go pro symplektické zakřivení skalárního ekvivariantního ansatzu nadále platí v jeho vymezeném rozsahu: DFT na prostoru módů nevytvoří šest nezávislých bivektorových koeficientů zakřivení vyžadovaných Palatiniho formulací. Nezavádíme žádný nový stupeň volnosti, akci, fyzikální symetrii, predikci hmotnosti ani tvrzení o odstranění ghostů.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.weil -->
## Bližší matematická cesta: Lorentzova kovariance uvnitř symplektické grupy

Existující Lorentzova kongruenční transformace (X\mapsto SXS^\dagger), (S\in SL(2,\mathbb C)), zachovává (B) a komutuje s (J); poskytuje tedy reálnou symplektickou reprezentaci (SL(2,\mathbb C)\to Sp(8,\mathbb R)) na stejných osmi reálných složkách pole. To je bližší [standardní Weilově/oscilátorové reprezentaci](https://www.math.iitb.ac.in/~dprasad/weil-repn.pdf), která stojí za theta korespondencí, než samotná konečná DFT. **Stále** však nejde o ztotožnění s Alpögeho theta jádrem na unitárních grupách.

Existuje přesná překážka kladnosti *na konečném nosiči složek*. Pro
\[
S=\operatorname{diag}(2,1/2),\quad
X_*=\operatorname{diag}(1,0),\quad
S X_* S^\dagger=4X_*,
\]
by každá kladně definitní Lorentzovsky invariantní kvadratická forma (P) musela splňovat (P(X_*,X_*)=P(4X_*,4X_*)=16P(X_*,X_*)), což je spor. **Na původním konečněrozměrném nosiči hodnot pole tedy neexistuje kladně definitní skalární součin invariantní vůči této celé kongruenční akci**. To nevylučuje fyzikální kladný Hilbertův prostor stavů.

Pro reálný osmireálný symplektický prostor má standardní metaplektické dvojné pokrytí (Mp(8,\mathbb R)) unitární oscilátorovou reprezentaci na (L^2(\mathbb R^4)); viz [standardní matematická konstrukce](https://www.math.iitb.ac.in/~dprasad/weil-repn.pdf). *Matematická cesta přes teorii reprezentací* je tedy dostupná bez přidání druhého fundamentálního pole UBT: **kvantovat symplektický prostor hodnot a testovat indukovanou Lorentzovu akci**. Oscilátorový Hilbertův prostor však není totéž jako Lorentzovsky invariantní kladná norma na (X), ani nejde o odvozenou kvantizaci UBT, fyzikální spektrum, akci, polarizaci či theta lift. Tyto mosty zůstávají **OPEN**.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.verification -->
## Ověření a status

Nezávislé analytické kroky: unitarita DFT, komplexní linearita, signatura (B) a přímý výpočet sharp metriky v plochém příkladu. Deterministický test přesné aritmetiky v SymPy je `research_tracks/action_selection/tests/test_alpoge_theta_fourier_transfer.py`; příkaz:
```sh
python -m unittest research_tracks.action_selection.tests.test_alpoge_theta_fourier_transfer -v
```
Sedm testů prošlo lokálně se SymPy 1.14.0 dne 2026-11-21: signatura, DFT čtvrtého řádu, kovariance (B/Omega), nesymplektický gaussovský filtr, zachování záporného směru a protipříklad s metrikou. Testy ověřují pouze zakódované konečněrozměrné identity; žádný skutečný automorfní lift, PDE UBT, Einsteinovy rovnice, spektrum s vazbami ani Alpögeho věta nebyly nezávisle znovu dokázány. **LEAN-PENDING**: pro tuto novou poznámku nebyl zkompilován soubor Leanu. Netvrdíme povýšení kanonického/statusového tvrzení ani schválení sémantické shody překladů.
