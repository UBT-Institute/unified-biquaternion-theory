<!-- BILINGUAL-UNIT: spatial-dynamics.scope -->
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

# Úplná prostorová dynamika v omezené rodině redukované metriky

**2026-10-29; C_working; CONDITIONAL.** Zdrojem překladu je angličtina. Tento výpočet vybírá Einsteinův kinetický poměr a relativní normalizaci křivosti v explicitně zadané rodině redukovaných hamiltoniánů. Zahrnuje libovolnou prostorovou závislost, lokální variace lapsu, pohybové rovnice a tenzorové módy na plochém pozadí. Nedokončuje mikroskopickou akci jediné Theta. Jde o reprodukovatelný omezený geometrodynamický výpočet, nikoli o tvrzení nové věty obecné relativity.

<!-- BILINGUAL-UNIT: spatial-dynamics.assumptions -->
## Fázový prostor, konvence a předpoklad výběru

Pracujeme na hladké orientované prostorové varietě dimenze **3**, s kladnou prostorovou metrikou a symetrickou sdruženou hybnostní hustotou váhy **1**. Používáme kompaktní řez bez hranice nebo testovací funkce a variace s kompaktním nosičem. Předpokládáme dostatečnou regularitu pro uvedené derivace a integrace po částech. Rychlost světla klademe rovnu **1** a laps normalizujeme na posunutí podél jednotkové geometrické normály. Neukládáme homogenitu ani omezení na preferované hodiny.

Prostorová metrika je prostorovým omezením stávající kanonické metriky z centrálního součinu sharp. Není novým fundamentálním polem ani náhradním předpisem čtení metriky. Zásadním podmíněným vstupem je, že po fyzikální Lorentzově/jetové redukci tvoří její fázový prostor následující kanonický kotečný prostor a připouští libovolné lokální variace metriky. Samotná stávající kinematická pravá inverze tento symplektický vstup pro úplnou UBT nedokazuje.

\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\qquad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf1,
\qquad h_{ij}=g_{ij},\quad h=\det(h_{ij})>0.
\]
\[
\{h_{ij}(x),\pi^{kl}(y)\}=\delta^k_{(i}\delta^l_{j)}\delta(x-y),
\quad \pi=h_{ij}\pi^{ij},\quad Q=\pi^{ij}\pi_{ij},
\quad \mathcal H=\frac{a}{\sqrt h}(Q-\chi\pi^2)-b\sqrt h\,{}^{(3)}R+c_0\sqrt h.
\]
\[
H[N]=\int N\mathcal H,\qquad
D[\xi]=\int\pi^{ij}\mathcal L_\xi h_{ij}
=-2\int\xi^i h_{ij}\nabla_k\pi^{jk}.
\]

Konstanty jsou reálné, prostorově nezávislé srovnávací koeficienty. Ansatz je ultralokální a kvadratický v hybnosti; potenciál obsahuje pouze skalární křivost a konstantu. Derivace hybnosti, vyšší křivost, hmota, fyzikální torze, další pole a nekanonické Diracovy závorky leží mimo tuto rodinu. Požadavek normalizované Lorentzovské algebry deformací nadploch **mimo řešení** je dodatečný předpoklad výběru. Nebyl odvozen z uzamčené kinematiky Theta ani z informačních principů. Současné přeškálování hamiltoniánu a lapsu mění normalizační konvenci; zde je geometrická normalizace lapsu pevná.

<!-- BILINGUAL-UNIT: spatial-dynamics.bracket -->
## Funkcionální závorka před jakýmkoli prostorovým omezením

Derivace podle hybnosti a část variace křivosti obsahující derivace lapsu jsou

\[
\frac{\delta H[N]}{\delta\pi^{ij}}
=\frac{2aN}{\sqrt h}(\pi_{ij}-\chi\pi h_{ij}),\qquad
\frac{\delta(-b\int N\sqrt h R)}{\delta h_{ij}}
=-b\sqrt h\left[N(\tfrac12h^{ij}R-R^{ij})+\nabla^i\nabla^jN-h^{ij}\Delta N\right].
\]

Křivost bez dalšího označení i kovariantní derivace jsou zde prostorové. Všechny algebraické členy se při záměně dvou funkcí lapsu vyruší. Závorka kinetické části se sebou se ruší bodově a závorka potenciálu se sebou je nulová. Kontrakce zbývajících symetrických tenzorů dává

\[
(\pi_{ij}-\chi\pi h_{ij})(\nabla^i\nabla^jM-h^{ij}\Delta M)
=\pi^{ij}\nabla_i\nabla_jM-(1-2\chi)\pi\Delta M.
\]

Jednou integrujeme po částech. Součiny prvních derivací lapsu se vyruší díky symetrii hybnostního tenzoru. Přesný výsledek je

\[
\beta^i=h^{ij}(N\partial_jM-M\partial_jN),\qquad
\nabla_i\pi=\sqrt h\,\partial_i(\pi/\sqrt h),
\]
\[
\boxed{\{H[N],H[M]\}=ab\,D[\beta]
+2ab(1-2\chi)\int\beta^i\nabla_i\pi.}
\]

Divergence a gradient stopy jsou mimo řešení nezávislé. U lokálně ploché metriky má hybnost, jejíž jediná nenulová příčná diagonální složka závisí na první souřadnici, nulovou divergenci, ale nekonstantní stopu. Naopak opačné první a druhé diagonální složky závislé na první souřadnici dávají nulovou stopu a nenulovou divergenci. Lokální jety lapsu mohou otestovat každý koeficient. Rovnost s požadovaným generátorem hybnosti pro libovolná data proto platí právě tehdy, když

\[
\boxed{ab=1,\qquad\chi=\tfrac12.}
\qquad
\{D[\xi],H[N]\}=H[\mathcal L_\xi N],\qquad
\{D[\xi],D[\zeta]\}=D[[\xi,\zeta]].
\]

Poslední dvě identity plynou z kanonického zobrazení momentu pro prostorové difeomorfismy a z váhy skalární hustoty hamiltoniánu. Společně dávají úplnou prostorovou algebru vazeb první třídy této vybrané rodiny metrik. Nevypočítávají neredukovanou algebru vazeb rozštěpeného jetu, komplexní Theta ani hmoty.

Periodický přesný příklad zviditelňuje překážku ve stopě bez hraničního členu:

\[
h_{ij}=\delta_{ij},\quad \pi^{ij}=\operatorname{diag}(0,\sin x,0),\quad
N=1,\quad M=\sin x,\quad x,y,z\in[0,2\pi],
\]
\[
D[\beta]=0,\qquad
\int\beta^i\nabla_i\pi=(2\pi)^2\int_0^{2\pi}\cos^2x\,dx=4\pi^3.
\]

Tento příklad testuje identitu mimo řešení; netvrdíme, že splňuje hamiltonovskou vazbu. Homogenní zkrácení tento člen skryje. Nulové závorky pouze na omezené vazbové ploše nedokazují požadované strukturní funkce mimo řešení. Alternativní větve s vazbami druhé třídy nebo s preferovanou foliací nejsou vyloučeny: rozlišení je explicitní u [Bellorína–Restuccii, rovnice 8–18](https://arxiv.org/pdf/1004.0055). Širší kanonický program je spojen s prací [Hojmana–Kuchaře–Teitelboima](https://doi.org/10.1016/0003-4916(76)90112-3); zde se nečiní nárok na prioritu.

<!-- BILINGUAL-UNIT: spatial-dynamics.evolution -->
## Vybraná evoluce a zbývající volné konstanty

Dosadíme vybraný poměr do téhož hamiltoniánu. Úplná vakuová evoluce metriky před omezením prostorovou symetrií je

\[
\dot h_{ij}=\frac{2aN}{\sqrt h}(\pi_{ij}-\tfrac12\pi h_{ij})+\mathcal L_\xi h_{ij},
\]
\[
\dot\pi^{ij}=-\frac{aN}{\sqrt h}
\left[2\pi^{ik}\pi_k{}^j-\pi\pi^{ij}-\tfrac12h^{ij}(Q-\tfrac12\pi^2)\right]
+b\sqrt h\left[N(\tfrac12h^{ij}R-R^{ij})+\nabla^i\nabla^jN-h^{ij}\Delta N\right]
-\tfrac12c_0N\sqrt h\,h^{ij}+\mathcal L_\xi\pi^{ij},
\qquad\mathcal H=0,\quad\mathcal H_i=-2h_{ij}\nabla_k\pi^{jk}=0.
\]

Lieova derivace hybnosti je derivací kontravariantní hustoty váhy **1**. Laps a posun jsou nezávislé lokální multiplikátory. Pokud je zahrneme jako kanonické souřadnice, jejich hybnosti jsou nulové a jejich zachování dává čtyři uvedené sekundární vazby. Ze zachování této uzavřené metrické algebry nevzniká další lokální vazba.

Pro nenulový kinetický koeficient je Legendreovo zobrazení invertibilní na šesti prostorových rychlostech metriky. S obvyklým hraničním předpisem dává

\[
K_{ij}=\frac{\dot h_{ij}-\mathcal L_\xi h_{ij}}{2N},\qquad
\pi^{ij}=\frac{\sqrt h}{a}(K^{ij}-Kh^{ij}),\qquad b=\frac1a,
\]
\[
S_{\rm red}=b\int dt\,d^3x\,N\sqrt h
\left(K_{ij}K^{ij}-K^2+{}^{(3)}R-2\Lambda\right),\qquad
c_0=2b\Lambda,\quad a=2\kappa,\quad b=\frac1{2\kappa}.
\]

To je Einsteinova–Lambda efektivní akce za uvedených předpokladů. Algebra ponechává nenulovou Newtonovu normalizaci a kosmologický koeficient volné. Nevybírá Holstův koeficient, neodvozuje normalizaci zdroje ani nedokazuje, že tato redukovaná akce pochází z mikroskopického funkcionálu Theta. Kladná energie tenzorů vybírá větev s kladnou normalizací; neurčuje její velikost.

<!-- BILINGUAL-UNIT: spatial-dynamics.modes -->
## Dva tenzorové módy a explicitní dynamické řešení

Pro plochý vakuový srovnávací model položíme kosmologický koeficient rovný nule, zvolíme jednotkový laps pozadí a nulový posun a vyřešíme linearizované vazby a kalibrační podmínky. Pro nenulový prostorový vlnový vektor má příčný bezstopý symetrický podprostor dimenzi **2**. Jeho kvadratický hamiltonián a rovnice jsou

\[
H^{(2)}_{\rm TT}=\int\left[a\,p^{ij}_{\rm TT}p_{ij}^{\rm TT}
+\frac b4\partial_k\gamma^{ij}_{\rm TT}\partial_k\gamma_{ij}^{\rm TT}\right],\quad
\dot\gamma^{\rm TT}_{ij}=2a p^{\rm TT}_{ij},\quad
\dot p^{ij}_{\rm TT}=\frac b2\Delta\gamma^{ij}_{\rm TT},
\]
\[
\ddot\gamma^{\rm TT}_{ij}=ab\Delta\gamma^{\rm TT}_{ij}=\Delta\gamma^{\rm TT}_{ij},\qquad
\gamma^{\rm TT}=\begin{pmatrix}A&B&0\\B&-A&0\\0&0&0\end{pmatrix}\cos(k(z-t)),\qquad
p^{\rm TT}=\dot\gamma^{\rm TT}/(2a).
\]

Obě polarizace mají kladnou kvadratickou energii nenulových módů právě na větvi s kladným kinetickým a křivostním koeficientem. Záporný konformní směr neredukované kinetické formy metriky je odstraněn metrickými vazbami a kalibrační redukcí; není další tenzorovou polarizací. Počet dvanácti metrických fázových souřadnic a čtyř vazeb první třídy dává **2** lokální konfigurační módy. Tento plochý poruchový výsledek nedokazuje nelineární globální kladnost energie ani stabilitu dalších módů Theta, imaginárního času, fyzikální torze či hmoty. Uvedená vlna je linearizovaným řešením této redukované větve, nikoli nově odvozeným mikroskopickým řešením Theta.

<!-- BILINGUAL-UNIT: spatial-dynamics.verification -->
## Ověření a přesná hranice uzavření

`tools/verify_spatial_constraint_closure.py` a `tests/test_spatial_constraint_closure.py` kontrolují tenzorové kontrakce, všech šest kinetických derivací podle hybnosti i metriky u nediagonální racionální metriky, variaci objemu, nezávislé koeficienty závorky, periodickou překážku, Legendreovu inverzi a vlnu se dvěma polarizacemi. Analytický funkcionální důkaz výše dodává kroky integrace po částech a prostorové kovariance.

Nezávislá implementace v NumPy počítá křivost z Christoffelových symbolů pomocí Fourierova derivování ve všech prostorových směrech. Vyhodnocuje Poissonovu závorku centrálními konečnými diferencemi funkcionálu křivosti podél kinetického hamiltonovského toku, bez dosazení analytického vzorce pro variaci křivosti. Deterministická nehomogenní periodická pole používají sítě s **12** a **20** body v každém směru a kroky **0.0002** a **0.0001**, včetně neeinsteinovského koeficientu stopy a nejednotkového součinu koeficientů. Absolutní tolerance přijetí je **0.000002**. Samostatná identita křivosti konformní metriky testuje numerickou implementaci křivosti.

`formal/lean/UBT/Hamiltonian/SpatialClosure.lean` zapisuje **6** konečných algebraických jader: výběr koeficientů, kontrakci stopy, inverzní kinetickou kontrakci, koeficient tenzorové vlny, jeho normalizovanou specializaci a nezápornou energii tenzorů. Stav jejich kompilace a přesné hashe zdrojů zaznamenává `reports/full_spatial_dynamics_2026_10_29.json`. Lokální prostředí Lean není dostupné. Kontinuální funkcionální závorka, redukce na kanonický metrický fázový prostor a úplná dynamika UBT zůstávají nad rámec těchto konečných jader ve stavu LEAN-PENDING.

[Dřívější audit ADM](adm_gr_hessian_constraint_audit.cs.md) předpokládal metrickou algebru; tento výpočet ji odvozuje v explicitní rodině. [Překážka holé akce](physics_closure_bare_action_2026_10.cs.md) není obejita pouhým zápisem tohoto křivostního hamiltoniánu. Dalším nevyřešeným mostem je odvození této redukované symplektické/akční struktury a jejího kladného koeficientu z téže mikroskopické teorie Theta, se zahrnutím všech indukovaných variací tetrády/spojení a všech dalších sektorů. Stav mikroskopické akce zůstává `DEFINED_FAMILY_NOT_FINALIZED`; efektivní závěr GR zůstává `CONDITIONAL`.
