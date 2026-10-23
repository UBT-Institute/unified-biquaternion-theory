<!-- BILINGUAL-UNIT: c5-aux.scope -->
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

# Test pomocného jetu v kinetické akci kontrahované vlastní metrikou

Datum: 2026-10-08. Stav: **DERIVED_WITH_ASSUMPTIONS [L1]**; fyzikální dokončení: **OPEN_GAP**. Jde o lokální překážku pro jednu výslovně definovanou akci ve výzkumné alternativě s nezávislým komplexním tau. Nemění kanonický registr akcí UBT ani nevyvrací jeho podmíněnou efektivní větev obecné relativity. [Přehled](README.cs.md) odděluje hypotézu komplexních souřadnic od tohoto reálného variačního testu.

<!-- BILINGUAL-UNIT: c5-aux.assumptions -->
## Oblast, nezávislé proměnné a reprezentace

Pracujeme na orientované reálné pětirozměrné oblasti, s hladkými poli, variacemi s kompaktní podporou a pevnou orientací. Volíme pevnou nikde nenulovou jednoformu u a předepsanou referenční Lorentzovu konexi omega. Nezávislými proměnnými jsou Lorentzovsky reálné složky X původního pole Theta, pomocná Lorentzovsky antisymetrická jednoforma K a relativně centrální reálná jednoforma w. Nepřidáváme další fundamentální hmotové pole. Pevnou globální normalizaci jetu absorbujeme do polí a volíme nenulovou konstantní tenzi T.

\[
A=0,\ldots,4,\quad a=0,\ldots,3,\quad
\eta_{ab}=\operatorname{diag}(-1,1,1,1),\quad
X^2=\eta_{ab}X^aX^b\ne0,\quad K_{Aab}=-K_{Aba}.
\]
\[
E_A^a=\partial_A X^a+\omega_A{}^a{}_bX^b
       +K_A{}^a{}_bX^b+w_AX^a,\qquad
e_A{}^I=(E_A^a,u_A),\qquad \det e\ne0.
\]

Složený korámec E nevarírujeme nezávisle. V bikvaternionové reprezentaci označuje ddagger hermitovské sdružení, Omega reprezentuje referenční Lorentzovu konexi a kaligrafické K její Lorentzovu jetovou korekci. Strany násobení jsou uvedeny výslovně:

\[
D_A\Theta=\partial_A\Theta+A_A\Theta-\Theta B_A,
\quad A_A=\Omega_A+\mathcal K_A+\tfrac12w_AI,
\quad B_A=-\Omega_A^\ddagger-\mathcal K_A^\ddagger-\tfrac12w_AI.
\]

Relativně centrální člen představuje dilataci jetu, nikoli metrickou fyzikální spinovou konexi. Tento výpočet neztotožňuje jetovou konexi s fyzikální Leviho–Civitovou konexí. Současné Lorentzovy změny rámce pro X, E a konexe zachovávají konstrukci; kalibračně invariantní potenciál musí být rovněž Lorentzovsky invariantní. Výpočet níže připouští libovolný hladký algebraický potenciál v pevném rámci. Nepředpokládá kvocient podle kalibračních transformací ani počet fyzikálních stupňů volnosti.

<!-- BILINGUAL-UNIT: c5-aux.action -->
## Definovaná akce a přesná kinetická kontrakce

Použijeme stejné Lorentzovo párování v metrice i kinetickém členu a hladký potenciál závisející pouze na hodnotách pole:

\[
g_{AB}=\eta_{ab}E_A^aE_B^b+u_Au_B,
\qquad
S_{\rm aux}=\mathcal T\int d^5Z\sqrt{|g|}
\left[\tfrac12g^{AB}\eta_{ab}E_A^aE_B^b-V(X)\right].
\]

Tento kandidát neobsahuje členy křivosti, derivace K ani w ani další členy. Invertibilita úplného korámce dává následující identity, aniž by E musel být exaktní:

\[
g^{AB}u_Au_B=1,\qquad
g^{AB}\eta_{ab}E_A^aE_B^b=4,\qquad
S_{\rm aux}=\mathcal T\int d^5Z\sqrt{|g|}F(X),
\quad F=2-V.
\]

Na rozdíl od případu exaktního gradientu nemusí být tato hustota zpětným obrazem pevné formy nejvyššího stupně. Její pomocnou variaci je proto nutné vypočítat. Držet složenou metriku pevnou by znamenalo jiný variační problém.

<!-- BILINGUAL-UNIT: c5-aux.inverse -->
## Použití existující pravé inverze jetu na kandidáta [L1]

Při pevných X a omega zvolme libovolnou hladkou cílovou variaci Y s kompaktní podporou. Existující konstrukce rozděleného jetu [U1, U2] platí nezávisle v každém souřadnicovém směru:

\[
\delta E_A^a=\delta K_A{}^a{}_bX^b+\delta w_AX^a,
\qquad
\delta w_A=\frac{X\cdot Y_A}{X^2},\qquad
Y_{\perp A}=Y_A-\delta w_AX,
\]
\[
\delta K_{Aab}=\frac{Y_{\perp Aa}X_b-X_aY_{\perp Ab}}{X^2}.
\]

Antisymetrie je explicitní. Kontrakce s X dává kolmou složku cíle a centrální člen složku rovnoběžnou. Pomocná variace tak realizuje každou variaci E. Na oblasti s nenulovou normou zůstávají zachovány hladkost i kompaktní podpora. Tato pravá inverze je existujícím výsledkem; zde testujeme její použití na uvedenou akci.

<!-- BILINGUAL-UNIT: c5-aux.stationarity -->
## Stacionarita vynucuje kritický nulový koeficient [L1]

Inverzní korámec označme e s dolním vnitřním a horním souřadnicovým indexem. Při pevném u je úplná variace

\[
\delta\sqrt{|g|}=\sqrt{|g|}\,e_a{}^A\delta E_A^a,
\qquad
\delta S_{\rm aux}=\mathcal T\int d^5Z\sqrt{|g|}
\left[F e_a{}^A\delta E_A^a-V_{,a}\delta X^a\right].
\]

Nejprve položíme variaci pole rovnu nule. Surjektivita zpřístupňuje každou variaci korámce, takže stacionarita vyžaduje vymizení F. Ekvivalentně zvolíme libovolný hladký skalár epsilon s kompaktní podporou a přeškálujeme všechny sloupce E:

\[
\delta E_A^a=\epsilon E_A^a,\qquad
\delta\sqrt{|g|}=4\epsilon\sqrt{|g|},\qquad
\delta S_{\rm aux}=4\mathcal T\int d^5Z\epsilon\sqrt{|g|}F
\quad\Longrightarrow\quad F=0.
\]

Ve stacionární konfiguraci F mizí na celé oblasti. Všechny indukované variace korámce při variaci X proto mají nulový koeficient, včetně derivačních členů. Zbývající rovnicí pole je podmínka kritického bodu:

\[
\boxed{V(X)=2,\qquad V_{,a}(X)=0.}
\]

Tyto podmínky jsou v daném oboru také postačující pro lokální stacionaritu. Nemá-li potenciál kritický bod s nenulovou normou při požadované hodnotě, neexistuje zde nedegenerovaná stacionární konfigurace. Má-li jej, konstantní pole v tomto bodě může pomocnou pravou inverzí realizovat libovolný úplný korámec s pevným u. Akce pak nevybírá jeho geometrii. Jde o vymizení skalárního koeficientu, nikoli o nulový či degenerovaný metrický objem.

<!-- BILINGUAL-UNIT: c5-aux.quadratic -->
## Kvadratická objemová akce [L1]

Rozvineme akci kolem libovolného stacionárního pozadí a připustíme fluktuace všech nezávislých proměnných. Poruchu pole označíme xi a kvadratickou akci definujeme jako koeficient druhé mocniny rozvojového parametru. Konstantní i lineární Taylorův koeficient F mizí, takže každá porucha objemu začíná přispívat až ve vyšším řádu:

\[
X=X_0+\varepsilon\xi+O(\varepsilon^2),\qquad
F(X_0)=0,\quad F_{,a}(X_0)=0,
\]
\[
\boxed{S^{(2)}=-\frac{\mathcal T}{2}\int d^5Z\sqrt{|g_0|}
V_{,ab}(X_0)\xi^a\xi^b.}
\]

V této kvadratické objemové akci nejsou derivace poruch. Na těchto pozadích neposkytuje běžný vlnový ani gravitonový kinetický operátor. Nejde o úplnou hamiltonovskou analýzu vazeb, výsledek o stabilitě ani tvrzení o každé komplexní složce Theta. Nulový Hessův operátor v některých směrech nedokazuje zdravý propagující mód.

<!-- BILINGUAL-UNIT: c5-aux.boundary -->
## Vztah ke kanonické akci a další výpočet

Překážka využívá nezávislé algebraické K a w, pevné u, stejné párování v metrice a kinetice a nepřítomnost dalších členů. Předepsaný složený jet závislý na derivacích tyto nezávislé variace nepřipouští; jeho úplné řetězové pravidlo i Hessův operátor se musí vypočítat zvlášť. Dosazení Leviho–Civitovy konexe jako funkcionálu E rovněž mění variační problém. Ani jednu z těchto substitucí tato věta neanalyzuje.

Existující Palatiniho kandidát s rozděleným jetem [U2] obsahuje křivost. Jeho pomocná variace přenáší Palatiniho rovnici pro korámec, která obsahuje více než skalární objemový koeficient. Tento výsledek proto neodporuje uvedené podmíněné konstrukci obecné relativity. Existující audit pevných konexí a konexí závislých na hodnotách pole [U3] již nachází příbuzné překážky pro Hessův operátor; u těchto dřívějších výsledků si nenárokujeme prvenství. Autoritou zůstává registr jediné akce [U4].

Dalším užitečným testem je výslovně specifikovaný složený jet závislý na derivacích s úplnou kvadratickou akcí a kvocientem podle vazeb, nebo odvození členu křivosti z registrované rodiny akcí. Dodatečná souřadnice a pomocná reprezentovatelnost samy chybějící dynamiku nedodávají. Zápis nepředpovídá konstantu jemné struktury ani kvantování energie a nedokazuje ekvivalenci se strunovou teorií.

<!-- BILINGUAL-UNIT: c5-aux.verification -->
## Ověření a omezení

`verify_auxiliary_action.py` zaznamenává 22 přesných kontrol do `auxiliary_action_results.json`: obecnou pravou inverzi v SymPy, kinetickou kontrakci korámce, škálování objemu a kvadratický koeficient a dále nezávisle implementované racionální pravé inverze, determinanty a polynomiální interpolaci pomocí Python Fraction. Racionální kanál je konečný soubor ověřených příkladů; obecný analytický argument je uveden výše. Verze nástrojů, předpoklady a vyloučené oblasti jsou zaznamenány v JSON a `status.json`.

**LEAN-PENDING:** V použitém prostředí nebyly dostupné spustitelné programy Lean a Lake. Lokální variační věta nebyla formalizována v Lean. Kontroly neověřují mikroskopickou akci UBT, všechny komplexní módy, fyzikální kalibrační kvocient, stabilitu ani pozorování. Zdrojem překladu byla angličtina; shodná struktura nenahrazuje lidskou revizi významové ekvivalence požadovanou před sloučením.

<!-- BILINGUAL-UNIT: c5-aux.sources -->
## Zdroje v repozitáři

- [U1] [Existující pravá inverze rozděleného jetu](../../canonical/gr_closure/gap_10t_split_jet_right_inverse.tex).
- [U2] [Palatiniho variační přenos rozděleným jetem](../action_selection/split_jet_palatii_variational_lift.cs.md).
- [U3] [Audit akce s pevnou konexí a konexí závislou na hodnotách pole](../action_selection/biquaternionic_induced_gravity_boundary.cs.md).
- [U4] [Registr jediné akce](../../canonical/ACTION.cs.md).
