<!-- BILINGUAL-UNIT: splitjet-dirac.scope -->
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

# Lokální Diracova redukce rodičovské akce čistě gravitačního split-jet sektoru

**2026-10-29; C_working; CONDITIONAL.** Zdrojem překladu je angličtina. [Úplný prostorový metrický výpočet](full_spatial_dynamics_2026_10.cs.md) předpokládal kanonický redukovaný metrický fázový prostor. Tato poznámka řeší dodatečnou jetovou část tohoto předpokladu pro již zvolenou čistě gravitační akci: její pomocné rozšíření zachovává Diracovy závorky základní teorie a nepřidává lokální fyzikální mód. Nevybírá základní akci z mikroskopické dynamiky Theta.

<!-- BILINGUAL-UNIT: splitjet-dirac.assumptions -->
## Oblast platnosti a nezávislé proměnné

Používáme hladká pole v regulárním souřadnicovém okolí nenulového interního vektoru s nenulovou normou, nedegenerovanou Lorentzovu tetrádu, pevnou kladnou normalizaci a kompaktní prostorový řez bez hranice nebo variace s kompaktním nosičem. Lokální hodnosti vazeb i symplektický kvocient základní teorie musí být regulární. Metrika zůstává kanonickou metrikou z centrálního součinu sharp. Základní akce je zadána, nezávisí explicitně na redundantním nosiči ani jetovém jádru a připouští hamiltonovský zápis prvního řádu s vazbami. Zamýšlenou základní teorií je zvolená bezspinová Palatiniho–HT gravitační akce; její obvyklá redukce spojení, Lorentzova redukce, redukce vazeb jednoduchosti a HT redukce zůstávají operacemi základní teorie, nikoli novými výsledky zde.

\[
s=\sqrt{\mathcal N_0}>0,\quad X^2=\eta_{ab}X^aX^b\ne0,\quad
Q_\mu=K_{J\mu}X+w_\mu X,\quad
sE_\mu=\partial_\mu X+\omega_\mu X+Q_\mu.
\]

Vektorový zápis je Lorentzovsky reálným gravitačním nosičem deklarované oboustranné derivace, nikoli náhradní algebrou pole nebo volbou fundamentálního počtu složek Theta. Fyzikální křivost používá nezávislé variační Lorentzovo spojení, zatímco jetová korekce je oddělená. Omezení tohoto výpočtu na gravitační funkcionál neodstraňuje zbývající sektory komplexní Theta, imaginárního času ani hmoty.

<!-- BILINGUAL-UNIT: splitjet-dirac.coordinates -->
## Adaptované jetové souřadnice a nutný posun hybnosti

Stávající věta o hodnosti poskytuje lokální adaptované souřadnice složené z obrazu a stabilizátoru. Stabilizátor má dimenzi **3** pro každý prostoročasový index, tedy celkem **12**. Jde o lokální bodovou transformaci s rámcem závislým na nosiči. Její úplný kotečný zdvih je

\[
k_\mu=(K_{J\mu},w_\mu)=k_\mu(X,u_\mu),\quad u_\mu=(Q_\mu,z_\mu),
\]
\[
P_X=p_X+\sum_\mu (\partial_X k_\mu)^T p_{k_\mu},\qquad
P_{u_\mu}=(\partial_{u_\mu}k_\mu)^T p_{k_\mu},
\]
\[
p_X\,\delta X+\sum_\mu p_{k_\mu}\,\delta k_\mu
=P_X\,\delta X+\sum_\mu P_{u_\mu}\,\delta u_\mu.
\]

Mimo vazbovou plochu nesmíme ztotožnit původní hybnost nosiče s adaptovanou hybností. Všechny hybnosti ve vazbách níže patří adaptovanému kanonickému systému souřadnic. Korekce ze všech prostoročasových sloupců se sčítají do téže hybnosti nosiče.

Konkrétní hladké souřadnicové okolí na budoucí časupodobné komponentě používá následující Lorentzův boost. Matice v klidovém rámci má libovolné prostorové antisymetrické složky, které jsou souřadnicemi jádra.

\[
r=\sqrt{(X^0)^2-\sum_i(X^i)^2}>0,\quad X^0>0,\quad
L^0{}_0=X^0/r,\quad L^0{}_i=L^i{}_0=X^i/r,\quad
L^i{}_j=\delta^i_j+\frac{X^iX^j}{r(X^0+r)},
\]
\[
q=L^{-1}Q,\quad w=q^0/r,\quad
R^0{}_i=R^i{}_0=q^i/r,\quad R^i{}_j=-R^j{}_i,\quad K_J=LRL^{-1}.
\]

Obraz je potom obnoven přesně a pomocný souřadnicový systém je invertibilní. Explicitní testovací bod i jeho derivace zachovávají příčné variace nosiče; nosič není zmrazen na svou klidovou osu. Jiná souřadnicová okolí s nenulovou normou potřebují vlastní hladký rámec stabilizátoru. Pokračování přes nulovou normu se netvrdí.

<!-- BILINGUAL-UNIT: splitjet-dirac.parent -->
## Ekvivalentní rodičovská akce prvního řádu

Nechť zadaný základní funkcionál závisí na tetrádě, fyzikálním spojení a vlastních pomocných proměnných. Následující rodičovskou akci zavedeme výhradně jako přesný přepis s vazbami:

\[
S_{\rm P}=S_0[E,\omega,\ldots]
+\int d^4x\,\lambda^\mu{}_a
\left(sE_\mu^a-\partial_\mu X^a-\omega_\mu{}^a{}_bX^b-Q_\mu^a\right).
\]

Multiplikátor je vektorová hustota. Eliminace jeho vazby obnovuje původní složený gravitační funkcionál. Naopak variace volných proměnných obrazu vynuluje všechny multiplikátory a zůstanou rovnice základní teorie. Nezávisle variovaná tetráda v této rodičovské akci je tedy proměnnou přepisu, nikoli přidaným fundamentálním fyzikálním polem. Souřadnice stabilizátoru v akci nevystupují. Nepřidává se žádný jetový kinetický ani hmotový člen.

Časová závislost nosiče vytváří primární vztah pro hybnost. Prostorové vztahy obsahují úplné prostorové derivace; nejde o homogenní vazby.

\[
p_{Xa}+\lambda^0{}_a=0,\qquad P_{Q_\mu a}=0,\qquad
P_{\lambda^\mu a}=0,\qquad P_{z^I}=0,
\]
\[
F_i=sE_i-\partial_iX-\omega_iX,\qquad
\lambda^i=0,\qquad Q_i-F_i=0.
\]

Poslední dvě rovnice plynou ze zachování prostorových primárních vazeb. Lze eliminovat časovou dvojici, poté prostorové dvojice multiplikátorů a prostorové dvojice obrazu. Původní matice vazeb má nenulové smíšené časové/prostorové složky; před touto postupnou redukcí ji nesmíme považovat za blokově diagonální.

<!-- BILINGUAL-UNIT: splitjet-dirac.graph -->
## Proč se fyzikální Diracova závorka nezmění

Pro libovolnou dvojici určující graf a libovolnou funkci závislou na základních proměnných, včetně funkcí s prostorovými derivacemi, zapišme matici vazeb a její přesnou inverzi jako

\[
\chi=(P_Q,Q-F),\qquad B_{IJ}=\{F_I,F_J\},\qquad
C=\begin{pmatrix}0&-I\\I&B\end{pmatrix},\qquad
C^{-1}=\begin{pmatrix}B&I\\-I&0\end{pmatrix}.
\]

Nepoužívá se předpoklad, že funkce obrazu komutuje se základními proměnnými. Zachovaná pozorovatelná nezávislá na eliminované dvojici má nulovou závorku s její pomocnou hybností. Dolní diagonální blok inverze proto vynuluje celou Diracovu korekci mezi libovolnými dvěma zachovanými pozorovatelnými. Výsledek se postupně použije na časový graf multiplikátoru, prostorové grafy multiplikátorů a prostorové grafy obrazu. V teorii pole značí maticový zápis jádra vyhodnocovaná na testovacích funkcích v uvedené oblasti; derivační vazby jsou zachovány. Tato eliminace pomocných proměnných neobsahuje žádnou inverzní prostorovou diferenciální rovnici ani Greenovu funkci.

Po redukci vazeb druhé třídy jsou kanonický potenciál a hamiltonián

\[
\vartheta_{\rm red}=\vartheta_0+\int
\left(p_X\,\delta X+P_{Q_0}\,\delta Q_0+P_z\,\delta z\right),
\]
\[
H_{\rm red}=H_0+\int p_X\cdot(sE_0-\omega_0X-Q_0),\qquad
\dot P_{Q_0}=p_X,\qquad \dot p_X=\omega_0^Tp_X.
\]

Časová hybnost obrazu a hybnost nosiče jsou první třídy, stejně jako všechny hybnosti stabilizátoru. Zadaná algebra vazeb základní teorie se na jejich kvocientu nezmění: smíšené příspěvky k zachování základních vazeb jsou úměrné těmto dodatečným vazbám. Tvrzení připouští, že základní teorie sama má vazby druhé třídy; nenahrazuje Palatiniho redukci vazeb jednoduchosti odhadnutou metrickou závorkou. Zejména nebyla zmrazena odezva Lorentzova spojení.

<!-- BILINGUAL-UNIT: splitjet-dirac.count -->
## Kalibrační generátor, regulární kvocient a počet módů

Posun nosiče a kompenzující jetový posun mají na zbývajících souřadnicích nosiče/obrazu následující generátor:

\[
G[\varepsilon]=\int\left[\varepsilon\cdot p_X
-(\dot\varepsilon+\omega_0\varepsilon)\cdot P_{Q_0}\right],\qquad
\delta X=\varepsilon,\quad\delta Q_\mu=-D_\mu\varepsilon,\quad
\delta E=\delta\omega=0.
\]

Prostorové posuny obrazu se obnoví z jejich eliminovaných grafových rovnic. Používáme pouze posuny, jejichž konečná dráha zůstává ve zvoleném souřadnicovém okolí. Je-li časové spojení zahrnuto mezi kanonické souřadnice, jeho sdružená hybnost dostává členy úměrné pomocné primární vazbě, protože koeficient generátoru závisí na poli. Tyto členy na kvocientu vymizí; nejsou dalším fyzikálním zdrojem spinu. Posuny stabilizátoru generují jeho adaptované hybnosti. Na dodatečné vazbové ploše je kanonický potenciál přesně potenciálem základní teorie a na regulárním lokálním kvocientu se odstraní všechny dodatečné směry vlákna.

| Přidané konfigurační souřadnice | Počet | Vazby druhé třídy | Vazby první třídy |
|---|---:|---:|---:|
| Časový nosič, obraz a multiplikátor | 12 | 8 | 8 |
| Prostorové obrazy a multiplikátory | 24 | 48 | 0 |
| Souřadnice stabilizátoru | 12 | 0 | 12 |
| Celkem | 48 | 56 | 20 |

\[
\Delta\dim\Gamma_{\rm physical}=2(48)-56-2(20)=0.
\]

Jde o přírůstky vůči fázovému prostoru základní teorie. Nesmějí se znovu přičítat k počtu gravitonů základní teorie. Pro zadanou regulární bezspinovou Einsteinovu větev zůstávají zachovány její **2** lokální tenzorové módy. Globální HT integrační údaj se nepočítá jako nový lokální mód. To je silnější výsledek než mechanická analogie nebo inkluze presymplektických jader, stále však platí pouze pro gravitaci. Nedokazuje, že všechny komplexní směry Theta jsou kalibrační, že další vazby na hmotu tento kvocient zachovají ani že mikroskopická akce má kladnou energii.

<!-- BILINGUAL-UNIT: splitjet-dirac.verification -->
## Ověření a zbývající mikroskopická povinnost

`tools/verify_splitjet_spatial_dirac.py` kontroluje inverzi grafového bloku s nenulovými interními závorkami, původní matici **56** vazeb se smíšenými časovými/prostorovými složkami, časové řetězce zachování a kalibračních transformací a přesné kotečné zobrazení závislé na nosiči. Vynechání posunu hybnosti nosiče dává explicitní selhání. Test společného nosiče zahrnuje všechny prostoročasové sloupce. `tests/test_splitjet_spatial_dirac.py` tyto případy zachovává.

Nezávislá implementace v NumPy/SciPy používá periodickou síť **3** krát **3** krát **3**, tedy **27** prostorových buněk, a **4** interní reálné gravitační souřadnice. Sestavuje všechny gradienty vazeb prostorového obrazu, včetně derivací ve všech směrech a variací fyzikálního spojení, a numericky invertuje jejich matici **648** vazeb. Zachované pozorovatelné zahrnují hybnosti kofrámečku, spojení a nosiče. Derivace grafu je nezávisle kontrolována centrálními diferencemi s krokem **0.00001** a tolerancí **0.00000001**. Tolerance inverze je **0.00000000001** a tolerance fyzikální Diracovy korekce je **0.0000000001**. Tato síť testuje prostorový grafový blok; ostatní řetězce mají samostatné přesné kontroly výše.

`formal/lean/UBT/Hamiltonian/SplitJetDirac.lean` dodává **6** konečných jader: oba součiny inverze grafového bloku nad libovolným okruhem, nulovou grafovou korekci, vyrušení dimenze, aditivní invarianci vertikálního posunu a radiální kotečnou identitu. Report `reports/splitjet_spatial_dirac_2026_10_29.json` váže hashe zdrojů, verze nástrojů a stav kompilace. Lokální prostředí Lean není k dispozici. Úplná kontinuální Diracova věta a redukce základní gravitace zůstávají nad rámec těchto jader ve stavu LEAN-PENDING jako formalizace.

Přepisy závislé na derivacích vyžadují argument invertibility nebo vazeb; nejsou automaticky neškodné. Související obecný problém řeší [Takahashi–Motohashi–Suyama–Kobayashi](https://arxiv.org/pdf/1702.01849). Zde explicitní rodičovské vazby dodávají argument pro tento konkrétní gravitační sektor s nenulovou normou. Dřívější [konečný konfigurační kvocient](mm_finite_splitjet_lift.cs.md) a [presymplektický výpočet](mm_composite_presymplectic_variation.cs.md) jsou předpoklady, nikoli nové objevy. Křivostní akce, kladná Newtonova normalizace, úplná vazba na hmotu/komplexní čas a pokračování přes nulovou normu, globálně i přes horizont zůstávají otevřenými mikroskopickými povinnostmi. Stav fundamentální akce zůstává `DEFINED_FAMILY_NOT_FINALIZED`; gravitační výsledek zůstává `CONDITIONAL`.
