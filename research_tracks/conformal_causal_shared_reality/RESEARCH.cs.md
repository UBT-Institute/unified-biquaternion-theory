<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# Konformní kauzalita a sdílená realita: most UBT postavený na větách

**2026-10-28 · C_working · nezávislé na PR #807 a PR #808.**
Studujeme podmíněně **jeden** maticový chart X∈Mat₂(C)
možného většího či jinak realizovaného nosiče UBT. Neurčujeme
fundamentální počet složek Theta ani neztotožňujeme komplexní
čas psi se čtyřmi imaginárními Minkowského souřadnicemi.
Žádná akce zde není vybrána.

## Tři principy zůstávají oddělené

**[G] Bikvaternionová geometrie:** C⊗H≅Mat₂(C) je známá
algebraická realizace. Matice W rozměru 2×2 slouží jen jako testovací sektor;
počet dimenzí chartu neurčuje počet fundamentálních složek.

**[C] Konečná rychlost signálu a kauzální uspořádání:**
Je-li dán Lorentzův prostoročas s kauzálním uspořádáním,
Zeemanova věta (1964) omezuje za příslušných předpokladů
jeho *globální* kauzální automorfismy ve vhodných dimenzích
na nehomogenní Lorentzovu grupu a kladné dilatace.
Samotná konečná rychlost neodvozuje lokální SU(2,2)
kalibrační fibraci, Einsteinovu akci ani měřítko metriky.
SO(2,4) je lokální konformní algebra plochého 4D
Minkowského prostoru; výběr Cartanovy geometrie je
samostatná hypotéza.

**[SR] Sdílená realita, operační KANDIDÁT AXIOMU:**
Každému kauzálnímu diamantu O přiřadíme algebru
lokálních pozorovatelných A(O) a kompatibilní stav omega_O.
Pro O1⊂O2 požadujeme A(O1)⊂A(O2) a
omega_O2|A(O1)=omega_O1; prostorově oddělené oblasti
splňují mikrokausalitu. Souhlas na překryvech je nutný,
ale v kvantové teorii sám nezaručuje existenci společného
globálního stavu (problém kvantových marginálů).
Princip zatím není dynamickým zákonem, symplektickou
strukturou ani selektorem akce.

## Testovací chart, kauzální kvadratická forma a metrika vnitřku

Uvažujme W=X+iY∈Mat₂(C), X=X†, Y=Y†, Y
pozitivně definitní. To je **future tube** T_+
komplexifikovaného Minkowského prostoru.
Pro X=x^mu sigma_mu platí

\[
 \det X=(x^0)^2-(x^1)^2-(x^2)^2-(x^3)^2.
\]

Podgrupa SL(2,C) transformuje X→SXS†, Y→SYS†,
čímž zachovává det X i budoucí kužel Y>0.
Totéž zachovávají hermitovské translace a kladné
dilatace. Plná SU(2,2) působí ve vhodné realizaci
lomově lineárně. Symetrická doména je G/K s
G=SU(2,2), K=S(U(2)×U(2)); dim G=15, dim K=7.

Přirozená pozitivní hermitovská metrika na T_+
má (až na měřítko) tvar

\[
 h_W(dW,dW)=\operatorname{Tr}
  (Y^{-1}dW\,Y^{-1}dW^\dagger)
 =\left\|Y^{-1/2}dW\,Y^{-1/2}\right\|_{\rm HS}^2\ge0.
\]

Pro nenulové dW je kladná. V bodě Y=I a při
dW=Σ_mu (dx_mu+i dy_mu)σ_mu dostaneme
h=2Σ_mu[(dx_mu)^2+(dy_mu)^2], signatura (8,0).
Její pullback libovolným hladkým Theta do reálné
čtyřvariety je tedy pozitivně semidefinitní,
nikoliv nedegenerovaná Lorentzova metrika.

**VĚTA T1 [analytická, podmíněná chartem future tube]:**
Lorentzovu tetrádu UBT nelze získat *pouze*
pullbackem této přirozené pozitivní metriky.
Nevylučuje to jiné bilineární formy, kovariantní
jety, soldering mapy, Cartanovy redukce či dynamiku.

Podmínka Y>0 zároveň znamená, že hranice Y=0
s reálným Hermitovským Minkowského prostorem
není regulární vnitřní bod. Ani konvence tetrády
i·Herm z repozitáře sama neurčuje vnitřek tube
či fyzikální význam psi.

## Klíčová přehlédnutá grupově-teoretická překážka

Máme DVA odlišné homogenní prostory:

\[
 \mathcal T_+=G/K,\quad K=S(U(2)\times U(2)),\quad\dim=8;
 \qquad
 \overline{\mathbb M}^{1,3}=G/P,\quad\dim=4,
\]

kde P je parabolický stabilizátor reálné nulové
přímky v SO(2,4), resp. jeho vzor v SU(2,2).
Struktura identity-komponenty je
P≈(Spin(1,3)×R_{>0})⋉R^4 (až na konečná centra).
Maximální kompaktní podgrupa P má dimenzi 3
(Spin(3)), zatímco K má dimenzi 7.

**VĚTA T2 [standardní argument Lieových grup,
podmíněný modelem G/K]:** Neexistuje
G-ekvivariantní mapa f:G/K→G/P.
Důkaz: Ekvivariance by pro f(eK)=gP znamenala,
že každý k∈K fixuje gP, tj. g^{-1}Kg⊂P.
Levá grupa je kompaktní a sedmirozměrná (dimenze 7).
Každá kompaktní podgrupa P leží až na konjugaci
v maximální kompaktní podgrupě dimenze 3.
Spor. QED.

**Rozsah:** neexistuje bodová *plně G-ekvivariantní*
redukce z jediného pole vnitřku future tube na
konformní kompenzátor nulového směru.
Nejde o no-go pro konstrukce používající první
jet J¹Theta, nezávislou konformní Cartanovu
konexi, hraniční či degenerovanou větev,
další vázané objekty nebo menší grupu symetrie.
Každý takový pokus musí předložit explicitní
transformační pravidla.

## Co musí skutečné nové konformní Cartanovo uzavření splnit

Pro Lorentzovu konformní Cartanovu geometrii se
pracuje s hlavní P-fibrací a konexí, jejíž lokální
rozklad lze (až na konvence znamének) psát

\[
 \mathcal A=e^aP_a+\tfrac12\omega^{ab}M_{ab}
                  +bD+f^aK_a.
\]

Soldering 1-formy e^a jsou **součástí konexe**.
Pouhé prohlášení e=pi_P(A) metriku dodává jako
nezávislou proměnnou, nikoliv jako důsledek Theta.
Normální Cartanovu konexi lze jednoznačně
sestrojit z JIŽ DANÉ konformní třídy; ani to
neodvozuje tuto třídu z Theta.

Hledáme případnou kovariantní mapu prvního jetu:
\[
 \mathcal E:J^1\Theta\times\{\mathcal A\}
       \longrightarrow T^*M\otimes\mathbb R^{1,3},
 \qquad e^a_\mu=\mathcal E^a_\mu(\Theta,D_\mu\Theta,\mathcal A).
\]
Nutno dokázat: (i) správnou G/P-kovarianci,
(ii) Lorentzovu realitu a invertibilitu,
(iii) hodnost 16 přípustné variační mapy,
(iv) absenci nezávisle zadaného e,
(v) fyzikální status konexe a jejích módů.

**Falešný úspěch:** nastavit e_mu^a=A_mu^{P_a}
jako volné nezávislé složky bez odvození či
vazby na Theta. Může jít o legitimní gravitační
model, ale není to odvození z Theta.

**OTEVŘENO / NESPOČÍTÁNO:** ekvivariantní
most prvního jetu, klasifikace invariantních akcí,
prostorově obecná Diracova analýza,
stabilita/ghosty a odvození GR.

## Fáze a upozornění ke komplexnímu času

Nelze zaměňovat obyčejnou maticovou fázi
W→e^{iα}W ve future tube s automorfismem
maticového disku Z→e^{iα}Z. Druhý lze realizovat
v SU(2,2), ale po Cayleyově transformaci už
neodpovídá prostému násobení W fází.
Protipříklad: W=diag(1,-1)+iI patří do T_+,
zatímco iW=-I+i·diag(1,-1) do T_+ nepatří.
Ani nepřítomnost fáze, ani její interpretace
jako Wickovy rotace t↔psi není dokázána.
Původní otázku fáze UBT necháváme OTEVŘENOU.

## Informace jako filtr, nikoliv zkratka k akci

Pro věrný referenční stav s vhodně definovaným
či regulovaným modulárním Hamiltoniánem
K_O=-log rho_O platí v okolí referenčního stavu
entanglementová první věta
delta S_O=delta< K_O >.
U zvláštních konformních vakuových koulí
má K_O lokální geometrický tvar.
Jacobson (2016) za explicitních předpokladů
spojuje entropickou rovnováhu malých koulí
při fixovaném objemu s Einsteinovou rovnicí;
obecný nekonformní případ vyžaduje další domněnku.
Tato identita nevytváří sama o sobě klasickou
symplektickou formu Theta ani nevybírá
koeficienty akce UBT. Nejprve potřebujeme
explicitní mapu závislou na Theta od diamantů
a stavů k variacím Cartanovy/metrické geometrie,
včetně normalizace entropie plochy a tenzoru
energie-hybnosti.

## Konečné výzkumné brány ve správném pořadí

1. **G0 — audit chartu:** Hermitovské matice,
   determinant, kužel, fáze, doména, signatury,
   stabilizátory. Testy ověřují konečnou algebru
   a analytické překážky T1–T2. Není to úplný
   důkaz v Leanu.
2. **G1 — jet/tetráda:** sestavit skutečně
   z Theta odvozenou Lorentzovu tetrádu s úplnou
   kovariancí a certifikátem hodnosti 16, nebo
   nalézt explicitní no-go/protipříklad. Porovnat #807.
3. **G2 — informační most:** upřesnit axiomy
   sdílených stavů a vypočítat variační důsledek
   na konkrétním konečném kauzálním diamantu.
   Nepředpokládat bez důkazu koeficient plošného
   zákona ani ztotožnění modulárního času.
4. **G3 — klasifikace akce:** po G1–G2
   vyčíslit polynomiální invarianty do explicitního
   celkového stupně; rozlišit zavedené a odvozené
   koeficienty narušení symetrie.
5. **G4 — Dirac a spektrum:** prostorově obecné
   vazby obou tříd, znaménka redukované kinetiky,
   helicity, hyperbolicita, limita GR, poté
   předregistrovaná nová měřitelná predikce.

**Zastavit po G1 kvůli nezávislé kritické kontrole.**
Ani negativní výsledek G1 není důvod zahodit
původní bikvaternionový projekt nebo mazat historii.

## Znovupoužití a izolace

- PR #807: no-go původní holé akce,
  redukovaný Holstův Hamiltonián,
  provizorní počet složek Theta.
- PR #808: odlišný SO(1,4) pětivektorový
  Cartanův model a hodnost plně proměnných
  složek rozšířené konexe.
- Nedotýkat se jejich větví, canonical/,
  claim matrix ani záznamů o autorství.
  Tento track vychází z master.
- Nic automaticky nemergovat ani nepovyšovat
  na definitivní akci UBT.

## Primární zdroje

- E. C. Zeeman, *Causality Implies the Lorentz Group*,
  J. Math. Phys. **5** (1964) 490,
  https://doi.org/10.1063/1.1704140
- A. Čap, referenční materiál ke konformní
  parabolické geometrii:
  https://www.mat.univie.ac.at/~cap/files/Srni20-beamer-3.pdf
- Konformní Cartanova geometrie a normálnost:
  https://intlpress.com/site/pub/files/_fulltext/journals/atmp/2018/0022/0008/ATMP-2018-0022-0008-a001.pdf
- SU(2,2) Hermitovská realizace tube:
  https://doi.org/10.1016/j.jnt.2026.02.009
- T. Jacobson, *Entanglement Equilibrium and the
  Einstein Equation*, PRL **116** (2016) 201101,
  https://doi.org/10.1103/PhysRevLett.116.201101

**Machine-readable claim statuses:** OPEN (kinematical jet bridge), OPEN (dynamics/Dirac spectrum).

## Kanonické srovnání sharp-vs-dagger [PROVED, omezeně; OPEN jako dynamika]

Dvojjazyčná poznámka G1_CANONICAL_SHARP_BRIDGE.en.md / .cs.md
kontroluje skutečný kanonický antikomutátor vůči dřívějšímu
Hermitovskému Gramovu srovnávacímu předpisu s dagger.
Kanonická forma sharp je komplexně bilineární a centrální
pro libovolné jety Mat(2,C), ale není automaticky reálná;
srovnávací forma dagger je reálná a fázově invariantní,
avšak **není** uzamčenou metrikou.
V regulárním bodě dříve uvedeného zakřiveného příkladu
je C_tt=1, C_xx=-2i, zatímco B_tt=1, B_xx=-2, pro kappa=1.
Společná jednotková fáze nesoulad neodstraní.
Algebraická faktorizace B na reálnou tetrádu není totéž
co získání kanonické metriky z DTheta.

Nová přesná věta pro čistý gradient: pro Theta=X+iY,
rank(dX)=4 a Im C(dTheta,dTheta)=0 při nulové konexi
splňuje Y v souřadnicích X Minkowského Killingovu rovnici;
výsledná nedegenerovaná centrální metrika je plochá.
To **není** no-go pro komplexní Theta: existuje explicitní
afinní komplexní tetráda mimo i-Herm s přesně reálnou
kanonickou Minkowského metrikou.
Chybějící konstruktivní složkou je netautologická
**dvoustranná** kovariantní konexe odvozená z Theta,
která vytvoří zakřivenou reálnou kanonickou centrální
metriku ze svých vlastních jetů.
G1 PARTIAL; fyzikální akce nebyla vybrána.
