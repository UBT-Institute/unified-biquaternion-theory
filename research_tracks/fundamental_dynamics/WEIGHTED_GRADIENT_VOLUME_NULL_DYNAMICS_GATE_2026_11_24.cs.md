<!-- BILINGUAL-UNIT: weighted-gradient-volume-null-dynamics-2026-11-24 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact restricted four-real pure-gradient theorem and independent algebraic-contortion comparator. NOT a full UBT dynamics no-go.
UBT-AI-PROVENANCE-END
-->
# Silnější výsledek inverzní dynamiky: libovolně vážený gradientový objem je nulový lagrangián

**24. listopadu 2026 — přesná podmíněná věta L0 ve čtyřreálné gradientové Lorentzově větvi; mikroskopická dynamika UBT OPEN.**

\[
e^a{}_\mu=\partial_\mu Y^a,\qquad
g_{\mu\nu}=\eta_{ab}e^a{}_\mu e^b{}_\nu,\qquad
J^a{}_\mu=\partial_\mu Y^a,\qquad \det J>0.\tag{1}
\]
\[
S_f[Y]=\int d^4x\,f(Y)\det J,\qquad
C_a{}^\mu=\frac{\partial\det J}{\partial J^a{}_\mu}.\tag{2}
\]
\[
\boxed{\partial_\mu C_a{}^\mu=0,\qquad
C_a{}^\mu\,\partial_\mu Y^b=\delta_a{}^b\det J.}\tag{3}
\]
\[
\boxed{\frac{\delta S_f}{\delta Y^a}
=\partial_a f(Y)\det J-\partial_\mu[f(Y)C_a{}^\mu]=0.}\tag{4}
\]
\[
F(Y)=\int_0^{Y^0}f(s,Y^1,Y^2,Y^3)\,ds,\qquad
\boxed{f(Y)dY^0\wedge dY^1\wedge dY^2\wedge dY^3
=d\left(F(Y)dY^1\wedge dY^2\wedge dY^3\right).}\tag{5}
\]
\[
\boxed{W_{ab}=\frac{\partial^2[f(Y)\det J]}{\partial\dot Y^a\partial\dot Y^b}=0.}\tag{6}
\]
\[
L_K=J_a(Y)K^a+\frac12 K^a M_{ab}(Y)K^b,\quad
K_*=-M^{-1}J,\quad
L_{K,\mathrm{red}}=-\frac12 J^TM^{-1}J.\tag{7}
\]
\[
L_K^{\mathrm{velocity\ toy}}=\alpha \dot q\,K+\frac m2K^2
\quad\Longrightarrow\quad
L_{\mathrm{red}}=-\frac{\alpha^2}{2m}\dot q^2,\qquad
\boxed{W=-\frac{\alpha^2}{m}.}\tag{8}
\]

## Předpoklady a přesný rozsah

Zachováváme axiom A (jediná \(\Theta\in M_2(\mathbb C)\)) a uzamčenou central-sharp metriku. Omezujeme se na **čtyřreálný**, netorzněný sektor s nulovou jetovou konexí a regulární tetrádou, kde je reálná Lorentzova kofráma po konstantní normalizaci **přesným Jacobiánem** (1). Oblast má pevnou orientaci se znaménkem \(\det J\); pro záporné znaménko se započítá odpovídající konstantní orientační faktor objemu. Čtyři \(Y^a\) jsou omezené složky téže \(\Theta\), **nikoli čtyři nová fundamentální pole**. Nezavádíme nezávislou metriku, konexi ani další strukturu pozorovatele.

Již známá identita sharp-pairingu ztotožňuje zřejmou kanonickou kvadratickou kontrakci s \(2\mathcal N_0\sqrt{|g|}\), tedy konstantním násobkem indukovaného objemu. Prověřujeme silnější otázku: lze získat *jakoukoli* dynamiku prostým vynásobením této hustoty hladkým bezderivačním skalárem **přesně těchto čtyř \(Y^a\)**, \(f(Y)\)? Rovnice (2)-(6) dávají pro celou hladkou rodinu zápornou odpověď, nezávisle na znaménku nebo tvaru \(f\).

## Přesná věta o Eulerových–Lagrangeových rovnicích a Hessianu

Pro \(J^a{}_\mu=\partial_\mu Y^a\) platí kofaktorové identity (3): první je Piolova identita, druhá plyne ze vzorce pro adjungovanou matici. Eulerova derivace akce \(S_f\) je proto díky řetězovému pravidlu identicky nulová, jak ukazuje (4). Geometrický důkaz (5) je ještě silnější: \(f(Y)d^4Y\) je na čtyřrozměrném cílovém prostoru exaktní diferenciální forma nejvyššího stupně. Pullback pomocí \(Y(x)\) komutuje s vnější derivací, takže při kompaktně podporovaných variacích je akce pouze okrajová.

Protože \(\det J\) je **afinní** ve svém časovém sloupci \(J^a{}_0=\dot Y^a\), zatímco \(f(Y)\) nezávisí na rychlostech, je čtyřikrát čtyři rychlostní Hessian (6) **identicky nulový**. Momenta jsou vázaná; v tomto sektoru nejsou lokální objemové Eulerovy rovnice a nešíří se gravitační mód. Čistě gradientová metrika (1) je při invertibilním \(J\) lokálně plochá, takže její Levi-Civitova skalární křivost mizí; samostatně přidaný Einsteinův–Hilbertův člen vyhodnocený na *tomto konkrétním* gradientovém uspořádání chybějící lokální módy neopraví.

**Zásadní omezení:** Tento výsledek nelze bez důkazu přenášet na obecnou osmireálnou \(\Theta\) s nenulovou dvoustrannou kompozitní konexí \(A[\Theta],B[\Theta]\), dalšími derivacemi podle \(\psi\), neexaktní kofrámou, torzí ani skutečně odvozenou kvantovou nelokální efektivní akcí. Pokud \(f\) závisí také na dalších nezávislých složkách, jejich derivacích, externím \(x\), křivosti či torzi, nejde o větu pro \(f(Y)\). Nulový Hessian této omezené parametrizace není tvrzení o úplném fyzikálním Hessianu po vazbové redukci.

## Pouhý algebraický zdroj torze není automatickou záchranou

Uvažujme jen komparátor s algebraickou invertibilní maticí \(M(Y)\) a zdrojem \(J(Y)\), obojí bez závislosti na rychlostech, podle (7). Stacionární eliminace dává potenciál \(L_{K,\mathrm{red}}\), ale **nevytvoří kinetický Hessian**. Samostatný jednosložkový model s derivačním zdrojem (8) ukazuje přesnou možnost úniku: *zvolený* člen \(\alpha\dot q K\) po eliminaci \(K\) vytvoří kinetickou energii, jejíž znaménko určuje *dosud nevybraný* koeficient \(m\). Kompozitní zákon torze závislý na rychlostech tedy může dynamiku vytvořit, ale kompatibilita s metrikou sama neurčuje stabilitu ani znaménko.

Tento algebraický model nepopisuje všech 24 reálných složek torze ani úplnou fyzikální konexi UBT; jejich implicitní derivační operátor a zdroj musíme spočítat zvlášť. Libovolná eliminace nezávisle variovaného \(K\) není totéž jako odvození kanonicky jednoznačného \(K[\Theta]\).

## Konkrétní rozhodnutí pro UBT

**Vyřadit** celou třídu \(f(Y)\sqrt{|g[Y]|}\) jako dynamickou akci v čistě gradientové čtyřreálné větvi. NEPŘIDÁVAT libovolný skalární prefaktor ani hmotový/potenciálový člen s tvrzením, že tím vznikla šířící se metrika. Nejmenším zbývajícím fyzikálním úkolem je ze symetrií a invariantů jediné uzamčené \(\Theta\) odvodit skutečně vybraný, rychlostně citlivý zákon konexe/torze nebo jiný nelineární/kvantový člen, **který nelze převést na indukovanou objemovou formu**. Potom určit úplný redukovaný osmireálný Eulerův operátor, on-shell vakuum, fyzikální Hessian, kalibrační vazby, znaménka ghostů a TT spektrální pól. Jde o **výzkumnou překážku**, nikoli úplný zákaz UBT ani hotovou stabilní fundamentální dynamiku.

Návaznost: research_tracks/T1_GR/gr_locked_kinetic_volume_2026_11_16.en.md; research_tracks/action_selection/sharp_kinetic_volume_collapse.en.md; research_tracks/action_selection/implicit_composite_legendre_gate.en.md; draft PR #909.

**Ověření:** tools/verify_theta_weighted_gradient_volume_null_lagrangian_2026_11_24.py a příslušný pytest adaptér. Přesná symbolická kontrola generického Jacobiánu 4 krát 4, adjungované matice a Hessianu, netriviálního neafinního \(Y(x)\) s nekonstantním \(f(Y)\), všech čtyř Eulerových identit a kontrastního algebraického modelu torze. **LEAN-PENDING, nutná fyzikální revize; akce není vybrána, nemergovat jako dokončenou dynamiku UBT.**

