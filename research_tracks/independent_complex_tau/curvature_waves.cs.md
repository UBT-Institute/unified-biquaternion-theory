<!-- BILINGUAL-UNIT: c5-curvature.scope -->
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

# Zakřivení a skutečné tenzorové vlny: podmíněná dynamická větev

Datum: 2026-10-10. Status: **DERIVED_WITH_ASSUMPTIONS / OPEN_GAP**. Toto je pokračování [auditu vln](wave_dynamics.cs.md). Výchozí revize je `d51d5d47428dd228086b5460ddfd2702e9251818`. Návrh nezávislého komplexního tau zůstává nezměněn. Vše níže se týká výslovně určených reálných časoprostorových sektorů; nejde o úplné spektrum na komplexním časoprostoru s nezávislým komplexním tau.

Výsledky jsou dva. Zakřivená homogenní symplektická větev má nadále degenerovanou normálovou kvadratickou akci. Existující split-jet kandidát MacDowell--Mansouri má kladný tenzorový kinetický člen, dvě šířící se tenzorové polarizace a explicitní vlnovou rovnici. Jeho gravitační akce již byla podmíněným kandidátem [U1]; tento zápis počítá její poruchy a jejich split-jet realizaci, aniž by tvrdil nové mikroskopické odvození nebo pozorovatelnou předpověď.

<!-- BILINGUAL-UNIT: c5-curvature.symplectic -->
## Zakřivená symplektická rodina stále neprochází vlnovým testem [L1]

Vezměme existující symplektickou akci [U2] s konvencemi předchozího zápisu o vlnách. Použijme pevnou Lorentzovu konexi, nikoli neurčený funkcionál závislý na poli. Na kontraktibilní reálné oblasti položme

\[
\eta_{ab}=\operatorname{diag}(-1,1,1,1),\qquad
\mathsf H_{ab}=-2\eta_{ab},\qquad
X^a=T(t)\delta^a_0,
\]
\[
\widehat\omega^i{}_0=\widehat\omega^0{}_i=\beta(t)\,dx^i,
\quad \widehat\omega^i{}_j=0,\qquad
P^0=\dot T\,dt,\quad P^i=\beta T\,dx^i,\quad
\dot T\,\beta T\ne0.
\]

Tetráda vzniká z téhož pole, P=DX. Zakřivení je obecně nenulové: jeho boostová složka obsahuje derivaci beta a prostorová rotační složka obsahuje beta na druhou. Tato konexe je určenou jetovou konexí; není bez dalšího ztotožněna s fyzikální Leviho–Civitovou konexí.

Pro neomezené normálové variace původního komplexního pole definujme

\[
\delta\Theta=i b_a\xi^a,\qquad
\alpha=-\mathsf H_{ab}\xi^aP^b
=-2\dot T\xi^0dt+2\beta T\xi^i dx^i.
\]
\[
\delta Q=-\mathsf H_{ab}D\xi^a\wedge P^b
=d\alpha-\frac{\dot\beta}{\beta}dt\wedge\alpha
=\beta\,d(\alpha/\beta).
\]

Člen se zakřivením je zahrnut: kovariantní identita má následující tvar se stejným symplektickým párováním v prostoru hodnot pole jako dříve.

\[
d\alpha=\delta Q+\omega(\delta\Theta,\widehat R\Theta_0).
\]

Pozadí je stacionární, protože jeho Q na Lorentzově reálném řezu mizí. Variace F podle pole vstupují až nad kvadratickým řádem. Jelikož zobrazení normálové poruchy na jednoformu je invertibilní, položme

\[
b=\alpha/\beta,\qquad W=F_0\beta^2,\qquad
S^{(2)}=\frac12\int W\,db\wedge db,\qquad
\boxed{dW\wedge db=0.}
\]

Jde přesně o dříve analyzovaný degenerovaný kvadratický funkcionál s jinou vahou. Je-li W lokálně konstantní, funkcionál je v objemu hraničním členem; kde je dW nenulové, mají jeho lokální řešení níže uvedený tvar a jsou nulovými směry této kvadratické objemové akce.

\[
b=d\chi+f\,dW.
\]

Pro homogenní váhu neobsahuje objemová hustota po integraci per partes časové derivace. Samotné nenulové zakřivení tedy tuto rodinu neopravuje. Nejde o výsledek pro všechny zakřivené konexe, konexe závislé na poli, hraniční módy ani nelineární kalibrační kvocient. Zejména zde variace při pevné konexi nenahrazuje úplnou variaci složené konexe. Hodnostní překážka skalárního ekvivariantního zakřivení v [U3] dává samostatný důvod nezaměňovat skalární symplektickou vazbu za úplnou Palatiniho bivektorovou vazbu.

<!-- BILINGUAL-UNIT: c5-curvature.candidate -->
## Použití existujícího kandidáta se zakřivením včetně řetězového pravidla [L1]

Již zapsaný kandidát [U1, U4] používá složenou tetrádu

\[
E^a=\frac1{\sqrt{N_0}}
\left[dX^a+\omega^a{}_bX^b+K_J{}^a{}_bX^b+wX^a\right],
\qquad X^2\ne0.
\]

Fyzikální Lorentzova konexe omega, jetová korekce a centrální forma se zde variují nezávisle jako v uvedeném kandidátu. Akce kvadratická v Cliffordově zakřivení má již známý přesný rozklad

\[
S_{\rm cand}=S_{\rm HP}[E,\omega;\kappa,\Lambda]
-\frac{\varepsilon_\psi\ell^2}{8\kappa}
\int\epsilon_{abcd}R^{ab}\wedge R^{cd},
\]
\[
\kappa=\frac{g_G^2\ell^2}{2},\qquad
\Lambda=\frac{3\varepsilon_\psi}{\ell^2},\qquad
g_G^2>0,\quad \ell>0.
\]

Při variacích s kompaktním nosičem a pevné topologii Eulerův člen nepřispívá k objemovému hessiánu. Bodová surjektivita jetových variací dává úplnou Palatiniho tetrádovou rovnici; zbývající rovnice fyzikální konexe je Cartanova rovnice. Jejím nedegenerovaným řešením bez spinu je Leviho–Civitova konexe. To využívá oba výskyty omega, v zakřivení i v E.

Explicitněji nechť Phi zobrazuje proměnné kandidáta na Palatiniho proměnné. Na stacionárním Palatiniho pozadí dává řetězové pravidlo

\[
\delta^2(S_{\rm HP}\circ\Phi)
=D\Phi^*\,\delta^2S_{\rm HP}\,D\Phi
+\delta S_{\rm HP}[D^2\Phi]
=D\Phi^*\,\delta^2S_{\rm HP}\,D\Phi.
\]

Poslední člen mizí díky rovnicím pozadí, nikoli držením složené tetrády pevně. Vyřešením linearizované Cartanovy rovnice a gravitačních vazeb dostaneme tenzorovou akci níže. Zápis pomocí kvadrátu zakřivení tedy v tomto kandidátu nezavádí další objemový tenzorový mód čtvrtého řádu. Tento závěr závisí na jeho konkrétním rozkladu na Eulerův a Palatiniho člen; nejde o tvrzení pro libovolné akce kvadratické v zakřivení.

<!-- BILINGUAL-UNIT: c5-curvature.tensor -->
## Tenzorový hessián na skutečném vakuovém pozadí [L1]

Zvolme kladné kosmologické znaménko a rozpínající se prostorově plochou de Sitterovu oblast. Konečná hodnota ell pro tuto větev nepřipouští ploché Minkowského vakuum. Použijme jednotky s rychlostí světla rovnou jedné, vlastní kosmický čas t a bezrozměrný škálový faktor a:

\[
\varepsilon_\psi=+1,\qquad
H=\frac1\ell,\qquad a(t)=e^{Ht},\qquad
ds^2=-dt^2+a^2(t)(e^h)_{ij}\,dx^i dx^j,
\quad h_{ii}=0,\quad \partial_i h_{ij}=0.
\]

Pozadí splňuje vakuovou Friedmannovu rovnici. Tenzorové poruchy splňují lineární vazby lapse a shiftu s nulovými poruchami těchto veličin v tenzorovém sektoru. Exponenciální parametrizace zachovává prostorový objem. Z ADM tvaru Einsteinovy akce dostaneme až na prostorové hraniční členy

\[
K^i{}_j=H\delta^i_j+\tfrac12\dot h^i{}_j+O(h^2),\qquad
\left[K^i{}_jK^j{}_i-K^2\right]_{h^2}
=\tfrac14\dot h_{ij}\dot h_{ij},
\]
\[
\left[\sqrt\gamma\,{}^{(3)}R\right]_{h^2}
=-\frac a4\partial_kh_{ij}\partial_kh_{ij}.
\]
\[
\boxed{S_T^{(2)}=\frac1{8\kappa}\int dt\,d^3x\,a^3
\left[\dot h_{ij}\dot h_{ij}
-\frac1{a^2}\partial_kh_{ij}\partial_kh_{ij}\right].}
\]

Ověřovací skript znovu vypočítává prostorové Christoffelovy symboly, Ricciho skalár a kontrakci vnější křivosti do kvadratického řádu pro obě polarizace s libovolným Fourierovým směrem otočeným do osy z. Rotační invariance a Fourierův rozklad dávají obecný kvadratický tenzorový výraz. Tím je uvnitř určeného výzkumného kandidáta UBT reprodukován standardní tenzorový výsledek GR, například [S1, rovnice (2.27)].

Při polarizačních tenzorech s druhou mocninou normy rovnou dvěma splňují dvě nezávislé amplitudy

\[
h_{xx}=h_+,\quad h_{yy}=-h_+,\quad h_{xy}=h_{yx}=h_\times,
\qquad h_{iz}=0,
\]
\[
\boxed{\ddot h_\lambda+3H\dot h_\lambda
-a^{-2}\nabla^2h_\lambda=0,\qquad \lambda\in\{+,\times\}.}
\]

Pro nenulovou prostorovou hybnost má symetrický prostorový tenzor šest složek a čtyři nezávislé vazby transverzality a stopy, takže zbývají dvě. Hlavní polynom při zmrazených koeficientech je níže uvedený Lorentzův světelný kužel. Popisuje lokální šíření, nikoli přesný globální mód s konstantní frekvencí v rozpínajícím se časoprostoru.

\[
-\omega_{\rm freq}^2+|\mathbf k|^2/a^2=0,
\qquad c_T^2=1.
\]

<!-- BILINGUAL-UNIT: c5-curvature.energy -->
## Kinetické znaménko, energie a kosmologické zeslabování [L1]

Pro každou nezávislou reálnou polarizační amplitudu jsou hybnost a hustota hamiltoniánu

\[
\pi_\lambda=\frac{a^3}{2\kappa}\dot h_\lambda,\qquad
\mathcal H_T=\sum_\lambda\frac{a^3}{4\kappa}
\left[\dot h_\lambda^2+a^{-2}|\nabla h_\lambda|^2\right]\geq0.
\]

Tento redukovaný klasický tenzorový sektor má tedy pro uvedenou kladnou vazbu kandidáta kladnou kinetickou a gradientovou energii. Hamiltonián výslovně závisí na čase; nerovnost není tvrzením o zachované globální energii ani důkazem stability všech komplexních módů UBT.

Pro rozlišení kosmologického zeslabování od vloženého mechanismu tlumení zaveďme konformní čas a kanonickou tenzorovou proměnnou:

\[
d\eta=dt/a,\qquad v_\lambda=\frac{a h_\lambda}{\sqrt{2\kappa}},\qquad
v_\lambda''+\left(k^2-\frac{a''}{a}\right)v_\lambda=0.
\]
\[
a=-\frac\ell\eta,\quad \eta<0,\quad \frac{a''}{a}=\frac2{\eta^2},\qquad
h_{\lambda,k}=C_\lambda(\eta-i/k)e^{-ik\eta}
+D_\lambda(\eta+i/k)e^{ik\eta},\quad k>0.
\]

Konstanty jsou počáteční data. Pro vlnové délky mnohem kratší než škála zakřivení se oscilující amplituda mění jako převrácená hodnota a; mimo tento režim se přesné řešení v pozdním čase blíží konečné konstantě. Zdánlivě záporný člen s druhou derivací a v kanonické proměnné není zápornou kinetickou normou. Zeslabování pochází z rozpínání, nikoli z disipace nebo odstraňování vyšších fraktálních úrovní. Nezískáváme Planckův cutoff, pravidlo kvantování energie, hodnotu alfa ani nezávisle vybranou délku. Na tuto tenzorovou akci lze dodatečně uplatnit kanonické kvantování, ale odvození jeho kvantových postulátů z UBT je samostatný úkol.

<!-- BILINGUAL-UNIT: c5-curvature.location -->
## Kde sídlí šířící se mód

Explicitní zdvih ukazuje omezení architektury. Zvolme na oblasti nenulové konstantní Lorentzovo reálné pole a položme

\[
X^a=\nu\delta^a_0,\quad \nu\ne0,\qquad
w=\frac{\sqrt{N_0}}\nu E^0,\qquad
K_J{}^i{}_0=K_J{}^0{}_i
=\frac{\sqrt{N_0}}\nu E^i-\omega^i{}_0.
\]

Po snížení prvního indexu jsou tyto složky lorentzovsky antisymetrické. Nevyužité prostorové rotační složky lze položit rovny nule. Generovaná tetráda je přesně E. Tenzorovou poruchu tedy lze zdvihnout s

\[
\delta X=0,\qquad \delta w=0,\qquad
\delta E^i=\frac a2h_{ij}dx^j,\qquad
\delta K_J{}^i{}_0
=\frac{\sqrt{N_0}}\nu\delta E^i-\delta\omega^i{}_0.
\]

Tenzorová vlna proto sídlí ve složené geometrii kódované jetovými a konexními proměnnými; tento výpočet není nenulovým propagátorem samotného Theta. Proměnná vystupující bez derivací v lagrangiánu prvního řádu nemusí po eliminaci jiné proměnné zmizet z fyzikálních šířících se kombinací. Zde eliminace fyzikální konexe dodává derivace tetrády. Označení všech jetových proměnných za algebraické nestačí k odvození akce pouze pro Theta. Další sektory mohou tento zdvih omezit, ale ve zvoleném vakuovém kandidátu nejsou zahrnuty.

<!-- BILINGUAL-UNIT: c5-curvature.observations -->
## Podmíněné srovnání s pozorováním

Vypočtený tenzorový sektor přebírá zákon šíření z GR. Srovnání jeho metrického světelného kužele s pozorovanou rychlostí světla navíc předpokládá, že se fotony vážou na stejnou fyzikální metriku; tato vazba hmoty zde nebyla odvozena. Za tohoto předpokladu leží hodnota c_T=c uvnitř meze z GW170817/GRB 170817A [S2], která závisí na předpokladech o emisi zdroje v dané analýze:

\[
-3\times10^{-15}\lesssim\frac{c_T-c}{c}\lesssim7\times10^{-16}.
\]

Dvě tenzorové polarizace jsou slučitelné s absencí silné evidence dalších polarizací v testech GWTC-5.0 [S3]. To nevylučuje každý slabě vázaný dodatečný mód UBT. Standardní expanzní člen 3H nedodává další parametr disipace. Nebyla vyhodnocena věrohodnost vlnových průběhů, vypočten vznik vln ve zdroji ani proveden fit amplitud nebo historie expanze. Samotné čisté de Sitterovo vakuum nepopisuje éru hmoty a záření.

Pouze pro referenční kalibraci použijme hodnoty Planck 2018 pro plochý základní model LambdaCDM [S4] se zanedbáním dnešního příspěvku záření. Po obnovení c dostaneme

\[
H_0=67.4\,\mathrm{km\,s^{-1}\,Mpc^{-1}},\qquad
\Omega_m=0.315,\quad \Omega_\Lambda\simeq0.685,
\]
\[
\Lambda=\frac{3H_0^2\Omega_\Lambda}{c^2}
\simeq1.09\times10^{-52}\,\mathrm{m^{-2}},\qquad
\ell=\sqrt{\frac3\Lambda}
=\frac{c}{H_0\sqrt{\Omega_\Lambda}}
\simeq1.66\times10^{26}\,\mathrm m\simeq5.37\,\mathrm{Gpc}.
\]

Ell je zde kosmologická délka zakřivení, nikoli identifikovaná Planckova mez. Tyto vstupy kalibrují volný parametr kandidáta; nejde o předpověď UBT ani nový kosmologický fit. Slučitelnost převzatá z tohoto sektoru GR neprokazuje soulad celé teorie komplexního časoprostoru s nezávislým tau s pozorováním.

<!-- BILINGUAL-UNIT: c5-curvature.verification -->
## Ověření a zbývající dynamické rozhodnutí

`verify_curvature_waves.py` kontroluje zakřivené normálové zobrazení včetně členu se zakřivením, ADM tenzorové koeficienty, hodnost vazeb, Eulerovu rovnici, hamiltonián, přesný de Sitterův mód a split-jet zdvih s konstantním polem. Samostatná implementace pomocí Python Fraction kontroluje konečné identity zakřiveného zobrazení a tenzorového zdvihu. `curvature_waves_results.json` zaznamenává počet kontrol a jejich omezení. Analytické argumenty se týkají lokálních variací s kompaktním nosičem; konečné kontroly neformalizují úplný kvocient vazeb.

**LEAN-PENDING:** nejsou dodány spustitelné Lean/Lake ani ověřená formalizace těchto geometrických a variačních argumentů. Zdrojem překladu je angličtina; lidská kontrola významové ekvivalence není doložena.

Užitečným kladným výsledkem je konkrétní šířící se tenzorový sektor existujícího kandidáta. Následujícím mikroskopickým požadavkem je odvodit jeho rozšířenou konexi, gradování a obsah proměnných i vazeb, nebo odvodit jinou akci s vlastním fyzikálním hessiánem. Konexní proměnné zejména nelze pouze přejmenovat na derivace Theta bez dodání a variování takového funkcionálu. Úplné komplexní pole, dynamika nezávislého tau, předpis reality, hmotový/Diracův sektor a výběr parametrů zůstávají otevřené. Kanonická akce a statusy tvrzení se nemění.

<!-- BILINGUAL-UNIT: c5-curvature.sources -->
## Zdroje

- [U1] [Existující kandidát se zakřivením a jedním Theta](../action_selection/single_theta_macdowell_mansouri_candidate.cs.md).
- [U2] [Existující audit symplektického Lorentzova řezu](../action_selection/multisymplectic_lorentz_slice_audit.cs.md).
- [U3] [Hodnostní hranice skalárního ekvivariantního zakřivení](../action_selection/equivariant_symplectic_curvature_rank_no_go.cs.md).
- [U4] [Variační split-jet zdvih Palatiniho akce](../action_selection/split_jet_palatii_variational_lift.cs.md).
- [S1] J. Maldacena, [Non-Gaussian features of primordial fluctuations in single field inflationary models](https://arxiv.org/abs/astro-ph/0210603), rovnice (2.27).
- [S2] LIGO/Virgo a partnerské kolaborace, [Gravitational Waves and Gamma-rays from a Binary Neutron Star Merger: GW170817 and GRB 170817A](https://dcc.ligo.org/P1700308/public), 2017.
- [S3] LIGO/Virgo/KAGRA, [GWTC-5.0: Tests of General Relativity](https://arxiv.org/abs/2607.19293), 2026.
- [S4] Kolaborace Planck, [Planck 2018 results. VI. Cosmological parameters](https://arxiv.org/abs/1807.06209), 2020, revize 2021.
