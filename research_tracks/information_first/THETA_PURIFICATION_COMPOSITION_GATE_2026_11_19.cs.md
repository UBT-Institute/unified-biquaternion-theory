<!-- BILINGUAL-UNIT: theta-purification-composition-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Purification and operator-composition mathematics only; the physical tensor split, on-shell quantization, Born instrument and gravity constraints remain OPEN.
UBT-AI-PROVENANCE-END
-->
# Jediné úplné Θ, purifikovaná hustota pozorovatele a chybějící fyzikální zákon tenzorového součinu

<!-- UNIT: scope -->
## Cíl: odvodit stopu bez zavádění druhého pole

Jděme za předchozí podmíněný důkaz jednoznačnosti: ukažme explicitně, jak jediné původní úplné Θ poskytuje matematickou amplitudu se dvěma indexy, jak zapomenutí jednoho indexu vede ke kandidátní matici hustoty a jakou další přesnou fyzikální strukturu to stále předpokládá. Jde o maticovou identitu a komparátor kvantového měřicího instrumentu, nikoli o dokončený výsledek kvantové dynamiky UBT.

<!-- UNIT: purification -->
## Jediný bikvaternion jako podmíněný purifikovaný stav pozorovatele

Pro již DEKLAROVANOU kandidátní pozorovatelskou referenci \(N=N^\dagger>0\) definujme \(T_N=N^{-1/2}\Theta N^{-1/2}\in M_2(\mathbb C)\) a její čtyřsložkovou **vektorizaci**
\[
\boxed{|T_N\rangle\rangle=\sum_{i,j=0}^{1}(T_N)_{ij}|i\rangle_A|j\rangle_B
\quad\in\mathbb C^2\otimes\mathbb C^2.}\tag{A}
\]
Oba štítky \(A,B\) jsou zatím matematickými maticovými indexy, **NIKOLI** prokázanými oddělenými částicemi, detektory, kauzálně nezávislými oblastmi nebo novým fundamentálním polem. Kladná Hilbertova norma vyžaduje **hermitovskou involuci zvolenou pozorovatelem** \(\dagger\), **NIKOLI** kanonickou komplexně bilineární gravitační sharp-operaci.

Pro \(T_N\ne0\) normalizujme \(|\Phi_N\rangle=|T_N\rangle\rangle/\sqrt{\langle\langle T_N|T_N\rangle\rangle}\); potom
\[
\langle\langle T_N|T_N\rangle\rangle=\operatorname{tr}(T_N^\dagger T_N),
\]
\[
\boxed{
\operatorname{Tr}_B(|\Phi_N\rangle\langle\Phi_N|)
=\frac{T_NT_N^\dagger}{\operatorname{tr}(T_NT_N^\dagger)}
=\rho_N.}\tag{B}
\]
Důkaz po maticových prvcích: \((\operatorname{Tr}_B|\Phi\rangle\langle\Phi|)_{ik}=\sum_j (T_N)_{ij}\overline{(T_N)_{kj}}/\operatorname{tr}(T_N^\dagger T_N)\). Jde o JEDNOZNAČNOU konečně rozměrnou algebraickou identitu pro **ZVOLENOU** faktorizaci. Zatím to není ontologické tvrzení, že UBT obsahuje druhý fyzikální podsystém \(B\).

Stopa se tak stává parciální stopou jedné amplitudy přes **předpokládaný nerozlišený index**, nikoli volným trikem s číselnou normalizací. Skutečně neurčenými fyzikálními předpoklady zůstávají interpretace indexu, kladnost a Hilbertův tenzorový součin.

<!-- UNIT: filter -->
## Kvadratické podíly filtrační odezvy: kde se Bornovo pravidlo předpokládá

Pro hypotetický kladný detektorový efekt \(0\le M\le I_2\) působící na index \(A\) a lineární filtr \(K\) splňující \(K^\dagger K=M\) je **podmíněný relativní podíl přenesené kvadratické odezvy**
\[
\boxed{
p(M|T_N)=\frac{\|(K\otimes I_2)|T_N\rangle\rangle\|^2}
{\||T_N\rangle\rangle\|^2}
=\frac{\operatorname{tr}(T_N^\dagger M T_N)}
{\operatorname{tr}(T_N^\dagger T_N)}
=\operatorname{tr}(\rho_NM).}\tag{C}
\]
Například vezměme \(M=\operatorname{diag}(1/4,3/4)\) a \(K=\operatorname{diag}(1/2,\sqrt3/2)\). Dva efekty \(M\) a \(I_2-M\) dávají v součtu identitu a jejich celkový přenesený podíl je \(1\). Přesný výpočet SymPy s \(T_N=\begin{psmallmatrix}1&2+i\\3-i&4\end{psmallmatrix}\) dává \(p(M)=21/32\).

Je-li výsledek **dodatečně vybrán**, normalizovaný filtrovaný stav \(A\) je obvyklé podmíněné zobrazení \(K\rho_NK^\dagger/\operatorname{tr}(M\rho_N)\). Samotná matematická identita (C) však neposkytuje fyzikální detektor ani dynamicky stochastický výsledek: předpoklad kladné Hilbertovy normy a lineárního filtru efektů už předpokládá podstatnou část struktury QM. Ze zamčené akce UBT není odvozena ani \(\sqrt M\), ani pravděpodobnosti výsledků v opakovaných experimentech, dekoherence ukazatele detektoru či skutečný kolaps.

<!-- UNIT: phase -->
## Lokálně skrytá fáze SU(2) a společná dvouindexová korelace

Malý přesný fázový příklad ilustruje, co jeden pozorovatel nevidí. Nechť
\[
\Theta_+=I_2,\qquad\Theta_-=i\sigma_3,\qquad N=I_2.
\]
Obě hodnoty jsou úplné invertibilní bikvaterniony a \(\Theta_-= \Theta_+ (i\sigma_3)\) s pravým faktorem v \(SU(2)\). Přesto
\[
\boxed{\rho_I[\Theta_+]=\rho_I[\Theta_-]=\tfrac12 I_2.}\tag{D}
\]
Jejich normalizované vektorizace jsou \(|\Phi_+\rangle=(|00\rangle+|11\rangle)/\sqrt2\) a \(|\Phi_-\rangle=i(|00\rangle-|11\rangle)/\sqrt2\). **Společný matematický operátor**, pokud by byl fyzikálně dostupný, rozliší relativní fázi:
\[
\boxed{
\langle\Phi_+|\sigma_1\otimes\sigma_1|\Phi_+\rangle=1,\qquad
\langle\Phi_-|\sigma_1\otimes\sigma_1|\Phi_-\rangle=-1.}\tag{E}
\]
Dosazením obou konstantních hodnot \(B\in\{\Theta_+,\Theta_-\}\) do TÉHOŽ afinního jetu jediného pole
\[
\Theta_B(t,x,y,z)=B+i(tI_2+x\sigma_1+y\sigma_2+z\sigma_3)
\]
dostaneme \(E_\mu=i\sigma_\mu\in W_L\) a uzamčenou sharp-metriku \(g=\eta\) pro **obě konfigurace**, v každém běžném bodě 4D. Zobrazená rovnost \(\rho_I\) je tvrzena v počátku souřadnic; mimo něj se mohou odečty lišit. Jde o OFF-SHELL plochou kinematiku, nikoli dvě vybraná úplná řešení UBT nebo pozorovaný Bellův experiment.

Je zásadní, že \(i\sigma_3\) je také jednou z pozorovatelsky nerozlišitelných pravých transformací, které při použití na **celý první jet** obecně nezachovají úplný Lorentzovsky reálný řez. Afinní příklad však mění pouze konstantní hodnotu \(B\) a zachovává \(E_\mu\); tyto transformace se **NESMĚJÍ** zaměňovat. Zda rozdíl v \(B\) představuje fyzikální pozorovatelnou veličinu nebo skrytý globální či kalibrační směr, vyžaduje zvolenou akci a zákon detektoru.

<!-- UNIT: lorentz -->
## Kovariance formální purifikace při současné Lorentzově změně rámce

Při již dokázané společné změně Lorentzova spinového rámce a pozorovatelské reference
\[
\Theta'=S\Theta S^\dagger,\quad N'=SNS^\dagger,\quad
U=N'^{-1/2}SN^{1/2}\in SU(2),
\]
platí \(T_{N'}'=UT_NU^\dagger\). Při konvenci vektorizace po řádcích
\[
\boxed{
|T_{N'}'\rangle\rangle=(U\otimes\overline U)|T_N\rangle\rangle,\qquad
\rho_{N'}'=U\rho_NU^\dagger.}\tag{F}
\]
To dává konzistentní KANDIDÁTNÍ transformaci pozorovatelského rámce, v níž se oba matematické faktory transformují **korelovaně**, nikoli jako dvě nezávisle odvozené fyzikální lokální kalibrační grupy. Fyzikální synchronizace více pozorovatelů a konexe potřebná pro porovnání různých bodů zůstávají neurčené. Pevná kanonická tetráda odvozená ze sharp-operace ani definice komplexního času \(\tau=t+i\psi\) se nemění.

<!-- UNIT: composites -->
## Bez operační faktorizace nevznikne druhá nezávislá lokální maticová algebra

**Nová kompoziční překážka NEZNÍ „matice \(2\times2\) nemůže popsat provázání dvou qubitů“.** Jak ukazují (A)–(E), vektorový prostor \(M_2(\mathbb C)\simeq\mathbb C^4\) LZE algebraicky faktorizovat jako \(\mathbb C^2\otimes\mathbb C^2\) pro jednotlivý *čistý* bipartitní matematický stav. Problém spočívá v tom, že **fyzikální tenzorové faktory ani lokální operátorové algebry nejsou vybrány kanonickými axiomy UBT**. Konkrétně požadujeme-li, aby dvě nezávislé úplné pozorovatelné algebry qubitů byly komutujícími unitalními podalgebrami UVNITŘ téže jediné výstupní algebry \(M_2(\mathbb C)\), je to nemožné: každé věrně vložené \(M_2(\mathbb C)\) tvoří celé \(M_2(\mathbb C)\), jehož komutantem jsou jen \(\mathbb C I_2\). Druhá nezávislá komutující kopie se tam proto nemůže vejít.

Levé a pravé násobení lze místo toho nechat působit na **vektorizované \(\mathbb C^4\)**, kde je tenzorová algebra \(M_2(\mathbb C)\otimes M_2(\mathbb C)\simeq M_4(\mathbb C)\). To je matematicky konzistentní, avšak jde o **dodatečnou operační faktorizaci**, nikoli fyzikální objev dvou qubitů z akce jediného pole. Rozdělení na řádky a sloupce závisí na rámci a referenci a úplná rodina pravých unitárních transformací není kanonickou kalibrací Lorentzovy tetrády.

Bodová amplituda jediného \(\mathbb C^4\) navíc nemůže reprezentovat libovolný čistý stav TŘÍ nezávisle adresovatelných qubitů (komplexní dimenze \(8\)); mnohočásticová fyzika potřebuje nelokální či multimódové kvantové stavy, vhodnou Fockovu/operátorovou konstrukci nebo jinou odůvodněnou emergentní kompoziční strukturu z JEDINÉHO prostorově rozprostřeného pole \(\Theta\). To **NEVYŽADUJE** další fundamentální klasická pole, **VYŽADUJE** však zvolenou mikroskopickou symplektickou formu, kvantování, lokalitu a kauzální komutativitu.

Konečně samotné deterministické klasické zobrazení \(\Theta\mapsto\rho_N\) nemůže vybrat skutečně náhodný jediný výsledek detektoru. Dynamický měřicí instrument (nebo odůvodněné vysvětlení skrytými proměnnými či větvením) a jeho počet pravděpodobností jsou samostatnými chybějícími částmi.

<!-- UNIT: norm-gauge -->
## Bikvaternionová sharp-norma, concurrence a věta o nepozorovatelnosti pravé kalibrace

Existuje užitečný přesný most k PŮVODNÍ bikvaternionové sharp-normě a silnější překážka fyzikální pozorovatelnosti.

Pro ZVOLENOU Hilbertovu faktorizaci \(2\otimes2\) normalizovaného \(|T_N\rangle\rangle\) je **concurrence** čistého bipartitního stavu standardní algebraickou veličinou
\[
\boxed{
\mathcal C_N=\frac{2|\det T_N|}{\operatorname{tr}(T_NT_N^\dagger)}
=\frac{2|\det\Theta|}{\operatorname{tr}(T_NT_N^\dagger)}
\quad(\det N=1).}\tag{G}
\]
Druhá rovnost plyne z \(T_N=N^{-1/2}\Theta N^{-1/2}\), zatímco identita pro kvaternionově sdružený objekt \(T_N^\sharp T_N=(\det T_N)I_2\) vysvětluje přítomnost determinantu přímo v původní algebře \(\mathbb C\otimes\mathbb H\). Pro redukovanou pozorovatelskou matici hustoty platí
\[
\boxed{
\operatorname{tr}(\rho_N^2)=1-\frac{\mathcal C_N^2}{2},
\qquad 0\le\mathcal C_N\le1.}\tag{H}
\]
Důkaz: \(\operatorname{tr}\rho_N=1\), \(\det\rho_N=|\det T_N|^2/[\operatorname{tr}(T_NT_N^\dagger)]^2\) a pro matici \(2\times2\) se stopou jedna \(\operatorname{tr}\rho_N^2=1-2\det\rho_N\). Omezení plyne z aritmeticko-geometrického průměru čtverců singulárních hodnot \(T_N\). Čistý redukovaný stav má \(\mathcal C_N=0\) a hodnost jedna \(T_N\). Maximálně smíšený redukovaný stav má \(\mathcal C_N=1\), kde \(T_N\) je úměrné unitární matici. Kandidátní \(\mathcal C_N\) je invariantní vůči deklarované současné změně Lorentzova rámce a pozorovatele \(T_N\mapsto U T_NU^\dagger\). **NENÍ** prokázaným fyzikálně měřeným monotónem provázání UBT, protože podsystém pravého indexu není dynamicky vybrán.

**Operační věta o pravé kalibraci.** Předpokládejme jako DODATEČNOU nedokázanou hypotézu, že úplná pravá volnost \(U(2)\) jednohodinového protokolu je skutečnou fyzikální kalibrační redundancí ve vektorizované purifikaci. Pak musí být každá přípustná hermitovská **společná pozorovatelná veličina** \(\mathcal O\) invariantní vůči všem \((I_2\otimes V)\) a \(V\in U(2)\) (až na nepodstatnou volbu transpozice pravého indexu). Z komutantu fundamentální ireducibilní reprezentace \(U(2)\) plyne
\[
\boxed{
[\mathcal O,I_2\otimes V]=0\quad\forall V\in U(2)
\;\Longrightarrow\;
\mathcal O=A\otimes I_2.}\tag{I}
\]
Důkaz bez odvolání na teoreticko-reprezentační černou skříňku: zapišme \(\mathcal O\) jako čtyři bloky \(2\times2\) na pravém indexu. Komutace s \(I_2\otimes\sigma_3\) nutí každý blok být diagonální, komutace s \(I_2\otimes\sigma_1\) vynucuje rovnost jeho diagonálních prvků. Každý blok je proto násobkem \(I_2\).

Proto \(\langle\mathcal O\rangle=\operatorname{tr}(\rho_N A)\) závisí POUZE na jednohodinové matici hustoty. Žádná **fyzikální kalibračně invariantní** pozorovatelná veličina pak nemůže rozlišit dřívější \(\Theta_+=I_2\) a \(\Theta_-=i\sigma_3\), přestože jejich matematická korelace \(\sigma_1\otimes\sigma_1\) je rozdílná. Ve skutečnosti
\[
(I_2\otimes i\sigma_3)^\dagger
(\sigma_1\otimes\sigma_1)
(I_2\otimes i\sigma_3)
=-(\sigma_1\otimes\sigma_1),\tag{J}
\]
takže tento komparátor konkrétně **NENÍ** invariantní vůči navržené pravé kalibraci. Jde o přesnou **alternativu buď/anebo**: pokud je celá pravá grupa skutečnou kalibrací, jsou skryté fázové rozdíly v jednohodinové teorii nepozorovatelné; pokud je odhaluje nezávisle kalibrovaná reference pravé fáze, pravá akce **NESMÍ** být považována za tuto neomezenou fyzikální kalibraci (nebo se musí reference transformovat jako součást plně kalibračně invariantního relačního měření). Dřívější kanonická překážka pravé akce \(W_L\) před takovým povýšením nezávisle varuje.

Sharp-norma spojuje algebraickou \(\Theta\) s matematickým zástupným ukazatelem provázání, ale **NEVYBÍRÁ** Bornovy výsledky, fyzikální druhý podsystém ani nový Hamiltonián.

<!-- UNIT: next -->
## Mikroskopická dynamika potřebná pro skutečnou kvantovou kompozici

**Konkrétní další odvození.** Určit přípustnou mikroskopickou akci úplného \(\Theta\), identifikovat její redukovaný fyzikální fázový prostor a symplektickou dvouformu a odvodit fundamentální kladnou pozorovatelskou reprezentaci. Potom otestovat, zda lze vytvořit dvě **prostorupodobně oddělené rozmazané algebry pozorovatelných veličin** s fyzikálně odůvodněnou komutací a faktorizací, nikoli pouhým libovolným označením dvou maticových indexů za částice. Teprve poté odvodit filtrační efekt detektoru, četnosti, projekci/aktualizaci a Bornovy váhy bez jejich předpokládání. Analyzovat tytéž kanonické Lorentzovsky reálné vazby \(D_\mu\Theta\), případnou torzi, kladnost ghostů/energie a stabilitu sektoru \(\psi\).

Tento text **NENÍ** proklamovaným novým důkazem standardní purifikace ani Bellových korelací. Jde o vymezený výsledek zpětného odvozování a konkrétní test **chybějící fyziky** v UBT.

Dříve mergnuté zdroje: canonical/AXIOMS.md, research_tracks/information_first/THETA_DENSITY_REVERSE_PRINCIPLE_2026_11_19.en.md, research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md. Předchozí rozpracovaná verze: research_tracks/information_first/THETA_OPERATIONAL_ADDITIVITY_LORENTZ_GAUGE_GATE_2026_11_19.en.md. Ověřovač: tools/verify_theta_purification_composition_gate_2026_11_19.py.