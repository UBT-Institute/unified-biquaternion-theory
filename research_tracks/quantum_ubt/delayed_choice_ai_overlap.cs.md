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

# Interference s odloženou volbou řízenou AI: podmíněný model překryvu a mezery UBT

**Datum:** 2026-10-16 · **Autoři:** Pracovní výzkumný návrh UBT Institute (s pomocí AI; kontrola autora čeká).

<!-- UNIT: DC-01 -->
## 1. Rozsah a status tvrzení

**Status: RESEARCH TRACK / DERIVED_WITH_ASSUMPTIONS (matematika), OPEN_GAP (dynamika přechodu UBT–foton a měření).** Tento dokument **neodvozuje** Bornovo pravidlo, objektivní kolaps, větvení vesmírů ani vazbu vědomí pozorovatele z UBT. **Netvrdí**, že jde o novou kvantitativní předpověď UBT. Deterministický ověřovací skript testuje pouze standardní algebru Hilbertova prostoru.

Kanonickým nositelem zůstává jediné pole \(\Theta(q,\tau)\in\mathbb C\otimes\mathbb H\), kde \(\tau=t+i\psi\). V uvedeném ansatzu kompaktních módů chápeme \(\psi\) jako pomocnou/interní souřadnici; neměníme uzamčenou metriku z kovariantního tetrádu a její definici nezískáváme průměrováním přes vlákno. Jediná úplná fundamentální akce a její kvantová redukce dosud nejsou dokončeny.

<!-- UNIT: DC-02 -->
## 2. Výslovné předpoklady a dvoudráhový módový rozvoj

Předpokládejme (H1) vyvážený dvoudráhový interferometr; (H2) zvolený pozitivní, normalizovaný Hilbertův–Schmidtův součin interních módových amplitud v \(2\times2\) komplexní maticové reprezentaci biquaternionů; (H3) běžné Bornovy pravděpodobnosti a unitární děliče svazku jako externí srovnávací pravidla; (H4) periodickou interní souřadnici \(\psi\) s poloměrem \(R_\psi>0\); a (H5) korespondenci laboratorního fotonu s \(\Theta\) **výhradně jako nedokázaný pracovní ansatz**. Při pevném vnějším \(q\) zapíšeme složky obou drah:

$$
\Theta_j(t,\psi)=\sum_{n\in\mathbb Z}a_{j,n}(t)\,
\frac{e^{in\psi/R_\psi}}{\sqrt{2\pi R_\psi}},\qquad j\in\{A,B\}.
$$

$$
\langle a,b\rangle=\frac12\sum_n\operatorname{Tr}(a_n^\dagger b_n),
\qquad\langle a,a\rangle=\langle b,b\rangle=1,\qquad
\gamma_\psi=\langle a,b\rangle.
$$

<!-- UNIT: DC-03 -->
## 3. Podmíněné pravděpodobnosti detektorů

Za předpokladů H1–H5 má uzavřený interferometr níže uvedený standardní interferenční zákon; viditelnost při skenování fáze je \(V\). Otevřený interferometr dává stejné marginální pravděpodobnosti na obou detektorech **za podmínky** vyvážených ramen a účinností detekce. Jde o identity v přijatém srovnávacím kvantovém popisu, **nikoli** o důsledky dosud nedokončené akce UBT.

Náčrt důkazu: amplituda na výstupu 0 je v každém normovaném módu \((a_n+e^{i\phi}b_n)/2\). Po umocnění normy dávají dva diagonální členy součet \(1/2\) a smíšené členy příspěvek \(\operatorname{Re}(e^{i\phi}\gamma_\psi)/2\). Z Cauchyho–Schwarzovy nerovnosti plyne \(V\le1\).

$$
P(D_0\mid\mathrm{closed},\phi)=
\frac12\left[1+\operatorname{Re}(e^{i\phi}\gamma_\psi)\right],
\quad
P(D_1\mid\mathrm{closed},\phi)=1-P(D_0\mid\mathrm{closed},\phi),
\quad V=|\gamma_\psi|\le1.
$$

$$
P(D_0\mid\mathrm{open})=P(D_1\mid\mathrm{open})=\frac12.
$$

<!-- UNIT: DC-04 -->
## 4. AI, paměť detektoru a interpretace

Řadič AI, který volí otevřenou/uzavřenou konfiguraci až po vstupu fotonu do interferometru, nemění uvedené pravděpodobnosti **podmíněné skutečně zvolenou konfigurací** pouze tím, že jde o AI. Rozhodnutí mohou záviset na předchozích výsledcích; analýza musí podmiňovat podle skutečných nastavení a vyloučit rušivé vlivy historie či času.

Jestliže fyzikální stavy aparatury korelované s drahami jsou \(|E_A\rangle,|E_B\rangle\), pak při faktorizaci interního stavu a aparatury vzniká následující překryv. Jsou-li tyto stavy ortogonální, může viditelnost zmizet ještě před tím, než člověk přečte záznam. Jde o standardní matematiku provázání/dekoherence; nedokazuje objektivní kolaps ani Everettovo větvení a nepotřebuje předpoklad vědomí. Nefaktorizující dynamika vyžaduje překryv úplných sdružených stavů místo tohoto součinu.

$$
\gamma_{\mathrm{eff}}=\gamma_\psi\langle E_A\mid E_B\rangle
\qquad\text{(only if the internal and apparatus states factorize).}
$$

<!-- UNIT: DC-05 -->
## 5. Ilustrativní kandidát interní fáze (není specifický pro UBT)

Zaveďme **nový neprokázaný ansatz**, podle kterého pouze dráha B získá posun \(\delta\) závislý na winding módu, aniž se změní velikosti módů. Relativní překryv plyne z ortogonality módů. Pro stejné váhy módů \(n=0,1\) získáme níže uvedenou fázovou závislost viditelnosti. Posun \(\delta\) zde **není** odvozenou optickou vazbou, \(R_\psi\) **není** určen a stejného chování lze dosáhnout v běžné vícemódové kvantové optice. Samotný výsledek neodliší UBT od obvyklé kvantové mechaniky.

$$
b_n=a_n e^{in\delta/R_\psi},\qquad
p_n=\tfrac12\operatorname{Tr}(a_n^\dagger a_n),\quad
\sum_n p_n=1,\qquad
\gamma_\psi(\delta)=\sum_n p_n e^{in\delta/R_\psi}.
$$

$$
p_0=p_1=\tfrac12,\quad p_{n\notin\{0,1\}}=0
\quad\Longrightarrow\quad
V(\delta)=\left|\cos\frac{\delta}{2R_\psi}\right|.
$$

<!-- UNIT: DC-06 -->
## 6. Podmíněná překážka globální holomorfnosti

Pro každou komplexní komponentu \(f(\tau)\) deklarovaného redukovaného sektoru \(\Theta\) předpokládejme celou holomorfní funkci v \(\tau=t+i\psi\), periodicitu v imaginární souřadnici \(\psi\) s periodou \(2\pi R_\psi\) a jednotnou omezenost pro všechna reálná \(t\) a \(\psi\). Z Liouvilleovy věty plyne, že \(f\) musí být konstantní. Ekvivalentně nenulové Fourierovy módy níže uvedeného analytického tvaru rostou alespoň v jednom časovém směru. Jde o **podmíněné no-go při současném uplatnění všech předpokladů**, nikoli o obecný zákaz pole \(\Theta\) nebo winding módů. Současný status UBT omezuje striktní holomorfnost na výslovně určené redukované sektory; netvrdíme globální, na vztažné soustavě nezávislou holomorfnost.

$$
\partial_{\bar\tau}f=0,\quad f(t+i[\psi+2\pi R_\psi])=f(t+i\psi),
\quad \sup_{t,\psi}|f(t+i\psi)|<\infty
\quad\Longrightarrow\quad f=\mathrm{constant}.
$$

$$
f_n(t,\psi)=c_n e^{n(t+i\psi)/R_\psi}.
$$

<!-- UNIT: DC-07 -->
## 7. Navržený rozlišovací experiment

Porovnejme (i) adaptivní řadič AI, (ii) deterministické přehrání **stejných zaznamenaných nastavení a časování** na témže hardwaru a (iii) randomizovanou kontrolu, při kontrole zdroje, optiky, ztrát, fáze, interakce s prostředím a prahů detekce. Volba musí být fyzicky provedena až po vstupu fotonu; zaznamenáme přesné časy a neplatné pokusy vyloučíme podle předem registrovaných pravidel. Bloky fázového skenu randomizujeme a zaslepíme, ponecháme nedotčený holdout a odhadneme podmíněné \(P(D_0\mid c,\phi)\) a viditelnost s intervaly spolehlivosti. Efekt specifický pro AI by vyžadoval reprodukovatelný rozdíl **po** vyrovnání fyzikálních historií a kontrole mnohonásobného testování, nikoli nezaslepené srovnání souhrnných počtů. Návrh, v němž se člověk podívá až později, sám nerozliší kvantové interpretace.

<!-- UNIT: DC-08 -->
## 8. Otevřené mezery a podmínka povýšení výsledku

**OPEN_GAP:** dokončit jedinou akci \(\Theta\) a fyzikální kvantovou redukci; odvodit pozitivní fyzikální Hilbertův prostor a Bornovy pravděpodobnosti; ztotožnit dráhové stavy \(a_n,b_n\) s měřitelnými fotonovými stavy; odvodit posun fáze \(\delta\) závislý na dráze a poloměr \(R_\psi\) **bez fitování na cílové pozorování**; vypočítat standardní pozadí, nejistoty a skutečně falsifikovatelnou odchylku. Vazba na vědomí pozorovatele, objektivní kolaps ani Everettovo větvení nejsou v kanonické UBT prokázány. Dokud nejsou mezery uzavřeny, jde o srovnávací model a výzkumnou hypotézu, **nikoli** o grantově připravenou předpověď specifickou pro UBT.

**Nejmenší další krok:** odvodit nebo vyloučit fyzikálně pozorovatelný operátor pro interakci fotonu a aparatury závislou na \(\psi\) ze *stejné* akce, s bezparametrickým srovnáním s běžnou kvantovou optikou. Pokud žádná taková vazba nevyplývá, zaznamenat negativní výsledek.

<!-- UNIT: DC-09 -->
## 9. Ověření a původ

**Analyticky:** přímý rozvoj norem obou výstupů vyváženého děliče; ortogonalita módů; Cauchyho–Schwarzova nerovnost; podmíněný argument Liouvilleovou větou. **Numericky:** \`check_delayed_choice_overlap.py\`, standardní knihovna Pythonu, deterministický seed 20261016, 500 náhodných normovaných dvojic komplexních módů a 401 bodů dvoumódové fáze; lokálně spuštěno s výsledkem PASS dne 2026-10-16. Numerický test ověřuje **pouze** standardní algebru Hilbertova prostoru, nikoli fyzikální předpověď odvozenou z UBT. **LEAN-PENDING:** přesné lemma pro překryv v Hilbertově prostoru a podmíněné no-go pro holomorfnost zde nebyly formalizovány ani zkompilovány v Leanu. **Lidská kontrola:** čeká, včetně výslovného schválení významové shody české a anglické verze; exhaustive human review is not claimed. Zdroj překladu: anglická verze.

<!-- UNIT: DC-10 -->
## 10. Výchozí odkazy

- [Kanonická akce / audit jediné akce](../../canonical/ACTION.en.md)
- [Kanonické definice \(\Theta\) a tetrádu](../../canonical/THEORY/math/fields/theta_field.tex)
- [Kanonická volba komplexního času](../../canonical/THEORY/complex_time_canonical_choice.tex)
- [Status kvantového sektoru / otevřená mezera Bornova pravidla](../../docs/quantum_sector_status.md)
- [Stažený důkaz Bornova pravidla — historický audit](../../canonical/qm_emergence/step7_born_rule.tex)
- [Aktuální status UBT včetně rozsahu holomorfnosti](../../STATUS_OF_UBT.md)
- [Pravidla původu](../../AI_PROVENANCE.md)
