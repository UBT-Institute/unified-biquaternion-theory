<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: minimal-C2-action-closure.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact minimal timelike action-family closure; not a no-go for nonminimal or general complex UBT actions.
UBT-AI-PROVENANCE-END -->
# Minimální akce jediného Theta: úplné dilema bez dynamiky pro každý C2 potenciál

**Stav: EXACT CONDITIONAL NO-GO / WHOLE UBT STILL UNDERDETERMINED.** Zobecňujeme Propozici 9 z `canonical_family_hamiltonian_bridge.en.md`: negativní výsledek již nepotřebuje kvartický, polynomiální, analytický, koercivní ani neustálený potenciál. Používá přesně deklarovanou minimální kineticko-potenciálovou akci, časupodobnou kladně hermitovskou Lorentzovu orbitu, kompozitní metriku a nezávislé pomocné spinové spojení. **Nepřidáváme žádný nový fundamentální člen.**

## Převzaté předpoklady, nikoli nové axiomy

Na souvislé orientované hladké čtyřrozměrné oblasti zvolíme lokální radiální Lorentzovu kalibraci časupodobné větve jediného Theta. Nezávislé bezestopé Lorentzovo spinové spojení má volné boostové komponenty. Generovaná tetráda je

\[
e_\mu{}^a=\frac1q(\partial_\mu\rho,\rho b_\mu{}^1,\rho b_\mu{}^2,\rho b_\mu{}^3),
\quad q=\sqrt{\mathcal N_0}>0,\quad \rho>0,\quad
g_{\mu\nu}=e_\mu{}^a\eta_{ab}e_\nu{}^b.
\]

Ponecháme původní reálné Lorentzovsky invariantní kvadratické kinetické párování, kompozitní metriku z vlastní kovariantní první derivace, nenulovou reálnou normalizaci c a libovolný reálný potenciál třídy C2. Zásadně **nemáme samostatnou křivost, derivace spojení ani další členy akce**. Přesná identita Lorentzova párování z původní Propozice 9 dává

\[
\mathcal B(D_\mu\Theta,D_\nu\Theta)=-2\mathcal N_0g_{\mu\nu},
\quad
S_{\min}=\int_M d^4x\,
|\det e|\,[4c\mathcal N_0-U(\rho)].
\]

## Úplná dichotomická věta

Dvanáct nezávislých boostových variací neobsahuje derivace spojení a při pevné orientaci dává

\[
\frac{\delta S_{\min}}{\delta b_\mu{}^i}=
[4c\mathcal N_0-U(\rho)]\,\frac{\rho}{q}
|\det e|(e^{-1})_i{}^\mu=0.
\]

Pro regulární matici nemohou všechny kofaktory jejího prostorového sloupce současně vymizet. Každá stacionární regulární konfigurace proto vyžaduje

\[
\boxed{\det e\ne0\quad\Longrightarrow\quad
U(\rho(x))=4c\mathcal N_0\quad\text{for all }x.}
\]

Regulární tetráda nemůže mít nulový sloupec radiálního gradientu:

\[
\det e=\frac{\rho^3}{q^4}
\det[\partial\rho,b^1,b^2,b^3]\ne0
\quad\Longrightarrow\quad d\rho\ne0.
\]

Podle věty o submerzi obsahuje obraz rho v okolí každého bodu otevřený interval. Boostová Eulerova rovnice tak vyžaduje **konstantní plošinu potenciálu** právě na úrovni kinetického objemového koeficientu:

\[
\boxed{
d\rho\ne0\quad\Longrightarrow\quad \rho(\mathcal U)
\text{ contains an open interval }I\subset(0,\infty),\qquad
U|_I\equiv4c\mathcal N_0.
}
\]

Pro každý radiální potenciál C2 v této větvi tedy nastává přesná alternativa: **(A)** nemá-li příslušná hladinová množina vnitřní interval, neexistuje regulární stacionární řešení; **(B)** existuje-li takový interval, každá stacionární regulární konfigurace má lokálně hodnoty rho v tomto intervalu a celá minimální akce je identicky nulová v okolí takové konfigurace v časupodobném redukovaném prostoru polí:

\[
S_{\min}\big|_{\rho\in I}=0,\qquad
\boxed{
\delta S_{\min}\big|_{\mathcal U}=0,\quad
\delta^2S_{\min}\big|_{\mathcal U}=0
}
\quad\text{for compactly supported variations staying inside }I.
\]

Lokální Eulerův i Hessův operátor pak mizí na všech kompaktně podepřených variacích zachovávajících danou plošinu. Větev nemá z této minimální akce **žádné netriviální místní gravitační rovnice ani kvadratický kinetický operátor**. Netvrdíme totéž o příčných komplexních směrech mimo Lorentzovsky reálnou časupodobnou varietu.

## Proč nepomůže libovolná hladká funkce

Konkrétní globálně neustálený C2 potenciál s konstantní plošinou je

\[
U(\rho)=4c\mathcal N_0+
\begin{cases}
(1-\rho)^4,&\rho<1,\\
0,&1\le\rho\le2,\\
(\rho-2)^4,&\rho>2,
\end{cases}
\quad U\in C^2,\quad U\not\equiv\mathrm{const}.
\]

Na této plošině máme lokální hladké regulární konfigurace, například

\[
\rho=qt,\quad 1<qt<2,\qquad
b_i{}^j=\frac{q}{\rho}\delta_i{}^j,\quad b_0{}^j=0
\quad\Longrightarrow\quad e_\mu{}^a=\delta_\mu{}^a.
\]

Nejde však o odvozenou gravitační dynamiku, ale pouze o **neurčené stacionární geometrie identicky nulové redukované akce**. Neutrální neustálené polynomy ani reálně analytické potenciály nemají otevřenou plošinu a spadají do varianty (A). Konstantní U rovné požadované hodnotě dává triviální celou akci; jiná konstanta vyloučí regulární stacionární tetrádu.

## Celá časupodobná kladně hermitovská Lorentzova orbita

Pro obecnou pozitivně hermitovskou X existuje lokální hladké radiální zobrazení v SL(2,C):

\[
X>0,\quad r=\sqrt{\det X},\quad
S=\sqrt r\,X^{-1/2}\in SL(2,\mathbb C),\quad
SXS^\dagger=rI.
\]

Jelikož původní minimální akce a U jsou Lorentzovsky invariantní a spinové spojení se transformuje odpovídajícím způsobem, platí stejné dilema v celé lokální kladně hermitovské časupodobné orbitě. **Nevztahuje se** na obecné nehermitovské komplexní Theta, samostatnou spinovou křivost, jinou mikroskopickou míru nebo odvozenou akci vyššího řádu.

## Nezávislá překážka: deklarované symetrie nevybírají jedinou akci

Již před řešením pohybových rovnic připouštějí původní Lorentzova kongruenční a fázová U(1) symetrie nezávislé skalární invarianty bez derivací. Vezměme existující kvadratický invariant H a determinant. Na dvou explicitních hodnotách pole máme
\[
X_1=I_2,\quad X_2=I_2+i\sigma_1,\qquad
(H(X_1)^2,|\det X_1|^2)=(4,1),\quad
(H(X_2)^2,|\det X_2|^2)=(0,4).
\]
\[
\boxed{\det\begin{pmatrix}4&1\\0&4\end{pmatrix}=16\ne0.}
\]
Jejich vyhodnocovací matice má nenulový determinant; tedy H² a |det X|² jsou lineárně nezávislé funkce celého osmireálného prostoru polí. Každá zvlášť respektuje **stejné deklarované symetrie**. Pouhý argument těmito symetriemi proto nemůže určit jejich relativní koeficienty, vybrat dynamické vakuum ani odvodit chybějící koeficient křivosti. Problém výběru akce je **skutečná matematická neurčenost**, nikoli administrativní nedodělek. Dynamický výběrový princip by musel být nezávisle odvozen, jinak je nutné přiznat, že teorie není určena; přidávat členy jen kvůli shodě s GR je dodatečný modelový vstup.

## Silnější uzavření: každý přirozený algebraický Lagrangián prvního jetu

**Věta o redukci orbity (bez nového axiomu):** Uvažujme libovolnou lokální diferencovatelnou hustotu akce, ne nutně polynom, která je skalární hustotou při prostoročasových difeomorfismech, invariantní při lokální vlastní ortochronní Lorentzově transformaci a je sestavena **pouze algebraicky** z existujícího časupodobného Lorentzova vektoru X, jeho regulární tetrády e=D X/q, invariantních Lorentzových tenzorů eta a epsilon a jejich inverzí či kontrakcí. Nepřipouštíme další tenzory pozadí, explicitní spinovou křivost, nezávislou kinetiku spojení, derivace e ani jiná pole než X a jeho pomocné Lorentzovo spojení. Fixujeme oblast s orientací a časovou orientací.

Za těchto *přesných* podmínek má každá taková hustota tvar

\[
\boxed{\mathcal L_{\mathrm{alg}}(X,e)=|\det e|\,F(r),\qquad
r=\sqrt{-\eta_{ab}X^aX^b},\qquad
e^a=q^{-1}D_\omega X^a.}
\]

**Důkaz:** V jednom bodě dovoluje regulární e lineární změnu prostoročasových souřadnic, která tetrádovou matici převede na jednotkovou. Po této operaci nemůže zbýt nezávislý invariant s prostoročasovým indexem, protože všechny souřadnicové indexy jsou zkontrahované a žádný další prostoročasový tenzor jsme nepřipustili. Zbývající vnitřní vlastní Lorentzova symetrie působí tranzitivně na každém budoucím časupodobném hyperboloidu s jediným invariantem r. Normalizovaná skalární hustota je proto hladkou funkcí F(r); kontrakce s epsilon mohou změnit pouze konstantní orientační faktor. Důkaz zahrnuje nelineární a nepolynomiální kontrakce libovolného stupně, ovšem jen za přesně vymezeného algebraického obsahu polí prvního jetu.

Metrická kompatibilita spinového spojení dává **kalibračně nezávislou** identitu radiálního gradientu:

\[
d(X^aX_a)=2X_aD_\omega X^a=2qX_ae^a,\qquad
\boxed{dr=-\frac{q}{r}X_ae^a,\quad g^{-1}(dr,dr)=-q^2.}
\]

Regulární časupodobná tetráda proto vynucuje nenulový dr bez nového předpokladu homogenních hodin. V lokální radiální Lorentzově kalibraci každý pomocný boost mění jeden prostorový sloupec nezávisle a stacionarita dává

\[
\frac{\delta S_{\mathrm{alg}}}{\delta b_\mu{}^i}=
\frac r q|\det e|\,(e^{-1})_i{}^\mu F(r)=0,
\qquad
\boxed{\det e\ne0\Longrightarrow F(r)=0.}
\]

Protože dr je všude nenulový, jeho lokální obraz obsahuje otevřený interval I, kde redukovaný skalární koeficient identicky mizí:

\[
\boxed{r(\mathcal U)\supset I,\quad F|_I\equiv0,\quad
S_{\mathrm{alg}}|_{\mathcal U}=0,\quad
\delta S_{\mathrm{alg}}|_{\mathcal U}=0,\quad
\delta^2 S_{\mathrm{alg}}|_{\mathcal U}=0.}
\]

Všechny přípustné malé kompaktně podepřené variace zůstávající uvnitř tohoto intervalu mají identicky nulovou redukovanou akci i její redukované variační derivace. Výsledek tak vylučuje **prediktivní časupodobnou gravitační dynamiku celé přirozené algebraické třídy prvního jetu**, nikoli pouze konkrétní kvadratické párování nebo přejmenovaný skalární, pseudoskalární či bivektorový potenciál.

**Přesná hranice:** Lokální redukce grupové orbity je geometrický důkaz, nikoli konečná počítačová enumerace; doplňkový symbolický ověřovač zkouší normalizaci rámce, objem epsilon, Lorentzovu kovarianci, identity projektoru a kofaktory boostů na netriviálních příkladech. Věta NEPLATÍ pro kovariantní derivace e, spinovou křivost, torzní členy obsahující de, derivované vazby, nezávislé struktury pozadí, nehermitovské Theta, globální holonomie ani příčné komplexní variace úplného pole. Zejména nedokazuje, že některý takový operátor musí vyplývat z principů UBT. **Bez zdůvodněného operátoru mimo tuto třídu dosavadní předpoklady nedávají dynamickou teorii gravitace.**

## Co je uzavřené a co není

**Negativně uzavřeno:** celá původní kineticko-potenciálová minimální akce s libovolným C2 potenciálem, nezávislým algebraickým Lorentzovým spojením a centrální kompozitní metrikou nemůže ve stanovené časupodobné větvi dodat regulární **prediktivní gravitační dynamiku**. Chytřejší skalární, pseudoskalární, vektorový, bivektorový nebo tenzorový *algebraický* potenciál nezruší objemový kolaps, pokud se jeho invariantní kontrakce redukuje na místní radiální U. Může změnit interakce komplexních příčných složek, ale neobnoví nenulový lokální gravitační Hessův operátor v této větvi.

**Otevřeno:** zda ze skutečně již přijatých principů UBT plyne *nezávisle zdůvodněný* křivostní invariant spojení, jiná orbita hodnot pole či nový variační princip. Aktuální kanonické zdroje JEDINOU akci s Einsteinovou, gravitonovou a Yangovou–Millsovou dynamikou jednoznačně neodvozují; přidání Palatiniho–Holstova členu ručně je srovnávací teorie, nikoli dokončení. Další ad hoc opravy nejsou tímto důkazem ospravedlněny.

**Ověření:** `tools/verify_minimal_all_C2_potentials.py` a cílený pytest; přesné determinanty/kofaktory, explicitní příklad, C2 plošina a nulový kvadratický operátor. **Předchozí výsledky:** `canonical/ACTION.en.md`, Propozice 9 `canonical_family_hamiltonian_bridge.en.md`, `timelike_orbit_unitclock.en.md` a mergnutý PR #694.
