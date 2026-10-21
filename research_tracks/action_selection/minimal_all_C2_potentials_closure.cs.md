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

## Co je uzavřené a co není

**Negativně uzavřeno:** celá původní kineticko-potenciálová minimální akce s libovolným C2 potenciálem, nezávislým algebraickým Lorentzovým spojením a centrální kompozitní metrikou nemůže ve stanovené časupodobné větvi dodat regulární **prediktivní gravitační dynamiku**. Chytřejší skalární, pseudoskalární, vektorový, bivektorový nebo tenzorový *algebraický* potenciál nezruší objemový kolaps, pokud se jeho invariantní kontrakce redukuje na místní radiální U. Může změnit interakce komplexních příčných složek, ale neobnoví nenulový lokální gravitační Hessův operátor v této větvi.

**Otevřeno:** zda ze skutečně již přijatých principů UBT plyne *nezávisle zdůvodněný* křivostní invariant spojení, jiná orbita hodnot pole či nový variační princip. Aktuální kanonické zdroje JEDINOU akci s Einsteinovou, gravitonovou a Yangovou–Millsovou dynamikou jednoznačně neodvozují; přidání Palatiniho–Holstova členu ručně je srovnávací teorie, nikoli dokončení. Další ad hoc opravy nejsou tímto důkazem ospravedlněny.

**Ověření:** `tools/verify_minimal_all_C2_potentials.py` a cílený pytest; přesné determinanty/kofaktory, explicitní příklad, C2 plošina a nulový kvadratický operátor. **Předchozí výsledky:** `canonical/ACTION.en.md`, Propozice 9 `canonical_family_hamiltonian_bridge.en.md`, `timelike_orbit_unitclock.en.md` a mergnutý PR #694.
