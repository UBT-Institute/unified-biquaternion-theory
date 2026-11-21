<!-- BILINGUAL-UNIT: hypertravel.scope -->
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

# Hyperprostor, dvojité rotace a komplexní čas: přesné základní kontroly

**2026-11-22 · C_working · podmíněné zkušební modely · LEAN-PENDING.** Cíl: oddělit matematicky netriviální grupovou strukturu od nového fyzikálního mechanismu cestování prostoročasem. **Nepředpokládáme** další fyzikální rozměry, tachyonické pole UBT, vybranou akci UBT, exotickou hmotu ani skutečný stroj času. Uzamčené kanonické definice neměníme.

<!-- BILINGUAL-UNIT: hypertravel.canonical -->
## Fyzikální rozsah versus kanonická UBT

[Uzamčené axiómy](../../canonical/AXIOMS.md) definují **jediné** bikvaternionové pole a komplexní skalární parametr \(\tau=t+i\psi\). Samy však **neurčují** další fyzikální složku metriky \(g_{\psi\psi}\), pětirozměrný Lorentzův prostoročas ani kinetický operátor podél \(\psi\). [Současný stav UBT](../../STATUS_OF_UBT.md) výslovně upozorňuje, že striktní Lorentzovsky kovariantní holomorfie v \(\tau\) obecně nefunguje pro nezávislé Lorentzovsky skalární \(\psi\); \(\psi\) je mimo redukované holomorfní sektory odděleným parametrem vlákna. Dvě signatury dalších rozměrů zkoumané níže jsou **alternativními srovnávacími modely**, nikoli souběžnými důsledky kanonické UBT. Efektivní gravitační větev UBT zůstává podmíněna přijatými předpoklady infračervené akce.

<!-- BILINGUAL-UNIT: hypertravel.boosts -->
## Přesná kontrola dvou boostů: rotace, nikoli překlad v čase

Pro \(\eta=\operatorname{diag}(-1,1,1,1)\) zvolme infinitesimální boosty \(K_x,K_y\) s nenulovými prvky \((K_x)_{01}=(K_x)_{10}=1\), \((K_y)_{02}=(K_y)_{20}=1\). Jejich komutátorem je generátor prostorové rotace \(J_z\):
\[
\boxed{[K_x,K_y]=J_z,\qquad
K_i^T\eta+\eta K_i=0,\quad
J_z^T\eta+\eta J_z=0.}
\]
(Při jiné konvenci znaménka rotačního generátoru se změní znaménko prvního vztahu.) Přesné konečné boosty s rapiditou \(\log2\) mají \(\cosh(\log2)=5/4,\ \sinh(\log2)=3/4\). Jejich součiny nekomutují, ale splňují
\[
\boxed{\Lambda^T\eta\Lambda=\eta,\qquad
\det\Lambda=1,\qquad\Lambda(0)=0.}
\]
Každé konečné složení **lineárních** vlastních ortochronních Lorentzových transformací zachovává intervaly, budoucí světelný kužel i počátek; nekomutující dvojitá rotace či boost **sama o sobě** nevytváří afinní posun, nemění kauzální kužel a neposílá událost do vlastní minulosti. To nevypovídá nic o globálním cestování časem v *zakřivených* prostoročasech s další strukturou. Wignerova–Thomasova rotace je známou součástí [speciální relativity](https://arxiv.org/abs/physics/0211022), nikoli novým jevem UBT.

<!-- BILINGUAL-UNIT: hypertravel.spin -->
## Úplná spinorová rotace nepřemisťuje prostoročasové souřadnice

Pro dvousložkový spinor spinu \(1/2\) se rotace o \(2\pi\) projeví zápornou jednotkovou maticí, zatímco rotace o \(4\pi\) působí jednotkově:
\[
U_z(\theta)=e^{-i\theta\sigma_z/2},\qquad
\boxed{U_z(2\pi)=-I,\qquad U_z(4\pi)=I.}
\]
Rozdíl dvojného pokrytí spinorů se může projevit **relativní fází**, nikoli překladem v prostoročase nebo posunem do minulosti. Samotná změna znaménka nedokládá druhou fyzikální časovou osu.

<!-- BILINGUAL-UNIT: hypertravel.comparators -->
## Zkušební model skalární vlny v 5D: obě signatury

**Předpoklady (nikoli důsledky UBT):** ploché součinové pozadí s jednou kompaktní kružnicí \(S^1_\psi\) o poloměru \(R>0\), volné skalární pole o hmotnosti \(m\ge0\), Fourierovo číslo vinutí \(n\in\mathbb Z\), jednotky \(c=\hbar=1\) a 5D kvadratický kinetický člen s výslovně zvolenou signaturou dalšího rozměru \(\varepsilon=\pm1\). Pro módy platí vztahy
\[
\boxed{\omega_n^2=k^2+m^2+\varepsilon\frac{n^2}{R^2},
\qquad \varepsilon=+1\text{ (spacelike)},\quad
\varepsilon=-1\text{ (timelike)}.}
\]
Pro prostorovou variantu (\(\varepsilon=+1\)) má každý mód reálnou frekvenci a pro šířící se vlnové balíky s kladnou frekvencí dostáváme
\[
\boxed{v_g=\frac{\partial\omega_n}{\partial k}
=\frac{k}{\sqrt{k^2+m^2+n^2/R^2}},\qquad |v_g|\le1.}
\]
Každá nulová trajektorie v této ploché \(4+1\) geometrii po projekci do pozorovaných prostorových souřadnic navíc splňuje \(|d\mathbf x/dt|\le1\). Kompaktní další **prostorový** rozměr tedy vytváří standardní Kaluzaův–Kleinův hmotnostní žebřík, **nikoli** automatickou nadsvětelnou zkratku. Pokřivené nebo nesoučinové metriky vyžadují samostatné důkazy a tento test je nepokrývá.

Pro časovou variantu (\(\varepsilon=-1\)) dávají při pevných \(k,m,R\) libovolně velká \(|n|\) hodnotu \(\omega_n^2<0\), tedy exponenciálně rostoucí nebo klesající módy. Při \(k=0,m=R=1,n=2\) dostáváme \(\omega_n^2=-3\). Nestabilita je **konkrétním selháním plochého skalárního modelu**; není důkazem, že selhat musí každá představitelná teorie s více časy. Další časové dimenze navíc čelí známým problémům tachyonů a ghostů (viz [Physical Review D 63, 065014](https://doi.org/10.1103/PhysRevD.63.065014)). Nulový mód \(n=0\) pro obě znaménka reprodukuje běžnou disperzi; jeho samotné měření mezi modely nerozliší.

<!-- BILINGUAL-UNIT: hypertravel.warped -->
## Pozitivní srovnávací příklad: kauzální zkratka v předpokládané zakřivené geometrii

Výsledek o nepřítomnosti zkratky v plochém součinovém prostoru **nevylučuje** zkratku v zakřiveném vyšším prostoru. Uvažujme **samostatně předpokládanou** lokální metriku v jednotkách \(c=1\) s přístupnou další **prostorovou** souřadnicí \(\psi\):
\[
\boxed{ds^2=-dt^2+a(\psi)^2dx^2+d\psi^2,\qquad
a(\psi)=\exp[-(\ln2)\psi^2].}
\]
Při \(\psi=0\) je \(a(0)=1\). Signál omezený na tento řez potřebuje čas \(T_{\rm brane}=L=10\) pro spojení bodů \(x=0\) a \(x=10\). **Po částech budoucnostně orientovaná nulová** cesta však může vystoupat z \(\psi=0\) do \(\psi=h=1\), pohybovat se ve směru \(x\) při \(\psi=h\) a vrátit se. Svislé úseky potřebují každý jednu jednotku souřadnicového času a díky \(a(h)=1/2\) trvá prostřední úsek \(L/2=5\). Proto
\[
\boxed{T_{\rm route}=2h+a(h)L=2+5=7<10=T_{\rm brane}.}
\]
Jde o konkrétní **kauzální geometrickou zkratku v předpokládané metrice**: žádný úsek lokálně nepřekračuje rychlost světla. Lomená nulová cesta má rohy a nemusí být geodetikou volně letícího tělesa; lze ji přiblížit hladkými kauzálními cestami s nepatrně delším časem stále menším než deset. Metrika je skutečně **zakřivená**, přičemž skalární křivost zobrazeného součinového sektoru se třemi souřadnicemi je
\[
\mathcal R=-2a''/a=4\ln2-8(\ln2)^2\psi^2.
\]
V plochém vyšším prostoru s \(a\equiv1\) trvá stejná oklika \(2h+L>L\), takže faktor zakřivení je nezbytný.

**Fyzikální omezení:** jde o vnějším předpokladem zadanou geometrii, **nikoli o metriku odvozenou z uzamčené čtyřrozměrné sharp metriky UBT** nebo jejích pohybových rovnic. Zatím nemáme zdrojový tenzor energie ani ověření energetických podmínek, stabilitu a vazbu fyzikálních signálů, možnost vstupovat do dalšího směru a vracet se, slučitelnost se známými gravitačními testy ani globální chronologii. Nedokazuje postavitelné hyperprostorové vozidlo ani cestování do minulosti. Poskytuje však užitečný **pozitivní cíl pro rozlišení modelů**: dokáže skutečná UBT s jediným polem \(\Theta\) vytvořit stabilní zakřivenou geometrii s měřitelným dřívějším příchodem vůči signálu omezenému na náš řez, aniž by porušila lokální kauzalitu?

<!-- BILINGUAL-UNIT: hypertravel.nec -->
## Kontrola energetických podmínek zakřivené zkratky

Uvedený faktor zakřivení splňuje test **kauzální geometrie**, ale neprochází důležitým testem **zdroje v běžné Einsteinově gravitaci**. V předpokládané metrice je budoucnostně orientovaný vektor \(\ell=\partial_t+\partial_\psi\) nulový a v bodě \(\psi=1\) platí:
\[
\boxed{R_{\mu\nu}\ell^\mu\ell^\nu=-\frac{a''(1)}{a(1)}
=2\ln2-4(\ln2)^2\approx-0.5355<0.}
\]
Tím je porušena **podmínka nulové konvergence**. Pokud by předpokládaná zakřivená metrika musela vyhovovat nezměněným Einsteinovým rovnicím s kladnou gravitační vazbou, jejich kontrakce v nulovém směru vyžaduje \(T_{\mu\nu}\ell^\mu\ell^\nu<0\), tedy porušení **nulové energetické podmínky** pro zdroj (kosmologická konstanta z nulové kontrakce vypadne). Tvrzení platí **pro uvedenou metriku a předpokládané rovnice**, nikoli jako všeobecný zákaz všech geometrických zkratek nebo budoucí dynamiky UBT. UBT dosud neodvodila zdroj, zakřivení ani jeho stabilitu. Jde o negativní test fyzikální přípustnosti proti předčasným tvrzením o pohonu.

<!-- BILINGUAL-UNIT: hypertravel.selection -->
## Co musíme v UBT skutečně odvodit

Před fyzikálním použitím jakékoli zkušební signatury \(\psi\) je nutné nezávisle získat z **jediného pole \(\Theta\)**: (1) určitý kovariantní dynamický operátor, (2) zachovávaný fyzikální presymplektický proud a uzavřené kalibrační vazby, (3) skutečný význam a obor \(\psi\) (parametr vlákna, kompaktní prostorová souřadnice, fyzikální druhý čas, nebo nic z toho), (4) kladnou normu fyzikálního spektra a reálné charakteristické kužele, (5) vyvratitelnou předpověď **odlišnou** od standardní relativity, Wignerovy rotace a běžných Kaluzaových–Kleinových hmotností.

Tvrzení o cestování hyperprostorem navíc vyžaduje fyzikální, na vztažné soustavě nezávislou pozorovatelnou cestovní dobu, globálně definovanou kauzální geometrii, přípustnou světočáru mezi koncovými body a výslovné kontroly energie a vazeb. Žádný takový mechanismus zde nebyl odvozen ani pozorován.

**Rozhodnutí:** spinorovou rotaci o \(4\pi\) a plochou signaturu dalšího času ponechat jako **negativní srovnávací modely**. Před návrhem zařízení nebo tvrzením o cestování časem upřednostnit skutečný hlavní symbol samotné \(\Theta\) a spektrum po redukci vazeb. [Rozpracovaný fyzikální symplektický proud](https://github.com/UBT-Institute/unified-biquaternion-theory/pull/912) je předpokladem, nikoli důkazem úspěšné fyziky. Směr RH/theta liftů je volitelný, dokud nemáme fyzikální operátor.

<!-- BILINGUAL-UNIT: hypertravel.verification -->
## Ověření

Patnáct deterministických přesných testů v SymPy 1.14.0 prošlo lokálně dne 2026-11-22: Lorentzova algebra, kovariance a nekomutativita konečných boostů, příklad budoucího kužele, nepřítomnost posunu počátku, spinorové chování při \(2\pi/4\pi\), plochá KK disperze a rychlost, tachyonický mód pro druhý čas, společný nulový mód a kauzální mez plochého prostorového \(\psi\), plochou okliku vyšším prostorem, lomenou nulovou zkratku v zakřiveném prostoru a nenulovou skalární křivost včetně kontroly nulové konvergence a energetické podmínky. Zdroj: \`research_tracks/action_selection/tests/test_double_rotation_extra_time_gate.py\`. Přesná algebra pouze **zkušebních modelů**; žádná numerická předpověď UBT, žádný běh Lean, žádný úplný průchod CI repozitáře ani nezávislá sémantická kontrola dvojjazyčnosti. **LEAN-PENDING.**
