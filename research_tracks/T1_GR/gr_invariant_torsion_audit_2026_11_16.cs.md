<!-- BILINGUAL-UNIT: gr-invariants-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exploratory analysis; not a canonical GR replacement or a formally verified theorem.
UBT-AI-PROVENANCE-END
-->
# Audit invariantů GR a torze — 2026-11-16

<!-- UNIT: scope -->
## Rozsah a status
[VÝZKUM / PODMÍNĚNÉ] Tento dokument testuje Cartanův komparátor s nejnižším derivačním řádem, nikoli odvození fundamentální akce UBT. Kanonická větev v10.x zachovává jediné pole Theta, kovariantní tetrádu E_mu=N0^(-1/2)D_mu Theta a centrální metriku z ostrého antikomutátoru. Navrhovaný biquaternionový tenzor 4x4 a metrika ReTr **nenahrazují** kanonickou GR. Ověření v Leanu čeká.

<!-- UNIT: definitions -->
## Geometrické definice
Nechť e^a je nedegenerovaná reálná kotetráda a omega^{ab}=-omega^{ba} metrická Lorentzova konexe. Definujme
```text
T^a = de^a + omega^a{}_b wedge e^b
R^{ab} = d omega^{ab} + omega^a{}_c wedge omega^{cb}
Sigma^{ab} = e^a wedge e^b
```
Jde o proměnné komparátoru; úplnou variaci kompozitního Theta nepředpokládáme.

<!-- UNIT: identity -->
## Přesná diferenciální identita (Nieh–Yan)
Z první Bianchiho identity D T^a = R^a{}_b wedge e^b plyne
```text
d(e^a wedge T_a) = T^a wedge T_a - e^a wedge e^b wedge R_ab.
```
Holstova hustota je tedy modulo okrajový člen ekvivalentní T^a wedge T_a. Holstův člen a tuto kvadratickou torzní hustotu nelze při platnosti okrajového vztahu počítat jako nezávisle nastavitelné objemové operátory. Okrajové podmínky a topologie mohou nadále hrát roli. Jde o standardní diferenciálně geometrickou identitu, nikoli nový výsledek UBT.

<!-- UNIT: basis -->
## Omezená báze invariantů
Při nejvýše jedné křivosti nebo dvou torzích, s metrickou kompatibilitou a sudou paritou, patří mezi přípustné schematické hustoty
```text
L_EC = epsilon_abcd e^a wedge e^b wedge R^cd
L_Lambda = epsilon_abcd e^a wedge e^b wedge e^c wedge e^d
L_T1 = T_abc T^abc vol
L_T2 = T_abc T^bac vol
L_T3 = T_a T^a vol,  T_a = T^b{}_{ab}
```
Před výpočtem je nutné sjednotit numerické normalizace, znaménkové konvence a možné lineární vztahy zvolené ireducibilní báze torze. Lichý Holstův člen lze reprezentovat pomocí výše uvedené identity Nieh–Yan. Jde o vymezenou bázi se sudou paritou, **nikoli** úplnou klasifikaci všech invariantů UBT. Členy kvadratické v křivosti, nemetricita, další invarianty Theta, hranice a topologické členy vyžadují samostatný rozbor.

<!-- UNIT: dynamics -->
## Důsledky variace a stability
Pro minimální Hilbertovu–Palatiniho akci s invertibilní e a bez spinového zdroje hmoty dává nezávislá variace podle omega algebraickou rovnici torze T^a=0; variace podle e pak vede k vakuovým Einsteinovým rovnicím. Přidání algebraických členů kvadratických v torzi zachovává algebraické rovnice torze, ale jejich koeficientní matice může být při zvláštních vazbách singulární. V této omezené prvořádové akci po integraci per partes nevzniká nezávislý Hessian rychlostí torze; samo to nedokazuje úplnou Hamiltonovu absenci ghostů. Linearizovaná metrická GR má na regulární Minkowského větvi dvě nehmotné spin-2 polarizace. Variace kompozitního E(Theta,omega) může přidat další vazby a **není** pokryta výsledkem komparátoru.

<!-- UNIT: decisions -->
## Otevřené podmínky a další testy
1. Před jakýmkoli povýšením ověřit přesné závislosti kanonické derivace a konexe.
2. Spočítat algebraickou torzní matici 24x24 pro zvolenou ireducibilní bázi; určit singulární množiny a explicitní spinové zdroje.
3. Provést úplnou spřaženou analýzu vazeb/Hessianu v kanonické větvi Theta; ověřit, že ploché pozadí je řešením rovnic (repozitář už eviduje překážku ploché větve se spinovým zdrojem torze).
4. Nepovyšovat informační výběr, nový tenzor 4x4 ani theta/QM módy na kanonické skutečnosti GR.
5. Čeká: formalizace v Leanu, nezávislá algebraická kontrola, dvojjazyčné významové ověření, CI.

<!-- UNIT: result -->
## Závěr
[PODMÍNĚNÉ] Cartanův komparátor poskytuje známou dynamiku GR, nikoli fundamentální akci UBT odvozenou z prvních principů. Identita Nieh–Yan odstraňuje jednu naivní redundanci seznamu invariantů. Hlavním otevřeným úkolem je slučitelnost s **kanonickou** variací Theta přes kovariantní tetrádu a jejím spinovým/torzním zdrojem.


<!-- UNIT: exact-matrix -->
## Přesná minimální Cartanova matice: dokončený test
Pro orientovanou kotetrádu e^a=dx^a rozepišme T^a=sum_{m<n}t^a_{mn} dx^m wedge dx^n. Indexy 24 sloupců jsou (a,m<n) a indexy 24 řádků jsou (c<d,i<j<k). Matice koeficientů zobrazení C(T)_{cd}=epsilon_{abcd}T^a wedge dx^b má
```text
shape = (24,24)
rank = 24
determinant = 16
inverse * matrix = identity
```
při uvedeném pořadí a orientaci. Determinant závisí na bázi; invertibilita nikoli. Přesný kontrolní program v SymPy je tools/verify_gr_cartan_map_2026_11_16.py. Reprodukuje již kanonicky zaznamenanou podmíněnou větu GAP-10T-PALATINI, nikoli nový důkaz dynamiky UBT.

<!-- UNIT: obstruction -->
## Důsledek pro kanonickou překážku odvození GR
Při nulovém Cartanově zdroji vynucuje invertibilita nulovou fyzikální torzi T=0. Avšak kanonický no-go GAP-10T-MINIMAL-ONE-CONNECTION-GR říká, že ztotožnění této bez-torzní fyzikální konexe s jedinou jet-konexí v čistě párové reprezentaci jediného Theta vylučuje obecnou zakřivenou GR. Nenulový zdroj indukovaný Theta může naopak vynucovat torzi i v nominálně plochém vakuu (GAP-10T-FLAT-NOGO). Samotná eliminace pomocné torze tedy **neřeší** odvození kanonické GR: musíme rozlišit jet-konexi a fyzikální konexi nebo prokázat životaschopné torzní rozšíření při úplné kompozitní variaci Theta. Rozdělenou jet-konstrukci nelze bez sladění s axiomem A nazývat nezávislým fundamentálním polem.

<!-- UNIT: verification -->
## Záznam ověření
Přesná hodnost, determinant a inverze byly ověřeny lokálním výpočtem v SymPy s exaktní aritmetikou. Commitnutý reprodukovatelný skript implementuje stejnou bázi. Kompletní CI repozitáře, dvojjazyčný významový ověřovač, kompilace Lean a spřažený kanonický Hessian zůstávají **NESPUŠTĚNÉ / ČEKAJÍ**. Merge je blokován, dokud neprojdou povinné kontroly repozitáře.
