<!-- BILINGUAL-UNIT: c5.scope -->
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

# Nezávislé komplexní tau: testy geometrie a akce

Datum: 2026-10-08. Status: **DERIVED_WITH_ASSUMPTIONS / OPEN_GAP**. Tato autorem požadovaná výzkumná alternativa zachovává nezávislé komplexní tau vedle komplexního časoprostoru. Nenahrazuje kanonickou volbu času, centrální metriku, architekturu jediného pole ani registr akce. Výchozím zdrojovým stavem je commit `2102540b0beb06d3abe707ba941c2a46cae394b9`.

Hlavním výsledkem je rozlišení tří otázek: pátý Cliffordův směr odstraní konkrétní defekt hodnosti; přesný doplněný korámec zůstává plochý; dynamické vložení nebo konstrukce pomocného jetu potřebují vlastní úplnou variaci. Níže uvedené pokračování dokazuje omezenou překážku pomocné akce, nikoli nemožnost celé UBT.

<!-- BILINGUAL-UNIT: c5.domain -->
## Obor a konvence

\[
Z^A=(z^0,z^1,z^2,z^3,\tau)\in\mathbb C^5,
\quad z^\mu=x^\mu+i y^\mu,\quad \tau=s+i\psi,
\quad \Theta:\mathbb C^5\longrightarrow\mathbb C\otimes\mathbb H\simeq\mathbb C^4.
\]

Všech deset reálných souřadnicových parametrů je nezávislých. Tau neztotožňujeme s první časoprostorovou souřadnicí. Holomorfie je dodatečný předpoklad, používaný jen tam, kde je uveden. Rozměr hodnot pole se liší od rozměru souřadnic. Kvaternionová konjugace sharp nesdružuje komplexní koeficienty; v maticové reprezentaci jde o adjugovanou matici. Polarizace jejího determinantu je pevná nedegenerovaná komplexní bilineární forma B. Jednotky a pevná globální normalizace jetu jsou absorbovány do uvedených polí. Fyzikální kosmologické a variační testy níže výslovně volí reálný Lorentzův model; neřeší fyzikální interpretaci všech deseti parametrů.

<!-- BILINGUAL-UNIT: c5.rank -->
## Hodnost a pátý Cliffordův směr [L1]

Pro pět kovariantních derivací s hodnotami ve stejném čtyřrozměrném komplexním nosiči platí

\[
g^{(0)}_{AB}=B(E_A,E_B)=JQJ^T,
\qquad \mathrm{rank}_{\mathbb C}g^{(0)}\leq4.
\]

To plyne z obdélníkového rozměru J a nepředpokládá obyčejné derivace. Jde o defekt hodnosti tohoto nezměněného předpisu, nikoli o námitku vůči kanonické čtyřrozměrné větě o hodnosti zobrazení tetrády na metriku.

Existující Cliffordův převod poskytuje

\[
\mathcal C(E)=\begin{pmatrix}0&E\\E^\sharp&0\end{pmatrix},
\qquad \Gamma_*=\mathrm{diag}(I_2,-I_2),
\qquad \widetilde\Gamma_A=\mathcal C(E_A)+u_A\Gamma_*.
\]
\[
\tfrac12\{\widetilde\Gamma_A,\widetilde\Gamma_B\}
=\bigl[B(E_A,E_B)+u_Au_B\bigr]I_4.
\]

Pokud první čtyři derivace tvoří bázi a pátá forma je zvolena níže uvedeným způsobem, Schurův doplněk dává

\[
g_5=g^{(0)}+u\otimes u,\quad u=\lambda d\tau,
\qquad \det g_5=\lambda^2\det g_4\ne0.
\]

Forma u a její normalizace jsou v této alternativě dodatečným vstupem; jejich dynamický původ není dokázán. Pátá Cliffordova matice již v repozitáři existuje a není zde novým objevem.

<!-- BILINGUAL-UNIT: c5.signature -->
## Spinory, realita a srovnání se strunami

Cliffordův modul pro pět komplexních směrů může používat čtyři komplexní složky. Plný desetirozměrný komplexní Diracův modul má 32 složek; Weylův modul má 16 komplexních složek a Majoranův–Weylův modul v Lorentzově signatuře má 16 reálných složek. Samotný bikvaternion tedy není plným desetirozměrným Lorentzovým spinorem. Při řešení lineárních podmínek antikomutace pro matice stejné velikosti nachází symbolická kontrola pro všech pět zvolených generátorů současně pouze nulovou matici.

Reálná část nedegenerované komplexní symetrické metriky má reálnou signaturu (5,5): násobení komplexní jednotkou obrací její znaménko. Hermitovská signatura (p,q) se naopak mění na (2p,2q). Reálná signatura (1,9) vyžaduje jiný předpis reality či metriky; Lorentzův pětirozměrný reálný model je samostatnou volbou.

Kritický rozměr RNS superstruny plyne z bilance anomálie na světoploše,

\[
c_{\mathrm{total}}=D+D/2-26+11=\tfrac32D-15,
\qquad c_{\mathrm{total}}=0\Longrightarrow D=10.
\]

UBT neposkytla potřebnou teorii světoplochy, fermiony, spektrum ani rušení anomálií [S1, S2]. Fourierovy hybnostní módy na kružnici samy neposkytují nezávislý člen strunového navíjení. Výraz pro nulové módy a jeho dualita jsou pouze srovnávací testy:

\[
\frac{n^2}{R^2}+\frac{w^2R^2}{\alpha'^2},
\qquad R\leftrightarrow\alpha'/R,\quad n\leftrightarrow w.
\]

Pokud by tau naopak parametrizovalo světoplochu, její parametry by se nemohly zároveň počítat jako další souřadnice cílového prostoru.

<!-- BILINGUAL-UNIT: c5.flat -->
## Přesný korámec: plochost a nulová variace akce [L1]

Předpokládejme obyčejné derivace, konstantní B a nenulovou konstantu lambda. Pro holomorfní pole nebo pro odpovídající reálný model definujme

\[
Y=(\Theta^0,\Theta^1,\Theta^2,\Theta^3,\lambda\tau),
\qquad g_5=Y^*\eta_5,\quad \eta_5=\mathrm{diag}(-1,1,1,1,1).
\]

Nedegenerovanost činí čtvercový Jacobián invertibilním. Y jsou pak lokální souřadnice s konstantní metrikou, takže celý Riemannův tenzor mizí. Nekonstantní souřadnicová konexe tento závěr nemění. Faktor závislý pouze na tau lze také integrovat do poslední souřadnice. Jde o rozšíření existujícího výsledku repozitáře o plochosti gradientní konstrukce [U1], nikoli o tvrzení pro libovolné kovariantní derivace.

Na orientovaném reálném oboru zvolme větev Jacobiánu zachovávající orientaci. S kompaktně podporovanými variacemi a potenciálem závislým pouze na hodnotách pole a tau testujme explicitní kompozitní funkcionál

\[
S_{\mathrm{test}}=\mathcal T\int d^5Z\sqrt{|g_5|}
\left[\tfrac12 g_5^{AB}B(\partial_A\Theta,\partial_B\Theta)-V(\Theta,\tau)\right].
\]

Stejné párování v metrice a kinetickém členu dává

\[
g_5^{AB}u_Au_B=1,\qquad
g_5^{AB}B(\partial_A\Theta,\partial_B\Theta)=4.
\]

Hustota je tedy Jacobián násobený níže uvedenou funkcí hodnot pole. Je pullbackem pevné formy nejvyššího stupně. Její variace je podle Cartanovy formule přesná forma a má nulový integrál:

\[
F=2-V,\qquad S_{\mathrm{test}}=\mathcal T\int Y^*(F\,d^5Y),
\qquad \delta S_{\mathrm{test}}=0.
\]

Argument F je zde chápán po souřadnicové substituci. Tvrzení se týká lokální objemové variace na větvi s pevnou orientací, nikoli nulové hodnoty akce, singulárních Jacobiánů, globálních sektorů či okrajové dynamiky. Kontrola ověřuje Piolovu identitu pro obecné funkce a nekonstantní potenciál. Variace kinetického členu při nesprávném zafixování jeho kompozitní metriky toto rušení přehlédne.

<!-- BILINGUAL-UNIT: c5.embedding -->
## Geometrie FLRW a variace vložení [L1]

Pro kladný faktor rozpínání s nenulovou derivací použijme plochou reálnou ambientní metriku a lokální vložení [S3]

\[
ds_5^2=-dU\,dV+d\mathbf X^2,\quad
U=a(t),\quad \mathbf X=a(t)\mathbf x,\quad
V=a(t)|\mathbf x|^2+f(t),\quad \dot f=1/\dot a.
\]

Jeho pullback je prostorově plochá FLRW metrika. Čas a a zde mají jednotku délky; komovující souřadnice jsou bezrozměrné. Prostorupodobná jednotková normála a druhá fundamentální forma mají při uvedené znaménkové konvenci tvar

\[
n=(\dot a,\dot a|\mathbf x|^2-1/\dot a,\dot a\mathbf x),
\quad K_{\mu\nu}=n\cdot\partial_\mu\partial_\nu Y,
\quad K_{00}=\ddot a/\dot a,\quad K_{ij}=-a\dot a\delta_{ij},\quad K_{0i}=0.
\]

Gaussova rovnice poskytuje zakřivenou vnitřní geometrii, i když ambientní křivost mizí. Nulová derivace a zneplatní tuto souřadnicovou mapu, nikoli každé možné vložení.

Nyní dodatečně předpokládejme Einsteinův–Hilbertův funkcionál s kovariantní hmotou na indukované metrice. Jde o podmíněného efektivního kandidáta, nikoli druhou fundamentální akci UBT. Je nutná kompaktní podpora nebo odpovídající okrajové členy. Variace Y včetně indukované variace metriky dává [S4]

\[
\mathcal E^{\mu\nu}=G^{\mu\nu}-\kappa T^{\mu\nu},\qquad
\nabla_\mu(\mathcal E^{\mu\nu}\partial_\nu Y^I)=0,
\qquad \mathcal E^{\mu\nu}K_{\mu\nu}=0.
\]

Poslední rovnice používá zachování hmoty a Bianchiho identitu. S jedinou normálou je slabší než úplné Einsteinovy rovnice. Konstrukce Palatiniho akce s odděleným pomocným jetem v repozitáři používá jinou, surjektivní třídu variací [U2]; tato překážka vložení nezneplatňuje její podmíněný výsledek.

<!-- BILINGUAL-UNIT: c5.cosmology -->
## Podmíněný kosmologický rozlišovací test [L1]

Definujme reziduum Einsteinových rovnic a předpokládejme zachování běžné hmoty:

\[
H=\dot a/a,\quad \rho_X=3H^2/\kappa-\rho,
\quad p_X=(-2\dot H-3H^2)/\kappa-p,
\quad \dot\rho+3H(\rho+p)=0.
\]

Reziduum také splňuje rovnici kontinuity. Normálová rovnice a její první integrál jsou

\[
\rho_X\ddot a/\dot a-3Hp_X=0,
\quad \frac{d}{dt}(a^3\dot a\rho_X)=0,
\quad \boxed{a^4H\rho_X=C},
\quad \boxed{3H^3-\kappa\rho(a)H-\kappa C/a^4=0}.
\]

Jde o známý Reggeho–Teitelboimův integrál [S5], reprodukovaný pro zvolené vložení. C je vstup z počátečních dat, nikoli předpovězená konstanta. Na expandující větvi je jeho znaménko znaménkem rezidua. Umocnění vztahu hustot toto znaménko ztrácí a musí být doplněno neumocněnou rovnicí. Větev s nulovým C a nenulovým H obnovuje Friedmannovy rovnice. Přímým protipříkladem automatické Einsteinovy dynamiky je

\[
\rho=p=0,\quad a(t)=a_*[(t-t_0)/t_*]^{3/4},\quad t>t_0,
\qquad G_{00}=\frac{27}{16(t-t_0)^2}\ne0,
\quad p_X/\rho_X=-1/9.
\]

Řeší rovnici vložení, ale ne vakuovou Einsteinovu rovnici. Blízko Einsteinovy větve dává dominantní zachovávaná tekutina s konstantním w následující škálování v prvním řádu v C:

\[
|\rho_X|\ll\rho,\quad H>0,\quad
\rho_X\simeq C/(a^4H_{\mathrm{GR}})\propto a^{-(5-3w)/2},
\quad w_X\simeq-(1+3w)/6.
\]

| Dominantní tekutina | Škálování rezidua | Poměr tlaku a hustoty rezidua |
|---|---|---|
| Záření | a⁻² | −1/3 |
| Prach | a⁻⁵ᐟ² | −1/6 |
| Vakuová energie | a⁻⁴ | +1/3 |

Mocniny se vztahují k bezrozměrnému poměru faktorů rozpínání. Neplatí, když korekce dominuje. Výsledek neprokazuje studenou temnou hmotu, zrychlené rozpínání ani stabilitu poruch.

<!-- BILINGUAL-UNIT: c5.other -->
## Další zachované hranice výsledku

Pokud se samostatně předpokládá desetirozměrná Einsteinova dynamika pro plochý nezkroucený součin s vnějším a vnitřním faktorem rozpínání, přímý tenzorový výpočet dává

\[
ds_{10}^2=-dt^2+a^2d\mathbf x_3^2+b^2d\mathbf y_6^2,
\quad H=\dot a/a,\quad S=\dot b/b,
\quad G_{00}=3H^2+18HS+15S^2.
\]
\[
G_{ii}/a^2=-2\dot H-3H^2-6\dot S-21S^2-12HS,
\quad G_{mm}/b^2=-3\dot H-6H^2-5\dot S-15S^2-15HS.
\]

Statické vnitřní rozměry vyžadují následující tlakovou podmínku, přičemž vakuové příspěvky jsou zahrnuty do celkového tenzoru energie a hybnosti:

\[
\rho-3p+2p_I=0.
\]

Vnitřní křivost, warp faktor, časová závislost a další zdroje tento omezený test mění. Nejde o odvození akce ani stabilizační mechanismus [S6].

Existuje také podmíněná překážka komplexního času. Holomorfní pokračování autonomní unitární grupy se samoadjungovaným generátorem na kladném Hilbertově prostoru spolu s obyčejnou periodicitou jednotlivého stavu v imaginárním čase s nenulovou reálnou periodou dává

\[
\Psi(s+i\psi)=e^{-isK}e^{\psi K}\Psi_0,
\quad (e^{LK}-1)\Psi_0=0,
\quad L\in\mathbb R\setminus\{0\}
\Longrightarrow \Psi_0\in\ker K.
\]

Analytické pokračování musí na daném stavu existovat. Implikace plyne ze spektrální věty pro reálné spektrum. Periodicita tepelných korelací je jinou podmínkou. Nekompaktní pokračování s opačným imaginárním znaménkem může tlumit módy kladného generátoru, ale neodvozuje minimální délku, kvantování energie ani jemnostrukturní konstantu.

<!-- BILINGUAL-UNIT: c5.continuation -->
## Pokračování a kanonická hranice

Úplný další výpočet je v [testu pomocné akce](auxiliary_action.cs.md): explicitní kandidát s rozděleným jetem na oblasti s nenulovou normou pole realizuje libovolné korámce, ale rodina kinetiky kontrahované vlastní metrikou vynucuje kritický nulový objemový koeficient a nemá na tomto pozadí derivační člen v kvadratické objemové akci.

To omezuje pouze daného kandidáta. Finalizovaná mikroskopická akce, kompozitní konexe závislá na derivacích, její úplný Hessián a fyzikální kvocient vazeb zůstávají otevřené. Registr akce [U3] má nadále přednost před staršími silnými tvrzeními. Nezapisujeme zde nepodmíněnou obecnou relativitu, ekvivalenci se strunami, předpověď alfa ani úplnou kvantovou teorii. Existující kanonické statusy zůstávají beze změny; lokální strojově čitelný registr zaznamenává tento rozsah.

[Pokračování o vlnové dynamice](wave_dynamics.cs.md) nyní testuje rodinu složených jetů závislých na derivacích a příčné komplexní fluktuace existujícího plochého symplektického kandidáta. Obě zůstávají za uvedených předpokladů lokálně degenerované. Zápis také odděluje podmíněný hyperbolický disperzní vztah od nevyřešeného odvození tohoto fyzikálního operátoru a zkoumá problém signatury s dodatečnými časovými směry.

[Výpočet vln se zakřivením](curvature_waves.cs.md) rozšiřuje symplektickou překážku na určenou zakřivenou izotropní rodinu a poté odvozuje kladný tenzorový hessián existujícího split-jet kandidáta se zakřivením. Tento podmíněný gravitační sektor má dvě polarizace se světelným kuželem a kosmologické zeslabování. Explicitní zdvih s konstantním Theta ukazuje, že vlny sídlí ve složené jetové a konexní geometrii; mikroskopický propagátor samotného Theta a spektrum nezávislého tau zůstávají otevřené.

<!-- BILINGUAL-UNIT: c5.verification -->
## Ověření

`verify_c5.py` kontroluje 51 exaktních identit. `verify_c5_dynamics.py` kontroluje 32 exaktních identit včetně úplných tenzorových komponent, Piolova rušení a prvního integrálu FLRW. `verify_auxiliary_action.py` kontroluje 22 identit pomocí SymPy a nezávislé implementace Python Fraction. `verify_wave_dynamics.py` přidává 21 kontrol pomocí stejných dvou tříd nástrojů se samostatnými implementacemi. `verify_curvature_waves.py` přidává 33 kontrol včetně přímého ADM rozvoje a přesných tenzorových módů. Každý skript zapíše svůj pojmenovaný výsledný JSON vedle sebe. Verze a omezení jsou zaznamenány v těchto výstupech a `status.json`; testy spouštějí stejná odvození na dočasných kopiích, aby nepřepisovaly sledované záznamy.

**LEAN-PENDING:** v běhovém prostředí nebyly dostupné spustitelné programy Lean a Lake; obecná tvrzení o hodnosti, spektru a diferenciální geometrii zde nebyla formalizována. Identity doprovázejí analytické důkazy; konečné symbolické či racionální kontroly neprokazují úplnou fyziku, stabilitu, empirickou shodu ani lidskou revizi. Dřívější výsledky o gradientech a pomocném jetu jsou výslovně připsány svým zdrojům [U1, U2, U4]. Zdrojem překladu této repozitářové edice byla angličtina. Strukturální shoda je kontrolována strojově; před sloučením zůstává nutná lidská kontrola významové shody.

<!-- BILINGUAL-UNIT: c5.sources -->
## Zdroje

- [U1] [Existující výsledek o gradientní plochosti a objemu](../../canonical/gr_closure/gap_10t_composite_flat_admissibility.tex).
- [U2] [Variační převod Palatiniho akce pomocným jetem](../action_selection/split_jet_palatii_variational_lift.cs.md).
- [U3] [Registr jediné akce](../../canonical/ACTION.cs.md).
- [U4] [Existující úplná variace pevné konexe a konexe závislé na hodnotách](../action_selection/biquaternionic_induced_gravity_boundary.cs.md).
- [S1] David Tong, [String Theory](https://www.damtp.cam.ac.uk/user/tong/string/string.pdf).
- [S2] Antoine Van Proeyen, [Tools for supersymmetry](https://arxiv.org/abs/hep-th/9910030).
- [S3] Sheykin a Paston, [Friedmann cosmology in Regge–Teitelboim gravity](https://arxiv.org/abs/1511.09268).
- [S4] Paston a Sheykin, [Embedding theory as new geometrical mimetic gravity](https://doi.org/10.1140/epjc/s10052-018-6474-9).
- [S5] Paston a Sheykin, [From the Embedding Theory to General Relativity in a result of inflation](https://arxiv.org/abs/1106.5212).
- [S6] Das, Haque a Underwood, [Constraints and Horizons for de Sitter with Extra Dimensions](https://arxiv.org/abs/1905.05864).
