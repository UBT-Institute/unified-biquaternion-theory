<!-- BILINGUAL-UNIT: physics-closure.bare-scope -->
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

# Překážka holé akce nezávislá na rozměru

[Přehled auditu](physics_closure_2026_10.cs.md). Zdrojem překladu je anglická verze. Jde o podmíněný výsledek pro určenou rodinu klasických akcí, nikoli o zákaz všech akcí UBT nebo výběr počtu složek Theta. Autor upřesnil, že navržený počet byl předběžný. Níže uvedený prostor variací je libovolný reálný prostor; aktuálně zapsaný maticový model poskytuje pouze ilustrativní příklad.

<!-- BILINGUAL-UNIT: physics-closure.bare-assumptions -->
## Předpoklady a převzatá identita

Použijme hladkou orientovanou nedegenerovanou Lorentzovu tetrádu ve čtyřech prostoročasových rozměrech, pevné centrální metrické vyčítání a variace s kompaktním nosičem. Předpokládejme, že kinetická dvojice je přesně Gramovou dvojicí definující tutéž metriku. Existující [výsledek zjednodušení se sharp](sharp_kinetic_volume_collapse.cs.md) pak dává
\[
g^{\mu\nu}\langle D_\mu\Theta,D_\nu\Theta\rangle=4N_0,
\qquad S_{\rm bare}=\int\nu_E F(\Theta),\qquad
F=\alpha-U(\Theta),\quad\alpha=2cN_0.
\]
Zde je normalizace kinetiky $c/2$ a $U$ je potenciál bez derivací s vazbou zahrnutou do jeho definice. Jde o explicitní volbu dvojice; abstraktní dvojice v nehotovém registru akcí se tím potají nefinalizuje. Identita využívá čtyřrozměrnost prostoročasu, nikoli počet složek pole. Dodatečné kinetické kanály odlišné od metrické Gramovy dvojice tento výsledek nepokrývá.

Předpokládejme, že existující algebraické pomocné proměnné jetu lze volně variovat, mají hladkou pravou inverzi na variace tetrády v oblasti s nenulovou normou a nevstupují do další nezávislé kinetické akce ani akce křivosti. Jde o deklarované srovnání s volným jetem. [Věta o variaci rozděleného jetu](split_jet_palatii_variational_lift.cs.md) poskytuje dříve dokázaný mechanismus pravé inverze; neposkytuje akci křivosti. Nezávislé přípustné variace pole je třeba uvést samostatně. Žádná fyzikální konexe se neztotožňuje s libovolnou pomocnou maticovou konexí.

<!-- BILINGUAL-UNIT: physics-closure.bare-proof -->
## Věta o lokální stacionaritě

Úplná variace podle pravidla pro součin je
\[
\delta S_{\rm bare}=\int\nu_E\left[
F e_a{}^\mu\delta e_\mu{}^a+dF_\Theta(\delta\Theta)\right].
\]
Při pevném Theta dovoluje pravá inverze jetu $\delta e_\mu{}^a=\varepsilon e_\mu{}^a$, což dává $4\varepsilon F$. Ze stacionarity proto plyne $F=0$. Při libovolné připuštěné variaci Theta kompenzujeme odezvu tetrády touto pravou inverzí. Dostáváme $dF=0$ na připuštěném tečném prostoru pole. Obráceně $F=0$ a nulový diferenciál na celém prostoru hodnot způsobí vymizení první variace pro každou přípustnou kompozitní odezvu, včetně všech indukovaných variací metriky a konexe. Při nezávislých variacích pole je tedy lokální kritérium
\[
\boxed{F(\Theta)=0,\qquad dF_\Theta=0.}
\]
Postačující směr platí i při uzavření omezujícím variace pole, protože nulový diferenciál na okolním prostoru vymizí na každém přípustném tečném podprostoru. V přípustné kritické nule $\Theta_*$ s nenulovou normou je proto při konstantním $\Theta_*$ stacionární každá hladká lokálně reprezentovatelná tetráda. Pokud taková kritická nula neexistuje, neexistuje při uvedených nezávislých variacích regulární stacionární větev. Ani jedna možnost v této rodině nevybírá Einsteinovu dynamiku.

`formal/lean/UBT/GR/BareSplitJet.lean` dokazuje kritérium variačního kovektoru pro libovolný reálný modul, skutečnou derivaci součinu jedné proměnné, vyrušení druhé variace podle pravidla pro součin a algebraickou pravou inverzi pomocných proměnných. Tyto konečné výroky nepředpokládají osm složek. Přechod k hladkému funkcionálu s uvedenou pravou inverzí je analytický a nad rámec těchto zapsaných jader zůstává `LEAN-PENDING`. Nová věta `firstVariation_at_vacuum` v existujícím modulu potenciálu kontroluje skutečnou směrovou derivaci, nikoli pouze předpokládaný kritický bod.

<!-- BILINGUAL-UNIT: physics-closure.bare-witness -->
## Neeinsteinovský stacionární příklad

Pro ilustrativního člena aktuálně zapsané rodiny maticových potenciálů normalizujeme jednotky pole, délky a času pouze pro tento příklad; nefixujeme žádnou měřenou škálu. Položme
\[
H(X)=2\operatorname{Re}(X_{11}\overline{X_{22}})-|X_{12}|^2-|X_{21}|^2,
\quad D(X)=|\det X|^2,\quad U=\alpha+1-H+D.
\]
Pak $F=H-D-1$ splňuje $F(iI_2)=0$ a má nulový gradient ve všech osmi reálných směrech maticových prvků. Tyto koeficienty jsou přípustným příkladem, nikoli odvozenými univerzálními konstantami. Existující důkaz potenciálu poskytuje jeho úplný směrový polynom; Lean ověřuje jeho první derivaci a nezávislý CAS kontroluje každou složku gradientu. Tento příklad nefixuje fundamentální rozměr pole ani netvrdí, že každý větší prostor hodnot má stejný potenciál.

Použijme vlastní čas $T$, jednotkovou uzavřenou prostorovou kofrámu a existující reálný rozdělený jet:
\[
\Theta_*=iI_2,\quad N=1,\quad a=1+T^2,\quad
B_{\rm phys}=2T,\quad C_{\rm phys}=-1,\quad
k_J=a-B_{\rm phys},\quad w_J=dT.
\]
Fyzikální Lorentzova konexe je Levi-Civitova, protože $B_{\rm phys}=\dot a/N$ a $C_{\rm phys}=-1$ dávají nulovou fyzikální torzi. Dodatečný boost jetu $k_J$ a reálná relativní 1-forma $w_J$ nejsou fyzikální torzí ani fází. Přímé maticové vyhodnocení dává
\[
D_J\Theta_*=iI_2\,dT+i(1+T^2)\sigma_j\upsilon^j,
\qquad ds^2=-dT^2+(1+T^2)^2d\Omega_3^2.
\]
Tetráda je regulární a splňuje původní vyčítání i při konstantním Theta. Podle věty o kritické nule je tato konfigurace stacionární při každé přípustné variaci uvedené holé akce. Nezávislý souřadnicový výpočet z Christoffelových symbolů dává při $T=0$
\[
R_{00}=-6,\quad R_{\chi\chi}=4,\quad
g_{00}=-1,\quad g_{\chi\chi}=1.
\]
Einsteinova podmínka $R_{\mu\nu}=\Lambda g_{\mu\nu}$ by vyžadovala současně $\Lambda=6$ a $\Lambda=4$. Lean dokazuje tento konečný spor; CAS počítá skutečnou křivost. Jde o explicitní neeinsteinovskou stacionární metriku v deklarované rodině, nikoli o navrženou fyzikální kosmologii nebo odmítnutí všech doplnění UBT.

<!-- BILINGUAL-UNIT: physics-closure.bare-hessian -->
## Hessián a hranice konstruktivního pokračování

V kritické nule jsou všechny členy odezvy objemu v úplné druhé variaci násobeny $F$ nebo $dF$ a vymizí. Pro dvě variace platí
\[
\delta_1\delta_2 S_{\rm bare}
=\int\nu_E\,d^2F_{\Theta_*}(\delta_1\Theta,\delta_2\Theta).
\]
Redukovaná holá větev má tedy algebraický hessián pole a žádný metrický kinetický blok. Nejde o nedegenerovaný fyzikální hessián Laplaceova typu předpokládaný v podmíněném vztahu indukované gravitace. Počítání zapsaných prvků pole jako propagujících módů není odůvodněné. Kvantová míra/jakobián, kvocient podle vazeb nebo další derivativní interakce potřebují vlastní odvození; tento klasický důkaz nevylučuje kvantové doplnění.

`tools/verify_bare_splitjet_selection.py` kontroluje celý maticový gradient, smíšenou druhou variaci, odezvu pomocných proměnných, původní vyčítání tetrády a příklad křivosti. Algebraické prostory velikosti $1,3,8,13$ testují logiku nezávislou na rozměru, nikoli preferované fyzikální počty. Oddělená implementace komplexních matic v NumPy kontroluje konvergentní první variace při současných změnách pole a tetrády. Přesná zapsaná algebra a derivace jsou ověřeny v Lean; úplné funkcionální/PDE a kvantové výroky zůstávají mimo tento důkaz. Einsteinův–Hilbertův člen a jeho nenulový koeficient z této holé rodiny nebyly odvozeny. Konstruktivní pokračování musí odůvodnit jiný zákon kinetiky/konexe nebo odvodit kvantovou efektivní akci a její fyzikální míru.
