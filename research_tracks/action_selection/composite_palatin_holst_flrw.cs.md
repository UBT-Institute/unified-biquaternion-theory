<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: composite-palatin-holst-homogeneous.provenance -->
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

# Kompozitní Palatiniho–Holstova akce: přesná homogenní variace spinového spojení

**Stav: CONDITIONAL EXACT MINISUPERSPACE RESULT / FULL UBT DYNAMICS OPEN.** Pokračuje za algebraické vyloučení pomocné axiální torze v draft PR #692. Einsteinova–Cartanova křivostní čtyřforma a nezávislý paritně lichý Holstův koeficient jsou **předpokládané srovnávací operátory**, nikoli odvození z jediné dosud nedokončené fundamentální akce Theta. Kompozitní vazbu ukládáme **před homogenní variací**, ale úplné obecné rovnice pole dosud neověřujeme.

## Volné homogenní spinové spojení, jediné Theta a topologie

Na kladném časovém intervalu uvažujeme levý ikosahedrální kvocient jednotkové grupové sféry. Homogenní boost B i prostorovou rotaci C ponecháme nezávislými redukovanými proměnnými až do Eulerovy variace. Zvolíme

\[
\Theta=iq V(t)I,\qquad
\Omega=\tfrac12\big(B(t)+iC(t)\big)\sigma_j\upsilon^j,\quad
e^0=dV,\quad e^j=V B\,\upsilon^j=:a\,\upsilon^j,\quad
N=\dot V>0,\quad B=a/V.
\]

Levě invariantní prostorová triáda a Lorentzův spinový zdvih splňují

\[
d\upsilon^i=-\epsilon^i{}_{jk}\upsilon^j\wedge\upsilon^k,\qquad
\omega^0{}_i=\omega^i{}_0=B\upsilon^i,\quad
\omega^i{}_j=C\epsilon^i{}_{jk}\upsilon^k,\quad
V_\Sigma=\pi^2/60.
\]

Oddělená prostorová rotace C je zásadní. Dosazení její Leviho–Civitovy hodnoty před variací by skrylo paritně lichou rovnici prvního řádu. Všechny formy sestupují při levé akci grupy.

## Nezávislý výpočet křivosti a torze

Přímý výpočet Maurerových–Cartanových vnějších forem (cyklické indexy) dává

\[
R^0{}_i=
\dot B\,dt\wedge\upsilon^i-
B(C+1)\epsilon^i{}_{jk}\upsilon^j\wedge\upsilon^k,\quad
R^1{}_2=\dot C\,dt\wedge\upsilon^3+
(B^2-C^2-2C)\upsilon^1\wedge\upsilon^2 .
\]

Cartanova torze je

\[
T^0=0,\quad
T^i=(\dot a-NB)\,dt\wedge\upsilon^i
-a(C+1)\epsilon^i{}_{jk}\upsilon^j\wedge\upsilon^k.
\]

Dvě normalizované invariantní čtyřformy jsou přesně

\[
\frac1{12}\epsilon_{abcd}e^a\wedge e^b\wedge R^{cd}
=a\big[N(B^2-C^2-2C)+a\dot B\big]\,
dt\wedge\upsilon^1\wedge\upsilon^2\wedge\upsilon^3.
\]

\[
\frac13\sum_{a<b}e_a\wedge e_b\wedge R^{ab}
=a\big[2NB(C+1)+a\dot C\big]\,
dt\wedge\upsilon^1\wedge\upsilon^2\wedge\upsilon^3.
\]

První je paritně sudá Palatiniho kontrakce tetrádových bivektorů a křivosti, druhá paritně lichá Holstova kontrakce. Tyto formule přesně určují zvolenou normalizaci a orientaci. Žádný jedinečný Holstův koeficient z bikvaternionové algebry neodvozujeme.

## Akce kompozitních hodin a přesná redukovaná variace

Po integraci přes prostor volíme normalizovanou externí srovnávací akci

\[
L_\alpha=\mathscr C\left[
a\big(N(B^2-C^2-2C)+a\dot B\big)
+\alpha a\big(2NB(C+1)+a\dot C\big)
-\frac{\Lambda}{3}Na^3
\right],\qquad
\mathscr C=\frac{3V_\Sigma}{8\pi G}.
\]

Kompozitní vazba Theta určuje spinový boost pomocí a a V, ale **neurčuje** C. Po dosazení této vazby a odstranění úplných derivací dostáváme

\[
\boxed{
L_\alpha\simeq\mathscr C\left\{
N\left[a+\frac{a^3}{3V^2}-\frac{\Lambda a^3}{3}
-a w^2+\frac{2\alpha a^2w}{V}\right]
-2\alpha a\dot a\,w
\right\},\quad w=C+1.
}
\]

Rovnost je zde platná až na okrajový člen; tento postup nemění objemové Eulerovy rovnice s kompaktním nosičem variací. Teprve nyní variujeme C neboli w:

\[
\frac{\delta L_\alpha}{\delta w}=0
\quad\Longrightarrow\quad
\boxed{w=\alpha\left(\frac aV-\frac{\dot a}{N}\right).}
\]

Po dosazení algebraické rovnice rotace zpět do stejné redukované akce vychází

\[
\boxed{
L_{\alpha,\mathrm{red}}\simeq\mathscr C\,N\left[
a+\frac{a^3}{3V^2}-\frac{\Lambda a^3}{3}
+\alpha^2 a\left(\frac aV-\frac{\dot a}{N}\right)^2
\right].
}
\]

**Nové strukturální zjištění:** Holstův operátor obecně generuje nenulovou prostorovou torzi w a kvadratický rychlostní člen měřítka. Při nulové paritní vazbě je w=0, zůstává však časová stopová torze. Nejde o vynucení nulové veškeré Cartanovy torze.

## Rozhodující výsledek holého Palatiniho členu a srovnání s vakuovými Einsteinovými rovnicemi

Pro externí Palatiniho komparátor s nulovou Holstovou i kosmologickou vazbou má Eulerova derivace měřítka přesný tvar

\[
\alpha=0,\quad\Lambda=0
\quad\Longrightarrow\quad
\frac1{\mathscr C}\frac{\delta L_{\mathrm{red}}}{\delta a}
=N\left(1+\frac{a^2}{V^2}\right)>0
\quad (N,a,V>0).
\]

V této omezené větvi tedy neexistuje žádná hladká regulární homogenní stacionární trajektorie s kladnými hodinami a měřítkem. Výrok se vztahuje pouze na uvedenou kompozici a symetricky redukovanou rodinu, ne na všechny Lorentzovy rámce, struktury torze nebo akce úplné UBT.

Pokud předpokládáme **externí** kladnou kosmologickou konstantu, ale nulový Holst, redukovaná rovnice dovoluje stacionární algebraickou větev

\[
\alpha=0,\quad\Lambda>0,\quad\Lambda V^2>1
\quad\Longrightarrow\quad
a(V)=\frac{V}{\sqrt{\Lambda V^2-1}}.
\]

Eulerova rovnice hodin je zohledněna samostatně, nikoli vynechána. V paritně sudé větvi dává reparametrizační invariance přesnou Noetherovu identitu
\[
F(a,V)=a+\frac{a^3}{3V^2}-\frac{\Lambda a^3}{3},\quad
L_{\alpha=0}/\mathscr C=\dot V\,F(a,V),\quad
\boxed{
\mathcal E_V=\dot V\partial_VF-\frac{dF}{dt}
=-\dot a\,\partial_aF,\qquad
\mathcal E_a=\dot V\,\partial_aF.
}
\]
Každá regulární větev splňující variační rovnici měřítka tedy splňuje také rovnici hodin. Uvedená algebraická větev s kladnou kosmologickou konstantou je proto stacionární vůči **oběma** redukovaným variacím, avšak nemusí splňovat nezávislou Einsteinovu normálovou vazbu. Jde tedy o skutečný dynamický protipříklad uvnitř omezeného ansatzu, nikoli jen řešení jedné libovolně vybrané rovnice.

Reparametrizační vazba je přítomna; nejde o nezávisle uloženou vakuovou Einsteinovu normálovou vazbu. Větev s nulovým koeficientem tuto druhou vazbu obecně nesplňuje. Při konkrétní volbě jednotek dostáváme přesné reziduum

\[
\Lambda=1,\quad V=2:\qquad
\dot a^2+1-\frac{\Lambda a^2}{3}=\frac{16}{27}\ne0
\qquad (N=1).
\]

Stacionární dynamika jedněch kompozitních hodin v Palatiniho *homogenní redukci* proto není totéž jako úplné vakuové Einsteinovy rovnice. Normálová vazba se neobnovila pouhým přidáním paritně sudé křivostní čtyřformy.

Hessova matice podle radiální rychlosti v redukci je

\[
\frac{\partial^2L_{\alpha,\mathrm{red}}}{\partial\dot a^2}
=\frac{2\mathscr C\,\alpha^2 a}{N},
\qquad
\frac{\partial^2L_{0,\mathrm{red}}}{\partial\dot a^2}=0.
\]

Holstova vazba vytváří nenulovou homogenní rychlostní Hessovu matici; její znaménko samo o sobě ale NENÍ důkazem fyzikálního ghostu ani stability. Lapse zůstává N=dV/dt a není nezávisle variovatelná. [Audit uzavření](physics_closure_2026_10.cs.md) nyní počítá úplnou homogenní primární Poissonovu matici, Diracovy závorky, Hamiltonián hodin a samostatnou vrstvu vazeb s nulovým koeficientem. Úplná prostorová algebra polních vazeb a všechny poruchové módy zůstávají nespočítané.

## Přísná omezení a následující fyzikální test

Jde o křivostní **komparátor**, nikoli dokončenou fundamentální akci UBT. Symetrická redukce na homogenní SU(2) pole před variací může odstranit rovnice, zejména normálové/lapse a anizotropní vazby. Neodvozujeme řešení úplných obecných rovnic pole, dynamiku všech 24 komponent torze, pozitivní Hamiltonián, kvantitativní CMB ani automatický výběr dvanáctistěnné topologie.

Další přesný úkol je úplná kompozitní variace spinového spojení v neomezené Palatiniho čtyřformě s existujícím zdvihem bez nových polí, určení ranku normálové rovnice a kontrola, zda odvozený Holstův koeficient zlepšuje či zhoršuje fyzikální hlavní symbol. Paritně lichá interakce není automaticky slučitelná s úplnými pravidly U(1) a parity; koeficient zůstává kandidátem, dokud nebude zdůvodněn.

**Ověření:** `tools/verify_composite_palatin_holst_flrw.py`, `tests/test_composite_palatin_holst_flrw.py`, samostatné CI. Výpočty používají reálné tetrády a vnější formy; bez dat Planck nebo CMB.

<!-- BILINGUAL-UNIT: composite-palatin-holst.selfdual -->
## Ověřené samoduální přiřazení a jeho překážka reality

[Audit uzavření](physics_closure_2026_10.cs.md) ověřuje časově závislou kanonickou transformaci a její přesný tvar GR FLRW při analyticky pokračovaném koeficientu $b=\pm i$. Zachovávaným momentem hodin je transformovaný moment, nikoli obecně původní moment. Integrační konstanta s chováním prachu je přípustná, ale nemusí být nenulová a není normalizována mikroskopickým odvozením zdroje. Ponechání původní hermitovské dvojice konexí mění generovanou prostorovou tetrádu při navržené imaginární rotaci, takže formální přiřazení ještě není přípustnou kanonickou větví UBT. Před výpočtem jejích fyzikálních poruch je nutný konzistentní předpis reality odvozený z akce. Stávající reziduum vakuové vazby zůstává přesným srovnáním, nikoli dokladem chybějící reparametrizační symetrie.
